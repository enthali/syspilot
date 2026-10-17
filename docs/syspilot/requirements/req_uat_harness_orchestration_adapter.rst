Harness Orchestration Adapter Test Data
=======================================

Test data requirements for
``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER``.


.. req:: UAT Test Data: Harness Orchestration Fallback
  :id: SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER
  :status: approved
  :priority: mandatory
  :tags: uat, harness, orchestration, fallback, test-data
  :links: SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER

   **Fixtures:**

   * ``F-ORCH-VSCODE``, ``F-ORCH-CLAUDE``, and ``F-ORCH-OPENCODE``: clean
     production targets configured for live native execution. Qoder
     orchestration acceptance is out of scope for this change; no
     ``F-ORCH-QODER`` live-execution fixture is required.
   * ``F-ORCH-JARVIS-PRESENT``: production target containing ``.jarvis/`` to
     prove that installation remains synchronous.

   **Required Artifacts and Tools:**

   * Both mutually exclusive orchestration Skills from the source product.
   * Deterministic generated variants for all four installable harnesses
     (including the Qoder package archive) whose designated binding sections
     map SEND to the corresponding native delegation mechanism where one
     exists.
   * A representative Manager fixture with a complete workflow whose known
     stage sequence delegates to every required Engineer fixture. Each
     Engineer response contains a unique fixed token, and the Manager's final
     result records every token in workflow order.
   * Installed VS Code GitHub Copilot, Claude Code, and OpenCode environments
     capable of live native Manager and Engineer execution. Qoder live
     execution capability is not required for this change.
   * A file-listing tool and access to each harness's task/subagent execution
     transcript.

   Every fixture SHALL be reset before its scenario. Manager and Engineer
   bodies SHALL be identical across harnesses except for frontmatter. The
   orchestration Skill's semantic definitions, rules, inputs, outputs, and
   ordering SHALL be identical; only its designated native-binding section may
   differ.

  This requirement owns orchestration behavior only. Clean installation,
  update, injected-failure, and rollback acceptance are owned exclusively by
  ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` and SHALL NOT be inferred from this
  requirement's evidence.

   **Acceptance Criteria:**

   * **AC1**: Each production harness MUST independently complete the
     representative Manager workflow through its live native integration,
     execute every required Engineer delegation, return every unique Engineer
     result to the Manager, and consume every result in the final workflow
     outcome without an intervening user approval gate. Manager invocation or
     a single successful delegation is insufficient.
