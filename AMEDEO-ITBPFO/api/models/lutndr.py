"""LUTNDR — Libro Unico delle Tecnologie: in uso, Nuova progettazione, Disuso, Riassetti.

Pydantic v2 models for the LUTNDR technology lifecycle registry as defined in
GQAOA-UTA-LUTNDR-001 (parent: GQAOA-UTA-SUPIA-001).
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


# ---------------------------------------------------------------------------
# Enums — LUTNDR §3.1 – §3.4
# ---------------------------------------------------------------------------


class TechState(str, Enum):
    """Four primary lifecycle states (LUTNDR §3.1)."""

    USO = "USO"  # In uso / Operational
    NPR = "NPR"  # Nuova progettazione / New design
    DIS = "DIS"  # Disuso / Disuse
    RIC = "RIC"  # Riassetti / Recycled-rearranged


class TechSubState(str, Enum):
    """Fifteen sub-states distributed across the four primary states (LUTNDR §3.2).

    USO  → USO_ACT, USO_STD, USO_LIM, USO_OBS  (4)
    NPR  → NPR_CON, NPR_DEV, NPR_VAL, NPR_CRT  (4)
    DIS  → DIS_PHO, DIS_FRZ, DIS_RET, DIS_ARC  (4)
    RIC  → RIC_REG, RIC_UPG, RIC_REP            (3)
    """

    # USO sub-states
    USO_ACT = "USO_ACT"  # Active / Fully operational
    USO_STD = "USO_STD"  # Standby
    USO_LIM = "USO_LIM"  # Limited use (conditional authorisation)
    USO_OBS = "USO_OBS"  # Obsolescence watch

    # NPR sub-states
    NPR_CON = "NPR_CON"  # Concept / Pre-design
    NPR_DEV = "NPR_DEV"  # Development
    NPR_VAL = "NPR_VAL"  # Validation
    NPR_CRT = "NPR_CRT"  # Certified / Qualified

    # DIS sub-states
    DIS_PHO = "DIS_PHO"  # Phase-out in progress
    DIS_FRZ = "DIS_FRZ"  # Frozen (no new applications)
    DIS_RET = "DIS_RET"  # Retired
    DIS_ARC = "DIS_ARC"  # Archived

    # RIC sub-states
    RIC_REG = "RIC_REG"  # Regenerated
    RIC_UPG = "RIC_UPG"  # Upgraded / Reprogrammed
    RIC_REP = "RIC_REP"  # Repurposed


# Mapping: allowed sub-states per primary state
_STATE_SUBSTATE_MAP: dict[TechState, set[TechSubState]] = {
    TechState.USO: {TechSubState.USO_ACT, TechSubState.USO_STD, TechSubState.USO_LIM, TechSubState.USO_OBS},
    TechState.NPR: {TechSubState.NPR_CON, TechSubState.NPR_DEV, TechSubState.NPR_VAL, TechSubState.NPR_CRT},
    TechState.DIS: {TechSubState.DIS_PHO, TechSubState.DIS_FRZ, TechSubState.DIS_RET, TechSubState.DIS_ARC},
    TechState.RIC: {TechSubState.RIC_REG, TechSubState.RIC_UPG, TechSubState.RIC_REP},
}


class TechClass(str, Enum):
    """Technology classification (LUTNDR §3.3)."""

    SYSTEM = "SYSTEM"
    SUBSYSTEM = "SUBSYSTEM"
    COMPONENT = "COMPONENT"
    MATERIAL = "MATERIAL"
    SOFTWARE = "SOFTWARE"
    PROCESS = "PROCESS"
    TOOL = "TOOL"
    STANDARD = "STANDARD"


class Era(str, Enum):
    """Technology era (LUTNDR §3.4)."""

    I = "I"     # noqa: E741  — Era I: legacy / first generation
    II = "II"
    III = "III"
    IV = "IV"


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------


class TransitionEntry(BaseModel):
    """A single LUTNDR state-transition event."""

    model_config = ConfigDict(use_enum_values=True)

    from_state: TechState
    to_state: TechState
    date: date
    eco: str  # Engineering Change Order identifier
    gate: str  # Governance gate that authorised the transition
    authority: str


class TraceabilityRef(BaseModel):
    """Traceability reference to a KNOT/KNU node."""

    knot_id: str
    knu_id: str | None = None
    lc_phase: str | None = None


# ---------------------------------------------------------------------------
# Core LUTNDR models
# ---------------------------------------------------------------------------


class LutndrRecord(BaseModel):
    """Full technology record in the LUTNDR register (LUTNDR §4)."""

    model_config = ConfigDict(use_enum_values=True)

    lutndr_id: str
    uta_chapter: str
    technology_name: str
    technology_class: TechClass
    current_state: TechState
    current_substate: TechSubState
    era: Era
    lifecycle_phase: str
    first_registered: date
    dpp_hash: str
    programmes: list[str] = []
    knot_refs: list[str] = []
    traceability: list[TraceabilityRef] = []
    circularity: dict[str, Any] = {}
    transition_history: list[TransitionEntry] = []

    @model_validator(mode="after")
    def validate_substate_matches_state(self) -> "LutndrRecord":
        state = TechState(self.current_state)
        substate = TechSubState(self.current_substate)
        allowed = _STATE_SUBSTATE_MAP[state]
        if substate not in allowed:
            raise ValueError(
                f"Sub-state '{substate}' is not valid for state '{state}'. "
                f"Allowed: {[s.value for s in allowed]}"
            )
        return self

    @field_validator("lutndr_id")
    @classmethod
    def validate_lutndr_id(cls, v: str) -> str:
        if not v.startswith("LUTNDR-"):
            raise ValueError("lutndr_id must start with 'LUTNDR-'")
        return v


class LutRegister(BaseModel):
    """Chapter-level LUTNDR register (stored as LUT_REGISTER.yaml in LC08)."""

    model_config = ConfigDict(use_enum_values=True)

    chapter: str
    chapter_name: str
    last_updated: date
    technologies: list[LutndrRecord] = []
