Skill: Orchestration — Agent Vocabulary Expected Outcomes
=========================================================

Expected outcomes specification for ``SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB``.
This document is the per-agent verification checklist.


.. spec:: UAT Expected Outcomes: Agent Workflow Vocabulary
   :id: SYSP_SPEC_UAT_SKILL_ORCHESTRATION_VOCAB
   :status: draft
   :priority: mandatory
   :tags: uat, skill, orchestration, agent-vocabulary, expected-outcomes
   :links: SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB

   **Definition:**

   For each agent file in ``syspilot/agents/``, the following specific
   outcomes SHALL be observable when the vocabulary migration is complete
   and correct.

   The tester opens each agent file, locates the ``## Workflow`` section,
   and verifies the checklist items for that agent.  A check item passes
   when the exact condition described is met; it fails otherwise.

   ---

   **TC-CM — syspilot.cm.agent.md (Change Manager)**

   Open ``syspilot/agents/syspilot.cm.agent.md``, navigate to ``## Workflow``.

   * [ ] Step 3 (System Designer dispatch) contains ``INVOKE`` — not "Invoke"
     (lowercase) and not any other synonym
   * [ ] Step 4 (Test Engineer dispatch) contains ``INVOKE``
   * [ ] Step 5 (Dev Engineer dispatch) contains ``INVOKE``
   * [ ] Step 6 (Quality Engineers dispatch) contains ``INVOKE``
   * [ ] Step 7 (Documentation Engineer dispatch) contains ``INVOKE``
   * [ ] The step that notifies PM and QM after merge contains ``DELEGATE``
     — the phrase "via Jarvis message queue" does NOT appear
   * [ ] The Post-Merge Confirmation step contains ``DELEGATE``
     — the phrase "via Jarvis" does NOT appear
   * [ ] No workflow step prose contains ``runSubagent()``,
     ``jarvis_sendToSession``, or "via Jarvis" in any form

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-1

   ---

   **TC-PM — syspilot.pm.agent.md (Project Manager)**

   Open ``syspilot/agents/syspilot.pm.agent.md``, navigate to ``## Workflow``.

   * [ ] The step that sends a Change Request to CM (main workflow step 7)
     contains ``DELEGATE``
   * [ ] The QM Findings Review Workflow step 4 (notify CM of merge decision)
     contains ``DELEGATE``
   * [ ] No workflow step prose contains ``runSubagent()``,
     ``jarvis_sendToSession``, or "via Jarvis" in any form

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-2

   ---

   **TC-QM — syspilot.qm.agent.md (Quality Manager)**

   Open ``syspilot/agents/syspilot.qm.agent.md``, navigate to ``## Workflow``.

   * [ ] Step 3 (MECE Engineer dispatch) contains ``INVOKE``
   * [ ] Step 3 (Trace Engineer dispatch) contains ``INVOKE``
   * [ ] Step 6 (route Findings Report to PM) contains ``DELEGATE``
   * [ ] No workflow step prose contains ``runSubagent()``,
     ``jarvis_sendToSession``, or "via Jarvis" in any form

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-3

   ---

   **TC-DESIGN — syspilot.design.agent.md (System Designer)**

   Open ``syspilot/agents/syspilot.design.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] Any advisory MECE call step (if present) contains ``INVOKE``
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-UAT — syspilot.uat.agent.md (Test Engineer)**

   Open ``syspilot/agents/syspilot.uat.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-IMPLEMENT — syspilot.implement.agent.md (Dev Engineer)**

   Open ``syspilot/agents/syspilot.implement.agent.md``, navigate to
   ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-MECE — syspilot.mece.agent.md (MECE Engineer)**

   Open ``syspilot/agents/syspilot.mece.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-TRACE — syspilot.trace.agent.md (Trace Engineer)**

   Open ``syspilot/agents/syspilot.trace.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-DOCU — syspilot.docu.agent.md (Documentation Engineer)**

   Open ``syspilot/agents/syspilot.docu.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-VERIFY — syspilot.verify.agent.md (Verify Engineer)**

   Open ``syspilot/agents/syspilot.verify.agent.md``, navigate to ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-RELEASE — syspilot.release.agent.md (Release Engineer)**

   Open ``syspilot/agents/syspilot.release.agent.md``, navigate to
   ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-INSTALLER — syspilot.installer.agent.md (Installer)**

   Open ``syspilot/agents/syspilot.installer.agent.md``, navigate to
   ``## Workflow``.

   * [ ] The final step of the workflow is ``REPLY`` (uppercase)
   * [ ] No workflow step prose contains a prohibited pattern

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4

   ---

   **TC-SETUP — syspilot.setup.agent.md (Setup Bootloader)**

   Open ``syspilot/agents/syspilot.setup.agent.md``, navigate to ``## Workflow``.

   * [ ] The step that invokes the Installer subagent contains ``INVOKE``
   * [ ] The phrase ``runSubagent()`` does NOT appear in workflow step prose
     (it may appear in YAML frontmatter ``tools:`` — this is acceptable)
   * [ ] No other prohibited pattern appears in workflow step prose

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-4, AC-5

   ---

   **TC-GREP — Global Prohibited-Pattern Sweep**

   Using a workspace-wide text search (grep, VS Code search, or equivalent):

   * [ ] Search for ``runSubagent()`` in ``syspilot/agents/`` scoped to
     lines that are NOT in YAML frontmatter → zero matches in workflow prose
   * [ ] Search for ``jarvis_sendToSession`` in ``syspilot/agents/`` → zero
     matches anywhere in workflow step prose
   * [ ] Search for ``via Jarvis`` in ``syspilot/agents/`` → zero matches
     anywhere in workflow step prose

   *Traces to:* ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB`` AC-5

   ---

   **Testability Note:**

   AC-1 of ``SYSP_US_SKILL_ORCHESTRATION`` ("the installed orchestration
   skill maps INVOKE to a concrete call mechanism") cannot be verified by
   inspecting agent document prose alone.  It requires a running Copilot
   session with the orchestration skill installed.  This AC is declared
   **out of scope for static text-inspection UAT** and deferred to
   integration testing.  The scenarios above cover only the static prose
   compliance aspect.
