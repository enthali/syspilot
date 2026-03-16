# Change Document: val-persist

**Status**: implemented
**Branch**: feature/val-persist
**Created**: 2026-03-14
**Author**: @enthali + @syspilot.change
**GitHub Issue**: —

---

## Summary

Persist the Verify Agent's validation report as a file in `docs/changes/` alongside the Change Document. The naming convention uses `val-<name>.md` paired with the existing `<name>.md` change document.

Additionally, change the Change Document lifecycle from "delete after merge" to "archive after merge". Both change documents and validation reports are moved to `docs/changes/archive/` after merge, providing a browsable historical record without requiring git archaeology. This also cleanly separates active work from completed work for the Implement Agent.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_CHG_VERIFY | Verify Implementation Completeness | modified | Add AC-4: report saved alongside Change Document |
| US_CHG_ITERATIVE | Iterative Level-Based Change Analysis | modified | AC-6: change "deleted" to "archived" |

### New User Stories

None needed — this is a refinement of existing user stories.

### Decisions

1. Naming convention (`val-<name>.md`) is a Level 1/2 detail, not US-level
2. Apply going forward only — no retroactive persistence of past reports
3. No new US needed; modifications to US_CHG_VERIFY and US_CHG_ITERATIVE cover the stakeholder needs
4. Archive lifecycle bundled into this change (Option A) — tightly coupled with val-persist

### Proposed Changes

**US_CHG_VERIFY** — Add acceptance scenario 4:

```rst
   4. Given verification completes, When the report is generated, Then the report
      is saved alongside the Change Document for auditable review
```

**US_CHG_ITERATIVE** — Modify acceptance scenario 6:

```rst
   6. Given Change is merged, When cleanup runs, Then Change Document and validation
      report are moved to archive (browsable without Git)
```

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies (US_CHG_ITERATIVE covers archive lifecycle; US_CHG_VERIFY covers report persistence)
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_CHG_VERIFY_AGENT | US_CHG_VERIFY | modified | Add AC-5: save report to `val-<name>.md` |
| REQ_CHG_CHANGE_DOC | US_CHG_ITERATIVE | modified | AC-5: "deleted after merge" → "archived after merge" |

### New Requirements

None needed — naming convention and archive lifecycle fit as ACs on existing REQs.

### Proposed Changes

**REQ_CHG_VERIFY_AGENT** — Add AC-5:

```rst
   * AC-5: Agent SHALL save the verification report to ``docs/changes/val-<name>.md``
     where ``<name>`` matches the corresponding Change Document name
```

**REQ_CHG_CHANGE_DOC** — Modify AC-5:

```rst
   * AC-5: Change Document and validation report SHALL be moved to
     ``docs/changes/archive/`` after merge
```

### Decisions

1. Verify agent creates the file automatically (consistent with Change Agent creating Change Document)
2. Archive instead of delete — physical separation means Implement Agent only sees active docs in `docs/changes/`
3. Naming: `val-<name>.md` prefix (short, pairs with `<name>.md`, sorts adjacent)

### Horizontal Check (MECE)

- [x] No contradictions — AC-4 (produce report) and AC-5 (save to disk) are complementary
- [x] No overlap — REQ_CHG_VERIFY_AGENT owns writing; REQ_CHG_CHANGE_DOC owns lifecycle
- [x] All modified REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_VERIFY_REPORT | REQ_CHG_VERIFY_AGENT | modified | Add report persistence to `val-<name>.md` |
| SPEC_CHG_CHANGE_DOCUMENT | REQ_CHG_CHANGE_DOC | modified | Step 5: "Delete" → "Archive to `docs/changes/archive/`" |

### Unchanged (Reviewed)

| ID | Why Unchanged |
|----|---------------|
| SPEC_IMPL_CHANGE_DOC_INPUT | Reads from `docs/changes/` top-level; archive is subdirectory — no conflict |

### Proposed Changes

**SPEC_VERIFY_REPORT** — Add "Report Persistence" section:

```rst
   **Report Persistence:**

   After generating the verification report in the chat, the Verify Agent
   SHALL save it to ``docs/changes/val-<name>.md`` where ``<name>`` is
   derived from the Change Document filename.

   **Derivation Rule:**
   If the Change Document is ``docs/changes/template-first.md``, the
   validation report is ``docs/changes/val-template-first.md``.

   **Content:** The saved file is identical to the report shown in the chat.
```

**SPEC_CHG_CHANGE_DOCUMENT** — Modify lifecycle step 5:

```rst
   5. **Archive** — After merge, move Change Document and validation report
      to ``docs/changes/archive/``
```

### Decisions

1. Verify agent creates the file automatically (trivial — `create_file`)
2. Archive step is manual/agent action after merge (`mv` instead of `rm`)
3. SPEC_IMPL_CHANGE_DOC_INPUT unchanged — physical separation handles it

### Horizontal Check (MECE)

- [x] No contradictions — write (SPEC_VERIFY_REPORT) vs. lifecycle (SPEC_CHG_CHANGE_DOCUMENT) are distinct
- [x] No overlap between specs
- [x] No gaps — implement agent reads top-level only, archive in subdirectory

---

*Generated by syspilot Change Agent*
