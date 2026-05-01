---
document_id: QATL-ATLAS-1000-ACV-710-719-01-020-00-OVERVIEW
title: "ACV 710-719 · 01.020.00 — charging/refuelling"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ACV
architecture_name: "Aerial City Viability / UAM Architecture"
master_range: "700–799"
code_range: "710-719"
section: "01"
section_title: "Vertipuertos y Heliplataformas"
subject: "00"
subject_title: "General Information"
subsection: "020"
subsection_title: "charging/refuelling"
subsubject: "00"
subsubject_title: "Overview"
primary_q_division: Q-GROUND
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-FIN, ORB-PMO]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ACV 710-719 · Section 01 · Subsection 020 — charging/refuelling

## 1. Purpose

Overview entry-point for the *charging/refuelling* subsection within the `710-719` code range (Section `01` — *Vertipuertos y Heliplataformas*) of the **ACV** architecture band (*Aerial City Viability / UAM Architecture*, master range `700–799`).

This subsubject (`00 Overview`) introduces the ACV 710-719.020.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *charging/refuelling* slice of the parent code range `710-719`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`01`–`99`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ACV` — Aerial City Viability / UAM Architecture |
| Master range | `700–799` |
| Code range | `710-719` |
| Section | `01` — Vertipuertos y Heliplataformas |
| Subject | `00` — General Information |
| Subsection | `020` — charging/refuelling |
| Subsubject | `00` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-FIN, ORB-PMO |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/700-799_ACV/710-719_Vertipuertos-y-Heliplataformas/020_charging-refuelling/` |
| Document | `00_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ACV §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `710-719` row (Section `01` — Vertipuertos y Heliplataformas, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^sae4754a]: **SAE ARP4754A — Guidelines for Development of Civil Aircraft and Systems** — Civil aircraft systems development baseline applied to ACV `700-799`.

[^easascvtol]: **EASA SC-VTOL — Special Condition for VTOL Aircraft** — Type-certification baseline for eVTOL / UAM aircraft within ACV.

[^rtcado178c]: **RTCA DO-178C — Software Considerations in Airborne Systems and Equipment Certification** — Airborne software assurance baseline used across ACV avionics.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- SAE ARP4754A — Guidelines for Development of Civil Aircraft and Systems[^sae4754a]
- EASA SC-VTOL — Special Condition for VTOL Aircraft[^easascvtol]
- RTCA DO-178C — Software Considerations in Airborne Systems and Equipment Certification[^rtcado178c]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

