from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.services.transformer import TransformerService

router = APIRouter(prefix="/transform", tags=["transform"])

_transformer = TransformerService()


class TransformRequest(BaseModel):
    ingestion_id: str | None = None
    raw_data: str | None = None
    source_type: str = "text"
    uta_chapter: str = "000"
    lc_phase: str = "LC02"


class TransformResponse(BaseModel):
    artifact_id: str
    ssot_path: str
    content: dict
    derivation: dict
    status: str


@router.post("", response_model=TransformResponse)
def transform(request: TransformRequest) -> TransformResponse:
    """Transform ingested data into a structured SSOT-formatted artifact.

    Accepts either an ``ingestion_id`` (referencing a prior /ingest call) or
    ``raw_data`` with ``source_type``.  Returns the artifact together with
    ``_derivation.yaml`` metadata.
    """
    if request.ingestion_id is None and request.raw_data is None:
        raise HTTPException(
            status_code=422,
            detail="Provide either 'ingestion_id' or 'raw_data'.",
        )

    input_data = request.raw_data or f"<ref:{request.ingestion_id}>"
    artifact = _transformer.transform(input_data, request.source_type)
    derivation = _transformer.generate_metadata(artifact)
    ssot_path = _transformer.map_to_ssot_path(request.uta_chapter, request.lc_phase)

    return TransformResponse(
        artifact_id=artifact.artifact_id,
        ssot_path=ssot_path,
        content=artifact.content,
        derivation=derivation.model_dump(),
        status="transformed",
    )
