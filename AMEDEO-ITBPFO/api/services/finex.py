"""FinexService — Final Execution engine.

Manages the full pipeline state machine (PENDING → INGESTED → TRANSFORMED →
TERMINAL), generates cryptographically sealed ``.finex`` ZIP packages, and
enforces the terminal-state invariant.
"""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from datetime import datetime, timezone
from typing import Any

import yaml

from api.models.finex import (
    EntityScope,
    FinexManifest,
    FinexPhase,
    FinexRecord,
    LockFile,
    PIPELINE_TRANSITIONS,
    PipelineEntry,
    PipelineState,
)


class FinexService:
    """In-memory FINEX engine.

    Production deployments should back the registries with persistent storage
    (e.g. PostgreSQL + MinIO/S3 for ``.finex`` packages).
    """

    def __init__(self, finex_storage_dir: str = "/tmp/finex") -> None:
        self._registry: dict[str, FinexRecord] = {}
        self._pipeline: dict[str, PipelineEntry] = {}
        self._finex_storage_dir = finex_storage_dir

    # ------------------------------------------------------------------
    # Pipeline state machine
    # ------------------------------------------------------------------

    def get_or_create_pipeline(self, entity_id: str) -> PipelineEntry:
        """Return the pipeline entry, creating one in PENDING state if absent."""
        if entity_id not in self._pipeline:
            now = datetime.now(timezone.utc)
            self._pipeline[entity_id] = PipelineEntry(
                entity_id=entity_id,
                state=PipelineState.PENDING,
                created_at=now,
                updated_at=now,
            )
        return self._pipeline[entity_id]

    def get_pipeline(self, entity_id: str) -> PipelineEntry | None:
        """Return the pipeline entry or ``None``."""
        return self._pipeline.get(entity_id)

    def advance_pipeline(
        self,
        entity_id: str,
        to_state: PipelineState,
        **updates: Any,
    ) -> PipelineEntry:
        """Advance the pipeline to ``to_state``.

        Raises ``ValueError`` if the transition is illegal.
        """
        entry = self.get_or_create_pipeline(entity_id)
        current = PipelineState(entry.state)

        if to_state not in PIPELINE_TRANSITIONS.get(current, set()):
            raise ValueError(
                f"Illegal pipeline transition for '{entity_id}': "
                f"{current.value} → {to_state.value}.  "
                f"Allowed next states: {[s.value for s in PIPELINE_TRANSITIONS.get(current, set())]}."
            )

        entry.state = to_state.value  # type: ignore[assignment]
        entry.updated_at = datetime.now(timezone.utc)
        for k, v in updates.items():
            if hasattr(entry, k):
                setattr(entry, k, v)
        return entry

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def is_finalized(self, entity_id: str) -> bool:
        """Return ``True`` if the entity has been finalized."""
        return entity_id in self._registry

    def get_record(self, entity_id: str) -> FinexRecord | None:
        """Return the FINEX record for the entity, or ``None``."""
        return self._registry.get(entity_id)

    def list_all(self) -> list[FinexRecord]:
        """Return all FINEX records."""
        return list(self._registry.values())

    # ------------------------------------------------------------------
    # Finalization  (TRANSFORMED → TERMINAL)
    # ------------------------------------------------------------------

    def finalize(
        self,
        entity_id: str,
        entity_scope: EntityScope,
        finex_phase: FinexPhase,
        reason: str,
        authority: str,
        mission: str | None = None,
        vision: str | None = None,
        plan_summary: str | None = None,
        compliance_refs: list[str] | None = None,
    ) -> FinexRecord:
        """Mark an entity as permanently finalized and generate a ``.finex`` package.

        Raises ``ValueError`` if the entity is already finalized.
        """
        if self.is_finalized(entity_id):
            raise ValueError(
                f"Entity '{entity_id}' is already finalized. "
                "No further modifications are allowed."
            )

        # Build .finex package
        pipeline = self._pipeline.get(entity_id)
        payload_data = pipeline.payload if pipeline else {}
        package_bytes, manifest, integrity_hex = self._build_finex_package(
            entity_id=entity_id,
            entity_scope=entity_scope,
            mission=mission,
            vision=vision,
            plan_summary=plan_summary,
            authority=authority,
            compliance_refs=compliance_refs or [],
            payload_data=payload_data,
        )

        # Store in-memory (production: write to object storage)
        package_key = f"{entity_id}.finex"
        self._store_package(package_key, package_bytes)

        now = datetime.now(timezone.utc)
        record = FinexRecord(
            entity_id=entity_id,
            entity_scope=entity_scope,
            finex_phase=finex_phase,
            reason=reason,
            authority=authority,
            finalized_at=now,
            pipeline_state=PipelineState.TERMINAL,
            mission=mission,
            vision=vision,
            plan_summary=plan_summary,
            finex_package_path=package_key,
            compliance_refs=compliance_refs or [],
        )
        self._registry[entity_id] = record

        # Advance pipeline to TERMINAL if tracked
        if entity_id in self._pipeline:
            entry = self._pipeline[entity_id]
            entry.state = PipelineState.TERMINAL.value  # type: ignore[assignment]
            entry.updated_at = now

        return record

    # ------------------------------------------------------------------
    # .finex package builder
    # ------------------------------------------------------------------

    def _build_finex_package(
        self,
        *,
        entity_id: str,
        entity_scope: EntityScope,
        mission: str | None,
        vision: str | None,
        plan_summary: str | None,
        authority: str,
        compliance_refs: list[str],
        payload_data: dict[str, Any],
    ) -> tuple[bytes, FinexManifest, str]:
        """Build a ``.finex`` ZIP archive (in-memory).

        Structure::

            <entity_id>.finex (ZIP)
            ├── payload.json
            ├── manifest.yaml
            ├── integrity.sha256
            └── lock.json
        """
        # 1. Serialise payload
        payload_json = json.dumps(payload_data, sort_keys=True, default=str)
        payload_hash = hashlib.sha256(payload_json.encode()).hexdigest()

        # 2. Build manifest
        now_iso = datetime.now(timezone.utc).isoformat()
        manifest = FinexManifest(
            id=entity_id,
            effective_date=now_iso,
            entity_scope=entity_scope,
            mission=mission,
            vision=vision,
            plan_phase=plan_summary,
            compliance_refs=compliance_refs,
            integrity={"sha256": payload_hash},
        )

        # 3. Build lock file
        lock = LockFile(
            sealed_at=now_iso,
            authority=authority,
        )

        # 4. Assemble ZIP
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("payload.json", payload_json)
            zf.writestr("manifest.yaml", yaml.dump(manifest.model_dump(), default_flow_style=False))
            zf.writestr("integrity.sha256", f"sha256:{payload_hash}\n")
            zf.writestr("lock.json", json.dumps(lock.model_dump(), indent=2))
        buf.seek(0)
        return buf.read(), manifest, payload_hash

    # ------------------------------------------------------------------
    # Package storage (in-memory stub)
    # ------------------------------------------------------------------

    _package_store: dict[str, bytes] = {}

    def _store_package(self, key: str, data: bytes) -> None:
        self._package_store[key] = data

    def get_package_bytes(self, entity_id: str) -> bytes | None:
        """Return the raw ``.finex`` ZIP bytes, or ``None``."""
        return self._package_store.get(f"{entity_id}.finex")

    # ------------------------------------------------------------------
    # Guard (used by other routes to reject requests)
    # ------------------------------------------------------------------

    def enforce(self, entity_id: str) -> None:
        """Raise ``ValueError`` if the entity is finalized.

        Call this from ``/ingest`` and ``/transform`` routes to block
        requests against finalized entities.
        """
        record = self.get_record(entity_id)
        if record is not None:
            raise ValueError(
                f"Entity '{entity_id}' was finalized on "
                f"{record.finalized_at.isoformat()} "
                f"(phase: {record.finex_phase}, reason: {record.reason}). "
                "No further requests are permitted."
            )
