---
name: syspilot.safety-tailoring
description: >
  Domain knowledge for tailoring safety-critical projects under functional-safety
  standards (ISO 26262, IEC 61508, DO-178C). Provides the Tailoring Agent with
  structured interview guidance, per-standard-requirement tailoring decisions,
  required work products, RASIC responsibility patterns, review-gate defaults and
  component-classification guidance. USE FOR: when the Tailoring Profile's
  standards[] includes ISO-26262, IEC-61508, or DO-178C and the Tailoring Agent
  needs to derive safety-specific content for the profile. Inspired by the
  Eclipse S-CORE Safety Management process.
---

# Skill: Safety Tailoring

> Extends `syspilot.tailoring` with functional-safety domain knowledge.
> Activated when `standards[]` includes a functional-safety standard.

## When to Use

The Tailoring Agent SHALL invoke this skill's guidance **whenever**:

* `standards[]` contains `ISO-26262`, `IEC-61508`, or `DO-178C`
* The user indicates the project involves safety-relevant functions

The skill provides **domain rules**, **interview templates**, and **decision
tables** — it does not run a script. The Tailoring Agent applies the guidance
during its normal interview workflow.

---

## Core Concept: Per-Requirement Tailoring Decisions

Functional-safety standards mandate a **complete** set of activities, work
products, and methods. Projects rarely need 100 % of them. Safety tailoring
is the formal, documented decision for each standard requirement:

```
For each requirement Ri in the applicable standard:
  Decision(Ri) ∈ { applicable, tailored_out }
  If applicable:   reference the process / workflow / work product that fulfils Ri
  If tailored_out: document the reasoning (why not applicable for THIS project)
```

**Output:** A **Safety Tailoring Document** — a structured RST artifact under
`docs/inst/syspilot/tailoring/safety-tailoring.rst` listing every tailored-out
requirement with its reasoning. This document is referenced by the Safety Plan
and SHALL be part of the Safety Package for audits.

---

## Interview Guidance (Safety-Specific)

When the Tailoring Agent detects a functional-safety standard, it SHALL add the
following stages to its normal interview (AFTER standard selection and
criticality assignment):

### Stage S1: Safety Element Scoping

Ask:

1. Is the product a **complete system** or a **Safety Element out of Context
   (SEooC)**?
   - SEooC → assumptions of use must be documented; safety manual required
   - Complete system → full safety case expected
2. What is the **hierarchy**? (Platform → Module → Component? Single product?
   Multi-ECU?)
   - Each level may need its own safety plan
3. Are there **pre-existing or OSS components** that need component
   classification (per ISO/PAS 8926 or ISO 26262-8 Clause 12)?
   - Yes → add `component-classification` to `required_artifacts`

### Stage S2: Work Product Planning

Present the standard's work products and ask which apply. Default: all at
the project's ASIL level are applicable unless user provides reasoning.

**ISO 26262 safety management work products:**

| Work Product | ISO Reference | Applies if… |
|---|---|---|
| Platform/Module Safety Plan | Part 2 Cl. 5.4/6.4 | Always (at each hierarchy level) |
| Safety Tailoring Document | Part 2 Cl. 6.5.3 | Always (documents non-applicable requirements) |
| Safety Package | Part 2 Cl. 6.4.8 | Always (collection of released work products) |
| Safety Manual | Part 4 Cl. 6 / Part 6 Cl. 6 | SEooC projects (instructs integrator on safe usage) |
| Component Classification | ISO/PAS 8926 / Part 8 Cl. 12 | Pre-existing / OSS components present |
| Formal Review Reports | Part 2 Cl. 6.5.5 | ASIL-B and above (or when audit is planned) |
| Safety Audit Report | Part 2 Cl. 6.5.5 | When independent audit is required (ASIL-C+) |
| SW Release Notes (safety) | Part 2 Cl. 6.4.6 | Always (release verification by Safety Manager) |

### Stage S3: Tailoring-Out Decisions

For each standard requirement the project does NOT intend to fulfil, ask for
reasoning. Common accepted reasons:

| Reasoning Pattern | Example |
|---|---|
| Not applicable at this ASIL | "Support requirement X is not required for ASIL-B per Table 1" |
| No HW component | "6454 — no HW part in SW platform" |
| No proven-in-use argument | "6453 — not claiming proven-in-use" |
| No distributed development | "64610 — single-site development" |
| No confidence-in-use | "6456 — not using confidence-in-use argument" |
| No independent assessment planned | "6412* — no external assessment in current lifecycle phase" |
| Covered by another mechanism | "Requirement X is met via ASPICE PAM4 linkage instead" |

The Tailoring Agent SHALL write each tailored-out decision as a sphinx-needs
item (`INST_SYSP_SPEC_TAIL_SAFETY_EXCL_*`) with fields:
- `:links:` → the standard requirement ID (if modelled)
- `:tags: safety-tailoring, tailored-out`
- Body: the reasoning

### Stage S4: RASIC Responsibility Assignment

Ask who fills each safety role for this project:

| Role | Responsibility | Default |
|---|---|---|
| Safety Manager | Create/maintain safety plan; approve classifications; formal reviews; monitor safety | Must be named |
| Safety Engineer | Support Safety Manager; maintain safety package + manual | Must be named |
| Project Lead | Approve safety plan; approve release notes; approve impact analysis | PM by default |
| External Auditor | Independent safety audit | Only at ASIL-C+ |

Store role assignments as profile fields under `companion_agents.safety_roles`.

### Stage S5: Review-Gate Derivation (Safety)

Functional-safety standards prescribe formal reviews at specific milestones.
The Tailoring Agent SHALL propose review gates based on ASIL level:

| Gate | ASIL-A | ASIL-B | ASIL-C | ASIL-D |
|---|---|---|---|---|
| design → implement | optional | **required** (human review of specs) | **required** | **required** |
| implement → verify | optional | optional | **required** (code review) | **required** |
| verify → merge | optional | optional | **required** (formal review) | **required** |
| Safety Plan formal review | — | recommended | **required** | **required** |
| Safety Package formal review | — | — | **required** | **required** |
| Independent safety audit | — | — | — | **required** |

These feed into the profile's `review_gates[]` field. The user may override.

### Stage S6: Coverage Targets (Safety)

Derive defaults from the standard:

| ASIL | Structural Coverage | Recommended Min % |
|---|---|---|
| QM | Statement | 60 |
| ASIL-A | Statement + Branch | 80 |
| ASIL-B | Branch | 90 |
| ASIL-C | Branch + MC/DC | 95 |
| ASIL-D | MC/DC | 100 |

Write to `coverage_targets.test_coverage` and
`coverage_targets.min_coverage_pct`.

---

## Component Classification Guidance

When the profile includes pre-existing or OSS components, the Tailoring Agent
SHALL prompt the user to list them and for each, capture:

1. **Component ID** — unique name
2. **Max ASIL** of safety requirements allocated to it
3. **Development process analysis** — was it developed to a recognised safety
   standard? (yes → reference; no → gaps identified)
4. **Complexity analysis** — simple (< 10 KLOC, single-purpose) / moderate /
   complex (> 100 KLOC, multi-purpose)
5. **Classification result** — determines what additional verification is needed:
   - Fully qualified → no gap
   - Partially qualified → additional testing/analysis needed (specify what)
   - Not qualified → must be replaced or wrapped with safety mechanisms

Store as `INST_SYSP_SPEC_TAIL_COMP_CLASS_*` items (one per component) with
`:links:` back to the profile.

---

## Impact Analysis (Safety Addendum)

When a Change Request is evaluated by the Tailoring Agent in per-CR mode, and
the project has a functional-safety standard, the validation SHALL additionally
check:

1. Does the CR affect any safety-classified component? If yes → flag that
   component classification may need re-evaluation.
2. Does the CR change any requirement linked to a countermeasure in the
   Security Plan or a safety goal? If yes → Safety Manager sign-off is
   required per ISO 26262-2:2018 section 5.2.2.3 d/e.
3. Does the CR introduce a new dependency? If yes → may need component
   classification.

These findings are added to the per-CR validation report.

---

## Exchange Contract

This skill provides domain knowledge only (no scripts). To replace or extend:

* Create a new skill folder (e.g. `syspilot.safety-tailoring-aspice/`)
* Provide the same interview-stage structure
* Update the `description` for Copilot discovery

---

## References

* Eclipse S-CORE Safety Management:
  https://eclipse-score.github.io/process_description/main/process_areas/safety_management/
* ISO 26262:2018 — Road vehicles — Functional safety
* IEC 61508 — Functional safety of E/E/PE safety-related systems
* DO-178C — Software Considerations in Airborne Systems
* ISO/PAS 8926 — Qualification of pre-developed software for road vehicles
