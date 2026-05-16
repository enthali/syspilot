Skill: Orchestration — Agent Vocabulary UAT
===========================================

User Acceptance Test Story for the agent workflow vocabulary migration
(``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB``).


.. story:: UAT: Agent Workflow Vocabulary
   :id: SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB
   :status: draft
   :priority: mandatory
   :tags: uat, skill, orchestration, agent-vocabulary
   :links: SYSP_US_SKILL_ORCHESTRATION

   **As a** syspilot Test Engineer,
   **I want** to verify that all product agent documents use INVOKE, DELEGATE,
   and REPLY vocabulary consistently in their workflow step prose,
   **so that** the orchestration skill can resolve verb invocations to runtime
   calls without ambiguity and no agent prescribes a concrete runtime tool.

   **Context:**

   Phase 3 of the Skill Architecture rollout migrated all agent workflow step
   prose from concrete tool references (e.g. ``runSubagent()``,
   ``jarvis_sendToSession``, "via Jarvis") to the three-verb model
   (INVOKE / DELEGATE / REPLY).  This test story covers end-to-end verification
   of that migration across all 13 product agents in ``syspilot/agents/``.

   The routing rule is: **Manager → Engineer = INVOKE**;
   **Manager → Manager = DELEGATE**; every callee agent's workflow ends with
   **REPLY**.

   **Artifacts Under Test:**

   All 13 agent files in ``syspilot/agents/``:

   * Manager agents: ``syspilot.cm``, ``syspilot.pm``, ``syspilot.qm``
   * Engineer agents: ``syspilot.design``, ``syspilot.uat``,
     ``syspilot.implement``, ``syspilot.mece``, ``syspilot.trace``,
     ``syspilot.docu``, ``syspilot.verify``, ``syspilot.release``,
     ``syspilot.installer``
   * Bootloader: ``syspilot.setup``

   **Traceability:**

   Covers feature ACs 1–3 of ``SYSP_US_SKILL_ORCHESTRATION`` (INVOKE mapping,
   DELEGATE mapping, REPLY delivery) and all ACs of
   ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` and
   ``SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB``.

   **Acceptance Criteria:**

   1. Given the CM agent (``syspilot.cm.agent.md``) workflow steps,
      When reviewed by a human tester,
      Then each step that calls an engineer subagent uses the word
      ``INVOKE`` (uppercase), each step that notifies PM or QM uses
      ``DELEGATE`` (uppercase), and neither "via Jarvis", "via Jarvis
      message queue", nor any runtime tool name appears in any workflow
      step — traces to ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-1,
      AC-2, AC-4, AC-5

   2. Given the PM agent (``syspilot.pm.agent.md``) workflow steps,
      When reviewed by a human tester,
      Then the step that sends a Change Request to CM uses ``DELEGATE``
      and no concrete tool name appears in any workflow step — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-2, AC-4

   3. Given the QM agent (``syspilot.qm.agent.md``) workflow steps,
      When reviewed by a human tester,
      Then the steps that dispatch MECE and Trace engineers use ``INVOKE``
      and the step that routes the Findings Report to PM uses ``DELEGATE``,
      and no concrete tool name appears in any step — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-1, AC-2, AC-4, AC-5

   4. Given each engineer agent (``syspilot.design``, ``syspilot.uat``,
      ``syspilot.implement``, ``syspilot.mece``, ``syspilot.trace``,
      ``syspilot.docu``, ``syspilot.verify``, ``syspilot.release``,
      ``syspilot.installer``) and the bootloader (``syspilot.setup``),
      When reviewed by a human tester,
      Then every agent whose workflow is invoked by a manager has
      ``REPLY`` (uppercase) as its terminal workflow step — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-3

   5. Given all 13 agent files in ``syspilot/agents/``,
      When searched for prohibited patterns,
      Then no file contains ``runSubagent()``, ``jarvis_sendToSession``,
      or any other runtime tool name within workflow step prose — traces to
      ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` AC-4
