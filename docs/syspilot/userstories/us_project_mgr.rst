Project Manager Agent
=====================


.. story:: Project Manager Agent
   :id: SYSP_US_PM
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, pm
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Project Manager agent (syspilot.pm) that handles portfolio
   planning, research, and feature discussions,
   **so that** I have a strategic thinking partner who plans ahead, prioritizes work
   and delegates changes to the Change Manager.

   **Context:**

   The Project Manager is a user-facing Manager agent. It does not execute
   technical work — it thinks strategically, conducts research, discusses
   features with the user, and creates well-defined Change Requests for
   the Change Manager to execute.

   **Acceptance Criteria:**

   1. Given a new feature idea, When I discuss it with PM, Then PM provides structured analysis and recommendations
   2. Given multiple pending features, When I ask PM to prioritize, Then PM produces a ranked backlog
   3. Given a research question, When PM investigates, Then PM produces a research document with findings
   4. Given an approved feature, When PM delegates, Then it creates a Change Request for the Change Manager
   5. Given a feature is ready to delegate, When PM creates the Change Request, Then the CR contains only user intent (WHAT), motivation (WHY), and user-visible acceptance criteria — no implementation details, file paths, code snippets, or agent-level instructions
   6. Given QM has reviewed a completed change, When QM routes findings to PM, Then PM decides whether findings are fixed immediately, deferred to a later release, or accepted as-is
   7. Given PM has made the fix/defer/accept decision, When PM approves the merge, Then PM communicates the approval to CM to proceed with merging to development
