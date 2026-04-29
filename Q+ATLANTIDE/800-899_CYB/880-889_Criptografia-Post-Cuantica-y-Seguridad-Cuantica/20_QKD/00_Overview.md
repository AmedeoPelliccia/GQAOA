---
document_id: QATL-ATLAS-1000-CYB-880-889-08-20-00-OVERVIEW
title: "CYB 880-889 · 08.20.00 — QKD"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: CYB
architecture_name: "Cybersecurity Architecture"
master_range: "800–899"
code_range: "880-889"
section: "08"
section_title: "Criptografía Post-Cuántica y Seguridad Cuántica"
subject: "00"
subject_title: "General Information"
subsection: "20"
subsection_title: "QKD"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-SPACE]
orb_function_support: [ORB-LEG, ORB-PMO]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# CYB 880-889 · Section 08 · Subsection 20 — QKD

## 1. Purpose

Overview entry-point for the *QKD* subsection within the `880-889` code range (Section `08` — *Criptografía Post-Cuántica y Seguridad Cuántica*) of the **CYB** architecture band (*Cybersecurity Architecture*, master range `800–899`).

This subsubject (`00 Overview`) introduces the CYB 880-889.20.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *QKD* slice of the parent code range `880-889`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `CYB` — Cybersecurity Architecture |
| Master range | `800–899` |
| Code range | `880-889` |
| Section | `08` — Criptografía Post-Cuántica y Seguridad Cuántica |
| Subject | `00` — General Information |
| Subsection | `20` — QKD |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-SPACE |
| ORB support | ORB-LEG, ORB-PMO |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/800-899_CYB/880-889_Criptografia-Post-Cuantica-y-Seguridad-Cuantica/20_QKD/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **CYB §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `880-889` row (Section `08` — Criptografía Post-Cuántica y Seguridad Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^iso27001]: **ISO/IEC 27001:2022 — Information security management systems — Requirements** — Information security management baseline for CYB `800-899`.

[^nist80053]: **NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations** — Security and privacy controls catalogue applied to CYB programs.

[^do326a]: **ED-202A / DO-326A — Airworthiness Security Process Specification** — Airworthiness-security baseline for cyber-resilience of airborne systems referenced by CYB.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ISO/IEC 27001:2022 — Information security management systems — Requirements[^iso27001]
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations[^nist80053]
- ED-202A / DO-326A — Airworthiness Security Process Specification[^do326a]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

