---
title: "Q-AIR — Aerodinámica y Control de Vuelo"
id: GQAOA-ORG-QDIV-Q-AIR-001
version: "1.0.0"
date: 2026-04-25
classification: Confidencial del Consorcio
author: "Q-AIR Division Lead / CTO Office"
status: α
type: division-readme
program: GQAOA
division: Q-AIR
domain: "Aerodinámica, Control de Vuelo"
language: es
tags:
  - Q-AIR
  - aerodynamics
  - flight-control
  - FCS
  - CFD
  - BWB
parent: "../Readme.md"
---

# Q-AIR — Aerodinámica y Control de Vuelo
> *El dominio que da forma al aire: perfiles, cargas y sistemas de vuelo inteligentes para la aeronave del futuro.*

**Identificador:** GQAOA-ORG-QDIV-Q-AIR-001
**Versión:** 1.0.0 · **Fecha:** 25 de abril de 2026 · **Estado:** α

---

## 1. Misión y Alcance

Q-AIR es la división técnica responsable del diseño, análisis y validación de todos los sistemas aerodinámicos y de control de vuelo (FCS[^1]) del programa GQAOA. Su alcance abarca desde la definición conceptual de la envolvente de vuelo hasta la certificación de los perfiles de sustentación conforme a CS-25/FAR-25[^2], los sistemas fly-by-wire y los algoritmos de control adaptativo asistidos por IA.

La división lidera la integración multidisciplinar entre la aerodinámica exterior (CFD[^3], túnel de viento), la dinámica de vuelo (estabilidad y control) y los sistemas embarcados de gestión de vuelo (FMS/FCS), coordinando activamente con Q-STRUCTURES (cargas y aeroelasticidad[^4]), Q-HPC (optimización cuántica QAOA[^5]) y Q-MECHANICS (actuadores FCS).

---

## 2. Responsabilidades Clave

- **Diseño aerodinámico (Aero Shaping):** Definición de la geometría externa de la aeronave, optimización de perfiles alar y configuraciones BWB/convencionales.
- **Análisis CFD y validación experimental:** Simulaciones de fluidos computacionales de alta fidelidad y coordinación de campañas en túnel de viento.
- **Dinámica de vuelo y envolvente de operación:** Determinación de límites de velocidad, altitud, maniobra y cargas de vuelo; documentación de la Flight Envelope.
- **Sistemas de Control de Vuelo (FCS):** Diseño, integración y verificación del sistema fly-by-wire, leyes de control, y funciones de protección de envolvente.
- **Gestión del sistema FMS/FGCS:** Integración del Flight Management System con los módulos de optimización de ruta asistidos por Q-HPC.
- **Aeroelasticidad y cargas estructurales:** Generación del espectro de cargas de diseño para Q-STRUCTURES, incluyendo análisis flutter y divergencia.
- **Reducción de ruido aerodinámico:** Diseño de configuraciones de bajo ruido (high-lift devices, trailing edge treatment) en cumplimiento con ICAO Annex 16.
- **Interfaces con sistemas de propulsión:** Análisis de efectos de instalación del sistema propulsivo (nacelle, inlet) sobre el campo aerodinámico global.

---

## 3. Entregables Clave

| ID | Descripción | Tipo | Estado |
|----|-------------|------|--------|
| Q-AIR-01-AERO-DESIGN-SPEC.md | Especificación de diseño aerodinámico — perfiles, polar, Cl/Cd objetivos | MD | α |
| Q-AIR-02-CFD-BASELINE-REPORT.pdf | Informe de simulación CFD — configuración de referencia BWB-Q100 | PDF | α |
| Q-AIR-03-FLIGHT-ENVELOPE.xlsx | Envolvente de vuelo certificable: límites V-n, altitud, temperatura | XLSX | α |
| Q-AIR-04-FCS-ARCHITECTURE.md | Arquitectura del sistema de control de vuelo (FBW, leyes de control) | MD | β |
| Q-AIR-05-LOADS-SPECTRUM.hdf5 | Espectro de cargas de diseño para Q-STRUCTURES (fatiga + estático) | HDF5 | β |
| Q-AIR-06-FLUTTER-ANALYSIS.md | Análisis de aeroelasticidad y flutter — márgenes de estabilidad | MD | β |
| Q-AIR-07-WIND-TUNNEL-REPORT.pdf | Informe de ensayos en túnel de viento (campaña α) | PDF | β |

---

## 4. RACI de Dominio

| Actividad | Q-AIR Lead | Co-Q-Divisions (C) | ORB Support (C/I) |
|-----------|-----------|-------------------|-------------------|
| Diseño perfil aerodinámico BWB | **A**/R | Q-STRUCTURES (C), Q-HPC (C) | ORB-PMO (I) |
| CFD analysis — alta fidelidad | **A**/R | Q-HPC (R), Q-SCIRES (C) | ORB-PMO (I) |
| Definición de cargas de diseño | **A**/R | Q-STRUCTURES (R), Q-MECHANICS (C) | ORB-PMO (I) |
| Diseño leyes de control FCS | **A**/R | Q-HPC (C), Q-MECHANICS (R) | ORB-IT (C) |
| Análisis flutter y aeroelasticidad | **A**/R | Q-STRUCTURES (R), Q-SCIRES (C) | ORB-PMO (I) |
| Ensayos en túnel de viento | **A**/R | Q-SCIRES (R), Q-HPC (C) | ORB-PMO (I) |
| Integración FMS/FGCS | **A**/R | Q-HPC (R), Q-DATAGOV (C) | ORB-IT (C) |
| Reducción de ruido aerodinámico | **A**/R | Q-SCIRES (C), Q-STRUCTURES (C) | ORB-CSR (I) |

```mermaid
graph LR
    QAIR["Q-AIR"]
    CFD["CFD / Túnel Viento\n(campañas Q-SCIRES)"]
    FCS["FCS SW\n(DO-178C Q-HPC)"]
    LOADS["Espectro de Cargas\n→ Q-STRUCTURES"]
    QAIR -->|"diseño perfil"| CFD
    CFD -->|"datos correlación"| QAIR
    QAIR -->|"requisitos deflexión"| FCS
    QAIR -->|"cargas aero"| LOADS
```

---

## 5. Interfaces Clave

### Con otras Q-Divisions

| Q-Division | Qué se intercambia | Dirección |
|------------|-------------------|-----------|
| Q-STRUCTURES | Espectro de cargas aero (Q-AIR → Q-STR); datos de peso/rigidez (Q-STR → Q-AIR) | Bidireccional |
| Q-HPC | Resultados CFD de alta fidelidad; optimización cuántica de perfiles | Bidireccional |
| Q-MECHANICS | Requisitos de deflexión y fuerza de actuadores FCS | Q-AIR → Q-MECH |
| Q-GREENTECH | Efectos aerodinámicos de instalación de celdas de combustible/baterías | Bidireccional |
| Q-SCIRES | Datos de ensayo en túnel de viento; correlación CFD-experimento | Bidireccional |
| Q-DATAGOV | Publicación de ICDs y DMs aerodinámicos en CSDB | Q-AIR → Q-DATAGOV |

### Con unidades ORB

| ORB Unit | Naturaleza de la interacción |
|----------|------------------------------|
| ORB-PMO | Planificación de hitos, gestión de cambios técnicos, seguimiento del cronograma |
| ORB-LEG | Cumplimiento EASA CS-25, FAR 25, ICAO Annex 16; propiedad intelectual de perfiles |
| ORB-FIN | Estimación de costes de campañas CFD y túnel de viento; ROI de herramientas HPC |
| ORB-IT | Infraestructura HPC para CFD; licencias software (ANSYS, OpenFOAM) |

---

## 6. KPIs del Dominio

| KPI | Objetivo | Fuente |
|-----|----------|--------|
| Relación L/D máxima (crucero) | ≥ 23 (BWB-Q100) | CFD + Túnel de viento |
| Reducción consumo combustible vs. gen. 2020 | ≥ 50% por asiento-km | Q-AIR-02-CFD-BASELINE-REPORT |
| Nivel de ruido acumulado ICAO (Chapter 14) | ≤ −10 dB margen acumulado | Q-SCIRES datos de ensayo |
| Tiempo de cierre de ciclo CFD (alta fidelidad) | ≤ 72 h por configuración | Q-HPC infraestructura |
| Margen de flutter (VD) | ≥ 15% sobre velocidad de diseño | Q-AIR-06-FLUTTER-ANALYSIS |
| Cobertura de verificación FCS (DO-178C) | 100% MC/DC coverage | Q-HPC V&V reports |

---

## 7. Riesgos Específicos

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Desviación L/D por interacciones motor-célula BWB | Alto | Media | Iteraciones CFD-Q-STRUCTURES; campaña túnel viento incremental |
| Retraso en certificación DO-178C del FCS | Alto | Baja | Plan de V&V temprano; contratación de DER (Designated Engineering Representative) |
| Inestabilidad aeroelástica imprevista (flutter) | Crítico | Baja | Análisis flutter en cada baseline congelado; ensayo GVT temprano |
| Insuficiencia de recursos HPC para CFD LES | Medio | Media | Acuerdo de capacidad HPC con Q-HPC; uso de cloud burst |

---

## 9. Hoja de Ruta Tecnológica

| Tecnología / Capacidad | TRL Actual | TRL Objetivo | Año Objetivo | Hito Clave |
|------------------------|-----------|-------------|-------------|------------|
| CFD LES a alta fidelidad | TRL 6 | TRL 8 | 2030 | First Flight CFD-validated |
| Optimización cuántica QAOA de perfiles | TRL 3 | TRL 6 | 2032 | Demo en túnel de viento |
| FCS adaptativo con IA embarcada | TRL 4 | TRL 7 | 2034 | Certificación DO-178C nivel A |
| Reducción activa de ruido aerodinámico | TRL 4 | TRL 7 | 2033 | Validación Chapter 14 ICAO |
| Diseño aerodinámico BWB certificable | TRL 5 | TRL 9 | 2038 | Type Certificate EIS |

---

## 8. Referencias

- [Matriz RACI Maestra Q-Divisions](../Readme.md)
- [Documento Organizacional Maestro GQAOA](../../README.md)
- [AMPEL360-BWB-Q100 Docs](../../../programs/AMPEL360/AMPEL360-BWB-Q100/Docs/readme.md)
- [CSDB S1000D Validator](../../../CSDB/s1000d_validator.py)


## Notas

[^1]: **FCS** (Flight Control System): sistema de control de vuelo fly-by-wire que transmite las órdenes del piloto a las superficies de control mediante señales eléctricas en lugar de conexiones mecánicas directas.
[^2]: **CS-25 / FAR-25**: Certification Specifications for Large Aeroplanes (EASA) / Federal Aviation Regulations Part 25 (FAA) — requisitos de aeronavegabilidad para aviones de transporte de gran tamaño.
[^3]: **CFD** (Computational Fluid Dynamics): disciplina que aplica métodos numéricos para simular el comportamiento de fluidos; en aeronáutica se usa para predecir la aerodinámica sin necesidad exclusiva de ensayos físicos.
[^4]: **Aeroelasticidad**: fenómeno de interacción entre las fuerzas aerodinámicas, la inercia y la elasticidad de la estructura; incluye flutter, divergencia y respuesta en ráfagas.
[^5]: **QAOA** (Quantum Approximate Optimization Algorithm): algoritmo cuántico variacional que busca soluciones aproximadas a problemas de optimización combinatoria, desarrollado por Q-HPC en el programa GQAOA.

**[FIN DEL DOCUMENTO]**
