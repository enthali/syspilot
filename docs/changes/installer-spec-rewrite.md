# Change Document: installer-spec-rewrite

**Status**: in-progress
**Branch**: feature/installer-spec-rewrite
**Created**: 2026-05-23
**Author**: PM

---

## Summary

Rewrite the Installer spec and agent so the **customer installation path** is the documented and validated one. Today's spec was written from inside the dogfooding workspace and describes a workflow that only works there: Step 1 offers a local-source shortcut that bypasses GitHub fetch, Step 2 compares against an already-overwritten Bootloader file, Step 4 asks an after-the-fact customization question and contains a broken double-write flow, and the spec is silent on UTF-8 encoding, wrapper-script discipline, and rollback. A live install attempt on 2026-05-23 confirmed the impact: the Installer agent shortcuts to a local copy, writes 26 files with UTF-8 BOM corruption, and generates a wrapper script that bypasses its own workflow. This CR fixes the spec so customers get a correct, transactional, customer-path-validated install. It is **release-blocking for v0.6.1** because v0.6.1 will be pulled by customers through whichever Installer ships with it — if that Installer is broken, the release breaks customer installations on first contact. **Motivation**: complete and trustworthy install for every customer, on every supported platform, every time. **Acceptance criteria**: (AC1) Installer always fetches from upstream GitHub — no local-source path in spec or agent. (AC2) Mode-Detect step (former Step 2) is removed; Installer always installs latest. (AC3) All written files are UTF-8 without BOM. (AC4) Installer performs file operations directly per file (Invoke-WebRequest + Out-File or equivalent) — no generation of wrapper scripts, no helper files in temp/. (AC5) Frontmatter preservation rule explicit: `tools:` is preserved per file; all other fields (`description`, `model`, `user-invocable`, `agents`, etc.) come from upstream; Bootloader (`syspilot.setup.agent.md`) is overwritten verbatim with no preservation. (AC6) Step 3 dependency check: if `sphinx-needs` is missing, print install instructions and stop — do not auto-install. (AC7) Git-based rollback: pre-install commit is created before file operations; on failure between install and final commit, `git reset --hard` restores the pre-install state. (AC8) Customization-question and double-write flow removed from Step 4 entirely. (AC9) Customer-path live validation: clean test repo, no local `syspilot/`, `@syspilot.setup` invoked with `development` branch override succeeds end-to-end and produces the per-directory summary table with `templates/` row.

Full design decisions, finding-by-finding rationale, and validation strategy are documented in `.jarvis/sessions/Project Manager/idea-installer-spec-rewrite.md` (PM session artefact, not a syspilot product spec). CM should treat that idea file as the authoritative source of decisions — every Workflow step rewrite, every removed step, and every new Soul/Duty entry traces back to a PM-confirmed decision recorded there.

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
