Jarvis Inter-Agent Communication
=================================


.. story:: Jarvis Inter-Agent Communication
   :id: SYSP_US_JARVIS
   :status: draft
   :priority: mandatory
   :tags: agent-v2, infrastructure, jarvis, communication
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** the syspilot manager agents to communicate with each other
   reliably via a defined messaging mechanism,
   **so that** completion notifications, findings reports, and merge
   approval decisions reach the right agent without me needing to relay
   messages manually between agents.

   **Context:**

   Several coordination events in the syspilot workflow require one manager
   agent to send structured information to another without user mediation:

   * CM → PM: change completion notification (Change Document path + summary)
   * CM → QM: targeted check trigger (Change Document path for scope)
   * QM → PM: Findings Report (per-level pass/fail with finding details)
   * CM → PM: post-merge confirmation (commit hash + branch name)
   * PM → CM: merge approval decision (approve / hold + rationale)

   Jarvis is the named mechanism for this inter-agent communication. It is
   a tool (``syspilot_jarvis_tools``) that exposes ``jarvis_sendToSession``
   for sending structured messages between agent sessions. Agents that need
   to send or receive these messages must declare ``syspilot_jarvis_tools``
   in their ``tools:`` frontmatter field.

   **Acceptance Criteria:**

   1. Given CM completes a change, When it notifies PM and QM, Then both agents
      receive the Change Document path and completion summary without user
      intervention
   2. Given QM produces a Findings Report, When routing to PM, Then the report
      reaches PM without user relay
   3. Given PM makes a merge approval decision, When communicating to CM, Then
      CM receives the decision (approve / hold) with rationale
   4. Given CM successfully merges to development, When sending post-merge
      confirmation, Then PM receives merge commit hash and branch name
   5. Given any agent that sends or receives Jarvis messages, When its
      frontmatter is read, Then ``syspilot_jarvis_tools`` is listed in its
      ``tools:`` field
