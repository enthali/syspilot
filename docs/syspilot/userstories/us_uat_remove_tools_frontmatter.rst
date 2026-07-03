Remove-Tools-Frontmatter UAT
============================

User Acceptance Test Story for the ``remove-tools-frontmatter`` change
request, covering the retirement of the ``tools:`` frontmatter prescription
(except for the Setup Bootloader) and the resulting tool-inheritance model.


.. story:: UAT: Remove Tools Frontmatter
   :id: SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: uat, agent-arch, tools, remove-tools-frontmatter
   :links: SYSP_US_AGENT_ARCH, SYSP_US_DOC_EXTERNAL

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify no
   agent (except the Setup Bootloader) prescribes a ``tools:`` field,
   the Setup Bootloader keeps its explicit list, an update run removes a
   stale ``tools:`` field rather than overwriting it, and the user is
   documented into enabling ``enthali.jarvis-core`` on their default agent,
   **so that** the retired base-toolset mechanism is fully gone from the
   product and the replacement inheritance model is discoverable by the user.

   **Context:**

   The ``remove-tools-frontmatter`` CR retires ``SYSP_SPEC_AGENT_BASE_TOOLSET``
   and strips the ``tools:`` frontmatter field from every agent spec and
   product agent file except the Setup Bootloader, which keeps an explicit,
   hardcoded list (its sole exception, because its one synchronous
   ``agent/runSubagent`` call to the Installer is a structural bootstrap
   dependency). Agents now inherit whatever tools are enabled on the user's
   default VS Code agent. Because the VS Code tool picker's runtime behavior
   is outside syspilot's control and cannot be driven by an automated test
   harness, the "agents function using the default agent's tool selection"
   claim is covered here as a documentation/design-record check, not a
   runtime functional test — this limitation is stated explicitly rather
   than silently assumed.

   **Artifacts Under Test:**

   * ``syspilot/agents/*.agent.md`` — all 14 product agent files
   * ``docs/syspilot/requirements/req_agent_arch.rst`` —
     ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-3, AC-10
   * ``docs/syspilot/design/spec_agent_arch.rst`` —
     ``SYSP_SPEC_AGENT_ARCH_FRONTMATTER``
   * External documentation files enumerated in ``SYSP_US_DOC_EXTERNAL``
     (README, architecture.md, workflows.md, or wherever the Documentation
     Engineer places the ``enthali.jarvis-core`` guidance)
   * A target project with an existing syspilot installation for the
     live-update scenario

   **Traceability:**

   Covers ``SYSP_US_AGENT_ARCH`` AC-6 (no ``tools:`` field except Setup
   Bootloader), ``SYSP_US_DOC_EXTERNAL`` AC-6 (documentation states
   ``enthali.jarvis-core`` requirement), ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
   AC-3 (no ``tools:`` except Setup) and AC-10 (Setup Bootloader is sole
   exception, carries ``agent/runSubagent``).
   Test data is defined in ``SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER``;
   expected outcomes in ``SYSP_SPEC_UAT_REMOVE_TOOLS_FRONTMATTER``.

   **Acceptance Criteria:**

   1. **No ``tools:`` field on any agent except Setup.**
      *Precondition:* The ``feature/remove-tools-frontmatter`` branch is
      checked out; all 14 files in ``syspilot/agents/`` are readable.
      *Action:* Open every agent file's frontmatter block and check for a
      ``tools:`` key.
      *Expected result:* Zero of the 13 non-Setup agent files contain a
      ``tools:`` key — traces to ``SYSP_US_AGENT_ARCH`` AC-6;
      ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-3

   2. **Setup Bootloader retains its explicit tools list.**
      *Precondition:* Same branch checked out.
      *Action:* Open ``syspilot/agents/syspilot.setup.agent.md`` frontmatter.
      *Expected result:* A ``tools:`` key is present and its value includes
      ``agent/runSubagent`` — traces to ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
      AC-10

   3. **Live update removes a stale ``tools:`` field (not overwrite).**
      *Precondition:* A target project with an existing syspilot
      installation where a non-Setup agent file (e.g.
      ``.github/agents/syspilot.cm.agent.md``) still carries a ``tools:``
      field from a prior install.
      *Action:* Re-invoke ``@syspilot.setup`` (update run).
      *Expected result:* After the run, the agent file's frontmatter block
      contains no ``tools:`` key at all (the field is removed, not
      rewritten with a new value) — traces to ``SYSP_US_AGENT_ARCH`` AC-6;
      ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-3

   4. **⚠ Testability-limited — tool inheritance functional claim.**
      *Precondition:* Same branch checked out; ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
      rationale text is readable.
      *Action:* Read the rationale paragraph for design intent; separately,
      a human tester manually confirms (outside syspilot's own test
      harness, using their own VS Code session) that a non-Setup agent
      remains usable with whatever tools are enabled on their default
      agent.
      *Expected result:* The rationale explicitly documents the
      inheritance model and the reason (VS Code tool-picker instability);
      the harness records this as a documentation-verification pass — the
      live functional claim ("agents function correctly using the default
      agent's tool selection") is **not mechanically verifiable by syspilot
      tooling** and is explicitly flagged as such rather than silently
      assumed passed — traces to ``SYSP_US_AGENT_ARCH`` AC-6

   5. **Documentation-presence: ``enthali.jarvis-core`` requirement stated.**
      *Precondition:* The Documentation Engineer has completed the
      ``SYSP_US_DOC_EXTERNAL`` AC-6 documentation update (may not yet be
      true at the time this UAT chain is authored — see note below).
      *Action:* Search the external documentation files for a statement
      that ``enthali.jarvis-core`` must be enabled on the user's default
      VS Code agent for orchestration to work.
      *Expected result:* At least one external documentation file contains
      this statement — traces to ``SYSP_US_DOC_EXTERNAL`` AC-6

      .. note::
         This scenario's execution depends on the Documentation Engineer
         stage of the ``remove-tools-frontmatter`` change, which had not
         yet run when this UAT chain was authored. The scenario is
         included now (forward coverage) so it is ready to execute the
         moment the documentation update lands — it is not itself a spec
         gap.
