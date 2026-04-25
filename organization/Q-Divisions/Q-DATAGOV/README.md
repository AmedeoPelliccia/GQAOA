---
title: "Q-DATAGOV — Gobierno del Dato, Normas, Documentación y CSDB"
id: GQAOA-ORG-QDIV-Q-DATAGOV-001
version: "1.0.0"
date: 2026-04-25
classification: Confidencial del Consorcio
author: "Q-DATAGOV Division Lead / CTO Office"
status: α
type: division-readme
program: GQAOA
division: Q-DATAGOV
domain: "Gobierno del Dato, Normas, Documentación, CSDB"
language: es
tags:
  - Q-DATAGOV
  - data-governance
  - S1000D
  - CSDB
  - BREX
  - SNS
  - LUTNDR
  - configuration-management
parent: "../Readme.md"
---

# Q-DATAGOV — Gobierno del Dato, Normas, Documentación y CSDB
> *El sistema nervioso documental del programa: datos, estándares y trazabilidad desde el concepto hasta el retiro.*

**Identificador:** GQAOA-ORG-QDIV-Q-DATAGOV-001
**Versión:** 1.0.0 · **Fecha:** 25 de abril de 2026 · **Estado:** α

---
## Glosario de Términos y Acrónimos

| Acrónimo / Término | Definición completa | Referencia externa |
|--------------------|--------------------|--------------------|
| **ACT** | *Applicability Cross-reference Table* — tabla S1000D que vincula atributos de aplicabilidad con los DMs correspondientes | [S1000D.net](https://www.s1000d.net/) |
| **ASD-STE100** | *Simplified Technical English* — especificación ASD para redacción técnica clara y sin ambigüedades | [ASD-STE100](https://www.asd-ste100.org/) |
| **BREX** | *Business Rules Exchange* — objeto S1000D con reglas de negocio para validar Data Modules del programa | [S1000D.net](https://www.s1000d.net/) |
| **CCT** | *Conditions Cross-reference Table* — tabla S1000D que mapea condiciones lógicas de aplicabilidad | [S1000D.net](https://www.s1000d.net/) |
| **CM** | *Configuration Management* — disciplina que gestiona la identificación, control y auditoría del estado de configuración | [IEEE 828](https://standards.ieee.org/ieee/828/4278/) |
| **CMP** | *Configuration Management Plan* — documento que establece las políticas y procedimientos de gestión de configuración | [IEEE 828](https://standards.ieee.org/ieee/828/4278/) |
| **CSA** | *Configuration Status Accounting* — registro del estado actualizado de todos los ítems de configuración | *(CMII best practice)* |
| **CSDB** | *Common Source DataBase* — repositorio centralizado de documentación técnica S1000D | [S1000D.net](https://www.s1000d.net/) |
| **DITA** | *Darwin Information Typing Architecture* — estándar OASIS de autoría modular XML; complementario a S1000D | [OASIS DITA](https://www.oasis-open.org/committees/dita/) |
| **DM** | *Data Module* — unidad atómica de información en S1000D, identificada por un código único (DMC) | [S1000D.net](https://www.s1000d.net/) |
| **DML** | *Data Module List* — lista de todos los DMs planificados o existentes en un proyecto S1000D | [S1000D.net](https://www.s1000d.net/) |
| **ECO** | *Engineering Change Order* — orden de cambio de ingeniería que formaliza una modificación en la configuración | *(CM best practice)* |
| **GDPR** | *General Data Protection Regulation* — Reglamento UE 2016/679 de protección de datos personales | [GDPR](https://gdpr-info.eu/) |
| **ICD** | *Interface Control Document* — documento que define la interfaz técnica entre dos sistemas o subsistemas | *(SE best practice)* |
| **IETP** | *Interactive Electronic Technical Publication* — publicación técnica electrónica interactiva conforme a S1000D | [S1000D.net](https://www.s1000d.net/) |
| **iSpec 2200** | Especificación ATA para sistemas de información de mantenimiento de aeronaves | [A4A iSpec 2200](https://www.airlines.org/dataset/ispec-2200/) |
| **LUTNDR** | Registro centralizado de tecnologías del programa GQAOA (en uso / nueva proyección / disuso / riassetti) | *(GQAOA-UTA-LUTNDR-001)* |
| **PCT** | *Product Cross-reference Table* — tabla S1000D que vincula productos con DMs y condiciones | [S1000D.net](https://www.s1000d.net/) |
| **S1000D** | Especificación internacional ASD/AIA/ATA para documentación técnica modular XML (Issue 5.0) | [S1000D.net](https://www.s1000d.net/) |
| **SNS** | *Standard Numbering System* — sistema de numeración jerárquico S1000D para identificar elementos de sistema | [S1000D.net](https://www.s1000d.net/) |
| **SSOT** | *Single Source of Truth* — principio: una única fuente autorizada para cada dato técnico | *(Data Governance best practice)* |


---

## 1. Misión y Alcance

Q-DATAGOV es la división técnica responsable del gobierno del dato, la gestión documental, la arquitectura de información y el Common Source DataBase (CSDB[^1]) del programa GQAOA. Su alcance cubre la definición y mantenimiento de estándares de documentación (S1000D[^2], ASD-STE100, iSpec 2200), la gestión del ciclo de vida de datos técnicos, la arquitectura de los Data Modules (DMs), y el esquema BREX[^3]/SNS[^4] del programa.

Q-DATAGOV actúa como la fuente única de verdad (SSOT[^5]) para toda la documentación técnica del programa, garantizando la trazabilidad, la coherencia semántica y la interoperabilidad de los datos entre todas las Q-Divisions y con los sistemas de los operadores y autoridades reguladoras.

---

## 2. Responsabilidades Clave

- **CSDB y S1000D:** Operación y mantenimiento del Common Source DataBase, incluyendo esquemas XML, BREX, SNS, ICNs y Data Module Lists (DML).
- **Estándares de documentación:** Definición y custodia de los estándares de autoría técnica del programa (S1000D, ASD-STE100 Simplified Technical English, DITA).
- **Gestión del ciclo de vida de datos:** Implementación del SSOT (Single Source of Truth) con control de versiones, configuración y trazabilidad de todos los artefactos técnicos.
- **Interface Control Documents (ICDs):** Coordinación de la publicación y control de cambios de los ICDs entre subsistemas y Q-Divisions.
- **LUTNDR — Registro de Tecnologías:** Mantenimiento del LUT_REGISTER.yaml y LUT_CIRCULARITY.yaml conforme a la especificación LUTNDR.
- **Arquitectura de información:** Diseño del esquema de metadatos, aplicabilidades (ACT/PCT/CCT) y modelo de datos del programa.
- **Gestión de configuración (CM):** Coordinación del Configuration Status Accounting (CSA) y del Configuration Management Plan (CMP).
- **Interoperabilidad con sistemas externos:** Publicación de datos en formatos IETP, exportación hacia sistemas de los operadores y autoridades de certificación.

---

## 3. Entregables Clave

| ID | Descripción | Tipo | Estado |
|----|-------------|------|--------|
| Q-DATAGOV-01-CSDB-SCHEMA.xml | Esquema XML maestro del CSDB GQAOA (S1000D Iss. 5.0) | XML | α |
| Q-DATAGOV-02-BREX-MASTER.xml | Business Rules Exchange Object maestro del programa | XML | α |
| Q-DATAGOV-03-SNS-CATALOG.xml | Standard Numbering System — catálogo completo del programa | XML | α |
| Q-DATAGOV-04-DML-MASTER.xml | Data Module List maestra (todas las Q-Divisions) | XML | α |
| Q-DATAGOV-05-DATA-GOV-PLAN.md | Plan de Gobierno del Dato — políticas, roles y procesos | MD | α |
| Q-DATAGOV-06-CM-PLAN.md | Plan de Gestión de Configuración (CMP) del programa | MD | α |
| Q-DATAGOV-07-APPLICABILITY-MODEL.md | Modelo de aplicabilidad S1000D (ACT/PCT/CCT — 9 atributos) | MD | α |

---

## 4. RACI de Dominio

| Actividad | Q-DATAGOV Lead | Co-Q-Divisions (C) | ORB Support (C/I) |
|-----------|---------------|-------------------|-------------------|
| Operación y mantenimiento CSDB | **A**/R | Todas las Q-Divisions (C) | ORB-IT (R) |
| Definición estándares S1000D / BREX | **A**/R | Q-SCIRES (C), Q-GROUND (C) | ORB-LEG (I) |
| Gestión de configuración (CMP) | **A**/R | ORB-PMO (R), Q-SCIRES (C) | ORB-PMO (R) |
| ICDs — publicación y control de cambios | **A**/R | Todas las Q-Divisions (R) | ORB-PMO (I) |
| LUTNDR — registro de tecnologías | **A**/R | Q-GREENTECH (C), Q-SCIRES (C) | ORB-CSR (I) |
| Modelo de aplicabilidad ACT/PCT/CCT | **A**/R | Q-SCIRES (C), Q-HPC (C) | ORB-LEG (I) |
| Publicaciones técnicas (AMM, SRM, IPC) | **A**/R | Q-STRUCTURES (R), Q-GROUND (R) | ORB-PMO (I) |
| Exportación IETP para operadores | **A**/R | Q-GROUND (C), Q-HPC (C) | ORB-MKTG (I) |

```mermaid
graph LR
    QDATA["Q-DATAGOV"]
    CSDB["CSDB\n(S1000D)"]
    BREX["BREX/SNS\nEsquemas"]
    ICD["ICDs\n(Control Interfaz)"]
    QDATA -->|"opera"| CSDB
    CSDB -->|"valida con"| BREX
    QDATA -->|"publica"| ICD
    ICD -->|"referencia"| CSDB
```

---

## 5. Interfaces Clave

### Con otras Q-Divisions

| Q-Division | Qué se intercambia | Dirección |
|------------|-------------------|-----------|
| Todas (10) | Entrega de DMs, ICDs y datos técnicos en el CSDB | Todas → Q-DATAGOV |
| Q-HPC | Datasets de simulación; metadatos de modelos IA/cuánticos | Bidireccional |
| Q-GROUND | Contenido de AMM/SRM/IPC para publicación | Q-GROUND → Q-DATAGOV |
| Q-SCIRES | Datos de ensayo y certificación para inclusión en CSDB | Q-SCIRES → Q-DATAGOV |
| Q-GREENTECH | LUT_REGISTER.yaml y LUT_CIRCULARITY.yaml | Q-GREENTECH → Q-DATAGOV |
| Q-SPACE | ICDs de comunicaciones satélite y enlace de datos | Q-SPACE → Q-DATAGOV |

### Con unidades ORB

| ORB Unit | Naturaleza de la interacción |
|----------|------------------------------|
| ORB-IT | Infraestructura del CSDB (servidores, backups, acceso), seguridad de datos |
| ORB-LEG | Cumplimiento S1000D, iSpec 2200, GDPR para datos de operadores |
| ORB-PMO | Integración del CMP con el cronograma maestro del programa |
| ORB-HR | Formación en herramientas de autoría S1000D y CSDB para todo el personal técnico |

---

## 6. KPIs del Dominio

| KPI | Objetivo | Fuente |
|-----|----------|--------|
| Cobertura de DMs en CSDB (vs. DML maestra) | ≥ 98% | Q-DATAGOV-04-DML-MASTER |
| Tasa de validación BREX (DMs válidos) | ≥ 99.5% | CSDB/s1000d_validator.py |
| Tiempo medio de publicación de un DM (autoría → CSDB) | ≤ 5 días hábiles | Q-DATAGOV-05-DATA-GOV-PLAN |
| Trazabilidad de requisitos a DMs (bidireccional) | 100% | Q-DATAGOV-06-CM-PLAN |
| Integridad del LUT_REGISTER.yaml (tecnologías registradas) | 100% cobertura de tecnologías activas | LUTNDR spec |

---

## 7. Riesgos Específicos

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Fragmentación de datos por herramientas propietarias no integradas | Alto | Media | Mandato de uso de CSDB/S1000D para todos los artefactos; auditorías trimestrales |
| Pérdida de trazabilidad requisito-entregable en cambios de configuración | Alto | Media | Control de cambios integrado en CSDB; proceso ECO obligatorio |
| Violación de GDPR en exportación de datos de operadores | Crítico | Baja | Cláusulas contractuales con ORB-LEG; anonimización de datos sensibles |
| Deuda técnica en el esquema BREX ante evolución del estándar S1000D | Medio | Media | Suscripción activa al ASD S1000D Steering Committee; revisión anual del BREX |

---

## 8. Referencias

### Internas
- [Matriz RACI Maestra Q-Divisions](../Readme.md)
- [Documento Organizacional Maestro GQAOA](../../README.md)
- [AMPEL360-BWB-Q100 Docs](../../../programs/AMPEL360/AMPEL360-BWB-Q100/Docs/readme.md)
- [CSDB S1000D Validator](../../../CSDB/s1000d_validator.py)
- [LUTNDR — Registro de Tecnologías](../../../OPT-INS_FRAMEWORK/GQAOA-UTA-LUTNDR-001.md)
- [CSDB APPLICABILITY Model](../../../CSDB/readme.md)

### Externas — Normativa y Estándares
| Referencia | Descripción | Enlace |
|-----------|-------------|--------|
| S1000D Issue 5.0 | International spec. for technical publications | [s1000d.net](https://www.s1000d.net/) |
| ASD-STE100 Issue 8 | Simplified Technical English specification | [asd-ste100.org](https://www.asd-ste100.org/) |
| A4A iSpec 2200 | Information Standards for Aviation Maintenance | [airlines.org](https://www.airlines.org/dataset/ispec-2200/) |
| OASIS DITA 1.3 | Darwin Information Typing Architecture | [oasis-open.org](https://www.oasis-open.org/committees/dita/) |
| GDPR (EU) 2016/679 | General Data Protection Regulation | [gdpr-info.eu](https://gdpr-info.eu/) |
| IEEE 828-2012 | Configuration Management in Systems and Software | [ieee.org](https://standards.ieee.org/ieee/828/4278/) |


## Notas

[^1]: **CSDB** (Common Source DataBase): repositorio centralizado de documentación técnica conforme a S1000D; almacena Data Modules, Publication Modules, ICNs y metadatos de aplicabilidad para todo el programa.
[^2]: **S1000D**: especificación internacional ASD/AIA/ATA para la producción y distribución de documentación técnica de sistemas de defensa y transporte; basada en XML y módulos de datos reutilizables.
[^3]: **BREX** (Business Rules Exchange): objeto S1000D que encapsula las reglas de negocio del programa (valores permitidos, estructuras obligatorias, restricciones semánticas) y se usa para validar todos los Data Modules.
[^4]: **SNS** (Standard Numbering System): sistema de numeración jerárquico S1000D que asigna identificadores únicos a los elementos del sistema, equivalente al sistema ATA de capítulos pero más flexible.
[^5]: **SSOT** (Single Source of Truth): principio de arquitectura de datos según el cual existe una única fuente autorizada para cada dato, evitando inconsistencias por copias divergentes.

**[FIN DEL DOCUMENTO]**
