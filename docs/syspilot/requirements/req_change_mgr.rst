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
   The Change Manager agent SHALL have Duties that guarantee intent translation,
   pipeline completeness, engineer separation, change auditability (PM creates
   document, CM fills engineering sections), merge abstinence (CM never merges),
   and PM readiness notification for every change.

   **Acceptance Criteria:**

   * AC-1: After every completed change, the engineer chain received only well-formulated intent — no raw CR detail leaked to engineers, no engineer detail leaked to the user
   * AC-2: No change reaches ``development`` without having passed through specification, test artifacts, implementation, quality gates, and documentation — the pipeline is never short-circuited
   * AC-3: No engineer session has knowledge of or dependency on another engineer session — each operates in isolation
   * AC-4: At every point during and after a change, the Change Document reflects the true state — PM creates the document by copying the template verbatim and filling header + Summary; CM fills all engineering sections (L0/L1/L2, MECE, Traceability, Sign-off) in-place — CM never creates the document and never replaces the template skeleton
   * AC-5: CM never merges to ``development`` — CM signals readiness to PM; PM performs the merge
   * AC-6: After every completed change, PM has received a readiness notification including the Change Document path and branch name — no change completes silently


.. req:: Change Manager Workflow
   :id: SYSP_REQ_CM_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, cm, workflow
   :links: SYSP_US_CM

   **Description:**
   The Change Manager drives a change through the engineering gates and reports
   its readiness to PM. PM hands over an existing Change Document (the contract)
   on its branch; CM fills the engineering sections, runs the change through the
   gates, triggers a QM review, and returns the change to PM for the merge
   decision. The concrete orchestration flow is specified in
   ``SYSP_SPEC_CM_WORKFLOW``.

   **Acceptance Criteria:**

   * AC-1: CM works on the Change Document and branch handed over by PM
   * AC-2: Every change passes specification, test artifacts, implementation, quality gates, and documentation before it is reported ready
   * AC-3: The true change scope is established by Impact Analysis before spec work begins — the CR file list is treated as a hint
   * AC-4: CM fills the engineering sections of the Change Document in-place; the section structure is owned by the Change Document template
   * AC-5: CM SENDs a quality review of the completed change to QM
   * AC-6: On completion, PM receives a readiness notification (branch and Change Document path) and decides on the merge; CM acts on PM's decision
   * AC-7: CM follows the ``Operation Mode`` declared in the Change Document header; on a conflicting mode in the dispatch message, CM resolves it with the user


.. req:: Change Manager Frontmatter Configuration
   :id: SYSP_REQ_CM_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, cm, frontmatter
   :links: SYSP_US_CM; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Change Manager agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable orchestrator. It declares no ``tools:``
   field.

   **Rationale:**
   The CM is the central workflow hub. It SENDs work to engineer sessions and
   manages change documents using whatever tools are enabled on the user's
   default VS Code agent, including session-messaging (``enthali.jarvis-core/*``) for
   inter-session communication. The CM does not invoke subagents; it omits
   ``agents:`` and carries no ``agent/runSubagent``.

   **Acceptance Criteria:**

   * AC-1: CM frontmatter declares ``user-invocable: true``
   * AC-2: CM frontmatter omits ``agents:`` — it SENDs to engineer sessions
   * AC-3: CM frontmatter declares no ``tools:`` field — it inherits the user's default agent tool selection


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
