# Change Document: security-agent

**Status**: completed
**Branch**: feature-tailoring-agent
**Created**: 2026-05-13
**Author**: syspilot.cm

---

## Summary

Introduce the Security Agent (`syspilot.security`) — a methodology-owned,
user-invocable agent that creates and maintains a project Security Plan covering
six elements: security goals, threat model, failure criticality, countermeasures,
update strategy, and monitoring/ops strategy. Activated by the Tailoring Profile
flag `security_required: true`; dispatched by QM as a subagent alongside
MECE/Trace.

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Intent (WHAT):**
> Add a `syspilot.security` agent responsible to keep and maintain a Security
> Plan with six elements:
> 1. Security Goals
> 2. Threats / Threat Scenarios
> 3. Failure Criticality
> 4. Countermeasures (linked to REQ/SPEC/tests)
> 5. Update Strategy (CVE observation, deployment of fixes)
> 6. Monitoring & Operations Strategy
>
> **Motivation (WHY):**
> Security concerns are cross-cutting and tend to be forgotten between releases.
> A dedicated plan owner ensures goals, threats, and countermeasures are maintained
> as a living document and that each change touching security-relevant components
> is reviewed against the plan.
>
> **Acceptance Criteria:**
> 1. A `syspilot.security` agent file exists, is user-invocable, and follows Soul/Duties/Workflow
> 2. The agent owns a Security Plan under `docs/inst/syspilot/security/` (hybrid RST+MD)
> 3. The plan covers all six elements with appropriate sphinx-needs linking
> 4. QM dispatches the Security Agent when `security_required: true` is set
> 5. Full traceability chain from US → REQ → SPEC → agent file

---

## Impact Analysis (CM)

**Performed**: 2026-05-13
**Method**: Manually traced new theme `SEC` through the three-level spec hierarchy and QM dispatch path.

**New elements created:**
| Level | ID | Title |
|-------|----|-------|
| L0 (US) | SYSP_US_SEC | Project Security Agent |
| L1 (REQ) | SYSP_REQ_SEC_SOUL | Security Agent Soul |
| L1 (REQ) | SYSP_REQ_SEC_DUTIES | Security Agent Duties |
| L1 (REQ) | SYSP_REQ_SEC_PLAN_STRUCTURE | Security Plan Structure |
| L1 (REQ) | SYSP_REQ_SEC_WORKFLOW | Security Agent Workflow |
| L1 (REQ) | SYSP_REQ_SEC_ACTIVATION | Security Agent Activation |
| L1 (REQ) | SYSP_REQ_SEC_FRONTMATTER | Security Agent Frontmatter |
| L2 (SPEC) | SYSP_SPEC_SEC_SOUL | Security Agent Soul |
| L2 (SPEC) | SYSP_SPEC_SEC_DUTIES | Security Agent Duties |
| L2 (SPEC) | SYSP_SPEC_SEC_PLAN_STRUCTURE | Security Plan Structure |
| L2 (SPEC) | SYSP_SPEC_SEC_WORKFLOW | Security Agent Workflow |
| L2 (SPEC) | SYSP_SPEC_SEC_ACTIVATION | Security Agent Activation |
| L2 (SPEC) | SYSP_SPEC_SEC_FRONTMATTER | Security Agent Frontmatter |

**Existing elements modified:**
| Element | Scope of Change |
|---------|-----------------|
| `syspilot.qm.agent.md` | Added `syspilot.security` to agents list; Duty #7 (Security Dispatch conditional); dispatch step updated; process flow includes [Security Eng.] |
| `docs/syspilot/userstories/index.rst` | Added `us_security` to toctree |
| `docs/syspilot/requirements/index.rst` | Added `req_security` to toctree |
| `docs/syspilot/design/index.rst` | Added `spec_security` to toctree |
| `README.md` | Added security agent to agent list |
| `docs/architecture.md` | Added security agent dispatch section |
| `docs/methodology.md` | Added security lifecycle section |
| `docs/workflows.md` | Added security workflow documentation |

**New files created:**
- `syspilot/agents/syspilot.security.agent.md`
- `syspilot/prompts/syspilot.security.prompt.md`
- `docs/syspilot/userstories/us_security.rst`
- `docs/syspilot/requirements/req_security.rst`
- `docs/syspilot/design/spec_security.rst`

---

## Process Log

| Step | Agent | Status | Notes |
|------|-------|--------|-------|
| Branch created | CM | ✅ | feature-tailoring-agent (shared branch with tailoring) |
| Impact Analysis | CM | ✅ | See section above |
| Change Document | CM | ✅ | This file |
| Design (L0) | syspilot.design | ✅ | SYSP_US_SEC — 5 acceptance criteria |
| Design (L1) | syspilot.design | ✅ | 6 REQs created (SOUL, DUTIES, PLAN_STRUCTURE, WORKFLOW, ACTIVATION, FRONTMATTER) |
| Design (L2) | syspilot.design | ✅ | 6 SPECs created (matching REQs) |
| Implement | syspilot.implement | ✅ | Agent file + prompt + QM wiring |
| Verify (sphinx) | syspilot.verify | ✅ | 0 new warnings, schema valid |
| Document | syspilot.docu | ✅ | README, architecture, methodology, workflows updated |
| PM Approval | PM | ⏳ | Awaiting |
| Merged | CM | ⏳ | Awaiting PM approval |

---

## Traceability Chain

```
SYSP_US_SEC
 ├── SYSP_REQ_SEC_SOUL           → SYSP_SPEC_SEC_SOUL           → syspilot.security.agent.md (Soul)
 ├── SYSP_REQ_SEC_DUTIES         → SYSP_SPEC_SEC_DUTIES         → syspilot.security.agent.md (Duties)
 ├── SYSP_REQ_SEC_PLAN_STRUCTURE → SYSP_SPEC_SEC_PLAN_STRUCTURE → docs/inst/syspilot/security/ (schema)
 ├── SYSP_REQ_SEC_WORKFLOW       → SYSP_SPEC_SEC_WORKFLOW       → syspilot.security.agent.md (Workflow)
 ├── SYSP_REQ_SEC_ACTIVATION     → SYSP_SPEC_SEC_ACTIVATION     → syspilot.qm.agent.md (dispatch)
 └── SYSP_REQ_SEC_FRONTMATTER   → SYSP_SPEC_SEC_FRONTMATTER   → syspilot.security.agent.md (YAML)
```

---

## Key Design Decisions

1. **Hybrid storage** — RST (sphinx-needs) for goals/threats/countermeasures
   (linkable, traceable); Markdown for narrative strategies (update, monitoring/ops).
2. **Subagent of QM** — QM dispatches Security Agent when profile flags
   `security_required: true`; Security Agent does not self-activate.
3. **Three operational modes** — Bootstrap (initial plan from scratch),
   Per-Change (review security impact of each CR), Maintenance (periodic CVE
   review, plan refresh).
4. **Never writes production code** — Only plan content, threat/countermeasure
   specs, and findings reports.
5. **User-invocable** — Can also be triggered directly by the user for ad-hoc
   security consultations outside the CR workflow.
