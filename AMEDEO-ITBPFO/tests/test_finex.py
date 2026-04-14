"""Tests for FINEX (Final Execution) engine — models, service, routes, .finex package."""

from __future__ import annotations

import json
import zipfile

import io
import pytest
from fastapi.testclient import TestClient

from api.main import app
from api.models.finex import (
    EntityScope,
    FinexManifest,
    FinexPhase,
    FinexRecord,
    LockFile,
    PIPELINE_TRANSITIONS,
    PipelineEntry,
    PipelineState,
)
from api.routes.finex import finex_service
from api.services.finex import FinexService

client = TestClient(app)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _clear_finex_registry():
    """Clear the global FINEX registry + pipeline before each test."""
    finex_service._registry.clear()
    finex_service._pipeline.clear()
    finex_service._package_store.clear()
    yield
    finex_service._registry.clear()
    finex_service._pipeline.clear()
    finex_service._package_store.clear()


# ---------------------------------------------------------------------------
# PipelineState enum & transitions
# ---------------------------------------------------------------------------


def test_pipeline_state_values():
    assert set(PipelineState) == {
        PipelineState.PENDING,
        PipelineState.INGESTED,
        PipelineState.TRANSFORMED,
        PipelineState.TERMINAL,
    }


def test_pipeline_transitions_terminal_is_absorbing():
    assert PIPELINE_TRANSITIONS[PipelineState.TERMINAL] == set()


def test_pipeline_transitions_complete_chain():
    """PENDING → INGESTED → TRANSFORMED → TERMINAL must be a valid path."""
    assert PipelineState.INGESTED in PIPELINE_TRANSITIONS[PipelineState.PENDING]
    assert PipelineState.TRANSFORMED in PIPELINE_TRANSITIONS[PipelineState.INGESTED]
    assert PipelineState.TERMINAL in PIPELINE_TRANSITIONS[PipelineState.TRANSFORMED]


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
    assert record.pipeline_state == PipelineState.TERMINAL.value


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
        compliance_refs=["ISO_27001", "ATA_00-GENERAL"],
    )
    assert record.mission == "Original mission statement"
    assert record.plan_summary == "Transition completed per plan v3.2"
    assert len(record.compliance_refs) == 2


def test_finex_record_compliance_refs_default():
    from datetime import datetime, timezone

    record = FinexRecord(
        entity_id="X-001",
        entity_scope=EntityScope.REPOSITORY,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Done",
        authority="Admin",
        finalized_at=datetime.now(timezone.utc),
    )
    assert record.compliance_refs == []


# ---------------------------------------------------------------------------
# PipelineEntry & LockFile / FinexManifest models
# ---------------------------------------------------------------------------


def test_pipeline_entry_defaults():
    entry = PipelineEntry(entity_id="PE-001", state=PipelineState.PENDING)
    assert entry.state == PipelineState.PENDING.value
    assert entry.ingestion_id is None


def test_lock_file_defaults():
    lock = LockFile()
    assert lock.terminal is True
    assert lock.block_downstream is True
    assert lock.block_ingestion is True
    assert lock.block_transformation is True
    assert lock.block_stock_requests is True


def test_finex_manifest_defaults():
    manifest = FinexManifest(id="M-001", effective_date="2026-04-14T00:00:00Z", entity_scope=EntityScope.PROGRAM)
    assert manifest.type == "finex_terminal"
    assert manifest.terminal_lock is True


# ---------------------------------------------------------------------------
# FinexService — pipeline state machine
# ---------------------------------------------------------------------------


def test_service_pipeline_create_and_advance():
    svc = FinexService()
    entry = svc.get_or_create_pipeline("SM-001")
    assert entry.state == PipelineState.PENDING.value

    svc.advance_pipeline("SM-001", PipelineState.INGESTED, ingestion_id="ING-X")
    assert entry.state == PipelineState.INGESTED.value
    assert entry.ingestion_id == "ING-X"

    svc.advance_pipeline("SM-001", PipelineState.TRANSFORMED, transform_artifact_id="ART-Y")
    assert entry.state == PipelineState.TRANSFORMED.value


def test_service_pipeline_illegal_transition():
    svc = FinexService()
    svc.get_or_create_pipeline("SM-002")
    with pytest.raises(ValueError, match="Illegal pipeline transition"):
        svc.advance_pipeline("SM-002", PipelineState.TRANSFORMED)


def test_service_pipeline_terminal_no_outbound():
    svc = FinexService()
    svc.get_or_create_pipeline("SM-003")
    svc.advance_pipeline("SM-003", PipelineState.INGESTED)
    svc.advance_pipeline("SM-003", PipelineState.TRANSFORMED)
    svc.finalize(
        entity_id="SM-003",
        entity_scope=EntityScope.PROGRAM,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Done",
        authority="Admin",
    )
    entry = svc.get_pipeline("SM-003")
    assert entry.state == PipelineState.TERMINAL.value


# ---------------------------------------------------------------------------
# FinexService — finalize + .finex package
# ---------------------------------------------------------------------------


def test_service_finalize_generates_package():
    svc = FinexService()
    record = svc.finalize(
        entity_id="PKG-001",
        entity_scope=EntityScope.ORGANIZATION,
        finex_phase=FinexPhase.LC14_DECOMMISSION,
        reason="Mission completed",
        authority="Board",
        mission="Deliver auditable artifacts",
        vision="Zero-ambiguity traceability",
        compliance_refs=["ISO_27001"],
    )
    assert record.finex_package_path == "PKG-001.finex"

    # Check package exists and is a valid ZIP
    data = svc.get_package_bytes("PKG-001")
    assert data is not None
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        names = zf.namelist()
        assert "payload.json" in names
        assert "manifest.yaml" in names
        assert "integrity.sha256" in names
        assert "lock.json" in names

        # Verify lock.json
        lock_data = json.loads(zf.read("lock.json"))
        assert lock_data["terminal"] is True
        assert lock_data["block_downstream"] is True

        # Verify integrity contains sha256 hash
        integrity = zf.read("integrity.sha256").decode()
        assert integrity.startswith("sha256:")


def test_service_double_finalize_raises():
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


def test_service_enforce_blocks_finalized():
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


def test_service_enforce_allows_non_finalized():
    svc = FinexService()
    svc.enforce("OPEN-001")  # Should not raise


def test_service_list_all():
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


def test_finex_post_creates_record():
    response = client.post("/finex", json={
        "entity_id": "ORG-ROUTE-001",
        "entity_scope": "organization",
        "finex_phase": "LC14_DECOMMISSION",
        "reason": "Mission completed",
        "authority": "Architecture Board",
        "compliance_refs": ["ISO_27001"],
    })
    assert response.status_code == 200
    data = response.json()
    assert data["entity_id"] == "ORG-ROUTE-001"
    assert data["finalized_at"]
    assert data["pipeline_state"] == "TERMINAL"
    assert data["finex_package_path"] == "ORG-ROUTE-001.finex"


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


# ---------------------------------------------------------------------------
# Route tests — GET /finex, /finex/{id}, /finex/status/{id}
# ---------------------------------------------------------------------------


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
    assert data["pipeline_state"] == "TERMINAL"


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


def test_finex_pipeline_status_tracked():
    """Pipeline status tracks entity from ingestion through finalization."""
    # Check unknown entity
    response = client.get("/finex/status/PIPE-001")
    assert response.status_code == 200
    assert response.json()["state"] == "UNKNOWN"

    # Ingest with entity_id → PENDING → INGESTED
    import json as json_mod
    metadata = json_mod.dumps({"source_type": "text", "entity_id": "PIPE-001", "mission": "Test mission"})
    client.post(
        "/ingest",
        files=[("file", ("test.txt", io.BytesIO(b"data"), "text/plain"))],
        data={"metadata": metadata},
    )
    response = client.get("/finex/status/PIPE-001")
    assert response.json()["state"] == "INGESTED"
    assert response.json()["mission"] == "Test mission"

    # Transform → TRANSFORMED
    client.post("/transform", json={"raw_data": "data", "entity_id": "PIPE-001"})
    response = client.get("/finex/status/PIPE-001")
    assert response.json()["state"] == "TRANSFORMED"

    # Finalize → TERMINAL
    client.post("/finex", json={
        "entity_id": "PIPE-001",
        "entity_scope": "program",
        "reason": "Complete",
        "authority": "PM",
    })
    response = client.get("/finex/status/PIPE-001")
    assert response.json()["state"] == "TERMINAL"
    assert response.json()["finalized"] is True


# ---------------------------------------------------------------------------
# Route tests — POST /finex/finalize/{entity_id}
# ---------------------------------------------------------------------------


def test_finalize_by_pipeline_requires_transformed():
    """Pipeline finalize endpoint rejects non-TRANSFORMED entities."""
    # Create pipeline and leave at PENDING
    finex_service.get_or_create_pipeline("FBP-001")
    response = client.post("/finex/finalize/FBP-001", json={
        "entity_id": "FBP-001",
        "entity_scope": "program",
        "reason": "Early",
        "authority": "PM",
    })
    assert response.status_code == 400
    assert "Must be TRANSFORMED" in response.json()["detail"]


def test_finalize_by_pipeline_success():
    """Full pipeline → finalize flow."""
    svc = finex_service
    svc.get_or_create_pipeline("FBP-002")
    svc.advance_pipeline("FBP-002", PipelineState.INGESTED)
    svc.advance_pipeline("FBP-002", PipelineState.TRANSFORMED, payload={"result": "ok"})

    response = client.post("/finex/finalize/FBP-002", json={
        "entity_id": "FBP-002",
        "entity_scope": "repository",
        "reason": "Archived",
        "authority": "Admin",
        "mission": "Deliver artifacts",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["pipeline_state"] == "TERMINAL"
    assert data["finex_package_path"] == "FBP-002.finex"


def test_finalize_by_pipeline_404():
    response = client.post("/finex/finalize/GHOST-001", json={
        "entity_id": "GHOST-001",
        "entity_scope": "program",
        "reason": "?",
        "authority": "?",
    })
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# Route tests — GET /finex/{entity_id}/download
# ---------------------------------------------------------------------------


def test_download_finex_package():
    client.post("/finex", json={
        "entity_id": "DL-001",
        "entity_scope": "organization",
        "reason": "Mission done",
        "authority": "Board",
    })
    response = client.get("/finex/DL-001/download")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    assert "DL-001.finex" in response.headers["content-disposition"]

    # Validate ZIP contents
    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        assert "payload.json" in zf.namelist()
        assert "manifest.yaml" in zf.namelist()
        assert "lock.json" in zf.namelist()
        assert "integrity.sha256" in zf.namelist()


def test_download_finex_package_not_found():
    response = client.get("/finex/NOPE-001/download")
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# FINEX enforcement in /ingest and /transform
# ---------------------------------------------------------------------------


def test_ingest_blocked_by_finex():
    import json as json_mod

    client.post("/finex", json={
        "entity_id": "FINEX-INGEST-001",
        "entity_scope": "repository",
        "reason": "Archived",
        "authority": "Admin",
    })

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
    import json as json_mod

    metadata = json_mod.dumps({"source_type": "text"})
    response = client.post(
        "/ingest",
        files=[("file", ("test.txt", io.BytesIO(b"data"), "text/plain"))],
        data={"metadata": metadata},
    )
    assert response.status_code == 200


def test_transform_blocked_by_finex():
    client.post("/finex", json={
        "entity_id": "FINEX-TRANSFORM-001",
        "entity_scope": "program",
        "reason": "Completed",
        "authority": "PM",
    })

    response = client.post("/transform", json={
        "raw_data": "some data",
        "entity_id": "FINEX-TRANSFORM-001",
    })
    assert response.status_code == 403
    assert "No further requests are permitted" in response.json()["detail"]


def test_transform_allowed_without_entity_id():
    response = client.post("/transform", json={"raw_data": "some data"})
    assert response.status_code == 200


# ---------------------------------------------------------------------------
# Full end-to-end pipeline test
# ---------------------------------------------------------------------------


def test_e2e_pipeline_ingest_transform_finalize_lock():
    """End-to-end: ingest → transform → finalize → verify lock."""
    import json as json_mod

    entity = "E2E-001"

    # 1. Ingest
    metadata = json_mod.dumps({"source_type": "yaml", "entity_id": entity, "mission": "E2E test"})
    resp = client.post(
        "/ingest",
        files=[("file", ("data.yaml", io.BytesIO(b"key: value"), "text/plain"))],
        data={"metadata": metadata},
    )
    assert resp.status_code == 200
    assert resp.json()["pipeline_state"] == "INGESTED"

    # 2. Transform
    resp = client.post("/transform", json={"raw_data": "key: value", "entity_id": entity})
    assert resp.status_code == 200
    assert resp.json()["pipeline_state"] == "TRANSFORMED"

    # 3. Finalize
    resp = client.post("/finex/finalize/" + entity, json={
        "entity_id": entity,
        "entity_scope": "program",
        "reason": "E2E complete",
        "authority": "Test",
    })
    assert resp.status_code == 200
    assert resp.json()["pipeline_state"] == "TERMINAL"

    # 4. Verify lock — ingest blocked
    metadata = json_mod.dumps({"source_type": "text", "entity_id": entity})
    resp = client.post(
        "/ingest",
        files=[("file", ("test.txt", io.BytesIO(b"more"), "text/plain"))],
        data={"metadata": metadata},
    )
    assert resp.status_code == 403

    # 5. Verify lock — transform blocked
    resp = client.post("/transform", json={"raw_data": "more", "entity_id": entity})
    assert resp.status_code == 403

    # 6. Download .finex package
    resp = client.get(f"/finex/{entity}/download")
    assert resp.status_code == 200
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        lock_data = json.loads(zf.read("lock.json"))
        assert lock_data["terminal"] is True
