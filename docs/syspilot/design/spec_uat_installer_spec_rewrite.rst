Installer — Spec Rewrite Expected Outcomes
==========================================

Expected outcomes specification for ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE``.
Per-scenario verification checklist for all nine CR acceptance criteria.


.. spec:: UAT Expected Outcomes: Installer Spec Rewrite
   :id: SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE
   :status: draft
   :priority: mandatory
   :tags: uat, installer, spec-rewrite, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE

   **Definition:**

   For each of the nine test scenarios derived from the ``installer-spec-rewrite``
   CR, the following outcomes SHALL be observable when the rewritten Installer
   is correct.  The tester executes each scenario in order and records pass/fail
   for every check item.

   ---

   **T-1 — Clean install end-to-end**

   *CR ACs:* AC1, AC9 |
   *REQ refs:* ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``, ``SYSP_REQ_INSTALLER_WORKFLOW``

   **Precondition:** Clean test repository (no ``.github/`` syspilot files);
   network access to GitHub; ``branch=development`` passed to ``@syspilot.setup``.

   **Actions:**

   1. Open VS Code Chat in the clean test repository.
   2. Invoke: ``@syspilot.setup branch=development``
   3. Observe agent output until completion or error.

   **Expected Results:**

   * [ ] The agent completes without an error message.
   * [ ] Files appear under ``.github/agents/``, ``.github/prompts/``,
     ``.github/skills/``, and ``.github/templates/``.
   * [ ] The agent output includes a per-directory summary table with rows
     for ``agents/``, ``prompts/``, ``skills/``, and ``templates/``.
   * [ ] No message indicates a local-source fallback was used; all fetches
     reference the upstream GitHub repository.
   * [ ] A Git commit is present in the test repo log after the run.

   **Pass criterion:** All five check items confirmed.

   **Fail criterion:** Any error message, any missing directory, summary table
   absent, or local-source message in the output.

   ---

   **T-2 — Re-invoke on existing installation (relaxed idempotency)**

   *CR AC:* AC2 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``

   **Precondition:** T-1 passed; the test repository has a complete syspilot
   installation.

   **Actions:**

   1. In the same test repository, invoke ``@syspilot.setup branch=development``
      again without making any other changes.
   2. Observe agent output until completion or error.

   **Expected Results:**

   * [ ] The agent completes without an error message on the second run.
   * [ ] No message indicates a "Mode-Detect", "same version", or "nothing to
     do" early-exit that would prevent files from being re-checked.
   * [ ] File content in ``.github/`` matches the upstream source after the run.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Error on second run, or agent halts citing Mode-Detect
   logic, or file content differs from upstream.

   ---

   **T-3 — UTF-8 BOM absence in all written files**

   *CR AC:* AC3 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_ENCODING``

   **Precondition:** T-1 or T-2 passed; the test repository contains a complete
   syspilot installation under ``.github/``.

   **Actions:**

   1. From the test repository root, run a BOM scan across all installed files:

      * **Linux / macOS:** ``grep -rl $'\xef\xbb\xbf' .github/``
      * **PowerShell:** ``Get-ChildItem -Recurse .github | ForEach-Object { $bytes = [System.IO.File]::ReadAllBytes($_.FullName); if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) { $_.FullName } }``

   2. Record all file paths returned by the scan.

   **Expected Results:**

   * [ ] The BOM scan returns zero results (empty output).

   **Pass criterion:** Zero files with BOM marker.

   **Fail criterion:** One or more files listed by the BOM scan.

   ---

   **T-4 — No wrapper scripts generated**

   *CR AC:* AC4 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_DIRECT_OPS``

   **Precondition:** T-1 passed; the test repository contains a complete
   syspilot installation.

   **Actions:**

   1. Inspect ``temp/`` in the test repository root:
      ``Get-ChildItem temp\ -ErrorAction SilentlyContinue``
   2. Inspect the project root for any ``.ps1`` or ``.sh`` script files not
      part of the project's own source:
      ``Get-ChildItem *.ps1, *.sh -ErrorAction SilentlyContinue``
   3. Search for ``install.ps1``, ``install.sh``, or any file whose name
      contains "install" outside the ``syspilot/`` product directory.

   **Expected Results:**

   * [ ] ``temp/`` contains no ``install.ps1``, ``install.sh``, or equivalent
     wrapper script created by the Installer.
   * [ ] The project root contains no Installer-generated ``.ps1`` or ``.sh``
     helper file.
   * [ ] The agent output contains no message about generating or writing a
     wrapper script.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Any Installer-generated wrapper script found in ``temp/``
   or the project root.

   ---

   **T-5 — Frontmatter preservation: ``tools:`` preserved, others reset**

   *CR AC:* AC5 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_DUTIES``

   **Precondition:** T-1 passed; ``.github/agents/syspilot.cm.agent.md`` exists.
   The tester has manually edited the ``tools:`` field in that file to a known
   custom value before this scenario begins (e.g. ``tools: [my-custom-tool]``).
   The ``model`` and ``description`` fields are noted before the re-run.

   **Actions:**

   1. Confirm the ``tools:`` custom value is saved in
      ``.github/agents/syspilot.cm.agent.md``.
   2. Invoke ``@syspilot.setup branch=development``.
   3. After completion, open ``.github/agents/syspilot.cm.agent.md`` and
      read the frontmatter.

   **Expected Results:**

   * [ ] The ``tools:`` field value matches the tester's custom value
     (``[my-custom-tool]`` or equivalent) — it was NOT overwritten.
   * [ ] The ``model`` field matches the upstream value (not the locally cached
     value if it changed upstream).
   * [ ] The ``description`` field matches the upstream value.
   * [ ] Open ``.github/agents/syspilot.setup.agent.md`` (the Bootloader):
     its entire content matches the upstream file verbatim — no field preservation
     was applied.

   **Pass criterion:** All four check items confirmed.

   **Fail criterion:** ``tools:`` value reset to upstream; or ``model`` /
   ``description`` not reset; or Bootloader content differs from upstream verbatim.

   ---

   **T-6 — Missing sphinx-needs dependency: stop with instructions**

   *CR AC:* AC6 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_WORKFLOW``

   **Precondition:** ``sphinx-needs`` is uninstalled from the active Python
   environment (``pip uninstall sphinx-needs -y``).  The test repository has no
   pre-existing syspilot installation (or use the clean test repo).

   **Actions:**

   1. Invoke ``@syspilot.setup branch=development``.
   2. Observe agent output.
   3. Inspect the test repository for any modified files.

   **Expected Results:**

   * [ ] The agent output contains instructions for installing
     ``sphinx-needs`` (e.g. ``pip install sphinx-needs``).
   * [ ] The agent stops before writing any syspilot files to ``.github/``.
   * [ ] No files under ``.github/agents/``, ``.github/prompts/``, or
     ``.github/skills/`` were created or modified.
   * [ ] No Git commit was made to the test repository.

   **Pass criterion:** All four check items confirmed.

   **Fail criterion:** Installer proceeds past the dependency check; any file
   written; or a commit created despite missing dependency.

   ---

   **T-7 — Rollback on mid-install failure**

   *CR AC:* AC7 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_ROLLBACK``

   **Testability concern:** See TC-1 below.  This scenario requires the tester
   to inject a failure mid-install.  The exact injection point is
   implementation-dependent.

   **Precondition:** Clean test repository (no syspilot install).  The tester
   has identified the Installer's pre-install commit step in the agent workflow
   and has a method to interrupt execution between file writes (e.g. by manually
   corrupting a file the Installer will write next, or by network interruption
   if the Installer fetches sequentially).

   **Actions:**

   1. Begin invoking ``@syspilot.setup branch=development``.
   2. After the pre-install commit is created (tester observes the commit in
      ``git log``), inject the failure before all files are written.
   3. Observe agent output for rollback messaging.
   4. Run ``git log --oneline -5`` to inspect the repository state.
   5. Inspect ``.github/`` for partially written files.

   **Expected Results:**

   * [ ] The agent output mentions rollback or ``git reset --hard``.
   * [ ] ``git log`` shows the repository is at the pre-install commit
     (i.e. the partial-write commits, if any, are gone).
   * [ ] ``.github/`` contains no partial or corrupt files from the failed run.
   * [ ] The working tree is clean (``git status`` reports no uncommitted changes
     from the Installer's partial work).

   **Pass criterion:** All four check items confirmed.

   **Fail criterion:** Repository left in a partial state; no rollback message;
   or partial files remain in ``.github/``.

   ---

   **T-8 — No customization-question in Step 4 of spec**

   *CR AC:* AC8 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_WORKFLOW``

   **Precondition:** Branch ``feature/installer-spec-rewrite`` is checked out;
   ``docs/syspilot/design/spec_installer.rst`` is readable.

   **Actions:**

   1. Open ``docs/syspilot/design/spec_installer.rst``.
   2. Locate the ``SYSP_SPEC_INSTALLER_WORKFLOW`` spec node.
   3. Find the content corresponding to Step 4 (Frontmatter Preservation /
      file-write step).
   4. Search the spec for "customization" and "double-write".

   **Expected Results:**

   * [ ] No step in ``SYSP_SPEC_INSTALLER_WORKFLOW`` contains a
     "customization question" prompt directed at the user.
   * [ ] No step describes a double-write flow (write once with placeholder,
     then write again with preserved values).
   * [ ] The search for "customization" in the context of a user-facing prompt
     returns no results in the workflow steps section.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Any customization question prompt or double-write step
   found in the spec.

   ---

   **T-9 — Per-directory summary table in run output**

   *CR AC:* AC9 (partial), ``SYSP_REQ_INSTALLER_WORKFLOW`` AC-10 |
   *REQ ref:* ``SYSP_REQ_INSTALLER_WORKFLOW``

   **Precondition:** T-1 passed; the agent output from T-1 is available for
   inspection (or the tester re-runs to capture fresh output).

   **Actions:**

   1. Review the final output section of the ``@syspilot.setup`` agent run.
   2. Locate the run summary.

   **Expected Results:**

   * [ ] A summary table is present in the agent output.
   * [ ] The table contains a row for ``agents/`` with an integer count.
   * [ ] The table contains a row for ``prompts/`` with an integer count.
   * [ ] The table contains a row for ``skills/`` with an integer count.
   * [ ] The table contains a row for ``templates/`` with an integer count.
   * [ ] All counts are non-negative integers (including zero).

   **Pass criterion:** All six check items confirmed.

   **Fail criterion:** Table absent; any directory row missing; any count is
   non-numeric or absent.

   ---

   **Testability Concerns**

   **TC-1 — T-7 Rollback scenario requires manual failure injection**

   Scenario T-7 requires the tester to interrupt the Installer mid-execution.
   This is fragile because:

   * The exact injection point depends on the Installer implementation detail
     (how it sequences file writes relative to the pre-install commit).
   * Network interruption mid-run may leave the agent in an undefined VS Code
     Chat state.
   * There is no automated test harness; the scenario relies on human timing
     and observation.

   *Recommendation:* Accept T-7 as a manual, best-effort scenario for this
   release.  If repeated rollback failures are observed, a dedicated automated
   test harness should be created as a follow-up work item.

   **TC-2 — T-6 requires ``sphinx-needs`` uninstall in a separate venv**

   Uninstalling ``sphinx-needs`` from the shared product venv would break the
   docs build.  The tester MUST use a separate Python environment for the test
   repository.  If no such environment is available, T-6 must be executed in an
   isolated container or VM.

   **TC-3 — T-5 upstream value observation**

   T-5 requires knowing the upstream ``model`` and ``description`` values before
   the re-run to confirm they are reset correctly.  If the upstream values are
   identical to local values, the check item is vacuously true.  The tester
   SHOULD temporarily set ``model`` to a dummy value locally before the re-run
   to make the check observable.
