Setup Manager Requirements
===========================


.. req:: Setup Manager Soul
   :id: SYSP_REQ_SETUP_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, soul
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Manager agent (syspilot.setup) SHALL have a Soul that defines it as
   helpful, user-facing, and focused on the first impression. It is a user-invocable
   manager that interacts directly with users.

   **Acceptance Criteria:**

   * AC-1: Setup Manager Soul defines a helpful, user-friendly character
   * AC-2: Setup Manager is user-invocable
   * AC-3: Setup Manager prioritizes a smooth first experience


.. req:: Setup Manager Duties
   :id: SYSP_REQ_SETUP_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, duties
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Manager agent SHALL have Duties covering environment detection,
   installation, updates, configuration, and validation.

   **Acceptance Criteria:**

   * AC-1: Setup Manager can detect install source (local directory or GitHub)
   * AC-2: Setup Manager can detect mode (fresh install or update)
   * AC-3: Setup Manager can install/copy all syspilot files
   * AC-4: Setup Manager can validate setup with sphinx-build
   * AC-5: Setup Manager can create a baseline Git commit


.. req:: Setup Manager Workflow
   :id: SYSP_REQ_SETUP_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, workflow
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Manager agent SHALL follow a workflow from source detection
   through installation to validation and commit.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with detecting install source and mode
   * AC-2: Setup Manager checks dependencies (Python, Sphinx, sphinx-needs)
   * AC-3: Setup Manager installs/updates files and configures the project
   * AC-4: Setup Manager validates with sphinx-build and creates baseline commit


.. req:: Setup Manager Frontmatter Configuration
   :id: SYSP_REQ_SETUP_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup, frontmatter
   :links: SYSP_US_SETUP; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Setup Manager agent SHALL be configured with YAML Agent Frontmatter that
   declares it as a user-invocable manager with editing and execution capabilities.

   **Acceptance Criteria:**

   * AC-1: Setup Manager frontmatter declares ``user-invocable: true``
   * AC-2: Setup Manager frontmatter lists an empty ``agents`` array
   * AC-3: Setup Manager frontmatter includes ``read``, ``edit``, ``search``, ``execute``, ``todo`` in tools


.. req:: Setup Manager Prompt File
   :id: SYSP_REQ_SETUP_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, prompt
   :links: SYSP_US_SETUP; SYSP_REQ_AGENT_ARCH_PROMPT

   **Description:**
   The Setup Manager SHALL have a prompt file ``syspilot.setup.prompt.md`` that
   enables direct user invocation via VS Code Copilot.

   **Acceptance Criteria:**

   * AC-1: File ``syspilot.setup.prompt.md`` exists in the prompts directory
