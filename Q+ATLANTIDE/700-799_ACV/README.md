---
document_id: QATL-ATLAS1000-ACV-README
title: "700–799 ACV — Aerial City Viability / UAM Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: ACV
architecture_name: "Aerial City Viability / UAM Architecture"
master_range: "700–799"
subrange_count: 10
governance_class: baseline
primary_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-CSR, ORB-FIN, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 700–799 ACV — Aerial City Viability / UAM Architecture

## 1. Purpose

Aerial city viability architecture band covering UAM vehicles, vertiport infrastructure, urban traffic management (UTM), noise & acoustics, environmental sustainability, certification & legal frameworks, urban interface & social acceptance, operational safety & resilience, quantum traffic optimisation, and UAM business models.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| ACV | Aerial City Viability | UAM and aerial-city architecture band `700-799`. |
| eVTOL | Electric Vertical Take-Off and Landing | Battery-electric VTOL aircraft platform. |
| ESG | Environmental, Social and Governance | Sustainability reporting framework. |
| UAM | Urban Air Mobility | Urban aerial mobility ecosystem. |
| UTM | Uncrewed / Urban Traffic Management | Traffic-management domain for UAM / uncrewed operations. |
| UX | User Experience | Human-centred interaction design. |
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
| 700–709 | Vehículos de Movilidad Aérea Urbana | eVTOL, UAM vehicles, urban air platforms | Q-AIR | Q-GREENTECH, Q-STRUCTURES, Q-HPC | ORB-MKTG, ORB-PMO |
| 710–719 | Vertipuertos y Heliplataformas | Vertiports, charging/refuelling, passenger infrastructure | Q-GROUND | Q-GREENTECH, Q-INDUSTRY | ORB-FIN, ORB-PMO |
| 720–729 | Gestión del Tráfico Aéreo Urbano | UTM, airspace integration, traffic management, autonomy | Q-AIR | Q-DATAGOV, Q-SPACE, Q-HPC | ORB-PMO, ORB-LEG |
| 730–739 | Ruido y Acústica Urbana | Noise modelling, acoustic footprint, urban impact | Q-AIR | Q-HPC, Q-GREENTECH | ORB-CSR, ORB-MKTG |
| 740–749 | Sostenibilidad Ambiental en UAM | Emissions, lifecycle impact, ESG, urban sustainability | Q-GREENTECH | Q-DATAGOV, Q-HPC | ORB-CSR, ORB-PMO |
| 750–759 | Legal, Regulación y Certificación UAM | Certification, airworthiness, operating rules, liability | Q-DATAGOV | Q-AIR, Q-GROUND | ORB-LEG, ORB-PMO |
| 760–769 | Interfaz Urbana y Aceptación Social | Human factors, accessibility, social acceptance, UX | Q-GROUND | Q-AIR, Q-DATAGOV | ORB-MKTG, ORB-CSR |
| 770–779 | Seguridad y Resiliencia Operacional | Safety, emergency response, operational resilience | Q-AIR | Q-GROUND, Q-DATAGOV, Q-HPC | ORB-PMO, ORB-LEG |
| 780–789 | Optimización Cuántica de Tráfico y Logística UAM | Quantum traffic optimization, urban logistics, routing | Q-HPC | Q-AIR, Q-DATAGOV, Q-HORIZON | ORB-PMO, ORB-FIN |
| 790–799 | Modelos de Negocio y Ecosistemas UAM | Operators, business models, infrastructure partnerships | Q-HORIZON | Q-AIR, Q-GROUND | ORB-MKTG, ORB-FIN |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `700–799` |
| Sub-ranges | 10 |
| Architecture code | `ACV` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-HPC |
| Folder path | `Q+ATLANTIDE/700-799_ACV/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = ACV`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

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
