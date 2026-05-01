```YAML
---
# Machine-readable controlled vocabulary for the AEROSPACEMODEL / DePutapapUE repository.
# Authority: ASIT
# Scope: Repository-wide
# Status: ACTIVE
# Article IX of the Model Digital Constitution (AEROSPACEMODEL-model-digital-constitution.md)
# Human-readable counterparts: acronyms.md, terms.md
#
# Schema:
#   Each top-level key is a vocabulary category.
#   Entries list every permitted value with a short definition.
#   "deprecated" flag marks values that must not be used in new content.
# ─────────────────────────────────────────────────────────────────────────────

schema_version: "1.0.0"
last_updated: "2026-05-01"
authority: ASIT
constitution_ref: "AEROSPACEMODEL-model-digital-constitution.md#article-ix"

# ─────────────────────────────────────────────
# 1. Document / Artefact Status Codes
# ─────────────────────────────────────────────
status_codes:
  - value: ACTIVE
    definition: "Document or artefact is in force and authoritative."
  - value: DRAFT
    aliases: ["Draft", "draft"]
    definition: "Work in progress; not yet approved or binding."
  - value: DRAFT_STAKEHOLDER_REVIEW
    aliases: ["Draft → Stakeholder Review"]
    definition: "Draft submitted for stakeholder review; not yet approved."
  - value: CONTROLLED_BASELINE
    aliases: ["controlled-baseline"]
    definition: "Approved and locked baseline; changes require a Change Request (CR)."
  - value: BALANCED_DRAFT
    aliases: ["balanced_draft"]
    definition: "Draft with competing stakeholder inputs reconciled; awaiting final approval."
  - value: SUPERSEDED
    definition: "Replaced by a newer version; retained for audit trail only."
  - value: DEPRECATED
    definition: "No longer recommended; will be removed in a future baseline."
  - value: REJECTED
    definition: "Proposed content formally rejected; recorded for audit."
  - value: ALPHA
    aliases: ["α"]
    definition: "Very early draft; experimental and subject to major change."
  - value: ARCHIVED
    definition: "Inactive and preserved for historical reference only."

# ─────────────────────────────────────────────
# 2. Repository Root Folder Names
# ─────────────────────────────────────────────
root_folders:
  - name: "00_META"
    definition: "Repository-wide metadata, glossaries, and governance configuration."
  - name: "Q+ATLANTIDE"
    definition: "Master classification system and knowledge architecture (Bands 000–899+)."
  - name: "IDEALE-ESG.panpara.eu"
    definition: "IDEALE-ESG framework domain tree (Aerospace, Defence, Energy, Economics, Environments, Governance, Information, Logistics, Social)."
  - name: "organization"
    definition: "Organizational structure: Q-Divisions, ORBs, programmes."
  - name: "docs"
    definition: "Reference documentation (S1000D architecture, standards)."
  - name: "scripts"
    definition: "Automation and tooling scripts (CI, SICOCA, utilities)."
  - name: "OPT-INS_FRAMEWORK"
    definition: "Optional-ins governance framework specifications (GQAOA, LUT, APE-ADAPT, etc.)."
  - name: "programs"
    definition: "Programme-specific PRDs and requirements (DTTA, Robbbo-T, etc.)."
  - name: "AMEDEO-ITBPFO"
    definition: "FINEX execution engine and associated API/frontend."

# ─────────────────────────────────────────────
# 3. Q+ATLANTIDE Band Codes
# ─────────────────────────────────────────────
qatl_bands:
  - code: "000-099"
    suffix: "ATLAS"
    definition: "Air Transport and Lifecycle Architecture Standard — aircraft systems, maintenance, identification."
  - code: "100-199"
    suffix: "STA"
    definition: "Space Technologies Architecture — space systems, propulsion, missions."
  - code: "300-399"
    suffix: "DTCEC"
    definition: "Digital Twin, Cloud, Edge Computing — digital twins, IoT, AI/ML, blockchain."
  - code: "500-599"
    suffix: "AMTA"
    definition: "Advanced Materials and Technologies for Aerospace."
  - code: "600-699"
    suffix: "OGATA"
    definition: "Open Ground and Autonomous Technology Architecture — robotics, autonomous vehicles, smart infrastructure."
  - code: "800-899"
    suffix: "CYB"
    definition: "Cybersecurity — governance, network security, cryptography, resilience."

# ─────────────────────────────────────────────
# 4. IDEALE-ESG Domain Codes
# ─────────────────────────────────────────────
ideale_esg_domains:
  - code: "A"
    name: "A-Aerospace"
    definition: "Aerospace domain."
  - code: "D"
    name: "D-Defense"
    definition: "Defence domain."
  - code: "E"
    name: "E-Energy"
    definition: "Energy domain."
  - code: "E2"
    name: "E2-Economics"
    definition: "Economics domain."
  - code: "E3"
    name: "E3-Environments"
    definition: "Environments domain."
  - code: "G"
    name: "G-Governance"
    definition: "Governance domain."
  - code: "I"
    name: "I-Information"
    definition: "Information domain."
  - code: "L"
    name: "L-Logistics"
    definition: "Logistics domain."
  - code: "S"
    name: "S-Social"
    definition: "Social domain."

# ─────────────────────────────────────────────
# 5. IDEALE-ESG Sub-Domain Codes
# ─────────────────────────────────────────────
ideale_esg_subdomains:
  - code: "I"
    name: "I-Infrastructures"
    definition: "Infrastructure assets and systems within an IDEALE-ESG domain."
  - code: "N"
    name: "N-Neural-Networks"
    definition: "AI and neural-network components within an IDEALE-ESG domain."
  - code: "O"
    name: "O-Organizations"
    definition: "Organizational entities within an IDEALE-ESG domain."
  - code: "P"
    name: "P-Programmes"
    definition: "Programmes and projects within an IDEALE-ESG domain."
  - code: "T"
    name: "T-Technologies"
    definition: "Technologies within an IDEALE-ESG domain."

# ─────────────────────────────────────────────
# 6. Lifecycle Phase Codes (LC01–LC14)
# ─────────────────────────────────────────────
lifecycle_phases:
  - code: LC01
    definition: "Concept / Feasibility"
  - code: LC02
    definition: "Requirements Definition"
  - code: LC03
    definition: "Preliminary Design"
  - code: LC04
    definition: "Detailed Design"
  - code: LC05
    definition: "Manufacturing / Development"
  - code: LC06
    definition: "Integration"
  - code: LC07
    definition: "Verification & Validation"
  - code: LC08
    definition: "Certification / Qualification"
  - code: LC09
    definition: "Production"
  - code: LC10
    definition: "Entry into Service / Deployment"
  - code: LC11
    definition: "Operations & Maintenance"
  - code: LC12
    definition: "Modification / Upgrade"
  - code: LC13
    definition: "Phase-Out / Decommission"
  - code: LC14
    definition: "Disposal / Recycling / Circularity"

# ─────────────────────────────────────────────
# 7. Mandatory Inheritance Marks
# ─────────────────────────────────────────────
mandatory_inheritance_marks:
  - mark: K
    name: "Kindness"
    category: "operating duty"
    definition: "Humane, respectful, non-harmful conduct toward people, ecosystems and machines."
  - mark: D
    name: "Determinism"
    category: "operating duty"
    definition: "Reproducible behaviour: declared inputs, pinned versions, recorded seeds, repeatable outputs."
  - mark: L-LEG
    name: "Legality"
    category: "design principle"
    definition: "Compliance encoded as architectural constraint from inception."
  - mark: L-LOY
    name: "Loyalty"
    category: "design principle"
    definition: "Fidelity to declared purpose, stakeholders, and charter; no hidden allegiances."
  - mark: F
    name: "Fairness"
    category: "ethical mark"
    definition: "Equal treatment, absence of unjustified bias, proportionality, accessibility."
  - mark: J
    name: "Justice"
    category: "ethical mark"
    definition: "Due process, proportional remedy, fair distribution of risk and reward."
  - mark: IE
    name: "Imparzialità Empatica / Empathic Impartiality"
    category: "ethical mark"
    definition: "Impartial in rule, empathic in application; synthesis of Kindness with Fairness and Justice."
  - mark: INV
    name: "Invulnerability"
    category: "security mark"
    definition: "Designed resilience: defence-in-depth, least privilege, zero-trust, redundancy."
  - mark: AR
    name: "Activist Rights"
    category: "civic mark"
    definition: "Protection of dissent, whistleblowing, conscientious objection, without retaliation."
  - mark: WR
    name: "Workers' Rights"
    category: "labour mark"
    definition: "Full labour rights for every worker (direct, contractor, supply-chain)."
  - mark: RA
    name: "Rights of People with Addictions"
    category: "health & dignity mark"
    definition: "Addiction treated as a health condition; full rights and dignity, no exploitation."

# ─────────────────────────────────────────────
# 8. Authority Roles
# ─────────────────────────────────────────────
authority_roles:
  - role: ASIT
    definition: "Authority for Structural and Integrity Traceability — repository traceability integrity, structural consistency, lifecycle operating coherence."
  - role: QA_AUTHORITY
    aliases: ["QA Authority"]
    definition: "Quality assurance sign-off authority."
  - role: CERTIFICATION_AUTHORITY
    aliases: ["Certification Authority"]
    definition: "Compliance and certification sign-off authority."
  - role: OBSERVER
    definition: "Read and monitor access; no write authority."
  - role: DELINEANT
    definition: "Boundary definition and scoping authority."

# ─────────────────────────────────────────────
# 9. Governance Branch Codes
# ─────────────────────────────────────────────
governance_branches:
  - code: LEG
    name: "Legislative"
    definition: "Stakeholder Assembly — strategy, budget oversight, executive confirmation, charter amendments."
  - code: EXE
    name: "Executive"
    definition: "Executive Committee — programme execution, operations, resource allocation."
  - code: JUD
    name: "Judicial / Oversight"
    definition: "Independent Tribunal of Safety, Ethics & Compliance — disputes, safety halts, whistleblower protection."
  - code: AUD
    name: "Auditorial / Control"
    definition: "Independent Audit Board — financial, operational, performance and compliance audits."

# ─────────────────────────────────────────────
# 10. Crossing Power Codes
# ─────────────────────────────────────────────
crossing_powers:
  - code: CP-1
    name: "Education & Training (Unity)"
    mode: "supporting · human-led"
    definition: "Corporate Academy and TMC — certifies competencies across all branches."
  - code: CP-2
    name: "Automation (Supervised Execution)"
    mode: "supporting · supervised"
    definition: "Office of Automation & Digital Operations — governed automation under human supervisor."

# ─────────────────────────────────────────────
# 11. Key Field Values (YAML / Frontmatter)
# ─────────────────────────────────────────────
field_values:
  classification:
    - value: "Consortium Confidential – Approved Stakeholders Only"
      definition: "Visible only to approved consortium members."
    - value: "Internal"
      definition: "Visible to all authorized repository contributors."
    - value: "Public"
      definition: "No access restriction."
  document_type:
    - value: "governance"
      definition: "Governance charter, constitution, or policy document."
    - value: "specification"
      definition: "Technical or regulatory specification."
    - value: "readme"
      definition: "Descriptive overview or index for a folder or module."
    - value: "glossary"
      definition: "Controlled vocabulary, terms, or acronym register."
    - value: "regulatory_framework_specification"
      definition: "Machine-readable regulatory framework (e.g., ESSA)."
    - value: "prd"
      definition: "Product Requirements Document."
  language:
    - value: "en"
      definition: "English."
    - value: "es"
      definition: "Spanish."
    - value: "it"
      definition: "Italian."
    - value: "mix"
      definition: "Mixed / multilingual document."

# ─────────────────────────────────────────────
# Amendment procedure
# ─────────────────────────────────────────────
amendment_procedure: >
  To add, modify, or deprecate a controlled vocabulary entry:
  1. Open a Change Request (CR) per Article VII of AEROSPACEMODEL-model-digital-constitution.md.
  2. Update this file and the corresponding human-readable counterpart (acronyms.md or terms.md) in the same commit.
  3. Obtain ASIT sign-off before merging to a governed baseline branch.
  4. Record the change in CHANGELOG.md with the CR reference.
**
---

# Acronyms

**Authority:** ASIT  
**Scope:** Repository-wide  
**Status:** ACTIVE  
**Source:** `AEROSPACEMODEL-model-digital-constitution.md` Article V.2 (canonical inline glossary) and repository content  
**Machine-readable counterpart:** `controlled_vocabulary.yaml`

This file is the authoritative register of acronyms used within this repository.  
All acronyms in folder names, status codes, and field values must be defined here.

---

| Acronym | Expansion |
|---------|-----------|
| AMM | Aircraft Maintenance Manual |
| AMTA | Advanced Materials and Technologies for Aerospace (Q+ATLANTIDE Band 500–599) |
| APE | Aided Prompt Engineering |
| AR | Activist Rights (Civic Mark — Mandatory Inheritance) |
| AS9100D | Aerospace quality management system standard |
| ASIT | Authority for Structural and Integrity Traceability |
| ATLAS | Air Transport and Lifecycle Architecture Standard (Q+ATLANTIDE Band 000–099) |
| CCT | Conditions Cross-Reference Table (S1000D) |
| CI | Continuous Integration |
| COI | Conflict Of Interest |
| CP-1 | Crossing Power 1 — Education & Training (Unity) |
| CP-2 | Crossing Power 2 — Automation (Supervised Execution) |
| CR | Change Request |
| CSDB | Common Source DataBase (S1000D) |
| CYB | Cybersecurity (Q+ATLANTIDE Band 800–899) |
| D | Determinism (Mandatory Inheritance) |
| DEGF | Democratic Enterprise Governance Framework |
| DO-178C | Software considerations in airborne systems (RTCA) |
| DO-254 | Design assurance for airborne electronic hardware (RTCA) |
| DTCEC | Digital Twin, Cloud, Edge Computing (Q+ATLANTIDE Band 300–399) |
| EAP | Employee Assistance Programme |
| EAR | Export Administration Regulations (US) |
| EASA | European Union Aviation Safety Agency |
| ESG | Environmental, Social and Governance |
| ESSA | European Union Space Safety Agency (governance artefact / institutional model) |
| EVM | Earned Value Management |
| F | Fairness (Ethical Mark — Mandatory Inheritance) |
| FAA | Federal Aviation Administration (US) |
| GAIA-QAO | GAIA Quantum Aerospace Organisation |
| GDPR | General Data Protection Regulation (EU) |
| GSE | Ground Support Equipment |
| HR | Human Resources |
| IE | Imparzialità Empatica / Empathic Impartiality (Ethical Mark — Mandatory Inheritance) |
| IDEALE | Infrastructures, Defence, Energy, Information, Aerospace, Logistics, Economics, Environments (ESG framework) |
| IETP | Interactive Electronic Technical Publication |
| ILO | International Labour Organization |
| INV | Invulnerability (Security Mark — Mandatory Inheritance) |
| ITAR | International Traffic in Arms Regulations (US) |
| J | Justice (Ethical Mark — Mandatory Inheritance) |
| K | Kindness (Mandatory Inheritance) |
| KPI | Key Performance Indicator |
| L | Legality and/or Loyalty (Design Principles — Mandatory Inheritance) |
| LC01–LC14 | Canonical 14-phase product lifecycle phase model |
| LUTNDR | Libro Unico delle Tecnologie: in uso, Nuova progettazione, Disuso, Riassetti |
| MLOps | Machine Learning Operations |
| NDA | Non-Disclosure Agreement |
| OGATA | Open Ground and Autonomous Technology Architecture (Q+ATLANTIDE Band 600–699) |
| ORB | Operational Review Board (executive office; sub-ORBs include FIN, LEG, HR) |
| ORB-FIN | ORB — Finance |
| ORB-HR | ORB — Human Resources |
| ORB-LEG | ORB — Legal |
| P&L.inc | Profit & Loss, incorporated (corporate vehicle paired with GAIA-QAO) |
| PRD | Product Requirements Document |
| QA | Quality Assurance |
| Q-CYBERSEC | Q-Division — Cybersecurity |
| Q-DATAGOV | Q-Division — Data Governance |
| Q-HPC | Q-Division — High-Performance Computing |
| Q-SCIRES | Q-Division — Scientific Research |
| Q-SPACE | Q-Division — Space |
| RA | Rights of People with Addictions (Health & Dignity Mark — Mandatory Inheritance) |
| S1000D | International specification for technical publications |
| SBOM | Software Bill of Materials |
| SLAPP | Strategic Lawsuit Against Public Participation |
| SLA | Service Level Agreement |
| STA | Space Technologies Architecture (Q+ATLANTIDE Band 100–199) |
| TMC | Training Master Class |
| UTCS | Universal Traceability and Configuration System |
| WR | Workers' Rights (Labour Mark — Mandatory Inheritance) |

---

*To add an acronym: open a Change Request (CR) per Article VII of the Model Digital Constitution, then update this file and `controlled_vocabulary.yaml` in the same commit.*
