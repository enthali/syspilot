Implement Agent Design
======================

Design specifications for the Implement Agent — code implementation with traceability.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Pre-Implementation Environment Check
   :id: SYSPILOT_SPEC_IMPL_PRE_CHECK
   :status: implemented
   :links: SYSPILOT_REQ_INST_AUTO_SETUP, SYSPILOT_REQ_CHG_IMPL_AGENT
   :tags: implement, init, validation

   **Design:**
   The Implement Agent checks for sphinx-needs availability before starting work.

   **Check Sequence:**

   1. Run ``sphinx-build --version`` (or ``uv run sphinx-build --version``)
   2. If NOT found → inform user to run ``@syspilot.setup`` to bootstrap environment
   3. If found → proceed with implementation

   **Rationale:** Cloud environments or fresh checkouts may lack dependencies.
   Catching this early avoids mid-implementation failures.

   **File:** ``.github/agents/syspilot.implement.agent.md``
   (section: "Pre-Implementation Check")


.. spec:: Change Document Consumption
   :id: SYSPILOT_SPEC_IMPL_CHANGE_DOC_INPUT
   :status: implemented
   :links: SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_CHG_CHANGE_DOC, SYSPILOT_SPEC_CHG_CHANGE_DOCUMENT
   :tags: implement, input, change-document

   **Design:**
   The Implement Agent reads the Change Document to determine implementation scope
   and then queries linked specs for detailed instructions.

   **Input Resolution:**

   The Change Document can come from:

   * A markdown file in ``docs/changes/<name>.md``
   * A GitHub Issue assigned to the implement agent
   * Direct handoff from the Change Agent

   **Consumption Workflow:**

   1. **Read Change Document** — Extract summary, scope, and affected IDs
   2. **Query Needs** — Use ``scripts/python/get_need_links.py`` to get
      all linked SPEC_* and REQ_* items
   3. **Read SPEC Files** — Understand implementation details and constraints
   4. **Read REQ Files** — Understand expected behavior and acceptance criteria

   **Scope Constraint:** The Implement Agent works only with pre-identified scope
   from the Change Document, avoiding context overflow.

   **Boundary Rules:**

   * Do NOT modify User Stories, Requirements, or Design Specs
   * Do NOT change specification statuses (that's the Verify Agent's job)
   * Do NOT update version.json (that's the Release Agent's job)


.. spec:: Implementation Completeness Check
   :id: SYSPILOT_SPEC_IMPL_COMPLETENESS_CHECK
   :status: implemented
   :links: SYSPILOT_REQ_CHG_IMPL_AGENT
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

      ☐ req_xxx_1: AC-1 ✓, AC-2 ✓, AC-3 ✓
      ☐ req_xxx_2: AC-1 ✓, AC-2 ✗ ← MISSING — implement before proceeding

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


.. spec:: Implementation Quality Gates
   :id: SYSPILOT_SPEC_IMPL_QUALITY_GATES
   :status: implemented
   :links: SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_REL_DOC_BUILD
   :tags: implement, quality, validation

   **Design:**
   The Implement Agent runs sphinx-build as quality gate before and after coding.

   **Quality Gate Workflow:**

   1. **Pre-Implementation Build** — Run sphinx-build to establish baseline
   2. If FAIL → fix docs before proceeding (do not start coding)
   3. If PASS → implement code with SPEC references
   4. **Implementation Completeness Check** — Verify all ACs covered
      (see SYSPILOT_SPEC_IMPL_COMPLETENESS_CHECK)
   5. Write tests with REQ references
   6. Run tests
   7. **Post-Implementation Build** — Final sphinx-build validation

   **Commands:**

   ::

      # Build docs (validates all)
      sphinx-build -b html docs docs/_build/html -W --keep-going

      # Run tests
      pytest tests/ -v

   **Fail-Fast Rule:** If pre-implementation build fails, the agent fixes
   documentation issues before touching any code.


.. spec:: Code and Test Traceability
   :id: SYSPILOT_SPEC_IMPL_CODE_TRACEABILITY
   :status: implemented
   :links: SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_CORE_TRACEABILITY
   :tags: implement, traceability, code

   **Design:**
   All code and tests written by the Implement Agent include traceability
   comments linking back to Design Specs and Requirements.

   **Code Traceability Format:**

   ::

      # Implementation: spec_xxx
      # Requirements: req_xxx_1, req_xxx_2

      def my_function():
          """
          Brief description.

          Implements:
              - req_xxx_1: [What this satisfies]
              - spec_xxx: [Design reference]
          """
          pass

   **Test Traceability Format:**

   ::

      class TestFeatureName:
          """
          Tests for req_xxx_1, req_xxx_2
          """

          def test_acceptance_criteria_1(self):
              """
              Verifies: req_xxx_1 AC-1
              """
              pass

   **Commit Traceability Format:**

   ::

      feat: [Feature name]

      Implements: [Change Document name]

      Requirements:
      - req_xxx_1: [description]

      Design:
      - spec_xxx_1: [description]

   **Rationale:** Traceability comments enable the Verify Agent and Trace Agent
   to validate implementation coverage without parsing complex code logic.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SYSPILOT_SPEC_IMPL')
