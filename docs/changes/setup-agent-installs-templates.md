# Change Document: setup-agent-installs-templates

**Status**: in-progress
**Branch**: feature/setup-agent-installs-templates
**Created**: 2026-05-21
**Author**: PM

---

## Summary

Setup Agent must sync `syspilot/templates/*` → `.github/templates/*` during instance install and update, analogous to how it already handles `syspilot/agents/`, `syspilot/prompts/`, and `syspilot/skills/`. Today `.github/templates/change-document.md` exists only because CR `pm-owns-branch-and-change-setup` placed it manually as a one-off; this CR makes Setup Agent the single source of truth for that sync so the file (and any future template) is reproducibly present in every installed instance, including customer projects that have no `syspilot/` folder. Motivation: without sync logic, the product source (`syspilot/templates/`) and the installed-instance copy (`.github/templates/`) will drift silently, and customer projects — which only contain `.github/` — will break PM/CM agent references that point to `.github/templates/change-document.md`. Acceptance: (1) Setup Agent specification (`syspilot/agents/syspilot.setup.agent.md` and corresponding design spec) describes the template sync responsibility on install and update; (2) Setup Agent copies every file under `syspilot/templates/` to `.github/templates/` on install and update, and is idempotent (re-running yields the same end-state); (3) Setup Agent removes orphan files in `.github/templates/` that no longer exist in `syspilot/templates/`, so no stale templates accumulate; (4) the sync action is observable in Setup Agent's run summary (installed / updated / removed counts, so PM can verify).

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
