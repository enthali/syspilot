Documentation
=============

User stories for external and internal documentation artifacts.


.. story:: External Documentation
   :id: SYSP_US_DOC_EXTERNAL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external
   :links: SYSP_US_AGENT_ARCH

   **As a** user or customer,
   **I want to** have up-to-date external documentation (README, methodology,
   architecture, workflows, naming conventions),
   **so that** I can understand and use syspilot.

   **Context:**

   External documentation is the primary entry point for anyone evaluating or
   adopting syspilot. It must accurately reflect the current architecture,
   terminology, and workflows to avoid confusion and reduce onboarding friction.

   **Acceptance Criteria:**

   1. Given the README, When I read it, Then it explains what syspilot is, how to install it, and how to get started
   2. Given methodology.md, When I read it, Then it describes spec-driven development, the specification hierarchy, and agent families
   3. Given architecture.md, When I read it, Then it describes the Product/Installation model and customization approach
   4. Given workflows.md, When I read it, Then it describes the change, quality, and release workflows
   5. Given namingconventions.md, When I read it, Then it defines ID formats, file naming, and theme abbreviations


.. story:: Internal Reference Documentation
   :id: SYSP_US_DOC_INTERNAL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, internal
   :links: SYSP_US_AGENT_ARCH

   **As a** developer or contributor,
   **I want to** have internal reference docs (copilot-instructions) that
   accurately reflect the current architecture,
   **so that** I can contribute effectively.

   **Context:**

   The copilot-instructions.md file is the primary context source for AI agents
   working on the syspilot codebase. It must be kept current with the project
   structure, conventions, and agent system so that AI-assisted development
   produces correct results.

   **Acceptance Criteria:**

   1. Given copilot-instructions.md, When an AI agent reads it, Then it has enough context to understand the project structure
   2. Given copilot-instructions.md, When the agent system changes, Then the file is updated to reflect the new architecture
   3. Given copilot-instructions.md, When I read it, Then it describes the specification hierarchy, agent roles, and development workflow


.. story:: Release Notes
   :id: SYSP_US_DOC_RELEASE_NOTES
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, release-notes
   :links: SYSP_US_AGENT_ARCH

   **As a** stakeholder,
   **I want to** have structured release notes that document each release,
   **so that** I can track what changed between versions.

   **Context:**

   Release notes are the authoritative record of what changed in each version.
   They serve both users (what's new, what to watch out for) and developers
   (which specs were modified, what was added or removed).

   **Acceptance Criteria:**

   1. Given a new release, When I read releasenotes.md, Then the latest version is listed first with date, summary, and changes
   2. Given any release entry, When I read it, Then it lists new features, fixes, and affected spec IDs
   3. Given the release history, When I scan the file, Then entries are in reverse chronological order
