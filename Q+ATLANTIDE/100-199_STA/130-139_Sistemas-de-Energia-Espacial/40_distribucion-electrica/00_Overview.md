---
document_id: QATL-ATLAS-1000-STA-130-139-03-40-00-OVERVIEW
title: "STA 130-139 · 03.40.00 — distribución eléctrica"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
section_title: "Sistemas de Energía Espacial"
subject: "00"
subject_title: "General Information"
subsection: "40"
subsection_title: "distribución eléctrica"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-SPACE, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 40 — distribución eléctrica

## 1. Purpose

Overview entry-point for the *distribución eléctrica* subsection within the `130-139` code range (Section `03` — *Sistemas de Energía Espacial*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`00 Overview`) introduces the STA 130-139.40.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *distribución eléctrica* slice of the parent code range `130-139`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subject | `00` — General Information |
| Subsection | `40` — distribución eléctrica |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HPC |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/40_distribucion-electrica/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `130-139` row (Section `03` — Sistemas de Energía Espacial, Primary Q-Division Q-GREENTECH).

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

