# Change Document: git-flow-and-modes

**Status**: in-progress
**Branch**: feature/git-flow-and-modes
**Created**: 2026-04-15
**Author**: @syspilot.change (CR8)

---

## Summary

Replace the chained branching strategy with a Git-Flow-inspired model using a permanent `development` integration branch. Feature branches are created from `development` and squash-merged back. Add change modes (autonomous/user-guided) as a behavioral qualifier to the Change Manager. Add CM-completion notification to QM as a targeted check trigger.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_SKILL_BRANCHING | Clear Branching Rules for Agents | modified | Replace chained with development branch model |
| SYSP_US_CM | Change Manager Agent | modified | Add change modes + CM→QM notification |
| SYSP_US_QM | Quality Manager Agent | modified | Add CM-completion as trigger path |

### Decisions

- Decision 1: No new User Stories needed — all three topics map to existing US
- Decision 2: Change modes is a behavioral qualifier, not a separate US

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_SKILL_BRANCHING_CHAINED | SYSP_US_SKILL_BRANCHING | major rewrite | Replace chained with development branch model |
| SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION | SYSP_US_SKILL_BRANCHING | modified | Add development→main merge path |
| SYSP_REQ_SKILL_BRANCHING_NAMING | SYSP_US_SKILL_BRANCHING | modified | Add development as permanent branch |
| SYSP_REQ_CM_WORKFLOW | SYSP_US_CM | modified | Add completion notification |
| SYSP_REQ_CM_DUTIES | SYSP_US_CM | modified | Add change modes conditional sentence |
| SYSP_REQ_QM_WORKFLOW | SYSP_US_QM | modified | Add CM-completion trigger |
| SYSP_REQ_QM_DUTIES | SYSP_US_QM | modified | Add targeted check duty |

### Decisions

- Decision 1: Rename SYSP_REQ_SKILL_BRANCHING_CHAINED is not possible (sphinx-needs IDs are stable) — rewrite content instead
- Decision 2: No new REQs — change modes is one sentence in CM_DUTIES

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Specs

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_SKILL_BRANCHING_STRATEGY | SYSP_REQ_SKILL_BRANCHING_CHAINED | major rewrite | New diagram, development branch model |
| SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS | SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION | modified | Add development branch permissions |
| SYSP_SPEC_CM_DUTIES | SYSP_REQ_CM_DUTIES | modified | Add mode-conditional sentence |
| SYSP_SPEC_CM_WORKFLOW | SYSP_REQ_CM_WORKFLOW | modified | Step 0 from development + notify step |
| SYSP_SPEC_QM_WORKFLOW | SYSP_REQ_QM_WORKFLOW | modified | Add CM-completion trigger |
| SYSP_SPEC_QM_DUTIES | SYSP_REQ_QM_DUTIES | modified | Add targeted check duty |
| SYSP_SPEC_DESIGN_WORKFLOW | SYSP_REQ_DESIGN_WORKFLOW | modified | Add Change Document maintenance per level |

### Decisions

- Decision 1: No new SPEC elements needed

---

## Implementation Findings

**Status**: ✅ completed

During CR8 implementation, the following issues were discovered:

### Finding 1: Design Workflow missing Change Document maintenance

The System Designer's workflow listed "propose → discuss → write RST" per level but did
not include "update Change Document → commit" as explicit steps. This caused the Change
Document to be created once at Intake with all levels pre-filled, instead of growing
incrementally with each level commit.

**Fix:** Updated `SYSP_SPEC_DESIGN_WORKFLOW` to include "update Change Document → commit"
in every level step. Added principle: "The Change Document is the living log of the
design process."

### Finding 2: Agent name `syspilot.change` is misleading

The agent was named `syspilot.change` but its persona is "System Designer" and it executes
the "Design Workflow" — a sub-workflow within the CM's Change Workflow. The name suggested
project-level change ownership, which belongs to the Change Manager.

**Fix:** Renamed `syspilot.change` → `syspilot.design` across all files:
- Agent files: `syspilot.change.agent.md` → `syspilot.design.agent.md`
- Prompt files: `syspilot.change.prompt.md` → `syspilot.design.prompt.md`
- All references in agents, skills, copilot-instructions, README, architecture docs

---

## Implementation

**Status**: ✅ completed

### Non-RST Artifacts Updated

| File | Changes |
|------|---------|
| `.github/skills/syspilot.branching/SKILL.md` | Replaced chained branching with development-branch model, updated diagram, workflow, permissions, naming table, YAML description |
| `syspilot/skills/syspilot.branching/SKILL.md` | Synced with installed copy |
| `.github/copilot-instructions.md` | Updated Branching Strategy section and Autonomy sentence for change modes |
| `.github/agents/syspilot.cm.agent.md` | Step 0 from `development`, added change modes, added notify step 9 |
| `syspilot/agents/syspilot.cm.agent.md` | Synced with installed copy |
| `.github/agents/syspilot.qm.agent.md` | Added CM-completion trigger, targeted check duty |
| `syspilot/agents/syspilot.qm.agent.md` | Synced with installed copy |
