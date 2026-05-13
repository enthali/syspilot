Tailoring Agent
================


.. story:: Project Tailoring Agent
   :id: SYSP_US_TAIL
   :status: draft
   :priority: mandatory
   :tags: agent, manager, tailoring, standards, project-shaping
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user starting (or rescoping) a project,
   **I want** a Tailoring Agent (syspilot.tailoring) that interviews me and
   the Project Manager to capture the project's type, applicable standards,
   criticality, quality goals and required review gates,
   **so that** the other syspilot agents (PM, CM, QM, ...) know which
   engineering rigor, artifacts and human review steps apply to this project.

   **Context:**

   syspilot is used in very different settings: web/cloud projects following
   OWASP, automotive projects following ASPICE / ISO 26262, embedded projects
   under IEC 61508, avionics under DO-178C, and lightweight tooling projects
   with no formal standard at all. The Tailoring Agent shapes syspilot to the
   actual project before any change work happens, and it captures this scope
   as a **Tailoring Profile** stored as RST sphinx-needs items under
   ``docs/inst/syspilot/tailoring/`` so it is fully traceable and project-owned.

   The Tailoring Agent is the only agent that *activates* other companion
   agents (e.g. ``syspilot.security``) by setting flags in the profile. Other
   agents read the profile and adapt their behaviour — they are not modified
   by the tailoring process itself.

   **Acceptance Criteria:**

   1. Given a fresh project, When the user invokes ``@syspilot.tailoring``,
      Then the agent interviews user and PM and produces a Tailoring Profile
      RST file under ``docs/inst/syspilot/tailoring/``
   2. Given an existing project whose scope has shifted, When the user invokes
      ``@syspilot.tailoring`` again, Then the agent updates the profile in
      place and reports what changed
   3. Given a Change Request inside the change workflow, When CM or PM ask the
      Tailoring Agent for validation, Then the agent reports whether the CR
      scope is consistent with the profile
   4. Given a profile with ``security_required: true``, When other agents read
      the profile, Then ``syspilot.security`` is treated as a mandatory
      participant in the change workflow
   5. The Tailoring Agent never writes code, never writes Change Requests, and
      never modifies other agents' files
