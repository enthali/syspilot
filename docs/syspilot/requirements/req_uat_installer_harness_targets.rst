Installer Harness Targets Test Data
====================================

Test data requirements for
``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS``.


.. req:: UAT Test Data: Installer Harness Targets
  :id: SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS
  :status: approved
  :priority: mandatory
  :tags: uat, installer, harness, regression, critical, test-data
  :links: SYSP_US_UAT_INSTALLER_HARNESS_TARGETS

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS``, the
   following artifacts, fixtures, and reference data SHALL be available to
   the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``syspilot.installer.agent.md``
        - ``syspilot/agents/``
        - Deterministic explicit-harness runtime guidance — all ACs
      * - ``spec_installer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_INSTALLER_HARNESS_TARGETS``
      * - ``spec_harness_adapters.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_HARNESS_TARGET_MATRIX``, ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``,
          ``SYSP_SPEC_HARNESS_SKILL_ADAPTER``, ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER``
      * - ``installer.py`` and ``test_installer.py``
        - ``syspilot/`` and ``tests/``
        - PEP 723 runtime, uv-only CLI/validation, and executable fixture suite

   **Target-Project Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-VSCODE-ONLY``
        - Existing syspilot installation under ``.github/``
        - AC-1 (no regression)
      * - ``F-CLAUDE-EMPTY``
        - Required production deterministic Claude Code adapter fixture
        - AC-2
      * - ``F-OPENCODE-EMPTY``
        - Clean Git repository; selected with ``--harness opencode``
        - AC-3
      * - ``F-QODER-EMPTY``
        - Clean Git repository; selected with ``--harness qoder``; required
          experimental-tier package-staging acceptance fixture
        - AC-4
      * - ``F-CLEAN``
        - Clean target project selected with ``--harness vscode``
        - AC-5
      * - ``F-CLAUDE-RETIRE``
        - Required production adapter fixture including ``.claude/agents/`` output; one
          previously-installed product agent removed from the simulated
          upstream source for this run
        - AC-6

   **Reference Data:**

   * Full per-harness target directory matrix:
     ``SYSP_SPEC_HARNESS_TARGET_MATRIX``
   * Agent frontmatter field-drop table: ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``
   * Skill frontmatter field table (six-field OpenCode allowlist context):
     ``SYSP_SPEC_HARNESS_SKILL_ADAPTER``

   **Tooling:**

   * VS Code with Copilot, target project open, Installer accessible — all
     scenarios
   * A directory listing / diff tool to compare ``.github/`` output
     before/after (AC-1) and to inspect generated frontmatter (AC-2, AC-3,
     AC-4)
   * A byte-level or line-level diff tool to confirm Skill body identity and
     agent-body identity outside authorized structural binding locations
     between a ``.github/`` file and its harness-adapted counterpart (AC-2)
   * A YAML parser and reference resolver for all 13 Claude Code native names,
     Agent allowlists, and Workflow/orchestration binding targets (AC-2)
   * ``uv`` and Git, plus a process-command recorder that identifies direct
     invocations of ``python``, ``python3``, ``pip``, ``pip3``, and
     ``sphinx-build``

   **Preconditions (all scenarios):**

   * AC-1: Fixture ``F-VSCODE-ONLY`` is prepared before AC-1 is run.
   * AC-2: Fixture ``F-CLAUDE-EMPTY`` is prepared before AC-2 is run.
   * AC-3: Fixture ``F-OPENCODE-EMPTY`` is prepared before AC-3 is run.
   * AC-4: Fixture ``F-QODER-EMPTY`` is prepared before AC-4 is run.
   * AC-5: Fixture ``F-CLEAN`` is prepared before AC-5 is run.
   * AC-6: Fixture ``F-CLAUDE-RETIRE`` is prepared before AC-6 is run.
   * AC-7: No virtual environment is activated and no fixture-local or global
     Python dependency installation is required; uv-managed state remains
     outside the target repository.

   **Acceptance Criteria:**

   This requirement owns explicit target selection and target-isolation
   evidence only. Clean installation, update, injected-failure, rollback, and
   lifecycle no-regression acceptance are owned exclusively by
   ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` and SHALL NOT be inferred from this
   requirement's evidence.

   * **AC9**: Acceptance MUST independently verify that ``claude`` is a
     selectable production target and ``qoder`` is a selectable
     experimental, installable target, and that each target's generated
     output remains isolated from every non-selected harness tree.
