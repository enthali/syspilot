# Change Document: frontmatter-and-instance-cleanup

**Status**: draft
**Branch**: feature/agent-architecture-v2
**Created**: 2026-04-11
**Author**: System Designer

---

## Summary

Two-part change: (A) Add frontmatter specifications at meta-level and per-agent level (REQ + SPEC), codifying the YAML frontmatter configuration of all 11 agents. (B) Remove the instance layer (`docs/inst/syspilot/`) and all references to it, simplifying the architecture to a single product layer.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_AGENT_ARCH | Agent Architecture US | none | Already covers agent structure; frontmatter is a natural extension |

### New User Stories

None — frontmatter configuration falls within the existing `SYSP_US_AGENT_ARCH` scope. Instance removal is an architectural simplification that doesn't require a new US.

### Decisions

- Decision 1: No new User Stories needed. Frontmatter is an aspect of agent architecture already covered by `SYSP_US_AGENT_ARCH`.
- Decision 2: Instance removal is a simplification, not a new feature. No US required.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_AGENT_ARCH_SOUL | SYSP_US_AGENT_ARCH | none | Unchanged |
| SYSP_REQ_AGENT_ARCH_DUTIES | SYSP_US_AGENT_ARCH | none | Unchanged |
| SYSP_REQ_AGENT_ARCH_WORKFLOW | SYSP_US_AGENT_ARCH | none | Unchanged |

### New Requirements

**Meta-level (append to `docs/syspilot/requirements/req_agent_arch.rst`):**

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_AGENT_ARCH_FRONTMATTER | Agent Frontmatter Definition | SYSP_US_AGENT_ARCH | mandatory |

> Every agent SHALL have YAML frontmatter defining its technical configuration (description, tools, user-invocable, agents, handover).

**Per-agent (append to each agent's req file):**

| ID | Title | Links | File |
|----|-------|-------|------|
| SYSP_REQ_CM_FRONTMATTER | CM Frontmatter Configuration | SYSP_US_CM | req_change_mgr.rst |
| SYSP_REQ_PM_FRONTMATTER | PM Frontmatter Configuration | SYSP_US_PM | req_project_mgr.rst |
| SYSP_REQ_QM_FRONTMATTER | QM Frontmatter Configuration | SYSP_US_QM | req_quality_mgr.rst |
| SYSP_REQ_DESIGN_FRONTMATTER | System Designer Frontmatter Configuration | SYSP_US_DESIGN | req_system_designer.rst |
| SYSP_REQ_IMPLEMENT_FRONTMATTER | Dev Engineer Frontmatter Configuration | SYSP_US_IMPLEMENT | req_dev_engineer.rst |
| SYSP_REQ_UAT_FRONTMATTER | Test Engineer Frontmatter Configuration | SYSP_US_UAT | req_test_engineer.rst |
| SYSP_REQ_DOCU_FRONTMATTER | Docu Engineer Frontmatter Configuration | SYSP_US_DOCU | req_docu_engineer.rst |
| SYSP_REQ_MECE_FRONTMATTER | MECE Engineer Frontmatter Configuration | SYSP_US_MECE | req_quality_mece.rst |
| SYSP_REQ_TRACE_FRONTMATTER | Trace Engineer Frontmatter Configuration | SYSP_US_TRACE | req_quality_trace.rst |
| SYSP_REQ_RELEASE_FRONTMATTER | Release Engineer Frontmatter Configuration | SYSP_US_RELEASE | req_release_engineer.rst |
| SYSP_REQ_SETUP_FRONTMATTER | Setup Engineer Frontmatter Configuration | SYSP_US_SETUP | req_setup_engineer.rst |

Each per-agent REQ specifies the concrete field values with rationale (why these tools, why user-invocable or not, why these subagents).

### Conflicts Detected

None.

### Decisions

- Decision 1: Per-agent frontmatter REQs link to their own agent US (e.g., `SYSP_REQ_CM_FRONTMATTER` → `SYSP_US_CM`), not to `SYSP_US_AGENT_ARCH`. The meta-level REQ covers the schema; per-agent REQs cover the concrete values.
- Decision 2: The `handover` field is not currently used by any agent. Per-agent specs will omit it (documented as not configured).

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_AGENT_ARCH_SOUL | SYSP_REQ_AGENT_ARCH_SOUL | none | Unchanged |
| SYSP_SPEC_AGENT_ARCH_DUTIES | SYSP_REQ_AGENT_ARCH_DUTIES | none | Unchanged |
| SYSP_SPEC_AGENT_ARCH_WORKFLOW | SYSP_REQ_AGENT_ARCH_WORKFLOW | none | Unchanged |

### New Design Elements

**Meta-level (append to `docs/syspilot/design/spec_agent_arch.rst`):**

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_AGENT_ARCH_FRONTMATTER | Frontmatter Field Schema | SYSP_REQ_AGENT_ARCH_FRONTMATTER |

> Field schema: `description` (string, agent purpose for Copilot discovery), `tools` (list, permitted tool categories), `user-invocable` (bool, whether users can invoke directly), `agents` (list, subagents this agent can call via runSubagent), `handover` (string, optional transfer target).

**Per-agent (append to each agent's spec file):**

| ID | Title | Links | File |
|----|-------|-------|------|
| SYSP_SPEC_CM_FRONTMATTER | CM Frontmatter | SYSP_REQ_CM_FRONTMATTER | spec_change_mgr.rst |
| SYSP_SPEC_PM_FRONTMATTER | PM Frontmatter | SYSP_REQ_PM_FRONTMATTER | spec_project_mgr.rst |
| SYSP_SPEC_QM_FRONTMATTER | QM Frontmatter | SYSP_REQ_QM_FRONTMATTER | spec_quality_mgr.rst |
| SYSP_SPEC_DESIGN_FRONTMATTER | System Designer Frontmatter | SYSP_REQ_DESIGN_FRONTMATTER | spec_system_designer.rst |
| SYSP_SPEC_IMPLEMENT_FRONTMATTER | Dev Engineer Frontmatter | SYSP_REQ_IMPLEMENT_FRONTMATTER | spec_dev_engineer.rst |
| SYSP_SPEC_UAT_FRONTMATTER | Test Engineer Frontmatter | SYSP_REQ_UAT_FRONTMATTER | spec_test_engineer.rst |
| SYSP_SPEC_DOCU_FRONTMATTER | Docu Engineer Frontmatter | SYSP_REQ_DOCU_FRONTMATTER | spec_docu_engineer.rst |
| SYSP_SPEC_MECE_FRONTMATTER | MECE Engineer Frontmatter | SYSP_REQ_MECE_FRONTMATTER | spec_quality_mece.rst |
| SYSP_SPEC_TRACE_FRONTMATTER | Trace Engineer Frontmatter | SYSP_REQ_TRACE_FRONTMATTER | spec_quality_trace.rst |
| SYSP_SPEC_RELEASE_FRONTMATTER | Release Engineer Frontmatter | SYSP_REQ_RELEASE_FRONTMATTER | spec_release_engineer.rst |
| SYSP_SPEC_SETUP_FRONTMATTER | Setup Engineer Frontmatter | SYSP_REQ_SETUP_FRONTMATTER | spec_setup_engineer.rst |

Each per-agent SPEC contains the exact frontmatter configuration matching the actual `.agent.md` file:

#### Frontmatter Values per Agent

| Agent | description | tools | user-invocable | agents |
|-------|-------------|-------|----------------|--------|
| **CM** | Central orchestrator of the change workflow. Receives Change Requests, invokes engineers in sequence, enforces quality gates, and reports completion with full traceability. | read, edit, search, agent, todo, execute, syspilot_jarvis_tools | true | syspilot.change, syspilot.uat, syspilot.implement, syspilot.mece, syspilot.trace, syspilot.release, syspilot.docu |
| **PM** | Strategic project manager that discusses features, prioritizes backlogs, conducts research, and delegates Change Requests to the Change Manager. | read, search, web, agent, todo, vscode, execute, github, context7, syspilot_jarvis_tools | true | *(none)* |
| **QM** | Independent quality guardian that dispatches MECE and Trace engineers, consolidates findings, and creates Change Requests for quality issues. | read, edit, search, agent, todo, execute, syspilot_jarvis_tools | true | syspilot.mece, syspilot.trace |
| **System Designer** | Subagent that analyzes change requests level-by-level (US → REQ → SPEC) with a persistent Change Document. Writes RST files with full traceability. | read, edit, search, todo, execute | false | syspilot.mece |
| **Dev Engineer** | Subagent that implements code changes from approved Change Documents. Reads specs, writes code, writes tests, commits with traceability. | read, edit, search, todo, execute | false | *(none)* |
| **Test Engineer** | Subagent that generates User Acceptance Test artifacts (stories, requirements, design specs) for a Change Document. | read, edit, search, todo, execute | false | *(none)* |
| **Docu Engineer** | Subagent that keeps internal and external documentation in sync with reality. Updates copilot-instructions.md, context.md, README, and methodology docs. | read, edit, search, todo, execute | false | *(none)* |
| **MECE Engineer** | Subagent that analyzes one specification level for MECE properties — finds redundancies, gaps, contradictions, and overlaps. | read, search, todo | false | *(none)* |
| **Trace Engineer** | Subagent that traces one specification element vertically through all levels (US → REQ → SPEC) and checks traceability completeness. | read, search, execute | false | *(none)* |
| **Release Engineer** | Subagent that guides the release process: squash merge, version bump, validation, release notes, change doc archival, git tagging. | read, edit, search, execute | false | *(none)* |
| **Setup Engineer** | Subagent that installs and updates syspilot in a project. Detects environment, manages dependencies, copies files, validates with sphinx-build. | read, edit, search, execute | false | *(none)* |

> **Note:** No agent currently uses the `handover` field. Per-agent specs will omit it.

### Conflicts Detected

None.

### Decisions

- Decision 1: Per-agent SPECs document the exact current frontmatter from `.agent.md` files — no aspirational values.
- Decision 2: `handover` is defined in the meta-level schema but not used per-agent yet.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Part B: Instance Layer Removal

### Files to Delete

| # | File | Content |
|---|------|---------|
| 1 | `docs/inst/syspilot/userstories/index.rst` | Instance US toctree |
| 2 | `docs/inst/syspilot/userstories/us_implement.rst` | Instance implement US |
| 3 | `docs/inst/syspilot/userstories/us_release.rst` | Instance release US |
| 4 | `docs/inst/syspilot/requirements/index.rst` | Instance REQ toctree |
| 5 | `docs/inst/syspilot/requirements/req_implement.rst` | Instance implement REQ |
| 6 | `docs/inst/syspilot/requirements/req_release.rst` | Instance release REQ |
| 7 | `docs/inst/syspilot/design/index.rst` | Instance SPEC toctree |
| 8 | `docs/inst/syspilot/design/spec_implement.rst` | Instance implement SPEC |
| 9 | `docs/inst/syspilot/design/spec_release.rst` | Instance release SPEC |

### Reference Updates

| # | File | Change |
|---|------|--------|
| 1 | `docs/index.rst` | Remove toctree section "syspilot Instance (Dogfooding)" with 3 entries: `inst/syspilot/userstories/index`, `inst/syspilot/requirements/index`, `inst/syspilot/design/index` |
| 2 | `.github/copilot-instructions.md` | Remove `inst/syspilot/` block from Project Structure tree (lines ~66–69); remove `Instance specs (project-specific)` line from Specification Hierarchy (line ~89) |
| 3 | `docs/architecture.md` | Remove or rewrite "What is Instance?" section and Instance references throughout. Keep "What is Product?" section. Update Overview table to remove Instance row. |

### Decisions

- Decision 1: Delete the entire `docs/inst/syspilot/` directory tree (9 files, 3 subdirectories).
- Decision 2: `docs/architecture.md` should be simplified to describe product-only architecture, noting that the Instance concept was removed.

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

**Part A — Frontmatter (meta-level):**

| User Story | Requirement | Design | Complete? |
|------------|-------------|--------|-----------|
| SYSP_US_AGENT_ARCH | SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_SPEC_AGENT_ARCH_FRONTMATTER | ✅ |

**Part A — Frontmatter (per-agent):**

| User Story | Requirement | Design | Complete? |
|------------|-------------|--------|-----------|
| SYSP_US_CM | SYSP_REQ_CM_FRONTMATTER | SYSP_SPEC_CM_FRONTMATTER | ✅ |
| SYSP_US_PM | SYSP_REQ_PM_FRONTMATTER | SYSP_SPEC_PM_FRONTMATTER | ✅ |
| SYSP_US_QM | SYSP_REQ_QM_FRONTMATTER | SYSP_SPEC_QM_FRONTMATTER | ✅ |
| SYSP_US_DESIGN | SYSP_REQ_DESIGN_FRONTMATTER | SYSP_SPEC_DESIGN_FRONTMATTER | ✅ |
| SYSP_US_IMPLEMENT | SYSP_REQ_IMPLEMENT_FRONTMATTER | SYSP_SPEC_IMPLEMENT_FRONTMATTER | ✅ |
| SYSP_US_UAT | SYSP_REQ_UAT_FRONTMATTER | SYSP_SPEC_UAT_FRONTMATTER | ✅ |
| SYSP_US_DOCU | SYSP_REQ_DOCU_FRONTMATTER | SYSP_SPEC_DOCU_FRONTMATTER | ✅ |
| SYSP_US_MECE | SYSP_REQ_MECE_FRONTMATTER | SYSP_SPEC_MECE_FRONTMATTER | ✅ |
| SYSP_US_TRACE | SYSP_REQ_TRACE_FRONTMATTER | SYSP_SPEC_TRACE_FRONTMATTER | ✅ |
| SYSP_US_RELEASE | SYSP_REQ_RELEASE_FRONTMATTER | SYSP_SPEC_RELEASE_FRONTMATTER | ✅ |
| SYSP_US_SETUP | SYSP_REQ_SETUP_FRONTMATTER | SYSP_SPEC_SETUP_FRONTMATTER | ✅ |

**Part B — Instance Removal:**

No traceability items — this is a deletion of existing content and reference cleanup.

### Files Summary

**Files to modify (Part A — append new specs):**

| # | File | New Element |
|---|------|-------------|
| 1 | `docs/syspilot/requirements/req_agent_arch.rst` | SYSP_REQ_AGENT_ARCH_FRONTMATTER |
| 2 | `docs/syspilot/design/spec_agent_arch.rst` | SYSP_SPEC_AGENT_ARCH_FRONTMATTER |
| 3 | `docs/syspilot/requirements/req_change_mgr.rst` | SYSP_REQ_CM_FRONTMATTER |
| 4 | `docs/syspilot/requirements/req_project_mgr.rst` | SYSP_REQ_PM_FRONTMATTER |
| 5 | `docs/syspilot/requirements/req_quality_mgr.rst` | SYSP_REQ_QM_FRONTMATTER |
| 6 | `docs/syspilot/requirements/req_system_designer.rst` | SYSP_REQ_DESIGN_FRONTMATTER |
| 7 | `docs/syspilot/requirements/req_dev_engineer.rst` | SYSP_REQ_IMPLEMENT_FRONTMATTER |
| 8 | `docs/syspilot/requirements/req_test_engineer.rst` | SYSP_REQ_UAT_FRONTMATTER |
| 9 | `docs/syspilot/requirements/req_docu_engineer.rst` | SYSP_REQ_DOCU_FRONTMATTER |
| 10 | `docs/syspilot/requirements/req_quality_mece.rst` | SYSP_REQ_MECE_FRONTMATTER |
| 11 | `docs/syspilot/requirements/req_quality_trace.rst` | SYSP_REQ_TRACE_FRONTMATTER |
| 12 | `docs/syspilot/requirements/req_release_engineer.rst` | SYSP_REQ_RELEASE_FRONTMATTER |
| 13 | `docs/syspilot/requirements/req_setup_engineer.rst` | SYSP_REQ_SETUP_FRONTMATTER |
| 14 | `docs/syspilot/design/spec_change_mgr.rst` | SYSP_SPEC_CM_FRONTMATTER |
| 15 | `docs/syspilot/design/spec_project_mgr.rst` | SYSP_SPEC_PM_FRONTMATTER |
| 16 | `docs/syspilot/design/spec_quality_mgr.rst` | SYSP_SPEC_QM_FRONTMATTER |
| 17 | `docs/syspilot/design/spec_system_designer.rst` | SYSP_SPEC_DESIGN_FRONTMATTER |
| 18 | `docs/syspilot/design/spec_dev_engineer.rst` | SYSP_SPEC_IMPLEMENT_FRONTMATTER |
| 19 | `docs/syspilot/design/spec_test_engineer.rst` | SYSP_SPEC_UAT_FRONTMATTER |
| 20 | `docs/syspilot/design/spec_docu_engineer.rst` | SYSP_SPEC_DOCU_FRONTMATTER |
| 21 | `docs/syspilot/design/spec_quality_mece.rst` | SYSP_SPEC_MECE_FRONTMATTER |
| 22 | `docs/syspilot/design/spec_quality_trace.rst` | SYSP_SPEC_TRACE_FRONTMATTER |
| 23 | `docs/syspilot/design/spec_release_engineer.rst` | SYSP_SPEC_RELEASE_FRONTMATTER |
| 24 | `docs/syspilot/design/spec_setup_engineer.rst` | SYSP_SPEC_SETUP_FRONTMATTER |

**Files to modify (Part B — reference updates):**

| # | File | Change |
|---|------|--------|
| 25 | `docs/index.rst` | Remove instance toctree section |
| 26 | `.github/copilot-instructions.md` | Remove inst/syspilot references |
| 27 | `docs/architecture.md` | Rewrite to remove Instance concept |

**Files to delete (Part B):**

| # | File |
|---|------|
| 28 | `docs/inst/syspilot/userstories/index.rst` |
| 29 | `docs/inst/syspilot/userstories/us_implement.rst` |
| 30 | `docs/inst/syspilot/userstories/us_release.rst` |
| 31 | `docs/inst/syspilot/requirements/index.rst` |
| 32 | `docs/inst/syspilot/requirements/req_implement.rst` |
| 33 | `docs/inst/syspilot/requirements/req_release.rst` |
| 34 | `docs/inst/syspilot/design/index.rst` |
| 35 | `docs/inst/syspilot/design/spec_implement.rst` |
| 36 | `docs/inst/syspilot/design/spec_release.rst` |

### Sign-off

- [ ] All levels completed
- [ ] All conflicts resolved
- [ ] Traceability verified
- [ ] Ready for implementation

---

## Appendix: Link Discovery Results

Part A links discovered from `SYSP_US_AGENT_ARCH`:
- → `SYSP_REQ_AGENT_ARCH_SOUL`, `SYSP_REQ_AGENT_ARCH_DUTIES`, `SYSP_REQ_AGENT_ARCH_WORKFLOW`
- → `SYSP_SPEC_AGENT_ARCH_SOUL`, `SYSP_SPEC_AGENT_ARCH_DUTIES`, `SYSP_SPEC_AGENT_ARCH_WORKFLOW`

Per-agent links: Each `SYSP_US_<ROLE>` → `SYSP_REQ_<ROLE>_{SOUL,DUTIES,WORKFLOW}` → `SYSP_SPEC_<ROLE>_{SOUL,DUTIES,WORKFLOW}`.
New FRONTMATTER elements follow the same chain: `SYSP_US_<ROLE>` → `SYSP_REQ_<ROLE>_FRONTMATTER` → `SYSP_SPEC_<ROLE>_FRONTMATTER`.
