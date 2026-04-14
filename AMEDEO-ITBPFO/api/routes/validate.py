from fastapi import APIRouter
from pydantic import BaseModel

from api.services.validator import ValidatorService

router = APIRouter(prefix="/validate", tags=["validate"])

_validator = ValidatorService()


class ValidateRequest(BaseModel):
    artifact: dict


class CheckResult(BaseModel):
    check: str
    passed: bool
    message: str


class ValidateResponse(BaseModel):
    artifact_id: str | None
    overall: bool
    checks: list[CheckResult]


@router.post("", response_model=ValidateResponse)
def validate_artifact(request: ValidateRequest) -> ValidateResponse:
    """Validate a structured artifact against the STD_Metadata-Schema-Guide.

    Runs the following checks:
    - **metadata**: completeness of required fields
    - **checksum**: SHA-256 integrity verification
    - **lutndr_state**: LUTNDR state/substate consistency
    - **applicability**: applicability expression syntax

    Returns a per-check pass/fail report.
    """
    report = _validator.full_validation_dict(request.artifact)
    return ValidateResponse(
        artifact_id=request.artifact.get("id"),
        overall=report["overall"],
        checks=[CheckResult(**c) for c in report["checks"]],
    )
