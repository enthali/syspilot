Harness Agent Adapter UAT
=========================

Manual acceptance scenarios for ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``.


.. story:: UAT: Harness Agent Frontmatter Adapter
   :id: SYSP_US_UAT_HARNESS_AGENT_ADAPTER
   :status: approved
   :priority: mandatory
   :tags: uat, harness, agent, frontmatter, portability
   :links: SYSP_US_HARNESS_PORTABILITY

   **As a** syspilot Test Designer,
   **I want** a human tester to compare adapted agent files with their source,
   **so that** only harness-specific structure changes while agent behavior
   remains single-source.

   **Artifacts Under Test:**

   * One generated Manager agent and one generated Engineer agent for each
     production-parity harness (VS Code GitHub Copilot, OpenCode, Claude
     Code), plus the staged Qoder package archive as the experimental,
     installable tier's artifact
   * Their corresponding source ``*.agent.md`` files
   * The field mapping in ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``

   **Traceability:**

   Covers ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``,
   ``SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE``, and
   ``SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE``. Test data is defined in
   ``SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER``; expected outcomes are defined in
   ``SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER``.

   **Acceptance Criteria:**

   1. Adapted Markdown bodies are byte-for-byte identical to their source
      except for the explicitly permitted structural binding adaptation.
   2. The Claude Code fixture contains all 13 product agents with required,
      valid, unique native ``name`` values mapped from dotted source IDs and
      ``user-invocable: false`` as a VS Code compatibility extension. Claude
      native names and Agent-tool bindings remain intact; live Claude Code
      discovery and VS Code picker evidence are owned exclusively by
      ``SYSP_US_UAT_HARNESS_TARGET_MATRIX``.
   3. OpenCode frontmatter expresses primary/subagent mode and SEND
      permissions without changing workflow prose.
   4. Qoder frontmatter, as staged inside the checksummed package archive,
      contains only documented mappings and does not invent equivalents for
      unsupported fields. Native in-app loading of that staged content is
      deferred future scope and is not evaluated here.
   5. Representative Manager and Engineer agents retain their specified
      guidance when adapted for each production-parity harness; live
      native-loading acceptance is owned exclusively by
      ``SYSP_US_UAT_HARNESS_TARGET_MATRIX`` and SHALL NOT be inferred from
      this criterion. Qoder's equivalent native-loading check is deferred to
      the future change that adds native import evidence.
