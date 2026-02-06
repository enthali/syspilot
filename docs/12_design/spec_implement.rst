Implement Agent Design
======================

Design specifications for the Implement Agent — code implementation with traceability.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Pre-Implementation Environment Check
   :id: SPEC_IMPL_PRE_CHECK
   :status: implemented
   :links: REQ_INST_AUTO_SETUP, REQ_CHG_IMPL_AGENT
   :tags: implement, init, validation

   **Design:**
   The Implement Agent checks for sphinx-needs availability before starting work.

   **Check Sequence:**

   1. Run ``sphinx-build --version`` (or ``uv run sphinx-build --version``)
   2. If NOT found → run init script to bootstrap environment
   3. If found → proceed with implementation

   **Rationale:** Cloud environments or fresh checkouts may lack dependencies.
   Catching this early avoids mid-implementation failures.

   **File:** ``.github/agents/syspilot.implement.agent.md``
   (section: "Pre-Implementation Check")


.. spec:: Change Document Consumption
   :id: SPEC_IMPL_CHANGE_DOC_INPUT
   :status: implemented
   :links: REQ_CHG_IMPL_AGENT, REQ_CHG_CHANGE_DOC
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


.. spec:: Implementation Quality Gates
   :id: SPEC_IMPL_QUALITY_GATES
   :status: implemented
   :links: REQ_CHG_IMPL_AGENT
   :tags: implement, quality, validation

   **Design:**
   The Implement Agent runs sphinx-build as quality gate before and after coding.

   **Quality Gate Workflow:**

   1. **Pre-Implementation Build** — Run sphinx-build to establish baseline
   2. If FAIL → fix docs before proceeding (do not start coding)
   3. If PASS → implement code with SPEC references
   4. Write tests with REQ references
   5. Run tests
   6. **Post-Implementation Build** — Final sphinx-build validation

   **Commands:**

   ::

      # Build docs (validates all)
      sphinx-build -b html docs docs/_build/html -W --keep-going

      # Run tests
      pytest tests/ -v

   **Fail-Fast Rule:** If pre-implementation build fails, the agent fixes
   documentation issues before touching any code.


.. spec:: Code and Test Traceability
   :id: SPEC_IMPL_CODE_TRACEABILITY
   :status: implemented
   :links: REQ_CHG_IMPL_AGENT, REQ_CORE_TRACEABILITY
   :tags: implement, traceability, code

   **Design:**
   All code and tests written by the Implement Agent include traceability
   comments linking back to Design Specs and Requirements.

   **Code Traceability Format:**

   ::

      # Implementation: SPEC_xxx
      # Requirements: REQ_xxx_1, REQ_xxx_2

      def my_function():
          """
          Brief description.

          Implements:
              - REQ_xxx_1: [What this satisfies]
              - SPEC_xxx: [Design reference]
          """
          pass

   **Test Traceability Format:**

   ::

      class TestFeatureName:
          """
          Tests for REQ_xxx_1, REQ_xxx_2
          """

          def test_acceptance_criteria_1(self):
              """
              Verifies: REQ_xxx_1 AC-1
              """
              pass

   **Commit Traceability Format:**

   ::

      feat: [Feature name]

      Implements: [Change Document name]

      Requirements:
      - REQ_xxx_1: [description]

      Design:
      - SPEC_xxx_1: [description]

   **Rationale:** Traceability comments enable the Verify Agent and Trace Agent
   to validate implementation coverage without parsing complex code logic.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_IMPL')
