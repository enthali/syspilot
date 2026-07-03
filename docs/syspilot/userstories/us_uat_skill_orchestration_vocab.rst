Skill: Orchestration — Agent Vocabulary UAT
===========================================

User Acceptance Test Story for the agent workflow vocabulary migration to the
peer-to-peer three-verb model
(``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB``).


.. story:: UAT: Agent Workflow Vocabulary
   :id: SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB
   :status: draft
   :priority: mandatory
   :tags: uat, skill, orchestration, agent-vocabulary
   :links: SYSP_US_SKILL_ORCHESTRATION

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify every
   product agent document uses the peer-to-peer **SEND / RECEIVE / RESPOND**
   vocabulary and carries the session-identity frontmatter,
   **so that** the orchestration skill can resolve verbs to runtime calls
   without ambiguity, no obsolete INVOKE / DELEGATE / REPLY token survives,
   and every orchestrating agent is a startable Jarvis session.

   **Context:**

   The ``session-first-orchestration`` CR flipped the orchestration default to
   asynchronous session messaging and replaced the old
   INVOKE / DELEGATE / REPLY vocabulary (with its manager-to-engineer routing
   rule) by a **role-agnostic, peer-to-peer** three-verb model:

   * **SEND** — pass work to another agent
   * **RECEIVE** — obtain triggering instructions (first workflow step)
   * **RESPOND** — return a result to the initiator (terminal workflow step)

   There is no separate synchronous verb and no manager / engineer framing in
   the orchestration contract. Any agent may communicate with any other.

   This story covers human verification of that migration across all product
   agents in ``syspilot/agents/``. The Test Designer authors the scenarios;
   a human tester runs them — there is no automated execution step.

   **Artifacts Under Test:**

   All agent files in ``syspilot/agents/``:

   * ``syspilot.cm``, ``syspilot.pm``, ``syspilot.qm``
   * ``syspilot.design``, ``syspilot.uat``, ``syspilot.implement``,
     ``syspilot.mece``, ``syspilot.trace``, ``syspilot.docu``,
     ``syspilot.verify``, ``syspilot.release``
   * Bootstrap layer (excluded from session identity): ``syspilot.setup``,
     ``syspilot.installer``

   **Traceability:**

   Covers the SEND / RECEIVE / RESPOND ACs of
   ``SYSP_US_SKILL_ORCHESTRATION`` and all ACs of
   ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB``,
   ``SYSP_SPEC_UAT_SKILL_ORCHESTRATION_VOCAB``, and the session-identity
   frontmatter ACs of ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` (AC-7, AC-8).

   **Acceptance Criteria:**

   1. **No obsolete vocabulary.**
      *Precondition:* The ``feature/session-first-orchestration`` work is on
      the active branch; the tester has a text-search tool.
      *Action:* Search every file in ``syspilot/agents/`` for the uppercase
      tokens ``INVOKE``, ``DELEGATE``, and ``REPLY`` in workflow prose.
      *Expected result:* Zero matches in any agent's ``## Workflow`` section —
      the obsolete vocabulary is fully removed — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-1

   2. **New vocabulary present and correctly routed.**
      *Precondition:* Each agent file is open at its ``## Workflow`` section.
      *Action:* Read the workflow prose of every agent.
      *Expected result:* Work passed to another agent reads ``SEND``; the
      step that obtains triggering instructions reads ``RECEIVE`` as the
      first step; the step that returns a result reads ``RESPOND`` as the
      terminal step — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-2, AC-3, AC-5

   3. **Peer-to-peer framing.**
      *Precondition:* Each agent file is open.
      *Action:* Scan workflow prose for routing framed by role
      (e.g. "Manager → Engineer", "managers DELEGATE, engineers REPLY",
      or any rule that conditions the verb on the caller's or callee's role).
      *Expected result:* No role-conditioned routing language remains; the
      verb chosen depends only on the action (pass work / receive / return),
      not on who the agents are — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-1

   4. **Session-identity frontmatter.**
      *Precondition:* Each agent file is open at its YAML frontmatter.
      *Action:* Inspect the frontmatter of every agent except
      ``syspilot.setup`` and ``syspilot.installer``.
      *Expected result:* Each carries a human-readable session ``name:`` and
      an ``agent:`` identifier, and declares ``user-invocable: true``; the
      two bootstrap agents carry neither session-identity field — traces to
      ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-7, AC-8

   5. **No concrete runtime tool names.**
      *Precondition:* The tester has the prohibited-pattern reference set
      from ``SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB``.
      *Action:* Search each agent's workflow prose for runtime tool names
      (e.g. ``runSubagent()``, ``jarvis_sendToSession``, ``jarvis_readMessage``,
      "via Jarvis").
      *Expected result:* Zero matches in workflow prose; tool mapping is left
      entirely to the installed orchestration skill — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-4
