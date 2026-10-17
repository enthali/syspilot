Harness Prompt Adapter Test Data
================================

Test data requirements for ``SYSP_US_UAT_HARNESS_PROMPT_ADAPTER``.


.. req:: UAT Test Data: Harness Prompt and Command Adapter
  :id: SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER
  :status: approved
  :links: SYSP_US_UAT_HARNESS_PROMPT_ADAPTER

   **Required Artifacts:**

   * A source Manager prompt with a known ``description`` and
     ``agent: syspilot.<name>`` route.
   * Generated VS Code GitHub Copilot, Claude Code, and OpenCode
     installations from the same source revision as required production
     evidence, plus a generated Qoder package-staging archive as required
     experimental-tier evidence.
   * Installed copies of the three production-parity harnesses and a project
     file-listing tool; Claude Code is required for independent live native
     acceptance. Qoder's live native acceptance is deferred future scope for
     this change.
   * One representative multi-token user request containing spaces and
     punctuation, plus a deterministic Manager receiver that records the exact
     request and observable outcome; use it unchanged for the paired VS Code
     and OpenCode native invocations.

   **Fixture Preparation:**

   .. list-table:: Prompt Fixtures
      :header-rows: 1
      :widths: 25 40 35

      * - Fixture
        - Initial State
        - Native Invocation
      * - ``F-PROMPT-VSCODE``
        - Empty ``.github/`` project harness directory
        - Prompt command routed to custom agent
      * - ``F-PROMPT-OPENCODE``
        - Empty ``.opencode/`` project harness directory
        - ``/<command-name>``
      * - ``F-PROMPT-CLAUDE``
        - required production empty ``.claude/`` project harness directory
        - ``@agent-name`` or installed Skill command
      * - ``F-PROMPT-QODER``
        - Required experimental-tier package-staging archive (no project
          ``.qoder/`` directory is written by this change)
        - Custom Agent invocation, deferred: requires the user's documented
          external UI import before it applies

   Each fixture SHALL be reset before its scenario, and the tester SHALL
    record the complete generated path list after installation. For
    ``F-PROMPT-VSCODE`` and ``F-PROMPT-OPENCODE``, the tester SHALL submit the
    same request text, record the selected Manager, and compare the observable
    workflow outcome and exact received request rather than treating matching
    routing metadata or fabricated metadata tuples as behavioral evidence.

    This requirement owns native prompt and command behavior only. Clean
    installation, update, injected-failure, and rollback acceptance are owned
    exclusively by ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` and SHALL NOT be
    inferred from this requirement's evidence.

   **Acceptance Criteria:**

   * **AC1**: Acceptance MUST independently demonstrate the required live
     native commands and prompts for production Claude Code; static or
     simulated invocation evidence is insufficient. Qoder acceptance is
     limited to the deterministic, checksummed package-staging archive;
     live native command/prompt evidence for Qoder is deferred future scope
     and is not required for this change.
