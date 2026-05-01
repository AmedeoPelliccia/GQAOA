---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-040-03-MOORING-STORAGE-AND-RETURN-TO-SERVICE
title: "ATLAS 000-009 · 00.040.03 — Mooring, Storage and Return-to-Service"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subject: "00"
subject_title: "General Information"
subsection: "040"
subsection_title: "operaciones básicas"
subsubject: "03"
subsubject_title: "Mooring, Storage and Return-to-Service"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 000-009 · Section 00 · Subsection 040 · Subsubject 03 — Mooring, Storage and Return-to-Service

## 1. Purpose

Defines the **mooring, storage and return-to-service** procedures under ATLAS `000-009.040` *operaciones básicas*: short-term mooring (high-wind / weather), short-/long-term storage preservation, and the inspection / fluid replenishment sequence required to return the airframe to service. Published as S1000D procedural data modules[^s1000d] under ATA iSpec 2200 Chapter 10 conventions[^ata2200], in conformance with the controlled Q+ATLANTIDE baseline[^baseline].

## 2. Scope

- Covers the *Mooring, Storage and Return-to-Service* subsubject (`03`) of subsection `040` *operaciones básicas*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Activity classes in scope: **mooring** (high-wind, severe weather), **short-term storage**, **long-term storage / preservation**, **engine and system pickling**, **return-to-service inspection**, **fluid replenishment**.
- Aligned with ATA iSpec 2200 Ch. 10[^ata2200], ATA Spec 100 numbering[^ataspec100], S1000D procedural DM schema[^s1000d] and AS9100D safety controls[^as9100d].

## 3. Diagram

The diagram below shows the mooring / storage / return-to-service state machine an airframe traverses between active operation and short- or long-term preservation.

```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> Mooring: high wind / weather
    Mooring --> Active: weather clear
    Active --> ShortTermStorage: < 30 days
    ShortTermStorage --> Active: pre-flight checks
    Active --> LongTermStorage: >= 30 days
    LongTermStorage --> Pickling: engines / systems pickled
    Pickling --> RTSInspection
    ShortTermStorage --> RTSInspection
    RTSInspection --> Replenish: fluids replenished
    Replenish --> Active
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subject | `00` — General Information |
| Subsection | `040` — operaciones básicas |
| Subsubject | `03` — Mooring, Storage and Return-to-Service |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/040_operaciones-basicas/` |
| Document | `03_Mooring-Storage-and-Return-to-Service.md` (this file) |
| Parent subsection | [`00_Overview.md`](./00_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `000-009` row (Section `00` — Información General y Servicio, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry standard for digital aircraft maintenance information; governs chapter / section / subject numbering inherited by ATLAS `000-099`.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Predecessor numbering scheme that established the 00–99 chapter map mirrored by ATLAS sub-ranges.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used across ATLAS technical publications.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
