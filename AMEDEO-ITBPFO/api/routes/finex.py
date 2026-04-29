"""FINEX route — Final Execution endpoints.

POST /finex                    — finalize an entity (legacy; creates TERMINAL + package)
POST /finex/finalize/{id}      — finalize a tracked entity (pipeline must be TRANSFORMED)
GET  /finex                    — list all finalized entities
GET  /finex/status/{id}        — pipeline + finex status
GET  /finex/{entity_id}        — check finalization status of a single entity
GET  /finex/{entity_id}/download — download the sealed ``.finex`` ZIP package
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

from api.models.finex import EntityScope, FinexPhase, PipelineState
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
    compliance_refs: list[str] = []


class FinexResponse(BaseModel):
    entity_id: str
    entity_scope: str
    finex_phase: str
    reason: str
    authority: str
    finalized_at: str
    pipeline_state: str = "TERMINAL"
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None
    finex_package_path: str | None = None
    compliance_refs: list[str] = []


class FinexStatusResponse(BaseModel):
    entity_id: str
    finalized: bool
    pipeline_state: str | None = None
    record: FinexResponse | None = None


class PipelineStatusResponse(BaseModel):
    entity_id: str
    state: str
    ingestion_id: str | None = None
    transform_artifact_id: str | None = None
    mission: str | None = None
    vision: str | None = None
    plan_summary: str | None = None
    finalized: bool = False


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def _record_to_response(record) -> FinexResponse:  # noqa: ANN001
    return FinexResponse(
        entity_id=record.entity_id,
        entity_scope=record.entity_scope,
        finex_phase=record.finex_phase,
        reason=record.reason,
        authority=record.authority,
        finalized_at=record.finalized_at.isoformat(),
        pipeline_state=record.pipeline_state,
        mission=record.mission,
        vision=record.vision,
        plan_summary=record.plan_summary,
        finex_package_path=record.finex_package_path,
        compliance_refs=record.compliance_refs,
    )


# ---------------------------------------------------------------------------
# Routes — Finalize
# ---------------------------------------------------------------------------


@router.post("", response_model=FinexResponse)
def finalize_entity(request: FinalizeRequest) -> FinexResponse:
    """Finalize an entity — generate a sealed ``.finex`` package and lock it.

    This action is **irreversible**.  After finalization:
    - ``POST /ingest`` → HTTP 403  (if ``entity_id`` matches)
    - ``POST /transform`` → HTTP 403
    - No further stock requests are permitted.
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
            compliance_refs=request.compliance_refs,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return _record_to_response(record)


@router.post("/finalize/{entity_id}", response_model=FinexResponse)
def finalize_by_pipeline(entity_id: str, request: FinalizeRequest) -> FinexResponse:
    """Finalize an entity that has been tracked through the pipeline.

    The pipeline must be in ``TRANSFORMED`` state.  This endpoint advances
    it to ``TERMINAL`` and generates the ``.finex`` package.
    """
    pipeline = finex_service.get_pipeline(entity_id)
    if pipeline is None:
        raise HTTPException(status_code=404, detail=f"No pipeline found for entity '{entity_id}'.")

    current = PipelineState(pipeline.state)
    if current == PipelineState.TERMINAL:
        raise HTTPException(status_code=409, detail=f"Entity '{entity_id}' is already TERMINAL.")
    if current != PipelineState.TRANSFORMED:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Entity '{entity_id}' is in state '{current.value}'. "
                "Must be TRANSFORMED before finalization."
            ),
        )

    try:
        record = finex_service.finalize(
            entity_id=entity_id,
            entity_scope=request.entity_scope,
            finex_phase=request.finex_phase,
            reason=request.reason,
            authority=request.authority,
            mission=request.mission or pipeline.mission,
            vision=request.vision or pipeline.vision,
            plan_summary=request.plan_summary or pipeline.plan_summary,
            compliance_refs=request.compliance_refs,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return _record_to_response(record)


# ---------------------------------------------------------------------------
# Routes — Status / Query
# ---------------------------------------------------------------------------


@router.get("/status/{entity_id}", response_model=PipelineStatusResponse)
def get_pipeline_status(entity_id: str) -> PipelineStatusResponse:
    """Return full pipeline + finex status for an entity."""
    pipeline = finex_service.get_pipeline(entity_id)
    finalized = finex_service.is_finalized(entity_id)

    if pipeline is None:
        return PipelineStatusResponse(
            entity_id=entity_id,
            state="UNKNOWN",
            finalized=finalized,
        )

    return PipelineStatusResponse(
        entity_id=entity_id,
        state=pipeline.state,
        ingestion_id=pipeline.ingestion_id,
        transform_artifact_id=pipeline.transform_artifact_id,
        mission=pipeline.mission,
        vision=pipeline.vision,
        plan_summary=pipeline.plan_summary,
        finalized=finalized,
    )


@router.get("", response_model=list[FinexResponse])
def list_finalized() -> list[FinexResponse]:
    """List all finalized entities."""
    return [_record_to_response(r) for r in finex_service.list_all()]


@router.get("/{entity_id}", response_model=FinexStatusResponse)
def check_finex_status(entity_id: str) -> FinexStatusResponse:
    """Check whether an entity is finalized."""
    record = finex_service.get_record(entity_id)
    pipeline = finex_service.get_pipeline(entity_id)
    pipeline_state = pipeline.state if pipeline else None

    if record is None:
        return FinexStatusResponse(
            entity_id=entity_id,
            finalized=False,
            pipeline_state=pipeline_state,
        )
    return FinexStatusResponse(
        entity_id=entity_id,
        finalized=True,
        pipeline_state=pipeline_state or "TERMINAL",
        record=_record_to_response(record),
    )


# ---------------------------------------------------------------------------
# Routes — Download .finex package
# ---------------------------------------------------------------------------


@router.get("/{entity_id}/download")
def download_finex_package(entity_id: str) -> Response:
    """Download the sealed ``.finex`` ZIP package for the entity.

    Returns ``application/zip`` with filename ``<entity_id>.finex``.
    """
    if not finex_service.is_finalized(entity_id):
        raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' has not been finalized.")

    data = finex_service.get_package_bytes(entity_id)
    if data is None:
        raise HTTPException(status_code=404, detail=f"No .finex package found for '{entity_id}'.")

    return Response(
        content=data,
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{entity_id}.finex"'},
    )
