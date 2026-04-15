Documentation Engineer Agent
=============================


.. story:: Documentation Engineer Agent
   :id: SYSP_US_DOCU
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, docu, documentation-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Documentation Engineer agent (syspilot.docu) that keeps
   both internal and external documentation in sync with the codebase,
   **so that** copilot-instructions.md, README, methodology docs, and other
   project documentation always reflect the current state of the project.

   **Context:**

   The Documentation Engineer replaces the former Memory Agent. It has two
   duty areas:

   * **Internal docs**: copilot-instructions.md, context.md, naming conventions
   * **External docs**: README, methodology, release notes, architecture, workflows

   Same soul ("keep docs in sync with reality"), different duties.

   **Acceptance Criteria:**

   1. Given codebase changes, When the Documentation Engineer runs, Then it identifies doc gaps
   2. Given internal docs, When updating, Then copilot-instructions.md reflects current project state
   3. Given external docs, When updating, Then README and methodology are current
   4. Given redundant documentation, When detected, Then it is removed or consolidated
