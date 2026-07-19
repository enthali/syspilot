# Change Document: releasenotes-ownership

**Status**: draft
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

**Status**: ⏳ not started

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_abc | ... | modified | ... |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| US_xxx | As a..., I want..., so that... | mandatory |

### Decisions

- Decision 1: ...
- Decision 2: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing User Stories
- [ ] No redundancies
- [ ] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ⏳ not started

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_abc | US_abc | modified | ... |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| REQ_xxx | ... | US_xxx | mandatory |

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

**Status**: ⏳ not started

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_abc | REQ_abc | modified | ... |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SPEC_xxx | ... | REQ_abc, REQ_xxx |

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

**Status**: ⏳ not started

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_xxx | REQ_xxx | SPEC_xxx | ✅ |

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

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** {DATE}

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L? | {ID} | {description} | high / medium / low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now / defer / accept-as-is | {rationale} |

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
