# Change Document: impl-ac-check

**Status**: approved
**Branch**: feature/impl-ac-check
**Created**: 2026-03-16
**Author**: Change Agent
**GitHub Issue**: #4

---

## Summary

The Implement Agent's workflow goes directly from Code → Quality Gates → Commit, without a systematic step to verify that every requirement acceptance criterion (AC) from the Change Document has been addressed in code. This causes implementation gaps only caught later by the Verify Agent — resulting in extra fix-and-reverify cycles.

**Proposed fix**: Add an "Implementation Completeness Check" step between Code and Quality Gates, where the agent systematically walks through every REQ AC and SPEC from the Change Document before proceeding.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_CHG_IMPLEMENT | Implement with Full Traceability | modified | Add acceptance scenario for self-verification of AC completeness |

### New User Stories

_None needed — the change fits naturally into the existing US._

### Proposed Changes

#### US_CHG_IMPLEMENT: Add Acceptance Scenario 4

Current ACs focus on traceability (code references SPEC IDs, tests reference REQ IDs, docs updated first). Missing: the agent should **self-verify completeness** against all ACs before moving to quality gates.

**New Acceptance Scenario:**

```rst
   4. Given code is written, When the agent checks completeness, Then every
      acceptance criterion from the Change Document has corresponding code
```

### Horizontal Check (MECE)

- ✅ No contradiction with US_CHG_VERIFY — that is *external* verification by the Verify Agent; this is *self-verification* by the Implement Agent
- ✅ No redundancy — US_CHG_VERIFY checks after implementation is committed; this check happens *before* quality gates
- ✅ No overlap with US_WF_CHANGE — workflow sequence remains unchanged, just an internal step added

### Decisions

- Decision: Kein neues US nötig, Änderung passt in bestehendes US_CHG_IMPLEMENT als neues Acceptance Scenario 4

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_CHG_IMPL_AGENT | US_CHG_IMPLEMENT | modified | Add AC-7 for completeness self-check |

### New Requirements

_None needed — the change fits as a new AC on the existing requirement._

### Proposed Changes

#### REQ_CHG_IMPL_AGENT: Add AC-7 and Description Point 6

The current requirement describes reading, implementing, testing, and traceability — but not **self-verification of completeness**. The Issue shows this gap leads to the Verify Agent catching missing ACs.

**Add to Description (point 6):**

```rst
   6. Verifies implementation completeness against all acceptance criteria before quality gates
```

**New Acceptance Criterion:**

```rst
   * AC-7: Agent SHALL verify every REQ acceptance criterion and SPEC from the
     Change Document has corresponding implementation before proceeding to
     quality gates
```

### Horizontal Check (MECE)

- ✅ No contradiction with REQ_CHG_VERIFY_AGENT — Verify Agent validates *after commit*, this AC requires self-check *before quality gates*
- ✅ No redundancy with REQ_CHG_ANALYSIS_AGENT — Analysis Agent works on specs, Implement Agent works on code
- ✅ Scoped check: Only REQ_CHG_IMPL_AGENT needs change; no other REQs in req_change_mgmt.rst are affected

### Decisions

- Decision: Kein neues REQ nötig, Änderung passt als AC-7 + Description Punkt 6 in bestehendes REQ_CHG_IMPL_AGENT

---

## Level 2: Design

**Status**: 🔄 in progress

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_IMPL_QUALITY_GATES | REQ_CHG_IMPL_AGENT | modified | Insert completeness check before quality gates |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SPEC_IMPL_COMPLETENESS_CHECK | Implementation Completeness Check | REQ_CHG_IMPL_AGENT |

### Proposed Changes

#### NEW: SPEC_IMPL_COMPLETENESS_CHECK

New Design Spec that describes the completeness self-check procedure. This is the core of Issue #4.

```rst
.. spec:: Implementation Completeness Check
   :id: SPEC_IMPL_COMPLETENESS_CHECK
   :status: draft
   :links: REQ_CHG_IMPL_AGENT
   :tags: implement, completeness, validation

   **Design:**
   Before running quality gates, the Implement Agent SHALL verify that every
   requirement acceptance criterion and design spec from the Change Document
   has been addressed in the implementation.

   **Procedure:**

   1. Re-read the Change Document and list every REQ_* with its ACs
   2. For each AC, confirm there is corresponding code or configuration
   3. Check **modified** requirements — new ACs added to existing REQs are easy to miss
   4. For each SPEC_*, confirm the implementation matches the design
   5. Create a checklist (using the todo list tool) with one item per requirement

   **Checklist Format:**

   ::

      ☐ REQ_xxx_1: AC-1 ✓, AC-2 ✓, AC-3 ✓
      ☐ REQ_xxx_2: AC-1 ✓, AC-2 ✗ ← MISSING — implement before proceeding

   **Common Gaps to Watch For:**

   * Modified requirements with new ACs (not just new requirements)
   * Design specs with multiple trigger conditions or branches
   * Cross-component integration points
   * Config keys that need to be added to schemas

   **Gate Rule:** Do NOT proceed to quality gates until every AC is covered.

   **Rationale:** Without this check, the Implement Agent moves to build/commit
   after writing the main feature code — missing integration points, new ACs
   on modified requirements, and multi-condition specs. The Verify Agent then
   catches these gaps, causing extra fix-and-reverify cycles.

   **File:** ``.github/agents/syspilot.implement.agent.md``
   (section: "Implementation Completeness Check", between Code and Quality Gates)
```

#### MODIFIED: SPEC_IMPL_QUALITY_GATES

Update the Quality Gate Workflow to reference the new completeness check as a prerequisite.

Current workflow step 3 is: "If PASS → implement code with SPEC references"

**Change workflow to:**

```rst
   **Quality Gate Workflow:**

   1. **Pre-Implementation Build** — Run sphinx-build to establish baseline
   2. If FAIL → fix docs before proceeding (do not start coding)
   3. If PASS → implement code with SPEC references
   4. **Implementation Completeness Check** — Verify all ACs covered
      (see SPEC_IMPL_COMPLETENESS_CHECK)
   5. Write tests with REQ references
   6. Run tests
   7. **Post-Implementation Build** — Final sphinx-build validation
```

### Horizontal Check (MECE)

- ✅ No overlap with SPEC_IMPL_CODE_TRACEABILITY — that covers *format* of traceability comments; this covers *completeness* verification
- ✅ No overlap with SPEC_IMPL_CHANGE_DOC_INPUT — that covers *reading* the Change Document; this covers *re-reading and verifying against* it
- ✅ Clear boundary: SPEC_IMPL_COMPLETENESS_CHECK is a gate between code and quality gates
- ✅ Separate SPEC justified — distinct concern (completeness verification vs. build/test execution)

### Decisions

- Decision: Neues SPEC_IMPL_COMPLETENESS_CHECK als eigene Spec; SPEC_IMPL_QUALITY_GATES Workflow anpassen
