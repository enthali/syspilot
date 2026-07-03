Branching Naming Fix Test Data
==============================

Test data requirements for ``SYSP_US_UAT_BRANCHING_NAMING_FIX``.


.. req:: UAT Test Data: Branching Naming Fix & Trace Cross-Reference Re-verification
   :id: SYSP_REQ_UAT_BRANCHING_NAMING_FIX
   :status: draft
   :priority: mandatory
   :tags: uat, skill-branching, trace, naming, regression, test-data
   :links: SYSP_US_UAT_BRANCHING_NAMING_FIX

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_BRANCHING_NAMING_FIX``, the
   following artifacts, fixtures, and reference data SHALL be available to
   the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``req_skill_branching.rst``
        - ``docs/syspilot/requirements/``
        - ``SYSP_REQ_SKILL_BRANCHING_NAMING`` (AC-1)
      * - ``syspilot.branching/SKILL.md``
        - ``.github/skills/`` (deployed instance)
        - Naming table (AC-2)
      * - ``spec_skill_branching.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` (AC-3, AC-4)
      * - ``req_quality_trace.rst`` / ``spec_quality_trace.rst``
        - ``docs/syspilot/requirements/`` /
          ``docs/syspilot/design/``
        - ``SYSP_REQ_TRACE_DUTIES``, ``SYSP_SPEC_TRACE_DUTIES`` (AC-3)

   **Regression Fixture (historical, not synthesized):**

   .. list-table:: Fixture
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - State
        - Used By Scenario
      * - ``F-INCIDENT-COMMIT``
        - Git commit ``96347f3`` checked out (read-only checkout, e.g.
          ``git show`` or a detached-HEAD worktree — no commits are made
          against it). At this commit,
          ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` already states the
          Installer creates no dedicated branch, while
          ``SYSP_REQ_SKILL_BRANCHING_NAMING`` still attributes
          ``update/v{version}`` creation to ``@syspilot.setup`` — the
          actual, historically real contradiction, not a constructed one
        - AC-3 (regression scenario), AC-4 (cross-reference confirmation)

   **Reference Data:**

   * Exact strings to search for in AC-1/AC-2's negative checks:
     ``update/v{version}``, ``@syspilot.setup`` (in a branch-creation
     context)
   * ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``'s ``:links:`` field value
     at commit ``96347f3`` (for AC-4's parent-vs-cross-reference
     comparison): ``SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION;
     SYSP_REQ_SKILL_BRANCHING_NAMING``

   **Tooling:**

   * A text search tool (VS Code Search, ``grep``, PowerShell
     ``Select-String``) — AC-1, AC-2
   * ``git show <commit>:<path>`` or a detached-HEAD worktree checkout of
     ``96347f3`` — AC-3, AC-4
   * ``get_need_links.py`` (``.github/skills/syspilot.impact-python/scripts/``)
     or manual ``:links:`` field inspection — AC-4
   * VS Code with Copilot, ``@syspilot.trace`` accessible from the Chat
     panel, pointed at the ``F-INCIDENT-COMMIT`` checkout — AC-3

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/branching-naming-fix`` is checked out for
     AC-1 and AC-4.
   * AC-2: The Implement stage of this CR has updated the deployed
     ``SKILL.md`` before AC-2 is run.
   * AC-3: Fixture ``F-INCIDENT-COMMIT`` is prepared (read-only checkout
     of ``96347f3``) before AC-3 is run; no changes are committed against
     this checkout — it is inspected and discarded afterward.
