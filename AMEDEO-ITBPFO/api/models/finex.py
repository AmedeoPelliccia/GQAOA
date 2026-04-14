"""FINEX — Final Execution / Terminal-State models.

Pydantic v2 models for the FINEX (Final Execution) engine, which tracks
pipeline state (PENDING → INGESTED → TRANSFORMED → TERMINAL) and generates
cryptographically sealed ``.finex`` packages.  Once an entity reaches the
TERMINAL state, no further ingestion, transformation, or stock requests are
permitted.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class EntityScope(str, Enum):
    """Scope of the entity being finalized."""

    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    PROGRAM = "program"
    COMPANY = "company"
    ENTERPRISE = "enterprise"


class FinexPhase(str, Enum):
    """Terminal lifecycle phase that triggers FINEX.

    LC14_DECOMMISSION is the canonical final phase in the OPT-INS lifecycle.
    CUSTOM allows governance boards to define ad-hoc terminal points.
    """

    LC14_DECOMMISSION = "LC14_DECOMMISSION"
    CUSTOM = "CUSTOM"


class PipelineState(str, Enum):
    """Pipeline state machine (AMEDEO-ITBPFO §2).

    PENDING     → entity registered, awaiting ingestion.
    INGESTED    → input accepted via ``POST /ingest``.
    TRANSFORMED → output produced via ``POST /transform``.
    TERMINAL    → sealed via ``POST /finalize``; immutable from this point.
    """

    PENDING = "PENDING"
    INGESTED = "INGESTED"
    TRANSFORMED = "TRANSFORMED"
    TERMINAL = "TERMINAL"


# Allowed state transitions (directed edges)
PIPELINE_TRANSITIONS: dict[PipelineState, set[PipelineState]] = {
    PipelineState.PENDING: {PipelineState.INGESTED},
    PipelineState.INGESTED: {PipelineState.TRANSFORMED},
    PipelineState.TRANSFORMED: {PipelineState.TERMINAL},
    PipelineState.TERMINAL: set(),  # absorbing / no outbound edges
}


# ---------------------------------------------------------------------------
# Core models
# ---------------------------------------------------------------------------


class FinexRecord(BaseModel):
    """A FINEX record — marks an entity as permanently finalized.

    Once a FINEX record exists for an ``entity_id``, all subsequent ingestion,
    transformation, and stock requests referencing that entity must be rejected.
    """

    model_config = ConfigDict(use_enum_values=True)

    entity_id: str
    entity_scope: EntityScope
    finex_phase: FinexPhase
    reason: str
    authority: str
    finalized_at: datetime
    pipeline_state: PipelineState = PipelineState.TERMINAL
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None
    finex_package_path: str | None = None
    compliance_refs: list[str] = []

    @field_validator("entity_id")
    @classmethod
    def validate_entity_id_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("entity_id must not be empty.")
        return v.strip()

    @field_validator("reason")
    @classmethod
    def validate_reason_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("reason must not be empty.")
        return v.strip()


class PipelineEntry(BaseModel):
    """Tracks the current pipeline state for a given entity_id."""

    model_config = ConfigDict(use_enum_values=True)

    entity_id: str
    state: PipelineState
    ingestion_id: str | None = None
    transform_artifact_id: str | None = None
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    payload: dict[str, Any] = {}


# ---------------------------------------------------------------------------
# .finex package sub-models
# ---------------------------------------------------------------------------


class FinexManifest(BaseModel):
    """manifest.yaml inside a ``.finex`` ZIP package."""

    model_config = ConfigDict(use_enum_values=True)

    id: str
    type: str = "finex_terminal"
    revision: str = "1.0.0"
    effective_date: str
    entity_scope: EntityScope
    mission: str | None = None
    vision: str | None = None
    plan_phase: str | None = None
    compliance_refs: list[str] = []
    integrity: dict[str, str] = {}
    terminal_lock: bool = True


class LockFile(BaseModel):
    """lock.json inside a ``.finex`` ZIP package."""

    terminal: bool = True
    block_downstream: bool = True
    block_ingestion: bool = True
    block_transformation: bool = True
    block_stock_requests: bool = True
    sealed_at: str = ""
    authority: str = ""
