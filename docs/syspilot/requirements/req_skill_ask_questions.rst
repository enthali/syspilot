Skill: Ask Questions Requirements
==================================

Requirements for selection menu usage.


.. req:: Selection Menu Usage Criteria
   :id: SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, ask-questions, dx
   :links: SYSP_US_SKILL_ASK_QUESTIONS

   **Description:**
   Agents SHALL use the ``ask_questions`` tool (VS Code quick-pick selection
   menus) for workflow transitions, decisions with 2–6 discrete options, and
   confirmations where alternatives exist.

   Agents SHALL NOT use selection menus for free-form questions requiring
   typed answers or single yes/no confirmations with no meaningful alternatives.

   **Rationale:**
   Selection menus provide structured, discoverable UI for user decisions.
   They reduce ambiguity compared to plain-text numbered lists and ensure
   consistent interaction patterns across all agents.

   **Acceptance Criteria:**

   * AC-1: Workflow transitions (level navigation, agent handoffs) use selection menus
   * AC-2: Decisions with 2–6 discrete options use selection menus
   * AC-3: Confirmations with alternatives (approve / revise / pause) use selection menus
   * AC-4: Free-form questions use normal conversation, not selection menus
   * AC-5: Single yes/no confirmations without meaningful alternatives do not use selection menus


.. req:: Selection Menu Format Constraints
   :id: SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, ask-questions, dx
   :links: SYSP_US_SKILL_ASK_QUESTIONS

   **Description:**
   Each ``ask_questions`` call SHALL contain at most 4 questions, each with
   2–6 options. Related questions SHALL be batched into a single call.

   **Rationale:**
   Limiting questions and options prevents cognitive overload. Batching
   related questions reduces interaction round-trips and keeps the user
   focused on one decision context.

   **Acceptance Criteria:**

   * AC-1: Maximum 4 questions per ``ask_questions`` call
   * AC-2: Each question has 2–6 options
   * AC-3: Every option includes both ``label`` and ``description``
   * AC-4: Related questions are batched into a single call
   * AC-5: The ``recommended`` flag marks the agent's suggested default
