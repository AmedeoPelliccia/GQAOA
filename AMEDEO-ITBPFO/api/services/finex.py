"""FinexService — Final Execution enforcement.

Manages the FINEX registry: records finalized entities and enforces the
terminal-state invariant (no further ingestion, transformation, or stock
requests once an entity is finalized).
"""

from __future__ import annotations

from datetime import datetime, timezone

from api.models.finex import EntityScope, FinexPhase, FinexRecord


class FinexService:
    """In-memory FINEX registry.

    Production deployments should back this with persistent storage
    (e.g. LUT_REGISTER.yaml or a database).
    """

    def __init__(self) -> None:
        self._registry: dict[str, FinexRecord] = {}

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def is_finalized(self, entity_id: str) -> bool:
        """Return ``True`` if the entity has been finalized."""
        return entity_id in self._registry

    def get_record(self, entity_id: str) -> FinexRecord | None:
        """Return the FINEX record for the entity, or ``None``."""
        return self._registry.get(entity_id)

    def list_all(self) -> list[FinexRecord]:
        """Return all FINEX records."""
        return list(self._registry.values())

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def finalize(
        self,
        entity_id: str,
        entity_scope: EntityScope,
        finex_phase: FinexPhase,
        reason: str,
        authority: str,
        mission: str | None = None,
        vision: str | None = None,
        plan_summary: str | None = None,
    ) -> FinexRecord:
        """Mark an entity as permanently finalized.

        Raises ``ValueError`` if the entity is already finalized.
        """
        if self.is_finalized(entity_id):
            raise ValueError(
                f"Entity '{entity_id}' is already finalized. "
                "No further modifications are allowed."
            )

        record = FinexRecord(
            entity_id=entity_id,
            entity_scope=entity_scope,
            finex_phase=finex_phase,
            reason=reason,
            authority=authority,
            finalized_at=datetime.now(timezone.utc),
            mission=mission,
            vision=vision,
            plan_summary=plan_summary,
        )
        self._registry[entity_id] = record
        return record

    # ------------------------------------------------------------------
    # Guard (used by other routes to reject requests)
    # ------------------------------------------------------------------

    def enforce(self, entity_id: str) -> None:
        """Raise ``ValueError`` if the entity is finalized.

        Call this from ``/ingest`` and ``/transform`` routes to block
        requests against finalized entities.
        """
        record = self.get_record(entity_id)
        if record is not None:
            raise ValueError(
                f"Entity '{entity_id}' was finalized on "
                f"{record.finalized_at.isoformat()} "
                f"(phase: {record.finex_phase}, reason: {record.reason}). "
                "No further requests are permitted."
            )
