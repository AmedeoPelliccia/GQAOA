"""RegistryService — LUT Registry operations.

Manages LUT_REGISTER.yaml files and LUTNDR record lifecycle transitions.
"""

from __future__ import annotations

import os
from datetime import date
from typing import Any

import yaml

from api.models.lutndr import LutRegister, LutndrRecord, TechState, TransitionEntry, _STATE_SUBSTATE_MAP


class RegistryService:
    """Service for loading and mutating LUTNDR chapter registers."""

    def __init__(self, base_path: str = "SSOT") -> None:
        self.base_path = base_path

    # ------------------------------------------------------------------
    # Register I/O
    # ------------------------------------------------------------------

    def load_register(self, chapter: str) -> LutRegister:
        """Load LUT_REGISTER.yaml for the given UTA chapter.

        Looks for the file at:
            ``{base_path}/LC08_CONFIGURATION/{chapter}/LUT_REGISTER.yaml``

        TODO: Replace the stub return with actual file loading once the SSOT
        directory tree is populated.
        """
        path = os.path.join(self.base_path, "LC08_CONFIGURATION", chapter, "LUT_REGISTER.yaml")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
            return LutRegister.model_validate(data)

        # Stub: return an empty register when the file does not yet exist.
        return LutRegister(
            chapter=chapter,
            chapter_name=f"Chapter {chapter}",
            last_updated=date.today(),
            technologies=[],
        )

    def add_technology(self, chapter: str, record: LutndrRecord) -> LutndrRecord:
        """Add a new technology record to the chapter register.

        TODO: Persist the updated register back to LUT_REGISTER.yaml once the
        file-system integration is wired up.
        """
        register = self.load_register(chapter)
        existing_ids = {t.lutndr_id for t in register.technologies}
        if record.lutndr_id in existing_ids:
            raise ValueError(f"Technology '{record.lutndr_id}' already exists in chapter {chapter}.")
        register.technologies.append(record)
        return record

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------

    def transition_state(
        self,
        lutndr_id: str,
        new_state: TechState,
        eco: str,
        gate: str,
        chapter: str = "000",
        authority: str = "GAIA-QAO Architecture Board",
    ) -> TransitionEntry:
        """Execute a validated state transition for a LUTNDR record.

        Validates that ``new_state`` is a legal adjacent state before recording
        the transition.

        TODO: Implement full transition matrix (adjacency rules) per LUTNDR §5.
        """
        register = self.load_register(chapter)
        record = next((t for t in register.technologies if t.lutndr_id == lutndr_id), None)
        if record is None:
            raise ValueError(f"Technology '{lutndr_id}' not found in chapter {chapter}.")

        entry = TransitionEntry(
            from_state=TechState(record.current_state),
            to_state=new_state,
            date=date.today(),
            eco=eco,
            gate=gate,
            authority=authority,
        )
        # TODO: persist the transition back to disk
        return entry

    # ------------------------------------------------------------------
    # Circularity metrics (LUTNDR §11.2)
    # ------------------------------------------------------------------

    def get_circularity_metrics(self, chapter: str) -> dict[str, Any]:
        """Compute circularity metrics for all technologies in a chapter.

        Returns IC (Index of Circularity), TR (Transition Rate), ΔCO₂,
        CDPP (Circularity DPP score), and VT (Value of Transformation) per
        LUTNDR §11.2.

        TODO: Replace stub formulas with the actual metrics defined in
        LUTNDR §11.2 once the specification is published.
        """
        register = self.load_register(chapter)
        total = len(register.technologies)
        ric_count = sum(
            1 for t in register.technologies if TechState(t.current_state) == TechState.RIC
        )

        ic = round(ric_count / total, 4) if total else 0.0
        return {
            "chapter": chapter,
            "total_technologies": total,
            "ric_count": ric_count,
            "IC": ic,          # Index of Circularity
            "TR": 0.0,         # TODO: Transition Rate (transitions / period)
            "delta_co2": 0.0,  # TODO: ΔCO₂ reduction estimate
            "CDPP": 0.0,       # TODO: Circularity DPP score
            "VT": 0.0,         # TODO: Value of Transformation
        }
