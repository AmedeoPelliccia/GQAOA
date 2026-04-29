---
document_id: QATL-ATLAS-1000-OGATA-660-669-06-20-00-OVERVIEW
title: "OGATA 660-669 · 06.20.00 — demolition automation"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: OGATA
architecture_name: "On-Ground Automation Technology Architecture"
master_range: "600–699"
code_range: "660-669"
section: "06"
section_title: "Construcción y Demolición Automatizada"
subject: "00"
subject_title: "General Information"
subsection: "20"
subsection_title: "demolition automation"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-GROUND
support_q_divisions: [Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# OGATA 660-669 · Section 06 · Subsection 20 — demolition automation

## 1. Purpose

Overview entry-point for the *demolition automation* subsection within the `660-669` code range (Section `06` — *Construcción y Demolición Automatizada*) of the **OGATA** architecture band (*On-Ground Automation Technology Architecture*, master range `600–699`).

This subsubject (`00 Overview`) introduces the OGATA 660-669.20.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *demolition automation* slice of the parent code range `660-669`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `OGATA` — On-Ground Automation Technology Architecture |
| Master range | `600–699` |
| Code range | `660-669` |
| Section | `06` — Construcción y Demolición Automatizada |
| Subject | `00` — General Information |
| Subsection | `20` — demolition automation |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-INDUSTRY, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/600-699_OGATA/660-669_Construccion-y-Demolicion-Automatizada/20_demolition-automation/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **OGATA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `660-669` row (Section `06` — Construcción y Demolición Automatizada, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^iso102181]: **ISO 10218-1:2011 — Robots and robotic devices — Safety requirements (Part 1)** — Safety baseline for industrial robots within OGATA `600-699`.

[^iso102182]: **ISO 10218-2:2011 — Robots and robotic devices — Safety requirements (Part 2)** — Integration safety baseline for robotic systems and cells inside OGATA.

[^isots15066]: **ISO/TS 15066:2016 — Robots and robotic devices — Collaborative robots** — Collaborative-robot safety reference for OGATA cells with human interaction.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ISO 10218-1:2011 — Robots and robotic devices — Safety requirements (Part 1)[^iso102181]
- ISO 10218-2:2011 — Robots and robotic devices — Safety requirements (Part 2)[^iso102182]
- ISO/TS 15066:2016 — Robots and robotic devices — Collaborative robots[^isots15066]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

