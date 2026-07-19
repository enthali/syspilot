# Change Document: releasenotes-ownership

**Status**: ready-for-merge
**Branch**: feature/releasenotes-ownership
**Created**: 2026-07-19
**Author**: Project Manager (triage), Change Manager (engineering)
**Operation Mode**: autonomous

---

## Summary

Release Notes are a version-bound artifact whose version string does not exist
until release time (decided by the Release Engineer per the versioning scheme).
Today two agents write `docs/releasenotes.md`: the Documentation Engineer during
the change pipeline (CM Step 7 → SEND to Doc Engineer) AND the Release Engineer
at release time (Step 6, generated from the archived Change Documents in
`docs/changes/<version>/`). This dual ownership forces the Doc Engineer to guess
a version number mid-change-run (e.g. `## v0.21.0 — unreleased`), producing wrong
entries that must be manually corrected to the actual patch version before every
merge. This CR applies strict separation (Issue #50, variant A): remove Release
Notes from the change-run Documentation Engineer scope, making the Release
Engineer the sole writer of `docs/releasenotes.md`. The Documentation Engineer
then handles only non-version-bound docs during a change (README, methodology,
architecture, conventions, context.md, copilot-instructions.md). The
release-notes artifact and its structure (`SYSP_US_DOC_RELEASE_NOTES` → REQ →
SPEC) remain unchanged — only the ownership/timing is made unambiguous.

**Root cause:** spec-level contradiction. `SYSP_SPEC_DOC_RELEASENOTES` already
states content is added by the Release Engineer per release, yet the
Documentation Engineer duties/workflow (`syspilot.docu.agent.md` Duty #6 and
Workflow Step 5, mirrored in `spec_docu_engineer.rst`, `req_docu_engineer.rst`,
`us_docu_engineer.rst`) still include Release Notes in scope.

**Acceptance (from Issue #50):**
- No versioned release-notes entry is written during a change pipeline.
- Release Engineer is the sole writer of `docs/releasenotes.md`.
- No manual version-number correction needed before merge.

**GitHub Issue:** #50

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_DOCU | Documentation Engineer | modified | Removed "release notes" from External docs bullet in Context |

### New User Stories

None.

### Decisions

- No new US needed — existing US SYSP_US_DOCU and SYSP_US_RELEASE cover the ownership split.
- SYSP_US_DOC_RELEASE_NOTES (artifact US) stays unchanged — it defines the artifact, not who writes it.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_DOCU_DUTIES | SYSP_US_DOCU | modified | Removed "release notes" from external doc list and AC-4 |
| SYSP_REQ_DOC_RELEASENOTES | SYSP_US_DOC_RELEASE_NOTES | modified | Added explicit sole-ownership statement for Release Engineer |

### New Requirements

None.

### Conflicts Detected

None — this CR resolves the pre-existing contradiction.

### Decisions

- SYSP_REQ_DOC_RELEASENOTES now explicitly states Release Engineer sole ownership and excludes Doc Engineer during change pipeline runs.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_DOCU_DUTIES | SYSP_REQ_DOCU_DUTIES | modified | Removed Duty #6 "Release Notes"; renumbered Architecture to #6 |
| SYSP_SPEC_DOCU_WORKFLOW | SYSP_REQ_DOCU_WORKFLOW | modified | Removed "release notes" from Step 5 "Update External Docs" |
| SYSP_SPEC_DOC_RELEASENOTES | SYSP_REQ_DOC_RELEASENOTES | modified | Added sole-writer statement in Status Notes |
| SYSP_SPEC_RELEASE_DUTIES | SYSP_REQ_RELEASE_DUTIES | modified | Added "sole writer of docs/releasenotes.md" to Complete Traceability duty |

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- Release Engineer's "Complete Traceability" duty now explicitly states sole writer status.
- Doc Engineer Duty #7 "Architecture" renumbered to #6 after Release Notes duty removal.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_DOCU | SYSP_REQ_DOCU_DUTIES | SYSP_SPEC_DOCU_DUTIES, SYSP_SPEC_DOCU_WORKFLOW | ✅ |
| SYSP_US_DOC_RELEASE_NOTES | SYSP_REQ_DOC_RELEASENOTES | SYSP_SPEC_DOC_RELEASENOTES | ✅ |
| SYSP_US_RELEASE | SYSP_REQ_RELEASE_DUTIES | SYSP_SPEC_RELEASE_DUTIES | ✅ |

### Artefakt-Removal-Check

Removed "release notes" from Doc Engineer scope (us/req/spec).

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| "release notes" in Doc Engineer scope | Fixed: us_docu_engineer.rst, req_docu_engineer.rst, spec_docu_engineer.rst, syspilot/agents/syspilot.docu.agent.md | none remaining | acceptable — earlier CDs may reference Doc Engineer + release notes historically |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

None. MECE and Trace checks both clean on first review round.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge
- [x] Documentation Engineer: no external doc changes required (workflows.md already correctly attributed release notes to Release Engineer)

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-19

#### Findings

None. Doc Engineer duty set MECE post-removal (6 duties, no gaps). Sole ownership unambiguous at L0/L1/L2. No contradictions. No active class (a)/(b) references remaining.

---

---

*Generated by syspilot Change Agent*

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
