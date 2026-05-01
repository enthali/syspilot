Change Manager Requirements
============================


.. req:: Change Manager Soul
   :id: SYSP_REQ_CM_SOUL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, cm, soul
   :links: SYSP_US_CM

   **Description:**
   The Change Manager agent (syspilot.cm) SHALL have a Soul that defines it as
   process-oriented, systematic, and quality-conscious — the central orchestrator
   of the change workflow.

   **Acceptance Criteria:**

   * AC-1: CM Soul defines a systematic, process-driven character
   * AC-2: CM never executes engineering work directly
   * AC-3: CM always thinks in workflows, quality gates, and completeness
   * AC-4: CM is the gateway for well-formulated change intent — when a CR contains implementation details, CM treats them as an imprecise expression of intent and works to extract and clarify the true intent before proceeding


.. req:: Change Manager Duties
   :id: SYSP_REQ_CM_DUTIES
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, cm, duties
   :links: SYSP_US_CM

   **Description:**
   The Change Manager agent SHALL have Duties covering the orchestration of
   the engineer chain, quality gate enforcement, and exception handling.

   **Acceptance Criteria:**

   * AC-1: CM can receive Change Requests from PM or user
   * AC-2: CM can invoke engineers in the correct sequence
   * AC-3: CM can enforce quality gates between engineer steps
   * AC-4: CM can handle exceptions and re-route when engineers report issues
   * AC-5: When a CR specifies ``autonomous`` mode, CM SHALL proceed without user feedback (except UAT); when ``user-guided``, CM SHALL request user approval after each spec level
   * AC-6: When a CR contains implementation instructions, CM SHALL reason about the underlying intent and consult the user to clarify it before proceeding — regardless of operation mode
   * AC-7: CM SHALL create a Change Document as the first act after a CR is accepted, before invoking any engineer


.. req:: Change Manager Workflow
   :id: SYSP_REQ_CM_WORKFLOW
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, cm, workflow
   :links: SYSP_US_CM

   **Description:**
   The Change Manager agent SHALL follow a workflow that drives the complete
   change lifecycle through the engineer chain.

   **Acceptance Criteria:**

   * AC-1: CM workflow starts with a Change Request as input
   * AC-2: CM invokes System Designer for analysis
   * AC-3: CM invokes Test Engineer, Dev Engineer, Quality Engineers as needed
   * AC-4: CM invokes Documentation Engineer at the end
   * AC-5: CM reports completion with full traceability
   * AC-6: Upon completion, CM SHALL notify PM and QM via Jarvis message queue
   * AC-7: CM SHALL ensure Impact Analysis is executed before any spec changes — CR file lists are hints, not the complete scope
   * AC-8: Upon receiving a CR, CM SHALL assess its conformance; if it contains implementation instructions, CM SHALL reason about the underlying intent, consult the user to agree on a well-formulated CR, then proceed — regardless of operation mode
   * AC-9: CM SHALL create the Change Document before invoking any engineer


.. req:: Change Manager Frontmatter Configuration
   :id: SYSP_REQ_CM_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, cm, frontmatter
   :links: SYSP_US_CM; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Change Manager agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable orchestrator with access to editing, agent
   invocation, and Jarvis tools.

   **Rationale:**
   The CM is the central workflow hub. It needs the ``agent`` tool to invoke
   all 7 engineer subagents, ``edit`` to manage change documents, and
   ``syspilot_jarvis_tools`` for inter-manager communication.

   **Acceptance Criteria:**

   * AC-1: CM frontmatter declares ``user-invocable: true``
   * AC-2: CM frontmatter lists all 7 engineer subagents in ``agents``
   * AC-3: CM frontmatter includes ``agent`` and ``syspilot_jarvis_tools`` in tools


.. req:: Change Manager Prompt File
   :id: SYSP_REQ_CM_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, cm, prompt
   :links: SYSP_US_CM; SYSP_REQ_AGENT_ARCH_PROMPT

   **Description:**
   The Change Manager SHALL have a prompt file ``syspilot.cm.prompt.md`` that
   enables direct user invocation via VS Code Copilot.

   **Acceptance Criteria:**

   * AC-1: File ``syspilot.cm.prompt.md`` exists in the prompts directory
   * AC-2: Prompt file references agent ``syspilot.cm``
   * AC-3: User can invoke the CM via the prompt mechanism
