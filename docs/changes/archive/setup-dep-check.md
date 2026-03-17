# Change Document: setup-dep-check

**Status**: approved
**Branch**: feature/setup-dep-check
**Created**: 2026-03-17
**Author**: syspilot.change

---

## Summary

The setup agent currently skips detection when checking for sphinx-needs and proceeds directly to presenting an install prompt. Customers who have sphinx-needs available via custom scripts or virtual environments are unnecessarily asked to install it. The setup agent should first detect whether sphinx-needs is already available, and only present installation options if it is missing — offering the user a choice between installing via pip/uv or confirming that a custom mechanism provides access.

---

## Level 0: User Stories

**Status**: ✅ completed

### Modified User Stories
- `US_INST_BOOTSTRAP`: AC-1 updated (detect-first), AC-4 added (skip if already available)

---

## Level 1: Requirements

**Status**: ✅ completed

### Modified Requirements
- `REQ_INST_AUTO_SETUP`: AC-1, AC-2 updated; AC-6 added (skip if already available)
- `REQ_INST_SPHINX_NEEDS_DEP`: AC-4 added (accept user confirmation for custom availability)

---

## Level 2: Design

**Status**: ✅ completed

### Modified Design Elements
- `SPEC_INST_SETUP_AGENT`: Section 2 redesigned — detect-first, then branch A/B/C if not found

### Agent Files Updated
- `.github/agents/syspilot.setup.agent.md`: Steps 3–4 redesigned
- `templates/agents/syspilot.setup.agent.md`: Steps 3–4 redesigned (distributable copy)

---

## Final Consistency Check

**Status**: ✅ approved

All elements updated to `:status: approved`. Ready for implementation.



