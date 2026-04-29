---
document_id: QATL-ATLAS-1000-DTCEC-370-379-07-20-00-OVERVIEW
title: "DTCEC 370-379 · 07.20.00 — model integrity"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: DTCEC
architecture_name: "Digital Twin, Cloud, Edge & AI Architecture"
master_range: "300–399"
code_range: "370-379"
section: "07"
section_title: "Ciberseguridad para Digital Twins"
subject: "00"
subject_title: "General Information"
subsection: "20"
subsection_title: "model integrity"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-HPC, Q-SPACE]
orb_function_support: [ORB-LEG, ORB-PMO]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# DTCEC 370-379 · Section 07 · Subsection 20 — model integrity

## 1. Purpose

Overview entry-point for the *model integrity* subsection within the `370-379` code range (Section `07` — *Ciberseguridad para Digital Twins*) of the **DTCEC** architecture band (*Digital Twin, Cloud, Edge & AI Architecture*, master range `300–399`).

This subsubject (`00 Overview`) introduces the DTCEC 370-379.20.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *model integrity* slice of the parent code range `370-379`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `DTCEC` — Digital Twin, Cloud, Edge & AI Architecture |
| Master range | `300–399` |
| Code range | `370-379` |
| Section | `07` — Ciberseguridad para Digital Twins |
| Subject | `00` — General Information |
| Subsection | `20` — model integrity |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-SPACE |
| ORB support | ORB-LEG, ORB-PMO |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/300-399_DTCEC/370-379_Ciberseguridad-para-Digital-Twins/20_model-integrity/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **DTCEC §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `370-379` row (Section `07` — Ciberseguridad para Digital Twins, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^isoiec30141]: **ISO/IEC 30141:2018 — Internet of Things (IoT) Reference Architecture** — Reference architecture for distributed edge / cloud / IoT systems mapped by DTCEC `300-399`.

[^isoiec23053]: **ISO/IEC 23053:2022 — Framework for AI Systems Using Machine Learning** — Framework standard applied to the AI/ML scope of DTCEC.

[^ieee7000]: **IEEE 7000-2021 — Model Process for Addressing Ethical Concerns during System Design** — Ethical-by-design process applied to digital-twin and AI flows.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ISO/IEC 30141:2018 — Internet of Things (IoT) Reference Architecture[^isoiec30141]
- ISO/IEC 23053:2022 — Framework for AI Systems Using Machine Learning[^isoiec23053]
- IEEE 7000-2021 — Model Process for Addressing Ethical Concerns during System Design[^ieee7000]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

