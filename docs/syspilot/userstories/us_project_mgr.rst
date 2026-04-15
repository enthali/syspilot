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
