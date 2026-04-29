---
document_id: QATL-ATLAS-1000-EPTA-470-479-07-30-00-OVERVIEW
title: "EPTA 470-479 · 07.30.00 — experimental TRL bajo"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: EPTA
architecture_name: "Energy & Propulsion Technology Architecture"
master_range: "400–499"
code_range: "470-479"
section: "07"
section_title: "Nuevas Formas de Propulsión"
subject: "00"
subject_title: "General Information"
subsection: "30"
subsection_title: "experimental TRL bajo"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-SPACE]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# EPTA 470-479 · Section 07 · Subsection 30 — experimental TRL bajo

## 1. Purpose

Overview entry-point for the *experimental TRL bajo* subsection within the `470-479` code range (Section `07` — *Nuevas Formas de Propulsión*) of the **EPTA** architecture band (*Energy & Propulsion Technology Architecture*, master range `400–499`).

This subsubject (`00 Overview`) introduces the EPTA 470-479.30.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *experimental TRL bajo* slice of the parent code range `470-479`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `EPTA` — Energy & Propulsion Technology Architecture |
| Master range | `400–499` |
| Code range | `470-479` |
| Section | `07` — Nuevas Formas de Propulsión |
| Subject | `00` — General Information |
| Subsection | `30` — experimental TRL bajo |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-HPC, Q-SPACE |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/400-499_EPTA/470-479_Nuevas-Formas-de-Propulsion/30_experimental-TRL-bajo/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **EPTA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `470-479` row (Section `07` — Nuevas Formas de Propulsión, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^iec61508]: **IEC 61508:2010 — Functional safety of E/E/PE safety-related systems** — Functional safety baseline for energy and propulsion electronics within EPTA `400-499`.

[^iso50001]: **ISO 50001:2018 — Energy Management Systems** — Energy management baseline for the energy domain of EPTA.

[^saeas6968]: **SAE AS6968 — Hydrogen Fuel Cell Aircraft** — Aerospace recommended practice for hydrogen / fuel-cell propulsion relevant to EPTA.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- IEC 61508:2010 — Functional safety of E/E/PE safety-related systems[^iec61508]
- ISO 50001:2018 — Energy Management Systems[^iso50001]
- SAE AS6968 — Hydrogen Fuel Cell Aircraft[^saeas6968]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

