from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import finex, ingest, transform, validate

app = FastAPI(
    title="AMEDEO-ITBPFO API",
    description=(
        "Autonomous Multimodal Execution — Intergenerational Transformation to Best "
        "Processable Formatted Output. Implements the GENESIS → SSOT transformation "
        "pipeline as defined in GQAOA-UTA-AMEDEO-ITBPFO-001."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router)
app.include_router(transform.router)
app.include_router(validate.router)
app.include_router(finex.router)


@app.get("/health", tags=["system"])
def health_check() -> dict:
    """Return API health status."""
    return {"status": "ok", "model": "AMEDEO-ITBPFO-001", "version": "1.0.0"}


@app.get("/", tags=["system"])
def root() -> dict:
    """Return API info."""
    return {
        "api": "AMEDEO-ITBPFO",
        "version": "1.0.0",
        "description": (
            "Autonomous Multimodal Execution — Intergenerational Transformation "
            "to Best Processable Formatted Output"
        ),
        "endpoints": ["/health", "/ingest", "/transform", "/validate", "/finex"],
        "docs": "/docs",
    }
