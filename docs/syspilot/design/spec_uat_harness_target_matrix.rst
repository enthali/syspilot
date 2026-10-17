Harness Target Matrix Expected Outcomes
=======================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX``.


.. spec:: UAT Expected Outcomes: Harness Target Matrix
  :id: SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX
  :status: approved
  :priority: mandatory
  :tags: uat, harness, matrix, portability, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_TARGET_MATRIX

  **TC-HTM-DIRS — Project-scoped artifacts and Qoder package staging**

    *Precondition:* Reset required production-parity fixtures for VS Code
    GitHub Copilot, Claude Code, and OpenCode, plus the Qoder
    experimental-tier package-staging fixture.

  *Action:* Run the syspilot installation entry point once per
   production-parity fixture, then list the generated agent and Skill files
   or, for Qoder, the deterministic Plugin/package staging artifact.

   *Expected result:*

   * [ ] VS Code agents are under ``.github/agents/*.agent.md`` and Skills
     under ``.github/skills/<name>/SKILL.md``.
   * [ ] Claude Code agents are under ``.claude/agents/*.md`` and Skills under
     ``.claude/skills/<name>/SKILL.md``.
   * [ ] OpenCode agents are under ``.opencode/agents/*.md`` and Skills under
     ``.opencode/skills/<name>/SKILL.md``.
   * [ ] Qoder staging contains exactly
     ``.syspilot/qoder/syspilot-qoder-plugin.zip``. Its normalized ZIP member
     inventory, ``plugin.json`` manifest inventory, member digests, package
     digest, and source revision match the frozen plan.
   * [ ] The Qoder staging artifact is source for documented Qoder UI import,
     not a claim that a project ``.qoder/`` directory is directly live-loaded
     or that the Installer completed native import.
   * [ ] No syspilot artifact is written to another harness's destination.

   *Traces to:* ``SYSP_US_UAT_HARNESS_TARGET_MATRIX`` AC-1

   ---

   **TC-HTM-PROMPTS — Prompt and command destinations**

    *Precondition:* The production-parity fixtures plus the Qoder
    experimental-tier fixture contain the completed TC-HTM-DIRS installation.

  *Action:* List prompt or command artifacts in each fixture and compare
  them with the source Manager prompts. For Qoder, inspect the staged package
  before its documented import or installation.

   *Expected result:*

   * [ ] VS Code has ``.github/prompts/*.prompt.md`` for source prompts.
   * [ ] OpenCode has ``.opencode/commands/<name>.md`` for source Manager
     prompts.
   * [ ] Claude Code has no separate syspilot prompt or command artifact and
     exposes its required native Manager invocation surface.
   * [ ] Qoder has no separate direct project prompt or command artifact; its
     imported Plugin/package supplies the required Custom Agent surface.

   *Traces to:* ``SYSP_US_UAT_HARNESS_TARGET_MATRIX`` AC-2

   ---

  **TC-HTM-NATIVE — Native artifacts load without config edits**

  *Precondition:* Reset one clean fixture per production-parity harness and
  record a complete identity baseline for every applicable personal/global
  harness configuration location. For each location record absent/present
  state, node type, and, for a regular file, byte digest; record directory
  identity and declared child inventory where the harness uses a
  configuration directory.

  *Action:* Install syspilot. For VS Code, Claude Code, and OpenCode, open the
   relevant native agent/Skill picker; for the Claude fixture, retain the
   source ``.github/agents`` tree while generating all 13 Claude agents, then
   inspect both VS Code's direct picker and Claude Code's native agent list.
   For OpenCode, restart or reload as its normal discovery flow requires.
   Re-observe every baseline global location after installation. Do not accept
   Qoder UI import in this lifecycle action.

   *Expected result:*

   * [ ] VS Code, Claude Code, and OpenCode list and load every installed
     syspilot Manager, Engineer, Skill, and applicable invocation surface from
     their project-scoped destination.
   * [ ] Claude Code lists and can invoke all 13 generated
     ``syspilot-<role>`` identities and retains Agent-tool orchestration.
   * [ ] VS Code lists none of those 13 Claude-format identities, including
     ``syspilot-release``. Its direct picker lists only source
     ``.github/agents`` roles declaring ``user-invocable: true``.
   * [ ] Qoder installer evidence is limited to a valid staged package and an
     unchanged global-state baseline; it does not claim native discovery or
     loading. This is Qoder's complete required evidence for this change's
     experimental, installable tier — native discovery/loading is deferred
     future scope, not a gap in this check.
   * [ ] Every personal/global baseline location retains the same
     absent/present state and node type; every pre-existing regular file has
     the same byte digest and every pre-existing directory the same declared
     identity/inventory. Creation of a formerly absent file or directory fails
     this check.
   * [ ] The tester performed no manual personal/global configuration edit.

   *Traces to:* ``SYSP_US_UAT_HARNESS_TARGET_MATRIX`` AC-3

   ---

  **TC-HTM-QODER-EXTERNAL-IMPORT — External native import prerequisite (deferred future scope)**

  *Precondition:* TC-HTM-DIRS produced the validated package digest. Qoder's
  documented UI import surface is available to a human operator.

  *Action:* The operator imports exactly the recorded archive through Qoder's
  documented UI, then records the Qoder version, visible package identity, and
  available Agent and Skill surfaces.

  *Expected result:*

  * [ ] This is explicitly external product-capability evidence, not an
    Installer command, transaction step, rollback step, or autonomous normal
    installation result.
  * [ ] The observed imported identity matches the staged package digest.
  * [ ] This scenario is out of scope for this change's Qoder acceptance,
    which is satisfied by deterministic package staging alone. Its
    absence, failure, or non-repeatability does not block this change's
    Qoder clearance; it blocks only the separate, future native-import
    milestone this scenario evidences for a later change.
  * [ ] Even a successful UI import does not clear Qoder orchestration:
    autonomous Manager workflow clearance remains exclusively owned by
    SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER and is out of scope for this
    change.

   ---

   **TC-HTM-REGRESSION — VS Code target remains unchanged**

   *Precondition:* Reset ``F-MATRIX-VSCODE`` and make the pre-change VS Code
   installation manifest available.

   *Action:* Install syspilot and compare all generated ``.github/`` paths
   with the reference manifest.

   *Expected result:*

   * [ ] The generated path set exactly matches the reference manifest.
   * [ ] Agent filenames retain ``*.agent.md`` and prompt filenames retain
     ``*.prompt.md``.
   * [ ] No non-VS Code harness directory is created.

   *Traces to:* ``SYSP_US_UAT_HARNESS_TARGET_MATRIX`` AC-4

   ---

   **Testability Note:**

  TC-HTM-NATIVE is the exclusive owner of live native discovery/loading
  evidence for the production-parity tier. TC-HTM-QODER-EXTERNAL-IMPORT
  records the Qoder UI prerequisite as deferred future scope; it is not
  required for this change's Qoder clearance and cannot turn staging into
  deterministic lifecycle success. Static inspection is insufficient for the
  production-parity tier. Missing live evidence blocks only the affected
  production-parity harness's clearance; Claude Code's result is independent
  of Qoder's experimental-tier result. Lifecycle acceptance remains
  exclusively owned by SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE.
