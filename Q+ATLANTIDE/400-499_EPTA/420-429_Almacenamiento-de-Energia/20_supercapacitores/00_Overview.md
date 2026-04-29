---
document_id: QATL-ATLAS-1000-EPTA-420-429-02-20-00-OVERVIEW
title: "EPTA 420-429 · 02.20.00 — supercapacitores"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: EPTA
architecture_name: "Energy & Propulsion Technology Architecture"
master_range: "400–499"
code_range: "420-429"
section: "02"
section_title: "Almacenamiento de Energía"
subject: "00"
subject_title: "General Information"
subsection: "20"
subsection_title: "supercapacitores"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-STRUCTURES, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# EPTA 420-429 · Section 02 · Subsection 20 — supercapacitores

## 1. Purpose

Overview entry-point for the *supercapacitores* subsection within the `420-429` code range (Section `02` — *Almacenamiento de Energía*) of the **EPTA** architecture band (*Energy & Propulsion Technology Architecture*, master range `400–499`).

This subsubject (`00 Overview`) introduces the EPTA 420-429.20.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *supercapacitores* slice of the parent code range `420-429`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `EPTA` — Energy & Propulsion Technology Architecture |
| Master range | `400–499` |
| Code range | `420-429` |
| Section | `02` — Almacenamiento de Energía |
| Subject | `00` — General Information |
| Subsection | `20` — supercapacitores |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/400-499_EPTA/420-429_Almacenamiento-de-Energia/20_supercapacitores/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **EPTA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `420-429` row (Section `02` — Almacenamiento de Energía, Primary Q-Division Q-GREENTECH).

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

