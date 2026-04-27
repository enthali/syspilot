# Change Document: live-rst

**Status**: implemented
**Branch**: feature/live-rst-per-level
**Created**: 2026-04-07
**Issues**: #6 (subsystem constraint traversal), ideas.md — MECE als Subagent
**Author**: Georg Doll

---

## Summary

Change the Change Agent workflow from **atomic RST write at the end** to
**per-level RST write after user approval of each level**. This makes
sphinx-needs links traversable during analysis (fixing Issue #6) and
enables the MECE Agent to run as a subagent after each level write.
The Change Document becomes a lean decision log from the start, not a
verbose RST dump.

---

## Level 0: User Stories

**Status**: 🔄 in progress

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSPILOT_US_CHG_ITERATIVE` | Iterative Level-Based Change Analysis | modified | Add ACs for per-level RST write + live link traversal |

### Decisions

- D-1: No new User Story needed — the WHY ("iterative level processing with
  complete change history") doesn't change. The improvement is in HOW the
  agent achieves it. New acceptance scenarios added to existing US.
- D-2: The "live traceability during analysis" aspect is a quality improvement
  of the same user goal, not a separate user need.

### Horizontal Check (MECE)

- ✅ No contradiction with `SYSPILOT_US_CHG_ANALYZE` (that US is about getting
  a change proposal, not about when RSTs are written)
- ✅ No overlap with `SYSPILOT_US_CHG_RECOVERY` (recovery complexity is a
  Level 1/2 concern, not a separate user goal at Level 0)
- ✅ Covers the link traversal problem completely — if RSTs exist per level,
  get_need_links.py can find newly introduced elements

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSPILOT_REQ_CHG_ANALYSIS_AGENT` | Change Analysis Agent | modified | AC-8: clarify "per-level write, not atomic at end" |
| `SYSPILOT_REQ_CHG_CHANGE_DOC` | Persistent Change Document | modified | AC-6 new: no verbose RST blocks; Change Doc is decision log from start |
| `SYSPILOT_REQ_CHG_MECE_PER_LEVEL` | Horizontal MECE Check | modified | AC-5 new: Change Agent SHALL delegate MECE check to MECE Agent as subagent invocation after per-level RST write; results are advisory |
| `SYSPILOT_REQ_CHG_BIDIR_NAV` | Bidirectional Navigation | modified | AC-5 new: on backward nav, agent informs user that lower-level RSTs may be inconsistent; user decides whether to update them |
| `SYSPILOT_REQ_CHG_FINAL_CHECK` | Final Consistency Check | modified | Role change: validate already-written RSTs (not trigger for writing) |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| `SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL` | Per-Level RST Writing | `SYSPILOT_US_CHG_ITERATIVE` | mandatory |

**SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL — Per-Level RST Writing**

The Change Agent SHALL write RST files immediately after user approval of
each level, not in a single atomic write at the end.

Rationale: Writing RSTs per level makes newly introduced sphinx-needs elements
queryable via link discovery during the analysis of subsequent levels. This
enables correct subsystem constraint traversal (Issue #6) and allows the MECE
Agent to run as a subagent with live data.

Acceptance Criteria:
- AC-1: After user approves Level 0, Change Agent writes all new/modified US RSTs with `:status: draft`
- AC-2: After user approves Level 1, Change Agent writes all new/modified REQ RSTs with `:status: draft`
- AC-3: After user approves Level 2, Change Agent writes all new/modified SPEC RSTs with `:status: draft`
- AC-4: After each write, sphinx-build is triggered to update needs_id data
- AC-5: After each write, MECE Agent runs as advisory subagent; findings are shown to user but do not block progress
- AC-6: After final approval, Change Agent sets all draft elements to `:status: approved`
- AC-7: The Change Document contains decision log (ID + rationale) from start — no verbose RST blocks

### Decisions

- D-1: MECE Subagent is **advisory**, not a hard stop. User sees findings and decides if critical.
- D-2: On backward navigation, the agent **informs** the user that lower-level RSTs may be inconsistent; the user decides whether/how to update them. No automatic rollback.
- D-3: `SYSPILOT_REQ_CHG_ATOMIC_UPDATE` (the "write at end" rule) is superseded by `SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL`. The Final Consistency Check remains but changes role to validation of already-written RSTs.

### Horizontal Check (MECE)

- ✅ No contradiction between new REQ and existing ANALYSIS_AGENT (Agent analyzes; new REQ specifies write timing)
- ✅ Conflict between CHANGE_DOC "verbose RST" and new model resolved: AC-6 in CHANGE_DOC explicitly removed verbose mode
- ✅ BIDIR_NAV and LIVE_RST_PER_LEVEL are coordinated via AC-5 in BIDIR_NAV (user-decision, not auto-rollback)

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Specs

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSPILOT_SPEC_CHG_LEVEL_PROCESSING` | Iterative Level Processing | modified | Add steps 5b (Write RST) + 5c (invoke MECE Agent as subagent) to processing flow |
| `SYSPILOT_SPEC_CHG_CHANGE_DOCUMENT` | Change Document Management | modified | Remove "Content Modes" (verbose/simplified distinction); Change Doc is always decision log |
| `SYSPILOT_SPEC_CHG_ATOMIC_UPDATE` | Atomic RST Updates | deprecated | Superseded by `SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL`; set to `:status: deprecated` |
| `SYSPILOT_SPEC_CHG_BIDIR_NAVIGATION` | Bidirectional Navigation | modified | Step 4: agent informs user which already-written lower-level RSTs may be inconsistent; user decides |

### New Design Specs

| ID | Title | Links | Notes |
|----|-------|-------|-------|
| `SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL` | Per-Level RST Write & MECE Delegation | `SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL`, `SYSPILOT_REQ_CHG_MECE_PER_LEVEL` | Specifies write trigger, sphinx-build, and subagent delegation |

**SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL — Per-Level RST Write & MECE Delegation**

Design:
After the user approves a level during Change Agent analysis, the agent SHALL:

1. Write all new/modified RST elements for that level with `:status: draft`
2. Trigger `sphinx-build` to update `docs/_build/html/needs_id/` data
3. Invoke the MECE Agent as a subagent via `runSubagent("syspilot.mece", ...)`
   scoped to the level just written
4. Present MECE findings to the user as advisory (non-blocking)
5. Proceed to next level (user may review findings first)

Status lifecycle:
- Per-level write: `:status: draft`
- After final approval: Change Agent updates all touched elements to `:status: approved`
- After implementation: Verify Agent sets `:status: implemented`

Subagent invocation detail:
- Scope: the level just written (e.g. "Level 1 Requirements, affected IDs: ...")
- Result: MECE Agent returns findings or "no issues found"
- Advisory: findings shown to user, no automatic blocking or rollback

### Decisions

- D-4: `SYSPILOT_SPEC_CHG_ATOMIC_UPDATE` is set to deprecated (not deleted) to preserve
  history. It links to the new `SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL` as superseding spec.
- D-5: MECE delegation mechanism is `runSubagent("syspilot.mece", ...)` — same tool
  the Change Agent already uses. No new infrastructure needed.
- D-6: sphinx-build is required between write and MECE invocation so that needs_id/
  data is current for the MECE Agent's link queries.

### Horizontal Check (MECE)

- ✅ No overlap between new SPEC and LEVEL_PROCESSING (workflow vs mechanism)
- ✅ ATOMIC_UPDATE deprecated resolves direct contradiction with new model
- ✅ CHANGE_DOCUMENT and new SPEC complementary (content format vs write timing)
- ✅ Subagent delegation mechanism consistent with existing runSubagent usage in agents

---

## Final Consistency Check

**Status**: ✅ completed

### Traceability

- ✅ Every new/modified REQ links to a US: `SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL` → `SYSPILOT_US_CHG_ITERATIVE`
- ✅ Every new/modified SPEC links to a REQ: `SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL` → `SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL` + `SYSPILOT_REQ_CHG_MECE_PER_LEVEL`
- ✅ No orphaned elements

### Cross-Level Consistency

- ✅ US intent (live traceability + MECE feedback per level) → REQ behavior (write RST + delegate to MECE Agent) → SPEC implementation (Steps 5b/5c in level processing, subagent invocation detail)
- ✅ Advisory/non-blocking decision consistent across all levels (D-1 at Level 1, AC-5 in REQ, Design detail in SPEC)
- ✅ Backward navigation user-decision principle consistent across REQ (AC-5 BIDIR_NAV) and SPEC (BIDIR_NAVIGATION step 4)

### MECE Across Levels

- ✅ All aspects of US AC-7/AC-8 covered by REQs
- ✅ All modified/new REQs addressed by SPECs
- ✅ ATOMIC_UPDATE deprecated — no contradiction with new model remains

### Document Completeness

- ✅ No DEPRECATED markers remaining
- ✅ All decisions documented (D-1 through D-6)
- ✅ All conflicts resolved
