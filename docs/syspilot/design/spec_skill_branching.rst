Skill: Branching Design
=======================

Design specifications for the Git branching strategy.


.. spec:: Development Branch Strategy
   :id: SYSP_SPEC_SKILL_BRANCHING_STRATEGY
   :status: draft
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_REQ_SKILL_BRANCHING_CHAINED

   **Definition:**

   syspilot uses a permanent ``development`` integration branch with short-lived
   feature branches:

   ::

      main (v0.2.3) ──────────────────────────── main (v0.2.4)
        │                                          ▲
        │                                          │ squash-merge (release only)
        ▼                                          │
      development ─┬──────────┬──────────────── development
                   │          │
                   │          └─ feature/CR8
                   │               ├── change + specs
                   │               ├── implement
                   │               └── verify
                   │               → squash-merge to development
                   │
                   └─ feature/CR7
                        ├── change + specs
                        ├── implement
                        └── verify
                        → squash-merge to development

   **Workflow Sequence:**

   1. ``@syspilot.design`` creates ``feature/<name>`` from ``development``
   2. ``@syspilot.implement`` commits code on the same branch
   3. ``@syspilot.verify`` commits validation report on the same branch
   4. ``@syspilot.docu`` commits documentation updates on the same branch
   5. Completed feature branch is squash-merged into ``development``
   6. ``@syspilot.release`` squash-merges ``development`` into ``main``, bumps version, tags

   **Key Properties:**

   * One branch per change — isolates each change for independent review
   * ``development`` as integration target — all features merge here
   * Squash-merge everywhere — clean history on ``development`` and ``main``
   * Main = releases only — main always equals the latest release
   * Tag on main — ``v{version}`` tags mark published releases


.. spec:: Branch Permissions
   :id: SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS
   :status: approved
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION; SYSP_REQ_SKILL_BRANCHING_NAMING

   **Definition:**

   Each agent role has specific branching permissions:

   .. list-table:: Branch Permissions
      :header-rows: 1
      :widths: 25 25 50

      * - Agent
        - May create
        - May commit to
      * - ``@syspilot.release``
        - (none)
        - ``main`` (squash merge from ``development`` + tag)
      * - ``@syspilot.design``
        - ``feature/<name>``
        - ``feature/<name>`` (the branch it created)
      * - ``@syspilot.setup``
        - ``update/v{version}``
        - ``update/v{version}`` (the branch it created)
      * - ``@syspilot.implement``
        - (none)
        - current feature branch
      * - ``@syspilot.verify``
        - (none)
        - current feature branch
      * - ``@syspilot.docu``
        - (none)
        - current feature branch
      * - All other engineers
        - (none)
        - current feature branch

   ``development`` is a permanent branch that all feature branches merge into.
   No agent creates ``development`` — it exists permanently.

   **Hard Rule:** If any agent finds itself on ``main`` and needs to make
   changes, it SHALL create a ``feature/<name>`` branch first. No exceptions.


.. spec:: Commit Message Conventions
   :id: SYSP_SPEC_SKILL_BRANCHING_COMMIT_CONVENTIONS
   :status: approved
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_REQ_SKILL_BRANCHING_NAMING

   **Definition:**

   Commit messages follow a Conventional Commits-inspired format:

   ::

      <type>: <short description>

   **Types:**

   .. list-table:: Commit Types
      :header-rows: 1
      :widths: 15 45 40

      * - Type
        - When to use
        - Example
      * - ``feat``
        - New feature or specification
        - ``feat: add branching skill RST specs``
      * - ``fix``
        - Bug fix or correction
        - ``fix: correct traceability link in REQ_123``
      * - ``docs``
        - Documentation changes (non-spec)
        - ``docs: update PM context with CR5 status``
      * - ``chore``
        - Maintenance, cleanup, tooling
        - ``chore: archive v0.2.2 change documents``
      * - ``refactor``
        - Restructuring without behavior change
        - ``refactor: reorganize index.rst toctrees``

   **Rules:**

   * Type is lowercase
   * Description is lowercase, no period at end
   * Keep description under 72 characters
   * Reference spec IDs in description when relevant
