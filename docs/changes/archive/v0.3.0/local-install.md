# Change Document: local-install

**Status**: approved
**Branch**: feature/local-install
**Created**: 2026-04-01
**Author**: @enthali
**GitHub Issue**: #9

---

## Summary

The Setup Agent currently only supports installing/updating syspilot via curl from GitHub. This change adds a **local install mode** that detects a `syspilot/` directory in the repo root and offers the user a choice between local copy and GitHub fetch, enabling dogfooding and fork-based development.

---

## Level 0: User Stories

**Status**: ✅ completed

### Modified User Stories
- SYSPILOT_US_INST_NEW_PROJECT: Added acceptance scenario 5 (local source choice)
- SYSPILOT_US_INST_ADOPT_EXISTING: Added acceptance scenario 5 (local source choice)
- SYSPILOT_US_INST_UPDATE: Added acceptance scenario 3 (local source choice)

### Decisions
- No new US needed — local-vs-remote source is a HOW detail, not a new WHY

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements
- SYSPILOT_REQ_INST_LOCAL_SOURCE: Local Install Source Detection

### Modified Requirements
- SYSPILOT_REQ_INST_NEW_PROJECT: AC-4 updated to include local source
- SYSPILOT_REQ_INST_ADOPT_EXISTING: AC-5 updated to include local source
- SYSPILOT_REQ_INST_VERSION_UPDATE: AC-5 updated to include local source
- SYSPILOT_REQ_INST_BOOTSTRAP_SELF: Description + AC-1 updated for local source

---

## Level 2: Design

**Status**: ✅ completed

### New Design Elements
- SYSPILOT_SPEC_INST_SOURCE_DETECTION: Install Source Detection (detection logic, user prompt, local copy mechanism)

### Modified Design Elements
- SYSPILOT_SPEC_INST_SETUP_AGENT: Added Section 0 (source detection), Section 3 branching (local vs GitHub)
- SYSPILOT_SPEC_INST_UPDATE_PROCESS: Steps 0-2 updated for local/GitHub branching
- SYSPILOT_SPEC_INST_VERSION_MARKER: `source` field now supports `"local"` value
