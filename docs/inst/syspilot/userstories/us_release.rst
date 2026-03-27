Release Instance User Stories
==============================

How the syspilot team releases syspilot itself.

**Last Updated**: 2026-03-27


.. story:: Release syspilot Using Our Own Process
   :id: INST_SYSPILOT_US_REL_OWN_RELEASE
   :status: approved
   :priority: mandatory
   :tags: instance, release, dogfooding
   :links: SYSPILOT_US_REL_CREATE, SYSPILOT_US_REL_AGENT_TEMPLATE

   **As** the syspilot team,
   **I want to** release syspilot using our own release agent and process,
   **so that** we dogfood our toolkit and improve it through direct use.

   **Acceptance Scenarios:**

   1. Given a set of merged changes, When I invoke @syspilot.release,
      Then a semver-tagged GitHub Release is created
   2. Given the release agent, When it runs, Then it uses the decisions
      documented in our customized .github/agents/syspilot.release.agent.md
   3. Given release is published, When users download, Then they get the
      latest syspilot agents, skills, and scripts
