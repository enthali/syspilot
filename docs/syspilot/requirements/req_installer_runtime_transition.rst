Installer Runtime Transition Requirements
=========================================


.. req:: Deprecated Bootloader Manifest Fetch
   :id: SYSP_REQ_SETUP_BOOTLOADER_FETCH
   :status: deprecated
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP; SYSP_REQ_HARNESS_NATIVE_INSTALL; SYSP_REQ_HARNESS_NATIVE_UPDATE

   **Description:**
   This requirement is deprecated. Initial installation executes the remote
   PEP 723 runtime directly, and installed Setup executes the stable local
   runtime; neither flow fetches or interprets ``bootstrap.json``.

   **Replacement:** ``SYSP_REQ_HARNESS_NATIVE_INSTALL`` and
   ``SYSP_REQ_HARNESS_NATIVE_UPDATE``.


.. req:: Deprecated Bootloader Installer Delegation
   :id: SYSP_REQ_SETUP_BOOTLOADER_INVOKE
   :status: deprecated
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP; SYSP_REQ_HARNESS_NATIVE_UPDATE

   **Description:**
   This requirement is deprecated. Setup invokes the deterministic runtime as
   a child process and never calls a native Installer agent.

   **Replacement:** ``SYSP_REQ_HARNESS_NATIVE_UPDATE``.


.. req:: Deprecated Bootloader Version Gate
   :id: SYSP_REQ_SETUP_BOOTLOADER_VERSION
   :status: deprecated
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP; SYSP_REQ_INSTALLER_GITHUB_SOURCE

   **Description:**
   This requirement is deprecated with the bootstrap manifest. Source revision
   selection is governed by ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``.

   **Replacement:** ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``.


.. req:: Installer Agent Internal Surface
   :id: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup, installer
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer agent MAY remain installed as a non-user-invocable diagnostic
   and documentation surface. Correct installation and update SHALL not depend
   on invoking it.

   **Acceptance Criteria:**

   * AC-1: Installer frontmatter declares ``user-invocable: false``
   * AC-2: Installer agent documentation states that deterministic runtime
     execution is authoritative and the agent is not a control-plane dependency
