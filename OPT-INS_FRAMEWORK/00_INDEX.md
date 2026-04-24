# OPT-INS Framework — Master Index

**Programme:** AMPEL360 Q100 · GAIA-SPACE-LAUNCHER · SPACET Q10  
**Version:** OPT-INS v1.0  
**Generated:** 2026-04-11

---

## 6-Axis Topology

| Axis | Name | Scope | Link |
|------|------|-------|------|
| **O** | Organizations | General info, maintenance policy, ops org, airworthiness, time limits (ATA 00–05) | [O-ORGANIZATIONS](./O-ORGANIZATIONS/) |
| **P** | Programs | Dimensions, lifting, leveling, towing, parking, placards, servicing (ATA 06–12) | [P-PROGRAMS](./P-PROGRAMS/) |
| **T** | Technologies — On-Board Systems | Airframe, cabins, mechanics, environment, data, energy, electrics, comms, propulsion, avionics, intelligence (ATA 20–80, 95, 97) | [T-TECHNOLOGIES_ON_BOARD_SYSTEMS](./T-TECHNOLOGIES_ON_BOARD_SYSTEMS/) |
| **I** | Infrastructures | Ground support, H₂ logistics, facilities, GSE | [I-INFRASTRUCTURES](./I-INFRASTRUCTURES/) |
| **N** | Neural Networks | Governance, traceability, DPP ledger, program slots (ATA 96, 98) | [N-NEURAL_NETWORKS](./N-NEURAL_NETWORKS/) |
| **S** | SIM-TEST — Space Specifics | Simulation, test, space-environment chapters (S-XX) | [S-SIM_TEST_SPACE_SPECIFICS](./S-SIM_TEST_SPACE_SPECIFICS/) |

## Cross-Programme Applicability

```
                    O   P   T   I   N   S
                    │   │   │   │   │   │
  AMPEL360 Q100     ●   ●   ●   ●   ●   ● (S1+S2 only)
  GAIA-SPACE-LAUN.  ●   ○   ●   ●   ●   ● (full S1+S2+S3)
  SPACET Q10        ●   ○   ●   ●   ●   ● (S1+S2+S3, excl. S32/S35/S37)

  ● = active    ○ = partial / adapted
```

## Total OPT-INS Chapters: ~97

| Axis | Chapters | Focus |
|------|:--------:|-------|
| **O** — Organizations | 6 | Governance, policy, airworthiness limits |
| **P** — Programs | 7 | Ground handling, servicing, dimensions |
| **T** — Technologies | 60+ | All on-board systems (airframe → propulsion → AI) |
| **I** — Infrastructures | 6+ | Ground support, H₂ supply chain, facilities |
| **N** — Neural Networks | 2 | DPP ledger, traceability, governance |
| **S** — SIM-TEST / Space | 16 | Simulation, test campaigns, space-specific systems |

---

## Companion Documents

| Document | Description |
|----------|-------------|
| [GQAOA-UTA-SUPIA-001.md](./GQAOA-UTA-SUPIA-001.md) | **SUPIA v1.0** — Sistema Unico di Progettazione Industriale Avanzata (17 sections + glossary) |
| [UTA-DOMAINS.md](./UTA-DOMAINS.md) | Universal Technology Architecture — 10 domains, 1000 chapters, decade block registry |
| [GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md](./GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md) | **G10.975 Containment Grammar** — G109 naming, containment/quarantine, and regency escalation primitive |
| [components/UTAExplorer.jsx](./components/UTAExplorer.jsx) | React interactive UTA Explorer |

---

*OPT-INS Framework v1.0 — Amedeo Pelliccia — AEROSPACEMODEL Lifecycle Operating System*
