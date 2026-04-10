# OPT-INS_FRAMEWORK — 6-Axis Topology

**Framework ID:** GAIA-QAO-OPT-INS-FW-001  
**Programme:** AMPEL360 Q100 (AMPEL360-AIR-T) · GAIA-SPACE-LAUNCHER · SPACET Q10  
**Version:** OPT-INS v1.0  
**Date:** 11 April 2026  
**Status:** Active — Production Specification  
**Owner:** Q-DATAGOV Division / GAIA-QAO Architecture Board

---

## Overview

The **OPT-INS Framework** organises every chapter of the GAIA-QAO ADVENT lifecycle documentation into a **6-axis topology**. Each axis groups related ATA / S-chapters by engineering domain, enabling modular activation per programme and mission profile.

Integration is governed by a feature-flag mechanism so core programs (AM.PEL, AMPEL360, GAIA-SP) remain lean while domain-specific extensions are loaded on demand.

## 6-Axis Topology

| Axis | Name | Scope | ATA Range | Link |
|------|------|-------|-----------|------|
| **O** | Organizations | General info, maintenance policy, ops org, airworthiness, time limits | 00–05 | [O-ORGANIZATIONS](./O-ORGANIZATIONS/) |
| **P** | Programs | Dimensions, lifting, leveling, towing, parking, placards, servicing | 06–12 | [P-PROGRAMS](./P-PROGRAMS/) |
| **T** | Technologies — On-Board Systems | Airframe, cabins, mechanics, environment, data, energy, electrics, comms, propulsion, avionics, intelligence, cryogenic cells | 20–80, 95, 97 | [T-TECHNOLOGIES_ON_BOARD_SYSTEMS](./T-TECHNOLOGIES_ON_BOARD_SYSTEMS/) |
| **I** | Infrastructures | Ground support, H₂ logistics, facilities, GSE | 03-I, 08-I, 10-I, 12-I, 85-I, IN-XX | [I-INFRASTRUCTURES](./I-INFRASTRUCTURES/) |
| **N** | Neural Networks | Governance, traceability, DPP ledger, program slots | 96, 98 | [N-NEURAL_NETWORKS](./N-NEURAL_NETWORKS/) |
| **S** | SIM-TEST — Space Specifics | Simulation, test, space-environment chapters | S10–S38 | [S-SIM_TEST_SPACE_SPECIFICS](./S-SIM_TEST_SPACE_SPECIFICS/) |

### Cross-Programme Applicability

```
                    O   P   T   I   N   S
                    │   │   │   │   │   │
  AMPEL360 Q100     ●   ●   ●   ●   ●   ● (S1+S2 only)
  GAIA-SPACE-LAUN.  ●   ○   ●   ●   ●   ● (full S1+S2+S3)
  SPACET Q10        ●   ○   ●   ●   ●   ● (S1+S2+S3, excl. S32/S35/S37)

  ● = active    ○ = partial / adapted
```

## 6-Axis Summary

| Axis | Chapters | Focus |
|------|:--------:|-------|
| **O** — Organizations | 6 | Governance, policy, airworthiness limits |
| **P** — Programs | 7 | Ground handling, servicing, dimensions |
| **T** — Technologies | 60+ | All on-board systems (airframe → propulsion → AI) |
| **I** — Infrastructures | 6+ | Ground support, H₂ supply chain, facilities |
| **N** — Neural Networks | 2 | DPP ledger, traceability, governance |
| **S** — SIM-TEST / Space | 16 | Simulation, test campaigns, space-specific systems |

**Total OPT-INS chapters: ~97**

## Design Principles

| Principle | Description |
|---|---|
| **Modularity** | Each opt-in module has a single domain responsibility |
| **Composability** | Multiple modules can be activated simultaneously without coupling |
| **Compliance-first** | Every module documents its applicable standards |
| **Backwards-compatible** | Activating a module never breaks an existing baseline |
| **Traceability** | All opt-ins link back to the full ALICE–BOB DT–CHARLIE-T–GENTLE–BOOST chain |

## Canonical Leaf-Node Pattern (all 6 axes)

```
<sub-subject>/
├── README.md
├── SSOT/
│   ├── LC01_PROBLEM_STATEMENT/   ← KNOTS.csv, KNU_PLAN.csv, TIMELINE.csv,
│   │                                RACI.csv, TOKENOMICS_TT.yaml, AWARDS_TT.csv
│   ├── LC02_SYSTEM_REQUIREMENTS/
│   ├── LC03_SAFETY_RELIABILITY/
│   ├── LC04_DESIGN_DEFINITION/
│   ├── LC05_ANALYSIS_MODELS/
│   ├── LC06_VERIFICATION/
│   ├── LC07_VALIDATION/
│   ├── LC08_CONFIGURATION/
│   ├── LC09_PRODUCTION/
│   ├── LC10_OPERATIONS/
│   ├── LC11_MAINTENANCE/
│   ├── LC12_CUSTOMER_CARE/
│   ├── LC13_TRAINING/
│   └── LC14_RETIREMENT_CIRCULARITY/
└── PUB/
    └── AMM/
        ├── CSDB/
        │   ├── DM/              ← Data Modules (S1000D XML)
        │   ├── PM/              ← Publication Modules
        │   ├── DML/             ← Data Module Lists
        │   ├── BREX/            ← Business Rules Exchange
        │   ├── ICN/             ← Information Control Numbers (graphics)
        │   ├── COMMON/          ← Reusable content primitives
        │   └── APPLICABILITY/   ← ACT / PCT / CCT
        ├── EXPORT/              ← Rendered PDF / HTML
        └── IETP/                ← Interactive viewer packaging
```

## Companion Specifications

| Document | Code | Description |
|---|---|---|
| **SUPIA v1.0** | [GQAOA-UTA-SUPIA-001.md](./GQAOA-UTA-SUPIA-001.md) | Sistema Unico di Progettazione Industriale Avanzata — 1000-chapter design system with 10 domains, KNOT/KNU orchestration, TT tokenomics, technical drawing norms, S1000D publication, and comprehensive glossary |
| **UTA Domain Map** | [UTA-DOMAINS.md](./UTA-DOMAINS.md) | Universal Technology Architecture — 10 domain groups (G1–G10), decade block registry, axis distribution, programme coverage |
| **UTA Explorer** | [components/UTAExplorer.jsx](./components/UTAExplorer.jsx) | React interactive visualisation of the full UTA domain map |

## Legacy References

| Module | File | Notes |
|---|---|---|
| S-SPACE (original spec) | [S-SPACE-SPECIFICS.md](./S-SPACE-SPECIFICS.md) | Retained; content migrated to S-axis |

## How to Use

1. **Identify applicable axis and chapter(s)** for your programme from the topology above.
2. **Read the axis README** to find individual ATA / S-chapters.
3. **Declare activation** in your programme's `manifest.yaml` under the `opt_ins:` key.
4. **Reference the module** from your ALICE–BOB DT–CHARLIE-T–GENTLE–BOOST traceability chain.

### Example `manifest.yaml` snippet

```yaml
program: AMPEL360-Q100
opt_ins:
  - axis: O
    chapters: [000, 01, 02, 03, 04, 05]
  - axis: P
    chapters: [06, 07, 08, 09, 10, 11, 12]
  - axis: T
    chapters: [20-80, 95, 97]
  - axis: S
    chapters: [S10, S11, S12, S20, S21, S22, S23]  # Q100: S1+S2 only
```

## Integration with GAIA-QAO Programs

| Program | Active Axes |
|---|---|
| AMPEL360 Q100 | O · P · T · I · N · S (S1+S2) |
| GAIA-SPACE-LAUNCHER | O · T · I · N · S (full S1+S2+S3) |
| SPACET Q10 | O · T · I · N · S (S1+S2+S3, excl. S32/S35/S37) |

## Governance

- **Approval authority:** GAIA-QAO Architecture Board (Q-DATAGOV)  
- **Change process:** RFC → review → merge into versioned release  
- **Audit trail:** All module activations logged in the provenance ledger (AM.PEL quantum-secured DAG)

## Full Index

See [00_INDEX.md](./00_INDEX.md) for the complete chapter registry.
