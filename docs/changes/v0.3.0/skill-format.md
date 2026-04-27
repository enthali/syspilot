# Change Document: skill-format

**Status**: merged
**Branch**: feature/skill-format
**Created**: 2026-03-31
**Author**: Georg Doll
**Issue**: [#12 — Migrate skills to VS Code standard format](https://github.com/enthali/syspilot/issues/12)

---

## Summary

Migrate skill files from the proprietary flat format (`syspilot.<name>.skill.md`) to the
VS Code standard folder-based format (`.github/skills/<name>/SKILL.md`) with YAML frontmatter
(`name` and `description` fields). This enables automatic skill discovery by Copilot and aligns
with VS Code ecosystem conventions. All references across specs, agents, copilot-instructions.md,
and the Setup Agent install logic must be updated accordingly.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSPILOT_US_DX_AGENT_INTERACTION | Consistent Agent Interaction via Selection Menus | unchanged | Parent US — skill format is a design refinement |
| SYSPILOT_US_INST_UPDATE | Update syspilot to Latest Version | unchanged | Setup Agent scope unaffected |
| SYSPILOT_US_INST_NEW_PROJECT | Install syspilot in New Project | unchanged | Installation scope unaffected |

### New User Stories

*None needed.* The existing US already cover the intent. Format migration is a Level 1/2 concern.

### Decisions

- No US changes required — agreed with user.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed — none found

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSPILOT_REQ_DX_AGENT_SKILL_FILES | SYSPILOT_US_DX_AGENT_INTERACTION | modified | Add AC-4 for VS Code standard format / auto-discovery |
| SYSPILOT_REQ_DX_AGENT_SELECTION_MENUS | SYSPILOT_US_DX_AGENT_INTERACTION | unchanged | About interaction pattern, not file format |
| SYSPILOT_REQ_INST_FILE_OWNERSHIP | SYSPILOT_US_INST_UPDATE | unchanged | Ownership rules unchanged |
| SYSPILOT_REQ_INST_TEMPLATE_SOURCE | SYSPILOT_US_INST_CROSS_PROJECT | unchanged | Distribution model unchanged |

### Modified Requirements

- SYSPILOT_REQ_DX_AGENT_SKILL_FILES: Added AC-4 (VS Code standard skill format for auto-discovery)

### New Requirements

*None needed.*

### Decisions

- Add AC-4 to SYSPILOT_REQ_DX_AGENT_SKILL_FILES — agreed with user.
- No new requirements needed.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All modified REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSPILOT_SPEC_AGENT_INTERACTION | SYSPILOT_REQ_DX_AGENT_SKILL_FILES | modified | Skill path + activation: manual → auto-discovery |
| SYSPILOT_SPEC_INST_SETUP_AGENT | SYSPILOT_REQ_INST_FILE_OWNERSHIP | modified | Copy rule: folder-based skill copy |
| SYSPILOT_SPEC_INST_FILE_OWNERSHIP | SYSPILOT_REQ_INST_FILE_OWNERSHIP | modified | Glob pattern for skills |
| SYSPILOT_SPEC_INST_UPDATE_PROCESS | SYSPILOT_REQ_INST_FILE_OWNERSHIP | modified | Skills row in update table |
| SYSPILOT_SPEC_INST_RELEASE_STRUCTURE | SYSPILOT_REQ_INST_TEMPLATE_SOURCE | modified | Directory tree: folder format |
| SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT | SYSPILOT_REQ_INST_TEMPLATE_SOURCE | modified | Distribution tree: folder format |
| SYSPILOT_SPEC_MEM_INSTRUCTIONS_STRUCTURE | SYSPILOT_REQ_DX_MEMORY_AGENT | modified | Agent Interaction section note |

### Modified Design Elements

- SYSPILOT_SPEC_AGENT_INTERACTION: Skill path → folder format, activation → auto-discovery
- SYSPILOT_SPEC_INST_SETUP_AGENT: Copy rule → folder-based skill copy
- SYSPILOT_SPEC_INST_FILE_OWNERSHIP: Glob pattern → folder format
- SYSPILOT_SPEC_INST_UPDATE_PROCESS: Skills row → folder format
- SYSPILOT_SPEC_INST_RELEASE_STRUCTURE: Directory tree → folder layout
- SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT: Distribution tree → folder layout
- SYSPILOT_SPEC_MEM_INSTRUCTIONS_STRUCTURE: Agent Interaction line updated

### Decisions

- All 7 specs modified — agreed with user.
- Manual activation in copilot-instructions.md replaced by auto-discovery.
- Product copy in syspilot/skills/ also uses folder format.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All modified SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|------------|--------|-----------|
| SYSPILOT_US_DX_AGENT_INTERACTION | SYSPILOT_REQ_DX_AGENT_SKILL_FILES (+AC-4) | SYSPILOT_SPEC_AGENT_INTERACTION | ✅ |
| SYSPILOT_US_INST_UPDATE | SYSPILOT_REQ_INST_FILE_OWNERSHIP | SYSPILOT_SPEC_INST_FILE_OWNERSHIP, SYSPILOT_SPEC_INST_UPDATE_PROCESS | ✅ |
| SYSPILOT_US_INST_NEW_PROJECT | SYSPILOT_REQ_INST_TEMPLATE_SOURCE | SYSPILOT_SPEC_INST_SETUP_AGENT, SYSPILOT_SPEC_INST_RELEASE_STRUCTURE, SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT | ✅ |
| SYSPILOT_US_DX_PROJECT_MEMORY | SYSPILOT_REQ_DX_MEMORY_AGENT | SYSPILOT_SPEC_MEM_INSTRUCTIONS_STRUCTURE | ✅ |

### Cross-Level Consistency

- All levels aligned: US intent → REQ behavior → SPEC implementation
- No semantic drift, no orphaned elements

### Summary

| Level | Changes |
|-------|---------|
| Level 0 | 0 US modified, 0 new |
| Level 1 | 1 REQ modified (SYSPILOT_REQ_DX_AGENT_SKILL_FILES +AC-4) |
| Level 2 | 7 SPECs modified |
