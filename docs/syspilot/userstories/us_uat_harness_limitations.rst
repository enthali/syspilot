Harness Limitations UAT
=======================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_LIMITATIONS``.


.. story:: UAT: Harness Disclosed Limitations
   :id: SYSP_US_UAT_HARNESS_LIMITATIONS
   :status: approved
   :priority: mandatory
   :tags: uat, harness, limitations, disclosure, portability
   :links: SYSP_US_HARNESS_PORTABILITY

   **As a** syspilot Test Designer,
   **I want** a human tester to verify every accepted harness limitation is
   accurate, visible, and isolated,
   **so that** unsupported behavior is never silently presented as parity and
   does not block supported behavior on other harnesses.

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_LIMITATIONS`` and
   ``SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_LIMITATIONS``; expected outcomes are defined in
   ``SYSP_SPEC_UAT_HARNESS_LIMITATIONS``.

   **Acceptance Criteria:**

   Claude Code scenarios are mandatory production checks evaluated
   independently. Qoder scenarios are evaluated against the experimental,
   installable tier bar. A disclosed limitation does not waive required
   production roles, Skills, commands or prompts, or Manager-to-Engineer
   orchestration on the production-parity tier, and does not convert Qoder's
   deferred native-import or orchestration scope into a silent gap.

   1. The Claude Code/VS Code cross-discovery boundary is disclosed and
      observable: ``user-invocable: false`` hides every generated
      Claude-format identity only from VS Code's direct picker and does not
      hide or disable native invocation in Claude Code.
   2. Claude Code main-thread Managers use explicit native Agent target
      restrictions, while nested-spawn behavior is disclosed without falsely
      claiming per-target enforcement for bare ``Agent``.
   3. OpenCode native Skill frontmatter omits unsupported ``group``, ``tools``,
      and ``triggers`` fields while source ``group`` metadata still drives
      Installer-side mutual exclusion.
   4. Qoder's undocumented nesting depth is disclosed; production
      orchestration acceptance does not apply to Qoder for this change, which
      is scoped to the experimental, installable tier.
   5. Qoder Rules are not shipped, and their Settings-UI registration gap is
      disclosed as future scope without affecting Agents or Skills.
   6. Native Qoder package import and Qoder Manager-to-Engineer orchestration
      parity are disclosed as explicitly deferred future scope, resolved by
      this change's scope revision rather than by evidence.
