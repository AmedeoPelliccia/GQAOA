---
title: "STANDARDS / IDEALE-ESG / MAPS / Q+ATLANTIDE — Map Index"
id: STD-IDEALE-MAPS-QATL-README
version: "1.0.0"
date: 2026-04-26
classification: open-technical-taxonomy
author: "GAIA-QAO / IDEALE-ESG"
status: controlled-baseline
type: map-index
program: GAIA-QAO
division: Q-DATAGOV
domain: "IDEALE-ESG × Q+ATLANTIDE crosslink artefacts"
language: en
tags:
  - IDEALE-ESG
  - Q+ATLANTIDE
  - crosslink
  - map
  - standards
parent: "../../README.md"
---

# STANDARDS / IDEALE-ESG / MAPS / Q+ATLANTIDE

## Purpose

This namespace holds **mapping and crosslinking artefacts** between the
[`IDEALE-ESG.panpara.eu/`](../../../../IDEALE-ESG.panpara.eu/README.md)
namespace (IDEALE-ESG frameworks decomposed along the OPT-IN axes) and the
[`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
baseline (controlled `000-999` architecture-band taxonomy with its
**ATLAS-1000** umbrella subpart).

The maps in this folder are read-only crosslink documents: they do not
duplicate normative content. Each map cell points back to:

- the authoritative IDEALE-ESG axis page (under `IDEALE-ESG.panpara.eu/`), and
- the authoritative Q+ATLANTIDE band entry (in `organization/Q+ATLANTIDE.md`).

## Document Metadata

| Field | Value |
|---|---|
| Document ID | STD-IDEALE-MAPS-QATL-README |
| Baseline | v1.0.0 |
| Status | controlled-baseline |
| Classification | open-technical-taxonomy |
| Owner | GAIA-QAO / IDEALE-ESG |
| Maintainer | Q-DATAGOV |
| Created | 2026-04-26 |
| Last updated | 2026-04-26 |

## Scope

Q+ATLANTIDE provides ten architecture bands across the controlled `000-999`
range. IDEALE-ESG decomposes each framework along the five OPT-IN axes
(`O-Organizations`, `P-Programmes`, `T-Technologies`, `I-Infrastructures`,
`N-Neural-Networks`). The maps in this folder express the crosslink between
the two structures, framework by framework.

## Maps

| Map | IDEALE-ESG framework | Target | Status |
|---|---|---|---|
| [`A-Aerospace-x-Q+ATLANTIDE.md`](A-Aerospace-x-Q+ATLANTIDE.md) | [`A-Aerospace/`](../../../../IDEALE-ESG.panpara.eu/A-Aerospace/README.md) | [`Q+ATLANTIDE`](../../../../organization/Q+ATLANTIDE.md) | controlled-baseline |

Additional framework maps (D-Defense, E-Energy, L-Logistics, E2-Economics,
E3-Environments, S-Social, G-Governance, I-Information) may be added later
under this same folder as separate `<framework>-x-Q+ATLANTIDE.md` files,
following the same conventions.

## Conventions

1. **No duplication.** Map cells reference (do not restate) the band focus
   and the OPT-IN axis role. Authoritative definitions remain in the source
   documents.
2. **Bidirectional links.** Each map links *into* both source namespaces, and
   the source namespaces link *back* to this folder via a Cross-Reference
   block (see `IDEALE-ESG.panpara.eu/A-Aerospace/README.md`).
3. **Crosslink granularity.** The primary mapping unit is
   `(IDEALE-ESG framework, OPT-IN axis) × (Q+ATLANTIDE architecture band)`.
   Subrange-level (e.g. `ATLAS 050-059`) crosslinks may be added when an
   axis-to-subrange relationship is materially distinct from the band-level
   default.
4. **Governance markers.** Cells touching DTTA (`200-299`), CYB (`800-899`),
   or QCSAA (`900-999`) inherit Q+ATLANTIDE Note `N-006`: additional
   governance, evidence packages and access controls beyond the baseline
   trace record are required.
## Cross-References

- IDEALE-ESG namespace index: [`IDEALE-ESG.panpara.eu/README.md`](../../../../IDEALE-ESG.panpara.eu/README.md)
- Q+ATLANTIDE baseline: [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- OPT-IN axes definition: [`IDEALE-ESG.panpara.eu/README.md`](../../../../IDEALE-ESG.panpara.eu/README.md) (§ OPT-IN Axes)
- Architecture-band catalogue: [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) (§ 3. Consolidated Architecture Table)

**[END OF DOCUMENT]**
