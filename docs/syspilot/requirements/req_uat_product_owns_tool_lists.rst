Product-Owns-Tool-Lists Test Data
==================================

Test data requirements for the ``product-owns-tool-lists`` UAT chains.

.. note::
   **Partially superseded by** ``remove-tools-frontmatter`` (2026-07-02).
   See ``docs/syspilot/userstories/us_uat_product_owns_tool_lists.rst`` for
   details. ``SYSP_REQ_UAT_AGENT_BASE_TOOLSET`` is deprecated in its
   entirety; the T-3 fixture below (Installer chain) is superseded.


.. req:: UAT Test Data: Installer Tool Ownership Transfer
   :id: SYSP_REQ_UAT_INSTALLER_TOOL_OWNERSHIP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, product-owns-tool-lists, test-data
   :links: SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP

   **Description:**

   To execute the three test scenarios in ``SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP``,
   the following artifacts, tools, and preconditions SHALL be available.

   **Primary Artifacts Under Test:**

   .. list-table:: Installer Artifacts Under Test
      :header-rows: 1
      :widths: 45 25 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_installer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_INSTALLER_DUTIES``, ``SYSP_SPEC_INSTALLER_WORKFLOW`` (T-1, T-2)
      * - ``req_setup_engineer.rst``
        - ``docs/syspilot/requirements/``
        - ``SYSP_REQ_INSTALLER_DUTIES``, ``SYSP_REQ_INSTALLER_WORKFLOW`` (T-1, T-2)
      * - ``syspilot.installer.agent.md``
        - ``syspilot/agents/``
        - Updated Installer agent (T-3)
      * - Agent file with edited ``tools:``
        - ``.github/agents/`` in target project
        - File with manually modified ``tools:`` for update test (T-3) —
          **superseded, see** ``SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER``

   **Test Environment Requirements:**

   .. list-table:: Test Environment
      :header-rows: 1
      :widths: 35 65

      * - Item
        - Value / Constraint
      * - Feature branch
        - ``feature/product-owns-tool-lists`` is checked out in the syspilot
          workspace before any scenario is executed.
      * - Existing installation repo
        - A separate Git-initialized target project with a syspilot installation
          already in place under ``.github/``. Used for T-3.
      * - Agent file with edited ``tools:``
        - ``.github/agents/syspilot.cm.agent.md`` in the target project, with
          the ``tools:`` frontmatter field manually set to a tester-chosen value
          (e.g. ``tools: [my-sentinel-tool]``) before T-3 begins. The sentinel
          value must not appear in the upstream ``syspilot/agents/`` files.
      * - VS Code with Copilot
        - VS Code open on the target project; ``@syspilot.setup`` accessible
          from the Chat panel.

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/product-owns-tool-lists`` is checked out in the
     syspilot workspace.
   * AC-2: The tester has read access to the spec and requirements RST files.
   * AC-3: For T-3 — a separate target project with an existing syspilot
     installation is available.


.. req:: UAT Test Data: Agent Base Toolset Uniformity
   :id: SYSP_REQ_UAT_AGENT_BASE_TOOLSET
   :status: deprecated
   :priority: mandatory
   :tags: uat, agent-arch, tools, product-owns-tool-lists, test-data
   :links: SYSP_US_UAT_AGENT_BASE_TOOLSET

   .. note::
      **⚠ DEPRECATED by** ``remove-tools-frontmatter``. See
      ``SYSP_US_UAT_AGENT_BASE_TOOLSET`` for rationale. Superseded by
      ``SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER``.

   **Description:**

   To execute the four test scenarios in ``SYSP_US_UAT_AGENT_BASE_TOOLSET``,
   the following artifacts, tools, and preconditions SHALL be available.

   **Primary Artifacts Under Test:**

   .. list-table:: Agent Arch Artifacts Under Test
      :header-rows: 1
      :widths: 45 25 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_agent_arch.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_AGENT_BASE_TOOLSET``, ``SYSP_SPEC_AGENT_ARCH_FRONTMATTER`` (T-1)
      * - ``req_agent_arch.rst``
        - ``docs/syspilot/requirements/``
        - ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10/11/12 (T-2, T-3, T-4)
      * - All agent files (14)
        - ``syspilot/agents/``
        - ``syspilot.cm``, ``syspilot.pm``, ``syspilot.qm``, ``syspilot.design``,
          ``syspilot.implement``, ``syspilot.docu``, ``syspilot.uat``,
          ``syspilot.mece``, ``syspilot.trace``, ``syspilot.verify``,
          ``syspilot.release``, ``syspilot.setup``, ``syspilot.installer``,
          ``syspilot.qm`` (T-2, T-3, T-4)

   **Test Environment Requirements:**

   .. list-table:: Test Environment
      :header-rows: 1
      :widths: 35 65

      * - Item
        - Value / Constraint
      * - Feature branch
        - ``feature/product-owns-tool-lists`` is checked out before any scenario.
      * - Text search tool
        - Any tool capable of searching for a string across multiple files
          (e.g. VS Code Search, ``grep``, PowerShell
          ``Select-String``). Used for T-3 (resolveMemoryFileUri scan) and
          T-4 (runSubagent scan).
      * - Reference tool list
        - The base toolset listed in ``SYSP_SPEC_AGENT_BASE_TOOLSET`` — tester
          should have this open alongside the agent files during T-2.
      * - Python environment
        - Active Python venv with ``sphinx-needs`` installed. Used for the
          shared sphinx-build scenario.

   **Expected agent file count:** 14 files matching ``syspilot/agents/syspilot.*.agent.md``.

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/product-owns-tool-lists`` is checked out.
   * AC-2: The tester has read access to all files under ``syspilot/agents/``
     and ``docs/syspilot/``.
   * AC-3: The Python venv under ``docs/.venv`` is activated (for the shared
     build scenario).
