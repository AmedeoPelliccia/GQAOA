# AMEDEO-ITBPFO — Backend + Frontend

**Model ID:** AMEDEO-ITBPFO-001  
**Version:** 1.0.0  
**Authority:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Parent Document:** GQAOA-UTA-SUPIA-001  
**Specification:** [GQAOA-UTA-AMEDEO-ITBPFO-001.yaml](../OPT-INS_FRAMEWORK/GQAOA-UTA-AMEDEO-ITBPFO-001.yaml)

---

## Architecture

```
┌──────────────────┐     ┌───────────────────────┐     ┌──────────────────────┐
│  FRONTEND (UI)   │────▶│   BACKEND (FastAPI)   │────▶│    FINEX ENGINE      │
│  Next.js/React   │     │   Pipeline + Guard    │     │   (Seal & Lock)      │
└──────────────────┘     └───────────────────────┘     └──────────────────────┘
        │                          │                           │
        ▼                          ▼                           ▼
  Entity Tracker            State Machine               .finex Package (ZIP)
  Pipeline Progress         PENDING→INGESTED→           ├── payload.json
  Terminal Lock UI          TRANSFORMED→TERMINAL        ├── manifest.yaml
  Mission/Vision Dash       FINEX Guard                 ├── integrity.sha256
  .finex Download           SHA-256 Integrity           └── lock.json
```

### Pipeline State Machine

```
  PENDING ──► INGESTED ──► TRANSFORMED ──► TERMINAL (sealed)
    │            │              │               │
  /ingest      /ingest        /transform     /finex
  (create)     (advance)     (advance)       (seal)
```

Once an entity reaches **TERMINAL**, a cryptographically sealed `.finex` ZIP package is generated and **all further requests are permanently blocked** (HTTP 403).

---

## Overview

The **AMEDEO-ITBPFO** (Autonomous Multimodal Execution — Intergenerational Transformation to Best Processable Formatted Output) system provides:

1. **Backend (FastAPI)** — Pipeline orchestration, schema validation, state management, FINEX terminal sealing
2. **Frontend (Next.js/React)** — Entity tracking, pipeline progress visualization, terminal lock UI, `.finex` download

It ingests multimodal inputs (text, sensor data, logs, images, YAML, CSV) from GENESIS knowledge nodes, transforms them through lifecycle-aware validation, and outputs versioned, structured artifacts to the SSOT and publication layers.

---

## Directory Structure

```
AMEDEO-ITBPFO/
├── README.md
├── requirements.txt
├── Dockerfile
├── api/
│   ├── __init__.py
│   ├── main.py                  ← FastAPI app entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ingest.py            ← POST /ingest (+ pipeline: PENDING → INGESTED)
│   │   ├── transform.py         ← POST /transform (+ pipeline: INGESTED → TRANSFORMED)
│   │   ├── validate.py          ← POST /validate
│   │   └── finex.py             ← POST/GET /finex/* (terminal sealing + download)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── finex.py             ← PipelineState, FinexRecord, FinexManifest, LockFile
│   │   ├── lutndr.py            ← LUTNDR Pydantic v2 models
│   │   ├── applicability.py     ← S1000D applicability models
│   │   └── metadata.py          ← Artifact metadata models
│   └── services/
│       ├── __init__.py
│       ├── finex.py             ← FinexService (state machine + .finex builder)
│       ├── transformer.py       ← TransformerService
│       ├── validator.py         ← ValidatorService
│       └── registry.py          ← RegistryService (LUT)
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_routes.py
│   └── test_finex.py            ← 37 FINEX-specific tests (pipeline + package + e2e)
└── frontend/
    ├── package.json
    ├── tsconfig.json
    ├── next.config.mjs
    ├── postcss.config.mjs
    └── src/
        ├── app/
        │   ├── globals.css
        │   ├── layout.tsx
        │   └── page.tsx             ← Main dashboard page
        ├── components/
        │   ├── PipelineDashboard.tsx ← Pipeline progress tracker
        │   ├── TerminalGuard.tsx     ← Terminal-state lock overlay
        │   └── MissionVisionCard.tsx ← Mission/Vision/Plan display
        └── lib/
            └── api.ts               ← API client functions
```

---

## Installation

### Backend

```bash
cd AMEDEO-ITBPFO
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Frontend

```bash
cd AMEDEO-ITBPFO/frontend
npm install
```

---

## Running

### Backend

```bash
uvicorn api.main:app --reload --port 8000
```

API at `http://localhost:8000`, docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm run dev
```

Dashboard at `http://localhost:3000`. API requests are proxied to `http://localhost:8000`.

### With Docker (backend only)

```bash
docker build -t amedeo-itbpfo:latest .
docker run -p 8000:8000 amedeo-itbpfo:latest
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/` | API info with all endpoints |
| `POST` | `/ingest` | Ingest multimodal input (pipeline: PENDING → INGESTED) |
| `POST` | `/transform` | Transform data to SSOT format (pipeline: INGESTED → TRANSFORMED) |
| `POST` | `/validate` | Validate artifact against STD_Metadata-Schema |
| `POST` | `/finex` | Finalize entity → TERMINAL + generate `.finex` package |
| `POST` | `/finex/finalize/{id}` | Finalize via pipeline (requires TRANSFORMED state) |
| `GET` | `/finex` | List all finalized entities |
| `GET` | `/finex/status/{id}` | Full pipeline + finex status |
| `GET` | `/finex/{id}` | Check finalization status |
| `GET` | `/finex/{id}/download` | Download sealed `.finex` ZIP package |

### FINEX Terminal Lock

When an entity is finalized:
- A `.finex` ZIP package is generated (payload + manifest + SHA-256 integrity + lock)
- All subsequent `/ingest` and `/transform` requests with that `entity_id` return **HTTP 403**
- The lock is **irreversible** — the entity cannot be un-finalized

### `.finex` Package Structure

```
<entity_id>.finex (ZIP)
├── payload.json        ← Transformed data payload
├── manifest.yaml       ← Metadata + mission/vision/plan + compliance refs
├── integrity.sha256    ← SHA-256 hash of payload
└── lock.json           ← Terminal lock flags (all true)
```

---

## Running Tests

```bash
cd AMEDEO-ITBPFO
pytest tests/ -v
```

All 69 tests cover:
- LUTNDR models and state/substate validation (19 tests)
- API routes: ingest, transform, validate (14 tests)
- FINEX: models, pipeline state machine, `.finex` package generation, route enforcement, end-to-end (36 tests)

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
| FINEX terminal lock | `FinexService` + `.finex` package + pipeline state machine |
| Mission/Vision/Plan | Captured in `manifest.yaml` inside `.finex` package |

---

## Governance

- **Approval authority:** GAIA-QAO Architecture Board (Q-DATAGOV)
- **Change process:** RFC → review → merge into versioned release
- **Versioning:** Semantic versioning (MAJOR.MINOR.PATCH)
- **FINEX policy:** Terminal state is irreversible; `.finex` packages are immutable audit artifacts
