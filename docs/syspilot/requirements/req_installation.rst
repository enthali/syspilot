Installation & Setup Requirements
==================================

Requirements for bootstrap, portability, installation, adoption, and updates.

**Last Updated**: 2026-03-16


.. req:: Portable Toolkit
   :id: SYSPILOT_REQ_INST_PORTABLE
   :status: implemented
   :priority: high
   :tags: portability, sync
   :links: SYSPILOT_US_INST_CROSS_PROJECT, SYSPILOT_REQ_INST_TEMPLATE_SOURCE

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
   SYSPILOT_REQ_INST_NEW_PROJECT through SYSPILOT_REQ_INST_VERSION_MARKER.


.. req:: Automatic Environment Setup
   :id: SYSPILOT_REQ_INST_AUTO_SETUP
   :status: implemented
   :priority: high
   :tags: init, automation
   :links: SYSPILOT_US_INST_BOOTSTRAP, SYSPILOT_REQ_CORE_SPHINX_NEEDS, SYSPILOT_REQ_INST_SPHINX_NEEDS_DEP

   **Description:**
   syspilot SHALL provide a curl-based bootstrap to initialize the setup agent,
   which then automatically sets up the sphinx-needs environment.

   **Rationale:**
   Agents running in cloud environments or fresh checkouts need to
   bootstrap their own dependencies without manual intervention.
   A single curl command downloads the setup agent which handles
   everything interactively.

   **Acceptance Criteria:**

   * AC-1: Detect whether sphinx-needs is already available (importable via current Python environment or project scripts)
   * AC-2: If sphinx-needs is NOT available, ask user whether to install via pip/uv OR confirm that a custom mechanism provides access
   * AC-3: Create required directory structure
   * AC-4: Validate installation before proceeding
   * AC-5: Bootstrap requires only a single curl/Invoke-WebRequest command
   * AC-6: If sphinx-needs is already available, skip installation and proceed without prompting to install


.. req:: syspilot Distribution via GitHub Releases
   :id: SYSPILOT_REQ_INST_GITHUB_RELEASES
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_US_REL_CREATE, SYSPILOT_REQ_REL_GITHUB_PUBLISH

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
   :id: SYSPILOT_REQ_INST_NEW_PROJECT
   :status: implemented
   :priority: mandatory
   :tags: install, new-project
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_REQ_INST_TEMPLATE_SOURCE, SYSPILOT_REQ_INST_LOCAL_SOURCE

   **Description:**
   syspilot SHALL be installable into a new project.

   **Rationale:**
   New projects need a straightforward path to adopt syspilot
   from the beginning.

   **Acceptance Criteria:**

   * AC-1: User can invoke syspilot agents after installation
   * AC-2: User can build sphinx-needs documentation after installation
   * AC-3: User receives clear confirmation of successful installation
   * AC-4: Setup agent SHALL fetch distributable files from GitHub main or local ``syspilot/`` directory per SYSPILOT_REQ_INST_LOCAL_SOURCE
   * AC-5: Setup agent SHALL NOT require manual path input
   * AC-6: Setup agent SHALL source distributable files from ``syspilot/`` directory per SYSPILOT_REQ_INST_TEMPLATE_SOURCE


.. req:: Existing Project Adoption
   :id: SYSPILOT_REQ_INST_ADOPT_EXISTING
   :status: implemented
   :priority: mandatory
   :tags: install, adoption
   :links: SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_REQ_INST_TEMPLATE_SOURCE, SYSPILOT_REQ_INST_LOCAL_SOURCE

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
   * AC-5: Setup agent SHALL fetch distributable files from GitHub main or local ``syspilot/`` directory per SYSPILOT_REQ_INST_LOCAL_SOURCE
   * AC-6: Setup agent SHALL source distributable files from ``syspilot/`` directory per SYSPILOT_REQ_INST_TEMPLATE_SOURCE


.. req:: Version Update and Migration
   :id: SYSPILOT_REQ_INST_VERSION_UPDATE
   :status: implemented
   :priority: mandatory
   :tags: update, migration
   :links: SYSPILOT_US_INST_UPDATE, SYSPILOT_REQ_INST_VERSION_MARKER, SYSPILOT_REQ_INST_TEMPLATE_SOURCE, SYSPILOT_REQ_INST_LOCAL_SOURCE

   **Description:**
   syspilot SHALL be updatable to newer versions.

   **Rationale:**
   Users need to benefit from new features, fixes, and improvements
   over time.

   **Acceptance Criteria:**

   * AC-1: User can determine currently installed version via local version marker and newest available version via GitHub main
   * AC-2: User can update to a newer version
   * AC-3: User's customizations are preserved after update per SYSPILOT_REQ_INST_FILE_OWNERSHIP
   * AC-4: User receives migration guidance for breaking changes
   * AC-5: Update SHALL fetch latest version from GitHub main or local ``syspilot/`` directory per SYSPILOT_REQ_INST_LOCAL_SOURCE
   * AC-6: Update SHALL source distributable files from ``syspilot/`` directory per SYSPILOT_REQ_INST_TEMPLATE_SOURCE
   * AC-7: Update SHALL update the setup agent itself first per SYSPILOT_REQ_INST_BOOTSTRAP_SELF


.. req:: Customization Preservation
   :id: SYSPILOT_REQ_INST_CUSTOM_PRESERVE
   :status: implemented
   :priority: high
   :tags: install, update, preservation
   :links: SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_US_INST_UPDATE, SYSPILOT_REQ_INST_FILE_OWNERSHIP

   **Description:**
   syspilot SHALL preserve user customizations during adoption and updates.

   **Rationale:**
   Users invest effort in customizing their requirements and configuration.
   This must not be lost during updates.

   **Acceptance Criteria:**

   * AC-1: User-created requirements documents are preserved
   * AC-2: User-modified configuration is preserved
   * AC-3: User can identify what is syspilot-owned vs project-owned per SYSPILOT_REQ_INST_FILE_OWNERSHIP


.. req:: Sphinx-Needs Mandatory Dependency
   :id: SYSPILOT_REQ_INST_SPHINX_NEEDS_DEP
   :status: implemented
   :priority: mandatory
   :tags: install, sphinx-needs, dependency
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_REQ_INST_AUTO_SETUP

   **Description:**
   syspilot SHALL declare sphinx-needs and its dependencies as mandatory
   components.

   **Rationale:**
   sphinx-needs provides the traceability infrastructure that syspilot
   relies on. Declaring dependencies explicitly enables automated
   installation by the setup agent (SYSPILOT_REQ_INST_AUTO_SETUP).

   **Acceptance Criteria:**

   * AC-1: Required dependencies are declared (Python, sphinx, sphinx-needs, furo)
   * AC-2: Optional dependencies are declared (graphviz for diagrams)
   * AC-3: Dependency list is maintained in ``docs/requirements.txt``
   * AC-4: If sphinx-needs is available via a means other than pip (virtual env, custom scripts, etc.), the setup agent SHALL accept user confirmation as proof of availability and proceed


.. req:: Installation Version Tracking
   :id: SYSPILOT_REQ_INST_VERSION_MARKER
   :status: implemented
   :priority: mandatory
   :tags: install, update, version
   :links: SYSPILOT_US_INST_UPDATE

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
   :id: SYSPILOT_REQ_INST_TEMPLATE_SOURCE
   :status: implemented
   :priority: mandatory
   :tags: install, distribution, templates
   :links: SYSPILOT_US_INST_AGNOSTIC, SYSPILOT_US_INST_CROSS_PROJECT

   **Description:**
   syspilot SHALL maintain a ``syspilot/`` directory as the single source
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
   Including ``version.json`` makes ``syspilot/`` the complete release package.

   **Acceptance Criteria:**

   * AC-1: A ``syspilot/`` directory SHALL contain all files intended for distribution
   * AC-2: The Setup Agent SHALL source distributable files exclusively from ``syspilot/``
   * AC-3: syspilot's own ``.github/agents/`` SHALL be a consumer installation (may diverge from templates)
   * AC-4: Template files SHALL be language-agnostic and project-neutral
   * AC-5: The ``syspilot/`` directory structure SHALL mirror the target project layout
   * AC-6: ``syspilot/version.json`` SHALL contain the release version


.. req:: Skeleton Implement Agent
   :id: SYSPILOT_REQ_INST_IMPL_SKELETON
   :status: implemented
   :priority: mandatory
   :tags: install, distribution, agent, skeleton
   :links: SYSPILOT_US_INST_AGNOSTIC, SYSPILOT_US_CHG_IMPLEMENT, SYSPILOT_REQ_INST_TEMPLATE_SOURCE

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
   * AC-6: Distributed implement and release agents SHALL contain a visible reminder
     to customize via @syspilot.change


.. req:: Setup Agent Self-Update
   :id: SYSPILOT_REQ_INST_BOOTSTRAP_SELF
   :status: implemented
   :priority: mandatory
   :tags: update, bootstrap, setup
   :links: SYSPILOT_US_INST_UPDATE, SYSPILOT_REQ_INST_LOCAL_SOURCE

   **Description:**
   When running in update mode, the Setup Agent SHALL update itself from
   the chosen source (GitHub or local ``syspilot/`` directory per
   SYSPILOT_REQ_INST_LOCAL_SOURCE) before updating any other files.

   **Rationale:**
   The locally installed setup agent may contain outdated update logic.
   By fetching and applying the latest setup agent first, all subsequent
   update operations use the current logic.

   **Acceptance Criteria:**

   * AC-1: Setup agent fetches its own latest version from the chosen source (GitHub or local ``syspilot/``) before any other operation
   * AC-2: If the remote setup agent differs from local, local is replaced immediately
   * AC-3: All subsequent update steps use the newly fetched setup agent logic


.. req:: File Ownership Categories
   :id: SYSPILOT_REQ_INST_FILE_OWNERSHIP
   :status: implemented
   :priority: mandatory
   :tags: update, ownership, install
   :links: SYSPILOT_US_INST_UPDATE, SYSPILOT_US_INST_AGNOSTIC

   **Description:**
   syspilot SHALL define explicit ownership categories for all files it
   manages, determining update behavior for each category.

   **Rationale:**
   The update process must distinguish between files that syspilot owns
   and should replace (methodology agents) and files the project owns
   and should never touch (release, implement agents).

   **Acceptance Criteria:**

   * AC-1: Methodology agents (change, verify, mece, trace, memory, setup) SHALL be
     replaced on every update
   * AC-2: Project-specific agents (release, implement) SHALL be copied on initial
     install but never modified by the update process
   * AC-3: Utility files (scripts, build files, skills, prompts, templates) SHALL be
     replaced on every update
   * AC-4: User content (specs, change docs, copilot-instructions) SHALL never be
     modified by the update process


.. req:: Local Install Source Detection
   :id: SYSPILOT_REQ_INST_LOCAL_SOURCE
   :status: implemented
   :priority: mandatory
   :tags: install, local, dogfooding
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_US_INST_UPDATE

   **Description:**
   The Setup Agent SHALL detect if a ``syspilot/`` directory exists in the
   repository root and, if so, offer the user a choice between installing
   from the local directory or fetching from GitHub.

   **Rationale:**
   When developing syspilot itself (dogfooding) or working from a local fork,
   developers need to test agent changes before pushing to GitHub. A local
   install mode enables this workflow.

   **Acceptance Criteria:**

   * AC-1: Setup Agent SHALL check for ``syspilot/`` directory in repository root
   * AC-2: If ``syspilot/`` exists, Setup Agent SHALL prompt user to choose between local copy and GitHub fetch
   * AC-3: If ``syspilot/`` does not exist, Setup Agent SHALL proceed with GitHub fetch (current behavior)
   * AC-4: Local install SHALL follow the same file ownership rules as GitHub install (methodology=replace, project=skip on update)
   * AC-5: Local install SHALL read from the same ``syspilot/`` directory structure defined by SYSPILOT_REQ_INST_TEMPLATE_SOURCE


.. req:: Post-Update Extension Review
   :id: SYSPILOT_REQ_INST_POST_UPDATE_REVIEW
   :status: implemented
   :priority: mandatory
   :tags: update, review, diff
   :links: SYSPILOT_US_INST_UPDATE, SYSPILOT_REQ_INST_FILE_OWNERSHIP

   **Description:**
   After replacing methodology-owned files during an update, the Setup Agent
   SHALL compare the old version (before replacement) with the new version.
   If the old version contained content not present in the new version
   (beyond whitespace and formatting), the Setup Agent SHALL warn the user
   and present the differences for review.

   **Rationale:**
   Projects may add custom extensions to methodology-owned files (e.g.,
   additional verification steps in the verify agent). These additions are
   silently lost when the file is replaced. A post-update review step
   detects this and lets the user decide how to proceed.

   **Acceptance Criteria:**

   * AC-1: For each replaced methodology-owned file, compare old vs new content
   * AC-2: If old version had content not present in new → flag for user review
   * AC-3: Present flagged files with a summary of what was lost
   * AC-4: User can accept the new version as-is or merge custom content back
   * AC-5: If no methodology-owned files had custom extensions → skip silently


.. req:: Update on Dedicated Branch
   :id: SYSPILOT_REQ_INST_UPDATE_BRANCH
   :status: implemented
   :priority: mandatory
   :tags: update, branch, traceability
   :links: SYSPILOT_US_INST_UPDATE

   **Description:**
   The Setup Agent SHALL perform updates on a dedicated branch and create
   a change document summarizing what was updated, so that changes are
   reviewable and traceable via standard git workflows.

   **Rationale:**
   Performing updates directly on the working branch makes it hard to review
   what changed and to roll back if needed. A dedicated branch with a change
   document provides the same traceability as any other syspilot change.

   **Acceptance Criteria:**

   * AC-1: Update creates a dedicated branch (e.g., ``update/v{version}``)
   * AC-2: A change document is created listing all replaced/updated files
   * AC-3: User can review the branch diff before merging into their working branch
   * AC-4: Change document summarizes version change (old → new) and lists affected files


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('SYSPILOT_REQ_INST')
