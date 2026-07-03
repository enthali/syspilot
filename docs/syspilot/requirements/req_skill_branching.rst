Skill: Branching Requirements
=============================

Requirements for the Git branching strategy.


.. req:: Development Integration Branch
   :id: SYSP_REQ_SKILL_BRANCHING_CHAINED
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_US_SKILL_BRANCHING

   **Description:**
   syspilot SHALL use a permanent ``development`` integration branch. Feature
   branches are created from ``development`` and squash-merged back into
   ``development`` when complete. All work — specs, code, tests, docs — is
   committed on the feature branch before merging.

   **Rationale:**
   A permanent integration branch decouples in-progress work from releases.
   Feature branches integrate into ``development`` via squash-merge, keeping
   history clean and enabling independent review per change.

   **Acceptance Criteria:**

   * AC-1: New feature branches are created from ``development``
   * AC-2: All changes (RST specs, code, tests, documentation) are committed on feature branches
   * AC-3: Completed feature branches are squash-merged into ``development``
   * AC-4: ``development`` is always the integration target — not other feature branches


.. req:: Main Branch Protection
   :id: SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_US_SKILL_BRANCHING

   **Description:**
   ONLY ``@syspilot.release`` SHALL commit to, merge to, or push to ``main``.
   No other agent may write to ``main`` under any circumstances.

   **Rationale:**
   Main always equals the latest release. Any non-release commit on main is a
   violation of the release process and could break the version history.

   **Acceptance Criteria:**

   * AC-1: Only ``@syspilot.release`` may commit to ``main``
   * AC-2: Only ``@syspilot.release`` may merge to ``main`` (squash merge from ``development``)
   * AC-3: Only ``@syspilot.release`` may push to ``main``
   * AC-4: If an agent finds itself on ``main``, it SHALL create a feature branch from ``development`` before making changes
   * AC-5: ``development`` → ``main`` merges are squash-merges performed exclusively by ``@syspilot.release``


.. req:: Branch Naming Conventions
   :id: SYSP_REQ_SKILL_BRANCHING_NAMING
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, branching, workflow
   :links: SYSP_US_SKILL_BRANCHING

   **Description:**
   Branches SHALL follow these naming conventions:

   * ``feature/<name>`` — for changes created by ``@syspilot.pm``
   * ``development`` — permanent integration branch
   * ``main`` — releases only, managed by ``@syspilot.release``

   **Rationale:**
   Consistent branch naming makes it immediately clear what type of work a
   branch contains and which agent created it.

   **Acceptance Criteria:**

   * AC-1: Change branches use the ``feature/<name>`` pattern
   * AC-2: No other branch patterns are used
   * AC-3: Branch names use lowercase with hyphens (no underscores or spaces)


.. req:: Feature Branch Retention Policy
   :id: SYSP_REQ_SKILL_BRANCHING_RETENTION
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, branching, workflow, tailoring
   :links: SYSP_US_SKILL_BRANCHING; SYSP_REQ_SKILL_ARCH_TAILORING

   **Description:**
   After a feature branch is squash-merged into ``development`` and a
   release completes, the branching skill SHALL default to retaining the
   branch (not deleting it). Deletion is an explicit per-project opt-in,
   configured via the skill's ``tailoring.md`` per
   SYSP_REQ_SKILL_ARCH_TAILORING — never the default.

   **Rationale:**
   Retained branches are harmless — they cost nothing and preserve
   forensic/bisect history. Silent deletion is a destructive default that
   could surprise a project relying on those branches for reference. This
   mirrors the product's established caution around not destroying
   customer artifacts without explicit configuration.

   **Acceptance Criteria:**

   * AC-1: Absent a tailoring override, feature branches merged into
     ``development`` are retained (not deleted) after a release
   * AC-2: A project MAY opt into deletion of merged feature branches via
     the branching skill's ``tailoring.md``
   * AC-3: The Release Engineer applies this policy at release time — the
     policy itself is owned and defined by the branching skill, not by the
     Release Engineer

