# Change Document: agent-architecture-v2

**Status**: in-progress
**Branch**: feature/agent-architecture-v2
**Created**: 2026-04-11
**Author**: Change Agent
**Concept**: projects/project-manager/konzept-agent-v2.md

---

## Summary

Complete green-field agent architecture v2 with new `SYSP_` prefix. Creates a full
traceability chain (US → REQ → SPEC) for all 11 agents plus a meta-level architecture
definition. Agents structured as Soul (immutable identity), Duties (customizable tasks),
Workflow (customizable process).

---

## Architectural Decisions

- D-0: **Green field** — new RST tree with `SYSP_` prefix, no links to old `SYSPILOT_` specs
- D-1: **ID ROLE slugs** use agent command names: PM, CM, QM, CHANGE, IMPLEMENT, UAT, DOCU, MECE, TRACE, RELEASE, SETUP
- D-2: **File slugs** use descriptive persona names to avoid conflicts with existing files (e.g., `us_release_engineer.rst` instead of `us_release.rst` which already exists)
- D-3: **Customization axis**: Soul = immutable, Duties = customer-customizable, Workflow = customer-customizable
- D-4: **Handoffs** not in agents — managers orchestrate, engineers are decoupled
- D-5: **3 Managers** (user-invocable) + **8 Engineers** (subagents) + 1 meta architecture
- D-6: **Status** of all new elements: `draft` (→ `approved` after final consistency check)

## File Naming Convention

| Agent | ID ROLE | File slug (us_, req_, spec_) |
|-------|---------|------------------------------|
| syspilot.pm | PM | project_mgr |
| syspilot.cm | CM | change_mgr |
| syspilot.qm | QM | quality_mgr |
| syspilot.change | CHANGE | system_designer |
| syspilot.implement | IMPLEMENT | dev_engineer |
| syspilot.uat | UAT | test_engineer |
| syspilot.docu | DOCU | docu_engineer |
| syspilot.mece | MECE | quality_mece |
| syspilot.trace | TRACE | quality_trace |
| syspilot.release | RELEASE | release_engineer |
| syspilot.setup | SETUP | setup_engineer |
| meta | AGENT_ARCH | agent_arch |

---

## Level 0: User Stories

**Status**: ✅ completed

### New User Stories

| ID | Title | File |
|----|-------|------|
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | us_agent_arch.rst |
| SYSP_US_PM | Project Manager Agent | us_project_mgr.rst |
| SYSP_US_CM | Change Manager Agent | us_change_mgr.rst |
| SYSP_US_QM | Quality Manager Agent | us_quality_mgr.rst |
| SYSP_US_DESIGN | System Designer Agent | us_system_designer.rst |
| SYSP_US_IMPLEMENT | Dev Engineer Agent | us_dev_engineer.rst |
| SYSP_US_UAT | Test Engineer Agent | us_test_engineer.rst |
| SYSP_US_DOCU | Documentation Engineer Agent | us_docu_engineer.rst |
| SYSP_US_MECE | Quality Engineer MECE Agent | us_quality_mece.rst |
| SYSP_US_TRACE | Quality Engineer Trace Agent | us_quality_trace.rst |
| SYSP_US_RELEASE | Release Engineer Agent | us_release_engineer.rst |
| SYSP_US_SETUP | Setup Engineer Agent | us_setup_engineer.rst |

### Decisions

- D-L0-1: One US per agent, one US for the meta architecture
- D-L0-2: No impacted old SYSPILOT_ user stories (green field)
- D-L0-3: All US tagged `agent-v2` plus role-specific tags

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Links | File |
|----|-------|-------|------|
| SYSP_REQ_AGENT_ARCH_SOUL | Agent Architecture: Soul Definition | SYSP_US_AGENT_ARCH | req_agent_arch.rst |
| SYSP_REQ_AGENT_ARCH_DUTIES | Agent Architecture: Duties Definition | SYSP_US_AGENT_ARCH | req_agent_arch.rst |
| SYSP_REQ_AGENT_ARCH_WORKFLOW | Agent Architecture: Workflow Definition | SYSP_US_AGENT_ARCH | req_agent_arch.rst |
| SYSP_REQ_PM_SOUL | PM Soul | SYSP_US_PM | req_project_mgr.rst |
| SYSP_REQ_PM_DUTIES | PM Duties | SYSP_US_PM | req_project_mgr.rst |
| SYSP_REQ_PM_WORKFLOW | PM Workflow | SYSP_US_PM | req_project_mgr.rst |
| SYSP_REQ_CM_SOUL | CM Soul | SYSP_US_CM | req_change_mgr.rst |
| SYSP_REQ_CM_DUTIES | CM Duties | SYSP_US_CM | req_change_mgr.rst |
| SYSP_REQ_CM_WORKFLOW | CM Workflow | SYSP_US_CM | req_change_mgr.rst |
| SYSP_REQ_QM_SOUL | QM Soul | SYSP_US_QM | req_quality_mgr.rst |
| SYSP_REQ_QM_DUTIES | QM Duties | SYSP_US_QM | req_quality_mgr.rst |
| SYSP_REQ_QM_WORKFLOW | QM Workflow | SYSP_US_QM | req_quality_mgr.rst |
| SYSP_REQ_DESIGN_SOUL | System Designer Soul | SYSP_US_DESIGN | req_system_designer.rst |
| SYSP_REQ_DESIGN_DUTIES | System Designer Duties | SYSP_US_DESIGN | req_system_designer.rst |
| SYSP_REQ_DESIGN_WORKFLOW | System Designer Workflow | SYSP_US_DESIGN | req_system_designer.rst |
| SYSP_REQ_IMPLEMENT_SOUL | Dev Engineer Soul | SYSP_US_IMPLEMENT | req_dev_engineer.rst |
| SYSP_REQ_IMPLEMENT_DUTIES | Dev Engineer Duties | SYSP_US_IMPLEMENT | req_dev_engineer.rst |
| SYSP_REQ_IMPLEMENT_WORKFLOW | Dev Engineer Workflow | SYSP_US_IMPLEMENT | req_dev_engineer.rst |
| SYSP_REQ_UAT_SOUL | Test Engineer Soul | SYSP_US_UAT | req_test_engineer.rst |
| SYSP_REQ_UAT_DUTIES | Test Engineer Duties | SYSP_US_UAT | req_test_engineer.rst |
| SYSP_REQ_UAT_WORKFLOW | Test Engineer Workflow | SYSP_US_UAT | req_test_engineer.rst |
| SYSP_REQ_DOCU_SOUL | Documentation Engineer Soul | SYSP_US_DOCU | req_docu_engineer.rst |
| SYSP_REQ_DOCU_DUTIES | Documentation Engineer Duties | SYSP_US_DOCU | req_docu_engineer.rst |
| SYSP_REQ_DOCU_WORKFLOW | Documentation Engineer Workflow | SYSP_US_DOCU | req_docu_engineer.rst |
| SYSP_REQ_MECE_SOUL | Quality Engineer MECE Soul | SYSP_US_MECE | req_quality_mece.rst |
| SYSP_REQ_MECE_DUTIES | Quality Engineer MECE Duties | SYSP_US_MECE | req_quality_mece.rst |
| SYSP_REQ_MECE_WORKFLOW | Quality Engineer MECE Workflow | SYSP_US_MECE | req_quality_mece.rst |
| SYSP_REQ_TRACE_SOUL | Quality Engineer Trace Soul | SYSP_US_TRACE | req_quality_trace.rst |
| SYSP_REQ_TRACE_DUTIES | Quality Engineer Trace Duties | SYSP_US_TRACE | req_quality_trace.rst |
| SYSP_REQ_TRACE_WORKFLOW | Quality Engineer Trace Workflow | SYSP_US_TRACE | req_quality_trace.rst |
| SYSP_REQ_RELEASE_SOUL | Release Engineer Soul | SYSP_US_RELEASE | req_release_engineer.rst |
| SYSP_REQ_RELEASE_DUTIES | Release Engineer Duties | SYSP_US_RELEASE | req_release_engineer.rst |
| SYSP_REQ_RELEASE_WORKFLOW | Release Engineer Workflow | SYSP_US_RELEASE | req_release_engineer.rst |
| SYSP_REQ_SETUP_SOUL | Setup Engineer Soul | SYSP_US_SETUP | req_setup_engineer.rst |
| SYSP_REQ_SETUP_DUTIES | Setup Engineer Duties | SYSP_US_SETUP | req_setup_engineer.rst |
| SYSP_REQ_SETUP_WORKFLOW | Setup Engineer Workflow | SYSP_US_SETUP | req_setup_engineer.rst |

### Decisions

- D-L1-1: Three REQs per agent: Soul, Duties, Workflow
- D-L1-2: Each REQ links to its parent US
- D-L1-3: REQs use keyword-style descriptions (concise, SHALL-based)

---

## Level 2: Design

**Status**: ✅ completed

### New Design Elements

| ID | Title | Links | File |
|----|-------|-------|------|
| SYSP_SPEC_AGENT_ARCH_SOUL | Soul Definition | SYSP_REQ_AGENT_ARCH_SOUL | spec_agent_arch.rst |
| SYSP_SPEC_AGENT_ARCH_DUTIES | Duties Definition | SYSP_REQ_AGENT_ARCH_DUTIES | spec_agent_arch.rst |
| SYSP_SPEC_AGENT_ARCH_WORKFLOW | Workflow Definition | SYSP_REQ_AGENT_ARCH_WORKFLOW | spec_agent_arch.rst |
| SYSP_SPEC_PM_SOUL | PM Soul Design | SYSP_REQ_PM_SOUL | spec_project_mgr.rst |
| SYSP_SPEC_PM_DUTIES | PM Duties Design | SYSP_REQ_PM_DUTIES | spec_project_mgr.rst |
| SYSP_SPEC_PM_WORKFLOW | PM Workflow Design | SYSP_REQ_PM_WORKFLOW | spec_project_mgr.rst |
| (same pattern for all 11 agents) | | | |

### Decisions

- D-L2-1: Three SPECs per agent matching the three REQs
- D-L2-2: Each SPEC links to its parent REQ
- D-L2-3: SPECs contain detailed content derivable to .agent.md files
