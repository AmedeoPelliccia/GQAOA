# AMEDEO-ITBPFO — FastAPI Backend

**Model ID:** AMEDEO-ITBPFO-001  
**Version:** 1.0.0  
**Authority:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Parent Document:** GQAOA-UTA-SUPIA-001  
**Specification:** [GQAOA-UTA-AMEDEO-ITBPFO-001.yaml](../OPT-INS_FRAMEWORK/GQAOA-UTA-AMEDEO-ITBPFO-001.yaml)

---

## Overview

The **AMEDEO-ITBPFO** (Autonomous Multimodal Execution — Intergenerational Transformation to Best Processable Formatted Output) backend provides a FastAPI service that implements the GENESIS → SSOT transformation pipeline defined in the OPT-INS framework.

It ingests multimodal inputs (text, sensor data, logs, images, YAML, CSV) from GENESIS knowledge nodes, transforms them through lifecycle-aware validation, and outputs versioned, structured artifacts to the SSOT and publication layers.

### Pipeline

```
GENESIS/O-KNOT ──┐
GENESIS/Y-KNOT ──┼──► [INGEST] ──► [TRANSFORM] ──► [VALIDATE] ──► SSOT/LCxx/_executions/
GENESIS/KNOT   ──┘                                                  PUB/AMM/CSDB/DM/
```

---

## Directory Structure

```
AMEDEO-ITBPFO/
├── README.md
├── requirements.txt
├── Dockerfile
├── api/
│   ├── __init__.py
│   ├── main.py              ← FastAPI app entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ingest.py        ← POST /ingest
│   │   ├── transform.py     ← POST /transform
│   │   └── validate.py      ← POST /validate
│   ├── models/
│   │   ├── __init__.py
│   │   ├── lutndr.py        ← LUTNDR Pydantic v2 models
│   │   ├── applicability.py ← S1000D applicability models
│   │   └── metadata.py      ← Artifact metadata models
│   └── services/
│       ├── __init__.py
│       ├── transformer.py   ← TransformerService
│       ├── validator.py     ← ValidatorService
│       └── registry.py      ← RegistryService (LUT)
└── tests/
    ├── __init__.py
    ├── test_models.py
    └── test_routes.py
```

---

## Installation

```bash
cd AMEDEO-ITBPFO
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the API

```bash
uvicorn api.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### With Docker

```bash
docker build -t amedeo-itbpfo:latest .
docker run -p 8000:8000 amedeo-itbpfo:latest
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/` | API info |
| `POST` | `/ingest` | Ingest multimodal input (file + metadata) |
| `POST` | `/transform` | Transform ingested data to SSOT format |
| `POST` | `/validate` | Validate artifact against STD_Metadata-Schema |

### POST /ingest

Accepts a multipart form with:
- `file`: the input artifact (text, sensor_data, logs, images, yaml, csv)
- `metadata`: JSON string with `source_type`, `genesis_source`, and optional fields

Returns an ingestion receipt with UUID, timestamp, and GENESIS/O-KNOT source mapping.

### POST /transform

Accepts JSON body with `ingestion_id` (or `raw_data` + `source_type`). Returns a structured SSOT-formatted artifact with `_derivation.yaml` metadata.

### POST /validate

Accepts a JSON artifact. Returns a validation report with pass/fail per check: metadata completeness, checksum integrity, LUTNDR state validity, applicability expression syntax.

---

## Running Tests

```bash
pytest tests/ -v
```

---

## OPT-INS Framework Alignment

| Concept | Implementation |
|---------|---------------|
| GENESIS/O-KNOT | `source` field in ingestion receipt |
| SSOT/LCxx | `ssot_path` computed by `TransformerService.map_to_ssot_path()` |
| `_derivation.yaml` | `DerivationMetadata` model + `TransformerService.generate_metadata()` |
| LUTNDR states | `TechState` / `TechSubState` enums in `api/models/lutndr.py` |
| S1000D applicability | `ApplicabilityExpression` in `api/models/applicability.py` |
| STD_Metadata-Schema | `ValidatorService.validate_metadata()` |

---

## Governance

- **Approval authority:** GAIA-QAO Architecture Board (Q-DATAGOV)
- **Change process:** RFC → review → merge into versioned release
- **Versioning:** Semantic versioning (MAJOR.MINOR.PATCH)
