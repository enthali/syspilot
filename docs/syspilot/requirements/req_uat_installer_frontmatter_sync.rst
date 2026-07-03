Installer Frontmatter Sync Test Data
====================================

Test data requirements for ``SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC``.


.. req:: UAT Test Data: Installer Frontmatter Sync
   :id: SYSP_REQ_UAT_INSTALLER_FRONTMATTER_SYNC
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, regression, critical, test-data
   :links: SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC

   **Description:**

   To run the single scenario in
   ``SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC``, the following artifacts and
   reference data SHALL be available to the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 45 30 25

      * - Artifact
        - Location
        - Relevance
      * - ``syspilot.installer.agent.md`` (product)
        - ``syspilot/agents/``
        - AC-1
      * - ``syspilot.installer.agent.md`` (instance)
        - ``.github/agents/``
        - AC-1
      * - ``spec_installer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4 (reference, unchanged)

   **Reference Data:**

   * Retired phrasing to search for (must be absent): "read the current
     ``tools:`` frontmatter value from disk", "replace the upstream
     ``tools:`` line with the saved value"
   * Target phrasing to confirm present (must match spec): "written
     verbatim from upstream", "no local field is preserved", Setup
     Bootloader ``tools:`` exception stated as also verbatim-from-upstream

   **Tooling:**

   * A text search tool (VS Code Search, ``grep``, PowerShell
     ``Select-String``)

   **Preconditions:**

   * AC-1: Branch ``feature/installer-frontmatter-sync`` is checked out;
     the Implement stage has updated both the product source and the
     installed instance of ``syspilot.installer.agent.md`` before this
     scenario is run.
