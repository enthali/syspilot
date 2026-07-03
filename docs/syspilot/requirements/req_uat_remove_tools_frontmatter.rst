Remove-Tools-Frontmatter Test Data
==================================

Test data requirements for ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER``.


.. req:: UAT Test Data: Remove Tools Frontmatter
   :id: SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: uat, agent-arch, tools, remove-tools-frontmatter, test-data
   :links: SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER``, the
   following artifacts, fixtures, and reference data SHALL be available to
   the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - All 14 product agent files
        - ``syspilot/agents/``
        - AC-1 (13 non-Setup), AC-2 (Setup)
      * - ``req_agent_arch.rst``
        - ``docs/syspilot/requirements/``
        - ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-3, AC-10 (AC-1, AC-2, AC-4)
      * - External documentation files
        - ``README.md``, ``docs/architecture.md``, ``docs/workflows.md``
          (or wherever the Documentation Engineer places the guidance)
        - AC-5 (``enthali.jarvis-core`` presence check)

   **Target-Project Fixture:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-STALE-TOOLS``
        - Target project with a completed prior syspilot installation;
          ``.github/agents/syspilot.cm.agent.md`` (or any non-Setup agent
          file) still carries a ``tools:`` frontmatter field from before
          this CR
        - AC-3 (live update removes stale field)

   **Expected agent file count:** 14 files matching
   ``syspilot/agents/syspilot.*.agent.md`` — 13 without ``tools:``, 1
   (``syspilot.setup.agent.md``) with an explicit ``tools:`` list.

   **Tooling:**

   * A text search tool capable of scanning YAML frontmatter blocks across
     multiple files (VS Code Search, ``grep``, PowerShell
     ``Select-String``) — used for AC-1, AC-2
   * VS Code with Copilot, target project open, ``@syspilot.setup``
     accessible from the Chat panel — used for AC-3
   * Read access to ``docs/syspilot/requirements/req_agent_arch.rst`` — AC-4
   * Read access to the external documentation files listed above — AC-5

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/remove-tools-frontmatter`` is checked out in the
     syspilot workspace.
   * AC-2: The tester has read access to all 14 files under
     ``syspilot/agents/``.
   * AC-3: For the live-update scenario — fixture ``F-STALE-TOOLS`` is
     prepared on a separate target project before the scenario is run.
   * AC-4: The tester acknowledges the documentation-verification scope
     limit before running AC-4 of the story (no live VS Code tool-picker
     assertion is attempted by syspilot's own harness).
