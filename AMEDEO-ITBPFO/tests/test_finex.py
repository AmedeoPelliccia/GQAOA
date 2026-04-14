"""Tests for FINEX (Final Execution) models, service, and routes."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from api.main import app
from api.models.finex import EntityScope, FinexPhase, FinexRecord
from api.routes.finex import finex_service
from api.services.finex import FinexService

client = TestClient(app)


# ---------------------------------------------------------------------------
# FinexRecord model tests
# ---------------------------------------------------------------------------


def test_finex_record_valid():
    from datetime import datetime, timezone

    record = FinexRecord(
        entity_id="ORG-001",
        entity_scope=EntityScope.ORGANIZATION,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Mission completed",
        authority="GAIA-QAO Architecture Board",
        finalized_at=datetime.now(timezone.utc),
    )
    assert record.entity_id == "ORG-001"
    assert record.entity_scope == EntityScope.ORGANIZATION.value


def test_finex_record_empty_entity_id():
    from datetime import datetime, timezone

    with pytest.raises(ValueError, match="entity_id must not be empty"):
        FinexRecord(
            entity_id="  ",
            entity_scope=EntityScope.PROGRAM,
            finex_phase=FinexPhase.LC14_DECOMMISSION,
            reason="Done",
            authority="Admin",
            finalized_at=datetime.now(timezone.utc),
        )


def test_finex_record_empty_reason():
    from datetime import datetime, timezone

    with pytest.raises(ValueError, match="reason must not be empty"):
        FinexRecord(
            entity_id="PROG-001",
            entity_scope=EntityScope.PROGRAM,
            finex_phase=FinexPhase.LC14_DECOMMISSION,
            reason="  ",
            authority="Admin",
            finalized_at=datetime.now(timezone.utc),
        )


def test_finex_record_with_mission_vision():
    from datetime import datetime, timezone

    record = FinexRecord(
        entity_id="ENT-001",
        entity_scope=EntityScope.ENTERPRISE,
        finex_phase=FinexPhase.CUSTOM,
        reason="Strategic pivot",
        authority="Board of Directors",
        finalized_at=datetime.now(timezone.utc),
        mission="Original mission statement",
        vision="Original vision statement",
        plan_summary="Transition completed per plan v3.2",
    )
    assert record.mission == "Original mission statement"
    assert record.plan_summary == "Transition completed per plan v3.2"


# ---------------------------------------------------------------------------
# FinexService tests
# ---------------------------------------------------------------------------


def test_finex_service_finalize_and_query():
    svc = FinexService()
    assert not svc.is_finalized("TEST-001")
    svc.finalize(
        entity_id="TEST-001",
        entity_scope=EntityScope.REPOSITORY,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Archived",
        authority="Admin",
    )
    assert svc.is_finalized("TEST-001")
    record = svc.get_record("TEST-001")
    assert record is not None
    assert record.entity_scope == EntityScope.REPOSITORY.value


def test_finex_service_double_finalize_raises():
    svc = FinexService()
    svc.finalize(
        entity_id="DUP-001",
        entity_scope=EntityScope.PROGRAM,
        finex_phase=FinexPhase.CUSTOM,
        reason="Done",
        authority="Admin",
    )
    with pytest.raises(ValueError, match="already finalized"):
        svc.finalize(
            entity_id="DUP-001",
            entity_scope=EntityScope.PROGRAM,
            finex_phase=FinexPhase.CUSTOM,
            reason="Again",
            authority="Admin",
        )


def test_finex_service_enforce_blocks_finalized():
    svc = FinexService()
    svc.finalize(
        entity_id="BLOCK-001",
        entity_scope=EntityScope.COMPANY,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Closed",
        authority="CEO",
    )
    with pytest.raises(ValueError, match="No further requests are permitted"):
        svc.enforce("BLOCK-001")


def test_finex_service_enforce_allows_non_finalized():
    svc = FinexService()
    # Should not raise
    svc.enforce("OPEN-001")


def test_finex_service_list_all():
    svc = FinexService()
    assert svc.list_all() == []
    svc.finalize(
        entity_id="A", entity_scope=EntityScope.ORGANIZATION,
        finex_phase=FinexPhase.LC14_DECOMMISSION, reason="Done", authority="X",
    )
    svc.finalize(
        entity_id="B", entity_scope=EntityScope.REPOSITORY,
        finex_phase=FinexPhase.CUSTOM, reason="Archived", authority="Y",
    )
    assert len(svc.list_all()) == 2


# ---------------------------------------------------------------------------
# Route tests — POST /finex
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _clear_finex_registry():
    """Clear the global FINEX registry before each test."""
    finex_service._registry.clear()
    yield
    finex_service._registry.clear()


def test_finex_post_creates_record():
    response = client.post("/finex", json={
        "entity_id": "ORG-ROUTE-001",
        "entity_scope": "organization",
        "finex_phase": "LC14_DECOMMISSION",
        "reason": "Mission completed",
        "authority": "Architecture Board",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["entity_id"] == "ORG-ROUTE-001"
    assert data["finalized_at"]


def test_finex_post_duplicate_returns_409():
    client.post("/finex", json={
        "entity_id": "DUP-ROUTE-001",
        "entity_scope": "program",
        "reason": "Done",
        "authority": "Admin",
    })
    response = client.post("/finex", json={
        "entity_id": "DUP-ROUTE-001",
        "entity_scope": "program",
        "reason": "Again",
        "authority": "Admin",
    })
    assert response.status_code == 409
    assert "already finalized" in response.json()["detail"]


def test_finex_get_status_not_finalized():
    response = client.get("/finex/UNKNOWN-001")
    assert response.status_code == 200
    data = response.json()
    assert data["finalized"] is False
    assert data["record"] is None


def test_finex_get_status_finalized():
    client.post("/finex", json={
        "entity_id": "STATUS-001",
        "entity_scope": "enterprise",
        "reason": "Sunset",
        "authority": "Board",
    })
    response = client.get("/finex/STATUS-001")
    assert response.status_code == 200
    data = response.json()
    assert data["finalized"] is True
    assert data["record"]["entity_scope"] == "enterprise"


def test_finex_list_empty():
    response = client.get("/finex")
    assert response.status_code == 200
    assert response.json() == []


def test_finex_list_populated():
    client.post("/finex", json={
        "entity_id": "LIST-001",
        "entity_scope": "company",
        "reason": "Closed",
        "authority": "CEO",
    })
    response = client.get("/finex")
    assert response.status_code == 200
    assert len(response.json()) == 1


# ---------------------------------------------------------------------------
# FINEX enforcement in /ingest and /transform
# ---------------------------------------------------------------------------


def test_ingest_blocked_by_finex():
    import io
    import json as json_mod

    # Finalize the entity first
    client.post("/finex", json={
        "entity_id": "FINEX-INGEST-001",
        "entity_scope": "repository",
        "reason": "Archived",
        "authority": "Admin",
    })

    # Attempt to ingest with the finalized entity_id
    metadata = json_mod.dumps({
        "source_type": "text",
        "entity_id": "FINEX-INGEST-001",
    })
    response = client.post(
        "/ingest",
        files=[("file", ("test.txt", io.BytesIO(b"data"), "text/plain"))],
        data={"metadata": metadata},
    )
    assert response.status_code == 403
    assert "No further requests are permitted" in response.json()["detail"]


def test_ingest_allowed_without_entity_id():
    import io
    import json as json_mod

    metadata = json_mod.dumps({"source_type": "text"})
    response = client.post(
        "/ingest",
        files=[("file", ("test.txt", io.BytesIO(b"data"), "text/plain"))],
        data={"metadata": metadata},
    )
    assert response.status_code == 200


def test_transform_blocked_by_finex():
    # Finalize the entity first
    client.post("/finex", json={
        "entity_id": "FINEX-TRANSFORM-001",
        "entity_scope": "program",
        "reason": "Completed",
        "authority": "PM",
    })

    # Attempt to transform with the finalized entity_id
    response = client.post("/transform", json={
        "raw_data": "some data",
        "entity_id": "FINEX-TRANSFORM-001",
    })
    assert response.status_code == 403
    assert "No further requests are permitted" in response.json()["detail"]


def test_transform_allowed_without_entity_id():
    response = client.post("/transform", json={"raw_data": "some data"})
    assert response.status_code == 200
