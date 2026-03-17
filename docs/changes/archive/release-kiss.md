# Change Document: release-kiss

**Status**: merged
**Branch**: feature/release-kiss
**Created**: 2026-03-16
**Author**: Georg Doll
**Related**: GitHub Issue #5

---

## Summary

Refactor the release agent template from a syspilot-specific playbook into a KISS template. Instead of describing every step (LLMs know how to release), the template focuses on documenting project-specific **design decisions** (version file location, change doc policy, validation commands). First @syspilot.release invocation bootstraps decisions. Change Documents are archived (not deleted) after release.

---

## Level 0: User Stories

### Modified
- **US_REL_AGENT_TEMPLATE**: Release Agent for Consumer Projects (rewritten)

### Unchanged
- US_REL_CREATE, US_REL_VALIDATE

### Decisions
1. Rewrite US_REL_AGENT_TEMPLATE — KISS agent with embedded decisions
2. Release decisions live in the agent file itself
3. First @syspilot.release invocation bootstraps decisions
4. Change documents archived, not deleted

---

## Level 1: Requirements

### Modified
- **REQ_REL_PROCESS_DOC**: Release Agent KISS Template (rewritten)

### Unchanged
- REQ_WF_RELEASE_SEQUENCE, REQ_CHG_CHANGE_DOC (AC-5 already covers archival), REQ_REL_NOTES, REQ_REL_SEMVER

### Decisions
1. Only REQ_REL_PROCESS_DOC rewritten — other REQs already generic
2. Change doc archival not duplicated — already in REQ_CHG_CHANGE_DOC AC-5

---

## Level 2: Design

### Modified
- **SPEC_REL_AGENT**: Release Agent Template (rewritten, added REQ_CHG_CHANGE_DOC link)

### Unchanged
- SPEC_REL_WORKFLOW, SPEC_REL_NOTES_STRUCTURE, SPEC_REL_VERSION_FORMAT, SPEC_REL_VALIDATION_CHECKLIST

### Decisions
1. Only SPEC_REL_AGENT rewritten — other SPECs already correct
2. Added REQ_CHG_CHANGE_DOC link for archival compliance

---

## Final Consistency Check

**Status**: ✅ passed
