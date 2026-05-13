# Change Document: tailoring-agent

**Status**: completed
**Branch**: feature-tailoring-agent
**Created**: 2026-05-13
**Author**: syspilot.cm

---

## Summary

Introduce the Tailoring Agent (`syspilot.tailoring`) — a methodology-owned,
user-invocable agent that interviews the user and PM to produce a **Tailoring
Profile** defining applicable standards, criticality, quality goals, and review
gates. The profile drives all downstream agents (PM, CM, QM) and conditionally
activates companion agents (security, safety, privacy).

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Intent (WHAT):**
> Add a `syspilot.tailoring` agent that works with the user and the project
> manager agent to define and scope the actual context in which the syspilots
> are used — covering OWASP, ASPICE / ISO 26262, ISO 25010, and manual review
> gates.
>
> **Motivation (WHY):**
> syspilot is used in heterogeneous settings (web/cloud, automotive, embedded,
> avionics, lightweight tooling). Without explicit tailoring, agents operate at
> maximum rigor indiscriminately or — worse — miss mandatory gates. The Tailoring
> Agent captures scope once and makes it available to all agents as a stable
> contract.
>
> **Acceptance Criteria:**
> 1. A `syspilot.tailoring` agent file exists, is user-invocable, and follows the Soul/Duties/Workflow structure
> 2. The agent produces a Tailoring Profile stored as RST sphinx-needs items under `docs/inst/syspilot/tailoring/`
> 3. The profile schema covers: project type, standards[], criticality, quality goals, review gates, companion agent flags
> 4. PM, CM, QM agents are updated to read and respect the profile
> 5. Full traceability chain from US → REQ → SPEC → agent file

---

## Impact Analysis (CM)

**Performed**: 2026-05-13
**Method**: Manually traced new theme `TAIL` through the three-level spec hierarchy and cross-agent references.

**New elements created:**
| Level | ID | Title |
|-------|----|-------|
| L0 (US) | SYSP_US_TAIL | Project Tailoring Agent |
| L1 (REQ) | SYSP_REQ_TAIL_SOUL | Tailoring Agent Soul |
| L1 (REQ) | SYSP_REQ_TAIL_DUTIES | Tailoring Agent Duties |
| L1 (REQ) | SYSP_REQ_TAIL_WORKFLOW | Tailoring Agent Workflow |
| L1 (REQ) | SYSP_REQ_TAIL_PROFILE_SCHEMA | Tailoring Profile Schema |
| L1 (REQ) | SYSP_REQ_TAIL_FRONTMATTER | Tailoring Agent Frontmatter |
| L1 (REQ) | SYSP_REQ_TAIL_SAFETY_SKILL | Safety Tailoring Skill Integration |
| L2 (SPEC) | SYSP_SPEC_TAIL_SOUL | Tailoring Agent Soul |
| L2 (SPEC) | SYSP_SPEC_TAIL_DUTIES | Tailoring Agent Duties |
| L2 (SPEC) | SYSP_SPEC_TAIL_PROFILE_SCHEMA | Tailoring Profile Schema |
| L2 (SPEC) | SYSP_SPEC_TAIL_WORKFLOW | Tailoring Agent Workflow |
| L2 (SPEC) | SYSP_SPEC_TAIL_FRONTMATTER | Tailoring Agent Frontmatter |

**Existing elements modified:**
| Element | Scope of Change |
|---------|-----------------|
| `syspilot.pm.agent.md` | Added `syspilot.tailoring` to agents list; Duty #8 (Project Tailoring); Workflow step #2 (Tailoring Check) |
| `syspilot.cm.agent.md` | Added `syspilot.tailoring` to agents list; Duty #9 (Tailoring-Driven Gates); Process Flow gate insertion points |
| `syspilot.qm.agent.md` | Dispatch step references Tailoring Profile for security companion activation |
| `syspilot.setup.agent.md` | Duty #9 (Project-Owned Data Directories); Step #5 (create empty docs/inst dirs) |
| `docs/syspilot/userstories/index.rst` | Added `us_tailoring` to toctree |
| `docs/syspilot/requirements/index.rst` | Added `req_tailoring` to toctree |
| `docs/syspilot/design/index.rst` | Added `spec_tailoring` to toctree |
| `README.md` | Added tailoring agent to agent list |
| `docs/architecture.md` | Added tailoring orchestration section |
| `docs/methodology.md` | Added tailoring lifecycle section |
| `docs/workflows.md` | Added tailoring workflow documentation |

**New files created:**
- `syspilot/agents/syspilot.tailoring.agent.md`
- `syspilot/prompts/syspilot.tailoring.prompt.md`
- `docs/syspilot/userstories/us_tailoring.rst`
- `docs/syspilot/requirements/req_tailoring.rst`
- `docs/syspilot/design/spec_tailoring.rst`

---

## Process Log

| Step | Agent | Status | Notes |
|------|-------|--------|-------|
| Branch created | CM | ✅ | feature-tailoring-agent |
| Impact Analysis | CM | ✅ | See section above |
| Change Document | CM | ✅ | This file |
| Design (L0) | syspilot.design | ✅ | SYSP_US_TAIL — 5 acceptance criteria |
| Design (L1) | syspilot.design | ✅ | 6 REQs created (SOUL, DUTIES, WORKFLOW, PROFILE_SCHEMA, FRONTMATTER, SAFETY_SKILL) |
| Design (L2) | syspilot.design | ✅ | 5 SPECs created (SOUL, DUTIES, PROFILE_SCHEMA, WORKFLOW, FRONTMATTER) |
| Implement | syspilot.implement | ✅ | Agent file + prompt + cross-agent wiring |
| Verify (sphinx) | syspilot.verify | ✅ | 0 new warnings, schema valid (11862 needs/s) |
| Document | syspilot.docu | ✅ | README, architecture, methodology, workflows updated |
| PM Approval | PM | ⏳ | Awaiting |
| Merged | CM | ⏳ | Awaiting PM approval |

---

## Traceability Chain

```
SYSP_US_TAIL
 ├── SYSP_REQ_TAIL_SOUL        → SYSP_SPEC_TAIL_SOUL        → syspilot.tailoring.agent.md (Soul)
 ├── SYSP_REQ_TAIL_DUTIES      → SYSP_SPEC_TAIL_DUTIES      → syspilot.tailoring.agent.md (Duties)
 ├── SYSP_REQ_TAIL_WORKFLOW    → SYSP_SPEC_TAIL_WORKFLOW    → syspilot.tailoring.agent.md (Workflow)
 ├── SYSP_REQ_TAIL_PROFILE_SCHEMA → SYSP_SPEC_TAIL_PROFILE_SCHEMA → profile.rst (schema def)
 ├── SYSP_REQ_TAIL_FRONTMATTER → SYSP_SPEC_TAIL_FRONTMATTER → syspilot.tailoring.agent.md (YAML)
 └── SYSP_REQ_TAIL_SAFETY_SKILL → (skill integration, see safety-tailoring-skill.md)
```

---

## Key Design Decisions

1. **Methodology-owned agent, project-owned data** — Agent file is replaced on
   methodology update; profile RST under `docs/inst/` is never overwritten.
2. **Activation contract** — The profile flag `security_required: true` activates
   the security companion; reserved keys `safety_required`, `privacy_required`
   for future companions.
3. **Criticality field is standard-agnostic** — Supports ASIL-A..D+QM,
   SIL-1..4, DAL-A..E, or `none`.
4. **Gates are enforced by CM and PM** — Tailoring Agent only records the desired
   gates; it never pauses other agents directly.
