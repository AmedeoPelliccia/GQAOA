"""FINEX route — Final Execution endpoint.

POST /finex   — finalize an entity (organization, repository, program, company, enterprise)
GET  /finex   — list all finalized entities
GET  /finex/{entity_id} — check finalization status of a single entity
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.models.finex import EntityScope, FinexPhase
from api.services.finex import FinexService

router = APIRouter(prefix="/finex", tags=["finex"])

# Shared singleton — imported by ingest/transform routes for guard checks
finex_service = FinexService()


# ---------------------------------------------------------------------------
# Request / response schemas
# ---------------------------------------------------------------------------


class FinalizeRequest(BaseModel):
    entity_id: str
    entity_scope: EntityScope
    finex_phase: FinexPhase = FinexPhase.LC14_DECOMMISSION
    reason: str
    authority: str
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None


class FinexResponse(BaseModel):
    entity_id: str
    entity_scope: str
    finex_phase: str
    reason: str
    authority: str
    finalized_at: str
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None


class FinexStatusResponse(BaseModel):
    entity_id: str
    finalized: bool
    record: FinexResponse | None = None


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@router.post("", response_model=FinexResponse)
def finalize_entity(request: FinalizeRequest) -> FinexResponse:
    """Finalize an entity — no further ingestion, transformation, or stock
    requests will be accepted for this ``entity_id``.

    This action is **irreversible** within the current process lifecycle.
    """
    try:
        record = finex_service.finalize(
            entity_id=request.entity_id,
            entity_scope=request.entity_scope,
            finex_phase=request.finex_phase,
            reason=request.reason,
            authority=request.authority,
            mission=request.mission,
            vision=request.vision,
            plan_summary=request.plan_summary,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return FinexResponse(
        entity_id=record.entity_id,
        entity_scope=record.entity_scope,
        finex_phase=record.finex_phase,
        reason=record.reason,
        authority=record.authority,
        finalized_at=record.finalized_at.isoformat(),
        mission=record.mission,
        vision=record.vision,
        plan_summary=record.plan_summary,
    )


@router.get("", response_model=list[FinexResponse])
def list_finalized() -> list[FinexResponse]:
    """List all finalized entities."""
    return [
        FinexResponse(
            entity_id=r.entity_id,
            entity_scope=r.entity_scope,
            finex_phase=r.finex_phase,
            reason=r.reason,
            authority=r.authority,
            finalized_at=r.finalized_at.isoformat(),
            mission=r.mission,
            vision=r.vision,
            plan_summary=r.plan_summary,
        )
        for r in finex_service.list_all()
    ]


@router.get("/{entity_id}", response_model=FinexStatusResponse)
def check_finex_status(entity_id: str) -> FinexStatusResponse:
    """Check whether an entity is finalized."""
    record = finex_service.get_record(entity_id)
    if record is None:
        return FinexStatusResponse(entity_id=entity_id, finalized=False)
    return FinexStatusResponse(
        entity_id=entity_id,
        finalized=True,
        record=FinexResponse(
            entity_id=record.entity_id,
            entity_scope=record.entity_scope,
            finex_phase=record.finex_phase,
            reason=record.reason,
            authority=record.authority,
            finalized_at=record.finalized_at.isoformat(),
            mission=record.mission,
            vision=record.vision,
            plan_summary=record.plan_summary,
        ),
    )
