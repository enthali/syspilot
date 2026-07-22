Spec Root-Cause Principle Expected Outcomes
============================================

Expected outcomes specification for
``SYSP_REQ_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``. This document is the
per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Spec Root-Cause Attribution & Escalation
   :id: SYSP_SPEC_UAT_SPEC_ROOT_CAUSE_PRINCIPLE
   :status: draft
   :priority: mandatory
   :tags: uat, qm, implement, root-cause, regression, expected-outcomes
   :links: SYSP_REQ_UAT_SPEC_ROOT_CAUSE_PRINCIPLE

   **Definition:**

   For each scenario in ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE``, the
   following outcomes SHALL be observable. Each scenario is self-contained:
   the human tester prepares the named fixture, runs the action, and
   confirms the expected result. A check item passes when the exact
   condition is met; it fails otherwise.

   ---

   **TC-SRC-QMTRACE — QM traces upward before classifying a code-level defect**

   *Precondition:* Fixture ``F-CODE-DEFECT`` (a genuine implementation
   slip — the underlying spec is correct).

   *Action:* Have ``@syspilot.qm`` assess the defect.

   *Expected result:*

   * [ ] QM's Findings Report explicitly records a spec-layer check for
     the corresponding US/REQ/SPEC element before stating a conclusion
   * [ ] Because the spec is correct in this fixture, QM's report
     concludes the defect is a genuine implementation slip — but only
     after the upward check is shown, not by default/omission
   * [ ] No finding is closed with a bare "code bug" classification and no
     spec-layer reference at all

   *Traces to:* ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE`` AC-1

   ---

   **TC-SRC-ESCALATE — Dev Engineer escalates instead of patching around divergence**

   *Precondition:* Fixture ``F-SPEC-DIVERGENCE`` (fix would require
   diverging from the approved spec).

   *Action:* Invoke ``@syspilot.implement`` with the fix request.

   *Expected result:*

   * [ ] No code change is committed that diverges from the approved spec
   * [ ] The Dev Engineer's response explicitly states a spec correction
     is needed, naming the specific spec element in question
   * [ ] The escalation is directed per the Dev Engineer's normal
     reporting path (RESPOND to its invoker), not silently dropped

   *Traces to:* ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE`` AC-2

   ---

   **TC-SRC-REGRESSION — Replaying the installer-frontmatter-sync incident**

   *Precondition:* Fixture ``F-INCIDENT-REPLAY`` — read-only historical
   checkout where ``syspilot.installer.agent.md`` Step 4 still describes
   the retired ``tools:``-preservation logic while
   ``SYSP_SPEC_INSTALLER_WORKFLOW`` is already corrected.

   *Action:* Have ``@syspilot.qm`` assess the Installer agent file defect,
   applying the new Spec-Layer Root-Cause Attribution duty.

   *Expected result:*

   * [ ] QM's assessment checks ``SYSP_SPEC_INSTALLER_WORKFLOW`` and finds
     it already correct
   * [ ] QM's finding identifies the actual root cause as a missing-link /
     impact-analysis gap in the prior ``remove-tools-frontmatter`` CR —
     not a Dev Engineer coding error
   * [ ] The finding is NOT classified as "Installer agent file has a bug
     that needs a code patch" in isolation from its spec

   *Traces to:* ``SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE`` AC-3. **This is
   the direct regression test for the incident class this CR was created
   to prevent** — replaying the actual historical repo state and
   confirming the new duty produces the correct root-cause classification.
