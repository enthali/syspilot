Harness Orchestration Adapter UAT
=================================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER``.


.. story:: UAT: Harness Orchestration Fallback
   :id: SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER
   :status: approved
   :priority: mandatory
   :tags: uat, harness, orchestration, fallback, portability
   :links: SYSP_US_HARNESS_PORTABILITY, SYSP_US_SKILL_ORCHESTRATION

   **As a** syspilot Test Designer,
   **I want** a human tester to verify deterministic synchronous orchestration
   installation and one-hop SEND behavior,
   **so that** installation never depends on Jarvis inference or actor setup.

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER`` and
   ``SYSP_REQ_SKILL_ORCHESTRATION_GROUP``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER``; expected outcomes are
   defined in ``SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER``.

   **Acceptance Criteria:**

   1. Every target installs the synchronous orchestration-group variant and no
      asynchronous variant, regardless of ``.jarvis/`` presence.
   2. Managers in VS Code GitHub Copilot, OpenCode, and Claude Code each
      complete a synchronous Manager-to-Engineer SEND and receive the
      Engineer result as production acceptance. Qoder orchestration
      acceptance is out of scope for this change and is deferred to a future
      change.
   3. Claude Code passes authenticated live native invocation and
      Manager-to-Engineer delegation as an independent quality gate. Qoder's
      equivalent live invocation/delegation evidence is explicitly deferred
      future scope, not a gate cleared or waived here.
   4. Claude Code independently completes a representative end-to-end
      Manager workflow in autonomous product operation, including every
      required Engineer delegation and returned result, without pausing for
      user approval between workflow stages; Manager invocation or a single
      successful delegation alone does not satisfy this criterion. Qoder is
      not evaluated against this criterion for this change; the deferral is
      disclosed, not silently dropped.
