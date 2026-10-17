Harness-Native Install Requirements
====================================

Requirements ensuring syspilot is installed and updated through each
supported harness's own native mechanism, never via hand-edited
configuration.


.. req:: Harness-Native Install Mechanism
   :id: SYSP_REQ_HARNESS_NATIVE_INSTALL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, installer, native
   :links: SYSP_US_HARNESS_INSTALL; SYSP_REQ_INSTALLER_SCOPE

   **Description:**
    On every production-supported harness, installation SHALL be one remote
    PEP 723 ``uv run --no-project`` command executed in the target Git
    repository root with an explicit ``--harness``. The deterministic runtime
    SHALL create Setup, all Managers and Engineers, Skills, and Commands where
    applicable for only the selected harness, plus the shared stable runtime
    and documentation, without pre-placing Setup or hand-editing configuration.

   **Acceptance Criteria:**

   * AC-1: Given a clean Git repository with Git and ``uv`` available, When
     the remote installer URL is executed through ``uv run --no-project``
     with an explicit ``--harness``, Then installation completes without a
     pre-existing Setup file or a hand-edited personal/global configuration
   * AC-2: Given any explicit production harness token, When installation
     completes, Then Setup, the complete Manager set, Engineer set, Skill set,
     native invocation surfaces, and ``.syspilot/installer.py`` are placed in
     valid project locations for exactly the selected harness and shared
     runtime; no other harness target is written
   * AC-3: Given any Python-related Setup, Installer, shipped-tool, test, or
     Sphinx-validation operation in this feature, When the operation is
     executed or documented, Then ``uv`` is its sole runtime, environment,
     and package entry point; Setup and Installer never invoke bare
     ``python``, ``python3``, ``pip``, ``pip3``, or ``sphinx-build``
   * AC-4: Given a clean project with ``uv`` and Git available, When Setup
     resolves the Installer's Python dependencies, Then dependencies are
     obtained deterministically from version-controlled PEP 723 inline script
     metadata through ``uv run`` without requiring an activated virtual
     environment, globally installed Python packages, or a dependency cache
     inside the target repository
   * AC-5: Given a repository uses multiple supported harnesses, When syspilot
     is installed, Then the command is run separately for each harness and no
     harness is selected by filesystem presence detection
   * AC-6: The production-supported matrix is VS Code GitHub Copilot, Claude Code,
     and OpenCode. Qoder is an experimental, installable harness: its
     required installability evidence is deterministic, checksummed package
     staging; native import and per-harness production clearance for Qoder
     are deferred to a future change.
   * AC-7: Path containment is owned exclusively by
     SYSP_REQ_INSTALLER_DIRECT_OPS; checkpoint scope, restoration, and
     concurrent-change preservation are owned exclusively by
     SYSP_REQ_INSTALLER_ROLLBACK

   * AC-8: Given Claude Code is selected, When native installation
     completes, Then the complete Managers, Engineers, Skills, and native
     invocation surfaces are loadable through that harness's live native
     integration, with isolated per-harness evidence.
   * AC-9: Given Qoder is selected, When installation completes, Then the
     deterministic, checksummed package archive is staged and independently
     verifiable; native in-app loading of its contents is out of scope for
     this change and is deferred to a future change, not silently omitted.

.. req:: Harness-Native Update Flow
   :id: SYSP_REQ_HARNESS_NATIVE_UPDATE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, installer, update
   :links: SYSP_US_HARNESS_INSTALL; SYSP_REQ_SETUP_BOOTLOADER_DUTIES

   **Description:**
    Re-running the same remote deterministic command, or invoking installed
    Setup to run the stable local runtime directly, SHALL give the user the
    selected upstream syspilot behavior without nested agent delegation.

   **Acceptance Criteria:**

   * AC-1: Given a new version of syspilot published upstream, When the same
     remote install command is re-run for a harness, Then the installation is
     updated idempotently to the selected upstream revision
   * AC-2: Given installed Setup, When Setup performs an update, Then it
     directly executes ``uv run --no-project .syspilot/installer.py install``
     with target, harness, repository, and branch inputs and does not invoke
     an Installer agent through Agent, Task, ``runSubagent``, or equivalent
   * AC-3: Given installed Setup starts an update, When control transfers to
     ``.syspilot/installer.py``, Then that stable local runtime is the sole
     authoritative executor and refreshes itself and selected content from
     the requested upstream revision
   * AC-4: Given an explicit upstream branch override, When the native
     install or update flow runs, Then branch propagation and immutable source
     fidelity conform to the normative owner
     SYSP_REQ_INSTALLER_GITHUB_SOURCE
   * AC-5: Given Claude Code is explicitly selected, When native update and
     rollback run, Then assets remain isolated to the selected native tree
     and the harness has independent update and rollback evidence. Given
     Qoder is explicitly selected, When native update and rollback run,
     Then the checksummed package archive is atomically replaced or rolled
     back, isolated to its declared staging path; this is Qoder's complete
     required evidence for this change.

.. req:: Harness Installation Prerequisites
   :id: SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, installer, enablement
   :links: SYSP_US_HARNESS_INSTALL

   **Description:**
    Initial installation SHALL require only a target Git repository, Git, and
    ``uv`` in addition to the selected harness itself. Harness authentication
    SHALL remain an external prerequisite rather than installation logic.

   **Acceptance Criteria:**

   * AC-1: Given a clean target Git repository, When initial installation
     begins, Then no Setup or Installer agent file is pre-placed
   * AC-2: Given Claude Code is selected, When installation or native UAT
     requires its CLI, Then Claude Code CLI installation and authentication are
     documented as external prerequisites and are not performed by syspilot
   * AC-3: Given installation succeeds, When the selected harness reloads its
     project configuration, Then installed Setup is discoverable as the
     primary user-facing update entry point
   * AC-4: Given Claude Code and Qoder external prerequisites, When readiness
     is evaluated, Then Claude Code CLI readiness is evidenced as production
     acceptance and Qoder's external documented UI-import prerequisite is
     disclosed as deferred future scope for this change, without hand-edited
     configuration.

.. req:: Harness Install No Regression
   :id: SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, installer, regression
   :links: SYSP_US_HARNESS_INSTALL

   **Description:**
    Existing VS Code GitHub Copilot installation and update flows and native
    installed files SHALL continue to work after the deterministic install
    entry point replaces bootstrap pre-placement. Methodology behavior is
    owned exclusively by SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION.

   **Acceptance Criteria:**

   * AC-1: Given an existing VS Code GitHub Copilot installation, When this
     CR is implemented and the deterministic update is run, Then its
     installation and update flow and its native files continue without
     regression
   * AC-2: Given the supported harness matrix, When installation and update
     are exercised, Then VS Code GitHub Copilot and OpenCode compatibility is
     separately observable, Claude Code lifecycle acceptance is
     independently evidenced at production parity, and Qoder lifecycle
     acceptance is independently evidenced at the experimental,
     installable tier (deterministic package staging and rollback).
     Methodology behavior is owned by portability no-regression.
