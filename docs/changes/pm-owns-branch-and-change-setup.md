# Change Document: pm-owns-branch-and-change-setup

**Status**: in-progress
**Branch**: feature/pm-owns-branch-and-change-setup
**Created**: 2026-05-21
**Author**: PM

---

## Summary

Clarify and enforce the ownership boundary between PM and CM for branch
creation, Change Document initialization, and integration. PM owns the
`development` branch and is responsible for creating the feature branch
and the Change Document header (Summary, WHY, ACs) before CM starts work.
CM receives a ready-made branch and document and fills in the engineering
detail. Integration into `development` is the responsibility of the PM
role — CM signals readiness, the integrator performs the merge. Feature
branches are retained after merge (for forensic/bisect purposes) and
cleaned up by the Release Agent at release time.

**WHY**: The current agent files leave branch creation and Change Document
initialization unassigned. Without explicit ownership, agents must infer
conventions from context — which is fragile. Explicit structural ownership
eliminates this class of ambiguity without requiring additional guardrails.

**Acceptance Criteria (user-visible):**
1. PM agent file describes PM's responsibility to create the feature branch
   and Change Document header before sending a CR to CM.
2. CM agent file states that CM receives branch + Change Document path from
   PM — CM never creates the branch or the initial Change Document.
3. CM agent file states CM never merges to `development`. Integration into
   `development` is the responsibility of the PM role — CM signals
   readiness, the integrator performs the merge.
4. Feature branches are not deleted after merge; cleanup is deferred to the
   Release Agent.
5. The Release Agent's cleanup step (delete merged feature branches) is
   described in the Release Agent file.

---

## Level 0: User Stories

*(CM fills in)*

---

## Level 1: Requirements

*(CM fills in)*

---

## Level 2: Design Specs

*(CM fills in)*
