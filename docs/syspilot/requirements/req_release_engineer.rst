Release Engineer Requirements
==============================


.. req:: Release Engineer Soul
   :id: SYSP_REQ_RELEASE_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, release, soul
   :links: SYSP_US_RELEASE

   **Description:**
   The Release Engineer agent (syspilot.release) SHALL have a Soul that defines
   it as process-oriented, careful, and quality-conscious. It ensures nothing
   ships without proper validation.

   **Acceptance Criteria:**

   * AC-1: Release Engineer Soul defines a careful, process-driven character
   * AC-2: Release Engineer never skips validation steps
   * AC-3: Release Engineer never force-pushes or rewrites history


.. req:: Release Engineer Duties
   :id: SYSP_REQ_RELEASE_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, release, duties
   :links: SYSP_US_RELEASE

   **Description:**
   The Release Engineer agent SHALL have Duties that guarantee versioned
   identification, validation, traceability, version consistency, clean
   branch separation, and tailored branch retention for every release.

   **Acceptance Criteria:**

   * AC-1: After every successful release, ``main`` carries a tag that uniquely identifies the released state — there is never an untagged release on ``main``
   * AC-2: Nothing reaches ``main`` that has not passed the project's validation suite (defined by tailoring) — a failed validation always blocks the release, checked before any archival or version-bump step
   * AC-3: After every successful release, all change documents from the release cycle are archived in ``docs/changes/<version>/`` and every archived document has a corresponding entry in release notes — no document is missing
   * AC-4: After every successful release, the version string is identical across the ``docs/changes`` archive folder name, the Git tag, the release notes header, and the project's own version marker (location defined by tailoring) — there is no version drift
   * AC-5: After every successful release, ``development`` and ``main`` are synchronized — there is no half-state where one branch has content the other lacks
   * AC-6: After every successful release, the project's tailored branch-retention policy (owned by the ``syspilot.branching`` skill; default: retain) is applied to all ``feature/*`` branches that have been merged into ``development``


.. req:: Release Engineer Workflow
   :id: SYSP_REQ_RELEASE_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, release, workflow
   :links: SYSP_US_RELEASE; SYSP_REQ_AGENT_WORKFLOW_BINDING; SYSP_REQ_SKILL_BRANCHING_CHAINED; SYSP_REQ_SKILL_BRANCHING_RETENTION

   **Description:**
   The Release Engineer agent SHALL follow a workflow that validates the
   project first, then prepares the release on ``development`` (archive,
   version bump, release notes) before squash-merging to ``main``, tagging,
   and back-merging — with merge mechanics and branch retention delegated
   to the ``syspilot.branching`` skill. The versioning scheme and the
   version-write-target are project-specific tailoring decisions per
   SYSP_REQ_AGENT_WORKFLOW_BINDING — not hardcoded in this requirement or
   the agent.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with validation on ``development`` using the project's tailored validation suite; only after validation passes does release preparation continue (archive, version bump, release notes from archived docs)
   * AC-2: Release Engineer reads the current version from the latest existing ``docs/changes/<version>/`` archive folder, computes the next version using the scheme defined in the tailoring file, and writes it to the project-specific version marker location defined by tailoring
   * AC-3: Release Engineer squash-merges ``development`` to ``main`` after all prep steps pass, per the ``syspilot.branching`` skill's merge mechanics
   * AC-4: Release Engineer tags ``main``, pushes, and creates GitHub Release
   * AC-5: Release Engineer back-merges ``main`` into ``development`` after tagging, per the ``syspilot.branching`` skill
   * AC-6: The Document step uses archived change documents in ``docs/changes/<version>/`` as the explicit source
   * AC-7: After back-merge, Release Engineer applies the project's tailored branch-retention policy (per SYSP_REQ_SKILL_BRANCHING_RETENTION; default: retain) to ``feature/*`` branches fully merged into ``development``
   * AC-8: Before determining the next version, Release Engineer reads its tailoring file for the project's versioning scheme and version-write-target; if the tailoring file is missing, it RESPONDs to PM that tailoring is needed rather than assuming either, per SYSP_REQ_AGENT_WORKFLOW_BINDING


.. req:: Release Engineer Frontmatter Configuration
   :id: SYSP_REQ_RELEASE_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, release, frontmatter
   :links: SYSP_US_RELEASE; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Release Engineer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with editing and execution
   capabilities but no subagents.

   **Rationale:**
   The Release Engineer edits version files, runs validation commands, and
   manages Git operations. It needs ``edit`` and ``execute`` tools but has
   no subagents.

   **Acceptance Criteria:**

   * AC-1: Release Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Release Engineer frontmatter lists an empty ``agents`` array
   * AC-3: Release Engineer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
