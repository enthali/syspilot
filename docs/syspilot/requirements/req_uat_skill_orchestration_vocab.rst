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

   To execute the test scenarios in ``SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB``,
   the following test data and preconditions SHALL be available:

   **Primary Artifacts Under Test:**

   The 13 product agent files in the ``syspilot/agents/`` directory after
   the ``agent-vocabulary-migration`` CR is merged to ``development``:

   .. list-table:: Agent Files Under Test
      :header-rows: 1
      :widths: 40 20 40

      * - File
        - Role
        - Key Vocabulary Expectation
      * - ``syspilot.cm.agent.md``
        - Manager
        - INVOKE for engineers; DELEGATE for PM/QM notifications; no "via Jarvis"
      * - ``syspilot.pm.agent.md``
        - Manager
        - DELEGATE for CM handoff; no concrete tool name in workflow steps
      * - ``syspilot.qm.agent.md``
        - Manager
        - INVOKE for MECE/Trace dispatch; DELEGATE for PM reporting
      * - ``syspilot.design.agent.md``
        - Engineer
        - REPLY as terminal step; INVOKE permitted for advisory MECE call
      * - ``syspilot.uat.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.implement.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.mece.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.trace.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.docu.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.verify.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.release.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.installer.agent.md``
        - Engineer
        - REPLY as terminal step
      * - ``syspilot.setup.agent.md``
        - Bootloader
        - INVOKE for Installer call; no ``runSubagent()`` in workflow step prose

   **Preconditions:**

   * AC-1: The ``feature/agent-vocabulary-migration`` branch is checked out
     or merged to ``development`` — test is executed on the migrated file set
   * AC-2: The tester has read access to ``syspilot/agents/`` in the workspace
   * AC-3: The tester has access to a text search tool (e.g. ``grep`` or
     VS Code search) to verify prohibited pattern absence

   **Prohibited-Pattern Reference Set:**

   The following strings SHALL NOT appear in workflow step prose of any agent
   file.  The tester uses these as a search corpus:

   * ``runSubagent()``
   * ``jarvis_sendToSession``
   * ``via Jarvis``
   * ``via Jarvis message queue``

   **Sensitive-Token Exclusion:**

   ``agent/runSubagent`` appearing in YAML frontmatter ``tools:`` or
   ``agents:`` fields is an agent path declaration — it is NOT a prohibited
   pattern.  Only workflow step prose (Markdown sections under ``## Workflow``)
   is in scope.

   **Acceptance Criteria:**

   * AC-1: All 13 agent files listed in the table above are present in
     ``syspilot/agents/`` at the time of test execution
   * AC-2: The tester can open each file and locate the ``## Workflow``
     section without consulting external references
   * AC-3: The prohibited-pattern reference set is available to the tester
     before execution begins
