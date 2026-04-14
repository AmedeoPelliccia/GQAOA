"""Artifact metadata models.

Pydantic v2 models for .meta.yaml and _derivation.yaml as used in the
AMEDEO-ITBPFO transformation pipeline.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator


class Integrity(BaseModel):
    """Checksum integrity record."""

    model_config = ConfigDict(use_enum_values=True)

    checksum: str
    algorithm: Literal["sha256"] = "sha256"

    @field_validator("checksum")
    @classmethod
    def validate_sha256_format(cls, v: str) -> str:
        import re

        if not re.fullmatch(r"[0-9a-f]{64}", v):
            raise ValueError("checksum must be a 64-character lowercase hex string (SHA-256).")
        return v


class ArtifactMetadata(BaseModel):
    """Artifact .meta.yaml record (STD_Metadata-Schema-Guide_rev1.1.0)."""

    model_config = ConfigDict(use_enum_values=True)

    id: str
    type: str
    revision: str
    effective_date: str  # ISO 8601 date string
    integrity: Integrity
    source: str
    lifecycle_phase: str
    opt_axis: str
    lutndr_ref: str | None = None


class DerivationMetadata(BaseModel):
    """_derivation.yaml record — records the provenance of a transformation."""

    model_config = ConfigDict(use_enum_values=True)

    source_id: str
    transformation_id: str
    timestamp: datetime
    pipeline_version: str
    input_hash: str
    output_hash: str
