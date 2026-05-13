Skill: Branching
================

Git branching rules for syspilot agents.


.. story:: Clear Branching Rules for Agents
   :id: SYSP_US_SKILL_BRANCHING
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_US_SKILL_ARCH

   **As a** syspilot agent,
   **I want** clear branching rules,
   **so that** I know where to commit and what branches to create.

   **Context:**

   Multiple agents operate on the same Git repository, often creating branches,
   committing changes, and merging work. Without clear rules, agents could
   commit to the wrong branch, overwrite each other's work, or violate the
   release-only main branch policy.

   The branching skill defines:

   * The development integration branch model (feature branches from ``development``, squash-merged back)
   * Who may write to which branches
   * Branch naming conventions
   * Commit message conventions

   **Acceptance Criteria:**

   1. Given any agent, When it needs to commit, Then it knows which branch to use
   2. Given ``main``, When any agent other than the release agent attempts to write, Then it is rejected
   3. Given a new change, When starting work, Then the agent creates a ``feature/<name>`` branch from ``development``
   4. Given an agent commits, When writing the message, Then it follows the Conventional Commits format
   5. Given a completed feature branch, When merging back, Then it is squash-merged into ``development``
