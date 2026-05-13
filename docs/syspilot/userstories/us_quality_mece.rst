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
   Die MECE-Engine ist verantwortlich für:

   * die vollständige Abdeckung der Items des geprüften Levels — kein Item bleibt ungeprüft
   * die Sichtbarkeit von Überlappungen — gefundene Überlappungen werden mit Details ausgewiesen, nicht implizit gelassen
   * die Sichtbarkeit von Lücken — fehlende Coverage wird benannt, nicht stillschweigend übergangen
   * die strikte Level-Begrenzung — ein Lauf prüft genau ein Level, vermischt L0/L1/L2 nicht

   **Workflow (high-level):**
   Receive level → Read all items → Analyze (overlaps, gaps, contradictions) → Report findings.

   **Acceptance Criteria:**

   1. Given a specification level, When MECE completes its run, Then every item at that level has been checked — no item remains unexamined
   2. Given overlapping items exist, When MECE detects them, Then the overlap is reported with specific details — no overlap remains implicit
   3. Given a gap in coverage exists, When MECE detects it, Then the missing coverage is explicitly named — no gap is silently passed over
   4. Given a MECE run, When it executes, Then it checks exactly one level (L0, L1, or L2) — levels are never mixed in a single run
