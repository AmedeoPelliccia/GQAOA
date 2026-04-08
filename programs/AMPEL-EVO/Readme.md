# AMPEL-EVO — AM.PEL Quantum-Enhanced Aerospace Astrophysics Extension

**Program:** AMPEL-EVO (AM.PEL Evolution)  
**Status:** Production-Ready Specification  
**Domain:** Cross-domain (Quantum / Space / Aerospace Data)

## Overview

AMPEL-EVO houses the artifacts for the **AM.PEL v2.0** quantum-augmented data processing pipeline — an evolution of the PapaLaiked AM.PEL baseline extending the core framework into aerospace astrophysics and quantum-accelerated analytics.

## Documents

| Document | Description | Version |
|---|---|---|
| [AMPEL-EVO-2026-04-05-PAPALAIKED-V2.md](./AMPEL-EVO-2026-04-05-PAPALAIKED-V2.md) | Full production-ready specification for AM.PEL v2.0 | 2.0 |

## Key Capabilities

- **Quantum ML** — VQE/QML kernels on 50+ logical qubits for alert classification and anomaly detection
- **Aerospace Integration** — Native CCSDS telemetry, SSA catalogs, radiation-hardened edge deployment
- **Post-Quantum Security** — Kyber-1024 provenance ledger, QKD inter-satellite simulation
- **Standards Compliance** — DO-178C, ECSS-E-ST-40C, NASA SP-7009, NIST SP 800-53

## Optional Integrations (OPT-INS)

Space-domain capabilities are managed through the [OPT-INS_FRAMEWORK](../../OPT-INS_FRAMEWORK/Readme.md). Recommended profiles:

| Profile | Use-case | Reference |
|---|---|---|
| `SSA_FULL` | Full SSA + CCSDS + ground station | [S-SPACE §4](../../OPT-INS_FRAMEWORK/S-SPACE-SPECIFICS.md#4-integration-profiles) |
| `EARTH_PROTECT` | Bologna EPC mission profile | [S-SPACE §6.1](../../OPT-INS_FRAMEWORK/S-SPACE-SPECIFICS.md#61-bologna-earth-protection-center) |
| `NAPLES_QH` | Naples Quantum Hub sensor streams | [S-SPACE §6.2](../../OPT-INS_FRAMEWORK/S-SPACE-SPECIFICS.md#62-naples-quantum-hub) |
| `QKD_SECURE_LINK` | Quantum-secured ISL for GAIA-SAT-02-QKD | [S-SPACE §5.4](../../OPT-INS_FRAMEWORK/S-SPACE-SPECIFICS.md#54-quantum-key-distribution-qkd-inter-satellite-link) |

## Hub Alignment

| Facility | Role in AM.PEL v2.0 |
|---|---|
| [Naples Quantum Hub](../../README.md#naples-quantum-hub) | Quantum propulsion sensor streams; QML kernel development |
| [Bologna Earth Protection Center](../../README.md#bologna-earth-protection-center) | SSA data pipelines; observation satellite telemetry; catastrophe prevention analytics |

## ALICE–BOB Traceability

| ALICE | BOB DT | CHARLIE_T |
|---|---|---|
| ALICE-AMPEL-EVO-PIPELINE | BOB-DT-AMPEL-EVO-PIPELINE | CHARLIE-T-AMPEL-EVO-PIPELINE |
