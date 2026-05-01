Change Manager Agent
====================


.. story:: Change Manager Agent
   :id: SYSP_US_CM
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, cm
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Change Manager agent (syspilot.cm) that orchestrates
   the end-to-end change process,
   **so that** changes flow through a structured pipeline of specialized
   engineers with quality gates, without me needing to invoke each engineer manually.

   **Context:**

   The Change Manager is the central orchestrator. It receives Change Requests
   (from PM or directly from the user), then drives the engineer chain:
   System Designer → Test Engineer → Dev Engineer → Quality checks →
   Release Engineer → Documentation Engineer.

   Engineers are decoupled — they don't know about each other. The Change
   Manager decides sequencing, handles exceptions, and ensures quality gates
   are met before proceeding.

   CM is a process controller — it owns its workflow independently and does not
   follow implementation instructions embedded in a CR. CRs provide intent only;
   CM decides how to execute.

   Change Requests may be processed in ``autonomous`` mode (CM works without
   user feedback, except UAT) or ``user-guided`` mode (user approves each spec
   level before CM proceeds).

   **Acceptance Criteria:**

   1. Given a Change Request, When CM starts processing, Then it invokes the System Designer first
   2. Given the engineer chain, When one engineer completes, Then CM invokes the next engineer
   3. Given a quality gate failure, When an engineer reports issues, Then CM handles the exception
   4. Given all engineers complete, When the change is done, Then CM reports completion with full traceability
   5. Given a completed change, When CM finishes, Then it notifies PM and QM via Jarvis
   6. Given a CR that contains implementation instructions (file paths, code, or step-by-step details), When CM receives it, Then CM reasons about the underlying intent, consults the user to agree on a well-formulated CR, and proceeds — regardless of requested execution mode
   7. Given a conforming CR is accepted, When CM starts processing, Then CM creates a Change Document as its first act, serving as a process log and recovery point for the change
   8. Given all engineering work is complete, When CM is ready to merge to development, Then CM requests PM's merge approval and only merges after PM explicitly approves
