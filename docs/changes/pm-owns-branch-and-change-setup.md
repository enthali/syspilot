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

This CR removes one template field: `Authoring Mode` (Change Document template, removed in commit `3000fbf`).

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `Authoring Mode` (template field) | none | none — all remaining `autonomous mode` / `user-guided mode` matches reference the **concept** (still in use), not the removed field | 1 (this CR's own narrative entry); historic CDs under `docs/changes/v0.5.2/` reference the concept, not the field |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

- [x] Product-side agents (`syspilot/agents/`) brought into sync with `.github/` end-state by Dev Engineer (commit `3dcf77b`); residual Frontmatter differences (tools/model) are intentional (source vs. installed instance).
- [ ] **Deferred to follow-up CR (Setup-Agent template sync):** `SYSP_REQ_INSTALLER_SCOPE` maps `syspilot/templates/` → `.syspilot/templates/` but the new template location is `.github/templates/` — Setup Agent needs a new sync rule for `syspilot/templates/` → `.github/templates/`.
- [ ] **Deferred to follow-up CR (Operation Mode signalling):** removing the `Authoring Mode` template field leaves no structural channel for PM to declare a CR's mode to CM — current CR-level practice is freeform text in the CR body or CM asks at intake. The justification in commit `3000fbf` ("redundant since PM sets branch context") does not address this gap.
- [x] **Scope bleed observed (informational only):** This bootstrap CR also includes commits unrelated to its stated intent — `ae65c55` (model-version fix), `0a98186` + `43b9fb8` (no-blame-language guidance), `3000fbf` (Authoring Mode removal). They are accepted as part of this CR but illustrate the very pattern the new ownership rules aim to make visible going forward.

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

## UAT Execution

**Status**: ⏳ PENDING — all rows must be executed by the human tester.

This CR is an agent-customization change. All UAT is inspection-based: the tester opens
the referenced spec files and verifies the stated text is present with the stated content.
No code execution is required except for AC6 (file existence check).

**Precondition (all rows):** Branch `feature/pm-owns-branch-and-change-setup` is checked
out. All committed changes from the Design subagent (commit `3720837`) are present.

| UAT-ID | AC | Inspection Step | Expected | Status |
|--------|----|-----------------|----------|--------|
| UAT_001 | AC1 | Open `docs/syspilot/design/spec_project_mgr.rst`. Find `:id: SYSP_SPEC_PM_DUTIES`. Locate the **Change Initialization** duty bullet. | Bullet states: PM copies `.github/templates/change-document.md` verbatim to `docs/changes/<name>.md` and fills only header fields (`Status`, `Branch`, `Created`, `Author`) and the `## Summary` section — all other template sections remain untouched for CM. | PENDING |
| UAT_002 | AC1 | In the same file, find `:id: SYSP_SPEC_PM_WORKFLOW`. Locate step **8 — Create Change Document**. Verify the exact PowerShell command is present. | Step 8 contains exactly: `Copy-Item .github/templates/change-document.md docs/changes/<name>.md` and explicitly lists only header fields + `## Summary` as PM-fillable; all other sections are marked CM territory. | PENDING |
| UAT_003 | AC2 | Open `docs/syspilot/design/spec_change_mgr.rst`. Find `:id: SYSP_SPEC_CM_DUTIES`. Locate the **Change Auditability** duty bullet. | Bullet states: PM creates the document by copying `.github/templates/change-document.md` verbatim and filling header + `## Summary`; CM fills all engineering sections in-place — CM never creates the document and never replaces the template skeleton with hand-written structure. | PENDING |
| UAT_004 | AC2 | In the same file, find `:id: SYSP_SPEC_CM_WORKFLOW`. Read step **1 — Receive + Intent Gate**. | Step 1 states: PM provides the branch name and Change Document path; CM checks out the provided branch — no branch creation and no Change Document creation by CM. | PENDING |
| UAT_005 | AC3 | In `docs/syspilot/design/spec_change_mgr.rst`, find `:id: SYSP_SPEC_CM_DUTIES`. Locate the **Merge Abstinence** duty bullet. | Bullet states: CM never merges to `development`. CM signals readiness to PM; PM performs the merge. CM's workflow ends when PM decides. | PENDING |
| UAT_006 | AC3 | In the same file, find `:id: SYSP_SPEC_CM_WORKFLOW`. Read step **9 — Await PM Decision**. | Step 9 contains the phrase "CM never merges" and maps PM decisions to CM actions — no merge command is issued by CM at any point in the described workflow. | PENDING |
| UAT_007 | AC4 | Open `docs/syspilot/design/spec_project_mgr.rst`. Find `:id: SYSP_SPEC_PM_WORKFLOW`. Locate the **QM Findings Review Workflow** sub-section, step **4 — Merge or Hold**. | Step 4 contains: "Feature branch is NOT deleted after merge — retained for forensics until the Release Agent cleans up at release time." | PENDING |
| UAT_008 | AC5 | Open `docs/syspilot/design/spec_release_engineer.rst`. Find `:id: SYSP_SPEC_RELEASE_DUTIES`. Locate the **Feature Branch Cleanup** duty bullet. | Bullet states: After every release, all `feature/*` branches merged into `development` are deleted locally and on remote; branches are retained for forensic/bisect purposes only until release time. | PENDING |
| UAT_009 | AC5 | In the same file, find `:id: SYSP_SPEC_RELEASE_WORKFLOW`. Locate step **10 — Cleanup Branches**. Verify the PowerShell cleanup command is present. | Step 10 contains: `git branch --merged development \| Where-Object { $_ -match 'feature/' } \| ForEach-Object { git branch -d $_.Trim(); git push origin --delete $_.Trim() }` and explicitly states that feature branches are cleaned up here at release time. | PENDING |
| UAT_010 | AC6 | Run in repo root: `Test-Path .github/templates/change-document.md` | Returns `True` — the file exists. | PENDING |
| UAT_011 | AC6 | Run: `Get-Content .github/templates/change-document.md \| Select-Object -First 10` | Output shows a template skeleton with `# Change Document: {NAME}`, status/branch/created/author header fields, a `## Summary` placeholder, and section stubs for L0/L1/L2 — confirming this is the installed-instance template copy, not a filled-out change document. | PENDING |

### AC Coverage

| AC | Description (abbreviated) | UAT-IDs |
|----|---------------------------|---------|
| AC1 | PM describes `Copy-Item` + exact fields filled | UAT_001, UAT_002 |
| AC2 | CM receives branch+CD from PM, never creates/replaces | UAT_003, UAT_004 |
| AC3 | CM never merges — PM performs integration | UAT_005, UAT_006 |
| AC4 | Feature branches not deleted after merge | UAT_007 |
| AC5 | Release Agent describes cleanup step | UAT_008, UAT_009 |
| AC6 | `.github/templates/change-document.md` exists | UAT_010, UAT_011 |

---

*Generated by syspilot Change Agent*
