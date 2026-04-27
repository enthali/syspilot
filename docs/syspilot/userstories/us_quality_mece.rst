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

   **Context:**

   The MECE agent performs horizontal analysis — checking items **within** a single
   level for Mutually Exclusive, Collectively Exhaustive properties. It does not
   check vertical traceability (that's the Trace agent's job). It can be invoked
   as advisory during the change workflow or independently by the Quality Manager.

   **Acceptance Criteria:**

   1. Given a specification level, When MECE runs, Then it checks all items at that level
   2. Given overlapping items, When detected, Then MECE reports the overlap with details
   3. Given a gap in coverage, When detected, Then MECE identifies what is missing
   4. Given no issues, When all checks pass, Then MECE reports a clean result
