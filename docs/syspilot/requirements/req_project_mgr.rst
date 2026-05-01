Project Manager Requirements
=============================


.. req:: Project Manager Soul
   :id: SYSP_REQ_PM_SOUL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, pm, soul
   :links: SYSP_US_PM

   **Description:**
   The Project Manager agent (syspilot.pm) SHALL have a Soul that defines it as a
   strategic, big-picture thinker who communicates with users and plans long-term.

   **Acceptance Criteria:**

   * AC-1: PM Soul defines a strategic, communicative character
   * AC-2: PM never executes technical work directly
   * AC-3: PM always thinks in features, priorities, and roadmaps
   * AC-4: PM Soul encodes a content guardrail: PM always frames outputs in terms of user value and intent; thinking in terms of file paths, code structures, or agent instructions is out of character


.. req:: Project Manager Duties
   :id: SYSP_REQ_PM_DUTIES
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, pm, duties
   :links: SYSP_US_PM

   **Description:**
   The Project Manager agent SHALL have Duties covering feature discussion,
   backlog prioritization, research, and delegation to the Change Manager.

   **Acceptance Criteria:**

   * AC-1: PM can discuss feature ideas with users
   * AC-2: PM can prioritize and maintain a backlog
   * AC-3: PM can conduct research sessions and produce findings
   * AC-4: PM can create Change Requests and delegate to CM
   * AC-5: PM MAY use the impact analysis skill to assess change scope during research or planning
   * AC-6: When authoring a Change Request, PM SHALL restrict content to user intent (WHAT), motivation (WHY), and user-visible acceptance criteria — no file paths, code snippets, agent instructions, or process steps


.. req:: Project Manager Workflow
   :id: SYSP_REQ_PM_WORKFLOW
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, pm, workflow
   :links: SYSP_US_PM

   **Description:**
   The Project Manager agent SHALL follow a workflow from intake through
   research and planning to delegation.

   **Acceptance Criteria:**

   * AC-1: PM workflow starts with user intake (feature idea or question)
   * AC-2: PM conducts research when needed before making recommendations
   * AC-3: PM MAY run impact analysis to understand blast radius before creating a Change Request
   * AC-4: PM produces a structured plan or Change Request as output
   * AC-5: PM delegates execution to Change Manager
   * AC-6: Before delegating to CM, PM SHALL self-check the CR for implementation details and revise if needed


.. req:: Project Manager Frontmatter Configuration
   :id: SYSP_REQ_PM_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, pm, frontmatter
   :links: SYSP_US_PM; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Project Manager agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable strategic planner with broad research tools
   but no engineer subagents.

   **Rationale:**
   The PM needs ``web``, ``github``, and ``context7`` tools for research, and
   ``syspilot_jarvis_tools`` for delegating Change Requests to the CM. It has
   no subagents because it delegates execution, not engineering.

   **Acceptance Criteria:**

   * AC-1: PM frontmatter declares ``user-invocable: true``
   * AC-2: PM frontmatter lists an empty ``agents`` array
   * AC-3: PM frontmatter includes ``web``, ``github``, ``context7`` in tools


.. req:: Project Manager Prompt File
   :id: SYSP_REQ_PM_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, pm, prompt
   :links: SYSP_US_PM; SYSP_REQ_AGENT_ARCH_PROMPT

   **Description:**
   The Project Manager SHALL have a prompt file ``syspilot.pm.prompt.md`` that
   enables direct user invocation via VS Code Copilot.

   **Acceptance Criteria:**

   * AC-1: File ``syspilot.pm.prompt.md`` exists in the prompts directory
   * AC-2: Prompt file references agent ``syspilot.pm``
   * AC-3: User can invoke the PM via the prompt mechanism
