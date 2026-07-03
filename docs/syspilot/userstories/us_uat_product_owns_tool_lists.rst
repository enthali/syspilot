Product-Owns-Tool-Lists UAT
===========================

User Acceptance Test Stories for the ``product-owns-tool-lists`` change request.
Two chains: Installer tool-ownership transfer and Agent base-toolset uniformity.

.. note::
   **Partially superseded by** ``remove-tools-frontmatter`` (2026-07-02).
   The ``SYSP_SPEC_AGENT_BASE_TOOLSET`` mechanism this chain validates has
   been retired; agents now inherit tools from the user's default VS Code
   agent instead of a product-prescribed list. See
   ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` for current coverage.
   ``SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP`` AC-3 is superseded (see inline
   note); AC-1, AC-2, AC-4 remain valid. ``SYSP_US_UAT_AGENT_BASE_TOOLSET``
   is deprecated in its entirety.


.. story:: UAT: Installer Tool Ownership Transfer
   :id: SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, product-owns-tool-lists
   :links: SYSP_US_INSTALLER

   **As a** syspilot Test Designer,
   **I want** to verify that the Installer no longer preserves ``tools:``
   during updates and instead overwrites it verbatim from upstream,
   **so that** product-side tool fixes reach installed instances and the
   broken preservation logic is fully removed.

   **Context:**

   CR ``product-owns-tool-lists`` transfers ownership of the ``tools:``
   frontmatter field from "user customization preserved by Installer" to
   product-owned.  The Installer previously read the on-disk ``tools:`` value
   and re-injected it after writing the upstream file; this logic has been
   removed.  The Installer now copies every frontmatter field verbatim from
   upstream — including ``tools:``.

   **Artifacts Under Test:**

   * ``docs/syspilot/design/spec_installer.rst`` — ``SYSP_SPEC_INSTALLER_DUTIES``,
     ``SYSP_SPEC_INSTALLER_WORKFLOW``, ``SYSP_SPEC_INSTALLER_ENCODING``
   * ``docs/syspilot/requirements/req_setup_engineer.rst`` — ``SYSP_REQ_INSTALLER_DUTIES``,
     ``SYSP_REQ_INSTALLER_WORKFLOW``
   * ``syspilot/agents/syspilot.installer.agent.md`` — updated Installer agent
   * A target project with an existing syspilot installation for live-update tests

   **Traceability:**

   Covers CR ACs 1 and 3 (spec inspection + build) and ``SYSP_REQ_INSTALLER_DUTIES``
   AC-5 (idempotent sync, verbatim copy), ``SYSP_REQ_INSTALLER_WORKFLOW`` AC-5
   (all frontmatter fields from upstream, none preserved locally).

   **Acceptance Criteria:**

   1. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When ``SYSP_SPEC_INSTALLER_DUTIES`` is inspected,
      Then no Duty or AC mentions preserving, retaining, skipping, or
      re-injecting a ``tools:`` value — traces to CR AC1,
      ``SYSP_REQ_INSTALLER_DUTIES``

   2. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When ``SYSP_SPEC_INSTALLER_WORKFLOW`` is inspected,
      Then AC-5 states that all frontmatter fields come from upstream and
      no local field is preserved — traces to CR AC1,
      ``SYSP_REQ_INSTALLER_WORKFLOW``

   3. Given a target project with an existing syspilot installation where
      ``tools:`` in one agent file has been manually modified,
      When ``@syspilot.setup`` is re-invoked,
      Then the manually modified ``tools:`` value is overwritten with the
      upstream value — traces to ``SYSP_REQ_INSTALLER_WORKFLOW`` AC-5,
      ``SYSP_REQ_INSTALLER_DUTIES``

      .. note::
         **⚠ SUPERSEDED by** ``remove-tools-frontmatter``. Upstream no
         longer carries a ``tools:`` value for non-Setup agents, so "the
         manually modified value is overwritten with the upstream value"
         no longer describes correct behavior — the field is removed
         entirely instead. Replaced by
         ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-3 (live-update scenario:
         stale ``tools:`` field is removed, not overwritten).

   4. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When ``sphinx-build -W`` is run on the ``docs/`` directory,
      Then the build exits with EXIT=0 and no warnings — traces to CR AC3


.. story:: UAT: Agent Base Toolset Uniformity
   :id: SYSP_US_UAT_AGENT_BASE_TOOLSET
   :status: deprecated
   :priority: mandatory
   :tags: uat, agent-arch, tools, product-owns-tool-lists
   :links: SYSP_US_AGENT_ARCH

   .. note::
      **⚠ DEPRECATED by** ``remove-tools-frontmatter`` (2026-07-02).
      ``SYSP_SPEC_AGENT_BASE_TOOLSET`` — the artifact every AC below
      inspects — has been retired from the product. All four scenarios in
      this story test a mechanism that no longer exists and will fail if
      executed against the current spec. Superseded by
      ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER``.

   **As a** syspilot Test Designer,
   **I want** to verify that all product agent files carry the uniform base
   toolset, no agent has workspace-memory access, and only the Setup Bootloader
   has ``agent/runSubagent``,
   **so that** tool permissions are product-defined, uniform, and correctly
   scoped from the single source of truth.

   **Context:**

   CR ``product-owns-tool-lists`` introduces ``SYSP_SPEC_AGENT_BASE_TOOLSET``
   as the single authoritative list of tool identifiers every agent ships with.
   Each of the 14 syspilot product agents in ``syspilot/agents/`` must carry
   exactly the base toolset (plus Setup Bootloader's ``agent/runSubagent``
   addition).  Legacy Jarvis tool names (``enthali.jarvis/``) are replaced
   by the marketplace prefix ``jarvis-core_``.  No agent receives
   ``vscode/resolveMemoryFileUri`` (workspace memory).

   **Artifacts Under Test:**

   * ``docs/syspilot/design/spec_agent_arch.rst`` — ``SYSP_SPEC_AGENT_BASE_TOOLSET``,
     ``SYSP_SPEC_AGENT_ARCH_FRONTMATTER``
   * ``docs/syspilot/requirements/req_agent_arch.rst`` — ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
     AC-10, AC-11, AC-12
   * All 14 files under ``syspilot/agents/``

   **Traceability:**

   Covers CR AC2 (product files have correct tool lists), CR AC3 (build clean),
   ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10 (uniform base toolset),
   AC-11 (no workspace memory), AC-12 (``agent/runSubagent`` Setup-only).

   **Acceptance Criteria:**

   1. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When ``SYSP_SPEC_AGENT_BASE_TOOLSET`` is inspected in the spec,
      Then the spec exists, contains the full tool list with the
      ``jarvis-core_`` prefix, and includes no ``enthali.jarvis/`` references
      — traces to CR AC2, ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10

   2. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When all 14 files in ``syspilot/agents/`` are opened and their ``tools:``
      frontmatter field is inspected,
      Then every agent carries all tools from ``SYSP_SPEC_AGENT_BASE_TOOLSET``
      — traces to CR AC2, ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10

   3. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When all 14 agent files are searched for ``vscode/resolveMemoryFileUri``,
      Then zero occurrences are found in any ``tools:`` field
      — traces to ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-11

   4. Given the ``feature/product-owns-tool-lists`` branch is checked out,
      When all 14 agent files are searched for ``agent/runSubagent``,
      Then exactly one file (``syspilot.setup.agent.md``) contains it and
      no other agent file does — traces to ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
      AC-12
