# Change Document: safety-tailoring-skill

**Status**: completed
**Branch**: feature-tailoring-agent
**Created**: 2026-05-13
**Author**: syspilot.cm

---

## Summary

Add a domain-knowledge skill (`syspilot.safety-tailoring`) that extends the
Tailoring Agent with functional-safety interview stages when ISO 26262,
IEC 61508, or DO-178C is in scope. Inspired by the Eclipse S-CORE Safety
Management guideline — provides per-standard-requirement tailoring, RASIC
responsibilities, work-product planning, component classification, and
ASIL-graduated coverage/gate tables.

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Intent (WHAT):**
> Read the Eclipse S-CORE Safety Management guideline and determine if it can
> extend the Tailoring Agent — potentially as a separate skill activated when
> functional-safety projects are being tailored.
>
> **Motivation (WHY):**
> Generic tailoring captures *which* standard applies but lacks deep
> functional-safety domain knowledge: safety element scoping (SEooC vs.
> complete system), per-clause tailoring-out rationale, ASIL-specific coverage
> targets, component classification for pre-existing/OSS software, and
> standard-specific review gates. The Eclipse S-CORE model demonstrates how
> safety management can be structured in an open, process-driven manner.
>
> **Acceptance Criteria:**
> 1. A skill at `syspilot/skills/syspilot.safety-tailoring/SKILL.md` exists
> 2. The skill provides structured interview stages (S1–S6+) covering safety element scope, work products, per-requirement tailoring, RASIC, gates, coverage, and component classification
> 3. The Tailoring Agent references the skill in its Soul and activates it conditionally (when a functional-safety standard is detected)
> 4. The agent's workflow step 2 includes S1–S7 safety-specific sub-stages
> 5. The design spec schema is extended with safety-tailoring output fields
> 6. A new requirement SYSP_REQ_TAIL_SAFETY_SKILL documents the integration contract

---

## Impact Analysis (CM)

**Performed**: 2026-05-13
**Method**: Traced from SYSP_US_TAIL through SYSP_REQ_TAIL_SAFETY_SKILL to skill file and agent cross-references.

**New elements created:**
| Level | ID / Path | Title |
|-------|-----------|-------|
| L1 (REQ) | SYSP_REQ_TAIL_SAFETY_SKILL | Safety Tailoring Skill Integration |
| Skill | `syspilot/skills/syspilot.safety-tailoring/SKILL.md` | Safety-Tailoring Skill |

**Existing elements modified:**
| Element | Scope of Change |
|---------|-----------------|
| `syspilot/agents/syspilot.tailoring.agent.md` | Soul: added skill reference; Workflow step 2: added stages S1–S7 |
| `docs/syspilot/design/spec_tailoring.rst` | SYSP_SPEC_TAIL_PROFILE_SCHEMA: added safety-tailoring extension fields |
| `docs/syspilot/requirements/req_tailoring.rst` | Added SYSP_REQ_TAIL_SAFETY_SKILL requirement |

**New files created:**
- `syspilot/skills/syspilot.safety-tailoring/SKILL.md`

---

## Process Log

| Step | Agent | Status | Notes |
|------|-------|--------|-------|
| Research (S-CORE) | CM | ✅ | Fetched 6+ Eclipse S-CORE pages; extracted safety-management structure |
| Impact Analysis | CM | ✅ | See section above |
| Change Document | CM | ✅ | This file |
| Design (Skill) | syspilot.design | ✅ | SKILL.md with 6 interview stages + decision tables |
| Implement | syspilot.implement | ✅ | Skill file created; agent Soul + Workflow updated; spec + req extended |
| Verify (sphinx) | syspilot.verify | ✅ | 0 new warnings, schema valid |
| PM Approval | PM | ⏳ | Awaiting |
| Merged | CM | ⏳ | Awaiting PM approval |

---

## Skill Content Overview

The `syspilot.safety-tailoring` skill provides domain knowledge (no scripts)
organised into six interview stages:

| Stage | Topic | Key Outputs |
|-------|-------|-------------|
| S1 | Safety Element Scoping | `safety_element_type`, `safety_hierarchy` |
| S2 | Work-Product Planning | `safety_work_products[]` (8 work products from ISO 26262 Part 2) |
| S3 | Per-Requirement Tailoring | `INST_SYSP_SPEC_TAIL_SAFETY_EXCL_*` items (clause + reasoning) |
| S4 | RASIC Assignment | `safety_roles` (Safety Mgr, Safety Eng, Project Lead, Auditor) |
| S5 | Review-Gate Refinement | ASIL→gate mapping table (overrides generic defaults) |
| S6 | Coverage Targets | ASIL→coverage method/threshold (Statement → MC/DC) |

Additional capabilities:
- **Component Classification** (S7): Per pre-existing/OSS component — max ASIL,
  process analysis, complexity, classification result → stored as
  `INST_SYSP_SPEC_TAIL_COMP_CLASS_*`
- **Safety Impact Analysis Addendum**: Per-CR check whether the CR affects
  safety-classified components or safety-linked requirements

---

## Traceability Chain

```
SYSP_US_TAIL
 └── SYSP_REQ_TAIL_SAFETY_SKILL
      ├── syspilot/skills/syspilot.safety-tailoring/SKILL.md (skill definition)
      ├── syspilot.tailoring.agent.md → Soul (skill reference)
      ├── syspilot.tailoring.agent.md → Workflow Step 2 (stages S1–S7)
      └── SYSP_SPEC_TAIL_PROFILE_SCHEMA (safety extension fields)
```

---

## Key Design Decisions

1. **Skill, not agent** — Safety tailoring is domain knowledge consumed by the
   Tailoring Agent, not a standalone actor with its own workflow.
2. **Per-standard-requirement tailoring** — Inspired by S-CORE's
   `wp__safety_tailoring`: every ISO clause NOT fulfilled gets an explicit
   exclusion item with reasoning (auditable, traceable via sphinx-needs links).
3. **ASIL-graduated tables** — Coverage and gate defaults scale with the
   criticality level; lower ASILs get lighter gates automatically.
4. **Component classification** — Based on ISO/PAS 8926 / Part 8 Clause 12;
   determines whether additional verification is required for pre-existing or
   OSS components.
5. **No scripts** — The skill is pure domain knowledge; the Tailoring Agent's
   existing interview workflow drives the interaction.

---

## Eclipse S-CORE Inspiration

Key concepts adopted from the Eclipse S-CORE Safety Management process:

- **Structured safety management** with explicit roles (Safety Manager owns the
  plan, Safety Engineer executes analysis, Project Lead integrates)
- **Per-requirement tailoring** as a first-class auditable artifact
- **Work-product-driven** approach (each phase produces named, reviewable
  deliverables)
- **Tool qualification awareness** (though not yet encoded — reserved for future
  extension)
- **Component classification** for mixed-criticality and pre-existing SW reuse
