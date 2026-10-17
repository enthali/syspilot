Harness Limitations Expected Outcomes
=====================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_LIMITATIONS``.


.. spec:: UAT Expected Outcomes: Harness Disclosed Limitations
  :id: SYSP_SPEC_UAT_HARNESS_LIMITATIONS
  :status: approved
  :priority: mandatory
  :tags: uat, harness, limitations, disclosure, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_LIMITATIONS

    Claude Code scenarios below are mandatory production evidence with
    independent results. Qoder scenarios are evaluated against the
    experimental, installable tier; native import and Manager-to-Engineer
    orchestration evidence for Qoder are explicitly deferred future scope for
    this change, not silently dropped. A disclosed limitation never waives a
    required role, Skill, invocation, orchestration, loading, or lifecycle
    capability on the production-parity tier.

  **TC-HL-CLAUDE-CROSS-DISCOVERY — Compatibility boundary is disclosed**

   *Precondition:* All 13 generated ``.claude/agents/*.md`` files and the
   corresponding limitation text are available. Retain the completed live
   evidence from ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX``.

  *Action:* Inspect every generated frontmatter block and the limitation text,
  then compare their claims with the referenced target-matrix evidence.

   *Expected result:*

   * [ ] Every generated Claude agent declares ``user-invocable: false``.
   * [ ] ``SYSP_SPEC_HARNESS_LIMITATIONS`` identifies the field as a VS Code
     compatibility extension and makes no Claude-native hiding claim.
   * [ ] The referenced ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX`` result proves
     the live VS Code and Claude Code behavior; this scenario does not
     duplicate picker or native-discovery evidence.

   *Traces to:* ``SYSP_US_UAT_HARNESS_LIMITATIONS`` AC-1

   ---

  **TC-HL-CLAUDE-ALLOWLIST — Main-thread and nested SEND boundaries**

    *Precondition:* The required Claude Code fixture is available; install the
    two-Engineer Manager fixture.

  *Action:* Inspect the main-thread Manager's adapted frontmatter and
  Workflow, compare every mapped target with generated native names, then
  inspect a nested-spawning subagent's Agent tool declaration.

   *Expected result:*

   * [ ] No source ``agents:`` field or invented field is present.
   * [ ] The main-thread Manager has an explicit
     ``Agent(syspilot-engineer-a, syspilot-engineer-b)`` tools entry and its
     structurally adapted Workflow names those same resolvable targets.
   * [ ] Bare ``Agent`` on a nested spawner is recognized as unrestricted and
     is not reported as an enforced per-target allowlist.
   * [ ] The limitation accurately identifies only the nested enforcement
     boundary.

   *Traces to:* ``SYSP_US_UAT_HARNESS_LIMITATIONS`` AC-2

   ---

    **TC-HL-OPENCODE-METADATA — Source metadata remains installation-effective**

   *Precondition:* Prepare two source orchestration Skills sharing one
   ``group`` and select one through the Installer in an OpenCode fixture.

   *Action:* Inspect installed frontmatter, open the Skill picker, and list
   installed orchestration-group directories.

   *Expected result:*

   * [ ] The selected Skill omits source ``group``, ``tools``, and
     ``triggers`` from native frontmatter and loads without a frontmatter error.
   * [ ] Exactly one orchestration-group Skill directory is installed,
     proving source ``group`` metadata drove mutual exclusion before adaptation.
   * [ ] The limitation states that unsupported keys are omitted without
     removing Installer-side semantics.

   *Traces to:* ``SYSP_US_UAT_HARNESS_LIMITATIONS`` AC-3

   ---

  **TC-HL-QODER-NESTING — Qoder orchestration remains deferred future scope**

    *Precondition:* The required Qoder experimental-tier package-staging
    fixture is available. Live Manager/Engineer Plugin/package import and
    execution is deferred future scope and is not a precondition for this
    change.

  *Action:* Review the limitation text and the orchestration UAT record.

   *Expected result:*

   * [ ] No result claims that Qoder's ``/`` selection surface, main-Agent
     coordination statement, or imported specialized Agents establish a
     programmable Manager-callable delegation API, blocking behavior, or a
     structured result-return contract.
   * [ ] The limitation states that Manager-to-Engineer orchestration parity
     for Qoder is out of scope for this change and explicitly deferred to a
     future change — a scope decision, not a blocked-pending-evidence gap.
     Engineer-to-Engineer nesting is neither required nor claimed.

   *Traces to:* ``SYSP_US_UAT_HARNESS_LIMITATIONS`` AC-4

   ---

   **TC-HL-QODER-RULES — Rules remain disclosed future scope**

    *Precondition:* The required Qoder experimental-tier fixture is
    available; install syspilot and capture a complete generated path
    manifest.

   *Action:* Search generated output for Qoder Rule artifacts, then verify
   installed Agents and Skills remain discoverable.

   *Expected result:*

   * [ ] No Qoder Rule artifact is generated or registered.
   * [ ] Generated Agent and Skill artifacts remain present; their live native
     discovery/loading result is referenced from the target matrix.
   * [ ] The limitation identifies Settings-UI registration as relevant only
     to a future Rules-distribution scope.

   *Traces to:* ``SYSP_US_UAT_HARNESS_LIMITATIONS`` AC-5

   ---

   **Testability Note:**

  Negative vendor-capability claims can change between harness versions.
  Every run must record the tested version and date. This design defers live
  native discovery/loading to SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX and lifecycle
  acceptance to SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE. If a newer harness adds
  a native capability, the corresponding scenario is a design-review trigger.
