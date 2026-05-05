Skill: Ask Questions
====================

User interaction via selection menus.


.. story:: Selection Menu Interaction
   :id: SYSP_US_SKILL_ASK_QUESTIONS
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, ask-questions, dx
   :links: SYSP_US_SKILL_ARCH

   **As a** syspilot user,
   **I want** agents to present choices via selection menus (quick-pick UI),
   **so that** workflow transitions are clear and consistent.

   **Context:**

   During agent interactions, agents frequently need user decisions — level
   transitions, approvals, conflict resolutions, or option selections.
   Plain-text numbered lists are error-prone and inconsistent. VS Code's
   quick-pick selection menus provide a structured, discoverable UI for
   presenting choices.

   **Acceptance Criteria:**

   1. Given an agent needs a user decision, When presenting discrete options, Then it uses the ``ask_questions`` tool
   2. Given a selection menu, When the user picks an option, Then the agent continues with the selected path
   3. Given a free-form question, When no discrete options exist, Then the agent uses normal conversation instead
   4. Given a single yes/no confirmation, When no meaningful alternatives exist, Then the agent does NOT use selection menus
