Skill: Orchestration — Agent Vocabulary Test Data
=================================================

Test data requirements for ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB``.


.. req:: UAT Test Data: Agent Workflow Vocabulary
   :id: SYSP_REQ_UAT_SKILL_ORCHESTRATION_VOCAB
   :status: draft
   :priority: mandatory
   :tags: uat, skill, orchestration, agent-vocabulary, test-data
   :links: SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB``, the
   following test data and preconditions SHALL be available to the human
   tester.

   **Primary Artifacts Under Test:**

   The product agent files in the ``syspilot/agents/`` directory after the
   ``session-first-orchestration`` CR is applied on the branch:

   .. list-table:: Agent Files Under Test
      :header-rows: 1
      :widths: 36 22 42

      * - File
        - Layer
        - Key Expectation
      * - ``syspilot.cm.agent.md``
        - Orchestrating
        - SEND for dispatch; RECEIVE first; RESPOND terminal; ``name:``/``agent:``/``user-invocable: true``
      * - ``syspilot.pm.agent.md``
        - Orchestrating
        - SEND for dispatch; session-identity frontmatter present
      * - ``syspilot.qm.agent.md``
        - Orchestrating
        - SEND to MECE/Trace; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.design.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.uat.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.implement.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.mece.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.trace.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.docu.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.verify.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.release.agent.md``
        - Orchestrating
        - RECEIVE first; RESPOND terminal; session-identity frontmatter present
      * - ``syspilot.setup.agent.md``
        - Bootstrap
        - No INVOKE/DELEGATE/REPLY in workflow prose; NO session-identity frontmatter (excluded)
      * - ``syspilot.installer.agent.md``
        - Bootstrap
        - No INVOKE/DELEGATE/REPLY in workflow prose; NO session-identity frontmatter (excluded)

   **Preconditions:**

   * AC-1: The ``feature/session-first-orchestration`` branch is checked out —
     the scenarios run against the migrated file set
   * AC-2: The tester has read access to ``syspilot/agents/`` in the workspace
   * AC-3: The tester has a text-search tool (e.g. ``grep`` or VS Code search)
     to verify token presence and prohibited-pattern absence

   **Obsolete-Vocabulary Reference Set:**

   The following uppercase verb tokens SHALL NOT appear in the ``## Workflow``
   prose of any agent file. The tester uses these as a search corpus:

   * ``INVOKE``
   * ``DELEGATE``
   * ``REPLY``

   **Prohibited-Tool Reference Set:**

   The following runtime tool names / mechanisms SHALL NOT appear in workflow
   step prose of any agent file:

   * ``runSubagent()``
   * ``jarvis_sendToSession``
   * ``jarvis_readMessage``
   * ``via Jarvis``
   * ``via Jarvis message queue``

   **Role-Framing Reference Set:**

   The following role-conditioned routing phrases SHALL NOT appear in workflow
   prose (the model is peer-to-peer):

   * ``Manager → Engineer``
   * ``Manager → Manager``
   * any rule that selects the verb based on caller or callee role

   **Sensitive-Token Exclusion:**

   ``agent``/``runSubagent`` appearing in YAML frontmatter ``tools:`` or
   ``agents:`` fields is a declaration — it is NOT a prohibited pattern. Only
   ``## Workflow`` step prose is in scope for the prohibited-tool and
   obsolete-vocabulary checks.

   **Acceptance Criteria:**

   * AC-1: All agent files listed in the table above are present in
     ``syspilot/agents/`` at the time the scenarios are run
   * AC-2: The tester can open each file and locate the ``## Workflow``
     section and the YAML frontmatter without consulting external references
   * AC-3: The obsolete-vocabulary, prohibited-tool, and role-framing
     reference sets are available to the tester before they begin
