Skill: Orchestration
====================

Peer-to-peer agent communication pattern.


.. story:: Consistent Agent Orchestration
   :id: SYSP_US_SKILL_ORCHESTRATION
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ARCH

   **As a** syspilot agent,
   **I want** a defined communication pattern with generic verbs,
   **so that** agent communication is consistent, traceable, and
   independent of the underlying orchestration mechanism.

   **Context:**

   Any syspilot agent may communicate with any other agent — the pattern
   is peer-to-peer and role-agnostic. Without a defined pattern, each agent
   would invent its own communication style, making the system inconsistent,
   hard to debug, and difficult to extend.

   syspilot leverages both asynchronous and synchronous communication
   methods between agents. The orchestration pattern defines three generic
   verbs:

   * **SEND** — pass work to another agent (the installed variant decides
     whether this is asynchronous message delivery or a synchronous call)
   * **RECEIVE** — obtain the instructions that triggered this run (a
     pending inbox message, or the task the agent was started with)
   * **RESPOND** — deliver the result back to the agent that initiated the
     work; the installed variant routes this appropriately

   These verbs are tool-agnostic. The concrete mapping is provided by the
   installed orchestration skill variant.

   **Acceptance Criteria:**

   1. Given any agent that says "SEND", When it dispatches work to another agent, Then the work reaches that agent regardless of the underlying communication mechanism
   2. Given any agent that says "RECEIVE", When it starts a run, Then it obtains the instructions that triggered the run
   3. Given any agent that says "RESPOND", When it completes its work, Then the result reaches the agent that initiated the work
