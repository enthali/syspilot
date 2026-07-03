Skill: Orchestration — Agent Vocabulary Expected Outcomes
=========================================================

Expected outcomes specification for ``SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB``.
This document is the per-agent verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Agent Workflow Vocabulary
   :id: SYSP_SPEC_UAT_SKILL_ORCHESTRATION_VOCAB
   :status: draft
   :priority: mandatory
   :tags: uat, skill, orchestration, agent-vocabulary, expected-outcomes
   :links: SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB

   **Definition:**

   For each agent file in ``syspilot/agents/``, the following outcomes SHALL
   be observable when the peer-to-peer three-verb migration is complete and
   correct. Each scenario is self-contained: a human tester opens the named
   file, performs the action, and confirms the expected result. A check item
   passes when the exact condition is met; it fails otherwise.

   ---

   **TC-VOCAB-ABSENT — Obsolete vocabulary removed (global)**

   *Precondition:* The migrated agent set is on the active branch; a
   text-search tool is available.

   *Action:* Search every file in ``syspilot/agents/`` for the uppercase
   tokens ``INVOKE``, ``DELEGATE``, and ``REPLY``, restricting attention to
   each file's ``## Workflow`` section.

   *Expected result:*

   * [ ] ``INVOKE`` — zero matches in any workflow prose
   * [ ] ``DELEGATE`` — zero matches in any workflow prose
   * [ ] ``REPLY`` — zero matches in any workflow prose

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-1

   ---

   **TC-VOCAB-PRESENT — New vocabulary present per agent (orchestrating)**

   *Precondition:* Each of the eleven orchestrating agents
   (``syspilot.cm``, ``syspilot.pm``, ``syspilot.qm``, ``syspilot.design``,
   ``syspilot.uat``, ``syspilot.implement``, ``syspilot.mece``,
   ``syspilot.trace``, ``syspilot.docu``, ``syspilot.verify``,
   ``syspilot.release``) is open at its ``## Workflow`` section.

   *Action:* Read the workflow prose of each agent and check the verb usage.

   *Expected result:* For every orchestrating agent —

   * [ ] Each step that passes work to another agent reads ``SEND``
     (uppercase)
   * [ ] The step that obtains triggering instructions reads ``RECEIVE`` and
     is the first workflow step
   * [ ] The step that returns a result reads ``RESPOND`` and is the terminal
     workflow step

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-2

   ---

   **TC-VOCAB-PEER — Peer-to-peer framing (global)**

   *Precondition:* Each agent file is open.

   *Action:* Scan workflow prose for role-conditioned routing language.

   *Expected result:*

   * [ ] No occurrence of "Manager → Engineer", "Manager → Manager", or any
     equivalent role-to-role routing arrow
   * [ ] No rule stating that the verb depends on the caller's or callee's
     role — the verb depends only on the action

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-3

   ---

   **TC-VOCAB-FRONTMATTER — Session-identity frontmatter**

   *Precondition:* Each agent file is open at its YAML frontmatter.

   *Action:* Inspect the frontmatter of every agent.

   *Expected result:*

   * [ ] Every agent except ``syspilot.setup`` and ``syspilot.installer``
     carries a human-readable ``name:`` field
   * [ ] Those same agents carry an ``agent:`` identifier field
   * [ ] Those same agents declare ``user-invocable: true``
   * [ ] ``syspilot.setup`` and ``syspilot.installer`` carry NO ``name:`` /
     ``agent:`` session-identity fields (bootstrap layer, excluded)

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-VOCAB-NOTOOLS — No runtime tool names in workflow prose (global)**

   *Precondition:* The prohibited-tool reference set from
   ``SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB`` is at hand.

   *Action:* Search each agent's ``## Workflow`` prose for the prohibited
   tool names.

   *Expected result:*

   * [ ] ``runSubagent()`` — zero matches in workflow prose (frontmatter
     ``tools:`` / ``agents:`` occurrences are out of scope)
   * [ ] ``jarvis_sendToSession`` — zero matches in workflow prose
   * [ ] ``jarvis_readMessage`` — zero matches in workflow prose
   * [ ] "via Jarvis" (any form) — zero matches in workflow prose

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-5

   ---

   **TC-VOCAB-BOOTSTRAP — Bootstrap agents (setup, installer)**

   *Precondition:* ``syspilot.setup.agent.md`` and
   ``syspilot.installer.agent.md`` are open at ``## Workflow``.

   *Action:* Inspect the workflow prose of both bootstrap agents.

   *Expected result:*

   * [ ] Neither contains ``INVOKE``, ``DELEGATE``, or ``REPLY`` in workflow
     prose
   * [ ] The Setup → Installer hand-off is described in tool-agnostic prose;
     ``runSubagent()`` does not appear in workflow prose (it may appear in
     frontmatter ``tools:`` — acceptable)

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-1, AC-5

   ---

   **Testability Note:**

   The runtime mapping of SEND / RECEIVE / RESPOND to concrete call
   mechanisms (verified by ``SYSP_REQ_SKILL_ORCHESTRATION_VERBS``) cannot be
   confirmed by inspecting agent document prose alone — it requires a running
   Copilot session with an orchestration-group skill installed. That behaviour
   is **out of scope for this static text-inspection UAT** and is covered by
   integration testing. The scenarios above verify only the static prose and
   frontmatter compliance of the agent documents.
