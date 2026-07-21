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

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB | UAT: Skill Orchestration Vocabulary | text update | Updated tool names in AC example list |

### New User Stories

None.

### Decisions

- No new US needed — this is a patch syncing existing specs with API renames.
- US impact is cosmetic (example tool names in AC text).

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] No gaps

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB | UAT: Orchestration Vocab | text update | Updated tool names in prohibited-pattern list |
| SYSP_REQ_INSTALLER_SESSION_SCAFFOLD | Installer Actor Creation | rewritten | Renamed from "Session Scaffold"; three-way idempotency with jarvis_createActor |

### New Requirements

None.

### Decisions

- SYSP_REQ_INSTALLER_SESSION_SCAFFOLD retains its ID for traceability continuity but is rewritten to describe actor creation via `jarvis_createActor` with three-way idempotency.
- AC count increased from 5 to 6 (new AC-4 for legacy session warning, AC-5 for create call).

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All REQs still link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_SPEC_SKILL_DEFINITIONS_TABLE | Skill Definitions Table | text update | `jarvis_sendToSession` → `jarvis_sendMessage` |
| SYSP_SPEC_UAT_SKILL_ORCHESTRATION_VOCAB | UAT: Orchestration Vocab Test | text update | Tool names in expected results |
| SYSP_SPEC_UAT_PRODUCT_OWNS_TOOL_LISTS | UAT: Product Owns Tool Lists | text update | Tool names in expected results |
| SYSP_SPEC_SETUP_FRONTMATTER | Setup Manager Frontmatter | modified | tools: list → group notation with enthali.jarvis-core/syspilot |
| SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD | Installer Actor Creation | rewritten | session.yaml scaffolding → jarvis_createActor with three-way idempotency |
| SYSP_SPEC_INSTALLER_WORKFLOW (Step 9) | Installer Workflow | text update | "Session Scaffolds" → "Actor Creation" |

### New Design Elements

None.

### Decisions

- SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD title changed to "Installer Actor Creation" but ID preserved.
- Setup Bootloader tools: switched from per-tool allowlist to group notation (`enthali.jarvis-core`, `enthali.jarvis-syspilot`).
- SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB already had correct names (previously updated) — no change needed.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All SPECs still link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB | SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB | SYSP_SPEC_UAT_SKILL_ORCHESTRATION_VOCAB | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_SESSION_SCAFFOLD | SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD | ✅ |
| SYSP_US_SETUP | (via SYSP_REQ_SETUP_FRONTMATTER) | SYSP_SPEC_SETUP_FRONTMATTER | ✅ |

### Artefakt-Removal-Check

Renamed tool APIs (`jarvis_sendToSession`, `jarvis_readMessage`) — grep in `docs/syspilot/`:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `jarvis_sendToSession` | none (0 hits in docs/syspilot/) | none | acceptable (historic CDs) |
| `jarvis_readMessage` | none (0 hits in docs/syspilot/) | none | acceptable (historic CDs) |
| `session.yaml` scaffolding | spec rewritten | spec rewritten | acceptable (historic CDs) |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding"

### Issues Found

None.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Artefakt-removal verified
- [x] Ready for implementation

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
