Harness Agent Adapter Test Data
===============================

Test data requirements for ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER``.


.. req:: UAT Test Data: Harness Agent Frontmatter Adapter
  :id: SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER
  :status: approved
  :priority: mandatory
  :tags: uat, harness, agent, frontmatter, test-data
  :links: SYSP_US_UAT_HARNESS_AGENT_ADAPTER

   **Required Artifacts:**

   * Source agents ``syspilot.cm.agent.md`` and
     ``syspilot.implement.agent.md``, plus ``syspilot.setup.agent.md``, from
     ``syspilot/agents/``.
   * Generated counterparts for VS Code and OpenCode; all 13 Claude Code
     product-agent counterparts are required production fixtures; the Qoder
     package-staging archive's agent members are required experimental,
     installable-tier fixtures.
   * A YAML parser or frontmatter inspector and a byte-level body comparison
     tool.
   * A process-command recorder for the installed Setup update invocation.
   * Installed OpenCode with a clean project containing its native harness
     directory and Claude Code CLI 2.1.274 or later with an isolated
     ``.claude/agents`` fixture. The installed Claude Code fixture is
     required for independent production acceptance; the staged Qoder
     archive is required for independent experimental-tier acceptance.

   **Reference Field Sets:**

   .. list-table:: Agent Adapter Expectations
      :header-rows: 1
      :widths: 20 40 40

      * - Harness
        - Required Mapping
        - Unsupported Source Fields
      * - Claude Code
        - Required ``name`` and ``description``, plus applicable ``tools``;
          dotted ``syspilot.<role>`` maps to ``syspilot-<role>``; every agent
          carries ``user-invocable: false`` as a VS Code compatibility
          extension without changing Claude-native discoverability
        - Source ``agents``, Jarvis ``agent``, ``version``
      * - OpenCode
        - ``description``, ``mode``, and Manager ``permission.task``
        - Jarvis ``name`` and ``agent`` identity
      * - Qoder
        - ``description``
        - ``user-invocable``, ``agents``, Jarvis identity, ``version``

   **Preconditions:**

   * Generate all adapted files from the same source revision.
   * Split each file at the closing YAML delimiter before comparing bodies.
   * Inventory the complete 13-file source agent set and derive the expected
     Claude Code name set before inspecting generated output.
   * Reset each runtime fixture before TC-HAA-RUNTIME.
   * Configure Setup with explicit repository, branch, target, and OpenCode
     harness inputs before TC-HAA-OPENCODE.

   **Acceptance Criteria:**

   This requirement owns adapted agent structure and role-execution semantics
   only. Live native agent discovery and loading acceptance are owned
   exclusively by ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` and SHALL NOT be
   inferred from this requirement's evidence.

   * **AC1**: Acceptance MUST independently demonstrate that production
     Claude Code agent adaptations preserve the required frontmatter
     mappings, unchanged source body, and prescribed role-execution
     semantics. Qoder acceptance is limited to its experimental-tier,
     package-staged agent adaptations preserving the same frontmatter
     mappings, unchanged source body, and prescribed role-execution
     semantics; live native Qoder agent-loading evidence is deferred future
     scope and is not required for this change.
