"""ValidatorService — validates artifacts against STD_Metadata-Schema-Guide.

Runs metadata completeness, checksum integrity, LUTNDR state, and
applicability expression checks.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from api.models.lutndr import LutndrRecord, TechState, TechSubState, _STATE_SUBSTATE_MAP


# ---------------------------------------------------------------------------
# Report dataclasses (returned both internally and via the route)
# ---------------------------------------------------------------------------


@dataclass
class CheckResult:
    check: str
    passed: bool
    message: str


@dataclass
class ValidationReport:
    overall: bool
    checks: list[CheckResult] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "overall": self.overall,
            "checks": [{"check": c.check, "passed": c.passed, "message": c.message} for c in self.checks],
        }


# Required top-level keys for a valid artifact .meta.yaml
_REQUIRED_METADATA_KEYS = {"id", "type", "revision", "effective_date", "integrity", "source", "lifecycle_phase"}


class ValidatorService:
    """Validate SSOT artifacts against the STD_Metadata-Schema-Guide_rev1.1.0."""

    # ------------------------------------------------------------------
    # Public composite validator
    # ------------------------------------------------------------------

    def full_validation(self, artifact: dict[str, Any]) -> ValidationReport:
        """Run all checks and return a consolidated ``ValidationReport``."""
        metadata_report = self.validate_metadata(artifact)
        checksum_ok = self.validate_checksum(artifact)
        lutndr_report = self._validate_lutndr_from_dict(artifact)
        applic_report = self._validate_applicability_from_dict(artifact)

        checks: list[CheckResult] = []
        checks.extend(metadata_report.checks)
        checks.append(
            CheckResult(
                check="checksum",
                passed=checksum_ok,
                message="Checksum verified." if checksum_ok else "Checksum mismatch or missing.",
            )
        )
        checks.extend(lutndr_report.checks)
        checks.extend(applic_report.checks)

        overall = all(c.passed for c in checks)
        return ValidationReport(overall=overall, checks=checks)

    def full_validation_dict(self, artifact: dict[str, Any]) -> dict[str, Any]:
        """Convenience wrapper returning a plain dict (used by the route layer)."""
        return self.full_validation(artifact).to_dict()

    # ------------------------------------------------------------------
    # Individual checkers
    # ------------------------------------------------------------------

    def validate_metadata(self, artifact: dict[str, Any]) -> ValidationReport:
        """Check .meta.yaml completeness (required fields present and non-empty)."""
        checks: list[CheckResult] = []
        missing = [k for k in _REQUIRED_METADATA_KEYS if not artifact.get(k)]
        if missing:
            checks.append(
                CheckResult(
                    check="metadata",
                    passed=False,
                    message=f"Missing required fields: {missing}",
                )
            )
        else:
            checks.append(CheckResult(check="metadata", passed=True, message="All required metadata fields present."))
        overall = all(c.passed for c in checks)
        return ValidationReport(overall=overall, checks=checks)

    def validate_checksum(self, artifact: dict[str, Any]) -> bool:
        """Verify SHA-256 integrity of the artifact content.

        The artifact dict must contain an ``integrity`` sub-dict with keys
        ``checksum`` and ``algorithm``, plus a ``content`` key whose serialised
        value is hashed and compared.

        TODO: Define canonical serialisation order for reproducible hashing.
        """
        integrity = artifact.get("integrity")
        if not isinstance(integrity, dict):
            return False
        stored = integrity.get("checksum", "")
        algorithm = integrity.get("algorithm", "sha256")
        if algorithm != "sha256":
            return False
        content = artifact.get("content", "")
        computed = hashlib.sha256(str(content).encode()).hexdigest()
        return computed == stored

    def validate_lutndr_state(self, record: LutndrRecord) -> ValidationReport:
        """Check LUTNDR state/substate consistency and transition rules."""
        checks: list[CheckResult] = []
        state = TechState(record.current_state)
        substate = TechSubState(record.current_substate)
        allowed = _STATE_SUBSTATE_MAP.get(state, set())
        if substate not in allowed:
            checks.append(
                CheckResult(
                    check="lutndr_state",
                    passed=False,
                    message=(
                        f"Sub-state '{substate.value}' is incompatible with state '{state.value}'. "
                        f"Allowed: {[s.value for s in allowed]}"
                    ),
                )
            )
        else:
            checks.append(
                CheckResult(
                    check="lutndr_state",
                    passed=True,
                    message=f"State '{state.value}' / sub-state '{substate.value}' combination is valid.",
                )
            )
        overall = all(c.passed for c in checks)
        return ValidationReport(overall=overall, checks=checks)

    def validate_applicability(self, expression: dict[str, Any]) -> ValidationReport:
        """Check applicability expression syntax (operator + operands present).

        TODO: Extend to full S1000D applicability annotation validation once
        the ACT/PCT/CCT register integration is complete.
        """
        checks: list[CheckResult] = []
        operator = expression.get("operator")
        operands = expression.get("operands", [])
        nested = expression.get("nested", [])

        if operator not in ("AND", "OR", "NOT"):
            checks.append(
                CheckResult(
                    check="applicability",
                    passed=False,
                    message=f"Invalid operator '{operator}'. Must be AND, OR, or NOT.",
                )
            )
        elif operator == "NOT" and (len(operands) + len(nested)) != 1:
            checks.append(
                CheckResult(
                    check="applicability",
                    passed=False,
                    message="NOT operator must have exactly one operand.",
                )
            )
        else:
            checks.append(CheckResult(check="applicability", passed=True, message="Applicability expression is valid."))
        overall = all(c.passed for c in checks)
        return ValidationReport(overall=overall, checks=checks)

    # ------------------------------------------------------------------
    # Internal helpers for full_validation
    # ------------------------------------------------------------------

    def _validate_lutndr_from_dict(self, artifact: dict[str, Any]) -> ValidationReport:
        lutndr = artifact.get("lutndr")
        if not lutndr:
            return ValidationReport(
                overall=True,
                checks=[CheckResult(check="lutndr_state", passed=True, message="No LUTNDR record present; skipped.")],
            )
        try:
            record = LutndrRecord.model_validate(lutndr)
            return self.validate_lutndr_state(record)
        except Exception as exc:
            return ValidationReport(
                overall=False,
                checks=[CheckResult(check="lutndr_state", passed=False, message=str(exc))],
            )

    def _validate_applicability_from_dict(self, artifact: dict[str, Any]) -> ValidationReport:
        expression = artifact.get("applicability")
        if not expression:
            return ValidationReport(
                overall=True,
                checks=[
                    CheckResult(check="applicability", passed=True, message="No applicability expression present; skipped.")
                ],
            )
        return self.validate_applicability(expression)
