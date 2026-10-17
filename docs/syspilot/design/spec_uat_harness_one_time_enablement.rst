Harness Deterministic Installation Expected Outcomes
====================================================

Expected outcomes for ``SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT``.


.. spec:: UAT Expected Outcomes: Harness One-Time Enablement
  :id: SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT
  :status: approved
  :priority: mandatory
  :tags: uat, harness, bootstrap, update, expected-outcomes
  :links: SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT

   **TC-HOTE-REMOTE-CLEAN — Remote URL clean install**

   *Precondition:* Reset a clean Git fixture with Git and ``uv`` available and
   no syspilot or Setup files.

  *Action:* From the fixture root, execute the selected branch's raw
  ``syspilot/installer.py`` URL through ``uv run --no-project`` with
  ``install``, explicit repository/branch, and each of ``--harness vscode``,
  ``--harness claude``, ``--harness opencode``, and ``--harness qoder`` in
  separate fixtures.

   *Expected result:*

   * [ ] Each production-parity harness (vscode, claude, opencode) installs
     successfully in its isolated run; the qoder run stages its deterministic
     package archive successfully, which is its complete required evidence
     at the experimental, installable tier.
   * [ ] Setup, all product agents/skills, applicable commands, shared docs
     bootstrap, and ``.syspilot/installer.py`` are present in the expected
     locations for only the selected harness.
   * [ ] No Setup or Installer agent was required before command execution.
   * [ ] Source bytes and generated native artifacts derive from one selected
     upstream revision and validation precedes the final commit.
   * [ ] No hand-edited personal or global harness configuration is required,
     and the installed project-scoped Setup entry persists for later updates.
   * [ ] Lifecycle pass/fail evidence is referenced from
     SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE rather than independently awarded by
     this enablement scenario.

   **TC-HOTE-REPEAT — Identical-command update**

   *Precondition:* Install revision ``R1`` with TC-HOTE-REMOTE-CLEAN, then make
   revision ``R2`` available at the selected branch.

   *Action:* Re-run the exact same remote command and arguments.

   *Expected result:*

   * [ ] The marked product artifact contains the ``R2`` value.
   * [ ] A third unchanged run is idempotent and creates no content change or
     unnecessary commit.
   * [ ] Only the explicitly selected harness target plus shared runtime/docs
     are updated; every unselected harness directory is unchanged.

   **TC-HOTE-SETUP-DIRECT — Setup invokes local runtime directly**

   *Precondition:* Use a successful production-harness installation and record
   child-process/tool calls. Configure Agent, Task, and ``runSubagent`` use to
   fail the scenario.

   *Action:* Invoke installed Setup for an update with explicit repository,
   branch, target root, and harness.

   *Expected result:*

   * [ ] Setup executes ``uv run --no-project .syspilot/installer.py install``
     with the explicit inputs.
   * [ ] No Installer-agent, Agent, Task, ``runSubagent``, SEND, or native
     subagent delegation occurs.
   * [ ] The update completes with the same deterministic summary and
     validation gates as direct invocation.

   **Ownership note:** This design owns the one-time enablement mechanism,
   persistence of the project-scoped Setup entry, and absence of hand-edited
   harness configuration. SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE exclusively
   owns clean-install, update, injected-failure, and rollback acceptance.
   SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX exclusively owns live native discovery
   and loading.
