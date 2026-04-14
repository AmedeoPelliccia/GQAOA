"""Tests for AMEDEO-ITBPFO API routes."""

from __future__ import annotations

import io
import json

import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


# ---------------------------------------------------------------------------
# /health
# ---------------------------------------------------------------------------


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["model"] == "AMEDEO-ITBPFO-001"


# ---------------------------------------------------------------------------
# /
# ---------------------------------------------------------------------------


def test_root_ok():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "AMEDEO-ITBPFO" in data["api"]


# ---------------------------------------------------------------------------
# POST /ingest
# ---------------------------------------------------------------------------


def _make_file(content: str = "hello world", filename: str = "test.txt") -> tuple:
    return ("file", (filename, io.BytesIO(content.encode()), "text/plain"))


def test_ingest_valid_text():
    metadata = json.dumps({"source_type": "text", "genesis_source": "GENESIS/O-KNOT"})
    response = client.post(
        "/ingest",
        files=[_make_file()],
        data={"metadata": metadata},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "accepted"
    assert data["source_type"] == "text"
    assert data["genesis_source"] == "GENESIS/O-KNOT"
    assert "ingestion_id" in data


def test_ingest_valid_yaml():
    metadata = json.dumps({"source_type": "yaml"})
    response = client.post(
        "/ingest",
        files=[_make_file("key: value", "data.yaml")],
        data={"metadata": metadata},
    )
    assert response.status_code == 200
    assert response.json()["source_type"] == "yaml"


def test_ingest_valid_csv():
    metadata = json.dumps({"source_type": "csv"})
    response = client.post(
        "/ingest",
        files=[_make_file("a,b\n1,2", "data.csv")],
        data={"metadata": metadata},
    )
    assert response.status_code == 200
    assert response.json()["source_type"] == "csv"


def test_ingest_rejects_unsupported_type():
    metadata = json.dumps({"source_type": "video"})
    response = client.post(
        "/ingest",
        files=[_make_file("data", "clip.mp4")],
        data={"metadata": metadata},
    )
    assert response.status_code == 422
    assert "Unsupported source_type" in response.json()["detail"]


def test_ingest_invalid_metadata_json():
    response = client.post(
        "/ingest",
        files=[_make_file()],
        data={"metadata": "not-json"},
    )
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# POST /transform
# ---------------------------------------------------------------------------


def test_transform_with_raw_data():
    response = client.post(
        "/transform",
        json={"raw_data": "sample text payload", "source_type": "text"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "transformed"
    assert "ssot_path" in data
    assert "derivation" in data


def test_transform_with_ingestion_id():
    response = client.post(
        "/transform",
        json={"ingestion_id": "00000000-0000-0000-0000-000000000001", "source_type": "yaml"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "transformed"


def test_transform_missing_input():
    response = client.post("/transform", json={})
    assert response.status_code == 422


def test_transform_ssot_path_format():
    response = client.post(
        "/transform",
        json={"raw_data": "x", "source_type": "text", "uta_chapter": "021", "lc_phase": "LC04"},
    )
    assert response.status_code == 200
    assert response.json()["ssot_path"] == "SSOT/LC04/021/_executions/"


# ---------------------------------------------------------------------------
# POST /validate
# ---------------------------------------------------------------------------


def _valid_artifact() -> dict:
    import hashlib

    content = {"data": "test"}
    checksum = hashlib.sha256(str(content).encode()).hexdigest()
    return {
        "id": "ART-001",
        "type": "yaml",
        "revision": "1.0",
        "effective_date": "2026-04-14",
        "integrity": {"checksum": checksum, "algorithm": "sha256"},
        "source": "GENESIS/O-KNOT",
        "lifecycle_phase": "LC02",
        "opt_axis": "T",
        "content": content,
    }


def test_validate_valid_artifact():
    response = client.post("/validate", json={"artifact": _valid_artifact()})
    assert response.status_code == 200
    data = response.json()
    assert data["overall"] is True
    checks = {c["check"]: c["passed"] for c in data["checks"]}
    assert checks["metadata"] is True
    assert checks["checksum"] is True


def test_validate_missing_metadata_field():
    artifact = _valid_artifact()
    del artifact["revision"]
    response = client.post("/validate", json={"artifact": artifact})
    assert response.status_code == 200
    data = response.json()
    assert data["overall"] is False
    checks = {c["check"]: c["passed"] for c in data["checks"]}
    assert checks["metadata"] is False


def test_validate_bad_checksum():
    artifact = _valid_artifact()
    artifact["integrity"]["checksum"] = "0" * 64
    response = client.post("/validate", json={"artifact": artifact})
    assert response.status_code == 200
    data = response.json()
    checks = {c["check"]: c["passed"] for c in data["checks"]}
    assert checks["checksum"] is False
