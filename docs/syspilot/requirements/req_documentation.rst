Documentation Requirements
==========================

Requirements for external and internal documentation artifacts.


.. req:: README Documentation
   :id: SYSP_REQ_DOC_README
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external, readme
   :links: SYSP_US_DOC_EXTERNAL

   **Description:**
   The README.md SHALL provide installation instructions, project overview,
   and quick-start guide.

   **Rationale:**
   The README is the first file users encounter. It must convey what syspilot
   is, how to install it, and how to get started within minutes.

   **Acceptance Criteria:**

   * AC-1: README contains a project overview explaining the core value proposition
   * AC-2: README contains platform-specific installation instructions (Linux/Mac, Windows)
   * AC-3: README contains a quick-start section or link to getting started
   * AC-4: README lists available agents with brief descriptions


.. req:: Methodology Documentation
   :id: SYSP_REQ_DOC_METHODOLOGY
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external, methodology
   :links: SYSP_US_DOC_EXTERNAL

   **Description:**
   The methodology.md SHALL describe the spec-driven development approach,
   specification hierarchy, and agent roles.

   **Rationale:**
   The methodology document explains the conceptual framework behind syspilot —
   agent families, product/instance separation, and the three-level specification
   hierarchy. Without it, users cannot understand why syspilot is structured
   the way it is.

   **Acceptance Criteria:**

   * AC-1: Describes spec-driven development as the core approach
   * AC-2: Explains the agent family concept and directory structure
   * AC-3: Defines the specification hierarchy (US → REQ → SPEC)
   * AC-4: Covers ID naming conventions at the framework level


.. req:: Architecture Documentation
   :id: SYSP_REQ_DOC_ARCHITECTURE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external, architecture
   :links: SYSP_US_DOC_EXTERNAL

   **Description:**
   The architecture.md SHALL describe the product architecture and
   customization model.

   **Rationale:**
   The architecture document explains the Product/Installation separation,
   which is the central design decision of syspilot. Users need to understand
   what is generic (Product) vs. what is project-specific (Installed copy)
   to know what they can customize and what gets overwritten on update.

   **Acceptance Criteria:**

   * AC-1: Describes the Product/Installation separation
   * AC-2: Explains the Setup Agent's role in installation
   * AC-3: Documents file ownership (methodology vs. project)
   * AC-4: Provides a concrete example (e.g., Release Agent)


.. req:: Workflows Documentation
   :id: SYSP_REQ_DOC_WORKFLOWS
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external, workflows
   :links: SYSP_US_DOC_EXTERNAL

   **Description:**
   The workflows.md SHALL describe the change, quality, and release workflows.

   **Rationale:**
   Workflows define the development process. Without clear documentation of
   agent sequencing and handoffs, users cannot follow the intended process
   and will invoke agents in the wrong order.

   **Acceptance Criteria:**

   * AC-1: Describes the Change Workflow (design → implement → uat → verify → docu)
   * AC-2: Describes the Quality Workflow (mece, trace)
   * AC-3: Describes the Release Workflow
   * AC-4: Each workflow section lists input, agent steps, and output


.. req:: Naming Conventions Documentation
   :id: SYSP_REQ_DOC_NAMINGCONVENTIONS
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, external, naming
   :links: SYSP_US_DOC_EXTERNAL

   **Description:**
   The namingconventions.md SHALL define ID prefixes, file naming patterns,
   and theme abbreviations.

   **Rationale:**
   Consistent naming is critical for sphinx-needs to resolve links. The naming
   conventions document is the single source of truth for how IDs are formed,
   what themes exist, and how files are named.

   **Acceptance Criteria:**

   * AC-1: Defines the ID format (FAMILY_TYPE_THEME_SLUG)
   * AC-2: Lists family prefixes and type abbreviations
   * AC-3: Covers file and directory naming patterns
   * AC-4: Defines slug guidelines


.. req:: Release Notes Documentation
   :id: SYSP_REQ_DOC_RELEASENOTES
   :status: approved
   :priority: mandatory
   :tags: agent-v2, documentation, release-notes
   :links: SYSP_US_DOC_RELEASE_NOTES

   **Description:**
   The releasenotes.md SHALL document each release with version, date, and
   change summary in reverse chronological order.

   **Rationale:**
   Release notes are the definitive record of what shipped. They allow users
   to assess upgrade impact and developers to trace changes back to specs.

   **Acceptance Criteria:**

   * AC-1: Each release entry has a version number and date
   * AC-2: Each entry has a summary, new features, and fixes section
   * AC-3: Entries reference affected spec IDs where applicable
   * AC-4: Entries are ordered newest-first (reverse chronological)


.. req:: Copilot Instructions Template Guidance
   :id: SYSP_REQ_DOC_COPILOT_INSTRUCTIONS
   :status: approved
   :tags: agent-v2, documentation, internal
   :links: SYSP_US_DOC_INTERNAL

   The copilot-instructions.md is a **project-owned** file. syspilot does
   not prescribe its content. The file SHALL be kept concise (always loaded
   into context), and MAY contain: project identity, tech stack, dev commands,
   safety rules, and pointers to syspilot skills and agents.

   **Rationale:** copilot-instructions is the only context file loaded
   automatically by VS Code Copilot. Its content is project-specific —
   Jarvis setup, branching rules, and team conventions belong to the project,
   not to the syspilot product. syspilot provides guidance on what it could
   contain, not requirements on what it must contain.

   **Acceptance Criteria:**

   1. Given a syspilot installation, When I check .github/, Then copilot-instructions.md exists
   2. Given copilot-instructions.md, When loaded by Copilot, Then it stays concise — no content that belongs in skills or agent files
   3. Given a project using syspilot agents, When I read copilot-instructions.md, Then it references the relevant skills
