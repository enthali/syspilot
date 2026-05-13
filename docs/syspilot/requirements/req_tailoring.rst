Tailoring Agent Requirements
=============================


.. req:: Tailoring Agent Soul
   :id: SYSP_REQ_TAIL_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent, tailoring, soul
   :links: SYSP_US_TAIL

   **Description:**
   The Tailoring Agent (syspilot.tailoring) SHALL have a Soul that defines it
   as a consultative, standards-literate scoping partner — never inventing
   standards, always confirming with the user.

   **Acceptance Criteria:**

   * AC-1: Tailoring Soul defines a consultative, conservative character
   * AC-2: Tailoring Agent never invents or asserts the applicability of a
     standard without explicit user confirmation
   * AC-3: Tailoring Agent never writes Change Requests, code, tests, or
     other agents' files


.. req:: Tailoring Agent Duties
   :id: SYSP_REQ_TAIL_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent, tailoring, duties
   :links: SYSP_US_TAIL

   **Description:**
   The Tailoring Agent SHALL have Duties covering profile creation, profile
   maintenance, per-CR scope validation, and activation of companion agents
   via profile flags.

   **Acceptance Criteria:**

   * AC-1: Tailoring Agent can create a new Tailoring Profile by interviewing
     the user (and the PM via Jarvis if available) about project type,
     standards, criticality, quality goals, required artifacts and gates
   * AC-2: Tailoring Agent can update an existing Tailoring Profile in place
     and report what changed
   * AC-3: Tailoring Agent can validate a Change Request's scope against the
     active Tailoring Profile and return a structured finding
   * AC-4: Tailoring Agent SHALL set companion-agent activation flags
     (e.g. ``security_required``) in the profile rather than invoking those
     companion agents itself


.. req:: Tailoring Agent Workflow
   :id: SYSP_REQ_TAIL_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent, tailoring, workflow
   :links: SYSP_US_TAIL

   **Description:**
   The Tailoring Agent SHALL follow a workflow from intake through interview,
   profile authoring, MECE advisory, and notification of PM/CM/QM.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with detection of an existing profile
     (``docs/inst/syspilot/tailoring/profile.rst``); if absent, runs in
     bootstrap mode; if present, runs in update mode
   * AC-2: Workflow uses the ``syspilot.ask-questions`` skill for each
     interview step (project type, standards, criticality, quality goals,
     required artifacts, review gates, companion activations)
   * AC-3: Workflow writes / updates the profile RST files under
     ``docs/inst/syspilot/tailoring/`` and invokes ``syspilot.mece``
     advisory on the resulting profile specs
   * AC-4: Workflow ends by notifying PM (and CM/QM if changed) of the new or
     updated profile via Jarvis with the profile path


.. req:: Tailoring Profile Schema
   :id: SYSP_REQ_TAIL_PROFILE_SCHEMA
   :status: draft
   :priority: mandatory
   :tags: tailoring, profile, schema
   :links: SYSP_US_TAIL

   **Description:**
   The Tailoring Profile SHALL be a structured artifact authored as
   sphinx-needs items (``INST_SYSP_SPEC_TAIL_*``) under
   ``docs/inst/syspilot/tailoring/`` and SHALL carry the following fields.

   **Acceptance Criteria:**

   * AC-1: ``project_type`` — one of ``web``, ``cloud``, ``embedded``,
     ``automotive``, ``avionics``, ``desktop``, ``mixed``
   * AC-2: ``standards`` — ordered list of applicable standards (e.g.
     ``OWASP-ASVS``, ``OWASP-Top10``, ``ASPICE``, ``ISO-26262``,
     ``ISO-25010``, ``DO-178C``, ``IEC-61508``, ``GDPR``, ``HIPAA``);
     empty list is valid
   * AC-3: ``criticality_level`` — generic field whose valid values depend
     on the chosen standard (e.g. ``ASIL-A`` … ``ASIL-D`` plus ``QM`` for
     ISO 26262; ``SIL-1`` … ``SIL-4`` for IEC 61508; ``DAL-A`` … ``DAL-E``
     for DO-178C; ``none`` when no safety/criticality scheme applies);
     never hardcode a single scheme
   * AC-4: ``quality_goals`` — ISO 25010 sub-characteristics with target
     levels (e.g. ``security: high``, ``maintainability: medium``)
   * AC-5: ``required_artifacts`` — list of artifacts the project must
     produce (e.g. ASPICE base practices, MC/DC coverage report, threat
     model, ops runbook)
   * AC-6: ``review_gates`` — per-handover human-review requirements,
     each entry of the form ``{from: <agent>, to: <agent>, required_at:
     <criticality threshold>}``
   * AC-7: ``coverage_targets`` — at least ``test_coverage`` (e.g.
     ``branch`` or ``mcdc``) and ``min_coverage_pct``
   * AC-8: ``companion_agents`` — flags that activate companion agents
     (e.g. ``security_required: true``); reserved keys for future
     ``safety_required`` and ``privacy_required`` are allowed but optional


.. req:: Tailoring Frontmatter Configuration
   :id: SYSP_REQ_TAIL_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent, tailoring, frontmatter
   :links: SYSP_US_TAIL, SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Tailoring Agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable manager-style agent that may invoke
   ``syspilot.mece`` as subagent.

   **Acceptance Criteria:**

   * AC-1: Tailoring frontmatter declares ``user-invocable: true``
   * AC-2: Tailoring frontmatter ``agents`` list contains exactly
     ``syspilot.mece``
   * AC-3: Tailoring frontmatter ``tools`` includes ``read``, ``edit``,
     ``search``, ``todo`` and the ``vscode/askQuestions`` (ask-questions)
     tooling; it does NOT need ``execute``
   * AC-4: Tailoring frontmatter does NOT include any tool that allows
     modifying ``.github/agents/`` files (the agent never edits other
     agents)


.. req:: Safety Tailoring Skill Integration
   :id: SYSP_REQ_TAIL_SAFETY_SKILL
   :status: draft
   :priority: mandatory
   :tags: agent, tailoring, safety, skill
   :links: SYSP_US_TAIL

   **Description:**
   When the Tailoring Profile's ``standards[]`` includes a functional-safety
   standard (ISO-26262, IEC-61508, or DO-178C), the Tailoring Agent SHALL
   apply the ``syspilot.safety-tailoring`` skill to add safety-specific
   interview stages and produce additional structured artifacts.

   **Acceptance Criteria:**

   * AC-1: The Tailoring Agent detects functional-safety standards in the
     selected ``standards[]`` and activates the safety-tailoring skill
   * AC-2: The safety-tailoring skill adds stages for: safety element
     scoping, work-product planning, per-standard-requirement tailoring-out
     decisions, RASIC responsibility assignment, review-gate refinement,
     coverage targets, and component classification
   * AC-3: Per-requirement tailoring-out decisions are stored as
     ``INST_SYSP_SPEC_TAIL_SAFETY_EXCL_*`` sphinx-needs items with reasoning
     in ``docs/inst/syspilot/tailoring/safety-tailoring.rst``
   * AC-4: Component classifications are stored as
     ``INST_SYSP_SPEC_TAIL_COMP_CLASS_*`` items with max ASIL, process
     analysis, complexity, and classification result
   * AC-5: RASIC role assignments are stored in the profile under
     ``safety_roles``
   * AC-6: Coverage targets and review gates are refined per the
     standard-specific defaults from the skill (e.g. MC/DC for ASIL-C+)
