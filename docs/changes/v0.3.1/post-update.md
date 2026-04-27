# Change Document: post-update

**Status**: implemented
**Branch**: feature/post-update
**Created**: 2026-04-02
**Author**: @syspilot.change
**Issue**: #16

---

## Summary

After updating syspilot, methodology-owned files are replaced silently. If the project had added custom extensions to those files (e.g., extra verification steps in the verify agent), those additions are lost without warning. This change adds a post-update review step: the Setup Agent compares old vs new for each replaced methodology-owned file, flags content that was present in the old version but missing in the new, and lets the user decide whether to merge their additions back.

---

## Level 0: User Stories

**Status**: ✅ completed

### Modified User Stories
- SYSPILOT_US_INST_UPDATE: Update syspilot to Latest Version — added AC-7 (post-update review) and AC-8 (update on branch)

### Decisions

- Both aspects (post-update diff review + update-on-branch) fit in existing US — no new US needed
- Longer-term alternatives (extension points, skill refs) are out of scope

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements
- SYSPILOT_REQ_INST_POST_UPDATE_REVIEW: Post-Update Extension Review
- SYSPILOT_REQ_INST_UPDATE_BRANCH: Update on Dedicated Branch

### Unchanged Requirements (reviewed)
- SYSPILOT_REQ_INST_VERSION_UPDATE: Core update REQ — new REQs extend its flow
- SYSPILOT_REQ_INST_FILE_OWNERSHIP: Ownership model unchanged; new REQ adds review after replacement
- SYSPILOT_REQ_INST_CUSTOM_PRESERVE: Covers user-owned files; new REQ covers methodology-owned with extensions

### Decisions

- Two new REQs rather than overloading existing ones — keeps concerns separated
- POST_UPDATE_REVIEW links to FILE_OWNERSHIP to express dependency on ownership categories

---

## Level 2: Design

**Status**: ✅ completed

### New Design Specs
- SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW: Post-Update Extension Review
- SYSPILOT_SPEC_INST_UPDATE_BRANCH: Update Branch Workflow

### Modified Design Specs
- SYSPILOT_SPEC_INST_UPDATE_PROCESS: Update Process — added Steps 0a, 3, 6 + links to new specs

### Decisions

- Git-based comparison (`git show HEAD:<path>`) — no temp files needed
- Line-based diff, ignoring whitespace — pragmatic, not semantic
- Branch naming: `update/v{version}` — distinct from `feature/` branches
- Change document created at end of update, after validation
