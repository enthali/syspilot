# Change Document: setup-update

**Status**: approved
**Branch**: feature/setup-update
**Created**: 2026-03-27
**Author**: Georg Doll

---

## Summary

Fix the setup agent update process with clear file ownership model. The setup agent
must bootstrap itself first, then replace syspilot-owned methodology agents wholesale
while never touching project-owned agents (release, implement). Template agents for
release and implement get a reminder banner prompting users to customize via @change.
Also fix stale `templates/` references in specs (now `syspilot/`).

---

## Decisions

1. **Bootstrap**: Setup agent updates itself first before updating anything else
2. **Methodology agents** (change, verify, mece, trace, memory, setup): always replaced on update
3. **Project agents** (release, implement): copied on initial install, never touched on update
4. **Template banner**: Generic release/implement agents ship with customization reminder
5. **Stale paths**: Fix `templates/` → `syspilot/` in all setup-related specs

---

## Level 0: User Stories

### Modified User Stories
- `SYSPILOT_US_INST_UPDATE`: Refined AC-2 (explicit ownership model), added AC-5 (bootstrap)
- `SYSPILOT_US_INST_AGNOSTIC`: Refined AC-3 (never modified), added AC-5 (template banner)

## Level 1: Requirements

### New Requirements
- `SYSPILOT_REQ_INST_BOOTSTRAP_SELF`: Setup Agent Self-Update
- `SYSPILOT_REQ_INST_FILE_OWNERSHIP`: File Ownership Categories

### Modified Requirements
- `SYSPILOT_REQ_INST_VERSION_UPDATE`: Added AC-7 (bootstrap), AC-3 references ownership, AC-6 path fix
- `SYSPILOT_REQ_INST_CUSTOM_PRESERVE`: AC-3 references FILE_OWNERSHIP
- `SYSPILOT_REQ_INST_TEMPLATE_SOURCE`: `templates/` → `syspilot/` throughout
- `SYSPILOT_REQ_INST_NEW_PROJECT`: AC-6 path fix
- `SYSPILOT_REQ_INST_ADOPT_EXISTING`: AC-6 path fix
- `SYSPILOT_REQ_INST_IMPL_SKELETON`: Added AC-6 (template banner)

## Level 2: Design Specs

### Rewritten Specs
- `SYSPILOT_SPEC_INST_UPDATE_PROCESS`: Bootstrap self-update + ownership-based update flow
- `SYSPILOT_SPEC_INST_FILE_OWNERSHIP`: Explicit 3-category ownership model

### Path Fixes (templates/ → syspilot/)
- `SYSPILOT_SPEC_INST_CURL_BOOTSTRAP`
- `SYSPILOT_SPEC_INST_SETUP_AGENT`
- `SYSPILOT_SPEC_INST_VERSION_MARKER`
- `SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT`
- `SYSPILOT_SPEC_INST_RELEASE_STRUCTURE`
- `SYSPILOT_SPEC_INST_SELF_INSTALL`
