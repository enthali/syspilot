Generic Agent Workflow Pattern — UAT
=====================================

User Acceptance Test Story for the ``generic-agent-workflow-pattern`` CR.
Covers the tailoring file mechanism: ``SYSP_US_CUSTOM_AGENT_WORKFLOWS`` and
the new AC-6 of ``SYSP_US_AGENT_ARCH``.


.. story:: UAT: Generic Agent Workflow Pattern
   :id: SYSP_US_UAT_GENERIC_AGENT_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: uat, agent-v2, architecture, tailoring
   :links: SYSP_US_CUSTOM_AGENT_WORKFLOWS; SYSP_US_AGENT_ARCH

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   tailoring file mechanism works correctly across all three states (missing,
   empty, present), that setup never overwrites a tailoring file, and that
   the PM workflow skeleton contains zero project-specific nouns,
   **so that** any project can install syspilot without touching agent files
   and the product/instance boundary is demonstrably preserved.

   **Context:**

   The ``generic-agent-workflow-pattern`` CR makes every agent's workflow
   skeleton project-neutral. Project-specific details live in a sibling
   ``syspilot.<name>.tailoring.md`` stored next to the agent in
   ``.github/agents/``. This file is instance-only: setup ships
   ``*.agent.md`` only and never writes ``*.tailoring.md``.

   Three states a tailoring file can be in at runtime:

   * **Missing** — agent must not proceed with assumptions; triggers
     the Tailoring Workflow (detect → interview → author → resume)
   * **Empty** — nothing to tailor; proceed generic
   * **Present with content** — agent reads it for project-specific steps

   This story covers static analysis of the agent and spec files plus the
   behavioral response of the PM agent to each tailoring file state.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.pm.agent.md`` — PM agent implementation
     (modified by Implement phase of this CR)
   * ``docs/syspilot/design/spec_agent_arch.rst`` —
     ``SYSP_SPEC_AGENT_ARCH_WORKFLOW`` (Tailoring File property)
   * ``docs/syspilot/requirements/req_agent_arch.rst`` —
     ``SYSP_REQ_AGENT_ARCH_WORKFLOW`` (AC-6),
     ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` (AC-1 through AC-5)

   **Traceability:**

   Covers ``SYSP_US_CUSTOM_AGENT_WORKFLOWS`` AC-1, AC-2, AC-3;
   ``SYSP_US_AGENT_ARCH`` AC-6;
   ``SYSP_REQ_AGENT_ARCH_WORKFLOW`` AC-6;
   ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-1 through AC-5.

   **Preconditions (all scenarios):**

   The Implement phase has completed and ``syspilot.pm.agent.md`` has been
   updated to match ``SYSP_SPEC_PM_WORKFLOW``. The tester has read access to
   ``.github/agents/`` and a text-search tool.

   **Acceptance Criteria:**

   1. **Agent directs to tailoring file (static).**
      *Precondition:* ``syspilot.pm.agent.md`` is open at its Workflow section.
      *Action:* Read the Preflight block at the top of the Workflow section.
      *Expected result:* The Preflight block contains a sentence directing the
      agent to read ``syspilot.pm.tailoring.md`` and describes the three states
      (missing → run Tailoring Workflow; empty → proceed generic; present →
      use content) — traces to
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-1,
      ``SYSP_US_CUSTOM_AGENT_WORKFLOWS`` AC-2

   2. **Missing tailoring file triggers Tailoring Workflow (behavioural).**
      *Precondition:* No ``syspilot.pm.tailoring.md`` exists in
      ``.github/agents/``; a PM session is started fresh (e.g. via
      ``@syspilot.pm``).
      *Action:* Invoke PM with any routine request (e.g. "what's the project
      backlog?").
      *Expected result:* Before doing any backlog work, PM detects the missing
      tailoring file and enters the Tailoring Workflow: it reports that the
      file is missing, reads the generic PM workflow aloud in the conversation,
      asks the user whether any step needs project-specific clarification, then
      creates ``syspilot.pm.tailoring.md`` (even if empty) before resuming —
      PM does not guess at project-specific values — traces to
      ``SYSP_US_CUSTOM_AGENT_WORKFLOWS`` AC-1,
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-3

   3. **Empty tailoring file → proceed generic (behavioural).**
      *Precondition:* ``syspilot.pm.tailoring.md`` exists and is empty
      (zero-byte file or whitespace only).
      *Action:* Invoke PM with a routine request.
      *Expected result:* PM reads the file during Preflight, finds no
      overrides, and immediately proceeds with the generic workflow steps —
      no interview is triggered, no warning is issued — traces to
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-4

   4. **Setup does not overwrite an existing tailoring file.**
      *Precondition:* ``syspilot.pm.tailoring.md`` exists in ``.github/agents/``
      with project-specific content (e.g. a branch naming clarification). A
      new syspilot release is available.
      *Action:* Run the Setup agent (``@syspilot.setup``) to install the new
      release.
      *Expected result:* After installation, ``syspilot.pm.tailoring.md``
      is unchanged — its content matches the pre-installation state byte for
      byte; the installer does not create, update, or delete
      ``*.tailoring.md`` files — traces to
      ``SYSP_US_CUSTOM_AGENT_WORKFLOWS`` AC-3,
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-2

   5. **PM workflow skeleton is project-neutral (static).**
      *Precondition:* ``syspilot.pm.agent.md`` is open at its Workflow section.
      *Action:* Read each numbered step in the Main Workflow and apply the
      neutrality test: "Would this sentence be true, unchanged, for a
      completely different project (different branch names, different release
      process, different distribution target)?"
      *Expected result:* Every step passes the neutrality test — no hardcoded
      branch name (e.g. ``experimental``, ``development``, ``main``), file
      path, distribution command, registry name, or tool-specific instruction
      appears in any step; references to branching mechanics use the phrase
      "per the ``syspilot.branching`` skill" or equivalent — traces to
      ``SYSP_US_AGENT_ARCH`` AC-6,
      ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` AC-5

   6. **Architecture spec carries Tailoring File property (static).**
      *Precondition:* ``docs/syspilot/design/spec_agent_arch.rst`` is open.
      *Action:* Locate the ``SYSP_SPEC_AGENT_ARCH_WORKFLOW`` node and read
      its property fields.
      *Expected result:* The node includes a **Tailoring File** property that
      describes the mechanism: skeleton directs to a sibling
      ``syspilot.<name>.tailoring.md``; the file may be empty, clarify, or
      override; if missing the agent RESPONDs to PM — traces to
      ``SYSP_REQ_AGENT_ARCH_WORKFLOW`` AC-6
