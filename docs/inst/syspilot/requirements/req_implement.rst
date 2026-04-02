Implementation Instance Requirements
=====================================

Project-specific implementation decisions for syspilot.

**Last Updated**: 2026-03-27


.. req:: Implement Agent Write Boundary
   :id: INST_SYSPILOT_REQ_IMPL_WRITE_BOUNDARY
   :status: implemented
   :priority: mandatory
   :tags: instance, implement, boundary
   :links: INST_SYSPILOT_US_IMPL_OWN_AGENTS, SYSPILOT_REQ_CHG_IMPL_AGENT

   The Implement Agent SHALL write exclusively to ``syspilot/`` (product artifacts).
   It SHALL NOT modify files in ``.github/``.

   * AC-1: All code changes from implement agent target ``syspilot/`` directory
   * AC-2: ``.github/agents/`` files are never touched by implement agent
   * AC-3: Spec updates target ``docs/syspilot/`` (product specs)


.. req:: Setup Agent Synchronization
   :id: INST_SYSPILOT_REQ_IMPL_SETUP_SYNC
   :status: implemented
   :priority: mandatory
   :tags: instance, implement, setup
   :links: INST_SYSPILOT_US_IMPL_OWN_AGENTS, SYSPILOT_REQ_INST_TEMPLATE_SOURCE

   The Setup Agent SHALL synchronize product artifacts from ``syspilot/``
   to ``.github/`` when the user requests an update.

   * AC-1: ``syspilot/agents/*.agent.md`` → ``.github/agents/``
   * AC-2: ``syspilot/skills/*/SKILL.md`` → ``.github/skills/*/``
   * AC-3: User-customized ``.github/`` files are preserved (intelligent merge)
