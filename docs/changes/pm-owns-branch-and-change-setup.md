# Change Document: pm-owns-branch-and-change-setup

**Status**: in-progress
**Branch**: feature/pm-owns-branch-and-change-setup
**Created**: 2026-05-21
**Author**: PM

---

## Summary

Clarify and enforce the ownership boundary between PM and CM for branch creation, Change Document initialization, and integration. PM creates the feature branch from `development` and creates the Change Document by copying `syspilot/templates/change-document.md` verbatim to `docs/changes/<name>.md`, then fills only the header fields and the `## Summary` section before sending the CR — the L0/L1/L2/MECE/Traceability/Sign-off sections remain untouched template skeleton. CM receives the ready-made branch and template-copied document and fills the engineering sections in-place, never replacing the template structure with hand-written content. Integration into `development` is the responsibility of the PM role — CM signals readiness, the integrator performs the merge. Feature branches are retained after merge for forensic/bisect purposes and cleaned up by the Release Agent at release time. Motivation: without explicit, verbatim-template ownership of branch and document setup, agents will improvise document structures, which silently erodes traceability and MECE discipline; explicit structural ownership and a hard "copy template, do not invent" rule eliminate this class of drift. Acceptance: (1) PM agent describes the `Copy-Item` from template + which exact fields PM fills (header + Summary only), (2) CM agent states CM receives branch + template-copied CD from PM and never creates the document or replaces its skeleton, (3) CM agent states CM never merges to `development` — Integration is a PM-role responsibility, (4) feature branches are not deleted after merge, (5) Release Agent file describes the cleanup step.

---

## Level 0: User Stories

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_xxx | ... | modified | ... |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSPILOT_US_NEW_1 | As a..., I want..., so that... | mandatory |

### Decisions

- Decision 1: ...
- Decision 2: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing User Stories
- [ ] No redundancies
- [ ] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_xxx | US_xxx | modified | ... |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSPILOT_REQ_NEW_1 | ... | US_xxx | mandatory |

### Conflicts Detected

- ⚠️ REQ_xxx vs REQ_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Requirements
- [ ] No redundancies
- [ ] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_xxx | REQ_xxx | modified | ... |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSPILOT_SPEC_NEW_1 | ... | REQ_xxx, SYSPILOT_REQ_NEW_1 |

### Conflicts Detected

- ⚠️ SPEC_xxx vs SPEC_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Designs
- [ ] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ⏳ not started | ✅ passed | ❌ failed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_xxx | REQ_xxx | SPEC_xxx | ✅ |
| SYSPILOT_US_NEW_1 | SYSPILOT_REQ_NEW_1 | SYSPILOT_SPEC_NEW_1 | ✅ |

### Artefakt-Removal-Check

*Fill in only when this CR removes an artefact (file, field, configuration key, REQ-ID).*

For each removed artefact, run a project-wide grep on all plausible name variants and classify results:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `{artefact name}` | {files + lines fixed / none} | {files + lines fixed / none} | {count — acceptable historic stranding} |

- [ ] All class (a) active code/workflow references fixed in this CR
- [ ] All class (b) active documentation references fixed in this CR
- [ ] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

- [ ] Issue 1: ...
- [ ] Issue 2: ...

### Sign-off

- [ ] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [ ] All conflicts resolved
- [ ] Traceability verified
- [ ] Ready for implementation

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
