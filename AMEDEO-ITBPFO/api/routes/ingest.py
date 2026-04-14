import json
import uuid
from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from api.models.finex import PipelineState
from api.routes.finex import finex_service

ALLOWED_SOURCE_TYPES = {"text", "sensor_data", "logs", "images", "yaml", "csv"}

router = APIRouter(prefix="/ingest", tags=["ingest"])


class IngestionReceipt(BaseModel):
    ingestion_id: str
    timestamp: str
    source_type: str
    genesis_source: str
    filename: str | None
    size_bytes: int
    status: str
    pipeline_state: str | None = None


@router.post("", response_model=IngestionReceipt)
async def ingest(
    file: Annotated[UploadFile, File(description="Multimodal input artifact")],
    metadata: Annotated[str, Form(description="JSON metadata with source_type and genesis_source")] = "{}",
) -> IngestionReceipt:
    """Ingest a multimodal input and return an ingestion receipt.

    Validates that the declared ``source_type`` is one of the types supported by the
    AMEDEO-ITBPFO model (text, sensor_data, logs, images, yaml, csv) and maps the
    artifact to the canonical GENESIS/O-KNOT source.

    If ``entity_id`` is provided in the metadata, the pipeline state is advanced
    from PENDING to INGESTED automatically.
    """
    try:
        meta = json.loads(metadata)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=422, detail=f"Invalid metadata JSON: {exc}") from exc

    source_type = meta.get("source_type", "text")
    if source_type not in ALLOWED_SOURCE_TYPES:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported source_type '{source_type}'. Allowed: {sorted(ALLOWED_SOURCE_TYPES)}",
        )

    genesis_source = meta.get("genesis_source", "GENESIS/O-KNOT")

    # FINEX guard — reject requests on finalized entities
    entity_id = meta.get("entity_id")
    if entity_id:
        try:
            finex_service.enforce(entity_id)
        except ValueError as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc

    content = await file.read()
    ingestion_id = str(uuid.uuid4())

    # Advance pipeline: PENDING → INGESTED
    pipeline_state = None
    if entity_id:
        try:
            entry = finex_service.get_or_create_pipeline(entity_id)
            mission = meta.get("mission")
            vision = meta.get("vision")
            plan_summary = meta.get("plan_summary")
            finex_service.advance_pipeline(
                entity_id,
                PipelineState.INGESTED,
                ingestion_id=ingestion_id,
                mission=mission,
                vision=vision,
                plan_summary=plan_summary,
            )
            pipeline_state = PipelineState.INGESTED.value
        except ValueError:
            # Pipeline already advanced past INGESTED — still accept the file
            pipeline_state = entry.state

    return IngestionReceipt(
        ingestion_id=ingestion_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        source_type=source_type,
        genesis_source=genesis_source,
        filename=file.filename,
        size_bytes=len(content),
        status="accepted",
        pipeline_state=pipeline_state,
    )
