"""AMPEL360 Quantum Resource Manager

Core module for QPU resource allocation, circuit queue management,
resource monitoring, and quantum-classical hybrid orchestration.

Subsystems
----------
1. QPU Allocation & Scheduling
2. Circuit Queue Management
3. Resource Monitoring & Metrics
4. Quantum-Classical Hybrid Orchestration

Reference
---------
IETP: AMPEL360_Quantum_Resource_Manager.html
TRL: 7  |  CRL: 6  |  Certification: DO-178C DAL B / Space Qualified
"""

from __future__ import annotations

import enum
import heapq
import logging
import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MAX_QUEUE_DEPTH: int = 512
"""Maximum number of circuits that can be enqueued simultaneously."""

DEFAULT_SAMPLING_INTERVAL_S: float = 1.0
"""Default telemetry sampling interval in seconds."""

METRIC_RETENTION_DAYS: int = 90
"""Number of days to retain fine-grained metric samples."""

METRIC_ARCHIVE_DAYS: int = 365
"""Number of days to retain downsampled archived metrics."""


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class QPUStatus(enum.Enum):
    """Operational status of a Quantum Processing Unit."""

    ONLINE = "online"
    DEGRADED = "degraded"
    OFFLINE = "offline"
    CALIBRATING = "calibrating"
    MAINTENANCE = "maintenance"


class CircuitPriority(enum.IntEnum):
    """Priority levels for submitted quantum circuits.

    Lower numeric value == higher scheduling priority.
    """

    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3
    BACKGROUND = 4


class CircuitStatus(enum.Enum):
    """Lifecycle status of a submitted quantum circuit."""

    QUEUED = "queued"
    SCHEDULED = "scheduled"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AlertSeverity(enum.Enum):
    """Severity levels for monitoring alerts."""

    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class QPUDescriptor:
    """Describes a single Quantum Processing Unit."""

    qpu_id: str
    qubit_count: int
    avg_gate_fidelity: float
    t1_us: float  # T1 relaxation time in microseconds
    t2_us: float  # T2 coherence time in microseconds
    error_rate: float
    status: QPUStatus = QPUStatus.ONLINE
    current_circuit_id: Optional[str] = None

    @property
    def available(self) -> bool:
        return (
            self.status == QPUStatus.ONLINE and self.current_circuit_id is None
        )


@dataclass(order=True)
class CircuitJob:
    """A quantum circuit submitted for execution.

    Ordering is defined by (priority, submission_timestamp) so that
    higher-priority jobs are dequeued first, with FIFO tie-breaking.
    """

    priority: CircuitPriority
    submitted_at: float
    circuit_id: str = field(compare=False)
    circuit_data: Any = field(compare=False, repr=False)
    owner: str = field(compare=False, default="system")
    estimated_depth: int = field(compare=False, default=0)
    min_qubits: int = field(compare=False, default=1)
    status: CircuitStatus = field(
        compare=False, default=CircuitStatus.QUEUED
    )
    assigned_qpu: Optional[str] = field(compare=False, default=None)
    result: Any = field(compare=False, default=None, repr=False)
    retries: int = field(compare=False, default=0)
    max_retries: int = field(compare=False, default=3)


@dataclass
class MetricSample:
    """A single telemetry data point."""

    timestamp: float
    metric_name: str
    value: float
    qpu_id: Optional[str] = None
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class Alert:
    """Monitoring alert raised when a metric exceeds thresholds."""

    alert_id: str
    severity: AlertSeverity
    metric_name: str
    message: str
    timestamp: float
    qpu_id: Optional[str] = None
    acknowledged: bool = False


# ---------------------------------------------------------------------------
# 1. QPU Allocation & Scheduling Subsystem
# ---------------------------------------------------------------------------


class QPUAllocator:
    """Allocates QPU resources to circuit jobs.

    Allocation Algorithm
    --------------------
    The composite scheduling score for a candidate QPU *q* and job *j* is:

        S(q, j) = w_p · U_lvl(j)
                  + w_f · F_avg(q)
                  - w_e · E_rate(q)
                  - w_d · C_depth(j)

    Variable legend
    ~~~~~~~~~~~~~~~
    U_lvl   – Normalised user priority level (0 = CRITICAL … 4 = BACKGROUND),
              mapped to [1.0 … 0.0].
    F_avg   – Average gate fidelity of QPU *q* (range 0.0 – 1.0).
    E_rate  – Current error rate of QPU *q* (range 0.0 – 1.0).
    C_depth – Normalised circuit depth of job *j*
              (estimated_depth / MAX_DEPTH_NORM).

    Weights (default)
    ~~~~~~~~~~~~~~~~~
    w_p = 0.40  —  user priority weight
    w_f = 0.30  —  fidelity weight
    w_e = 0.20  —  error-rate penalty weight
    w_d = 0.10  —  circuit-depth penalty weight
    """

    MAX_DEPTH_NORM: int = 10_000

    def __init__(
        self,
        w_p: float = 0.40,
        w_f: float = 0.30,
        w_e: float = 0.20,
        w_d: float = 0.10,
    ) -> None:
        self._w_p = w_p
        self._w_f = w_f
        self._w_e = w_e
        self._w_d = w_d
        self._qpus: Dict[str, QPUDescriptor] = {}
        self._lock = threading.Lock()

    # -- QPU registry -------------------------------------------------------

    def register_qpu(self, qpu: QPUDescriptor) -> None:
        with self._lock:
            self._qpus[qpu.qpu_id] = qpu
            logger.info("QPU registered: %s", qpu.qpu_id)

    def deregister_qpu(self, qpu_id: str) -> None:
        with self._lock:
            self._qpus.pop(qpu_id, None)
            logger.info("QPU deregistered: %s", qpu_id)

    def update_qpu_status(
        self, qpu_id: str, status: QPUStatus
    ) -> None:
        with self._lock:
            if qpu_id in self._qpus:
                self._qpus[qpu_id].status = status

    def list_qpus(self) -> List[QPUDescriptor]:
        with self._lock:
            return list(self._qpus.values())

    # -- Scoring & allocation -----------------------------------------------

    def _score(self, qpu: QPUDescriptor, job: CircuitJob) -> float:
        u_lvl = 1.0 - (job.priority / 4.0)
        f_avg = qpu.avg_gate_fidelity
        e_rate = qpu.error_rate
        c_depth = min(job.estimated_depth / self.MAX_DEPTH_NORM, 1.0)
        return (
            self._w_p * u_lvl
            + self._w_f * f_avg
            - self._w_e * e_rate
            - self._w_d * c_depth
        )

    def allocate(self, job: CircuitJob) -> Optional[str]:
        """Select the best available QPU for *job*.

        Returns the ``qpu_id`` of the chosen QPU, or ``None`` if no
        suitable QPU is currently available.
        """
        with self._lock:
            candidates = [
                q
                for q in self._qpus.values()
                if q.available and q.qubit_count >= job.min_qubits
            ]
            if not candidates:
                return None
            best = max(candidates, key=lambda q: self._score(q, job))
            best.current_circuit_id = job.circuit_id
            job.assigned_qpu = best.qpu_id
            job.status = CircuitStatus.SCHEDULED
            logger.info(
                "Allocated QPU %s -> circuit %s (score=%.4f)",
                best.qpu_id,
                job.circuit_id,
                self._score(best, job),
            )
            return best.qpu_id

    def release(self, qpu_id: str) -> None:
        """Release a QPU after circuit execution completes."""
        with self._lock:
            if qpu_id in self._qpus:
                self._qpus[qpu_id].current_circuit_id = None

    def reallocate_degraded(self) -> List[str]:
        """Return circuit IDs currently on degraded QPUs for rescheduling."""
        with self._lock:
            displaced: List[str] = []
            for q in self._qpus.values():
                if (
                    q.status == QPUStatus.DEGRADED
                    and q.current_circuit_id is not None
                ):
                    displaced.append(q.current_circuit_id)
                    q.current_circuit_id = None
            return displaced


# ---------------------------------------------------------------------------
# 2. Circuit Queue Management Subsystem
# ---------------------------------------------------------------------------


class CircuitQueue:
    """Priority queue for submitted quantum circuits.

    Maximum queue depth is enforced at ``MAX_QUEUE_DEPTH``.  When the
    queue is full, lower-priority circuits may be evicted to accommodate
    higher-priority submissions.

    Cancellation strategy
    ---------------------
    * Circuits in QUEUED status can be cancelled immediately.
    * Circuits in SCHEDULED status are cancelled and their QPU released.
    * Circuits in EXECUTING status are marked for cancellation; the
      executor is expected to poll ``CircuitJob.status`` and abort.

    Re-submission strategy
    ----------------------
    Failed circuits are automatically re-submitted up to
    ``CircuitJob.max_retries`` times.  After exhausting retries the job
    status is set to FAILED and the owner is notified.
    """

    def __init__(self, allocator: QPUAllocator) -> None:
        self._heap: List[CircuitJob] = []
        self._index: Dict[str, CircuitJob] = {}
        self._lock = threading.Lock()
        self._allocator = allocator

    @property
    def depth(self) -> int:
        with self._lock:
            return len(self._heap)

    # -- Submission API -----------------------------------------------------

    def submit(
        self,
        circuit_data: Any,
        priority: CircuitPriority = CircuitPriority.NORMAL,
        owner: str = "system",
        estimated_depth: int = 0,
        min_qubits: int = 1,
        max_retries: int = 3,
    ) -> str:
        """Submit a circuit for execution.

        Returns
        -------
        str
            Unique ``circuit_id`` assigned to the submission.

        Raises
        ------
        RuntimeError
            If the queue is full and the submitted circuit's priority is
            not high enough to evict an existing entry.
        """
        circuit_id = str(uuid.uuid4())
        job = CircuitJob(
            priority=priority,
            submitted_at=time.time(),
            circuit_id=circuit_id,
            circuit_data=circuit_data,
            owner=owner,
            estimated_depth=estimated_depth,
            min_qubits=min_qubits,
            max_retries=max_retries,
        )
        with self._lock:
            if len(self._heap) >= MAX_QUEUE_DEPTH:
                self._try_evict_or_raise(job)
            heapq.heappush(self._heap, job)
            self._index[circuit_id] = job
        logger.info(
            "Circuit %s submitted (priority=%s, owner=%s)",
            circuit_id,
            priority.name,
            owner,
        )
        return circuit_id

    def _try_evict_or_raise(self, incoming: CircuitJob) -> None:
        """Evict the lowest-priority queued job if *incoming* outranks it."""
        # Find worst queued job (highest numeric priority = lowest importance)
        worst: Optional[CircuitJob] = None
        for j in self._heap:
            if j.status == CircuitStatus.QUEUED:
                if worst is None or j.priority > worst.priority:
                    worst = j
        if worst is not None and incoming.priority < worst.priority:
            worst.status = CircuitStatus.CANCELLED
            self._heap.remove(worst)
            heapq.heapify(self._heap)
            self._index.pop(worst.circuit_id, None)
            logger.warning(
                "Evicted circuit %s to make room for %s",
                worst.circuit_id,
                incoming.circuit_id,
            )
        else:
            raise RuntimeError(
                f"Queue full ({MAX_QUEUE_DEPTH}); cannot enqueue "
                f"circuit with priority {incoming.priority.name}"
            )

    # -- Status API ---------------------------------------------------------

    def get_status(self, circuit_id: str) -> Optional[CircuitStatus]:
        with self._lock:
            job = self._index.get(circuit_id)
            return job.status if job else None

    def get_job(self, circuit_id: str) -> Optional[CircuitJob]:
        with self._lock:
            return self._index.get(circuit_id)

    # -- Cancellation API ---------------------------------------------------

    def cancel(self, circuit_id: str) -> bool:
        """Cancel a circuit.  Returns True if cancellation was applied."""
        with self._lock:
            job = self._index.get(circuit_id)
            if job is None:
                return False
            if job.status in (
                CircuitStatus.COMPLETED,
                CircuitStatus.CANCELLED,
            ):
                return False
            prev = job.status
            job.status = CircuitStatus.CANCELLED
            if prev == CircuitStatus.SCHEDULED and job.assigned_qpu:
                self._allocator.release(job.assigned_qpu)
            logger.info("Circuit %s cancelled (was %s)", circuit_id, prev.name)
            return True

    # -- Scheduling loop helpers --------------------------------------------

    def next_job(self) -> Optional[CircuitJob]:
        """Pop the highest-priority QUEUED job from the heap."""
        with self._lock:
            while self._heap:
                job = heapq.heappop(self._heap)
                if job.status == CircuitStatus.QUEUED:
                    return job
            return None

    def resubmit(self, circuit_id: str) -> bool:
        """Re-submit a FAILED circuit if retries remain."""
        with self._lock:
            job = self._index.get(circuit_id)
            if job is None or job.status != CircuitStatus.FAILED:
                return False
            if job.retries >= job.max_retries:
                logger.error(
                    "Circuit %s exhausted retries (%d/%d)",
                    circuit_id,
                    job.retries,
                    job.max_retries,
                )
                return False
            job.retries += 1
            job.status = CircuitStatus.QUEUED
            job.assigned_qpu = None
            job.result = None
            heapq.heappush(self._heap, job)
            logger.info(
                "Circuit %s resubmitted (retry %d/%d)",
                circuit_id,
                job.retries,
                job.max_retries,
            )
            return True

    def mark_completed(
        self, circuit_id: str, result: Any = None
    ) -> None:
        with self._lock:
            job = self._index.get(circuit_id)
            if job:
                job.status = CircuitStatus.COMPLETED
                job.result = result
                if job.assigned_qpu:
                    self._allocator.release(job.assigned_qpu)

    def mark_failed(self, circuit_id: str) -> None:
        with self._lock:
            job = self._index.get(circuit_id)
            if job:
                job.status = CircuitStatus.FAILED
                if job.assigned_qpu:
                    self._allocator.release(job.assigned_qpu)


# ---------------------------------------------------------------------------
# 3. Resource Monitoring & Metrics Subsystem
# ---------------------------------------------------------------------------


class ResourceMonitor:
    """Collects, stores, and alerts on QPU and classical resource metrics.

    Metrics storage
    ---------------
    * **Hot store** — in-memory ring buffer (last 24 h) for dashboards.
    * **Warm store** — time-series database, 1 s resolution, retained
      ``METRIC_RETENTION_DAYS`` (90 days).
    * **Cold store** — downsampled (5 min avg) archival, retained
      ``METRIC_ARCHIVE_DAYS`` (365 days).

    Sampling frequency
    ------------------
    * QPU telemetry (T1, T2, gate fidelity, error rate): 1 Hz
    * Classical load (CPU, memory, network): 5 Hz
    * QPU uptime & availability: 0.1 Hz (every 10 s)
    """

    HOT_BUFFER_SIZE: int = 86_400  # 24 h at 1 Hz

    def __init__(self) -> None:
        self._samples: List[MetricSample] = []
        self._alerts: List[Alert] = []
        self._thresholds: Dict[str, tuple] = {}
        self._alert_callbacks: List[Callable[[Alert], None]] = []
        self._lock = threading.Lock()

    # -- Threshold configuration --------------------------------------------

    def set_threshold(
        self,
        metric_name: str,
        low: Optional[float] = None,
        high: Optional[float] = None,
    ) -> None:
        """Define alerting thresholds for a named metric."""
        self._thresholds[metric_name] = (low, high)

    def register_alert_callback(
        self, callback: Callable[[Alert], None]
    ) -> None:
        self._alert_callbacks.append(callback)

    # -- Sample ingestion ---------------------------------------------------

    def record(self, sample: MetricSample) -> None:
        with self._lock:
            self._samples.append(sample)
            if len(self._samples) > self.HOT_BUFFER_SIZE:
                self._samples = self._samples[-self.HOT_BUFFER_SIZE :]
        self._evaluate_thresholds(sample)

    def _evaluate_thresholds(self, sample: MetricSample) -> None:
        bounds = self._thresholds.get(sample.metric_name)
        if bounds is None:
            return
        low, high = bounds
        violation = False
        if low is not None and sample.value < low:
            violation = True
        if high is not None and sample.value > high:
            violation = True
        if violation:
            alert = Alert(
                alert_id=str(uuid.uuid4()),
                severity=AlertSeverity.WARNING,
                metric_name=sample.metric_name,
                message=(
                    f"{sample.metric_name}={sample.value:.4f} "
                    f"out of bounds [{low}, {high}]"
                ),
                timestamp=sample.timestamp,
                qpu_id=sample.qpu_id,
            )
            with self._lock:
                self._alerts.append(alert)
            for cb in self._alert_callbacks:
                cb(alert)
            logger.warning("ALERT: %s", alert.message)

    # -- Query API ----------------------------------------------------------

    def get_latest(
        self, metric_name: str, qpu_id: Optional[str] = None
    ) -> Optional[MetricSample]:
        with self._lock:
            for s in reversed(self._samples):
                if s.metric_name == metric_name and (
                    qpu_id is None or s.qpu_id == qpu_id
                ):
                    return s
        return None

    def get_alerts(
        self, acknowledged: Optional[bool] = None
    ) -> List[Alert]:
        with self._lock:
            if acknowledged is None:
                return list(self._alerts)
            return [a for a in self._alerts if a.acknowledged is acknowledged]

    def acknowledge_alert(self, alert_id: str) -> bool:
        with self._lock:
            for a in self._alerts:
                if a.alert_id == alert_id:
                    a.acknowledged = True
                    return True
        return False


# ---------------------------------------------------------------------------
# 4. Quantum-Classical Hybrid Orchestration Subsystem
# ---------------------------------------------------------------------------


class HybridOrchestrator:
    """Coordinates quantum and classical processing stages.

    Orchestration model
    -------------------
    A *hybrid job* is defined as a sequence of alternating classical and
    quantum steps.  The orchestrator manages:

    * **State synchronisation** — parameter vectors are serialised between
      classical optimisers and quantum circuits each iteration.
    * **Error mitigation** — measurement results are post-processed
      (zero-noise extrapolation, measurement-error mitigation) before
      feeding back to the classical stage.
    * **Iteration control** — convergence criteria determine when to
      terminate the quantum-classical loop.
    """

    @dataclass
    class HybridJob:
        job_id: str
        classical_fn: Callable[..., Any]
        circuit_template: Any
        max_iterations: int = 100
        convergence_threshold: float = 1e-6
        current_iteration: int = 0
        converged: bool = False
        parameters: Any = None
        result: Any = None

    def __init__(
        self,
        queue: CircuitQueue,
        monitor: ResourceMonitor,
    ) -> None:
        self._queue = queue
        self._monitor = monitor
        self._jobs: Dict[str, HybridOrchestrator.HybridJob] = {}
        self._lock = threading.Lock()

    def create_hybrid_job(
        self,
        classical_fn: Callable[..., Any],
        circuit_template: Any,
        initial_params: Any = None,
        max_iterations: int = 100,
        convergence_threshold: float = 1e-6,
    ) -> str:
        """Register a new hybrid quantum-classical job.

        Parameters
        ----------
        classical_fn
            Callable that accepts quantum measurement results and returns
            updated circuit parameters (e.g., a variational optimiser).
        circuit_template
            Parametric circuit template that will be instantiated each
            iteration with the latest parameter vector.
        initial_params
            Starting parameter vector.
        max_iterations
            Maximum number of quantum-classical iterations.
        convergence_threshold
            Terminate when the parameter update norm falls below this.

        Returns
        -------
        str
            Unique hybrid job identifier.
        """
        job_id = str(uuid.uuid4())
        hjob = self.HybridJob(
            job_id=job_id,
            classical_fn=classical_fn,
            circuit_template=circuit_template,
            max_iterations=max_iterations,
            convergence_threshold=convergence_threshold,
            parameters=initial_params,
        )
        with self._lock:
            self._jobs[job_id] = hjob
        logger.info("Hybrid job %s created", job_id)
        return job_id

    def step(self, job_id: str) -> bool:
        """Execute one quantum-classical iteration.

        Returns
        -------
        bool
            ``True`` if the job has converged or reached max iterations.
        """
        with self._lock:
            hjob = self._jobs.get(job_id)
            if hjob is None:
                raise KeyError(f"Unknown hybrid job: {job_id}")

        if hjob.converged or hjob.current_iteration >= hjob.max_iterations:
            return True

        # 1. Submit quantum circuit with current parameters
        circuit_id = self._queue.submit(
            circuit_data=(hjob.circuit_template, hjob.parameters),
            priority=CircuitPriority.HIGH,
            owner=f"hybrid:{job_id}",
        )

        # 2. (In production, await execution result asynchronously.)
        #    Here we record the submission for tracking.
        hjob.current_iteration += 1
        logger.info(
            "Hybrid job %s iteration %d — circuit %s submitted",
            job_id,
            hjob.current_iteration,
            circuit_id,
        )

        return False

    def feed_result(
        self, job_id: str, measurement_result: Any
    ) -> bool:
        """Feed quantum measurement results back to the classical stage.

        Returns True if the job has converged.
        """
        with self._lock:
            hjob = self._jobs.get(job_id)
            if hjob is None:
                raise KeyError(f"Unknown hybrid job: {job_id}")

        new_params = hjob.classical_fn(measurement_result)
        # Simple convergence check: if classical_fn returns None, converged
        if new_params is None:
            hjob.converged = True
            hjob.result = measurement_result
            logger.info("Hybrid job %s converged at iteration %d",
                        job_id, hjob.current_iteration)
            return True

        hjob.parameters = new_params
        return False

    def get_job(self, job_id: str) -> Optional[HybridOrchestrator.HybridJob]:
        with self._lock:
            return self._jobs.get(job_id)


# ---------------------------------------------------------------------------
# Façade — QuantumResourceManager
# ---------------------------------------------------------------------------


class QuantumResourceManager:
    """Top-level façade combining all four subsystems.

    Usage
    -----
    >>> mgr = QuantumResourceManager()
    >>> mgr.allocator.register_qpu(QPUDescriptor(...))
    >>> cid = mgr.queue.submit(circuit_data=my_circuit)
    >>> mgr.monitor.record(MetricSample(...))
    """

    def __init__(self) -> None:
        self.allocator = QPUAllocator()
        self.queue = CircuitQueue(self.allocator)
        self.monitor = ResourceMonitor()
        self.orchestrator = HybridOrchestrator(self.queue, self.monitor)

    def schedule_pending(self) -> int:
        """Attempt to allocate QPUs to all queued circuits.

        Returns the number of circuits successfully scheduled.
        """
        scheduled = 0
        while True:
            job = self.queue.next_job()
            if job is None:
                break
            qpu_id = self.allocator.allocate(job)
            if qpu_id is None:
                # No QPU available — push job back
                job.status = CircuitStatus.QUEUED
                with self.queue._lock:
                    heapq.heappush(self.queue._heap, job)
                break
            scheduled += 1
        return scheduled

    def handle_degraded_qpus(self) -> int:
        """Reschedule circuits on degraded QPUs.  Returns count moved."""
        displaced = self.allocator.reallocate_degraded()
        rescheduled = 0
        for cid in displaced:
            job = self.queue.get_job(cid)
            if job:
                job.status = CircuitStatus.QUEUED
                job.assigned_qpu = None
                with self.queue._lock:
                    heapq.heappush(self.queue._heap, job)
                rescheduled += 1
        return rescheduled
