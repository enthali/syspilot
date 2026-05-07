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
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, cm, duties
   :links: SYSP_US_CM

   **Description:**
   The Change Manager agent SHALL have Duties that guarantee intent translation,
   pipeline completeness, engineer separation, change traceability, merge authority,
   and PM notification for every change.

   **Acceptance Criteria:**

   * AC-1: After every completed change, the engineer chain received only well-formulated intent — no raw CR detail leaked to engineers, no engineer detail leaked to the user
   * AC-2: No change reaches ``development`` without having passed through specification, test artifacts, implementation, quality gates, and documentation — the pipeline is never short-circuited
   * AC-3: No engineer session has knowledge of or dependency on another engineer session — each operates in isolation
   * AC-4: At every point during and after a change, the Change Document reflects the true state — including after abort or failure
   * AC-5: No merge to ``development`` occurs without explicit PM approval — CM never merges autonomously
   * AC-6: After every completed change, PM has received a post-merge confirmation — no change completes silently


.. req:: Change Manager Workflow
   :id: SYSP_REQ_CM_WORKFLOW
   :status: draft
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
   * AC-10: Before merging to development, CM SHALL request PM's merge approval; CM SHALL only proceed with the merge after PM explicitly approves
   * AC-11: After merging to development, CM SHALL send a post-merge confirmation message to PM via Jarvis containing the merge commit hash and branch name


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
