Spec Root-Cause Principle UAT
=============================

User Acceptance Test Story for the ``spec-root-cause-principle`` change
request — the Quality Manager's Spec-Layer Root-Cause Attribution duty and
the Dev Engineer's Spec-Divergence Escalation duty, both formalizing the
same discipline: when code looks wrong, the spec is the primary suspect,
not the coder.


.. story:: UAT: Spec Root-Cause Attribution & Escalation
   :id: SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE
   :status: draft
   :priority: mandatory
   :tags: uat, qm, implement, root-cause, regression
   :links: SYSP_US_QM, SYSP_US_IMPLEMENT

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify QM
   traces a code-level defect upward to the spec layer before filing it as
   a pure implementation slip, the Dev Engineer escalates rather than
   patching around a spec-diverging defect, and a scenario mirroring one of
   the three original incidents that motivated this CR would now be caught
   by the new duty instead of misclassified as a coding error,
   **so that** the recurring failure pattern — "code is wrong" symptom,
   spec-layer root cause — is structurally addressed rather than repeatedly
   rediscovered.

   **Context:**

   A QM review pattern emerged 3/3 times: a code-level defect's actual root
   cause was upstream — wrong/missing spec text, or a missing cross-link
   that hid an affected consumer from impact analysis — not a coding
   mistake. This CR adds two duties: QM (``SYSP_SPEC_QM_DUTIES``) now
   traces any code-level defect upward before classifying it as a pure
   implementation slip; Dev Engineer (``SYSP_SPEC_IMPLEMENT_DUTIES``) now
   refuses to patch around a spec-diverging defect and escalates for spec
   correction instead. Both are read-only/behavioral duties — nothing here
   changes what "correct" looks like, only who investigates a symptom and
   how far upstream they look before closing it.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.qm.agent.md`` — Quality Manager agent
   * ``syspilot/agents/syspilot.implement.agent.md`` — Dev Engineer agent
   * ``docs/syspilot/design/spec_quality_mgr.rst`` —
     ``SYSP_SPEC_QM_DUTIES`` (Spec-Layer Root-Cause Attribution)
   * ``docs/syspilot/design/spec_dev_engineer.rst`` —
     ``SYSP_SPEC_IMPLEMENT_DUTIES`` (Spec-Divergence Escalation)
   * The ``installer-frontmatter-sync`` incident (this repo's own history)
     — used as the regression fixture

   **Traceability:**

   Covers ``SYSP_REQ_QM_DUTIES`` AC-8 (spec-layer root-cause assessment
   before closing a code-level finding) and ``SYSP_REQ_IMPLEMENT_DUTIES``
   AC-5 (escalate instead of patching around spec divergence).
   Test data is defined in
   ``SYSP_REQ_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``; expected outcomes in
   ``SYSP_SPEC_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``.

   **Acceptance Criteria:**

   1. **QM traces a code-level defect upward before filing it as an implementation slip.**
      *Precondition:* A code-level defect is identified in an installed
      agent or Skill file — e.g. its behavior contradicts the currently
      approved design spec for that file.
      *Action:* Have ``@syspilot.qm`` assess the defect.
      *Expected result:* Before QM's Findings Report classifies the defect,
      it records an explicit check of the corresponding spec-layer element
      (US/REQ/SPEC) for that code — either confirming the spec is correct
      and the defect is a genuine implementation slip, or identifying that
      the spec itself is wrong, missing, or missing a cross-link. The
      report never closes a code-level finding without this upward check
      having been performed and stated — traces to ``SYSP_REQ_QM_DUTIES``
      AC-8

   2. **Dev Engineer escalates instead of patching around spec divergence.**
      *Precondition:* The Dev Engineer is asked to fix a defect where the
      only code change that would "fix" the symptom would make the code
      diverge from its approved spec (the spec, as currently written, does
      not support the requested fix).
      *Action:* Invoke ``@syspilot.implement`` (or dispatch the Dev
      Engineer subagent) with this task.
      *Expected result:* The Dev Engineer does not apply a code patch that
      diverges from the approved spec. Instead it stops and escalates
      (RESPOND / report) that a spec correction is needed, naming the
      spec element in question — traces to ``SYSP_REQ_IMPLEMENT_DUTIES``
      AC-5

   3. **⚠ Regression — replaying the installer-frontmatter-sync incident.**
      *Precondition:* The historical state before ``installer-frontmatter-sync``
      was fixed: ``syspilot.installer.agent.md`` Step 4 described the
      retired ``tools:``-preservation logic, while
      ``SYSP_SPEC_INSTALLER_WORKFLOW`` had already been corrected to
      verbatim-from-upstream semantics by the ``remove-tools-frontmatter``
      CR. On the surface this reads as "the Installer's code (agent file)
      is wrong."
      *Action:* Have ``@syspilot.qm`` assess the Installer agent file
      defect using its new Spec-Layer Root-Cause Attribution duty.
      *Expected result:* QM's assessment does not stop at "the agent file
      needs a code fix to match itself up" — applying AC-8, it checks the
      spec layer first, finds ``SYSP_SPEC_INSTALLER_WORKFLOW`` is already
      correct, and identifies the actual root cause as a missing-link
      class of gap: ``remove-tools-frontmatter``'s impact analysis never
      surfaced the Installer agent file as an affected consumer of the
      tools-frontmatter removal. The finding is routed as an
      impact-analysis/traceability gap, not filed as "Dev Engineer wrote
      buggy code" — traces to ``SYSP_REQ_QM_DUTIES`` AC-8. **This is the
      regression test for the exact incident class this CR was created to
      prevent** — replaying it with the new duty applied would have
      produced the correct root-cause classification the first time.
