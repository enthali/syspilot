# Change Document: pm-owns-branch-and-change-setup

**Status**: in-progress
**Branch**: feature/pm-owns-branch-and-change-setup
**Created**: 2026-05-21
**Author**: PM

---

## Summary

Clarify and enforce the ownership boundary between PM and CM for branch creation, Change Document initialization, and integration. PM creates the feature branch from `development` and creates the Change Document by copying `.github/templates/change-document.md` verbatim to `docs/changes/<name>.md`, then fills only the header fields and the `## Summary` section before sending the CR — the L0/L1/L2/MECE/Traceability/Sign-off sections remain untouched template skeleton. CM receives the ready-made branch and template-copied document and fills the engineering sections in-place, never replacing the template structure with hand-written content. Integration into `development` is the responsibility of the PM role — CM signals readiness, the integrator performs the merge. Feature branches are retained after merge for forensic/bisect purposes and cleaned up by the Release Agent at release time. Templates live at `.github/templates/` so they are present in any installed instance (Kunden-Repo) alongside agents/prompts/skills; the corresponding Setup-Agent sync logic (`syspilot/templates/` → `.github/templates/`) is scope of a separate follow-up CR. Motivation: without explicit, verbatim-template ownership of branch and document setup, agents will improvise document structures, which silently erodes traceability and MECE discipline; explicit structural ownership and a hard "copy template, do not invent" rule eliminate this class of drift. Acceptance: (1) PM agent describes the `Copy-Item .github/templates/change-document.md` + which exact fields PM fills (header + Summary only), (2) CM agent states CM receives branch + template-copied CD from PM and never creates the document or replaces its skeleton, (3) CM agent states CM never merges to `development` — Integration is a PM-role responsibility, (4) feature branches are not deleted after merge, (5) Release Agent file describes the cleanup step, (6) `.github/templates/change-document.md` exists in the repo as the installed-instance copy of the template.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_PM | Project Manager Agent | modified | Added duties for Change Initialization + Integration Responsibility; updated AC4 (PM performs merge); added AC7 (branch+doc setup) |
| SYSP_US_CM | Change Manager Agent | modified | Sharpened duties: Merge Abstinence (never merges), Change Auditability (PM creates doc, CM fills); updated ACs 7-9 |
| SYSP_US_RELEASE | Release Engineer Agent | modified | Added duty for feature-branch cleanup at release time; added AC7 |

### New User Stories

_(none — existing USes cover the scope)_

### Decisions

- Decision 1: SYSP_US_SETUP is explicitly out of scope (deferred follow-up CR for Setup-Agent sync logic)
- Decision 2: PM US duty "Autorität über Merge und Release" split into "Change Initialization" + "Integration Responsibility" for clarity
- Decision 3: CM US no longer creates branch or Change Document — these are PM responsibilities

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_PM_DUTIES | SYSP_US_PM | modified | Added ACs 4-6 for Change Initialization + Integration Responsibility; renumbered remaining |
| SYSP_REQ_PM_WORKFLOW | SYSP_US_PM | modified | Added ACs 5-6 (branch creation, template copy); AC-7 (delegation with branch+path); AC-9 (PM performs merge); AC-10 (branch retention) |
| SYSP_REQ_CM_DUTIES | SYSP_US_CM | modified | AC-4 updated (PM creates doc, CM fills); AC-5 (merge abstinence); AC-6 (readiness notification); status → approved |
| SYSP_REQ_CM_WORKFLOW | SYSP_US_CM | modified | Removed Branch/CD creation steps; added checkout step; updated merge language; status → approved |
| SYSP_REQ_RELEASE_DUTIES | SYSP_US_RELEASE | modified | Added AC-6 for feature-branch cleanup |
| SYSP_REQ_RELEASE_WORKFLOW | SYSP_US_RELEASE | modified | Added AC-8 for branch cleanup step |

### New Requirements

_(none — existing REQs cover the scope after modification)_

### Conflicts Detected

_(none)_

### Decisions

- Decision 1: SYSP_REQ_CM_DUTIES and SYSP_REQ_CM_WORKFLOW promoted from `draft` to `approved` since they now reflect the agreed bootstrap state
- Decision 2: SYSP_REQ_SETUP_BOOTLOADER_* not touched (deferred follow-up CR for template sync)
- Decision 3: The Installer scope REQ (SYSP_REQ_INSTALLER_SCOPE) already maps `syspilot/templates/` → `.syspilot/templates/` — a separate follow-up CR will add the `.github/templates/` path when Setup-Agent sync is implemented

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_PM_DUTIES | SYSP_REQ_PM_DUTIES | modified | Replaced "Merge and Release Authority" with "Change Initialization" + "Integration Responsibility" |
| SYSP_SPEC_PM_WORKFLOW | SYSP_REQ_PM_WORKFLOW | modified | Added Create Branch, Create Change Document, SEND steps; updated QM workflow to perform merge |
| SYSP_SPEC_CM_DUTIES | SYSP_REQ_CM_DUTIES | modified | Updated Change Auditability (template ownership), replaced Merge-Authority with Merge Abstinence, updated PM Notification; status → approved |
| SYSP_SPEC_CM_WORKFLOW | SYSP_REQ_CM_WORKFLOW | modified | Removed Branch+CD creation steps; CM receives branch from PM; updated PM Decision mapping (PM merges); status → approved |
| SYSP_SPEC_RELEASE_DUTIES | SYSP_REQ_RELEASE_DUTIES | modified | Added Feature Branch Cleanup duty |
| SYSP_SPEC_RELEASE_WORKFLOW | SYSP_REQ_RELEASE_WORKFLOW | modified | Added step 10 Cleanup Branches; renumbered Publish to step 11 |

### New Design Elements

_(none — existing SPECs cover the scope after modification)_

### Conflicts Detected

_(none)_

### Decisions

- Decision 1: SYSP_SPEC_CM_DUTIES and SYSP_SPEC_CM_WORKFLOW promoted from `draft` to `approved`
- Decision 2: Release workflow Cleanup step placed after Back-Merge (step 10) to ensure branches are only cleaned after full synchronization

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_PM | SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW | SYSP_SPEC_PM_DUTIES, SYSP_SPEC_PM_WORKFLOW | ✅ |
| SYSP_US_CM | SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_WORKFLOW | SYSP_SPEC_CM_DUTIES, SYSP_SPEC_CM_WORKFLOW | ✅ |
| SYSP_US_RELEASE | SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW | SYSP_SPEC_RELEASE_DUTIES, SYSP_SPEC_RELEASE_WORKFLOW | ✅ |

### Artefakt-Removal-Check

_Not applicable — this CR does not remove any artefact. The "Authoring Mode" field was removed from the template in a prior commit but is not a spec-level artefact._

### Issues Found

- [x] Product-side agents (`syspilot/agents/`) are not yet updated to match `.github/` end-state — this is implementation work for the Dev Engineer (not spec scope)
- [x] `SYSP_REQ_INSTALLER_SCOPE` maps `syspilot/templates/` → `.syspilot/templates/` but the new template location is `.github/templates/` — deferred to a follow-up CR for Setup-Agent sync

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
