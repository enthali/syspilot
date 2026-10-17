Harness Prompt Adapter UAT
==========================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER``.


.. story:: UAT: Harness Prompt and Command Adapter
   :id: SYSP_US_UAT_HARNESS_PROMPT_ADAPTER
   :status: approved
   :priority: mandatory
   :tags: uat, harness, prompt, command, portability
   :links: SYSP_US_HARNESS_PORTABILITY

   **As a** syspilot Test Designer,
   **I want** a human tester to verify each harness's invocation surface,
   **so that** prompt files are generated only where a native prompt or
   command format exists.

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` and
   ``SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE`` and
   ``SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER``; expected outcomes are defined in
   ``SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER``.

   **Acceptance Criteria:**

   1. VS Code prompt files and ``agent:`` routing remain unchanged, and a
      representative request invokes the expected Manager behavior.
   2. OpenCode receives a thin native command for each source Manager prompt,
      and the same representative request invokes equivalent Manager behavior.
   3. Claude Code provides a production-ready native command, prompt, agent,
      or Skill invocation surface for each Manager workflow, and a
      representative request invokes equivalent Manager behavior.
   4. Qoder's native import of the staged Custom Agent package, and any
      invocation surface it might provide for each Manager workflow, are
      deferred future scope for this change and are not verified here;
      independent production-parity clearance for Qoder is not evaluated.
