Developer Experience Requirements
==================================

Requirements for developer experience, project memory, and process ergonomics.

**Last Updated**: 2026-02-06


.. req:: Project Memory Agent
   :id: REQ_DX_MEMORY_AGENT
   :status: implemented
   :priority: high
   :tags: agent, memory
   :links: US_DX_PROJECT_MEMORY

   **Description:**
   syspilot SHALL provide a memory agent that maintains the project's
   copilot-instructions.md as the codebase evolves.

   **Rationale:**
   Long-term project memory ensures new Copilot sessions have full context.

   **Acceptance Criteria:**

   * AC-1: Agent detects changes in project structure
   * AC-2: Agent updates copilot-instructions.md
   * AC-3: Agent removes outdated information
   * AC-4: Agent documents new patterns and conventions


.. req:: Agent Selection Menus for User Choices
   :id: REQ_DX_AGENT_SELECTION_MENUS
   :status: implemented
   :priority: high
   :tags: agent, ux, developer-experience
   :links: US_DX_AGENT_INTERACTION

   **Description:**
   syspilot agents SHALL use VS Code's ``ask_questions`` tool (quick-pick
   selection menus) when presenting choices to the user during a session.

   **Rationale:**
   Free-text choices require users to type or copy responses, and the
   presentation varies between agents. Using the native selection menu
   provides a consistent, single-click interaction pattern across all agents.

   **Acceptance Criteria:**

   * AC-1: Agents SHALL use the ``ask_questions`` tool when presenting 2 or
     more options to the user
   * AC-2: Each option SHALL include a label and a brief description
   * AC-3: All syspilot agents SHALL follow the same interaction pattern for
     presenting choices
   * AC-4: Free-form input SHALL be enabled (``allowFreeformInput``) when the
     user may want to provide a custom response beyond the listed options


.. req:: Shared Skill Files for Agent Patterns
   :id: REQ_DX_AGENT_SKILL_FILES
   :status: implemented
   :priority: high
   :tags: agent, ux, developer-experience, skills
   :links: US_DX_AGENT_INTERACTION, REQ_DX_AGENT_SELECTION_MENUS

   **Description:**
   syspilot SHALL provide a mechanism for consolidating reusable interaction
   patterns into shared skill files that are available to all agents.

   **Rationale:**
   Without consolidation, reusable patterns (like how to present choices)
   must be duplicated across agent files. Skill files define the pattern
   once and make it available to all agents through a single reference.

   **Acceptance Criteria:**

   * AC-1: Reusable agent patterns SHALL be defined in dedicated skill files
   * AC-2: Skill files SHALL be accessible to all agents without duplication
   * AC-3: Adding a new skill SHALL require minimal configuration
     (single reference point)


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_DX')
