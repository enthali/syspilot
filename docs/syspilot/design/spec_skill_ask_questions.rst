Skill: Ask Questions Design
===========================

Design specifications for the ask_questions tool API and usage rules.


.. spec:: ask_questions Tool API
   :id: SYSP_SPEC_SKILL_ASK_QUESTIONS_API
   :status: approved
   :tags: agent-v2, skill, ask-questions, dx
   :links: SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE; SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT

   **Definition:**

   The ``ask_questions`` tool presents choices via VS Code's quick-pick
   selection menus. It accepts a structured JSON parameter:

   **API Structure:**

   ::

      ask_questions({
        questions: [{
          header: "≤12 chars",          // Quick-pick title, unique ID
          question: "Full context",      // Explains what is being decided
          options: [
            { label: "Option A", description: "Brief detail" },
            { label: "Option B", description: "Brief detail", recommended: true }
          ],
          allowFreeformInput: false      // true when custom response is expected
        }]
      })

   **Parameters:**

   * **header** (string) — Short title (≤12 characters), serves as unique ID
     for the question within the call
   * **question** (string) — Full context explaining what is being decided
   * **options** (array) — List of selectable choices, each with ``label``
     and ``description``
   * **options[].label** (string) — Display text for the option
   * **options[].description** (string) — Brief detail explaining the option
   * **options[].recommended** (boolean, optional) — Marks the agent's
     suggested default; user sees it pre-selected
   * **allowFreeformInput** (boolean) — When ``true``, user may type a
     custom response beyond listed options


.. spec:: ask_questions Usage Rules
   :id: SYSP_SPEC_SKILL_ASK_QUESTIONS_RULES
   :status: approved
   :tags: agent-v2, skill, ask-questions, dx
   :links: SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE; SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT

   **Definition:**

   Five rules govern the use of the ``ask_questions`` tool across all agents:

   1. **``recommended`` marks the default** — The agent sets ``recommended: true``
      on its suggested option. The user sees it pre-selected in the quick-pick UI.

   2. **``allowFreeformInput: true`` for open-ended decisions** — When the user
      may want a custom response beyond the listed options, set this flag to
      allow typed input.

   3. **Max 4 questions, 2–6 options each** — Limits per call to prevent
      cognitive overload and keep interactions focused.

   4. **Batch related questions** — Multiple related decisions go into a single
      ``ask_questions`` call rather than separate sequential calls.

   5. **Every option needs ``label`` + ``description``** — Both fields are
      mandatory. Labels are concise identifiers; descriptions provide context.

   **Common Use Cases:**

   * Level transitions (Change Agent): "Proceed to Level 2" / "Revise Level 1" / "Pause"
   * Approval gates: "Approve and proceed" / "Edit manually" / "Cancel"
   * Conflict resolution: "Keep A" / "Keep B" / "Merge both" (with ``allowFreeformInput: true``)
   * File conflicts (Setup Agent): "Keep mine" / "Use theirs" / "Show diff"
