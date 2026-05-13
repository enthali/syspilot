Skill: Impact Analysis
======================

Impact analysis for specification elements.


.. story:: Impact Analysis Before Design Work
   :id: SYSP_US_SKILL_IMPACT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, impact, traceability
   :links: SYSP_US_DESIGN; SYSP_US_PM; SYSP_US_SKILL_ARCH

   **As a** System Designer,
   **I want** a skill that provides impact analysis for Need elements,
   **so that** I can see the complete dependency tree before starting my analysis
   — and the underlying tool can be swapped without changing my workflow.

   **Context:**

   Before analyzing a change request, the System Designer needs to know which
   specification elements are potentially affected. Today this is done manually
   via grep and semantic search, which is error-prone and slow.

   The impact analysis skill wraps a tool (currently ``get_need_links.py``) that
   traverses the sphinx-needs link graph. The skill is **exchangeable**: a
   different implementation (e.g. ubCode) can replace it without changing the
   designer's workflow. This reflects the architectural principle that agents
   define stable processes while skills define exchangeable tool bindings.

   **Acceptance Criteria:**

   1. Skill provides the impact tree for a given Need ID
   2. Depth and direction (vertical/horizontal, in/out/both) are configurable
   3. Skill uses the existing Python script — no new tooling required
   4. The skill is exchangeable: an alternative skill (e.g. ubCode-based) can
      replace it without changing the System Designer's workflow
