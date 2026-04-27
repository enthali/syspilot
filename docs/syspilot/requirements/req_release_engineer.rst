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
   The Release Engineer agent SHALL have Duties covering version management,
   validation, release notes, change document archival, and Git tagging.

   **Acceptance Criteria:**

   * AC-1: Release Engineer can bump versions following semantic versioning
   * AC-2: Release Engineer can run validation (sphinx-build) before releasing
   * AC-3: Release Engineer can generate and update release notes
   * AC-4: Release Engineer can archive change documents
   * AC-5: Release Engineer can squash-merge ``development`` to ``main``
   * AC-6: Release Engineer can back-merge ``main`` into ``development`` after tagging
   * AC-7: Release Engineer can create Git tags and GitHub Releases


.. req:: Release Engineer Workflow
   :id: SYSP_REQ_RELEASE_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, release, workflow
   :links: SYSP_US_RELEASE

   **Description:**
   The Release Engineer agent SHALL follow a workflow that prepares the release
   on ``development`` (archive, version bump, release notes, validation) before
   squash-merging to ``main``, tagging, and back-merging.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with release preparation on ``development`` (archive, version, release notes, validate)
   * AC-2: Release Engineer reads project-specific release decisions
   * AC-3: Release Engineer squash-merges ``development`` to ``main`` after all prep steps pass
   * AC-4: Release Engineer tags ``main``, pushes, and creates GitHub Release
   * AC-5: Release Engineer back-merges ``main`` into ``development`` after tagging
   * AC-6: If squash-merge produces conflicts, resolve with ``-X theirs`` (development wins)


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
