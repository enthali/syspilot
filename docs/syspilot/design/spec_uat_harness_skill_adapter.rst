Harness Skill Adapter Expected Outcomes
=======================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER``.


.. spec:: UAT Expected Outcomes: Harness Skill Frontmatter Adapter
  :id: SYSP_SPEC_UAT_HARNESS_SKILL_ADAPTER
  :status: approved
  :priority: mandatory
  :tags: uat, harness, skill, frontmatter, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER

   **TC-HSA-BODY — Skill body remains single-source**

   *Precondition:* Source and generated copies of both selected Skills are
   available from the same revision.

   *Action:* Remove only YAML frontmatter and compare each generated Markdown
   body byte-for-byte with its source.

   *Expected result:*

   * [ ] Every generated Instructions/Rules body exactly matches its source.
   * [ ] No harness-specific instruction is inserted into the body.

   *Traces to:* ``SYSP_US_UAT_HARNESS_SKILL_ADAPTER`` AC-1

   ---

   **TC-HSA-DISCOVERY — Description and directory invocation name**

    *Precondition:* Generate both Skills for VS Code GitHub Copilot,
    OpenCode, and Claude Code using the original directory names, plus the
    Qoder experimental-tier fixture with Skills contained in the
    deterministic Plugin/package staging artifact. Native loading is
    established by SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX before this content
    check, for the production-parity tier.

  *Action:* Inspect generated YAML and verify the expected directory invocation
  name against the target-matrix discovery/loading record.

   *Expected result:*

   * [ ] Every copy retains the source ``description`` unchanged.
   * [ ] OpenCode's expected invocation name is its source directory name.
   * [ ] Claude Code satisfies the static content and invocation-name checks.
   * [ ] Qoder satisfies its static checks from package staging alone, which
     is its complete required evidence at the experimental, installable
     tier; its imported Plugin/package loading and invocation evidence is
     deferred future scope, not required for this change.

   *Traces to:* ``SYSP_US_UAT_HARNESS_SKILL_ADAPTER`` AC-2

   ---

    **TC-HSA-METADATA — Unsupported native metadata is omitted**

    *Precondition:* The selected metadata-rich Skill is generated for OpenCode
    and for the required Claude Code production fixture and the Qoder
    experimental-tier fixture.

    *Action:* Parse each generated YAML block, record the source ``group``
    before adaptation, and install a second Skill from the same group.

   *Expected result:*

   * [ ] ``group``, ``tools``, and ``triggers`` are absent from every adapted
     native frontmatter block where the harness does not support them.
   * [ ] The Installer uses the source ``group`` value before adaptation and
     replaces the previously installed member of that group.
   * [ ] Exactly one Skill from the group remains installed even though the
     adapted ``SKILL.md`` does not retain the ``group`` key.
   * [ ] Every production-parity fixture contains parser-valid adapted Skill
     frontmatter; native loading evidence remains exclusively in the target
     matrix result. The Qoder fixture's staged frontmatter is parser-valid;
     native loading evidence for Qoder is deferred future scope.

   *Traces to:* ``SYSP_US_UAT_HARNESS_SKILL_ADAPTER`` AC-3

   ---

   **TC-HSA-RUNTIME — Representative Skill instructions are available**

    *Precondition:* The target matrix has recorded live native discovery/loading
     for both Skills in every production-parity harness. Qoder is excluded
     from this live-runtime check for this change.

  *Action:* Use the target-matrix loading record and compare the first
  instruction and one rule from the corresponding generated Skill body.

   *Expected result:*

   * [ ] Both Skill combinations retain the source instruction and rule in
     their generated bodies for the production-parity tier, with Claude
     Code's result recorded independently of Qoder's deferred experimental-
     tier static-only evidence.
   * [ ] The identified instruction and rule match the source text.

   *Traces to:* ``SYSP_US_UAT_HARNESS_SKILL_ADAPTER`` AC-4

   ---

   **Testability Note:**

  Description-based automatic invocation is model-selected and cannot be
  made deterministic from a fixed prompt. This design verifies description,
  invocation-name, and body preservation only. Live native discovery/loading
  is exclusively deferred to SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX; lifecycle
  acceptance is exclusively deferred to SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE.
