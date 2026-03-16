Installation & Setup Requirements
==================================

Requirements for bootstrap, portability, installation, adoption, and updates.

**Last Updated**: 2026-03-16


.. req:: Portable Toolkit
   :id: REQ_INST_PORTABLE
   :status: implemented
   :priority: high
   :tags: portability, sync
   :links: US_INST_CROSS_PROJECT, REQ_INST_TEMPLATE_SOURCE

   **Description:**
   syspilot SHALL be a standalone toolkit that can be used across
   multiple projects.

   **Rationale:**
   Enables syspilot to be maintained separately and reused across
   multiple projects.

   **Acceptance Criteria:**

   * AC-1: syspilot is self-contained and portable
   * AC-2: syspilot can be installed into any project

   **Note:** Installation, update, and version tracking covered by
   REQ_INST_NEW_PROJECT through REQ_INST_VERSION_MARKER.


.. req:: Automatic Environment Setup
   :id: REQ_INST_AUTO_SETUP
   :status: implemented
   :priority: high
   :tags: init, automation
   :links: US_INST_BOOTSTRAP, REQ_CORE_SPHINX_NEEDS, REQ_INST_SPHINX_NEEDS_DEP

   **Description:**
   syspilot SHALL provide a curl-based bootstrap to initialize the setup agent,
   which then automatically sets up the sphinx-needs environment.

   **Rationale:**
   Agents running in cloud environments or fresh checkouts need to
   bootstrap their own dependencies without manual intervention.
   A single curl command downloads the setup agent which handles
   everything interactively.

   **Acceptance Criteria:**

   * AC-1: Detect if sphinx-needs is installed
   * AC-2: Install required dependencies automatically
   * AC-3: Create required directory structure
   * AC-4: Validate installation before proceeding
   * AC-5: Bootstrap requires only a single curl/Invoke-WebRequest command


.. req:: syspilot Distribution via GitHub Releases
   :id: REQ_INST_GITHUB_RELEASES
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_REL_CREATE, REQ_REL_GITHUB_PUBLISH

   **Description:**
   syspilot SHALL be distributed via GitHub, with the main branch always
   representing the current release. Users obtain files via curl from
   GitHub raw content. GitHub Releases with semantic versioning provide
   version tags and optional archive downloads.

   **Rationale:**
   Direct curl from main provides the simplest installation path.
   GitHub Releases provides version history, release notes, and
   optional archive downloads as a convenience.

   **Acceptance Criteria:**

   * AC-1: User can identify release versions via GitHub Releases page
   * AC-2: User can download files directly from main via curl
   * AC-3: Installation instructions are included with each release
   * AC-4: Main branch always represents the current release


.. req:: New Project Installation
   :id: REQ_INST_NEW_PROJECT
   :status: implemented
   :priority: mandatory
   :tags: install, new-project
   :links: US_INST_NEW_PROJECT, REQ_INST_TEMPLATE_SOURCE

   **Description:**
   syspilot SHALL be installable into a new project.

   **Rationale:**
   New projects need a straightforward path to adopt syspilot
   from the beginning.

   **Acceptance Criteria:**

   * AC-1: User can invoke syspilot agents after installation
   * AC-2: User can build sphinx-needs documentation after installation
   * AC-3: User receives clear confirmation of successful installation
   * AC-4: Setup agent SHALL fetch distributable files from GitHub main
   * AC-5: Setup agent SHALL NOT require manual path input
   * AC-6: Setup agent SHALL source distributable files from ``templates/`` directory per REQ_INST_TEMPLATE_SOURCE


.. req:: Existing Project Adoption
   :id: REQ_INST_ADOPT_EXISTING
   :status: implemented
   :priority: mandatory
   :tags: install, adoption
   :links: US_INST_ADOPT_EXISTING, REQ_INST_TEMPLATE_SOURCE

   **Description:**
   syspilot SHALL be adoptable into an existing project without data loss.

   **Rationale:**
   Projects already in progress need to adopt syspilot without
   disrupting their existing work.

   **Acceptance Criteria:**

   * AC-1: User's existing documentation is preserved
   * AC-2: User's existing code is preserved
   * AC-3: User is guided through any required decisions
   * AC-4: User can invoke syspilot agents after adoption
   * AC-5: Setup agent SHALL fetch distributable files from GitHub main
   * AC-6: Setup agent SHALL source distributable files from ``templates/`` directory per REQ_INST_TEMPLATE_SOURCE


.. req:: Version Update and Migration
   :id: REQ_INST_VERSION_UPDATE
   :status: implemented
   :priority: mandatory
   :tags: update, migration
   :links: US_INST_UPDATE, REQ_INST_VERSION_MARKER, REQ_INST_TEMPLATE_SOURCE

   **Description:**
   syspilot SHALL be updatable to newer versions.

   **Rationale:**
   Users need to benefit from new features, fixes, and improvements
   over time.

   **Acceptance Criteria:**

   * AC-1: User can determine currently installed version via local version marker and newest available version via GitHub main
   * AC-2: User can update to a newer version
   * AC-3: User's customizations are preserved after update
   * AC-4: User receives migration guidance for breaking changes
   * AC-5: Update SHALL fetch latest version from GitHub main
   * AC-6: Update SHALL source distributable files from ``templates/`` directory per REQ_INST_TEMPLATE_SOURCE


.. req:: Customization Preservation
   :id: REQ_INST_CUSTOM_PRESERVE
   :status: implemented
   :priority: high
   :tags: install, update, preservation
   :links: US_INST_ADOPT_EXISTING, US_INST_UPDATE

   **Description:**
   syspilot SHALL preserve user customizations during adoption and updates.

   **Rationale:**
   Users invest effort in customizing their requirements and configuration.
   This must not be lost during updates.

   **Acceptance Criteria:**

   * AC-1: User-created requirements documents are preserved
   * AC-2: User-modified configuration is preserved
   * AC-3: User can identify what is syspilot core vs user content


.. req:: Sphinx-Needs Mandatory Dependency
   :id: REQ_INST_SPHINX_NEEDS_DEP
   :status: implemented
   :priority: mandatory
   :tags: install, sphinx-needs, dependency
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, REQ_INST_AUTO_SETUP

   **Description:**
   syspilot SHALL declare sphinx-needs and its dependencies as mandatory
   components.

   **Rationale:**
   sphinx-needs provides the traceability infrastructure that syspilot
   relies on. Declaring dependencies explicitly enables automated
   installation by the setup agent (REQ_INST_AUTO_SETUP).

   **Acceptance Criteria:**

   * AC-1: Required dependencies are declared (Python, sphinx, sphinx-needs, furo)
   * AC-2: Optional dependencies are declared (graphviz for diagrams)
   * AC-3: Dependency list is maintained in ``docs/requirements.txt``


.. req:: Installation Version Tracking
   :id: REQ_INST_VERSION_MARKER
   :status: implemented
   :priority: mandatory
   :tags: install, update, version
   :links: US_INST_UPDATE

   **Description:**
   syspilot SHALL store the installed version in the target project so that
   the update process can determine the currently installed version.

   **Rationale:**
   Without a version marker, the update process cannot determine whether
   a newer version is available on GitHub main. The marker enables
   version comparison without requiring the full syspilot repository
   to be present locally.

   **Acceptance Criteria:**

   * AC-1: Installed version is stored persistently in the target project
   * AC-2: Version marker is created during initial installation
   * AC-3: Version marker is updated after each successful update
   * AC-4: Update process can compare local version with remote version


.. req:: Template-First Distribution
   :id: REQ_INST_TEMPLATE_SOURCE
   :status: implemented
   :priority: mandatory
   :tags: install, distribution, templates
   :links: US_INST_AGNOSTIC, US_INST_CROSS_PROJECT

   **Description:**
   syspilot SHALL maintain a ``templates/`` directory as the single source
   for all files distributed to target projects, including the release
   version identifier. The Setup Agent SHALL source all distributable
   files (agents, prompts, skills, scripts, document templates, version
   metadata) from this directory, not from syspilot's own ``.github/``
   or project-specific configuration.

   **Rationale:**
   The syspilot repository is both the product (distributed toolkit) and a
   consumer (dogfooding). Separating the distributable templates from the
   project-specific installation prevents language-specific or
   project-specific content from leaking into distributed files.
   Including ``version.json`` makes ``templates/`` the complete release package.

   **Acceptance Criteria:**

   * AC-1: A ``templates/`` directory SHALL contain all files intended for distribution
   * AC-2: The Setup Agent SHALL source distributable files exclusively from ``templates/``
   * AC-3: syspilot's own ``.github/agents/`` SHALL be a consumer installation (may diverge from templates)
   * AC-4: Template files SHALL be language-agnostic and project-neutral
   * AC-5: The ``templates/`` directory structure SHALL mirror the target project layout
   * AC-6: ``templates/version.json`` SHALL contain the release version


.. req:: Skeleton Implement Agent
   :id: REQ_INST_IMPL_SKELETON
   :status: implemented
   :priority: mandatory
   :tags: install, distribution, agent, skeleton
   :links: US_INST_AGNOSTIC, US_CHG_IMPLEMENT, REQ_INST_TEMPLATE_SOURCE

   **Description:**
   syspilot SHALL distribute an implement agent that contains the
   workflow structure (Read Change Document → Query Needs → Implement →
   Quality Gates → Commit) but no language-specific code examples,
   build commands, or test runner references.

   **Rationale:**
   The implement agent is the only agent that crosses from the specification
   world into the code world. All other agents work with RST/sphinx-needs
   and are inherently project-agnostic. The distributed implement agent
   must use TODO placeholders where project-specific configuration is needed.

   **Acceptance Criteria:**

   * AC-1: Distributed implement agent SHALL contain the full workflow structure
   * AC-2: Build/test/lint commands SHALL use TODO placeholders, not hardcoded commands
   * AC-3: Traceability comment patterns SHALL be language-agnostic (show pattern, not syntax)
   * AC-4: Agent SHALL include clear instructions on what the user needs to customize
   * AC-5: The workflow (Change → Implement → Verify) SHALL remain functional end-to-end with the skeleton


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_INST')
