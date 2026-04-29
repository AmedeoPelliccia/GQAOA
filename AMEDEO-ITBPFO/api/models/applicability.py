"""S1000D Applicability models.

Pydantic v2 models for S1000D applicability as used in the AMEDEO-ITBPFO
transformation pipeline (CSDB/APPLICABILITY/).
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, model_validator


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class ApplicOperator(str, Enum):
    """Logical operators for applicability expressions (S1000D §6.x)."""

    AND = "AND"
    OR = "OR"
    NOT = "NOT"


class Environment(str, Enum):
    """Operating environment variants."""

    STANDARD = "STANDARD"
    COLD = "COLD"
    HOT = "HOT"
    HUMID = "HUMID"
    SALT = "SALT"
    ALTITUDE = "ALTITUDE"


class OptAxis(str, Enum):
    """OPT-INS topology axes."""

    O = "O"  # Organizations
    P = "P"  # Programs
    T = "T"  # Technologies
    I = "I"  # Infrastructures  # noqa: E741
    N = "N"  # Neural Networks
    S = "S"  # SIM-TEST / Space


# ---------------------------------------------------------------------------
# Attribute and expression models
# ---------------------------------------------------------------------------


class ApplicabilityAttribute(BaseModel):
    """Single applicability attribute definition (ACT entry)."""

    model_config = ConfigDict(use_enum_values=True)

    ident: str
    type: str  # e.g. "prodattr", "condition"
    values: list[str]
    s1000d_mapping: str | None = None


class ApplicabilityExpression(BaseModel):
    """Logical applicability expression (AND / OR / NOT tree)."""

    model_config = ConfigDict(use_enum_values=True)

    operator: ApplicOperator
    operands: list[str] = []
    nested: list["ApplicabilityExpression"] = []

    @model_validator(mode="after")
    def validate_not_arity(self) -> "ApplicabilityExpression":
        if self.operator == ApplicOperator.NOT:
            total = len(self.operands) + len(self.nested)
            if total != 1:
                raise ValueError("NOT operator must have exactly one operand.")
        return self


# ---------------------------------------------------------------------------
# Cross-reference table entries
# ---------------------------------------------------------------------------


class ACTEntry(BaseModel):
    """Applicability Cross-reference Table entry (ACT)."""

    applicability_id: str
    attributes: list[ApplicabilityAttribute]


class PCTEntry(BaseModel):
    """Product Cross-reference Table entry (PCT)."""

    product_id: str
    applicability_id: str
    attribute_values: dict[str, Any] = {}


class CCTEntry(BaseModel):
    """Condition Cross-reference Table entry (CCT)."""

    condition_id: str
    applicability_id: str
    environment: Environment
    opt_axis: OptAxis
    description: str | None = None
