Harness Target Matrix Test Data
===============================

Test data requirements for ``SYSP_US_UAT_HARNESS_TARGET_MATRIX``.


.. req:: UAT Test Data: Harness Target Matrix
  :id: SYSP_REQ_UAT_HARNESS_TARGET_MATRIX
  :status: approved
  :priority: mandatory
  :tags: uat, harness, matrix, portability, test-data
  :links: SYSP_US_UAT_HARNESS_TARGET_MATRIX

   **Description:**

   The following fixtures and references SHALL be available to the human
   tester.

   .. list-table:: Target Fixtures
      :header-rows: 1
      :widths: 25 40 35

      * - Fixture
        - Initial State
        - Scenarios
      * - ``F-MATRIX-VSCODE``
        - Clean project with ``.github/`` as its harness signal
        - TC-HTM-DIRS, TC-HTM-PROMPTS, TC-HTM-REGRESSION
      * - ``F-MATRIX-CLAUDE``
        - Clean project with the source ``.github/agents`` tree, an empty
          ``.claude/`` directory, live Claude Code integration, and VS Code
        - TC-HTM-DIRS, TC-HTM-PROMPTS, TC-HTM-NATIVE
      * - ``F-MATRIX-OPENCODE``
        - Clean project with an empty ``.opencode/`` directory
        - TC-HTM-DIRS, TC-HTM-PROMPTS, TC-HTM-NATIVE
      * - ``F-MATRIX-QODER``
        - Clean project after installation; the checksummed package archive
          ``.syspilot/qoder/syspilot-qoder-plugin.zip`` exists per the Qoder
          Staging Contract. No ``.qoder/`` project directory or live Qoder
          integration is required for this change's experimental-tier
          acceptance.
        - TC-HTM-DIRS, TC-HTM-PROMPTS

   **Reference Data:**

   * The complete directory and distribution table in
     ``SYSP_SPEC_HARNESS_TARGET_MATRIX``
   * A pre-change VS Code installation manifest listing every path under
     ``.github/``
   * The complete 13-agent source inventory, one representative Skill, and one
     Manager prompt from the syspilot source distribution

   **Tooling and Preconditions:**

   * VS Code and OpenCode are installed and can open their matching fixture.
     An installed Claude Code fixture is required for independent production
     acceptance. The Qoder fixture requires only the staged, checksummed
     package archive for independent experimental-tier acceptance; live
     native discovery for Qoder is deferred future scope.
   * The current syspilot installer or equivalent implemented installation
     entry point is available.
   * The tester can list project files, compare manifests, and inspect each
     harness's loaded agents, Skills, and commands.
   * Each fixture is reset to its stated initial state before its scenario.

    This requirement owns target-matrix coverage and is the exclusive UAT owner
    for live native discovery and loading acceptance. Clean installation,
    update, injected-failure, and rollback acceptance are owned exclusively by
    ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` and SHALL NOT be inferred from this
    requirement's evidence.

   **Acceptance Criteria:**

   * **AC1**: Claude Code MUST independently load the installed complete
     Manager set, Engineer set, Skill set, and native invocation surfaces
     through the live native integration; static file presence or a
     simulated adapter is insufficient. Qoder's independent experimental-tier
     acceptance is the staged, checksummed package archive
     (``.syspilot/qoder/syspilot-qoder-plugin.zip``) with its manifest and
     digest present per the Qoder Staging Contract; live native discovery or
     loading is deferred future scope for Qoder.
   * **AC2**: With the complete source and generated Claude agent trees in one
     project, VS Code MUST expose no generated Claude-format identity in its
     direct picker, including ``syspilot-release``. ``.github/agents`` MUST be
     the sole VS Code picker surface, with only source roles declaring
     ``user-invocable: true`` visible, while Claude Code MUST still discover
     and permit native invocation of every generated agent.
