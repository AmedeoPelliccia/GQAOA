---
document_id: QATL-ATLAS1000-DTTA-README
title: "200–299 DTTA — Defence Technology Type Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: DTTA
architecture_name: "Defence Technology Type Architecture"
master_range: "200–299"
subrange_count: 10
governance_class: restricted
restricted_rule: N-006
primary_q_divisions: [Q-DATAGOV, Q-GROUND, Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-FIN, ORB-HR, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 200–299 DTTA — Defence Technology Type Architecture

## 1. Purpose

Defence technology type architecture band covering combat & weapons systems, C4ISR, protection & resilience, defence robotics & autonomous systems, military logistics, cyber-defence & electronic warfare, defence materials & sensors, military simulation & training, quantum warfare, and future operational concepts.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| DTTA | Defence Technology Type Architecture | Defence architecture band `200-299` (restricted). |
| C4ISR | Command, Control, Communications, Computers, Intelligence, Surveillance and Reconnaissance | Defence and mission systems classification. |
| EW | Electronic Warfare | Spectrum operations and electromagnetic effects. |
| UGV | Unmanned Ground Vehicle | Land-based autonomous platform. |
| UAV | Unmanned Aerial Vehicle | Air-based autonomous platform. |
| USV | Unmanned Surface Vehicle | Sea-surface autonomous platform. |
| XR | Extended Reality | Immersive / mixed / augmented reality technologies. |
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
| 200–209 | Sistemas de Combate y Armamento | Sistemas de combate, efectos, integración de plataformas | Q-HORIZON | Q-AIR, Q-SPACE, Q-DATAGOV | ORB-LEG, ORB-PMO |
| 210–219 | C4ISR | Mando, control, comunicaciones, inteligencia, vigilancia, reconocimiento | Q-DATAGOV | Q-SPACE, Q-HPC, Q-AIR | ORB-PMO, ORB-LEG |
| 220–229 | Protección y Resiliencia | Protección de sistemas, supervivencia, hardening, resiliencia operacional | Q-HORIZON | Q-STRUCTURES, Q-DATAGOV, Q-HPC | ORB-LEG, ORB-PMO |
| 230–239 | Robótica y Sistemas Autónomos de Defensa | UGV, UAV, USV, autonomía, swarms, control humano-supervisado | Q-HPC | Q-HORIZON, Q-DATAGOV, Q-AIR | ORB-PMO, ORB-LEG |
| 240–249 | Logística y Mantenimiento en Defensa | MRO militar, logística desplegada, soporte en campaña | Q-GROUND | Q-INDUSTRY, Q-DATAGOV, Q-MECHANICS | ORB-PMO, ORB-FIN |
| 250–259 | Ciberdefensa y Guerra Electrónica | EW, cyber defence, spectrum operations, resilience | Q-DATAGOV | Q-SPACE, Q-HPC, Q-HORIZON | ORB-LEG, ORB-PMO |
| 260–269 | Materiales y Sensores para Defensa | Sensores, protección, materiales especiales, stealth conceptual | Q-STRUCTURES | Q-HORIZON, Q-HPC, Q-DATAGOV | ORB-PMO, ORB-LEG |
| 270–279 | Simulación y Entrenamiento Militar | Synthetic environments, simuladores, wargaming, entrenamiento XR | Q-HPC | Q-DATAGOV, Q-AIR, Q-GROUND | ORB-PMO, ORB-HR |
| 280–289 | Guerra Cuántica y Tecnologías Disruptivas | Quantum sensing, quantum comms, quantum cyber, tecnologías emergentes | Q-HORIZON | Q-HPC, Q-DATAGOV, Q-SPACE | ORB-LEG, ORB-PMO |
| 290–299 | Conceptos Operacionales Futuros | Future operating concepts, multi-domain operations, doctrina tecnológica | Q-HORIZON | Q-HPC, Q-DATAGOV, Q-SPACE | ORB-PMO, ORB-MKTG |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `200–299` |
| Sub-ranges | 10 |
| Architecture code | `DTTA` |
| Governance class | `restricted` |
| Restricted band | Yes (rule N-006[^n006]) |
| Primary Q-Divisions | Q-DATAGOV, Q-GROUND, Q-HORIZON, Q-HPC, Q-STRUCTURES |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = DTTA`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

**Restricted band (N-006[^n006]).** Templates inside this band must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`.

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^table]: **§3 — Consolidated Architecture Table** — [`organization/Q+ATLANTIDE.md` §3](../../organization/Q+ATLANTIDE.md#3-consolidated-architecture-table).

[^glossary]: **§2 — Acronyms** — [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../organization/Q+ATLANTIDE.md#5-templates-system). Mandatory template header fields, naming rules and lifecycle integration.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n003]: **Note N-003** — The `000-999` range is controlled; `ATLAS-1000` is the umbrella name, not an additional numeric band. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Defence-related (`200-299` DTTA), cybersecurity-related (`800-899` CYB) and quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^repo]: **Repository root README** — [`README.md`](../../README.md). Top-level entry point referencing the Q+ATLANTIDE baseline and the ATLAS-1000 register subpart.
