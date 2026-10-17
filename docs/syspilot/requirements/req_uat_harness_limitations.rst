Harness Limitations Test Data
=============================

Test data requirements for ``SYSP_US_UAT_HARNESS_LIMITATIONS``.


.. req:: UAT Test Data: Harness Disclosed Limitations
  :id: SYSP_REQ_UAT_HARNESS_LIMITATIONS
  :status: approved
  :priority: mandatory
  :tags: uat, harness, limitations, disclosure, test-data
  :links: SYSP_US_UAT_HARNESS_LIMITATIONS

   **Required Evidence:**

   The limitation entries in ``SYSP_SPEC_HARNESS_LIMITATIONS`` SHALL be
   available together with:

   * A generated OpenCode installation; a generated Claude Code installation
     is a required production fixture, and a generated Qoder package-staging
     archive is a required experimental-tier fixture.
   * The installed production harness version and its current native
     agent/Skill UI or execution transcript; required Claude Code
     observations record the exact version and test date and are required as
     independent production evidence. The Qoder package archive's checksum
     and manifest record the same for the experimental tier.
   * A Manager with a two-Engineer source allowlist and two Skills sharing
     the same orchestration ``group``.

   **Reference Checks:**

   * The generated Claude frontmatter and cross-discovery limitation text;
     live VS Code picker and Claude Code discovery evidence referenced from
     ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX``.
   * Claude Code generated main-thread and nested-spawning Manager
     frontmatter, mapped Workflow bindings, and Agent-tool semantics.
   * OpenCode Skill loading plus the Installer's mutually exclusive Skill
     placement result.
   * Qoder generated Agents, Skills, and Rules paths as staged inside the
     package archive.

   **Preconditions:**

   * Reset the relevant harness fixture before every scenario.
   * Generate all artifacts from the same source revision.
   * Preserve screenshots or text transcripts for positive UI/runtime
     observations and complete path manifests for absence checks.

   **Acceptance Criteria:**

   * **AC1**: Acceptance MUST independently verify production Claude Code
     capabilities and the Qoder experimental-tier package-staging capability;
     limitation disclosures MUST NOT waive any required production capability
     on the production-parity tier, and MUST NOT silently drop Qoder's
     disclosed deferred future scope (native import, Manager delegation
     transcript).
