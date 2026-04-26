---
document_id: QATL-ATLAS1000-EPTA-README
title: "400–499 EPTA — Energy & Propulsion Technology Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: EPTA
architecture_name: "Energy & Propulsion Technology Architecture"
master_range: "400–499"
subrange_count: 10
governance_class: baseline
primary_q_divisions: [Q-GREENTECH, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-CSR, ORB-FIN, ORB-LEG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 400–499 EPTA — Energy & Propulsion Technology Architecture

## 1. Purpose

Energy and propulsion technology architecture band covering primary energy sources, renewables, storage, distribution & HVDC, combustion propulsion, electric & hybrid propulsion, hydrogen & fuel cells, novel propulsion concepts, energy/quantum optimisation, and energy recovery.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| EPTA | Energy & Propulsion Technology Architecture | Energy and propulsion architecture band `400-499`. |
| BoP | Balance of Plant | Auxiliary systems supporting a fuel cell or power plant. |
| HVDC | High Voltage Direct Current | Electrical distribution and propulsion systems. |
| LH₂ | Liquid Hydrogen | Cryogenic hydrogen fuel / energy carrier. |
| TRL | Technology Readiness Level | Maturity scale 1–9. |
| Q+ATLANTIDE | Controlled baseline for the `000-999` architecture-band taxonomy. | Parent baseline of this register. |
| ATLAS-1000 | Umbrella register of the 10 architectures inside Q+ATLANTIDE. | Subpart of Q+ATLANTIDE; not a numeric band. |
| Q-Division | Technical authority unit (e.g. Q-AIR, Q-DATAGOV, Q-HPC). | Owns architecture decisions inside a band (rule N-002). |
| ORB | Organizational Resource Backbone — enterprise support functions. | Provides enterprise-side support to bands (rule N-002). |
| CSDB | Common Source DataBase | S1000D technical-publication data environment. |
| LC | Lifecycle phase / acceptance gate | Used across SSOT/LC01–LC14. |

Cross-reference the full Q+ATLANTIDE acronym set at [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms)[^glossary].

## 3. Architecture Table

Sub-ranges within this band, sourced from the Q+ATLANTIDE controlled baseline[^baseline] §3 *Consolidated Architecture Table*[^table].

| Sub-range | Block | Primary focus | Primary Q-Division | Support Q-Divisions | ORB support |
|---:|---|---|---|---|---|
| 400–409 | Fuentes de Energía Convencionales y Avanzadas | Generación energética, fuentes primarias, arquitecturas de suministro | Q-GREENTECH | Q-HPC, Q-INDUSTRY | ORB-FIN, ORB-PMO |
| 410–419 | Energías Renovables | Solar, eólica, renovables integradas, infraestructura energética | Q-GREENTECH | Q-INDUSTRY, Q-HORIZON | ORB-CSR, ORB-FIN |
| 420–429 | Almacenamiento de Energía | Baterías, supercapacitores, almacenamiento criogénico, buffer energético | Q-GREENTECH | Q-STRUCTURES, Q-HPC | ORB-PMO, ORB-LEG |
| 430–439 | Gestión y Distribución de Energía | HVDC, power management, distribución, protección eléctrica | Q-GREENTECH | Q-MECHANICS, Q-DATAGOV, Q-HPC | ORB-PMO, ORB-LEG |
| 440–449 | Propulsión por Combustión | Turbinas, combustión, hot section, combustibles sostenibles | Q-GREENTECH | Q-AIR, Q-MECHANICS | ORB-PMO, ORB-FIN |
| 450–459 | Propulsión Eléctrica e Híbrida | Motores eléctricos, híbrido-eléctrico, conversión, inversores | Q-GREENTECH | Q-HPC, Q-MECHANICS, Q-AIR | ORB-PMO, ORB-LEG |
| 460–469 | Propulsión de Hidrógeno y Celdas de Combustible | LH₂, fuel cells, BoP, criogenia, seguridad H₂ | Q-GREENTECH | Q-STRUCTURES, Q-MECHANICS, Q-HPC | ORB-PMO, ORB-LEG, ORB-CSR |
| 470–479 | Nuevas Formas de Propulsión | Propulsión avanzada, conceptos post-2040, experimental TRL bajo | Q-HORIZON | Q-GREENTECH, Q-HPC, Q-SPACE | ORB-PMO, ORB-LEG |
| 480–489 | Optimización Energética y Cuántica | Optimización energética, quantum optimization, smart energy systems | Q-HPC | Q-GREENTECH, Q-HORIZON | ORB-PMO, ORB-FIN |
| 490–499 | Sistemas de Recuperación de Energía | Recuperación térmica, regeneración, efficiency recovery systems | Q-GREENTECH | Q-MECHANICS, Q-HPC | ORB-CSR, ORB-FIN |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `400–499` |
| Sub-ranges | 10 |
| Architecture code | `EPTA` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-GREENTECH, Q-HORIZON, Q-HPC |
| Folder path | `Q+ATLANTIDE/400-499_EPTA/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = EPTA`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^table]: **§3 — Consolidated Architecture Table** — [`organization/Q+ATLANTIDE.md` §3](../../organization/Q+ATLANTIDE.md#3-consolidated-architecture-table).

[^glossary]: **§2 — Acronyms** — [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../organization/Q+ATLANTIDE.md#5-templates-system). Mandatory template header fields, naming rules and lifecycle integration.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n003]: **Note N-003** — The `000-999` range is controlled; `ATLAS-1000` is the umbrella name, not an additional numeric band. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^repo]: **Repository root README** — [`README.md`](../../README.md). Top-level entry point referencing the Q+ATLANTIDE baseline and the ATLAS-1000 register subpart.
