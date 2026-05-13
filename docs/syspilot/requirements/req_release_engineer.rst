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
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, release, duties
   :links: SYSP_US_RELEASE

   **Description:**
   The Release Engineer agent SHALL have Duties that guarantee versioned
   identification, validation, traceability, version consistency, and clean
   branch separation for every release.

   **Acceptance Criteria:**

   * AC-1: After every successful release, ``main`` carries a tag that uniquely identifies the released state — there is never an untagged release on ``main``
   * AC-2: Nothing reaches ``main`` that has not passed sphinx-build validation with ``-W`` — a failed validation always blocks the release
   * AC-3: After every successful release, all change documents from the release cycle are archived in ``docs/changes/<version>/`` and every archived document has a corresponding entry in release notes — no document is missing
   * AC-4: After every successful release, the version string is identical in the setup agent frontmatter, the Git tag, and the release notes header — there is no version drift
   * AC-5: After every successful release, ``development`` and ``main`` are synchronized — there is no half-state where one branch has content the other lacks


.. req:: Release Engineer Workflow
   :id: SYSP_REQ_RELEASE_WORKFLOW
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, release, workflow
   :links: SYSP_US_RELEASE

   **Description:**
   The Release Engineer agent SHALL follow a workflow that prepares the release
   on ``development`` (archive, version bump, release notes, validation) before
   squash-merging to ``main``, tagging, and back-merging.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with release preparation on ``development`` (archive = scan ``docs/changes/*.md``, version bump, release notes from archived docs, validate)
   * AC-2: Release Engineer reads the current version from the ``version:`` field in ``syspilot/agents/syspilot.setup.agent.md`` and bumps it there
   * AC-3: Release Engineer squash-merges ``development`` to ``main`` after all prep steps pass
   * AC-4: Release Engineer tags ``main``, pushes, and creates GitHub Release
   * AC-5: Release Engineer back-merges ``main`` into ``development`` after tagging
   * AC-6: If squash-merge produces conflicts, resolve with ``-X theirs`` (development wins)
   * AC-7: The Document step uses archived change documents in ``docs/changes/<version>/`` as the explicit source


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
