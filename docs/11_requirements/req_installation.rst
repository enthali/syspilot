Installation & Setup Requirements
==================================

Requirements for bootstrap, portability, installation, adoption, and updates.

**Last Updated**: 2026-02-06


.. req:: Portable Toolkit
   :id: REQ_INST_PORTABLE
   :status: implemented
   :priority: high
   :tags: portability, sync
   :links: US_INST_CROSS_PROJECT

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
   REQ_INST_NEW_PROJECT through REQ_INST_AUTO_DETECT.


.. req:: Automatic Environment Setup
   :id: REQ_INST_AUTO_SETUP
   :status: implemented
   :priority: high
   :tags: init, automation
   :links: US_INST_BOOTSTRAP, REQ_CORE_SPHINX_NEEDS

   **Description:**
   syspilot SHALL automatically initialize the sphinx-needs environment
   when it is not available.

   **Rationale:**
   Agents running in cloud environments or fresh checkouts need to
   bootstrap their own dependencies without manual intervention.

   **Acceptance Criteria:**

   * AC-1: Detect if sphinx-needs is installed
   * AC-2: Install required dependencies automatically
   * AC-3: Create required directory structure
   * AC-4: Validate installation before proceeding


.. req:: syspilot Distribution via GitHub Releases
   :id: REQ_INST_GITHUB_RELEASES
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_REL_CREATE

   **Description:**
   syspilot SHALL be distributed via GitHub Releases with semantic versioning.

   **Rationale:**
   GitHub Releases provides versioned distribution with automatic archive
   creation, enabling users to obtain specific versions and track what they
   have installed.

   **Acceptance Criteria:**

   * AC-1: User can identify release versions via GitHub Releases page
   * AC-2: User can download specific version archives (.zip, .tar.gz)
   * AC-3: Installation instructions are included with each release


.. req:: New Project Installation
   :id: REQ_INST_NEW_PROJECT
   :status: implemented
   :priority: mandatory
   :tags: install, new-project
   :links: US_INST_NEW_PROJECT, REQ_INST_AUTO_DETECT

   **Description:**
   syspilot SHALL be installable into a new project.

   **Rationale:**
   New projects need a straightforward path to adopt syspilot
   from the beginning.

   **Acceptance Criteria:**

   * AC-1: User can invoke syspilot agents after installation
   * AC-2: User can build sphinx-needs documentation after installation
   * AC-3: User receives clear confirmation of successful installation
   * AC-4: Setup agent SHALL use REQ_INST_AUTO_DETECT auto-detection to locate syspilot files within the project directory
   * AC-5: Setup agent SHALL NOT require manual path input


.. req:: Existing Project Adoption
   :id: REQ_INST_ADOPT_EXISTING
   :status: implemented
   :priority: mandatory
   :tags: install, adoption
   :links: US_INST_ADOPT_EXISTING, REQ_INST_AUTO_DETECT

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
   * AC-5: Setup agent SHALL use REQ_INST_AUTO_DETECT auto-detection to locate syspilot files within the project directory


.. req:: Version Update and Migration
   :id: REQ_INST_VERSION_UPDATE
   :status: implemented
   :priority: mandatory
   :tags: update, migration
   :links: US_INST_UPDATE, REQ_INST_AUTO_DETECT

   **Description:**
   syspilot SHALL be updatable to newer versions.

   **Rationale:**
   Users need to benefit from new features, fixes, and improvements
   over time.

   **Acceptance Criteria:**

   * AC-1: User can determine currently installed version AND newest available syspilot via REQ_INST_AUTO_DETECT auto-detection
   * AC-2: User can update to a newer version
   * AC-3: User's customizations are preserved after update
   * AC-4: User receives migration guidance for breaking changes
   * AC-5: Update SHALL use newest version found (not oldest cached)


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
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING

   **Description:**
   syspilot SHALL require sphinx-needs and its dependencies as mandatory components,
   and guide the user through installation if not available.

   **Rationale:**
   sphinx-needs provides the traceability infrastructure that syspilot
   relies on. The setup agent assists with dependency installation.

   **Acceptance Criteria:**

   * AC-1: User is informed about required dependencies (Python, sphinx, sphinx-needs, furo)
   * AC-2: User is informed about optional dependencies (graphviz for diagrams)
   * AC-3: Setup agent guides user through installation of missing dependencies
   * AC-4: User can build documentation using sphinx-needs after setup


.. req:: Auto-Detection of syspilot Installation
   :id: REQ_INST_AUTO_DETECT
   :status: implemented
   :priority: mandatory
   :tags: install, autodetect
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_INST_UPDATE

   **Description:**
   syspilot SHALL auto-detect its own location by searching for version.json files
   within the project directory only.

   **Rationale:**
   Release ZIP structure places syspilot in versioned folders (syspilot-X.Y.Z/).
   Manual path input is error-prone and breaks user experience. Auto-detection
   enables seamless installation from arbitrary extraction locations.
   Searching above the project root is a security/correctness risk when the
   download location is outside the workspace.

   **Acceptance Criteria:**

   * AC-1: Search within the project directory (workspace root and subdirectories) for version.json files
   * AC-2: Parse each version.json to extract version number
   * AC-3: When multiple found, select newest semantic version (including pre-release tags)
   * AC-4: Return syspilot root directory (where version.json was found)
   * AC-5: If no version.json found within project directory, inform user and offer to download the latest version from GitHub Releases
   * AC-6: Log all found versions for debugging
   * AC-7: SHALL NOT search above the project root directory


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_INST')
