Harness Prompt Adapter Expected Outcomes
========================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER``.


.. spec:: UAT Expected Outcomes: Harness Prompt/Command Adapter
  :id: SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER
  :status: approved
  :links: SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER

   **TC-HPA-VSCODE — Existing VS Code prompt remains unchanged**

   *Precondition:* Reset ``F-PROMPT-VSCODE`` and retain the source prompt.

    *Action:* Install syspilot, open the generated prompt, and invoke it with
    the representative request from the test-data requirement.

   *Expected result:*

   * [ ] ``.github/prompts/syspilot.<name>.prompt.md`` exists.
   * [ ] Its description and ``agent: syspilot.<name>`` route match source.
   * [ ] Invocation starts the named Manager agent.
   * [ ] The Manager produces the fixture's observable workflow outcome for
     the representative request.

   *Traces to:* ``SYSP_US_UAT_HARNESS_PROMPT_ADAPTER`` AC-1

   ---

   **TC-HPA-OPENCODE — OpenCode command mirrors the prompt role**

   *Precondition:* Reset ``F-PROMPT-OPENCODE`` and retain every product source
   prompt, including one prompt without a description and names containing
   dots.

    *Action:* Install syspilot, inspect the generated command, and invoke it by
    its native command name with exactly the same representative request used
    in TC-HPA-VSCODE.

   *Expected result:*

   * [ ] Exactly one ``.opencode/commands/<name>.md`` exists for every product
     ``<name>.prompt.md``; removing the exact suffix preserves all dots in
     ``<name>``.
   * [ ] Its frontmatter retains the source description or, when absent, uses
     the corresponding agent description, and routes through the source
     ``agent: <name>`` value.
   * [ ] The body is exactly ``$ARGUMENTS`` plus one terminal newline and does
     not duplicate the Manager's workflow prose.
   * [ ] Native invocation supplies a multi-token request containing spaces and
     punctuation; OpenCode substitutes the complete request and the routed
     Manager records the exact received text.
   * [ ] The selected Manager and observable workflow outcome are equivalent
     to TC-HPA-VSCODE for the identical request; matching route metadata alone
     does not satisfy this check.

   *Traces to:* ``SYSP_US_UAT_HARNESS_PROMPT_ADAPTER`` AC-2

   ---

   **TC-HPA-CLAUDE — Claude Code uses no separate prompt file**

    *Precondition:* Required production fixture ``F-PROMPT-CLAUDE`` is reset.

   *Action:* Install syspilot, list all generated paths, and invoke the
   Manager through its native agent or Skill entry point.

   *Expected result:*

   * [ ] No syspilot prompt/command directory or separate prompt artifact is
     generated under ``.claude/``.
   * [ ] The Manager remains invocable through its installed native surface.
   * [ ] The representative request reaches the selected Manager and produces
     the expected workflow outcome; lifecycle evidence is referenced from
     SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE rather than repeated here.

   *Traces to:* ``SYSP_US_UAT_HARNESS_PROMPT_ADAPTER`` AC-3

   ---

   **TC-HPA-QODER — Qoder uses no separate prompt file (experimental tier, native invocation deferred)**

    *Precondition:* The Qoder experimental-tier package-staging fixture is
    reset. This scenario's live-invocation portion requires the deferred,
    out-of-scope external UI import and is not required for this change's
    Qoder clearance.

  *Action:* Install syspilot and inspect the deterministic Qoder package. If
  and only if external UI import evidence exists under
  SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX (deferred future scope for this
  change), directly invoke the Manager through the imported Custom Agent
  surface with the representative request.

   *Expected result:*

   * [ ] No separate Qoder prompt/command artifact is generated; staging is
     exactly the documented import package and direct project paths are not
     treated as native artifacts. This is Qoder's complete, sufficient
     evidence for this change's experimental, installable tier.
   * [ ] If a future change supplies external UI import evidence, the
     imported Plugin/package-supplied Custom Agent would be expected to
     remain directly invocable and to reach the selected Manager for a basic
     direct-invocation response — routing evidence only, not
     production-parity or autonomous workflow clearance.
   * [ ] Production-parity-equivalent Qoder orchestration evidence (native
     transcript, fixture-defined ordered Engineer tokens, returned-result
     consumption, terminal ordered result, no manual relay) is out of scope
     for this change and is deferred to a future change; its absence does
     not block this change's Qoder acceptance, which rests solely on
     deterministic package staging.

   *Traces to:* ``SYSP_US_UAT_HARNESS_PROMPT_ADAPTER`` AC-4

   **Ownership note:** This design owns prompt/command adaptation and request
   routing behavior. Clean installation, update, injected failure, and rollback
   are exclusively deferred to SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE. Live native
   discovery/loading is exclusively deferred to
   SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX.
