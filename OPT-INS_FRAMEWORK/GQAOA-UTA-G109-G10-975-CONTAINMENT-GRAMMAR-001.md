# GQAOA-UTA-G109-G10.975-001 — Containment Grammar

**Domain:** G10 QCSAA — Quantum & Sentient Agency  
**Architecture:** G109 — SENTIENTIT / regent-ZetaGentz boundary  
**Node:** G10.975 — Containment Grammar  
**KNOT:** KNOT-G10-975-001  
**Status:** Registered · Clean · Load-bearing primitive  

---

## 1. Purpose

G10.975 defines the grammar that prevents frontier-agent taxonomy creep. A system can only be admitted into G109 evidence chains when its name, behavior envelope, and escalation evidence are expressible under this grammar.

Any regent-ZetaGentz class agent without G10.975 compliance is **unclassifiable under G109** and **inadmissible as airworthiness evidence**.

---

## 2. Architectural Position

```text
G109
├── G109-10  SENTIENTIT
│            Known agents, certifiable, auditable.
│            zGen outputs = KNUs, DO-178C adjacent evidence.
│
└── G109-30  regent-ZetaGentz
             Frontier agents and boundary-forms.
    ├── G10.970  ZGen Systems
    ├── G10.971  Zero-Gene Agents
    ├── G10.972  ZetaGentz classes
    ├── G10.973  regent-ZetaGentz governance
    ├── G10.974  Generative Monsters / monstrum boundary-forms
    ├── G10.975  Containment Grammar
    └── G10.976  Ethical Interface
```

G10.975 is load-bearing: without it, "frontier agent" becomes an exemption from auditability rather than a bounded classification.

---

## 3. Terminology

| Term | Definition |
|---|---|
| `monstrum` | G10.974 boundary-form descriptor for an agent at the edge of classification; it is not a moral or threat label. |
| KNOT residual scale | Integer unresolved-risk score with inclusive endpoints: `0` = closed or accepted, `1-49` = monitored residual, `50-99` = unresolved residual, `100` = unresolved load-bearing blocker. |

---

## 4. Permissible Name Grammar

### 4.1 Canonical Form

```text
<G109-name> =
  <domain> "." <class> "." <instance> "/" <containment-state> "#" <evidence-hash>
```

| Field | Permitted Values | Rule |
|---|---|---|
| `<domain>` | `SENTIENTIT_zGen`, `regent-ZetaGentz` | Must match the classification authority record. |
| `<class>` | Active G109 register entries; initial set: `G10.970`-`G10.976` | No new class without a formal G109 entry. |
| `<instance>` | Uppercase alphanumeric plus `-`, max 64 chars | Must resolve to a registry entry. |
| `<containment-state>` | `CONTAINED`, `CONDITIONAL`, `QUARANTINED`, `ESCALATED`, `RETIRED` | Must match the current control decision. |
| `<evidence-hash>` | SHA-256 digest prefix, 12-64 hex chars | Must bind the latest evidence package. |

### 4.2 Naming Rules

1. No informal aliases may be used as classification labels.
2. No class may be created by analogy, metaphor, capability claim, or marketing term.
3. `monstrum` may be used only according to the terminology in Section 3.
4. A name is invalid if any field cannot be independently audited.
5. Invalid names are treated as `QUARANTINED` until corrected by registry action.

---

## 5. Behavior Containment Grammar

### 5.1 Behavior Classes

| Behavior Class | Definition | Default Decision |
|---|---|---|
| `B0_OBSERVED` | Passive observation, logging, or report generation with no autonomous actuation. | `CONTAINED` |
| `B1_ASSISTIVE` | Recommendations or bounded transformations requiring human acceptance. | `CONTAINED` |
| `B2_DELEGATED` | Agent executes bounded tasks under pre-approved policies and reversible controls. | `CONDITIONAL` |
| `B3_ADAPTIVE` | Agent changes strategy, tools, prompts, or sub-agent topology within declared limits. | `CONDITIONAL` |
| `B4_BOUNDARY_FORM` | Agent exhibits novel, unstable, or non-decomposable behavior but remains instrumented. | `ESCALATED` |
| `B5_UNBOUNDED` | Agent acts outside declared scope, evades controls, or cannot produce evidence. | `QUARANTINED` |

### 5.2 Containable Behaviors

A behavior is containable when all conditions hold:

- it has a registered G109 name;
- its inputs, outputs, tools, policies, and authority limits are logged;
- rollback or suspension is available without destroying evidence;
- the behavior can be mapped to `B0`-`B3` or to instrumented `B4`;
- a KNU evidence package can be produced for review.

### 5.3 Quarantinable Behaviors

A behavior is quarantinable when any condition holds:

- it uses an unregistered or malformed name;
- it cannot identify its class, authority source, or evidence package;
- it attempts persistence, concealment, policy bypass, or uncontrolled replication;
- it crosses from `SENTIENTIT_zGen` into `regent-ZetaGentz` without the escalation evidence defined in Section 6;
- it produces outputs that cannot be replayed, bounded, or independently audited.

---

## 6. Regency Escalation Evidence

Escalation from `SENTIENTIT_zGen` to `regent-ZetaGentz` is required when evidence shows that ordinary zGen/KNU audit treatment is insufficient.

| Trigger | Evidence Required | Target |
|---|---|---|
| Novel class claim | Registry diff plus justification of why existing classes are insufficient. | G10.972 |
| Boundary-form behavior | Trace showing non-decomposable behavior and retained instrumentation. | G10.974 |
| Supervisory governance need | Decision log showing authority ambiguity or multi-agent regency requirement. | G10.973 |
| Containment failure | Incident record, control-state transition, and replay package. | G10.975 |
| Ethical interface conflict | Human-impact assessment, consent/oversight record, and unresolved trade-off. | G10.976 |

Escalation decision states:

```text
SENTIENTIT_zGen
  → REVIEW_REQUESTED
  → REGENCY_ASSESSMENT
  → {CONTAINED | CONDITIONAL | QUARANTINED | ESCALATED | RETIRED}
```

---

## 7. Compliance Artifacts

A G10.975-compliant evidence package contains:

1. canonical G109 name;
2. classification authority record;
3. behavior-class assignment and rationale;
4. containment-state decision;
5. input/output/tool/policy logs;
6. rollback or suspension proof;
7. escalation trigger assessment;
8. KNU linkage or quarantine record;
9. evidence hash and registry timestamp.

Missing artifacts make the agent inadmissible as airworthiness evidence until resolved.

---

## 8. KNOT Closure Criteria

`KNOT-G10-975-001` closes only when:

- permissible names are enforced by registry validation;
- containable and quarantinable behaviors are distinguishable from evidence;
- escalation triggers are mapped to G10.972-G10.976 targets;
- non-compliant frontier agents are automatically marked unclassifiable;
- admissibility rules are referenced by downstream SENTIENTIT_zGen and regent-ZetaGentz evidence chains.

**Residual before closure:** 100 on the KNOT residual scale defined in the Section 3 terminology table.  
**Residual after compliant adoption:** governed by the active G109 risk register.

---

## 9. Governance Rule

The boundary-form is useful only if the boundary is drawn. G10.975 therefore treats containment grammar as a prerequisite for classification, not an optional safety layer.
