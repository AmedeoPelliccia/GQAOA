---
document_id: QATL-ATLAS-1000-STA-110-119-01-030-00-OVERVIEW
title: "STA 110-119 · 01.030.00 — protección térmica y radiación"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subject: "00"
subject_title: "General Information"
subsection: "030"
subsection_title: "protección térmica y radiación"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-SPACE, Q-HORIZON, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 030 — protección térmica y radiación

## 1. Purpose

Overview entry-point for the *protección térmica y radiación* subsection within the `110-119` code range (Section `01` — *Estructuras y Materiales Espaciales*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`00 Overview`) introduces the STA 110-119.030.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *protección térmica y radiación* slice of the parent code range `110-119`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subject | `00` — General Information |
| Subsection | `030` — protección térmica y radiación |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-STRUCTURES[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/030_proteccion-termica-y-radiacion/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `110-119` row (Section `01` — Estructuras y Materiales Espaciales, Primary Q-Division Q-STRUCTURES).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ecsseastm10c]: **ECSS-E-ST-10C Rev.1 — Space engineering: System engineering general requirements** — European Cooperation for Space Standardization baseline for space system engineering applied to STA `100-199`.

[^nasanpr71205]: **NASA NPR 7120.5F — NASA Space Flight Program and Project Management Requirements** — Programmatic baseline for orbital and interplanetary missions covered by STA.

[^ccsds]: **CCSDS Recommended Standards — Consultative Committee for Space Data Systems** — Interoperability standards for space data, telemetry and link layers used inside STA.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ECSS-E-ST-10C Rev.1 — Space engineering: System engineering general requirements[^ecsseastm10c]
- NASA NPR 7120.5F — NASA Space Flight Program and Project Management Requirements[^nasanpr71205]
- CCSDS Recommended Standards — Consultative Committee for Space Data Systems[^ccsds]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

