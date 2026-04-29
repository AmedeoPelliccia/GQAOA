---
document_id: QATL-ATLAS1000-OGATA-README
title: "600–699 OGATA — On-Ground Automation Technology Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: OGATA
architecture_name: "On-Ground Automation Technology Architecture"
master_range: "600–699"
subrange_count: 10
governance_class: baseline
primary_q_divisions: [Q-GROUND, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-CSR, ORB-FIN, ORB-HR, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 600–699 OGATA — On-Ground Automation Technology Architecture

## 1. Purpose

On-ground automation technology architecture band covering industrial & collaborative robotics, autonomous ground vehicles, smart infrastructure, Factory 4.0 & advanced manufacturing, automated logistics, precision agriculture, construction automation, indoor service robots, AI/quantum optimisation, and Human-Robot Interaction.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| OGATA | On-Ground Automation Technology Architecture | Ground automation architecture band `600-699`. |
| AGV | Automated Guided Vehicle | Path-following autonomous transport unit. |
| AMR | Autonomous Mobile Robot | Free-navigating autonomous transport unit. |
| FAL | Final Assembly Line | Manufacturing assembly stage. |
| HRI | Human-Robot Interaction | Ground automation and collaborative robotics. |
| MES | Manufacturing Execution System | Factory production management software. |
| Q+ATLANTIDE | Controlled baseline for the `000-999` architecture-band taxonomy. | Parent baseline of this register. |
| ATLAS-1000 | Umbrella register of the 10 architectures inside Q+ATLANTIDE. | Subpart of Q+ATLANTIDE; not a numeric band. |
| Q-Division | Technical authority unit (e.g. Q-AIR, Q-DATAGOV, Q-HPC). | Owns architecture decisions inside a band (rule N-002). |
| ORB | Organizational Resource Backbone — enterprise support functions. | Provides enterprise-side support to bands (rule N-002). |
| CSDB | Common Source DataBase | S1000D technical-publication data environment. |
| LC | Lifecycle phase / acceptance gate | Used across SSOT/LC01–LC14. |

Cross-reference the full Q+ATLANTIDE acronym set at [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms)[^glossary].

## 3. Architecture Table

Sub-ranges within this band, sourced from the Q+ATLANTIDE controlled baseline[^baseline] §3 *Consolidated Architecture Table*[^table].

| Code range | Section | Section title | Subject | Subject title | Primary focus | Primary Q-Division | Support Q-Divisions | ORB support |
|---:|---:|---|---:|---|---|---|---|---|
| 600–609 | 00 | Robótica Industrial y Colaborativa | 00 | General Information | Robots industriales, cobots, automation cells, safety | Q-INDUSTRY | Q-HPC, Q-GROUND | ORB-PMO, ORB-FIN |
| 610–619 | 01 | Vehículos Autónomos Terrestres | 00 | General Information | AGV, AMR, autonomous towing, yard automation | Q-GROUND | Q-HPC, Q-INDUSTRY, Q-DATAGOV | ORB-PMO, ORB-FIN |
| 620–629 | 02 | Infraestructura Inteligente | 00 | General Information | Smart infrastructure, connected facilities, sensorized ground systems | Q-GROUND | Q-DATAGOV, Q-INDUSTRY | ORB-FIN, ORB-PMO |
| 630–639 | 03 | Fábricas 4.0 y Manufactura Avanzada | 00 | General Information | Digital manufacturing, FAL automation, MES, robotics | Q-INDUSTRY | Q-DATAGOV, Q-HPC | ORB-PMO, ORB-FIN |
| 640–649 | 04 | Logística y Almacenamiento Automatizado | 00 | General Information | Warehousing, automated logistics, supply chain robotics | Q-INDUSTRY | Q-GROUND, Q-DATAGOV | ORB-FIN, ORB-PMO |
| 650–659 | 05 | Agricultura de Precisión | 00 | General Information | Agro-automation, robotics, monitoring, autonomous farming systems | Q-HORIZON | Q-HPC, Q-GROUND | ORB-CSR, ORB-MKTG |
| 660–669 | 06 | Construcción y Demolición Automatizada | 00 | General Information | Construction robotics, demolition automation, autonomous site operations | Q-GROUND | Q-INDUSTRY, Q-HPC | ORB-PMO, ORB-LEG |
| 670–679 | 07 | Servicios Autónomos en Entornos Cerrados | 00 | General Information | Indoor robotics, maintenance support, facility service robots | Q-GROUND | Q-HPC, Q-DATAGOV | ORB-PMO, ORB-HR |
| 680–689 | 08 | Optimización con IA y Cuántica | 00 | General Information | Scheduling, routing, quantum optimization, logistics intelligence | Q-HPC | Q-DATAGOV, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 690–699 | 09 | Interacción Humano-Robot y Seguridad | 00 | General Information | HRI, safety cases, human factors, collaborative procedures | Q-INDUSTRY | Q-HPC, Q-GROUND | ORB-HR, ORB-LEG |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `600–699` |
| Sub-ranges | 10 |
| Architecture code | `OGATA` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-GROUND, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| Folder path | `Q+ATLANTIDE/600-699_OGATA/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = OGATA`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

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
