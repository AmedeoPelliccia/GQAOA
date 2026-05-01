---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-020-03-MODIFICATION-STATUS
title: "ATLAS 000-009 · 00.020.03 — Modification Status"
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
subsection: "020"
subsection_title: "configuración"
subsubject: "03"
subsubject_title: "Modification Status"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 000-009 · Section 00 · Subsection 020 · Subsubject 03 — Modification Status

## 1. Purpose

Defines the **modification status** semantics under ATLAS `000-009.020` *configuración*: the registry of Service Bulletins (SB), Modifications (Mod), Airworthiness Directives (AD) and embodied changes that move an airframe from one configuration baseline to the next. Status values are exposed as the S1000D `modStatus` applicability property[^s1000d] and traced to ATA iSpec 2200 records[^ata2200], in conformance with the controlled Q+ATLANTIDE baseline[^baseline].

## 2. Scope

- Covers the *Modification Status* subsubject (`03`) of subsection `020` *configuración*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Object classes in scope: **Service Bulletins (SB)**, **Modifications (Mod)**, **Airworthiness Directives (AD)**, **embodiment records**, **status transitions** (planned → embodied → not-applicable).
- Surfaces values for the S1000D `modStatus` applicability property and the ATA iSpec 2200 modification register[^ata2200][^s1000d]; quality controls per AS9100D[^as9100d].

## 3. Diagram

The diagram below shows the state machine an SB / Mod / AD record traverses on a given airframe, from declaration through embodiment or formal exclusion.

```mermaid
stateDiagram-v2
    [*] --> Planned
    Planned --> InWork: kit released
    InWork --> Embodied: workpack closed
    Planned --> NotApplicable: applicability eval = false
    InWork --> Cancelled: SB withdrawn
    Embodied --> Superseded: replacement SB
    Embodied --> [*]
    NotApplicable --> [*]
    Cancelled --> [*]
    Superseded --> [*]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subject | `00` — General Information |
| Subsection | `020` — configuración |
| Subsubject | `03` — Modification Status |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/020_configuracion/` |
| Document | `03_Modification-Status.md` (this file) |
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
