---
document_id: QATL-ATLAS1000-ATLAS-README
title: "000–099 ATLAS — Aircraft Top-Level Architecture System"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
subrange_count: 9
governance_class: baseline
structural_interface_rule: N-005
primary_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-MECHANICS, Q-STRUCTURES]
orb_function_support: [ORB-FIN, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 000–099 ATLAS — Aircraft Top-Level Architecture System

## 1. Purpose

Aircraft top-level architecture band covering identification, ground handling, core aircraft systems, mechanical protection, avionics & APU, primary structures, traditional and alternative propulsion, and aircraft-type expansion.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| ATLAS | Aircraft Top-Level Architecture System | Aircraft architecture band `000-099`. |
| APU | Auxiliary Power Unit | Onboard auxiliary power generator. |
| BWB | Blended Wing Body | Aircraft configuration family. |
| CMS | Central Maintenance System | Onboard maintenance computing function. |
| ECS | Environmental Control System | Cabin air conditioning and pressurisation. |
| GSE | Ground Support Equipment | Ground operations and maintenance support. |
| HVDC | High Voltage Direct Current | Electrical distribution and propulsion systems. |
| IMA | Integrated Modular Avionics | Aircraft avionics architecture. |
| LH₂ | Liquid Hydrogen | Cryogenic hydrogen fuel / energy carrier. |
| WTW | Wide Tube and Wing | Aircraft configuration family. |
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
| 000–009 | Información General y Servicio | Identificación, configuración, documentación general, operaciones básicas | Q-DATAGOV | Q-GROUND, Q-AIR | ORB-PMO, ORB-LEG |
| 010–019 | Manejo en Tierra & Servicio | Ground handling, servicing, acceso, remolque, parking, GSE | Q-GROUND | Q-MECHANICS, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 020–029 | Sistemas Core de Aeronave | Aviónica base, eléctrica, hidráulica, ECS, fuel, flight control | Q-AIR | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH | ORB-PMO, ORB-LEG |
| 030–039 | Protección & Sistemas Mecánicos | Ice/rain protection, fire protection, tren, actuadores | Q-MECHANICS | Q-AIR, Q-STRUCTURES | ORB-PMO, ORB-LEG |
| 040–049 | Aviónica, Información & APU | IMA, redes de datos, CMS, APU, onboard information systems | Q-DATAGOV | Q-AIR, Q-SPACE, Q-HPC | ORB-PMO, ORB-LEG |
| 050–059 | Estructuras Primarias e Interfaces de Programa / Q-Division | Fuselaje, alas, BWB, WTW, zonas estructurales, interfaces técnicas | Q-STRUCTURES | Q-AIR, Q-INDUSTRY, Q-HPC | ORB-PMO, ORB-FIN, ORB-LEG |
| 060–079 | Propulsión Tradicional & Eco-Tech | Turbofan, híbrido-eléctrico, thermal management, nacelles | Q-GREENTECH | Q-MECHANICS, Q-AIR, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 080–089 | Propulsión Alternativa & Cuántica | LH₂, fuel cells, HVDC, superconductores, Q-sensing | Q-GREENTECH | Q-HORIZON, Q-HPC, Q-STRUCTURES | ORB-PMO, ORB-LEG, ORB-FIN |
| 090–099 | Tipos Específicos & Expansión | Variantes BWB/WTW, demostradores, clases especiales de aeronaves | Q-HORIZON | Q-AIR, Q-STRUCTURES, Q-GREENTECH | ORB-PMO, ORB-MKTG |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `000–099` |
| Sub-ranges | 9 |
| Architecture code | `ATLAS` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-MECHANICS, Q-STRUCTURES |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |
| Structural-interface rule | Sub-range `050–059` shall use the title fragment *Estructuras Primarias e Interfaces de Programa / Q-Division* (rule N-005[^n005]). |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^table]: **§3 — Consolidated Architecture Table** — [`organization/Q+ATLANTIDE.md` §3](../../organization/Q+ATLANTIDE.md#3-consolidated-architecture-table).

[^glossary]: **§2 — Acronyms** — [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../organization/Q+ATLANTIDE.md#5-templates-system). Mandatory template header fields, naming rules and lifecycle integration.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n003]: **Note N-003** — The `000-999` range is controlled; `ATLAS-1000` is the umbrella name, not an additional numeric band. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n005]: **Note N-005** — `ATLAS 050–059` shall use *Estructuras Primarias e Interfaces de Programa / Q-Division*. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^repo]: **Repository root README** — [`README.md`](../../README.md). Top-level entry point referencing the Q+ATLANTIDE baseline and the ATLAS-1000 register subpart.
