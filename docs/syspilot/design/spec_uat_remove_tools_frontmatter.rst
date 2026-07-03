Remove-Tools-Frontmatter Expected Outcomes
==========================================

Expected outcomes specification for ``SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Remove Tools Frontmatter
   :id: SYSP_SPEC_UAT_REMOVE_TOOLS_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: uat, agent-arch, tools, remove-tools-frontmatter, expected-outcomes
   :links: SYSP_REQ_UAT_REMOVE_TOOLS_FRONTMATTER

   **Definition:**

   For each scenario in ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER``, the
   following outcomes SHALL be observable. Each scenario is self-contained:
   the human tester prepares the named fixture (if any), runs the action,
   and confirms the expected result. A check item passes when the exact
   condition is met; it fails otherwise.

   ---

   **TC-RT-NOTOOLS — No ``tools:`` field on non-Setup agents**

   *Precondition:* Branch ``feature/remove-tools-frontmatter`` checked out.

   *Action:* Open every file in ``syspilot/agents/*.agent.md``, inspect the
   YAML frontmatter block, search for a ``tools:`` key.

   *Expected result:*

   * [ ] 14 files are found matching the glob
   * [ ] 13 of the 14 files (every file except ``syspilot.setup.agent.md``)
     contain no ``tools:`` key in their frontmatter
   * [ ] No non-Setup agent file references ``SYSP_SPEC_AGENT_BASE_TOOLSET``
     anywhere in its body

   *Traces to:* ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-1

   ---

   **TC-RT-SETUP — Setup Bootloader keeps explicit tools list**

   *Precondition:* Branch ``feature/remove-tools-frontmatter`` checked out.

   *Action:* Open ``syspilot/agents/syspilot.setup.agent.md`` frontmatter.

   *Expected result:*

   * [ ] A ``tools:`` key is present
   * [ ] The ``tools:`` value includes ``agent/runSubagent``
   * [ ] No other agent file's ``tools:`` field (there should be none) lists
     ``agent/runSubagent``

   *Traces to:* ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-2

   ---

   **TC-RT-UPDATE — Live update removes stale ``tools:`` field**

   *Precondition:* Fixture ``F-STALE-TOOLS`` (target project, completed
   prior install, a non-Setup agent file still carries a ``tools:`` field).

   *Action:* Re-invoke ``@syspilot.setup`` (update run) on the target
   project.

   *Expected result:*

   * [ ] The agent completes without error
   * [ ] The previously-tooled agent file's frontmatter no longer contains
     a ``tools:`` key at all — not an empty list, not a rewritten value,
     the key itself is absent
   * [ ] All other frontmatter fields in that file (``description``,
     ``user-invocable``, session-identity fields) are present and match
     the current upstream file

   *Traces to:* ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-3

   ---

   **TC-RT-DOCTESTABILITY — Tool-inheritance functional claim (testability-limited)**

   *Precondition:* Branch checked out; ``SYSP_REQ_AGENT_ARCH_FRONTMATTER``
   readable.

   *Action:* Read the requirement's rationale paragraph. Separately, in the
   tester's own VS Code session (outside syspilot's own test harness),
   invoke a non-Setup agent and confirm it can use tools enabled on the
   default agent.

   *Expected result:*

   * [ ] The rationale paragraph explicitly states the inheritance model
     and cites VS Code tool-picker instability as the reason
   * [ ] The tester's manual invocation completes without a tool-availability
     error
   * [ ] **Explicitly recorded:** this check is a human-observed, one-off
     confirmation — it is not a repeatable, syspilot-owned automated test,
     because the tool picker's state is outside syspilot's control

   *Traces to:* ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-4

   ---

   **TC-RT-DOCPRESENCE — ``enthali.jarvis-core`` documentation presence**

   *Precondition:* Documentation Engineer has completed the
   ``SYSP_US_DOC_EXTERNAL`` AC-6 update (may be pending at authoring time).

   *Action:* Search ``README.md``, ``docs/architecture.md``,
   ``docs/workflows.md`` (and any other external documentation file) for a
   statement that ``enthali.jarvis-core`` must be enabled on the user's
   default VS Code agent for orchestration to work.

   *Expected result:*

   * [ ] At least one external documentation file contains this statement

   *Traces to:* ``SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER`` AC-5
