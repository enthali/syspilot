Installer Harness Targets Expected Outcomes
============================================

Expected outcomes specification for
``SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS``. This document is the
per-scenario verification contract. Deterministic adapter behavior is run
against filesystem and upstream-response fixtures; harness discovery and
invocation scenarios remain runtime UAT.


.. spec:: UAT Expected Outcomes: Installer Harness Targets
  :id: SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS
  :status: approved
  :priority: mandatory
  :tags: uat, installer, harness, regression, critical, expected-outcomes
  :links: SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS

   **Definition:**

   For each scenario in ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS``, the
   following outcomes SHALL be observable. Each scenario is self-contained:
   the human tester prepares the named fixture, runs the action, and
   confirms the expected result. A check item passes when the exact
   condition is met; it fails otherwise.

   ---

   **TC-IHT-VSCODE — VS Code-only project unaffected**

   *Precondition:* Fixture ``F-VSCODE-ONLY``.

      *Action:* Run the Installer update with ``--harness vscode``.

   *Expected result:*

   * [ ] ``.github/`` output is unchanged in content from a pre-CR
     Installer run (same files, same frontmatter, same bodies)
   * [ ] Shared Skill resources and templates exist only below ``.syspilot``
   * [ ] No ``.claude/``, ``.opencode/``, or ``.qoder/`` directory exists
     after the run

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-1

   ---

  **TC-IHT-CLAUDE — Claude Code production target selection**

   *Precondition:* Fixture ``F-CLAUDE-EMPTY``.

      *Action:* Run a fresh install with ``--harness claude``.

   *Expected result:*

   * [ ] ``.claude/agents/*.md`` exists for every product agent
   * [ ] ``.claude/skills/<name>/SKILL.md`` exists for every product Skill
   * [ ] Each adapted file's Markdown body is byte-for-byte identical to
     the corresponding ``.github/`` file's body
   * [ ] Every adapted agent contains required ``name`` and ``description``;
     all 13 ``name`` values are valid, unique ``syspilot-<role>`` identities
   * [ ] Adapted agent frontmatter declares ``user-invocable: false`` on every
     generated agent and contains no source ``agents``, Jarvis ``agent``, or
     ``version`` key
   * [ ] Every Claude Agent allowlist and Workflow/orchestration binding
     reference resolves to one of those 13 identities

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-2

   ---

   **TC-IHT-OPENCODE — OpenCode adapted output incl. commands**

   *Precondition:* Fixture ``F-OPENCODE-EMPTY``.

      *Action:* Run a fresh install with ``--harness opencode``.

   *Expected result:*

   * [ ] ``.opencode/agents/*.md`` exists for every product agent
   * [ ] ``.opencode/skills/<name>/SKILL.md`` exists for every product Skill
   * [ ] ``.opencode/commands/<name>.md`` exists for each Manager-style
     agent that has a VS Code prompt file counterpart
   * [ ] Installed Skill frontmatter omits source-only ``group``/``tools``/
     ``triggers`` keys while preserving the Instructions/Rules body bytes
   * [ ] Parsed agent YAML uses ``mode: primary`` for Managers and
     ``mode: subagent`` for Engineers; a nonempty source allowlist produces a
     ``permission.task`` map with ``"*": deny`` and one explicit allow entry,
     while Setup has no Installer task permission
   * [ ] Every source prompt produces a command whose filename preserves dots,
     whose frontmatter contains description (including fallback) and agent,
     and whose body is exactly ``$ARGUMENTS`` plus one terminal newline
   * [ ] Required templates and non-native Skill resources exist under shared
     ``.syspilot/{templates,skills}``; no ``.github`` path is created

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-3

   ---

      **TC-IHT-QODER — Qoder package staging (experimental, installable tier)**

   *Precondition:* Fixture ``F-QODER-EMPTY``.

      *Action:* Run a fresh install with ``--harness qoder`` and inspect the
      Installer-owned deterministic Qoder Plugin/package staging artifact.

   *Expected result:*

   * [ ] Exactly one final archive exists at
     ``.syspilot/qoder/syspilot-qoder-plugin.zip``; its ZIP structure,
     ``plugin.json`` manifest, normalized member inventory, source revision,
     member digests, and package digest are valid and match the frozen plan.
   * [ ] The structured result is ``staged``. The archive is the sole source
     for documented Qoder UI import; it is not a directly live-loaded
     ``.qoder/`` project tree, an imported native result, or a parity pass.
   * [ ] No separate Qoder command/prompt artifact is generated and no
     user-global configuration is hand-edited.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-4

   ---

      **TC-IHT-NOSPEC — Unselected harnesses remain untouched**

   *Precondition:* Fixture ``F-CLEAN``.

      *Action:* Run a fresh install with ``--harness vscode``.

   *Expected result:*

   * [ ] ``.claude/`` does not exist after the run
   * [ ] ``.opencode/`` does not exist after the run
   * [ ] No Qoder Plugin/package staging artifact exists after a non-Qoder run
   * [ ] Only ``.github/``, declared shared ``.syspilot`` runtime/resources,
     and missing-only documentation bootstrap files exist as installer-created
     output

   * [ ] Public selection accepts exactly ``vscode``, ``claude``, ``opencode``,
     and ``qoder``; any other value fails before mutation.
   * [ ] Selection never depends on installed applications, existing harness
     directories, personal/global configuration, or launcher names.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-5

   ---

   **TC-IHT-ORPHAN — Orphan cleanup and summary extend to harness dirs**

   *Precondition:* Fixture ``F-CLAUDE-RETIRE`` (prior install with
   ``.claude/`` output; one product agent retired from upstream for this
   run).

      *Action:* Run the deterministic Claude adapter update fixture.

   *Expected result:*

   * [ ] The retired agent's file is absent from ``.claude/agents/`` after
     the run
   * [ ] ``.github/agents/`` is unchanged by the Claude-targeted run
   * [ ] The run summary table contains a row for ``.claude/agents/`` (and
     ``.claude/skills/`` if any Skill was also affected) with correct
     installed/updated/removed counts

   *Traces to:* ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` AC-6

   ---

  **Executable fixture suite — adapter and selection contract**

   *Precondition:* Create an isolated Git repository and a fake upstream
   revision containing product roots plus a conflicting ``.github`` tree.
   Include frontmatter requiring structured YAML parsing, bodies with both EOF
   newline states, all harness presence signals, protected files, and orphans.

    *Action:* Execute the PEP 723 test entry point as ``uv run --no-project
    tests/test_installer.py`` and invoke the engine CLI once for each public
    harness value plus one invalid value. Record selected destinations and
    target mutations.

   *Expected result:*

   * [ ] Only selected-revision ``syspilot/{agents,prompts,skills,templates}``
     entries are enumerated; the conflicting ``.github`` tree is ignored and
     every recorded fetch uses the requested branch/revision
   * [ ] Agent, Skill, and command adapters produce parser-valid native YAML,
     exact filenames, UTF-8 without BOM, and byte-identical methodology bodies
     including terminal-newline state
   * [ ] Orphan eligibility and per-directory summaries match fixture state
   * [ ] Every valid value writes only its selected native tree or, for Qoder,
     the final archive ``.syspilot/qoder/syspilot-qoder-plugin.zip``, plus
     declared shared paths; the invalid value causes zero mutation.
   * [ ] Claude Code and Qoder target-selection results are reported
     independently.

   **Ownership note:** This design owns explicit target selection, deterministic
   adaptation, and selected-tree isolation. SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE
   exclusively owns clean installation, update, injected-failure, and rollback
   acceptance. SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX exclusively owns live native
   discovery and loading.
