Harness Agent Adapter Expected Outcomes
=======================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER``.


.. spec:: UAT Expected Outcomes: Harness Agent Frontmatter Adapter
  :id: SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER
  :status: approved
  :priority: mandatory
  :tags: uat, harness, agent, frontmatter, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER

   **TC-HAA-BODY — Agent body remains single-source**

   *Precondition:* All generated Manager and Engineer files and their source
   files are available from the same revision.

   *Action:* Remove only each YAML frontmatter block and perform byte-level
   comparisons of the remaining Markdown bodies.

   *Expected result:*

   * [ ] Every adapted body exactly matches its source body outside the
     deterministic structural binding locations authorized by
     ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``.
   * [ ] Only dotted target identities in Workflow/orchestration bindings are
     replaced by Claude native names; Soul, Duties, headings, ordering,
     ordinary prose, Tailoring text, and all other bytes are unchanged.

   *Traces to:* ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER`` AC-1

   ---

   **TC-HAA-CLAUDE — Claude Code field mapping**

    *Precondition:* All 13 generated Claude Code product agents and their
    source files are available.

   *Action:* Parse each YAML block and compare its keys with the Claude Code
   row in the reference field set.

   *Expected result:*

   * [ ] Every file contains required ``name`` and ``description`` fields;
     every name equals its dotted source ID with periods replaced by hyphens.
   * [ ] Exactly 13 names exist, all are unique, and each contains only
     lowercase letters and hyphens.
   * [ ] A main-thread Manager with a source allowlist has an explicit
     ``Agent(<native-name>, ...)`` tools entry containing exactly the mapped
     target set plus any independently approved/inherited tools.
   * [ ] A nested spawning subagent follows documented Claude Agent-tool
     semantics; bare ``Agent`` is treated as unrestricted, never as a
     per-target allowlist.
   * [ ] Every Workflow and orchestration binding target resolves to exactly
     one of the 13 generated names.
   * [ ] Every generated agent declares ``user-invocable: false`` as a VS
     Code compatibility extension; source ``agents``, Jarvis ``agent``, and
     ``version`` are absent.
   * [ ] No replacement field with different semantics was introduced.
   * [ ] The compatibility field is not reported as Claude-native hiding; all
     13 generated native names and their Agent-tool bindings are preserved.
     Live Claude Code discovery/invocation and VS Code direct-picker evidence
     are referenced from ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX`` rather than
     duplicated here.

   *Traces to:* ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER`` AC-2

   ---

   **TC-HAA-OPENCODE — OpenCode mode and task permissions**

   *Precondition:* Generated OpenCode Manager and Engineer agents are
   available.

   *Action:* Parse their YAML and compare Manager task permissions with the
   Manager's source ``agents:`` allowlist.

   *Expected result:*

   * [ ] The Manager is ``mode: primary`` and its ``permission.task`` grants
     the named Engineer targets.
   * [ ] ``permission.task`` is a YAML map containing ``"*": deny`` and one
     explicit ``<source-allowlist-agent>: allow`` entry for every allowed
     target, rather than a list or combined allow value.
   * [ ] An empty source allowlist produces ``mode: subagent`` and no
     ``permission.task`` map; a nonempty allowlist produces ``mode: primary``.
   * [ ] Setup is ``mode: primary`` because it is user-invocable, has no
     ``permission.task`` map, and grants no Installer delegation.
   * [ ] Jarvis-only ``name`` and ``agent`` identity fields are absent.
   * [ ] Both bodies still pass TC-HAA-BODY.
   * [ ] Invoking Setup records a direct ``uv run --no-project
     .syspilot/installer.py install`` child process with the explicit inputs;
     no Agent, Task, ``runSubagent``, SEND, or Installer-agent invocation is
     recorded.

   *Traces to:* ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER`` AC-3

   ---

  **TC-HAA-QODER — Qoder package field mapping (experimental, installable tier)**

  *Precondition:* The deterministic Qoder Plugin/package staging artifact
  contains all generated Qoder Manager and Engineer agents as the required
  experimental-tier fixture.

  *Action:* Parse staged agent YAML and compare all keys with the documented
  Qoder mapping.

   *Expected result:*

   * [ ] ``description`` is present and unchanged.
   * [ ] ``user-invocable``, ``agents``, ``name``, ``agent``, and ``version``
     are absent.
   * [ ] No undocumented SEND-tool or allowlist key was invented.
   * [ ] The artifact is identified as package source/staging, not as a
     directly live-loaded ``.qoder/`` project path. This static field-mapping
     check is the complete required Qoder evidence for this change; native
     in-app loading is deferred future scope.

   *Traces to:* ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER`` AC-4

   ---

  **TC-HAA-RUNTIME — Representative agents retain original guidance**

   *Precondition:* SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX has independently
   confirmed native loading for each production harness. Retain the loaded
   Manager and Engineer plus their generated and source files.

  *Action:* Invoke each already-loaded agent by its native mechanism and ask it
  to state its role, duties, first workflow step, and terminal workflow step
  from its instructions. Record the generated Claude Code identities for
  user-facing Setup, PM, QM, and CM. Qoder is excluded from this live-runtime
  check for this change; its evidence is limited to TC-HAA-QODER's static
  field mapping.

   *Expected result:*

   * [ ] Each production-parity harness response reflects the source role,
     duties, RECEIVE-first step, and RESPOND-terminal step.
   * [ ] Claude Code's result is recorded independently of Qoder's deferred,
     out-of-scope experimental-tier result; neither result masks the other.
   * [ ] Discovery and loading evidence is referenced from
     SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX rather than duplicated here.

   **OpenCode native configuration check:** in an isolated OpenCode fixture,
   run ``opencode debug config`` from the project root and parse the resolved
   agent configuration. The command must complete without a parser error and
   show the specified Setup and representative Manager/Engineer modes and Task
   permission maps, including Setup's absent task permission. Record the
   OpenCode version; if the command is unavailable, report the runtime check as
   unavailable rather than passing it from static inspection.

   *Traces to:* ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER`` AC-5

   ---

   **Testability Note:**

  Static comparison proves content identity and field mapping. It cannot prove
  model behavior is identical; TC-HAA-RUNTIME checks role-execution semantics
  only after the target matrix has supplied discovery/loading evidence.
  Lifecycle acceptance is exclusively deferred to
  SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE, and live discovery/loading is
  exclusively deferred to SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX.
