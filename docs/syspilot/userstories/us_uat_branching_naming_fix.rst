Branching Naming Fix UAT
========================

User Acceptance Test Story for the ``branching-naming-fix`` change request,
covering both independent fixes: removal of the stale ``update/v{version}``
attribution in ``SYSP_REQ_SKILL_BRANCHING_NAMING``, and the Trace Engineer's
new duty to re-verify content consistency on a modified element's existing
cross-reference links.


.. story:: UAT: Branching Naming Fix & Trace Cross-Reference Re-verification
   :id: SYSP_US_UAT_BRANCHING_NAMING_FIX
   :status: draft
   :priority: mandatory
   :tags: uat, skill-branching, trace, naming, regression
   :links: SYSP_US_SKILL_BRANCHING, SYSP_US_TRACE

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   stale ``update/v{version}`` / ``@syspilot.setup`` branch-creation claim
   is gone from both the spec and the deployed Skill, and that the Trace
   Engineer's extended duty actually catches the exact class of
   cross-reference contradiction that let the original stale claim slip
   through undetected,
   **so that** the specific gap that allowed this incident (a modified
   element's *existing* cross-reference link not re-checked) cannot recur.

   **Context:**

   ``SYSP_REQ_SKILL_BRANCHING_NAMING`` incorrectly attributed the
   ``update/v{version}`` branch pattern to ``@syspilot.setup``, contradicting
   ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` (already correctly describing
   the Installer's no-dedicated-branch behavior). The two elements are
   ``:links:``-connected, but a prior CR (``release-agent-tailoring-semver``)
   modified only the Permissions side and the contradiction went uncaught —
   because Trace's semantic-consistency check only verified the direct
   structural US→REQ→SPEC lineage of the *modified* element, not its other
   existing cross-reference links. This CR (1) removes the stale content and
   (2) extends the Trace Engineer's duty so it re-verifies a modified
   element's content against **all** currently-linked elements, including
   cross-references that sit outside the direct parent/child chain.

   **Artifacts Under Test:**

   * ``docs/syspilot/requirements/req_skill_branching.rst`` —
     ``SYSP_REQ_SKILL_BRANCHING_NAMING``
   * ``docs/syspilot/design/spec_skill_branching.rst`` —
     ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` (cross-reference partner)
   * ``docs/syspilot/design/spec_quality_trace.rst`` —
     ``SYSP_SPEC_TRACE_DUTIES`` (Duty #4 reworded, new Duty #6)
   * ``docs/syspilot/requirements/req_quality_trace.rst`` —
     ``SYSP_REQ_TRACE_DUTIES`` AC-4, AC-5
   * ``syspilot/skills/syspilot.branching/SKILL.md`` — deployed Skill
     naming table (Dev Engineer implementation target)
   * Git commit ``96347f3`` (merge of ``release-agent-tailoring-semver`` into
     ``experimental``) — the exact historical commit at which the
     contradiction existed uncaught; used as a regression fixture

   **Traceability:**

   Covers ``SYSP_REQ_SKILL_BRANCHING_NAMING`` (stale attribution removed);
   ``SYSP_US_TRACE`` AC-5, ``SYSP_REQ_TRACE_DUTIES`` AC-4/AC-5,
   ``SYSP_SPEC_TRACE_DUTIES`` Duty #4/#6 (modified-element cross-reference
   re-verification).
   Test data is defined in ``SYSP_REQ_UAT_BRANCHING_NAMING_FIX``; expected
   outcomes in ``SYSP_SPEC_UAT_BRANCHING_NAMING_FIX``.

   **Acceptance Criteria:**

   1. **No stale attribution in the requirement spec.**
      *Precondition:* Branch ``feature/branching-naming-fix`` checked out.
      *Action:* Open ``SYSP_REQ_SKILL_BRANCHING_NAMING`` and search its full
      node body for ``update/v{version}`` and ``@syspilot.setup``.
      *Expected result:* Neither string appears anywhere in the node —
      traces to the CR's primary acceptance criterion

   2. **⏳ Forward coverage — no stale attribution in the deployed Skill.**
      *Precondition:* The Dev Engineer has updated
      ``.github/skills/syspilot.branching/SKILL.md`` to match the corrected
      spec (pending at UAT authoring time).
      *Action:* Open the deployed ``SKILL.md`` naming table and search for
      ``update/v{version}`` and ``@syspilot.setup``.
      *Expected result:* Neither string appears in the naming table —
      traces to the CR's primary acceptance criterion

      .. note::
         This scenario's execution depends on the Implement stage of this
         CR, which had not yet run when this UAT chain was authored.
         Included now as forward coverage, not a spec gap.

   3. **Regression scenario — Trace catches the exact original contradiction (cross-reference case).**
      *Precondition:* A checkout of commit ``96347f3`` (the historical
      state where ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` had already
      been corrected by the prior CR but ``SYSP_REQ_SKILL_BRANCHING_NAMING``
      still carried the stale ``update/v{version}`` / ``@syspilot.setup``
      claim) — this is the actual incident state, not a synthesized one.
      *Action:* Invoke ``@syspilot.trace`` on
      ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` (the element the prior CR
      actually modified).
      *Expected result:* Trace's Duty #6 (Modified-Element
      Re-verification) checks ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``
      against every element in its ``:links:`` field — including
      ``SYSP_REQ_SKILL_BRANCHING_NAMING``, which is a **cross-reference**
      rather than that spec's direct structural parent requirement — and
      flags a content contradiction between the two: Permissions states
      no dedicated branch is created for the Installer, while Naming still
      attributes ``update/v{version}`` creation to ``@syspilot.setup`` —
      traces to ``SYSP_US_TRACE`` AC-5, ``SYSP_REQ_TRACE_DUTIES`` AC-4,
      AC-5, ``SYSP_SPEC_TRACE_DUTIES`` Duty #6

   4. **Confirm the checked link is genuinely a cross-reference, not parent/child.**
      *Precondition:* ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``'s
      ``:links:`` field is readable.
      *Action:* Compare the ``:links:`` field's element list against which
      requirement is this spec's direct structural parent (the requirement
      it primarily elaborates).
      *Expected result:* ``SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION`` is
      the spec's direct structural parent;
      ``SYSP_REQ_SKILL_BRANCHING_NAMING`` is an additional, lateral
      cross-reference in the same ``:links:`` field — confirming scenario 3
      exercises the cross-reference gap class specifically, not ordinary
      parent/child lineage checking already covered by pre-existing Trace
      duties — traces to ``SYSP_US_TRACE`` AC-5
