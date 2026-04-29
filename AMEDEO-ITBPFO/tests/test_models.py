"""Tests for AMEDEO-ITBPFO Pydantic v2 models."""

from __future__ import annotations

from datetime import date

import pytest

from api.models.applicability import ApplicabilityAttribute, ApplicabilityExpression, ApplicOperator
from api.models.lutndr import (
    Era,
    LutRegister,
    LutndrRecord,
    TechClass,
    TechState,
    TechSubState,
    TransitionEntry,
    _STATE_SUBSTATE_MAP,
)
from api.models.metadata import ArtifactMetadata, Integrity


# ---------------------------------------------------------------------------
# TechState / TechSubState enums
# ---------------------------------------------------------------------------


def test_tech_state_values():
    assert set(TechState) == {TechState.USO, TechState.NPR, TechState.DIS, TechState.RIC}


def test_tech_substate_count():
    """Exactly 15 sub-states must be defined (LUTNDR §3.2)."""
    assert len(TechSubState) == 15


def test_state_substate_map_totals():
    total = sum(len(v) for v in _STATE_SUBSTATE_MAP.values())
    assert total == 15


def test_tech_substate_prefixes():
    """Each sub-state value must begin with its parent state prefix."""
    for state, substates in _STATE_SUBSTATE_MAP.items():
        for ss in substates:
            assert ss.value.startswith(state.value), f"{ss.value} not prefixed with {state.value}"


# ---------------------------------------------------------------------------
# LutndrRecord creation and validation
# ---------------------------------------------------------------------------


def _valid_record(**overrides) -> dict:
    base = {
        "lutndr_id": "LUTNDR-000-001",
        "uta_chapter": "000",
        "technology_name": "Test Technology",
        "technology_class": TechClass.SOFTWARE,
        "current_state": TechState.USO,
        "current_substate": TechSubState.USO_ACT,
        "era": Era.I,
        "lifecycle_phase": "LC02",
        "first_registered": date(2026, 1, 1),
        "dpp_hash": "a" * 64,
    }
    base.update(overrides)
    return base


def test_lutndr_record_valid():
    record = LutndrRecord(**_valid_record())
    assert record.lutndr_id == "LUTNDR-000-001"
    assert record.current_state == TechState.USO.value


def test_lutndr_record_invalid_id_prefix():
    with pytest.raises(ValueError, match="lutndr_id must start with 'LUTNDR-'"):
        LutndrRecord(**_valid_record(lutndr_id="BAD-000-001"))


def test_lutndr_record_invalid_substate():
    """A DIS sub-state must not be accepted for an USO state."""
    with pytest.raises(ValueError, match="Sub-state.*not valid for state"):
        LutndrRecord(**_valid_record(current_substate=TechSubState.DIS_RET))


def test_lutndr_record_npr_valid():
    record = LutndrRecord(**_valid_record(current_state=TechState.NPR, current_substate=TechSubState.NPR_DEV))
    assert record.current_substate == TechSubState.NPR_DEV.value


def test_lutndr_record_ric_valid():
    record = LutndrRecord(**_valid_record(current_state=TechState.RIC, current_substate=TechSubState.RIC_REG))
    assert record.current_state == TechState.RIC.value


# ---------------------------------------------------------------------------
# LutRegister
# ---------------------------------------------------------------------------


def test_lut_register_creation():
    reg = LutRegister(
        chapter="000",
        chapter_name="General",
        last_updated=date.today(),
        technologies=[LutndrRecord(**_valid_record())],
    )
    assert len(reg.technologies) == 1


# ---------------------------------------------------------------------------
# ApplicabilityExpression
# ---------------------------------------------------------------------------


def test_applic_expression_and():
    expr = ApplicabilityExpression(operator=ApplicOperator.AND, operands=["msn==001", "variant==A"])
    assert expr.operator == ApplicOperator.AND.value


def test_applic_expression_or():
    expr = ApplicabilityExpression(operator=ApplicOperator.OR, operands=["msn==001", "msn==002"])
    assert len(expr.operands) == 2


def test_applic_expression_not_valid():
    expr = ApplicabilityExpression(operator=ApplicOperator.NOT, operands=["msn==001"])
    assert expr.operator == ApplicOperator.NOT.value


def test_applic_expression_not_invalid_arity():
    with pytest.raises(ValueError, match="exactly one operand"):
        ApplicabilityExpression(operator=ApplicOperator.NOT, operands=["msn==001", "msn==002"])


def test_applic_expression_nested():
    inner = ApplicabilityExpression(operator=ApplicOperator.OR, operands=["msn==001", "msn==002"])
    outer = ApplicabilityExpression(operator=ApplicOperator.AND, nested=[inner], operands=["variant==A"])
    assert len(outer.nested) == 1


def test_applic_attribute():
    attr = ApplicabilityAttribute(ident="msn", type="prodattr", values=["001", "002"])
    assert attr.ident == "msn"


# ---------------------------------------------------------------------------
# ArtifactMetadata / Integrity
# ---------------------------------------------------------------------------


def test_integrity_valid():
    i = Integrity(checksum="a" * 64)
    assert i.algorithm == "sha256"


def test_integrity_invalid_checksum():
    with pytest.raises(ValueError, match="64-character"):
        Integrity(checksum="not-a-valid-hash")


def test_artifact_metadata_valid():
    meta = ArtifactMetadata(
        id="ART-001",
        type="yaml",
        revision="1.0",
        effective_date="2026-04-14",
        integrity=Integrity(checksum="b" * 64),
        source="GENESIS/O-KNOT",
        lifecycle_phase="LC02",
        opt_axis="T",
    )
    assert meta.id == "ART-001"
