# Change Document: impact-analysis-skill

**Status**: completed
**Branch**: feature/impact-analysis-skill
**Created**: 2026-04-15
**Completed**: 2026-04-16
**Author**: @syspilot.cm (CR9)

---

## Summary

Create a `syspilot.impact-python` skill that wraps the existing `scripts/python/get_need_links.py` as an Impact Analysis tool for the System Designer. The designer can query the full dependency tree of a Need element before starting analysis, giving a complete map of potentially affected elements.

---

## Level 0: User Stories

**Status**: ✅ completed

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_SKILL_IMPACT | Impact Analysis Before Design Work | mandatory |

### Decisions

- Decision 1: New US needed — no existing US covers tool-assisted impact analysis
- Decision 2: AC4 captures the architectural principle: agents = stable processes, skills = exchangeable tool bindings
- Decision 3: Notified PM about this design principle for broader documentation
- Decision 4: Links set FROM US_CHANGE and US_PM TO US_SKILL_IMPACT (they consume the skill)

### Impact Analysis (sphinx-needs)

Raw output from `get_need_links.py` (depth 2, direction in) per consumer US.
Candidates are listed without assessment — verdict happens at Level 1 and Level 2.

**From SYSP_US_DESIGN (System Designer):**

```
SYSP_REQ_DESIGN_DUTIES
SYSP_REQ_DESIGN_FRONTMATTER
SYSP_REQ_DESIGN_SOUL
SYSP_REQ_DESIGN_WORKFLOW
SYSP_SPEC_DESIGN_DUTIES
SYSP_SPEC_DESIGN_FRONTMATTER
SYSP_SPEC_DESIGN_SOUL
SYSP_SPEC_DESIGN_WORKFLOW
```

**From SYSP_US_PM (Project Manager):**

```
SYSP_REQ_PM_DUTIES
SYSP_REQ_PM_FRONTMATTER
SYSP_REQ_PM_SOUL
SYSP_REQ_PM_WORKFLOW
SYSP_SPEC_PM_DUTIES
SYSP_SPEC_PM_FRONTMATTER
SYSP_SPEC_PM_SOUL
SYSP_SPEC_PM_WORKFLOW
```

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Links to |
|----|-------|----------|
| SYSP_REQ_SKILL_IMPACT_QUERY | Impact Analysis Query | SYSP_US_SKILL_IMPACT |
| SYSP_REQ_SKILL_IMPACT_EXCHANGE | Impact Analysis Exchangeability | SYSP_US_SKILL_IMPACT |

### Impacted Requirements (from Level 0 candidates)

| ID | Linked From | Verdict | Change |
|----|-------------|---------|--------|
| SYSP_REQ_DESIGN_DUTIES | SYSP_US_DESIGN | ✅ modified | AC-6: SHALL use impact analysis skill |
| SYSP_REQ_DESIGN_WORKFLOW | SYSP_US_DESIGN | ✅ modified | AC-2: identify via impact analysis |
| SYSP_REQ_DESIGN_SOUL | SYSP_US_DESIGN | ❌ not affected | Soul = character, not tools |
| SYSP_REQ_DESIGN_FRONTMATTER | SYSP_US_DESIGN | ❌ not affected | No skill references in frontmatter |
| SYSP_REQ_PM_DUTIES | SYSP_US_PM | ✅ modified | AC-5: MAY use impact skill for scoping |
| SYSP_REQ_PM_WORKFLOW | SYSP_US_PM | ✅ modified | AC-3: MAY run impact analysis before CR |
| SYSP_REQ_PM_SOUL | SYSP_US_PM | ❌ not affected | Soul = character |
| SYSP_REQ_PM_FRONTMATTER | SYSP_US_PM | ❌ not affected | No skill references in frontmatter |

### Decisions

- Decision 1: Designer impact analysis is mandatory (SHALL), PM is optional (MAY)
- Decision 2: Exchangeability as separate REQ — this is an architectural principle

---

## Level 2: Design Specs

**Status**: ✅ completed

### Impact Analysis (raw tool output)

```
SYSP_REQ_SKILL_IMPACT_QUERY    → incoming: (none — new)
SYSP_REQ_SKILL_IMPACT_EXCHANGE → incoming: (none — new)
SYSP_REQ_DESIGN_DUTIES         → incoming: SYSP_SPEC_DESIGN_DUTIES
SYSP_REQ_DESIGN_WORKFLOW       → incoming: SYSP_SPEC_DESIGN_WORKFLOW
SYSP_REQ_PM_DUTIES             → incoming: SYSP_SPEC_PM_DUTIES
SYSP_REQ_PM_WORKFLOW           → incoming: SYSP_SPEC_PM_WORKFLOW
```

### New Design Specs

| ID | Title | Links to |
|----|-------|----------|
| SYSP_SPEC_SKILL_IMPACT_QUERY | Impact Analysis Query Interface | SYSP_REQ_SKILL_IMPACT_QUERY |
| SYSP_SPEC_SKILL_IMPACT_EXCHANGE | Impact Analysis Exchangeability | SYSP_REQ_SKILL_IMPACT_EXCHANGE |

### Impacted Design Specs

| ID | Linked From | Verdict | Change |
|----|-------------|---------|--------|
| SYSP_SPEC_DESIGN_DUTIES | SYSP_REQ_DESIGN_DUTIES | ✅ modified | Duty 7: Impact Analysis added |
| SYSP_SPEC_DESIGN_WORKFLOW | SYSP_REQ_DESIGN_WORKFLOW | ✅ modified | Each level starts with impact analysis |
| SYSP_SPEC_PM_DUTIES | SYSP_REQ_PM_DUTIES | ✅ modified | Duty 6: optional Impact Scoping |
| SYSP_SPEC_PM_WORKFLOW | SYSP_REQ_PM_WORKFLOW | ✅ modified | Step 4: optional Impact Scoping |
| SYSP_SPEC_DOC_WORKFLOWS | SYSP_SPEC_DESIGN_WORKFLOW (depth 2) | ✅ modified | Status notes: workflows.md must reflect impact analysis |

### Decisions

- Decision 1: SPEC_SKILL_IMPACT_QUERY documents the full script interface (params, usage patterns, data source)
- Decision 2: SPEC_SKILL_IMPACT_EXCHANGE defines the exchange contract (folder, frontmatter, capability match)
- Decision 3: Consumer SPECs get minimal additions — concrete tool usage, not architecture
- Decision 4: Depth 2 at Level 2 catches second-order consumers (e.g. documentation SPECs that link to workflow SPECs)
- Decision 5: SPEC_SKILL_IMPACT_QUERY now includes recommended depth per level
