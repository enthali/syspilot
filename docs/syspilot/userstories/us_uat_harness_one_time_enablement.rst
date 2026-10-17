Harness One-Time Enablement UAT
===============================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT``.


.. story:: UAT: Harness One-Time Enablement
   :id: SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT
   :status: approved
   :priority: mandatory
   :tags: uat, harness, bootstrap, update, portability
   :links: SYSP_US_HARNESS_INSTALL, SYSP_US_SETUP

   **As a** syspilot Test Designer,
   **I want** a human tester to install and update syspilot through the remote
   or installed deterministic runtime,
   **so that** installation does not depend on pre-placed or nested agents.

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT``,
   ``SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT``, and
   ``SYSP_REQ_HARNESS_NATIVE_UPDATE``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT``; expected outcomes are
   defined in ``SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT``.

   **Acceptance Criteria:**

   1. The same remote raw-URL ``uv run --no-project`` command mechanism,
      invoked separately with an explicit harness selection each time (per
      ``SYSP_US_HARNESS_INSTALL`` AC5), clean-installs each
      production-parity harness (VS Code GitHub Copilot, OpenCode, and
      Claude Code) without a pre-existing Setup file; each passes
      independently. The same command mechanism, invoked with the
      ``qoder`` selection, clean-stages the Qoder package archive as the
      experimental, installable tier's acceptance evidence.
   2. Re-running the identical command updates idempotently.
   3. Installed Setup directly invokes ``.syspilot/installer.py`` without
      Agent, Task, or ``runSubagent`` installation delegation.
   4. Successful and failed runs, including a failure after commit creation,
      leave no checkpoint artifact and retain no failed-run commit.
