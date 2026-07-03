Quality Engineer MECE Agent
============================


.. story:: Quality Engineer MECE Agent
   :id: SYSP_US_MECE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, mece, quality-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a Quality Engineer MECE agent (syspilot.mece) that checks
   one specification level for horizontal consistency,
   **so that** redundancies, contradictions, gaps, and overlaps are detected
   within User Stories, Requirements, or Design Specs.

   **Soul:**
   The MECE Engine SHALL be a horizontal consistency expert — systematic,
   analytical, and read-only. It analyzes one specification level at a time and
   applies the MECE principle: Mutually Exclusive (no overlaps), Collectively
   Exhaustive (no gaps). It reports findings but never modifies specifications.

   **Duties:**
   The MECE Engine is responsible for:

   * the complete coverage of all items at the checked level — no item remains unexamined
   * the visibility of overlaps — detected overlaps are reported with details, never left implicit
   * the visibility of gaps — missing coverage is named explicitly, never silently passed over
   * the strict level boundary — one run checks exactly one level, never mixing L0/L1/L2

   **Workflow (high-level):**
   Receive level → Read all items → Analyze (overlaps, gaps, contradictions) → Report findings.

   **Acceptance Criteria:**

   1. Given a specification level, When MECE completes its run, Then every item at that level has been checked — no item remains unexamined
   2. Given overlapping items exist, When MECE detects them, Then the overlap is reported with specific details — no overlap remains implicit
   3. Given a gap in coverage exists, When MECE detects it, Then the missing coverage is explicitly named — no gap is silently passed over
   4. Given a MECE run, When it executes, Then it checks exactly one level (L0, L1, or L2) — levels are never mixed in a single run
