# Q-INDUSTRY — Fabricación, Ensamblaje y Producción
> *De la materia prima al avión certificado: excelencia en manufactura avanzada y cadena de valor europea.*

**Identificador:** GQAOA-ORG-QDIV-Q-INDUSTRY-001
**Versión:** 1.0.0 · **Fecha:** 25 de abril de 2026 · **Estado:** α

---

## 1. Misión y Alcance

Q-INDUSTRY es la división técnica responsable de la planificación, ejecución y control de todos los procesos de fabricación, ensamblaje y producción del programa GQAOA. Su alcance cubre desde la ingeniería de producción (DFM/DFA) hasta la aprobación de la organización de producción conforme a EASA Part 21G y Part 145, incluyendo la gestión de la cadena de suministro de nivel 1 y 2.

La división es propietaria de la Final Assembly Line (FAL), del Manufacturing Process Instructions (MPIs), del sistema de control de calidad (AOG/SPC) y de la cualificación de proveedores estratégicos. Q-INDUSTRY trabaja en estrecha colaboración con Q-STRUCTURES (especificaciones de materiales y tolerancias), Q-GREENTECH (procesos de sistemas de energía) y Q-GROUND (integración con GSE de producción).

---

## 2. Responsabilidades Clave

- **Ingeniería de producción (DFM/DFA):** Asegurar la fabricabilidad y la montabilidad del diseño; generación de Manufacturing Process Instructions (MPIs).
- **Final Assembly Line (FAL):** Planificación, secuenciación y control de la línea de ensamblaje final, incluyendo la integración de sistemas.
- **Control de calidad (QA/QC):** Implementación del sistema de control estadístico de proceso (SPC), gestión de no conformidades y AOG (Aircraft on Ground) decisions.
- **Aprobación Part 21G / Part 145:** Obtención y mantenimiento de la aprobación EASA de organización de producción y de mantenimiento en base.
- **Gestión de la cadena de suministro:** Cualificación, seguimiento y auditoría de proveedores de nivel 1 y 2; gestión de riesgos de suministro.
- **Planificación MPS/MRP:** Desarrollo y mantenimiento del Master Production Schedule y Material Requirements Planning.
- **Automatización y robótica:** Integración de sistemas de fabricación automatizada (robots de ensamblaje, células automatizadas) conforme a OGATA 600-609.
- **Lean Manufacturing y eficiencia:** Implementación de metodologías lean, six-sigma y mejora continua en todos los procesos de producción.

---

## 3. Entregables Clave

| ID | Descripción | Tipo | Estado |
|----|-------------|------|--------|
| Q-INDUSTRY-01-MPS-MASTER.xlsx | Master Production Schedule — planificación de producción a 5 años | XLSX | α |
| Q-INDUSTRY-02-FAL-SEQUENCE-PLAN.md | Plan de secuenciación de la Final Assembly Line (FAL) | MD | α |
| Q-INDUSTRY-03-MPI-SET.xml | Set de Manufacturing Process Instructions (S1000D XML) | XML | β |
| Q-INDUSTRY-04-QUALITY-PLAN.md | Plan de Calidad de Producción (QAP) — SPC, inspección, NC | MD | α |
| Q-INDUSTRY-05-SUPPLIER-QUAL-MATRIX.xlsx | Matriz de cualificación de proveedores nivel 1 y 2 | XLSX | α |
| Q-INDUSTRY-06-PART21G-APPROVAL-DOSSIER.md | Dossier de aprobación organización de producción (Part 21G) | MD | β |
| Q-INDUSTRY-07-AUTOMATION-SPEC.md | Especificación de sistemas de fabricación automatizada (robots) | MD | β |

---

## 4. RACI de Dominio

| Actividad | Q-INDUSTRY Lead | Co-Q-Divisions (C) | ORB Support (C/I) |
|-----------|----------------|-------------------|-------------------|
| Master Production Schedule (MPS) | **A**/R | Q-STRUCTURES (C), Q-GREENTECH (C) | ORB-PROC (C), ORB-FIN (C) |
| Ingeniería de producción (DFM/DFA) | **A**/R | Q-STRUCTURES (R), Q-MECHANICS (C) | ORB-PMO (I) |
| Final Assembly Line (FAL) | **A**/R | Q-MECHANICS (R), Q-GROUND (R) | ORB-PROC (C) |
| Control de calidad (SPC/NC) | **A**/R | Q-STRUCTURES (C), Q-SCIRES (C) | ORB-LEG (C) |
| Cualificación de proveedores | **A**/R | Q-GREENTECH (C), Q-STRUCTURES (C) | ORB-PROC (C), ORB-LEG (C) |
| Aprobación Part 21G/Part 145 | **A**/R | Q-DATAGOV (R), Q-SCIRES (C) | ORB-LEG (C) |
| Automatización FAL (robots OGATA 600) | **A**/R | Q-HPC (C), Q-MECHANICS (C) | ORB-IT (C) |
| Gestión de no conformidades (NC) | **A**/R | Q-STRUCTURES (C), Q-SCIRES (C) | ORB-LEG (C), ORB-PMO (I) |

```mermaid
graph LR
    QIND["Q-INDUSTRY"]
    FAL["Final Assembly\nLine (FAL)"]
    QUALITY["Control\nCalidad (SPC)"]
    SUPPLY["Cadena\nSuministro"]
    QIND -->|"secuencia"| FAL
    FAL -->|"métricas NC"| QUALITY
    QIND -->|"gestiona"| SUPPLY
    SUPPLY -->|"materiales"| FAL
```

---

## 5. Interfaces Clave

### Con otras Q-Divisions

| Q-Division | Qué se intercambia | Dirección |
|------------|-------------------|-----------|
| Q-STRUCTURES | Especificaciones de materiales, tolerancias de fabricación, DFM feedback | Bidireccional |
| Q-MECHANICS | Procedimientos de instalación de actuadores, tuberías, sistemas mecánicos | Q-MECH → Q-IND |
| Q-GREENTECH | Procesos de fabricación de packs de baterías y sistemas H₂ | Bidireccional |
| Q-GROUND | Integración FAL con GSE de producción; entrega de aeronave al cliente | Q-IND → Q-GROUND |
| Q-SCIRES | Inspección de componentes; ensayos de aceptación de producción | Bidireccional |
| Q-DATAGOV | Publicación de MPIs y work instructions en CSDB | Q-IND → Q-DATAGOV |

### Con unidades ORB

| ORB Unit | Naturaleza de la interacción |
|----------|------------------------------|
| ORB-PROC | Gestión de contratos con proveedores; cualificación y auditoría de proveedores |
| ORB-FIN | Presupuesto de producción; control de CAPEX en equipos de FAL; ROI robótica |
| ORB-LEG | Cumplimiento Part 21G/145, REACH, normativa laboral de fabricación |
| ORB-HR | Formación en fabricación avanzada, certificación de operarios |
| ORB-PMO | Seguimiento de cadencia de producción vs. cronograma maestro |

---

## 6. KPIs del Dominio

| KPI | Objetivo | Fuente |
|-----|----------|--------|
| Takt time FAL (tiempo entre aviones entregados) | ≤ 4 aviones/mes en producción pico | Q-INDUSTRY-01-MPS-MASTER |
| Tasa de no conformidades en FAL (NCs/aeronave) | ≤ 5 NCs mayor por aeronave | Q-INDUSTRY-04-QUALITY-PLAN |
| On-time delivery de proveedores nivel 1 | ≥ 95% | Q-INDUSTRY-05-SUPPLIER-QUAL-MATRIX |
| Cobertura de automatización en operaciones FAL | ≥ 60% de operaciones por robot | Q-INDUSTRY-07-AUTOMATION-SPEC |
| Primer vuelo sin AOG por causa de producción | 0 AOGs post-entrega año 1 | Q-INDUSTRY-04-QUALITY-PLAN |

---

## 7. Riesgos Específicos

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Retraso en obtención de aprobación Part 21G por EASA | Alto | Media | Engagement temprano con EASA; auditorías de preparación (mock audit) con ORB-LEG |
| Ruptura de cadena de suministro de materiales compuestos | Alto | Media | Inventario de seguridad; dual-sourcing para materiales críticos |
| Defectos de fabricación en packs de baterías HV | Crítico | Baja | Celdas de prueba destructiva por lote; inspección 100% por rayos X |
| Insuficiencia de personal cualificado para compuestos CFRP | Medio | Alta | Programa de formación con ORB-HR; partnerships con escuelas de FP aeroespacial |

---

## 8. Referencias

- [Matriz RACI Maestra Q-Divisions](../Readme.md)
- [Documento Organizacional Maestro GQAOA](../../README.md)
- [AMPEL360-BWB-Q100 Docs](../../../programs/AMPEL360/AMPEL360-BWB-Q100/Docs/readme.md)
- [Robbbo-T Robotics PRD (OGATA 600)](../../../programs/Robbbo-T_Robotics_PRD/Readme.md)

---

**[FIN DEL DOCUMENTO]**
