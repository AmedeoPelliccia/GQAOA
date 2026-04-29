---
document_id: QATL-ATLAS1000-STA-README
title: "100–199 STA — Space Technology Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
subrange_count: 10
governance_class: baseline
primary_q_divisions: [Q-GREENTECH, Q-HORIZON, Q-SPACE, Q-STRUCTURES]
orb_function_support: [ORB-FIN, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 100–199 STA — Space Technology Architecture

## 1. Purpose

Space technology architecture band covering general space systems and life support, space structures and materials, traditional and advanced propulsion, space energy, mission avionics & control, communications, payloads, on-orbit operations, infrastructure & logistics, and future space concepts.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| STA | Space Technology Architecture | Space architecture band `100-199`. |
| GNC | Guidance, Navigation and Control | Space and aerospace control systems. |
| Satcom | Satellite Communications | Space-segment communications systems. |
| Cis-lunar | Cis-lunar Space | Region of space between Earth and the Moon. |
| MRO | Maintenance, Repair and Overhaul | Lifecycle support discipline. |
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
| 100–109 | 00 | Sistemas Generales y Soporte Vital Espacial | 00 | General Information | Arquitectura general espacial, habitabilidad, soporte vital, seguridad de misión | Q-SPACE | Q-DATAGOV, Q-HORIZON | ORB-PMO, ORB-LEG |
| 110–119 | 01 | Estructuras y Materiales Espaciales | 00 | General Information | Estructuras orbitales, materiales espaciales, protección térmica y radiación | Q-STRUCTURES | Q-SPACE, Q-HORIZON, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 120–129 | 02 | Propulsión Espacial Tradicional y Avanzada | 00 | General Information | Propulsión química, eléctrica, nuclear conceptual, avanzada | Q-GREENTECH | Q-SPACE, Q-HORIZON, Q-HPC | ORB-PMO, ORB-LEG |
| 130–139 | 03 | Sistemas de Energía Espacial | 00 | General Information | Solar, baterías, energía nuclear espacial conceptual, distribución eléctrica | Q-GREENTECH | Q-SPACE, Q-HPC | ORB-PMO, ORB-FIN |
| 140–149 | 04 | Aviónica y Control de Misión Espacial | 00 | General Information | GNC, avionics, flight software, mission control, autonomy | Q-SPACE | Q-DATAGOV, Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 150–159 | 05 | Comunicaciones Espaciales | 00 | General Information | Satcom, enlaces ópticos, redes espaciales, comunicación intersatélite | Q-SPACE | Q-DATAGOV, Q-HPC | ORB-PMO, ORB-LEG |
| 160–169 | 06 | Sensores y Carga Útil Espacial | 00 | General Information | Payloads, instrumentación, sensores científicos, observación | Q-SPACE | Q-HORIZON, Q-HPC, Q-DATAGOV | ORB-PMO, ORB-MKTG |
| 170–179 | 07 | Operaciones y Mantenimiento en Órbita | 00 | General Information | Servicing orbital, inspección, reparación, ensamblaje en órbita | Q-SPACE | Q-GROUND, Q-HORIZON, Q-MECHANICS | ORB-PMO, ORB-LEG |
| 180–189 | 08 | Infraestructura y Logística Espacial | 00 | General Information | Bases orbitales, logística cis-lunar, transporte espacial, recursos | Q-SPACE | Q-INDUSTRY, Q-GROUND, Q-HORIZON | ORB-PMO, ORB-FIN |
| 190–199 | 09 | Sistemas Avanzados, Conceptos y Futuro Espacial | 00 | General Information | Interplanetario, hábitats avanzados, conceptos post-2040 | Q-HORIZON | Q-SPACE, Q-HPC, Q-GREENTECH | ORB-PMO, ORB-MKTG |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `100–199` |
| Sub-ranges | 10 |
| Architecture code | `STA` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-GREENTECH, Q-HORIZON, Q-SPACE, Q-STRUCTURES |
| Folder path | `Q+ATLANTIDE/100-199_STA/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = STA`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

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
