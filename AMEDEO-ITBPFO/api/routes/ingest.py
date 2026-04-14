import json
import uuid
from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

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


@router.post("", response_model=IngestionReceipt)
async def ingest(
    file: Annotated[UploadFile, File(description="Multimodal input artifact")],
    metadata: Annotated[str, Form(description="JSON metadata with source_type and genesis_source")] = "{}",
) -> IngestionReceipt:
    """Ingest a multimodal input and return an ingestion receipt.

    Validates that the declared ``source_type`` is one of the types supported by the
    AMEDEO-ITBPFO model (text, sensor_data, logs, images, yaml, csv) and maps the
    artifact to the canonical GENESIS/O-KNOT source.
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
    return IngestionReceipt(
        ingestion_id=str(uuid.uuid4()),
        timestamp=datetime.now(timezone.utc).isoformat(),
        source_type=source_type,
        genesis_source=genesis_source,
        filename=file.filename,
        size_bytes=len(content),
        status="accepted",
    )
