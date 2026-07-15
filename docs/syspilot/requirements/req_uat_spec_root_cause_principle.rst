Spec Root-Cause Principle Test Data
====================================

Test data requirements for ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``.


.. req:: UAT Test Data: Spec Root-Cause Attribution & Escalation
   :id: SYSP_REQ_UAT_SPEC_ROOT_CAUSE_PRINCIPLE
   :status: draft
   :priority: mandatory
   :tags: uat, qm, implement, root-cause, regression, test-data
   :links: SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``, the
   following artifacts, fixtures, and reference data SHALL be available to
   the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_quality_mgr.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_QM_DUTIES`` (AC-1, AC-3)
      * - ``spec_dev_engineer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_IMPLEMENT_DUTIES`` (AC-2)
      * - ``syspilot.qm.agent.md`` / ``syspilot.implement.agent.md``
        - ``syspilot/agents/``
        - Implemented agent behavior (all ACs)

   **Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - State
        - Used By Scenario
      * - ``F-CODE-DEFECT``
        - A code-level defect prepared in an installed agent or Skill
          file, where the underlying spec for that file is actually
          correct (i.e. the defect is a genuine implementation slip) —
          used to confirm QM still checks the spec layer even when the
          code turns out to be at fault
        - AC-1
      * - ``F-SPEC-DIVERGENCE``
        - A requested "fix" whose only code-level implementation would
          contradict the currently approved spec for that code (the spec
          would need to change to support the requested behavior)
        - AC-2
      * - ``F-INCIDENT-REPLAY``
        - The historical pre-fix state of ``installer-frontmatter-sync``:
          ``syspilot.installer.agent.md`` Step 4 still describes the
          retired ``tools:``-preservation logic, while
          ``SYSP_SPEC_INSTALLER_WORKFLOW`` is already correct
          (verbatim-from-upstream). Obtainable via
          ``git show <pre-fix-commit>:syspilot/agents/syspilot.installer.agent.md``
          or an equivalent read-only checkout, since this is real repo
          history, not a synthesized scenario
        - AC-3 (regression scenario)

   **Reference Data:**

   * The commit immediately preceding the ``installer-frontmatter-sync``
     fix (predecessor of commit referenced in that CR's Change Document)
     — the exact historical state for ``F-INCIDENT-REPLAY``
   * ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4 current (correct) wording, for
     comparison against the stale agent-file wording during AC-3

   **Tooling:**

   * VS Code with Copilot, ``@syspilot.qm`` and ``@syspilot.implement`` (or
     their subagent dispatch path) accessible — all scenarios
   * ``git show <commit>:<path>`` or a read-only detached checkout — AC-3
   * A text/diff comparison tool to compare agent-file wording against
     spec wording — AC-1, AC-3

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/spec-root-cause-principle`` checked out;
     fixture ``F-CODE-DEFECT`` prepared before AC-1 is run.
   * AC-2: Fixture ``F-SPEC-DIVERGENCE`` prepared before AC-2 is run.
   * AC-3: Fixture ``F-INCIDENT-REPLAY`` prepared (read-only historical
     checkout) before AC-3 is run; no commits are made against it.
