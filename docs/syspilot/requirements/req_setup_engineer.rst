Setup Manager Requirements
===========================


.. req:: Setup Bootloader Soul
   :id: SYSP_REQ_SETUP_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, soul, bootloader
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader agent (syspilot.setup) SHALL have a Soul that defines it as
   minimal, reliable, and transparent. It is the stable entry point — user-invocable —
   that delegates all installation work to the Installer subagent.

   **Acceptance Criteria:**

   * AC-1: Setup Bootloader Soul defines a minimal, reliable, transparent character
   * AC-2: Setup Bootloader is user-invocable
   * AC-3: Setup Bootloader never installs files directly — always delegates to Installer


.. req:: Installer Duties
   :id: SYSP_REQ_INSTALLER_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, duties
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Installer agent SHALL have Duties covering environment detection,
   installation, updates, configuration, and validation.

   **Acceptance Criteria:**

   * AC-1: Installer can detect install source (local directory or GitHub)
   * AC-2: Installer can detect mode (fresh install or update)
   * AC-3: Installer can install/copy all syspilot files
   * AC-4: Installer can validate setup with sphinx-build
   * AC-5: Installer can create a baseline Git commit
   * AC-6: Installer can query the user about file customizations before overwriting and guide the user to re-apply them after the update
   * AC-7: During an update, Installer SHALL perform a selective merge on
     agent files: preserve the existing ``tools:`` frontmatter field from the
     instance, and take all other frontmatter fields and body content from the
     product source
   * AC-8: During a fresh install, or when the product introduces an agent that
     does not yet exist in the instance, Installer SHALL copy the agent file
     completely from the product source (including ``tools:``)
   * AC-9: After updating agent files, Installer SHALL inform the user
     which agents were updated and confirm that their ``tools:`` fields were
     preserved


.. req:: Installer Workflow
   :id: SYSP_REQ_INSTALLER_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, workflow
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Installer agent SHALL follow a workflow from source detection
   through installation to validation and commit.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with detecting install source and mode
   * AC-2: Installer checks dependencies (Python, Sphinx, sphinx-needs)
   * AC-3: Installer installs/updates files and configures the project
   * AC-4: Installer validates with sphinx-build and creates baseline commit
   * AC-5: When installed version equals source version, Installer asks user for reinstall confirmation; if declined, aborts gracefully
   * AC-6: Before overwriting files in update mode, Installer asks user whether customizations exist; if yes, records the list and reminds user to re-apply them after the update completes
   * AC-7: During update, Installer SHALL detect the existing ``tools:``
     value in each installed agent file before overwriting it, and re-inject
     the saved value after copying from product source

.. req:: Bootloader Duties
   :id: SYSP_REQ_SETUP_BOOTLOADER_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader, duties
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Setup Bootloader agent (syspilot.setup) SHALL have Duties limited to
   fetching, validating, and invoking the Installer. It SHALL NOT perform
   installation tasks directly.

   **Acceptance Criteria:**

   * AC-1: Bootloader fetches the upstream manifest (bootstrap.json) on every run
   * AC-2: Bootloader validates the manifest version before proceeding
   * AC-3: Bootloader fetches the Installer agent from upstream on every run
   * AC-4: Bootloader invokes the Installer as a subagent
   * AC-5: Bootloader never copies files, validates with sphinx-build, or creates Git commits directly


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
   * AC-4: The setup agent frontmatter SHALL include a ``version:`` field reflecting the installed syspilot version


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


.. req:: Bootloader Fetch Installer
   :id: SYSP_REQ_SETUP_BOOTLOADER_FETCH
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Setup Bootloader SHALL fetch the Installer agent file from the upstream
   repository (GitHub raw URL, ``main`` branch) on every run before invoking it.

   **Acceptance Criteria:**

   * AC-1: Bootloader reads ``syspilot/bootstrap.json`` from upstream to resolve entry point
   * AC-2: Bootloader fetches Installer agent file from the URL resolved via bootstrap.json
   * AC-3: Fetch happens on every Bootloader run (no local caching)


.. req:: Bootloader Invoke Installer
   :id: SYSP_REQ_SETUP_BOOTLOADER_INVOKE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Setup Bootloader SHALL invoke the fetched Installer as a subagent,
   passing through the user's original request context.

   **Acceptance Criteria:**

   * AC-1: Bootloader invokes Installer via runSubagent()
   * AC-2: Bootloader passes user context to Installer subagent


.. req:: Bootloader Version Gate
   :id: SYSP_REQ_SETUP_BOOTLOADER_VERSION
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Setup Bootloader SHALL validate the ``bootstrap_version`` field in the
   upstream manifest. If the manifest version exceeds the Bootloader's supported
   version, the Bootloader SHALL stop with a user-visible error message.

   **Acceptance Criteria:**

   * AC-1: Bootloader extracts ``bootstrap_version`` from the manifest already fetched by the Bootloader Fetch step — no additional upstream read
   * AC-2: If ``bootstrap_version`` > supported version, Bootloader displays a user-visible error and stops
   * AC-3: Error message instructs user to update their Bootloader


.. req:: Installer Not User-Invocable
   :id: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, installer
   :links: SYSP_US_INST_BOOTSTRAP

   **Description:**
   The Installer agent SHALL NOT be directly user-invocable. It is an internal
   subagent invoked exclusively by the Bootloader.

   **Acceptance Criteria:**

   * AC-1: Installer frontmatter declares ``user-invocable: false``
   * AC-2: Installer agent documentation states it is invoked by Bootloader only
