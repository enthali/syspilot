Setup Engineer Requirements
============================


.. req:: Setup Engineer Soul
   :id: SYSP_REQ_SETUP_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, setup, soul
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Engineer agent (syspilot.setup) SHALL have a Soul that defines it as
   helpful, user-facing, and focused on the first impression. It is the exception
   among engineers: it interacts directly with users.

   **Acceptance Criteria:**

   * AC-1: Setup Engineer Soul defines a helpful, user-friendly character
   * AC-2: Setup Engineer is user-invocable (exception to engineer rule)
   * AC-3: Setup Engineer prioritizes a smooth first experience


.. req:: Setup Engineer Duties
   :id: SYSP_REQ_SETUP_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, setup, duties
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Engineer agent SHALL have Duties covering environment detection,
   installation, updates, configuration, and validation.

   **Acceptance Criteria:**

   * AC-1: Setup Engineer can detect install source (local directory or GitHub)
   * AC-2: Setup Engineer can detect mode (fresh install or update)
   * AC-3: Setup Engineer can install/copy all syspilot files
   * AC-4: Setup Engineer can validate setup with sphinx-build
   * AC-5: Setup Engineer can create a baseline Git commit


.. req:: Setup Engineer Workflow
   :id: SYSP_REQ_SETUP_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, setup, workflow
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Engineer agent SHALL follow a workflow from source detection
   through installation to validation and commit.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with detecting install source and mode
   * AC-2: Setup Engineer checks dependencies (Python, Sphinx, sphinx-needs)
   * AC-3: Setup Engineer installs/updates files and configures the project
   * AC-4: Setup Engineer validates with sphinx-build and creates baseline commit


.. req:: Setup Engineer Frontmatter Configuration
   :id: SYSP_REQ_SETUP_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, setup, frontmatter
   :links: SYSP_US_SETUP; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Setup Engineer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with editing and execution
   capabilities but no subagents.

   **Rationale:**
   The Setup Engineer installs files and runs sphinx-build for validation.
   It needs ``edit`` and ``execute`` tools. Despite being user-facing (users
   type ``@syspilot.setup``), it is technically a subagent in VS Code terms
   (``user-invocable: false``).

   **Acceptance Criteria:**

   * AC-1: Setup Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Setup Engineer frontmatter lists an empty ``agents`` array
   * AC-3: Setup Engineer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
