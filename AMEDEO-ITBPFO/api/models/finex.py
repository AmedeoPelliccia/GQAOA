"""FINEX — Final Execution / Terminal-State models.

Pydantic v2 models for the FINEX (Final Execution) endpoint, which marks an
entity (organization, repository, program, company, or enterprise) as finalized.
Once finalized, no further ingestion, transformation, or stock requests are
permitted against that entity.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, field_validator


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
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None

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
