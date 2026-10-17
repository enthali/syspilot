Harness Skill Adapter Test Data
===============================

Test data requirements for ``SYSP_US_UAT_HARNESS_SKILL_ADAPTER``.


.. req:: UAT Test Data: Harness Skill Frontmatter Adapter
   :id: SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER
   :status: approved
   :priority: mandatory
   :tags: uat, harness, skill, frontmatter, test-data
   :links: SYSP_US_UAT_HARNESS_SKILL_ADAPTER

   **Required Artifacts:**

   * One source Skill that declares ``group``, ``tools``, and ``triggers``
     and one source Skill that declares only required metadata.
   * Generated copies under the VS Code and OpenCode native Skill directories;
     Claude Code generated copies are required production fixtures; Qoder
     Skill members staged inside the package archive are required
     experimental-tier fixtures.
   * A YAML parser, byte-level body comparison tool, and installed OpenCode
     harness; an installed Claude Code harness is a required production
     fixture, and the staged Qoder archive is a required experimental-tier
     fixture.
   * Installed production-harness fixtures containing shared
     ``.syspilot/templates/change-document.md``, shared non-native Skill
     resources below ``.syspilot/skills/``, and no unselected harness tree.

   **Reference Data:**

   * The source directory name, complete YAML mapping, and Instructions/Rules
     body for each selected Skill.
   * OpenCode's recognized fields: ``name``, ``description``, ``license``,
     ``compatibility``, and ``metadata``.
   * The expectation that Installer mutual exclusion reads ``group`` before
     adaptation and placement; adapted native frontmatter omits ``group``,
     ``tools``, and ``triggers``, and no target harness is expected to enforce
     ``group`` itself.

   **Preconditions:**

   * Generate all copies from the same source revision.
   * Reset each harness project and preserve each source directory name.
   * Split frontmatter from the Markdown body before byte comparison.
   * Invoke change-launcher and impact path resolution from OpenCode without a
     ``.github`` directory and record every resolved shared resource path.

   **Acceptance Criteria:**

   This requirement owns Skill adaptation and content-correctness acceptance
   only. Live native Skill discovery and loading acceptance are owned
   exclusively by ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` and SHALL NOT be
   inferred from this requirement's evidence.

   * **AC1**: Acceptance MUST independently demonstrate that production
     Claude Code Skill adaptations preserve the required target frontmatter,
     source directory name, Instructions/Rules body, and shared resource
     resolution. Qoder acceptance is limited to its experimental-tier,
     package-staged Skill adaptations preserving the same target
     frontmatter, source directory name, Instructions/Rules body, and shared
     resource resolution; live native Qoder Skill-loading evidence is
     deferred future scope and is not required for this change.
