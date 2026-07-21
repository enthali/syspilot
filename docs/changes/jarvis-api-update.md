# Change Document: jarvis-api-update

**Status**: in-progress
**Branch**: feature/jarvis-api-update
**Created**: 2026-07-21
**Author**: Project Manager
**Operation Mode**: autonomous

---

## Summary

Patch to keep syspilot in sync with breaking API changes in Jarvis. Three
independent fixes, all triggered by Jarvis renaming and restructuring its
tool API:

1. **Tool name updates** — Jarvis renamed `sendToSession` → `sendMessage`,
   `readMessage` → `receiveMessage`. All references in syspilot agent specs,
   skills, and documentation must be updated to the new names. Affected: Setup
   Bootloader `tools:` frontmatter, `syspilot.orchestration-jarvis` skill
   (already partially updated), and prose in conventions.md and UAT specs.

2. **Setup Bootloader `tools:` frontmatter** — Replace the long explicit
   per-tool allowlist with the compact group-based notation:
   `[vscode, execute, read, edit, search, web, browser, agent, todo,
   enthali.jarvis-core, enthali.jarvis-syspilot]`. This also ensures Jarvis
   tools are available to sessions started from the Setup Bootloader.

3. **Installer Step 9 — actor creation** — Jarvis now uses `actor.yaml` /
   `.jarvis/actors/<name>/` (previously `session.yaml` / `.jarvis/sessions/<name>/`).
   The installer currently scaffolds session files directly on disk; it must
   switch to calling `jarvis_createActor`. Idempotency logic:
   - `.jarvis/actors/<name>/` exists → skip (`jarvis_createActor` is idempotent
     but explicit skip is cleaner)
   - `.jarvis/sessions/<name>/` exists → skip + warn user (legacy format
     detected; syspilot will not create a duplicate; manual Jarvis migration
     may be needed if Jarvis no longer reads sessions/)
   - Neither exists → call `jarvis_createActor(name, ...)`

**Acceptance criteria:**
- AC-1: All `sendToSession`/`readMessage` references replaced by
  `sendMessage`/`receiveMessage` repo-wide (active code and docs; historical
  Change Documents accepted as stranded).
- AC-2: Setup Bootloader `tools:` uses group notation; `enthali.jarvis-core`
  and `enthali.jarvis-syspilot` groups present.
- AC-3: Installer Step 9 uses `jarvis_createActor` with the three-way
  idempotency check; no file-scaffolding of session.yaml.
- AC-4: `sphinx-build -W` clean.

**GitHub Issue:** #58

---

## Level 0: User Stories

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

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

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

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

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

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

**Status**: ⏳ not started | ✅ passed | ❌ failed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_xxx | REQ_xxx | SPEC_xxx | ✅ |
...

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
