Implementation Instance User Stories
=====================================

How the syspilot team implements changes to product artifacts.

**Last Updated**: 2026-03-27


.. story:: Implement syspilot Agents as Product Artifacts
   :id: INST_SYSPILOT_US_IMPL_OWN_AGENTS
   :status: implemented
   :priority: mandatory
   :tags: instance, implement, dogfooding
   :links: SYSPILOT_US_CHG_IMPLEMENT

   **As** the syspilot team,
   **I want to** implement approved changes into syspilot's product artifacts
   (agents, skills, scripts in syspilot/),
   **so that** the implement agent writes to the correct product directory
   and our distributed artifacts always match the specs.

   **Acceptance Scenarios:**

   1. Given an approved Change Document, When @syspilot.implement runs,
      Then it modifies files in syspilot/ (not .github/)
   2. Given an implement run, When it updates agent templates,
      Then the corresponding .github/ agents are NOT automatically changed
   3. Given implementation is done, When @syspilot.verify runs,
      Then it checks completeness against the Change Document
