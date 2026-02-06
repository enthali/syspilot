Traceability & Quality Requirements
=====================================

Requirements for cross-cutting quality validation and traceability verification.

**Last Updated**: 2026-02-06


.. req:: MECE Requirements Review
   :id: REQ_TRACE_MECE
   :status: implemented
   :priority: high
   :tags: agent, review, mece
   :links: US_TRACE_MECE

   **Description:**
   syspilot SHALL provide a mece agent that analyzes ONE level (US, REQ, or SPEC)
   for MECE properties (Mutually Exclusive, Collectively Exhaustive).

   **Rationale:**
   Horizontal consistency within a level ensures no redundancies or contradictions.
   Focused scope prevents context overflow.

   **Acceptance Criteria:**

   * AC-1: Accept level parameter (US, REQ, SPEC)
   * AC-2: Detect redundant items (same thing said differently)
   * AC-3: Detect contradictions (conflicting items)
   * AC-4: Detect gaps (missing items for completeness)
   * AC-5: Detect overlaps (unclear boundaries)
   * AC-6: Detect missing horizontal links (item uses terms from another without :links:)
   * AC-7: Produce report with severity and recommendations


.. req:: Vertical Traceability Verification
   :id: REQ_TRACE_VERTICAL
   :status: implemented
   :priority: high
   :tags: agent, trace, vertical
   :links: US_TRACE_VERTICAL

   **Description:**
   syspilot SHALL provide a trace agent that verifies ONE user story or requirement
   is fully traced through all levels (US → REQ → SPEC → Code → Test).

   **Rationale:**
   Vertical traceability ensures complete implementation. Semantic validation
   catches links that exist but don't make sense.

   **Acceptance Criteria:**

   * AC-1: Accept starting item (US_xxx or REQ_xxx)
   * AC-2: Follow all :links: to find connected items
   * AC-3: Check link completeness (are there REQs? SPECs? Tests?)
   * AC-4: Check semantic validity (does REQ actually implement US intent?)
   * AC-5: Report coverage: FULL / PARTIAL / MISSING
   * AC-6: Identify gaps at each level


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_TRACE')
