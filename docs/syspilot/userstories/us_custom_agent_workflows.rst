Custom Agent Workflow Tailoring
===============================


.. story:: Custom Agent Workflow Tailoring
   :id: SYSP_US_CUSTOM_AGENT_WORKFLOWS
   :status: draft
   :priority: mandatory
   :tags: agent-v2, architecture, process
   :links: SYSP_US_AGENT_ARCH

   **As a** project owner using syspilot in my own repository,
   **I want** each agent's workflow to be project-neutral by default and
   customizable through a per-agent tailoring file stored next to the agent
   (``syspilot.<name>.tailoring.md``),
   **so that** I can install syspilot without editing agent files, and agents
   that need project-specific steps either read their tailoring file or, if it
   is missing, interview me to create it.

   **Context:**

   Agent workflow skeletons ship as product and contain only generic,
   project-neutral steps. Project-specific details (what step 5 "release"
   means here, branch base, paths) live in a sibling tailoring file. The
   tailoring file may be empty (nothing to tailor — proceed generic), clarify
   a step, or override it. Setup ships ``*.agent.md`` only and never the
   ``*.tailoring.md`` file, so the product/instance boundary holds. This is the
   established session ``context.md`` pattern, promoted to an official,
   predictable per-agent filename.

   **Acceptance Criteria:**

   1. Given a syspilot agent with a generic workflow skeleton, When it is invoked and its ``syspilot.<name>.tailoring.md`` is missing, Then the agent RESPONDs to PM (or, if the agent is PM, triggers its own Tailoring Workflow); PM interviews the user and authors the tailoring file before the agent proceeds — no agent proceeds with assumptions
   2. Given a present tailoring file, When the agent is invoked, Then it reads that file for project-specific steps — no agent (product) file modification is required
   3. Given a syspilot product update that ships new agent versions, When installed, Then existing ``*.tailoring.md`` files are never overwritten — the product/instance boundary is preserved
