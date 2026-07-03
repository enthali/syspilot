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

   **Key Properties:**

   * One branch per change — isolates each change for independent review
   * ``development`` as integration target — all features merge here
   * Squash-merge everywhere — clean history on ``development`` and ``main``
   * Main = releases only — main always equals the latest release
   * Tag on main — ``v{version}`` tags mark published releases
   * Back-merge after release — ``git checkout development && git merge main``
     prevents conflicts on next release
   * Conflict guidance — squash-merge conflicts resolve with ``-X theirs``
     (development wins)


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
        - ``main`` (squash merge from ``development`` + tag); ``development`` (prep + back-merge)
      * - ``@syspilot.pm``
        - ``feature/<name>``
        - ``feature/<name>`` (the branch it created)
      * - ``@syspilot.installer``
        - (none)
        - pre-install and final commit on the branch that was checked out
          when invoked (no dedicated branch created)
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
   changes, it SHALL create a ``feature/<name>`` branch from ``development``
   first. No exceptions.


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


.. spec:: Feature Branch Retention Policy
   :id: SYSP_SPEC_SKILL_BRANCHING_RETENTION
   :status: draft
   :tags: agent-v2, skill, branching, workflow, tailoring
   :links: SYSP_REQ_SKILL_BRANCHING_RETENTION; SYSP_SPEC_SKILL_ARCH_TAILORING

   **Definition:**

   After a feature branch is squash-merged into ``development`` and the
   release that includes it completes, the default policy is to **retain**
   the branch (locally and on remote) rather than delete it.

   **Tailoring:**

   A project MAY opt into automatic deletion of merged feature branches by
   stating so in ``.github/skills/syspilot.branching/tailoring.md``, e.g.:

   ::

      Delete feature branches after they are merged into development and
      released — do not retain them.

   Absent such an override, branches are retained indefinitely; retaining
   them costs nothing and preserves forensic/bisect history.

   **Execution:** The Release Engineer applies this policy during its
   Branch Retention workflow step — the policy itself is defined here, not
   in the Release Engineer's own spec.

   **Input:** List of ``feature/*`` branches merged into ``development``
   **Output:** Branches retained (default) or deleted (if tailored) locally and on remote

