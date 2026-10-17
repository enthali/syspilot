Harness Target Matrix UAT
=========================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_TARGET_MATRIX``.


.. story:: UAT: Harness Target Matrix
   :id: SYSP_US_UAT_HARNESS_TARGET_MATRIX
   :status: approved
   :priority: mandatory
   :tags: uat, harness, matrix, portability
   :links: SYSP_US_HARNESS_PORTABILITY, SYSP_US_HARNESS_INSTALL

   **As a** syspilot Test Designer,
   **I want** a human tester to verify every production harness destination,
   **so that** generated artifacts use native locations without changing the
   established VS Code installation.

   **Artifacts Under Test:**

   * The implemented harness-target selection derived from
     ``SYSP_SPEC_HARNESS_TARGET_MATRIX``
   * A syspilot source distribution containing agents, Skills, and prompts
   * Clean production-parity fixtures for VS Code GitHub Copilot, OpenCode,
     and Claude Code, plus a clean Qoder package-staging fixture evaluated at
     the experimental, installable tier

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_TARGET_MATRIX``,
   ``SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE``, and
   ``SYSP_REQ_HARNESS_NATIVE_INSTALL``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX``; expected outcomes are defined in
   ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX``.

   **Acceptance Criteria:**

   1. **Project-scoped agent and Skill destinations.** Install syspilot into
      each production-parity fixture; verify files are written only to the
      selected harness's documented project directories. Claude Code passes
      independently. Qoder acceptance is the checksummed package archive at
      its documented staging path, not a project-scoped agent/Skill
      directory.
   2. **Prompt/command destinations.** Verify VS Code receives prompt files,
      OpenCode receives command files, and Claude Code and the Qoder package
      archive receive no separate prompt/command files.
   3. **Native loading and cross-discovery.** Verify every production-parity
      harness loads its project artifacts without a manual edit to personal
      or global configuration. With both VS Code and Claude trees present,
      Claude Code loads all generated native agents while VS Code hides every
      duplicate Claude-format identity and shows only user-invocable source
      roles from ``.github/agents``. Qoder native loading requires the
      user's documented external UI import of the staged package and is
      deferred future scope for this change.
   4. **VS Code mapping unchanged.** Compare a VS Code-only installation with
      the pre-change reference manifest and verify its paths and file set are
      unchanged.
