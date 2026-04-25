# OGATA 600-10-10: Robots de 6 y 7 Ejes para Tareas de Ensamblaje y Soldadura

> **UTCS Classification:** OGATA 600-10-10
> **Parent:** 600-10-00 — Robots de Brazo Articulado y Cartesianos
> **Domain:** G7 — OGATA · Ground Automation (600–699)
> **ROBOT.INCs Classes:** ROBOT.INC-M (Manipuladores), ROBOT.INC-A (Assemblaggio)
> **Version:** 1.0 | **Status:** DRAFT
> **Date:** 2026-04-17
> **Author:** GQAOA, INC. — Robbbo-T Robotics PRD

---

## Table of Contents

1. [Scope and Purpose](#1-scope-and-purpose)
2. [Kinematic Architecture](#2-kinematic-architecture)
3. [Operational Envelopes](#3-operational-envelopes)
4. [Welding Applications](#4-welding-applications)
5. [Precision Assembly Applications](#5-precision-assembly-applications)
6. [Safety Standards and Compliance](#6-safety-standards-and-compliance)
7. [Risk Assessment Methodology](#7-risk-assessment-methodology)
8. [Human-Robot Interaction and Cell Design](#8-human-robot-interaction-and-cell-design)
9. [GQAOA Integration and UTCS Mapping](#9-gqaoa-integration-and-utcs-mapping)
10. [References](#10-references)

---

## 1. Scope and Purpose

This document provides a comprehensive technical overview of **6-axis and 7-axis articulated industrial robots** specifically engineered for **automated assembly and welding applications**. It serves as the authoritative reference for UTCS code **600-10-10** within the GQAOA On-Ground Automation Technology Architecture (OGATA).

### 1.1 Applicability

This specification applies to:

- Serial-link articulated manipulators with 6 or 7 revolute joints
- Automated and semi-automated welding cells (MIG, TIG, plasma, laser-hybrid)
- Precision assembly stations for aerospace, automotive, and electronics manufacturing
- Robotic cells operating within GQAOA-governed facilities (Robbbo-T/Factory program)

#### 1.1.1 Primary Deployment Site — Getafe Robotics FAL

The primary target of this specification is the **Airbus Getafe (Madrid, Spain) Final Assembly Line (FAL)** and its associated robotics cells (structural assembly, drilling/riveting, automated welding of metallic sub-assemblies, composite trimming/inspection). Consequently, **all applicable European Union and Spanish national regulations apply in addition to the international ISO/IEC standards listed below**. Where conflicts exist, the more stringent requirement governs, and the Spanish transposition of the EU directive prevails for legal compliance within Spanish territory.

Jurisdictional layering for any 600-10-10 cell deployed at Getafe FAL:

1. **EU level** — Machinery Regulation (EU) 2023/1230 (replacing Directive 2006/42/EC from 20 January 2027), Low Voltage Directive 2014/35/EU, EMC Directive 2014/30/EU, ATEX Directive 2014/34/EU, Use of Work Equipment Directive 2009/104/EC, Workplace Safety Framework Directive 89/391/EEC, REACH Regulation (EC) 1907/2006, CLP Regulation (EC) 1272/2008.
2. **Spanish national level** — Ley 31/1995 de Prevención de Riesgos Laborales (PRL); RD 1644/2008 (machinery — currently transposing 2006/42/EC); RD 1215/1997 (work equipment); RD 486/1997 (workplaces); RD 614/2001 (electrical risk); RD 681/2003 (ATEX); RD 374/2001 (chemical agents — welding fumes); RD 286/2006 (noise); RD 1311/2005 (mechanical vibration); RD 773/1997 (PPE); RD 488/1997 (display screen equipment for teach-pendant operators); ITC-MIE-AEM-2 (lifting/handling equipment associated with the cell).
3. **Aeronautical sector level** — EASA Part 21 Subpart G (Production Organisation Approval), Part 145 (Maintenance Organisation Approval), Airbus **AIPS** (Airbus Industrial Process Specifications) for welding/assembly, Airbus **AP** (Airbus Process) standards, and Airbus AITM/ABT test methods invoked by the relevant FAL work-package (A400M, Eurofighter Typhoon Spain workshare, C295/C295W, future FCAS demonstrators).
4. **Spanish technical guidance** — INSST (Instituto Nacional de Seguridad y Salud en el Trabajo) NTPs (Notas Técnicas de Prevención) applicable to robotic and welding operations (notably NTP 884 — robot industriales, NTP 494/495 — soldadura, NTP 1142 — colaborativos).

Compliance evidence for a Getafe-deployed cell shall therefore be assembled as a **dual-track dossier**: (a) the CE Declaration of Conformity / Technical File per the Machinery Regulation and (b) the Spanish PRL evaluation per Ley 31/1995, in addition to the GQAOA-internal artefacts defined in §6 and §9.

### 1.2 Normative References

#### 1.2.1 International (ISO/IEC/AWS)

| Standard | Title |
|----------|-------|
| ISO 10218-1:2011 | Robots and robotic devices — Safety requirements — Part 1: Robots |
| ISO 10218-2:2011 | Robots and robotic devices — Safety requirements — Part 2: Robot systems and integration |
| ANSI/RIA R15.06-2012 | Industrial Robots and Robot Systems — Safety Requirements |
| ISO/TS 15066:2016 | Robots and robotic devices — Collaborative robots |
| ISO 12100:2010 | Safety of machinery — General principles for design |
| ISO 13849-1:2023 | Safety of machinery — Safety-related parts of control systems — Part 1 |
| IEC 62061:2021 | Safety of machinery — Functional safety of E/E/PE control systems |
| IEC 61508 | Functional safety of E/E/PE safety-related systems |
| ISO 3691-4:2020 | Industrial trucks — Safety requirements — Driverless industrial trucks |
| ISO 9283:1998 | Manipulating industrial robots — Performance criteria and related test methods |
| AWS D8.1M | Specification for Automotive Weld Quality — Arc Welding |
| ISO 14731:2019 | Welding coordination — Tasks and responsibilities |

#### 1.2.2 European Union — Directives and Regulations (Getafe FAL applicability)

| Reference | Title / Subject |
|-----------|-----------------|
| Regulation (EU) 2023/1230 | Machinery Regulation (applicable from 20 January 2027; supersedes 2006/42/EC) |
| Directive 2006/42/EC | Machinery Directive (currently in force; CE marking obligation) |
| Directive 2014/35/EU | Low Voltage Directive (LVD) |
| Directive 2014/30/EU | Electromagnetic Compatibility (EMC) Directive |
| Directive 2014/34/EU | ATEX equipment in potentially explosive atmospheres |
| Directive 2009/104/EC | Use of work equipment by workers at work |
| Directive 89/391/EEC | OSH Framework Directive |
| Directive 2003/10/EC | Workers' exposure to noise |
| Directive 2002/44/EC | Workers' exposure to mechanical vibration |
| Regulation (EC) 1907/2006 | REACH — chemicals registration (welding consumables, lubricants) |
| Regulation (EC) 1272/2008 | CLP — classification, labelling and packaging |
| EN ISO 10218-1/-2 | Harmonised version of ISO 10218 (CE-marking presumption of conformity) |
| EN ISO 13849-1, EN 62061 | Harmonised functional-safety standards |
| EN ISO 12100 | Harmonised risk-assessment standard |

#### 1.2.3 Spanish National Law (Reino de España)

| Reference | Title / Subject |
|-----------|-----------------|
| Ley 31/1995, de 8 de noviembre | Prevención de Riesgos Laborales (PRL) |
| RD 1644/2008 | Normas para la comercialización y puesta en servicio de las máquinas (transposes 2006/42/EC) |
| RD 1215/1997 | Disposiciones mínimas de seguridad para la utilización de equipos de trabajo |
| RD 486/1997 | Disposiciones mínimas de seguridad y salud en los lugares de trabajo |
| RD 614/2001 | Disposiciones mínimas frente al riesgo eléctrico |
| RD 681/2003 | Protección frente a atmósferas explosivas (ATEX, lugar de trabajo) |
| RD 374/2001 | Protección frente a riesgos por agentes químicos (humos de soldadura) |
| RD 286/2006 | Protección de los trabajadores frente al ruido |
| RD 1311/2005 | Protección frente a vibraciones mecánicas |
| RD 773/1997 | Disposiciones mínimas para la utilización de equipos de protección individual (EPI) |
| RD 488/1997 | Pantallas de visualización (operadores de teach-pendant / HMI) |
| RD 39/1997 | Reglamento de los Servicios de Prevención |
| ITC-MIE-AEM-2 | Instrucción técnica complementaria — grúas torre y equipos de elevación asociados a la celda |
| INSST NTP 884, 494/495, 1142 | Notas Técnicas de Prevención — robots industriales, soldadura, robots colaborativos |

#### 1.2.4 Aeronautical Sector (Getafe FAL — Airbus / EASA)

| Reference | Title / Subject |
|-----------|-----------------|
| Regulation (EU) 748/2012 | EASA Initial Airworthiness — Part 21 (incl. Subpart G — Production Organisation Approval) |
| Regulation (EU) 1321/2014 | EASA Continuing Airworthiness — Part 145 (Maintenance Organisation Approval) |
| Airbus AIPS series | Airbus Industrial Process Specifications (welding, fastening, surface treatment, NDT applicable to FAL workshare) |
| Airbus AP series | Airbus Process standards invoked by the FAL work-package (A400M, Eurofighter, C295) |
| Airbus AITM / ABT | Airbus test methods for qualification of automated welding/assembly outputs |
| EN 9100:2018 | Aerospace Quality Management Systems (Getafe FAL accredited scope) |
| EN 4179 / NAS 410 | Qualification and approval of personnel for non-destructive testing of welded joints |

---

## 2. Kinematic Architecture

### 2.1 Six-Axis (6-DOF) Articulated Robots

The standard 6-axis industrial robot consists of a serial kinematic chain with six revolute joints, providing the **minimum degrees of freedom (DOF)** required to position and orient an end-effector arbitrarily within the robot's reachable workspace.

#### 2.1.1 Joint Configuration (Anthropomorphic Serial Chain)

```
Base (J1: Rotation) → Shoulder (J2: Pitch) → Elbow (J3: Pitch)
→ Wrist-1 (J4: Roll) → Wrist-2 (J5: Pitch) → Wrist-3 (J6: Roll)
```

| Joint | Axis | Typical Range | Function |
|-------|------|---------------|----------|
| J1 — Base | Vertical rotation | ±180° to ±360° | Horizontal sweep |
| J2 — Shoulder | Pitch (forward/back) | +155° / −60° | Vertical reach |
| J3 — Elbow | Pitch (up/down) | +70° / −170° | Radial positioning |
| J4 — Wrist Roll | Roll | ±360° | Tool orientation |
| J5 — Wrist Pitch | Pitch (bend) | ±120° to ±130° | Approach angle |
| J6 — Wrist Roll | Roll (spin) | ±360° | Tool rotation |

#### 2.1.2 Forward and Inverse Kinematics

- **Forward Kinematics:** Computed via Denavit-Hartenberg (D-H) parameterization; each joint transformation is a 4×4 homogeneous matrix. The end-effector pose **T₀₆** is the product of six individual transformations.
- **Inverse Kinematics:** For a 6R robot with a spherical wrist (axes J4, J5, J6 intersecting at a single point), the problem decouples into:
  - **Position IK** (J1, J2, J3) → wrist center position
  - **Orientation IK** (J4, J5, J6) → end-effector orientation
  - Up to **8 distinct IK solutions** exist; selection criteria include joint-limit avoidance, singularity distance, and minimum travel.

#### 2.1.3 Kinematic Advantages of 6-DOF

- **Full 6-DOF Pose Control:** Simultaneous control of position (x, y, z) and orientation (roll, pitch, yaw)
- **Well-established control theory:** Mature Jacobian-based velocity control, resolved-rate algorithms
- **High repeatability:** ±0.02–0.06 mm typical for industrial-grade units
- **Fast cycle times:** Optimized joint velocities (up to 200°/s on major axes, 400°/s on wrist axes)
- **Cost-effective:** Extensive supply chain, proven reliability (MTBF > 80,000 hours)

#### 2.1.4 Singularity Conditions

6-DOF robots encounter three classical singularity types:

| Singularity | Condition | Impact |
|-------------|-----------|--------|
| **Wrist singularity** | J5 ≈ 0° (axes J4, J6 collinear) | Loss of one rotational DOF; infinite joint velocities near singularity |
| **Shoulder singularity** | Wrist center on J1 axis | Ambiguous J1 rotation |
| **Elbow singularity** | Arm fully extended (J3 at limit) | Loss of radial reach control |

### 2.2 Seven-Axis (7-DOF) Redundant Robots

A 7-axis robot adds a **redundant joint** to the 6-DOF serial chain, typically inserted between the shoulder and wrist as an additional elbow or inline rotation joint.

#### 2.2.1 Typical Joint Configuration

```
Base (J1) → Shoulder (J2) → Upper Arm Roll (J3: Redundant)
→ Elbow (J4) → Forearm Roll (J5) → Wrist Pitch (J6) → Wrist Roll (J7)
```

Alternative: Some designs place the 7th axis as an inline rotation in the forearm (e.g., KUKA LBR iiwa, Motoman SIA series).

#### 2.2.2 Kinematic Redundancy — The Self-Motion Manifold

With 7 joints and 6 task-space DOF, the robot possesses **one degree of kinematic redundancy** (null-space dimension = 1). This means:

- For any given end-effector pose, there exists a **1-parameter family of joint configurations** (the self-motion manifold), parameterized by the "elbow angle" or "arm angle" φ.
- The null-space velocity **q̇_null = (I − J⁺J) z** allows internal motion without changing the end-effector pose, where J⁺ is the Moore-Penrose pseudo-inverse and z is an arbitrary joint velocity vector.

#### 2.2.3 Kinematic Advantages of 7-DOF Over 6-DOF

| Advantage | Description | Practical Impact |
|-----------|-------------|------------------|
| **Singularity avoidance** | Redundant DOF allows the robot to reconfigure its elbow posture to navigate away from wrist/shoulder singularities | Smoother welding seam trajectories without speed reductions |
| **Obstacle avoidance** | The arm can "bend around" fixtures, clamps, and workpieces while maintaining end-effector path | Access to confined weld joints (e.g., inside fuselage frames, internal corners) |
| **Joint limit avoidance** | Null-space optimization can continuously push joints away from their mechanical limits | Extended duty cycles without path replanning |
| **Optimized dynamics** | Null-space can minimize joint torques, accelerations, or energy consumption | Reduced wear on gear trains; improved cycle-time-to-quality ratio |
| **Human-like dexterity** | Arm posture reconfiguration mimics human arm movements | Intuitive programming by demonstration (PbD); improved collaborative operation |
| **Improved manipulability** | Maintains high manipulability index (√det(JJᵀ)) across a wider task space | Better force/velocity transmission in welding and assembly tasks |

#### 2.2.4 Redundancy Resolution Strategies

| Strategy | Method | Use Case |
|----------|--------|----------|
| **Weighted pseudo-inverse** | q̇ = J_w⁺ ẋ + (I − J_w⁺J) z | General-purpose; weights prioritize certain joints |
| **Task augmentation** | Augment task with secondary objectives (e.g., minimize ‖q − q_ref‖²) | Maintaining a preferred elbow posture during welding |
| **Gradient projection** | z = α ∇H(q), optimizing objective H in null-space | Joint-limit avoidance (H = manipulability, distance to limits) |
| **Configuration control** | Parameterize self-motion by arm angle φ; plan φ(t) explicitly | Deterministic weld path planning in constrained cells |

### 2.3 Comparative Summary

| Parameter | 6-Axis | 7-Axis |
|-----------|--------|--------|
| Degrees of Freedom | 6 | 7 (1 redundant) |
| Inverse Kinematics | Closed-form (spherical wrist) | Iterative or parameterized by arm angle |
| Singularity avoidance | Path planning workarounds | Real-time null-space reconfiguration |
| Obstacle negotiation | Limited; may require tool reorientation | Elbow repositioning without tool movement |
| Repeatability | ±0.02–0.06 mm | ±0.03–0.10 mm (slightly higher due to added joint) |
| Payload capacity (typical) | 6–500+ kg | 5–150 kg (focused on dexterity tasks) |
| Cost premium | Baseline | +15–40% vs. equivalent 6-axis |
| Control complexity | Standard | Higher (redundancy resolution required) |

---

## 3. Operational Envelopes

### 3.1 Workspace Definitions

| Term | Definition |
|------|------------|
| **Reachable workspace** | Set of all positions attainable by the end-effector reference point with at least one orientation |
| **Dexterous workspace** | Subset where the end-effector can achieve any arbitrary orientation |
| **Service volume** | Practical workspace accounting for payload, tool geometry, and singularity-free zones |

### 3.2 Typical Operational Envelopes by Robot Class

| Robot Class | Reach (mm) | Payload (kg) | Repeatability (mm) | Primary Application |
|-------------|------------|--------------|--------------------|--------------------|
| **Small 6-axis** (e.g., Fanuc LR Mate, ABB IRB 1200) | 500–900 | 3–7 | ±0.02–0.03 | Electronics assembly, small part welding |
| **Medium 6-axis** (e.g., Fanuc M-20, ABB IRB 2600) | 1,400–1,850 | 12–25 | ±0.03–0.05 | Automotive welding, general assembly |
| **Large 6-axis** (e.g., Fanuc M-900, KUKA KR 600) | 2,500–3,900 | 150–600 | ±0.05–0.10 | Heavy structural welding, aerospace panel handling |
| **Medium 7-axis** (e.g., KUKA LBR iiwa, Yaskawa SIA series) | 800–1,500 | 7–20 | ±0.05–0.10 | Confined-space welding, precision assembly |
| **Extended-reach 7-axis** (on linear track) | 5,000–15,000+ | 10–50 | ±0.10–0.20 | Large-structure welding (fuselage, ship hull) |

### 3.3 Workspace Optimization

- **Track-mounted systems (OGATA 600-10-20 link):** Adding a 7th or 8th axis via floor-mounted linear rail extends reach for large workpieces (e.g., aircraft wing skins, rail car bodies).
- **Positioner-coordinated cells:** Rotary/tilt positioners (2–3 external axes) coordinated with the robot controller effectively extend the dexterous workspace by presenting optimal weld orientations.
- **Ceiling/wall-mounted configurations:** Inverting or tilting the robot base maximizes downward reach and avoids floor obstructions in dense manufacturing cells.

### 3.4 Performance Metrics per ISO 9283

| Metric | Definition | Typical Industrial Values |
|--------|------------|--------------------------|
| **Pose accuracy (AP)** | Deviation of actual pose from commanded | 0.1–0.5 mm |
| **Pose repeatability (RP)** | Scatter of repeated moves to same target | 0.02–0.10 mm |
| **Multi-directional variation of pose accuracy** | Accuracy variation by approach direction | < 0.3 mm |
| **Distance accuracy/repeatability** | Performance on linear paths | Accuracy: ±0.5 mm; Repeatability: ±0.1 mm |
| **Path accuracy/repeatability** | Deviation from programmed trajectory | Accuracy: 0.3–1.5 mm; Repeatability: 0.1–0.5 mm |
| **Settling time** | Time to reach static accuracy after move | 20–80 ms |

---

## 4. Welding Applications

### 4.1 Overview

Robotic welding is the dominant application for 6 and 7-axis articulated robots, accounting for approximately 29% of global industrial robot installations. The combination of precise trajectory control, consistent torch orientation, and high duty cycles makes articulated robots ideal for MIG/MAG and TIG welding processes.

### 4.2 MIG/MAG (GMAW) Welding

#### 4.2.1 Process Characteristics

| Parameter | Typical Range |
|-----------|---------------|
| Wire feed speed | 2–25 m/min |
| Welding current | 50–500 A |
| Arc voltage | 15–40 V |
| Travel speed | 200–2,000 mm/min |
| Shielding gas | Ar/CO₂ mixtures (75/25 to 98/2); 100% CO₂ for carbon steel |

#### 4.2.2 Alloy-Specific Considerations

**Mild and Carbon Steel (ASTM A36, A572)**

- Most common robotic welding application
- Short-circuit, spray, and pulsed-spray transfer modes
- Gas: 75% Ar / 25% CO₂ (C25) or 90% Ar / 10% CO₂
- Wire: ER70S-6 (1.0–1.6 mm diameter)
- Robot requirements: ±0.5 mm path accuracy sufficient; medium-speed travel

**Aluminum Alloys (5xxx series — 5083, 5086; 6xxx series — 6061, 6063)**

- Push-pull or spool-gun torch systems to prevent wire buckling (soft wire)
- Pulsed MIG essential for thin sections (< 3 mm) to control heat input
- Gas: 100% Argon or Ar/He mixtures for deeper penetration
- Wire: ER4043 (general), ER5356 (for 5xxx base metals)
- Robot requirements: ±0.3 mm path accuracy; precise torch-to-work distance control (CTWD ±1 mm); 7-axis advantageous for complex aluminum extrusion joints
- Critical: Pre-weld cleaning (oxide removal), interpass temperature control

**Stainless Steel (304, 316, 321 — Austenitic)**

- Tri-mix gas: 98% Ar / 1% CO₂ / 1% O₂ or 97.5% Ar / 2.5% CO₂
- Wire: ER308L, ER316L (matching base metal)
- Pulsed transfer for thin-gauge (< 2 mm) to minimize distortion and sensitization
- Robot requirements: Consistent heat input critical; seam tracking sensors (through-arc or laser) recommended
- Post-weld: Passivation or pickling may be required

#### 4.2.3 Robot-Specific MIG Requirements

| Requirement | Specification |
|-------------|---------------|
| Torch mount | Collision-protected, quick-change coupling (e.g., Binzel ABIROB, Fronius Robacta) |
| Wire feeder | Robot-mounted or close-coupled; push-pull for aluminum |
| Cable management | Integrated dress pack through hollow wrist (J6) to prevent cable wrap |
| TCP calibration | Automatic TCP (Tool Center Point) calibration station; ±0.1 mm accuracy |
| Seam tracking | Through-arc sensing, laser triangulation, or tactile sensing for real-time path correction |
| Anti-spatter | Nozzle cleaning station with automatic reaming and spray |

### 4.3 TIG (GTAW) Welding

#### 4.3.1 Process Characteristics

| Parameter | Typical Range |
|-----------|---------------|
| Welding current | 5–350 A (DC) / up to 500 A (AC for aluminum) |
| Arc voltage | 8–20 V |
| Travel speed | 50–600 mm/min |
| Shielding gas | 100% Argon; Ar/He mixtures for thick sections |
| Filler wire | Optional cold-wire or hot-wire feed (0.8–1.6 mm) |

#### 4.3.2 Alloy-Specific Applications

**Aluminum (AC-TIG)**

- AC welding provides cathodic cleaning action to break through Al₂O₃ oxide layer
- Advanced waveform control (variable polarity, square wave) for precise heat input
- Orbital TIG for tube-to-tubesheet joints in heat exchangers
- Robot requirements: **7-axis highly advantageous** — complex orbital paths around curved aluminum structures (e.g., aircraft fuselage skins, fuel tank seams)

**Stainless Steel and Nickel Alloys (DC-TIG)**

- DC electrode negative (DCEN) with thoriated or ceriated tungsten
- Critical for thin-wall tubing (aerospace, pharmaceutical, semiconductor)
- Automatic voltage control (AVC) for consistent arc length
- Robot requirements: ±0.1 mm path repeatability for narrow-gap joints; programmable pulsing (0.5–500 Hz)

**Titanium (Ti-6Al-4V)**

- Full inert gas shielding (trailing shield, backup purge) to prevent embrittlement
- Low heat input essential; pulsed DC at 50–150 A typical
- Dedicated clean-room compatible robot cell
- Robot requirements: Gas lens torch; laminar flow shielding; 7-axis for complex contour following

#### 4.3.3 Robot-Specific TIG Requirements

| Requirement | Specification |
|-------------|---------------|
| Torch rigidity | High-stiffness mount; minimal vibration at low travel speeds |
| Arc length control | Automatic Voltage Control (AVC) — ±0.1 mm resolution |
| Wire feed | Integrated cold-wire or hot-wire feeder; programmable feed angle and speed |
| Electrode maintenance | Automatic tungsten grinder/changer station |
| Cleanliness | Dedicated gas lines; HEPA-filtered enclosures for reactive metals |

### 4.4 Advanced Welding Processes

| Process | Robot Configuration | Application |
|---------|-------------------|-------------|
| **Laser-MIG Hybrid** | 6-axis + fiber-optic laser head | High-speed deep-penetration welding of thick steel (shipbuilding, heavy equipment) |
| **Friction Stir Welding (FSW)** | Heavy-duty 6-axis (500+ kg payload) or dedicated FSW machine | Solid-state joining of aluminum aerospace panels |
| **Plasma Arc (PAW)** | 6/7-axis with keyhole plasma torch | Precision welding of stainless steel and titanium thin-wall structures |
| **CMT (Cold Metal Transfer)** | 6-axis with Fronius CMT torch | Ultra-low-spatter joining of galvanized steel, aluminum thin-sheet |

### 4.5 Quality Assurance in Robotic Welding

| Method | Standard | Description |
|--------|----------|-------------|
| Real-time monitoring | ISO 14731, AWS D8.1M | Current, voltage, wire speed, gas flow logged per weld |
| Seam inspection | ISO 5817, AWS D1.1 | Visual + NDT (ultrasonic, radiographic) of completed welds |
| Weld parameter database | GQAOA CSDB (DM 600-10-10) | S1000D data module for weld procedure specifications |
| Statistical process control | ISO 3951 | Control charts for critical weld parameters |

---

## 5. Precision Assembly Applications

### 5.1 Overview

Six and seven-axis robots perform precision assembly tasks requiring sub-millimeter accuracy, controlled insertion forces, and repeatable orientation control. The 7-axis configuration is particularly valuable in confined assembly spaces where multiple approach vectors are needed.

### 5.2 Electronics Manufacturing

#### 5.2.1 PCB and Module Assembly

| Task | Robot Requirements | Typical Specifications |
|------|-------------------|----------------------|
| Component placement (through-hole) | 6-axis, small-class | ±0.05 mm repeatability; vacuum gripper |
| Connector insertion | 6/7-axis with force/torque sensor | 5–50 N insertion force; ±0.1 mm alignment |
| Cable routing and harness assembly | 7-axis for dexterity | Compliant end-effector; vision-guided |
| Thermal interface material (TIM) dispensing | 6-axis with precision dispenser | ±0.01 mL volume control |
| Screw driving | 6-axis with torque-controlled driver | 0.01–10 Nm; angle/torque monitoring |

#### 5.2.2 Semiconductor and Cleanroom Applications

- Class 1–100 cleanroom compatibility
- ESD-safe construction (conductive coatings, grounded joints)
- Cleanroom compatibility: ISO 14644-1 Class 5 (airborne particle concentration limits per m³ at specified particle sizes)
- Robot examples: Fanuc CR series (cleanroom), Stäubli TX2-60 CR

### 5.3 Aerospace Component Assembly

#### 5.3.1 Structural Assembly

| Task | Description | Robot Configuration |
|------|-------------|-------------------|
| **Drilling and fastening** | Automated drill-rivet-bolt for airframe panels | Large 6-axis on gantry (600-10-20 link) |
| **Sealant application** | Precision bead of polysulfide sealant along faying surfaces | Medium 6-axis with vision |
| **Shim measurement and placement** | Measuring gaps, cutting custom shims, inserting | 7-axis for access to recessed areas |
| **Composite layup assistance** | Handling and placement of pre-impregnated plies | 6-axis with vacuum grippers, force feedback |

#### 5.3.2 Engine Component Assembly

- Turbine blade-to-disc assembly: ±0.01 mm tolerance, force-controlled insertion
- Fuel nozzle assembly: Torque-controlled fastening, leak testing integration
- Gearbox assembly: Multi-stage press-fit, automated backlash measurement

### 5.4 Automotive Assembly

| Application | Robot Type | Key Parameters |
|-------------|-----------|----------------|
| Door/hood/trunk fitting | Large 6-axis | ±0.5 mm; 100–250 kg payload |
| Windshield insertion | Medium 6-axis with vision | Adhesive bead + force-controlled placement |
| Battery module stacking (EV) | Medium 6-axis, cleanroom-rated | ±0.1 mm; thermal interface dispensing |
| Wire harness insertion | 7-axis for routing dexterity | Flexible gripper; vision + force guided |

### 5.5 End-Effector Technologies for Assembly

| Type | Application | Key Feature |
|------|-------------|-------------|
| Vacuum grippers | Flat/smooth surfaces | Multi-zone, adaptive suction |
| Mechanical grippers | Cylindrical/irregular parts | Parallel, angular, or 3-finger adaptive |
| Magnetic grippers | Ferrous parts | Switchable electro-permanent magnets |
| Force/torque sensors | Insertion, press-fit | 6-axis F/T; 0.1 N / 0.005 Nm resolution |
| Compliance devices | Peg-in-hole, snap-fit | Remote center of compliance (RCC); active compliance |
| Tool changers | Multi-process cells | Automatic coupling of pneumatic, electric, signal interfaces |

---

## 6. Safety Standards and Compliance

### 6.1 Regulatory Framework Overview

The safety of industrial robot systems is governed by a hierarchical set of international standards. Within the GQAOA framework, all ROBOT.INCs must comply with these standards, cross-referenced to UTCS codes **691-10-xx** (Functional Safety Standards) and **690-xx-xx** (Human-Robot Interaction).

```
                    ┌────────────────────────┐
                    │    ISO 12100:2010       │  ← General Principles (Type-A)
                    │  Safety of Machinery    │
                    └────────────┬───────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                  │
     ┌──────────┴──────────┐          ┌───────────┴───────────┐
     │  ISO 13849-1:2023   │          │   IEC 62061:2021      │
     │  Safety-Related      │          │   Functional Safety   │
     │  Control Systems     │          │   E/E/PE Systems      │
     └──────────┬──────────┘          └───────────┬───────────┘
                │                                  │
                └────────────────┬─────────────────┘
                                 │
                    ┌────────────┴───────────┐
                    │  ISO 10218-1/2:2011    │  ← Robot-Specific (Type-C)
                    │  Robot Safety Reqs.     │
                    └────────────┬───────────┘
                                 │
                    ┌────────────┴───────────┐
                    │  ISO/TS 15066:2016     │  ← Collaborative Operations
                    │  Cobots Spec.           │
                    └────────────────────────┘
```

### 6.2 ISO 10218 — Safety Requirements for Industrial Robots

#### 6.2.1 Part 1: Robots (ISO 10218-1:2011)

Specifies safety requirements for the **robot itself** (the manipulator and controller). Key requirements relevant to 600-10-10:

| Requirement | Description | Impact on 6/7-Axis Systems |
|-------------|-------------|---------------------------|
| **Emergency stop (Category 0/1)** | Hardwired e-stop circuit removing power to actuators | All axes must decelerate within defined stopping time; 7-axis requires additional brake |
| **Protective stop (Category 2)** | Controlled stop maintaining motor power for restart | Essential for welding cycle interruption (torch retract before stop) |
| **Speed and force limiting** | Programmable speed reduction zones | Must account for all 6/7 joint velocities in resultant TCP speed |
| **Axis limiting** | Software and hardware limits on each joint | 7th axis must have independent limit switches and software limits |
| **Singular configuration management** | Safe behavior at kinematic singularities | Wrist singularity protection critical for 6-axis; less critical for 7-axis |
| **Safety-rated monitored stop** | STO/SLS/SLP per IEC 61800-5-2 | Drive-integrated safety functions for each axis servo |

> **Editorial note:** Because IEC 61800-5-2 is cited here for drive-integrated safety functions, it shall also be added to **Section 1.2 Normative References** and **Section 10 References** for completeness and auditability.
| **Pendant and teach mode** | Reduced-speed operation (≤250 mm/s TCP speed) | Teach pendant with enabling device (3-position) and dead-man switch |

#### 6.2.2 Part 2: Robot Systems and Integration (ISO 10218-2:2011)

Addresses the **complete robot cell** design. Requirements specific to welding and assembly cells:

| Requirement | Description | Application to 600-10-10 |
|-------------|-------------|--------------------------|
| **Perimeter safeguarding** | Physical barriers, interlocked gates, presence-sensing devices | Welding cells: solid panels (UV/spatter protection); assembly cells: light curtains |
| **Risk assessment** | Per ISO 12100; mandatory before commissioning | See [Section 7](#7-risk-assessment-methodology) |
| **Safeguarded space** | Maximum volume swept by robot + tool + workpiece | Must include torch length, wire stick-out, and positioner swept volume |
| **Interlocked guards** | Category per ISO 14119; guard locking if hazard persists after stop | Welding: guard lock until fume extraction confirms safe atmosphere |
| **Presence-sensing devices** | Safety laser scanners, safety mats, light curtains | Graded response: speed reduction → protective stop → emergency stop |
| **Ergonomic access** | Safe access for loading, maintenance, tool change | Dual-circuit interlock on access doors; bypass key for maintenance |

### 6.3 ANSI/RIA R15.06-2012 — US National Adoption

ANSI/RIA R15.06 is the **US implementation** of ISO 10218, with additional requirements:

| Additional Requirement | Description |
|----------------------|-------------|
| **Employer responsibilities** | Documented risk assessment, operator training records, periodic inspection |
| **Awareness barriers** | Clearly marked robot operating envelope on floor (yellow/black striping) |
| **Lockout/Tagout (LOTO)** | Per OSHA 29 CFR 1910.147 — mandatory for maintenance entry |
| **Pendant requirements** | Enabling device must be 3-position; teach speed ≤250 mm/s resultant |
| **Inspection intervals** | Annual inspection by qualified person; documentation retained |
| **Training requirements** | Operator, programmer, maintenance personnel certification paths |

#### 6.3.1 RIA TR R15.306-2016 — Task-Based Risk Assessment

The RIA Technical Report provides a structured, **task-based approach** to risk assessment for robot systems:

1. Identify all tasks (programming, production, maintenance, troubleshooting, clean-up)
2. For each task: identify hazards, estimate risk (severity × probability × avoidance)
3. Apply risk reduction measures (inherent design → safeguards → information)
4. Document residual risk acceptance

### 6.4 ISO/TS 15066:2016 — Collaborative Robot Operations

While 600-10-10 primarily addresses traditional industrial robots (not cobots), collaborative operation modes may apply when robots operate in shared spaces:

| Collaborative Mode (per ISO 10218-1) | Applicability to 600-10-10 |
|---------------------------------------|---------------------------|
| **Safety-rated monitored stop** | Loading/unloading welding fixtures with robot in monitored stop |
| **Hand-guiding** | Teaching weld paths by physically guiding the robot (7-axis especially suitable) |
| **Speed and separation monitoring** | Dynamic speed reduction when operator approaches cell for quality checks |
| **Power and force limiting** | Generally NOT applicable to large industrial welding robots (payload/speed exceed limits) |

**Biomechanical load limits** (ISO/TS 15066, Annex A):

- Maximum transient contact force: 65–280 N (depending on body region)
- Maximum quasi-static contact force: 30–160 N
- Maximum pressure: 110–380 N/cm²
- **Note:** Standard industrial welding robots (6-axis, > 20 kg payload) **cannot** meet PFL limits during normal operation; full safeguarding required.

### 6.5 UTCS 600-10-10 as GQAOA Internal Standard

Within the GQAOA framework, the UTCS code **600-10-10** functions as an **internal classification and requirements document** for 6/7-axis robots in assembly and welding. It mandates:

1. **Compliance matrix:** Each ROBOT.INC-M and INC-A unit must maintain a documented compliance matrix mapping robot features to ISO 10218, ANSI/RIA R15.06, and applicable welding standards.
2. **Safety data module:** A CSDB Data Module (DM-600-10-10-SAFETY) in S1000D format, containing all safety-related configuration data, risk assessments, and compliance evidence.
3. **Lifecycle traceability:** Safety-critical components tracked through GQAOA lifecycle phases (CON → DES → TST → CRT → PRD → OPS → MNT → SUP → REP → RET), with mandatory review gates at CRT (certification) and OPS (operational release).
4. **CHARLIE_T integration:** The digital agent maintains a live safety status dashboard, aggregating sensor data (force/torque, speed monitors, safeguard status) and flagging deviations in real time.

### 6.6 Getafe FAL Compliance Overlay (EU + Spain + Aerospace)

For any 600-10-10 cell installed at the **Airbus Getafe Final Assembly Line** the requirements of §6.1–§6.5 are layered on top of the following **legally binding** obligations. This subsection is the dispositive checklist the integrator and the GQAOA Robbbo-T program shall satisfy before the cell is released to production.

| Layer | Obligation | Acceptance evidence at Getafe FAL |
|-------|------------|-----------------------------------|
| **EU machinery (in force)** | CE marking per Directive 2006/42/EC; Annex IV procedure where applicable; Technical File retained 10 years | EC Declaration of Conformity + Technical File + harmonised-standard list (EN ISO 10218-1/-2, EN ISO 13849-1, EN 62061, EN ISO 12100) |
| **EU machinery (transition)** | Migration plan to Regulation (EU) 2023/1230 by 20 January 2027; high-risk Annex I machinery (incl. safety-critical AI components) requires third-party assessment | Gap-analysis dossier + revised DoC template + notified-body engagement record (where AI safety functions are present) |
| **EU LVD / EMC / ATEX** | 2014/35/EU + 2014/30/EU; ATEX 2014/34/EU only if welding cell is in/adjacent to a classified zone (e.g. paint-shop boundary, hydrogen storage at H₂-conversion lines) | LVD/EMC test reports; ATEX zoning plan + equipment category mapping (Cat 2/3 GD) |
| **Spain — PRL** | Ley 31/1995: written risk assessment, preventive planning, worker information/consultation, health surveillance | Evaluación de riesgos del puesto + Plan de prevención (servicio de prevención propio Airbus) + actas del Comité de Seguridad y Salud |
| **Spain — RD 1644/2008** | National declaration & Spanish-language documentation (instrucciones, marcado, EC declaration) | Documentación en castellano firmada por el fabricante / integrador |
| **Spain — RD 1215/1997** | Adequacy of work equipment (existing robots retrofitted into the cell) | Informe de adecuación RD 1215 firmado por técnico competente |
| **Spain — RD 614/2001** | Electrical-risk assessment (480 V cell mains, servo cabinets, weld-current returns) | Procedimiento de trabajo eléctrico + cualificación del personal (autorizado/cualificado) |
| **Spain — RD 374/2001 + RD 286/2006 + RD 1311/2005** | Welding-fume, noise and vibration measurement campaigns | Higienic measurement reports vs. VLA-ED/VLA-EC limits; LEX,8h ≤ 87 dB(A); A(8) for hand-arm vibration |
| **Spain — RD 681/2003 (ATEX workplace)** | Document on Explosion Protection (DPE) when applicable | DPE signed by Airbus EHS + zoning markings |
| **Spain — RD 773/1997** | PPE matrix consistent with §8.4 mapped to Airbus Getafe PPE catalogue | EPI assignment record per operator/role |
| **Aerospace — EASA Part 21G** | Production output of the FAL must remain within the POA scope; any process change (incl. new robotic cell) requires POA Form 4 / change notification | POA change package + AIPS revalidation record |
| **Aerospace — Airbus AIPS/AP** | Welding/fastening/sealing performed by the cell qualified to the AIPS revision invoked by the work-package | Qualified Process File (QPF) + welder/operator AIPS qualification cards (where mandated) |
| **Aerospace — EN 9100** | The cell's processes integrated into the Airbus Getafe EN 9100 quality system | Process FMEA + Control Plan + first-article inspection (FAI) per AS9102 |

> **Conflict-resolution rule:** Where a Spanish RD imposes a stricter requirement than the EU directive it transposes (e.g. operator information in castellano, mandatory written risk-assessment), the Spanish requirement governs. Where the Airbus AIPS imposes a stricter process tolerance than ISO 5817, the AIPS governs for that work-package. In all cases the higher of {ISO PL/SIL, RIA SIL, IEC 62061 SIL} shall be implemented in the safety-related control system.

---

## 7. Risk Assessment Methodology

### 7.1 Framework per ISO 12100:2010

All robotic cells under UTCS 600-10-10 must undergo a formal risk assessment following the iterative process defined in ISO 12100:

```
┌─────────────────────────────────────────┐
│  1. DETERMINE MACHINE LIMITS            │
│     - Intended use and foreseeable misuse│
│     - Space limits (safeguarded space)   │
│     - Time limits (lifecycle phases)     │
│     - Environmental limits               │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  2. HAZARD IDENTIFICATION               │
│     - Mechanical (crushing, shearing)    │
│     - Electrical (arc, contact)          │
│     - Thermal (welding heat, spatter)    │
│     - Radiation (UV from arc, laser)     │
│     - Chemical (fumes, shielding gas)    │
│     - Ergonomic (loading postures)       │
│     - Noise (> 85 dBA in welding cells)  │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  3. RISK ESTIMATION                      │
│     Severity (S) × Frequency/Duration (F)│
│     × Probability of Occurrence (O)      │
│     × Avoidability (A)                   │
│     → Risk level: High / Medium / Low    │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  4. RISK EVALUATION                      │
│     - Is risk adequately reduced?        │
│     - Compare to ALARP (As Low As        │
│       Reasonably Practicable)            │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  5. RISK REDUCTION (3-Step Method)       │
│     Step 1: Inherently safe design       │
│     Step 2: Safeguarding & complementary │
│     Step 3: Information for use          │
└─────────────────────────────────────────┘
```

### 7.2 Hazard Identification for 600-10-10 Systems

#### 7.2.1 Mechanical Hazards

| Hazard | Source | Risk Scenario |
|--------|--------|---------------|
| **Crushing** | Robot arm vs. fixed structure | Operator trapped between robot and workpiece positioner |
| **Impact** | Moving robot arm/tool | Unexpected motion during teach mode or restart |
| **Shearing** | Joint articulations | Fingers/hand caught in joint during maintenance |
| **Entanglement** | Rotating wrist (J6/J7) | Loose clothing/hair caught in spinning wrist |
| **Ejection** | Workpiece release | Gripper failure releasing heavy component |
| **Stabbing/puncture** | Welding wire, sharp tools | Contact with welding wire protruding from torch |

#### 7.2.2 Welding-Specific Hazards

| Hazard | Source | Mitigation |
|--------|--------|-----------|
| **Arc flash (UV/IR)** | Welding arc | Auto-darkening screens; opaque cell panels; warning beacons |
| **Spatter/molten metal** | MIG/MAG process | Spatter guards; fire-resistant curtains; PPE for operators nearby |
| **Fumes and gases** | Metal vaporization | Local exhaust ventilation (LEV); fume extraction torches; OSHA PEL compliance |
| **Electrical shock** | Welding power source (OCV 40–80V) | Isolation transformers; insulated torch body; GFCI protection |
| **Fire/explosion** | Flammable materials near arc | Housekeeping; fire watch; hot work permits per NFPA 51B |
| **Shielding gas asphyxiation** | Argon/CO₂ displacement in confined spaces | O₂ monitoring; ventilation; confined-space entry procedures |

#### 7.2.3 Assembly-Specific Hazards

| Hazard | Source | Mitigation |
|--------|--------|-----------|
| **Pinch points** | Gripper closure | Force-limited grippers; finger-safe openings |
| **Dropped parts** | Gripper failure, workpiece misalignment | Part-present sensors; gravity-secure fixturing |
| **Adhesive/sealant exposure** | Dispensing operations | Enclosed dispensing; ventilation; PPE |
| **Noise** | Press-fit, riveting, fastening | Acoustic enclosure; hearing protection above 85 dBA |

### 7.3 Safety Integrity Level (SIL) / Performance Level (PL) Determination

Per ISO 13849-1 and IEC 62061, the safety-related control system for a 600-10-10 robot cell typically requires:

| Safety Function | Typical Required PL (ISO 13849) | Typical SIL (IEC 62061) |
|-----------------|--------------------------------|------------------------|
| Emergency stop | PLd or PLe | SIL 2 or SIL 3 |
| Protective stop (guard interlock) | PLd | SIL 2 |
| Speed monitoring (teach mode) | PLd | SIL 2 |
| Axis range limiting | PLc or PLd | SIL 1 or SIL 2 |
| Safety-rated monitored stop | PLd | SIL 2 |
| Presence detection (light curtain) | PLd or PLe | SIL 2 or SIL 3 |
| Enabling device (teach pendant) | PLd | SIL 2 |

### 7.4 GQAOA Risk Documentation Requirements

All risk assessments for 600-10-10 systems must be documented in the CSDB following S1000D conventions:

| Document | CSDB Location | Content |
|----------|---------------|---------|
| Risk Assessment Report | DM-600-10-10-RA-001 | Full ISO 12100 risk assessment |
| Safety Requirements Spec | DM-600-10-10-SRS-001 | Safety functions, PL/SIL targets |
| Validation Report | DM-600-10-10-VAL-001 | Verification that PL/SIL achieved |
| Residual Risk Notice | DM-600-10-10-RRN-001 | Accepted residual risks, operator warnings |

---

## 8. Human-Robot Interaction and Cell Design

### 8.1 Cell Design Principles

#### 8.1.1 Welding Cell Layout

A typical robotic welding cell for 600-10-10 robots includes:

```
┌──────────────────────────────────────────────────────┐
│                    WELDING CELL                       │
│                                                      │
│  ┌─────────────┐      ┌─────────────┐               │
│  │  ROBOT      │      │  POSITIONER │               │
│  │  (6/7-axis) │─────▶│  (2-axis)   │               │
│  │             │      │  ┌───────┐  │               │
│  └─────────────┘      │  │ WORK- │  │               │
│        │              │  │ PIECE │  │               │
│        │              │  └───────┘  │               │
│  ┌─────▼─────┐        └─────────────┘               │
│  │ WIRE FEED │                                      │
│  │ & POWER   │        ┌─────────────┐               │
│  │ SOURCE    │        │ FUME        │               │
│  └───────────┘        │ EXTRACTION  │               │
│                       └─────────────┘               │
│  ┌───────────┐                                      │
│  │ NOZZLE    │   ┌──────────────────┐               │
│  │ CLEANING  │   │ TCP CALIBRATION  │               │
│  │ STATION   │   │ STATION          │               │
│  └───────────┘   └──────────────────┘               │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [INTERLOCKED GATE] ◀═══ [LIGHT CURTAIN]            │
│  ┌────────────────────────────────────────┐         │
│  │           OPERATOR ZONE                 │         │
│  │  [TEACH PENDANT] [HMI] [E-STOP]        │         │
│  └────────────────────────────────────────┘         │
└──────────────────────────────────────────────────────┘
```

#### 8.1.2 Assembly Cell Layout Considerations

| Design Element | Requirement | Standard Reference |
|----------------|-------------|-------------------|
| **Minimum clearance** | ≥500 mm between robot maximum reach and fixed structures | ISO 10218-2 §5.4 |
| **Access points** | Interlocked gates with guard locking (trapped key or solenoid) | ISO 14119 |
| **Dual-channel safety** | All safety circuits redundant with cross-monitoring | ISO 13849-1 Cat. 3/4 |
| **Visibility** | Operator must see entire robot workspace from control station | ISO 10218-2 §5.10 |
| **Lighting** | ≥300 lux general; ≥500 lux at load/unload stations | ISO 12100 |
| **Floor marking** | Yellow/black hazard zones; robot reach envelope marked | ANSI/RIA R15.06 |
| **Ventilation** | Welding cells: ≥0.5 m/s face velocity at fume capture point | ACGIH TLV guidelines |

### 8.2 Safeguarding Hierarchy

Per ISO 10218-2 and ANSI/RIA R15.06, safeguarding must follow the hierarchy:

1. **Elimination/substitution:** Remove hazards through inherent design (e.g., no sharp edges, limited force capability)
2. **Engineering controls:**
   - **Perimeter guards:** Fixed fencing (welding: solid panels for UV/spatter; assembly: mesh/polycarbonate)
   - **Interlocked gates:** Solenoid-locked, dual-channel; guard locking time ≥ robot stopping time
   - **Presence-sensing devices:** Safety laser scanners (Type 3 per IEC 61496); light curtains (Type 2/4)
   - **Safety-rated software limits:** Axis limits, speed limits, safe zones (space restriction)
   - **Pressure-sensitive mats:** For floor-level detection at loading stations
3. **Administrative controls:** Training, SOPs, signage, PPE requirements
4. **Information for use:** Warning labels, operator manuals, markings

### 8.3 Safe Human-Robot Interaction Best Practices

#### 8.3.1 For Traditional Industrial Robots (600-10-10 Primary Scope)

| Practice | Description |
|----------|-------------|
| **Zero-energy state for maintenance** | Full LOTO (lockout/tagout) per OSHA 1910.147 before entering safeguarded space |
| **Teach mode restrictions** | ≤250 mm/s TCP speed; enabling device held; reduced power mode |
| **Start-up warning** | Audible alarm + visual beacon ≥3 seconds before automatic mode start |
| **Restart interlock** | Automatic mode cannot restart until all safeguards confirmed closed and reset |
| **Trap protection** | No pinch points between robot and fixed objects with < 500 mm clearance (120 mm for body; 25 mm for fingers) |
| **Emergency stop accessibility** | E-stop within reach at every operator station and on teach pendant |
| **Dual operator awareness** | When multiple operators work around a cell, all must acknowledge before restart |

#### 8.3.2 For Semi-Collaborative Scenarios

In some 600-10-10 applications, operators may need to interact with the cell during production (e.g., manual loading of weld fixtures):

| Scenario | Safeguarding Strategy |
|----------|----------------------|
| **Part loading while robot welds** | Dual-station turntable or shuttle; interlocked partition separates operator from active zone |
| **Quality inspection during cycle** | Observation window with welding-grade filter; or robot pauses in monitored stop |
| **Manual touch-up after robotic weld** | Robot moved to safe home position + monitored stop; operator enters with enabling device |
| **Collaborative teaching (7-axis)** | Hand-guiding mode per ISO 10218-1 §5.7; reduced-speed; F/T sensor monitoring |

### 8.4 Personal Protective Equipment (PPE)

| PPE | Welding Cell | Assembly Cell |
|-----|-------------|---------------|
| Safety glasses (ANSI Z87.1) | ✓ (with side shields) | ✓ |
| Welding helmet (auto-darkening, shade 9–13) | ✓ (when arc visible) | — |
| Flame-resistant clothing (NFPA 2112) | ✓ | — |
| Hearing protection (NRR ≥ 25 dB) | ✓ (if > 85 dBA) | As needed |
| Safety shoes (ASTM F2413) | ✓ | ✓ |
| Cut-resistant gloves (ANSI A4+) | ✓ (handling parts) | ✓ (handling parts) |
| Respiratory protection | ✓ (if LEV insufficient) | As needed (adhesives) |

### 8.5 Operator Training Requirements

Per ANSI/RIA R15.06 and OSHA requirements:

| Training Level | Personnel | Content |
|----------------|-----------|---------|
| **Awareness** | All facility staff | Robot hazards, no-go zones, emergency procedures |
| **Operator** | Cell operators | Start/stop, loading, cycle monitoring, fault recovery, PPE use |
| **Programmer** | Robot programmers | Teach pendant operation, safe programming practices, motion testing |
| **Integrator** | System integrators | Risk assessment, safeguard design, commissioning, validation |
| **Maintenance** | Maintenance technicians | LOTO, fault diagnosis, component replacement, safety system verification |

---

## 9. GQAOA Integration and UTCS Mapping

### 9.1 UTCS Cross-Reference Matrix

This document (600-10-10) interfaces with the following UTCS codes:

| UTCS Code | Domain | Relationship |
|-----------|--------|-------------|
| **600-10-00** | OGATA | Parent: Articulated arm and Cartesian robots |
| **600-10-20** | OGATA | Sibling: Cartesian and gantry robots (track extensions) |
| **600-10-30** | OGATA | Sibling: SCARA robots (pick & place) |
| **600-20-xx** | OGATA | Controllers and programming software |
| **601-xx-xx** | OGATA | Collaborative robots (cobots) — safety interface |
| **602-xx-xx** | OGATA | Vision systems — seam tracking, part recognition |
| **603-10-10** | OGATA | Assembly process automation — welding stations |
| **604-xx-xx** | OGATA | Maintenance and diagnostics — predictive maintenance |
| **690-xx-xx** | OGATA | Human-robot interaction framework |
| **691-xx-xx** | OGATA | Functional safety standards |
| **300-xx-xx** | DTCEC | Digital twin — BOB DT kinematic model |
| **320-xx-xx** | DTCEC | AI — path planning, weld parameter optimization |
| **870-xx-xx** | CYB | Cybersecurity — robot controller network protection |
| **960-xx-xx** | QCSAA | Quantum robotics — QAOA path optimization |
| **570-xx-xx** | AMTA | Advanced materials — weld metallurgy |

### 9.2 ROBOT.INCs Registration

Each 6/7-axis robot deployed under 600-10-10 is registered as a **ROBOT.INC-M** (Manipulator) or **ROBOT.INC-A** (Assembly) entity with:

| Field | Description |
|-------|-------------|
| `robot_inc_id` | Unique identifier (e.g., `INC-M-FAC01-R001`) |
| `utcs_code` | `600-10-10` |
| `robot_model` | Manufacturer and model (e.g., `FANUC-M20iD-25`) |
| `dof` | `6` or `7` |
| `payload_kg` | Rated payload |
| `reach_mm` | Maximum reach |
| `applications` | `["welding-MIG", "welding-TIG", "assembly"]` |
| `safety_compliance` | `["ISO-10218-1", "ISO-10218-2", "ANSI-RIA-R15.06"]` |
| `lifecycle_phase` | Current GQAOA lifecycle phase |
| `alice_id` | Physical system identifier |
| `bob_dt_id` | Digital twin identifier |
| `charlie_t_id` | Digital agent identifier |

### 9.3 CSDB Data Module Structure

The following S1000D data modules are maintained for each 600-10-10 installation:

| Data Module Code | Title | Content |
|------------------|-------|---------|
| `DM-600-10-10-D-001` | Descriptive — Robot System Overview | Kinematic specs, operational envelope, installed configuration |
| `DM-600-10-10-P-001` | Procedural — Welding Operations | Weld procedures, parameter databases, torch maintenance |
| `DM-600-10-10-P-002` | Procedural — Assembly Operations | Assembly sequences, force profiles, quality checks |
| `DM-600-10-10-F-001` | Fault Isolation — Troubleshooting | Fault codes, diagnostic procedures, recovery actions |
| `DM-600-10-10-M-001` | Maintenance — Scheduled Tasks | PM intervals, lubrication, calibration, safety system checks |
| `DM-600-10-10-RA-001` | Risk Assessment Report | ISO 12100 risk assessment for the specific cell |
| `DM-600-10-10-SRS-001` | Safety Requirements Specification | Safety functions, PL/SIL targets, validation plan |

### 9.4 Digital Twin Integration (BOB DT)

The BOB DT (Digital Twin) for a 600-10-10 robot maintains:

- Real-time kinematic model synchronized with physical joint positions
- Welding process parameters (current, voltage, wire speed, gas flow) mirrored in real time
- Collision detection using the digital twin's geometric model + safety margins
- Predictive maintenance triggers based on joint torque profiles, vibration signatures
- Weld quality prediction using thermal simulation + ML models (DTCEC 320-xx link)

### 9.5 CHARLIE_T Agent Functions

The CHARLIE_T contextual digital agent for 600-10-10 systems provides:

| Function | Description |
|----------|-------------|
| **Safety monitoring** | Continuous aggregation of safety sensor data; anomaly detection |
| **Weld quality narration** | Natural-language summaries of weld quality metrics per production run |
| **Predictive alerts** | Advance warning of maintenance needs, consumable depletion |
| **Compliance tracking** | Automated verification of safety system check intervals |
| **Operator guidance** | AR-overlay instructions for fault recovery, tool change, LOTO procedures |

---

## 10. References

### 10.1 International Standards

| Standard | Full Title |
|----------|-----------|
| ISO 10218-1:2011 | Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots |
| ISO 10218-2:2011 | Robots and robotic devices — Safety requirements for industrial robots — Part 2: Robot systems and integration |
| ISO/TS 15066:2016 | Robots and robotic devices — Collaborative robots |
| ISO 12100:2010 | Safety of machinery — General principles for design — Risk assessment and risk reduction |
| ISO 13849-1:2023 | Safety of machinery — Safety-related parts of control systems — Part 1: General principles for design |
| IEC 62061:2021 | Safety of machinery — Functional safety of safety-related control systems |
| IEC 61508 (series) | Functional safety of electrical/electronic/programmable electronic safety-related systems |
| ISO 9283:1998 | Manipulating industrial robots — Performance criteria and related test methods |
| ISO 14119:2013 | Safety of machinery — Interlocking devices associated with guards |
| IEC 61496 (series) | Safety of machinery — Electro-sensitive protective equipment |
| ISO 14731:2019 | Welding coordination — Tasks and responsibilities |
| ISO 5817:2014 | Welding — Fusion-welded joints in steel, nickel, titanium and their alloys — Quality levels for imperfections |
| ISO 3691-4:2020 | Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks |

### 10.2 US National Standards

| Standard | Full Title |
|----------|-----------|
| ANSI/RIA R15.06-2012 | Industrial Robots and Robot Systems — Safety Requirements |
| RIA TR R15.306-2016 | Industrial Robots and Robot Systems — Safety Requirements — Task-Based Risk Assessment Methodology |
| RIA TR R15.606-2016 | Collaborative Robot Safety — Guidelines for Power and Force Limiting |
| OSHA 29 CFR 1910.147 | The Control of Hazardous Energy (Lockout/Tagout) |
| OSHA 29 CFR 1910.252 | General Requirements (Welding, Cutting, and Brazing) |
| NFPA 51B | Standard for Fire Prevention During Welding, Cutting, and Other Hot Work |
| AWS D1.1/D1.1M | Structural Welding Code — Steel |
| AWS D1.2/D1.2M | Structural Welding Code — Aluminum |
| AWS D8.1M | Specification for Automotive Weld Quality — Arc Welding |

### 10.3 GQAOA Internal References

| Document | Location |
|----------|----------|
| Robbbo-T Robotics PRD — MACCHIN-AR-IA Definition | `programs/Robbbo-T_Robotics_PRD/Readme.md` |
| UTA Domains Master Specification | `OPT-INS_FRAMEWORK/UTA-DOMAINS.md` |
| SUPIA v1.0 — Sistema Unico di Progettazione Industriale Avanzata | `OPT-INS_FRAMEWORK/GQAOA-UTA-SUPIA-001.md` |
| GQAOA Master README — UTCS v1.1 | `README.md` (root) |
| CSDB Validator | `CSDB/s1000d_validator.py` |

### 10.4 European Union — Directives and Regulations (Getafe FAL)

| Reference | Full Title |
|-----------|-----------|
| Regulation (EU) 2023/1230 | Regulation of the European Parliament and of the Council on machinery (entry into application 20 January 2027) |
| Directive 2006/42/EC | Directive on machinery, amending Directive 95/16/EC (Machinery Directive) |
| Directive 2014/35/EU | Low Voltage Directive (LVD) — making available on the market of electrical equipment within certain voltage limits |
| Directive 2014/30/EU | Electromagnetic Compatibility Directive (EMC) |
| Directive 2014/34/EU | ATEX equipment Directive — equipment and protective systems intended for use in potentially explosive atmospheres |
| Directive 2009/104/EC | Minimum safety and health requirements for the use of work equipment by workers at work |
| Directive 89/391/EEC | OSH Framework Directive — measures to encourage improvements in the safety and health of workers |
| Directive 2003/10/EC | Minimum health and safety requirements regarding workers' exposure to noise |
| Directive 2002/44/EC | Minimum health and safety requirements regarding workers' exposure to mechanical vibration |
| Regulation (EC) 1907/2006 | REACH — Registration, Evaluation, Authorisation and Restriction of Chemicals |
| Regulation (EC) 1272/2008 | CLP — Classification, Labelling and Packaging of substances and mixtures |

### 10.5 Spanish National Law (Reino de España)

| Reference | Full Title |
|-----------|-----------|
| Ley 31/1995, de 8 de noviembre | Ley de Prevención de Riesgos Laborales |
| RD 1644/2008, de 10 de octubre | Normas para la comercialización y puesta en servicio de las máquinas |
| RD 1215/1997, de 18 de julio | Disposiciones mínimas de seguridad y salud para la utilización por los trabajadores de los equipos de trabajo |
| RD 486/1997, de 14 de abril | Disposiciones mínimas de seguridad y salud en los lugares de trabajo |
| RD 614/2001, de 8 de junio | Disposiciones mínimas para la protección de la salud y seguridad de los trabajadores frente al riesgo eléctrico |
| RD 681/2003, de 12 de junio | Protección de la salud y la seguridad de los trabajadores expuestos a los riesgos derivados de atmósferas explosivas |
| RD 374/2001, de 6 de abril | Protección de la salud y seguridad de los trabajadores contra los riesgos relacionados con los agentes químicos durante el trabajo |
| RD 286/2006, de 10 de marzo | Protección de la salud y la seguridad de los trabajadores contra los riesgos relacionados con la exposición al ruido |
| RD 1311/2005, de 4 de noviembre | Protección de la salud y la seguridad de los trabajadores frente a los riesgos derivados de la exposición a vibraciones mecánicas |
| RD 773/1997, de 30 de mayo | Disposiciones mínimas de seguridad y salud relativas a la utilización por los trabajadores de equipos de protección individual |
| RD 488/1997, de 14 de abril | Disposiciones mínimas de seguridad y salud relativas al trabajo con equipos que incluyen pantallas de visualización |
| RD 39/1997, de 17 de enero | Reglamento de los Servicios de Prevención |
| ITC-MIE-AEM-2 | Instrucción técnica complementaria — grúas torre desmontables para obras |
| INSST NTP 884 | Evaluación de riesgos en operaciones con robots industriales |
| INSST NTP 494 / 495 | Soldadura eléctrica al arco — normas de seguridad |
| INSST NTP 1142 | Robots colaborativos — evaluación del riesgo |

### 10.6 Aeronautical Sector — EASA / Airbus (Getafe FAL)

| Reference | Full Title |
|-----------|-----------|
| Regulation (EU) 748/2012 | Implementing rules for the airworthiness and environmental certification of aircraft and related products, parts and appliances (Part 21, incl. Subpart G — POA) |
| Regulation (EU) 1321/2014 | Continuing airworthiness of aircraft and aeronautical products, parts and appliances (Part 145, Part-M, Part-CAMO) |
| EN 9100:2018 | Quality Management Systems — Requirements for Aviation, Space and Defence Organisations |
| EN 4179 | Aerospace series — Qualification and approval of personnel for non-destructive testing |
| AS9102 | Aerospace First Article Inspection Requirement |
| Airbus AIPS | Airbus Industrial Process Specifications (welding, fastening, sealing, surface treatment, NDT) |
| Airbus AP | Airbus Process standards (process-control documents invoked by AIPS and by FAL work-packages) |
| Airbus AITM / ABT | Airbus test methods and test specifications |

---

## Document Status

| Field | Value |
|-------|-------|
| Version | 1.1 |
| Status | DRAFT |
| Classification | UTCS OGATA 600-10-10 |
| Author | GQAOA, INC. — Robbbo-T Robotics PRD |
| Domain | TERRA |
| Primary Deployment Site | Airbus Getafe Final Assembly Line (FAL), Madrid, España |
| Jurisdiction | EU + Spain (ES); aeronautical sector under EASA |
| ROBOT.INCs | ROBOT.INC-M, ROBOT.INC-A |
| S1000D Applicability | `product="GQAOA" variant="OGATA" optAxis="600-10-10" environment="GETAFE-FAL"` |
| Review Required | Safety Engineering, Welding Engineering, Robotics Integration, Airbus EHS Getafe, EASA POA Office |
| Date | 2026-04-25 |
