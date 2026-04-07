Change Management Requirements
===============================

Requirements for the change analysis, implementation, and verification workflow.

**Last Updated**: 2026-02-06


.. req:: Change Analysis Agent
   :id: SYSPILOT_REQ_CHG_ANALYSIS_AGENT
   :status: implemented
   :priority: mandatory
   :tags: agent, change
   :links: SYSPILOT_US_CHG_ANALYZE

   **Description:**
   syspilot SHALL provide a change agent that:

   1. Analyzes user requests against current specifications AND current implementation
   2. Produces a structured Change Document with analysis and decisions
   3. Updates US/REQ/SPEC RST files directly after user approval

   **Rationale:**
   The change agent has full context during analysis and should capture this
   in the specification immediately. Separating analysis from spec-writing
   would require duplicate work and risk information loss.

   **Acceptance Criteria:**

   * AC-1: Agent reads current User Stories, Requirements, and Design docs
   * AC-2: Agent reads current implementation (code, scripts, agents) to understand what exists
   * AC-3: Agent identifies affected US, REQ, and SPEC items
   * AC-4: Agent produces Change Document with analysis, decisions, and affected IDs
   * AC-5: Agent supports ADD, MODIFY, DELETE actions
   * AC-6: Agent detects conflicting requirements and discusses resolution with user
   * AC-7: Agent ensures every REQ change traces back to a User Story
   * AC-8: Agent writes US/REQ/SPEC RST files immediately after user approval of each
     level (per-level write), not in a single atomic write at the end


.. req:: Implementation Agent with Full Traceability
   :id: SYSPILOT_REQ_CHG_IMPL_AGENT
   :status: implemented
   :priority: mandatory
   :tags: agent, implementation
   :links: SYSPILOT_US_CHG_IMPLEMENT, SYSPILOT_REQ_CORE_SPHINX_NEEDS, SYSPILOT_REQ_CORE_TRACEABILITY, SYSPILOT_REQ_CHG_CHANGE_DOC, SYSPILOT_REQ_DOC_SCOPE

   **Description:**
   syspilot SHALL provide an implement agent that:

   1. Reads the Change Document to identify affected SPECs
   2. Reads only the relevant SPEC sections as identified in the Change Document
   3. Implements code, scripts, agents, and documentation according to these SPECs
   4. Writes tests that verify the implementation
   5. Maintains traceability via comments and references
   6. Verifies implementation completeness against all acceptance criteria before quality gates

   **Rationale:**
   The Change Document provides focused context. The implement agent
   works only with the pre-identified scope, avoiding context overflow.

   **Acceptance Criteria:**

   * AC-1: Agent reads Change Document to get list of affected SPECs
   * AC-2: Agent reads only the SPECs identified in Change Document
   * AC-3: Agent runs sphinx-build to validate docs before coding
   * AC-4: Agent writes code with traceability comments (SPEC IDs)
   * AC-5: Agent writes tests referencing requirement IDs
   * AC-6: Agent runs tests and ensures they pass
   * AC-7: Agent SHALL verify every REQ acceptance criterion and SPEC from the
     Change Document has corresponding implementation before proceeding to
     quality gates


.. req:: Verification Agent
   :id: SYSPILOT_REQ_CHG_VERIFY_AGENT
   :status: implemented
   :priority: mandatory
   :tags: agent, verification
   :links: SYSPILOT_US_CHG_VERIFY, SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_CHG_CHANGE_DOC

   **Description:**
   syspilot SHALL provide a verify agent that validates implementation
   completeness against the change proposal.

   **Rationale:**
   Verification ensures no requirements are missed and traceability
   is complete.

   **Acceptance Criteria:**

   * AC-1: Agent compares implementation to change proposal
   * AC-2: Agent checks all acceptance criteria have tests
   * AC-3: Agent validates traceability (REQ → SPEC → Code → Test)
   * AC-4: Agent produces verification report with PASS/PARTIAL/FAIL
   * AC-5: Agent SHALL save the verification report to ``docs/changes/val-<name>.md``
     where ``<name>`` matches the corresponding Change Document name


.. req:: Workflow Step Suggestions
   :id: SYSPILOT_REQ_CHG_WORKFLOW_STEPS
   :status: implemented
   :priority: high
   :tags: agent, handoffs, workflow
   :links: SYSPILOT_US_WF_CHANGE, SYSPILOT_US_CHG_ANALYZE, SYSPILOT_US_CHG_IMPLEMENT, SYSPILOT_US_CHG_VERIFY, SYSPILOT_US_DOC_MAINTAIN, SYSPILOT_US_TRACE_MECE, SYSPILOT_US_TRACE_VERTICAL, SYSPILOT_REQ_CHG_ANALYSIS_AGENT, SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_CHG_VERIFY_AGENT, SYSPILOT_REQ_TRACE_MECE, SYSPILOT_REQ_TRACE_VERTICAL, SYSPILOT_REQ_WF_CHANGE_SEQUENCE

   **Description:**
   syspilot SHALL suggest appropriate next workflow steps after agent completion.

   **Rationale:**
   Users need guidance on which agent to invoke next based on the current workflow state.
   This reduces cognitive load and ensures the correct workflow is followed.

   **Acceptance Criteria:**

   * AC-1: After agent execution, VS Code displays handoff suggestions in UI
   * AC-2: Main workflow chain (change→implement→verify→memory) has directional handoffs
   * AC-3: Analysis agents (mece/trace) have bidirectional handoffs
   * AC-4: Memory agent is suggested after verify
   * AC-5: Each handoff includes a default prompt for the target agent


Iterative Change Processing
----------------------------

.. req:: Sphinx-Needs Link Discovery
   :id: SYSPILOT_REQ_CHG_LINK_DISCOVERY
   :status: implemented
   :priority: mandatory
   :tags: agent, change, links
   :links: SYSPILOT_US_CHG_ITERATIVE

   **Description:**
   The Change Agent SHALL use Sphinx-Needs links (via ``needs_id/*.json``)
   to find impacted elements at each level.

   **Rationale:**
   Automatic link discovery prevents manual searching and ensures
   all impacted elements are found.

   **Acceptance Criteria:**

   * AC-1: Script reads from ``docs/_build/html/needs_id/*.json``
   * AC-2: Script returns outgoing and incoming links for any ID
   * AC-3: Script traces impact to configurable depth
   * AC-4: Script triggers sphinx-build if needs_id is missing


.. req:: Persistent Change Document
   :id: SYSPILOT_REQ_CHG_CHANGE_DOC
   :status: implemented
   :priority: mandatory
   :tags: agent, change, document
   :links: SYSPILOT_US_CHG_ITERATIVE

   **Description:**
   The Change Agent SHALL maintain a persistent Change Document in Markdown
   that records all analysis, decisions, and changes.

   **Rationale:**
   A persistent document provides context across sessions, enables
   review, and creates audit trail.

   **Acceptance Criteria:**

   * AC-1: Change Document created at start of change process
   * AC-2: Each level's work recorded in dedicated section
   * AC-3: Decisions and conflicts documented
   * AC-4: Navigation between levels logged
   * AC-5: Change Document and validation report SHALL be moved to
     ``docs/changes/archive/`` after merge
   * AC-6: Change Document SHALL contain decision log format (ID + rationale) from
     the start; no verbose RST blocks are embedded during analysis


.. req:: Horizontal MECE Check per Level
   :id: SYSPILOT_REQ_CHG_MECE_PER_LEVEL
   :status: implemented
   :priority: high
   :tags: agent, change, mece
   :links: SYSPILOT_US_CHG_ITERATIVE, SYSPILOT_US_TRACE_MECE, SYSPILOT_REQ_TRACE_MECE

   **Description:**
   The Change Agent SHALL perform horizontal consistency check
   within each level before proceeding to the next.

   **Rationale:**
   Catching conflicts early prevents cascading issues at lower levels.

   **Acceptance Criteria:**

   * AC-1: Check for contradictions with existing items at same level
   * AC-2: Check for redundancies
   * AC-3: Report conflicts before proceeding
   * AC-4: Document resolutions
   * AC-5: Change Agent SHALL delegate the MECE check to the MECE Agent as a
     subagent invocation after writing RST for each level; results are advisory


.. req:: Bidirectional Level Navigation
   :id: SYSPILOT_REQ_CHG_BIDIR_NAV
   :status: implemented
   :priority: high
   :tags: agent, change, navigation
   :links: SYSPILOT_US_CHG_ITERATIVE

   **Description:**
   The Change Agent SHALL support navigation back to previous levels
   when issues are discovered.

   **Rationale:**
   Design feasibility issues may require requirement changes,
   which may require user story adjustments.

   **Acceptance Criteria:**

   * AC-1: User can request to go back to any previous level
   * AC-2: Previous level work preserved in Change Document
   * AC-3: New iteration marked in document
   * AC-4: Navigation logged with reason
   * AC-5: On backward navigation, agent informs user which already-written
     lower-level RSTs may be inconsistent; user decides whether to update them


.. req:: Final Consistency Check
   :id: SYSPILOT_REQ_CHG_FINAL_CHECK
   :status: implemented
   :priority: mandatory
   :tags: agent, change, verification
   :links: SYSPILOT_US_CHG_ITERATIVE, SYSPILOT_REQ_TRACE_VERTICAL

   **Description:**
   The Change Agent SHALL perform a final consistency check across all levels
   after completing analysis of the Design level, validating already-written RSTs.

   **Rationale:**
   With per-level RST writing, the final check validates that the collectively
   written RSTs are consistent and traceable — it is no longer the trigger for
   writing RST files.

   **Acceptance Criteria:**

   * AC-1: Verify all links are valid (US→REQ→SPEC)
   * AC-2: Verify no orphaned elements
   * AC-3: Verify Change Document is internally consistent
   * AC-4: Produce sign-off checklist


.. req:: Per-Level RST Writing
   :id: SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL
   :status: implemented
   :priority: mandatory
   :tags: agent, change, rst, traceability
   :links: SYSPILOT_US_CHG_ITERATIVE

   **Description:**
   The Change Agent SHALL write RST files immediately after user approval of
   each level, not in a single atomic write at the end.

   **Rationale:**
   Writing RSTs per level makes newly introduced sphinx-needs elements
   queryable via link discovery during analysis of subsequent levels. This
   enables correct subsystem constraint traversal and allows the MECE Agent
   to run as a subagent with live sphinx-needs data.

   **Acceptance Criteria:**

   * AC-1: After user approves Level 0, Change Agent writes all new/modified US
     RSTs with ``:status: draft``
   * AC-2: After user approves Level 1, Change Agent writes all new/modified REQ
     RSTs with ``:status: draft``
   * AC-3: After user approves Level 2, Change Agent writes all new/modified SPEC
     RSTs with ``:status: draft``
   * AC-4: After each level write, sphinx-build is triggered to update
     ``needs_id/`` data for link discovery
   * AC-5: After each level write, MECE Agent runs as advisory subagent; findings
     are shown to the user but do not block progress
   * AC-6: After final approval of all levels, Change Agent sets all
     ``:status: draft`` elements introduced in this change to ``:status: approved``
   * AC-7: The Change Document contains decision log format (ID + rationale)
     from the start — no verbose RST blocks


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('SYSPILOT_REQ_CHG')
