Installer — Spec Rewrite Test Data
===================================

Test data requirements for ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE``.


.. req:: UAT Test Data: Installer Spec Rewrite
   :id: SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE
   :status: draft
   :priority: mandatory
   :tags: uat, installer, spec-rewrite, test-data
   :links: SYSP_US_UAT_INSTALLER_SPEC_REWRITE

   **Description:**

   To execute the nine test scenarios in ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE``,
   the following test data, tools, and preconditions SHALL be available.

   **Primary Artifacts Under Test:**

   .. list-table:: Installer Artifacts Under Test
      :header-rows: 1
      :widths: 45 25 30

      * - Artifact
        - Location
        - Relevance
      * - ``syspilot.installer.agent.md``
        - ``syspilot/agents/``
        - Rewritten Installer agent (all scenarios)
      * - ``syspilot.setup.agent.md``
        - ``syspilot/agents/``
        - Bootloader (T-1, T-2)
      * - ``spec_installer.rst``
        - ``docs/syspilot/design/``
        - SYSP_SPEC_INSTALLER_* nodes (T-8)
      * - ``req_setup_engineer.rst``
        - ``docs/syspilot/requirements/``
        - SYSP_REQ_INSTALLER_* nodes (all)

   **Test Environment Requirements:**

   .. list-table:: Test Environment
      :header-rows: 1
      :widths: 35 65

      * - Item
        - Value / Constraint
      * - Clean test repository
        - A Git-initialized repository with **no** ``.github/`` syspilot install
          and **no** local ``syspilot/`` product directory. Used for T-1, T-6,
          T-7.
      * - Existing installation repo
        - The same test repository after T-1 completes.  Used for T-2 (re-run),
          T-3 (BOM check), T-4 (wrapper script check), T-5 (frontmatter
          preservation).
      * - Agent file with edited ``tools:``
        - ``.github/agents/syspilot.cm.agent.md`` in the test repo, with the
          ``tools:`` frontmatter field manually set to a tester-chosen value
          (e.g. ``tools: [my-custom-tool]``) before T-5 begins.
      * - Python environment without ``sphinx-needs``
        - The active venv for the test repo must have ``sphinx-needs``
          uninstalled (``pip uninstall sphinx-needs``).  Used for T-6.
      * - BOM detection tool
        - Any tool capable of detecting UTF-8 BOM (``\xEF\xBB\xBF``): e.g.
          ``grep -rl $'\xef\xbb\xbf' .github/`` on Linux/macOS,
          ``Get-Content -Encoding Byte`` on PowerShell, or a hex editor.
      * - Branch override
        - The ``@syspilot.setup`` invocation in T-1 SHALL include the parameter
          ``branch=development``.
      * - Feature branch
        - ``feature/installer-spec-rewrite`` is checked out and all CR commits
          are present in the working tree before any test scenario is executed.

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/installer-spec-rewrite`` is checked out.
   * AC-2: The tester has write access to the test repository and can run
     ``@syspilot.setup`` from the VS Code Chat panel.
   * AC-3: The tester can run PowerShell or Bash commands in the test repository.
   * AC-4: Network access to ``github.com/georgdoll/syspilot`` is available for
     scenarios that invoke the Installer (T-1, T-2, T-5, T-7).

   **Failure Injection Method (T-7 only):**

   To simulate a mid-install failure for T-7, the tester SHALL corrupt a file
   in the temporary staging area before the installer writes it to disk.
   The exact method is implementation-dependent on the installer's mechanism;
   the tester SHALL consult the installer agent's workflow to identify the
   appropriate injection point.  If no reproducible injection point is
   available, this scenario is marked as requiring a test harness and its
   fragility SHALL be reported (see testability concern TC-1 in
   ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE``).

   **Acceptance Criteria:**

   * AC-1: The clean test repository is a valid Git repository with no
     pre-existing ``.github/`` syspilot files at test start.
   * AC-2: The tester can identify and invoke ``@syspilot.setup`` from VS Code
     Chat with a branch override parameter.
   * AC-3: A BOM detection method is confirmed working on the test system before
     T-3 is executed.
   * AC-4: The Python venv for the test repository can have ``sphinx-needs``
     removed and re-installed without affecting the product repository.
