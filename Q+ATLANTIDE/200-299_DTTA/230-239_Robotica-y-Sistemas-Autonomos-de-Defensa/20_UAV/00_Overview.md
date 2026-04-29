---
document_id: QATL-ATLAS-1000-DTTA-230-239-03-20-00-OVERVIEW
title: "DTTA 230-239 · 03.20.00 — UAV"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: DTTA
architecture_name: "Defence Technology Type Architecture"
master_range: "200–299"
code_range: "230-239"
section: "03"
section_title: "Robótica y Sistemas Autónomos de Defensa"
subject: "00"
subject_title: "General Information"
subsection: "20"
subsection_title: "UAV"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-HPC
support_q_divisions: [Q-HORIZON, Q-DATAGOV, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# DTTA 230-239 · Section 03 · Subsection 20 — UAV

## 1. Purpose

Overview entry-point for the *UAV* subsection within the `230-239` code range (Section `03` — *Robótica y Sistemas Autónomos de Defensa*) of the **DTTA** architecture band (*Defence Technology Type Architecture*, master range `200–299`).

This subsubject (`00 Overview`) introduces the DTTA 230-239.20.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *UAV* slice of the parent code range `230-239`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `DTTA` — Defence Technology Type Architecture |
| Master range | `200–299` |
| Code range | `230-239` |
| Section | `03` — Robótica y Sistemas Autónomos de Defensa |
| Subject | `00` — General Information |
| Subsection | `20` — UAV |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/230-239_Robotica-y-Sistemas-Autonomos-de-Defensa/20_UAV/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **DTTA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `230-239` row (Section `03` — Robótica y Sistemas Autónomos de Defensa, Primary Q-Division Q-HPC).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^stanag4671]: **NATO STANAG 4671 — UAV Systems Airworthiness Requirements (USAR)** — Airworthiness baseline for defence unmanned platforms inside DTTA `200-299`.

[^milstd961]: **MIL-STD-961F — Defense and Program-Unique Specifications Format and Content** — Format baseline for defence technical specifications produced under DTTA.

[^milhdbk516]: **MIL-HDBK-516C — Airworthiness Certification Criteria** — Airworthiness criteria reference for crewed and uncrewed defence air systems.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- NATO STANAG 4671 — UAV Systems Airworthiness Requirements (USAR)[^stanag4671]
- MIL-STD-961F — Defense and Program-Unique Specifications Format and Content[^milstd961]
- MIL-HDBK-516C — Airworthiness Certification Criteria[^milhdbk516]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

