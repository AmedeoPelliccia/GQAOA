from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.models.finex import PipelineState
from api.routes.finex import finex_service
from api.services.transformer import TransformerService

router = APIRouter(prefix="/transform", tags=["transform"])

_transformer = TransformerService()


class TransformRequest(BaseModel):
    ingestion_id: str | None = None
    raw_data: str | None = None
    source_type: str = "text"
    uta_chapter: str = "000"
    lc_phase: str = "LC02"
    entity_id: str | None = None


class TransformResponse(BaseModel):
    artifact_id: str
    ssot_path: str
    content: dict
    derivation: dict
    status: str
    pipeline_state: str | None = None


@router.post("", response_model=TransformResponse)
def transform(request: TransformRequest) -> TransformResponse:
    """Transform ingested data into a structured SSOT-formatted artifact.

    Accepts either an ``ingestion_id`` (referencing a prior /ingest call) or
    ``raw_data`` with ``source_type``.  Returns the artifact together with
    ``_derivation.yaml`` metadata.

    If ``entity_id`` is provided, the pipeline state is advanced from
    INGESTED to TRANSFORMED automatically.
    """
    if request.ingestion_id is None and request.raw_data is None:
        raise HTTPException(
            status_code=422,
            detail="Provide either 'ingestion_id' or 'raw_data'.",
        )

    # FINEX guard — reject requests on finalized entities
    if request.entity_id:
        try:
            finex_service.enforce(request.entity_id)
        except ValueError as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc

    input_data = request.raw_data or f"<ref:{request.ingestion_id}>"
    artifact = _transformer.transform(input_data, request.source_type)
    derivation = _transformer.generate_metadata(artifact)
    ssot_path = _transformer.map_to_ssot_path(request.uta_chapter, request.lc_phase)

    # Advance pipeline: INGESTED → TRANSFORMED
    pipeline_state = None
    if request.entity_id:
        try:
            finex_service.advance_pipeline(
                request.entity_id,
                PipelineState.TRANSFORMED,
                transform_artifact_id=artifact.artifact_id,
                payload=artifact.content,
            )
            pipeline_state = PipelineState.TRANSFORMED.value
        except ValueError:
            # Pipeline not in INGESTED state — still return the artifact
            entry = finex_service.get_pipeline(request.entity_id)
            pipeline_state = entry.state if entry else None

    return TransformResponse(
        artifact_id=artifact.artifact_id,
        ssot_path=ssot_path,
        content=artifact.content,
        derivation=derivation.model_dump(),
        status="transformed",
        pipeline_state=pipeline_state,
    )
