PM Agent — Generic Workflow UAT
================================

User Acceptance Test Story for the PM-specific changes in the
``generic-agent-workflow-pattern`` CR.
Covers PM Duties and PM Workflow as redesigned under ``SYSP_US_PM``.


.. story:: UAT: PM Generic Workflow
   :id: SYSP_US_UAT_PM_GENERIC_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: uat, agent-v2, manager, pm, workflow
   :links: SYSP_US_PM

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the PM
   agent's Duties and Workflow contain zero hardcoded project-specific nouns,
   that the Preflight block handles all three tailoring states, that the
   Tailoring Workflow follows its four-step structure, and that branching
   references use the ``syspilot.branching`` skill name — not a hardcoded
   branch,
   **so that** PM can be installed in any project without editing the agent
   file, and all bindings are in the tailoring file or the branching skill.

   **Context:**

   The ``generic-agent-workflow-pattern`` CR rewrote PM Duties and the PM
   Workflow to remove hardcoded bindings. The key changes:

   * **PM Duties** — Change Initialization, Integration Responsibility, and
     Post-Release Distribution duties had hardcoded branch names, paths, or
     agent names; all replaced with ``syspilot.branching`` skill references
     or generic descriptions (tailoring detail).
   * **PM Workflow** — Gained a Preflight block (read/handle tailoring file)
     and a separate Tailoring Workflow (detect → interview → author → resume).
     The Main Workflow is restructured into three phases: Initiate (steps
     1–9), Review (steps 10–13), Release (steps 14–17).
   * **Branching** — Steps 7 (Create Branch) and 13 (Merge or Loop) now
     reference ``syspilot.branching`` skill; no branch name is hardcoded.
   * **Post-release** — Step 17 is the generic "perform the project's
     post-release distribution"; mechanism is a tailoring detail.

   This story covers both static analysis (reading file content) and
   behavioural verification (invoking the PM agent and observing responses).

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.pm.agent.md`` — PM agent implementation
     (modified by Implement phase of this CR)
   * ``docs/syspilot/design/spec_project_mgr.rst`` —
     ``SYSP_SPEC_PM_DUTIES``, ``SYSP_SPEC_PM_WORKFLOW``
   * ``docs/syspilot/requirements/req_project_mgr.rst`` —
     ``SYSP_REQ_PM_DUTIES``, ``SYSP_REQ_PM_WORKFLOW``

   **Traceability:**

   Covers ``SYSP_REQ_PM_DUTIES`` AC-4, AC-6, AC-8;
   ``SYSP_REQ_PM_WORKFLOW`` AC-6, AC-8, AC-9;
   ``SYSP_SPEC_PM_DUTIES``, ``SYSP_SPEC_PM_WORKFLOW`` (all modified sections).

   **Preconditions (all scenarios):**

   The Implement phase has completed and ``syspilot.pm.agent.md`` has been
   updated to match ``SYSP_SPEC_PM_DUTIES`` and ``SYSP_SPEC_PM_WORKFLOW``.
   The tester has read access to ``.github/agents/`` and a text-search tool.

   **Acceptance Criteria:**

   1. **PM Duties — Change Initialization uses branching skill (static).**
      *Precondition:* ``syspilot.pm.agent.md`` is open at its Duties section.
      *Action:* Locate the Change Initialization duty. Read the branch-creation
      sub-item.
      *Expected result:* The duty states that the feature branch is created
      "per the ``syspilot.branching`` skill" (or equivalent phrasing); no
      concrete branch name (``experimental``, ``development``, ``feature/*``,
      etc.) appears in the duty text — traces to
      ``SYSP_REQ_PM_DUTIES`` AC-4, ``SYSP_SPEC_PM_DUTIES``
      Change Initialization

   2. **PM Duties — Integration Responsibility uses branching skill (static).**
      *Precondition:* ``syspilot.pm.agent.md`` Duties section is open.
      *Action:* Locate the Integration Responsibility duty.
      *Expected result:* The duty references the ``syspilot.branching`` skill
      for the merge operation and contains no hardcoded branch name —
      traces to
      ``SYSP_REQ_PM_DUTIES`` AC-6, ``SYSP_SPEC_PM_DUTIES``
      Integration Responsibility

   3. **PM Duties — Post-Release Distribution is generic (static).**
      *Precondition:* ``syspilot.pm.agent.md`` Duties section is open.
      *Action:* Locate the Post-Release Distribution duty.
      *Expected result:* The duty contains no hardcoded distribution
      mechanism, agent name, or target system; it states only that "the
      project's post-release distribution" is performed and explicitly
      labels the distribution mechanism as a tailoring detail —
      traces to
      ``SYSP_REQ_PM_DUTIES`` AC-8, ``SYSP_SPEC_PM_DUTIES``
      Post-Release Distribution

   4. **PM Workflow Preflight — three-state handling (static).**
      *Precondition:* ``syspilot.pm.agent.md`` is open at its Workflow section.
      *Action:* Read the Preflight block at the top of the Workflow section.
      *Expected result:* The Preflight block explicitly names all three cases:
      (a) file missing → run the Tailoring Workflow;
      (b) file empty → proceed generic;
      (c) file present → use content for project-specific steps.
      No fourth case or default assumption is present — traces to
      ``SYSP_REQ_PM_WORKFLOW`` AC-9, ``SYSP_SPEC_PM_WORKFLOW`` Preflight

   5. **PM Workflow steps 7 and 13 — no hardcoded branch name (static).**
      *Precondition:* ``syspilot.pm.agent.md`` Main Workflow is open.
      *Action:* Locate step 7 (Create Branch) and step 13 (Merge or Loop).
      Read both step texts.
      *Expected result:* Step 7 instructs the PM to create the branch "per
      the ``syspilot.branching`` skill"; no concrete branch name appears.
      Step 13 instructs the PM to merge "per the ``syspilot.branching`` skill"
      (or equivalent); no concrete branch name appears in either step —
      traces to
      ``SYSP_REQ_PM_WORKFLOW`` AC-6, ``SYSP_SPEC_PM_WORKFLOW`` steps 7 and 13

   6. **PM Workflow step 17 — no hardcoded distribution (static).**
      *Precondition:* ``syspilot.pm.agent.md`` Main Workflow Release phase
      is open.
      *Action:* Locate step 17 (Post-Release Distribution) and read its
      text.
      *Expected result:* Step 17 contains no hardcoded command, agent
      invocation, or system name; the text reads "Perform the project's
      post-release distribution" (or equivalent generic phrasing) —
      traces to
      ``SYSP_REQ_PM_WORKFLOW`` AC-8, ``SYSP_SPEC_PM_WORKFLOW`` step 17

   7. **PM Tailoring Workflow — four-step structure (static).**
      *Precondition:* ``syspilot.pm.agent.md`` is open; tester locates the
      Tailoring Workflow section (a separate numbered list after the Main
      Workflow).
      *Action:* Count the steps and read each one.
      *Expected result:* Exactly four steps are present in this order:
      (1) Detect — states that no tailoring file exists for the named agent;
      (2) Interview — PM reads the agent's generic workflow and asks the user
      whether any step needs project-specific clarification;
      (3) Author — PM writes ``syspilot.<name>.tailoring.md`` (may be empty,
      clarify steps, or override them); the file is instance-only and never
      shipped by setup;
      (4) Resume — the agent continues now that its tailoring file exists.
      No step proceeds with assumptions before the file is authored —
      traces to
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING``,
      ``SYSP_SPEC_PM_WORKFLOW`` Tailoring Workflow

   8. **PM Tailoring Workflow — triggered by agent RESPOND (behavioural).**
      *Precondition:* A non-PM agent (e.g. ``syspilot.cm``) is invoked and
      RESPONDs to PM that its tailoring file is missing.
      *Action:* PM receives the RESPOND message. Observe PM's next action.
      *Expected result:* PM enters the Tailoring Workflow for the reporting
      agent (not for itself) — it reads that agent's generic workflow, asks
      the user, and authors ``syspilot.<name>.tailoring.md`` — then
      RESPONDs to the original agent to resume — PM does not escalate or
      ask the user to handle it — traces to
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-3,
      ``SYSP_SPEC_PM_WORKFLOW`` Tailoring Workflow step 2
