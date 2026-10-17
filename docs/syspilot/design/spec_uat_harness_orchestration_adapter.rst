Harness Orchestration Adapter Expected Outcomes
===============================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER``.


.. spec:: UAT Expected Outcomes: Harness Orchestration Fallback
  :id: SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER
  :status: approved
  :priority: mandatory
  :tags: uat, harness, orchestration, fallback, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER

   **TC-HOA-SYNC — Every target selects the synchronous variant**

  *Precondition:* Reset all production orchestration fixtures (VS Code
  GitHub Copilot, Claude Code, OpenCode, and the Qoder package-staging
  fixture), including ``F-ORCH-JARVIS-PRESENT``.

   *Action:* Install syspilot in each fixture and inspect the installed
   orchestration-group Skill.

   *Expected result:*

   * [ ] Each fixture contains ``syspilot.orchestration-subagent``.
   * [ ] No fixture contains ``syspilot.orchestration-jarvis``, including the
     fixture with a pre-existing ``.jarvis/`` directory.
   * [ ] Exactly one Skill with ``group: orchestration`` is installed.

   *Traces to:* ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER`` AC-1

   ---

   **TC-HOA-BINDING — Deterministic native binding generation**

   *Precondition:* Install the same source revision into clean VS Code and
   OpenCode fixtures and retain source plus generated orchestration Skills.

   *Action:* Parse the designated binding section and compare all content
   outside frontmatter and that section byte-for-byte.

   *Expected result:*

   * [ ] VS Code maps SEND to ``runSubagent`` and contains no OpenCode Task
     instruction in its binding section.
   * [ ] OpenCode maps SEND to native Task and contains no ``runSubagent``
     instruction in its binding section.
   * [ ] RECEIVE, RESPOND, synchronous ordering, result propagation, and every
     rule outside the binding section are byte-identical to the semantic source.
   * [ ] A missing, duplicate, or malformed binding boundary fails before
     checkpoint creation.

   *Traces to:* ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER`` AC-2

   ---

   **TC-HOA-PRODUCTION — Complete autonomous Manager workflows**

   *Precondition:* Complete TC-HOA-SYNC for VS Code GitHub Copilot, Claude
   Code, and OpenCode, then install a representative Manager workflow
   requiring multiple Engineer roles. Qoder is not a precondition target for
   this scenario; its orchestration evidence is out of scope for this
   change (see TC-HOA-QODER).

   *Action:* Invoke the Manager in autonomous product operation on each of
   the three production-parity harnesses. Inspect every delegation, returned
   result, stage transition, and the final Manager response.

   *Expected result:*

   * [ ] The fixture declares its ordered Engineer list and one unique fixed
     result token per Engineer before execution.
   * [ ] The captured native transcript shows every required Manager-to-
     Engineer delegation and returned token in declared order.
   * [ ] Terminal Manager RESPOND contains every unique token in declared
     order, proving result consumption and complete stage progression without
     a user prompt or approval gate between stages.
   * [ ] Invocation or one successful delegation alone is not a pass.
   * [ ] Claude Code's result is recorded and cleared independently of
     Qoder's deferred, out-of-scope result; the two are not conflated.
   * [ ] VS Code GitHub Copilot and OpenCode each independently pass the
     ordered-token transcript and terminal-result assertions; matching paths,
     frontmatter, route metadata, or one delegation is not no-regression
     evidence.

   *Traces to:* ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER`` AC-2

   ---

   **TC-HOA-CLAUDE — Claude Code native binding and delegation**

   *Precondition:* Complete Claude static adapter checks; install a Manager and
   its allowed Engineer under their mapped native names. Authenticate Claude
   Code for the live portion, or record authentication as externally blocked.

  *Action:* Inspect the Manager tools/Workflow bindings and execute the
  complete representative autonomous Manager workflow.

   *Expected result:*

   * [ ] The main-thread Manager's explicit ``Agent(<native-name>, ...)``
     targets and every Workflow binding resolve to generated Claude names.
   * [ ] Authenticated execution uses every mapped Engineer identity required
     by the workflow and returns every result to the Manager.
   * [ ] Agent-not-found is a failure. Authentication failure is an external
     blocked result that proves neither delegation nor production support.
   * [ ] Static parsing, discovery, or one delegation alone is not production
     acceptance.

   *Traces to:* ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER`` AC-3

   ---

  **TC-HOA-QODER — Qoder autonomous delegation evidence gate (deferred future scope)**

   *Precondition:* Complete static adapter checks for Qoder's package-staging
   artifact.

  *Action:* This scenario is retained as the acceptance test for a future
  change that pursues Qoder Manager-to-Engineer orchestration parity. For
  this change, it is not executed as a clearance requirement: record the
  tested Qoder version and the staged package's checksum only. Should a
  future change attempt live evidence, it would build and import the
  deterministic Qoder Plugin/package through its documented extension
  mechanism, then run the repeatable ordered-token Manager fixture, capturing
  actual main-Agent coordination, every required specialized-Agent
  invocation, each returned and consumed result, and terminal Manager output,
  without specifying or assuming an undocumented tool/API, blocking behavior,
  or result-return syntax, and without relaying requests or results through
  the user.

   *Expected result:*

   * [ ] This change records Qoder orchestration as explicitly out of scope
     and deferred, not as blocked-pending-evidence: the distinction matters
     because deferral is a scope decision, not a failed acceptance gate.
   * [ ] Plugin/package import, ``/`` agent selection, task-description
     matching, or a general main-Agent coordination statement remains
     insufficient by itself to establish autonomous Manager-to-Engineer
     orchestration, if and when this scope is picked up in a future change.
   * [ ] Should complete live evidence be produced in a future change, the
     native transcript and terminal response would need to pass the
     ordered-token assertions in TC-HOA-PRODUCTION.
   * [ ] No Engineer-to-Engineer nesting capability is required or claimed.
   * [ ] Deferring this scenario does not change any production-parity
     harness's independently recorded result.

   *Traces to:* ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER`` AC-3

   ---

  **Testability Note:** This design owns repeatable live orchestration behavior
  only, for the production-parity tier (VS Code GitHub Copilot, OpenCode,
  Claude Code). Native discovery/loading is exclusively owned by
  SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX; clean installation, update, injected
  failure, and rollback are exclusively owned by
  SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE. Missing authentication or harness
  availability blocks the affected production-parity harness's clearance and
  is never converted into a pass. Qoder orchestration evidence is out of
  scope for this change and is deferred to a future change; that deferral is
  a disclosed scope decision, not a blocked gate within this change.
