Branching Naming Fix Expected Outcomes
=======================================

Expected outcomes specification for ``SYSP_REQ_UAT_BRANCHING_NAMING_FIX``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Branching Naming Fix & Trace Cross-Reference Re-verification
   :id: SYSP_SPEC_UAT_BRANCHING_NAMING_FIX
   :status: draft
   :priority: mandatory
   :tags: uat, skill-branching, trace, naming, regression, expected-outcomes
   :links: SYSP_REQ_UAT_BRANCHING_NAMING_FIX

   **Definition:**

   For each scenario in ``SYSP_US_UAT_BRANCHING_NAMING_FIX``, the following
   outcomes SHALL be observable. Each scenario is self-contained: the human
   tester prepares the named fixture (if any), runs the action, and confirms
   the expected result. A check item passes when the exact condition is
   met; it fails otherwise.

   ---

   **TC-BNF-REQCLEAN — No stale attribution in the requirement spec**

   *Precondition:* Branch ``feature/branching-naming-fix`` checked out.

   *Action:* Open ``SYSP_REQ_SKILL_BRANCHING_NAMING``; search its full node
   body for ``update/v{version}`` and ``@syspilot.setup``.

   *Expected result:*

   * [ ] Zero occurrences of ``update/v{version}`` in the node
   * [ ] Zero occurrences of ``@syspilot.setup`` in a branch-creation
     context in the node
   * [ ] The node's remaining branch patterns (``feature/<name>``,
     ``development``, ``main``) are internally consistent with its own
     AC list (no orphaned AC referencing a removed pattern)

   *Traces to:* ``SYSP_US_UAT_BRANCHING_NAMING_FIX`` AC-1

   ---

   **TC-BNF-SKILLCLEAN — No stale attribution in the deployed Skill (forward coverage)**

   *Precondition:* Dev Engineer has updated
   ``.github/skills/syspilot.branching/SKILL.md`` for this CR.

   *Action:* Open the deployed ``SKILL.md`` naming table; search for
   ``update/v{version}`` and ``@syspilot.setup``.

   *Expected result:*

   * [ ] Zero occurrences of ``update/v{version}`` in the naming table
   * [ ] Zero occurrences of ``@syspilot.setup`` attributed to branch
     creation in the naming table

   *Traces to:* ``SYSP_US_UAT_BRANCHING_NAMING_FIX`` AC-2 (pending
   Implement stage — not yet executable at authoring time)

   ---

   **TC-BNF-REGRESSION — Trace catches the exact original contradiction (regression test)**

   *Precondition:* Fixture ``F-INCIDENT-COMMIT`` — a read-only checkout of
   commit ``96347f3``.

   *Action:* Invoke ``@syspilot.trace`` on
   ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` in that checkout.

   *Expected result:*

   * [ ] Trace's report explicitly lists ``SYSP_REQ_SKILL_BRANCHING_NAMING``
     among the elements checked for content consistency (not just its
     direct structural parent requirement)
   * [ ] Trace's report flags a semantic-drift / content-contradiction
     finding between ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS`` (no
     dedicated branch for the Installer) and
     ``SYSP_REQ_SKILL_BRANCHING_NAMING`` (``update/v{version}`` attributed
     to ``@syspilot.setup``)
   * [ ] The finding is reported as a gap requiring correction, not silently
     passed

   *Traces to:* ``SYSP_US_UAT_BRANCHING_NAMING_FIX`` AC-3. **This is the
   direct regression test for the incident this CR fixes** — it replays
   the actual historical state (not a synthesized one) and confirms the
   new Duty #6 would have caught it before this CR existed.

   ---

   **TC-BNF-CROSSREF — Confirm cross-reference, not parent/child**

   *Precondition:* ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``'s ``:links:``
   field is readable (at commit ``96347f3`` or current branch — the field
   value is unchanged by this CR).

   *Action:* List the elements in ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``'s
   ``:links:`` field; identify which one is the spec's direct structural
   parent requirement (the one it primarily elaborates).

   *Expected result:*

   * [ ] ``SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION`` is identified as the
     direct structural parent
   * [ ] ``SYSP_REQ_SKILL_BRANCHING_NAMING`` is identified as an additional
     lateral cross-reference in the same ``:links:`` field — not the
     parent
   * [ ] This confirms TC-BNF-REGRESSION exercises the cross-reference gap
     class specifically (the class that slipped through in the original
     incident), not ordinary parent/child lineage checking that pre-existing
     Trace duties already covered

   *Traces to:* ``SYSP_US_UAT_BRANCHING_NAMING_FIX`` AC-4
