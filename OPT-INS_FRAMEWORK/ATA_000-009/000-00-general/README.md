# ATA 000‑009: Información General y Servicio

**Programme:** AMPEL360 Q100 (AMPEL360-AIR-T)  
**OPT-IN Axis:** O — Organizations  
**Framework:** [OPT-INS_FRAMEWORK](../../Readme.md)  
**Version:** 1.0.0  
**Date:** 11 April 2026  
**Status:** 🟢 Active — Structure Established  

---

## Overview

This directory contains the ATA 000‑009 chapter tree for the GAIA-QAO ADVENT aircraft programme, following the **canonical leaf-node pattern** with SSOT lifecycle directories (LC01–LC14) and S1000D publication tree (PUB/AMM/CSDB).

## Node Index

| Node | Title | LC01 Seeded | KNOT Prefix |
|------|-------|:-----------:|-------------|
| `000-00-00-00` | Características Generales — General | ✅ | `KNOT-ATA000-00-00` |
| `000-00-00-90` | Características Generales — Glossary | — | — |
| `000-10-00-00` | Documentación Técnica — General | ✅ | `KNOT-ATA000-10-00` |
| `000-10-00-90` | Documentación Técnica — Glossary | — | — |
| `000-10-10-00` | Manuales Digitales S1000D — General | ✅ | `KNOT-ATA000-10-10` |
| `000-10-10-90` | Manuales Digitales S1000D — Glossary | — | — |

## Chapter Structure

```
000-00-general/
├── 000-00-00-caracteristicas-generales/
│   ├── 000-00-00-00-general/          (SSOT + PUB)
│   └── 000-00-00-90-glossary/         (SSOT + PUB)
└── 000-10-00-documentacion-tecnica/
    ├── 000-10-00-00-general/          (SSOT + PUB)
    ├── 000-10-00-90-glossary/         (SSOT + PUB)
    └── 000-10-10-manuales-s1000d/
        ├── 000-10-10-00-general/      (SSOT + PUB)
        └── 000-10-10-90-glossary/     (SSOT + PUB)
```

## Traceability

All documents follow the **ALICE → BOB DT → CHARLIE-T → GENTLE → BOOST** traceability chain as defined in the [OPT-INS Framework](../../Readme.md).
