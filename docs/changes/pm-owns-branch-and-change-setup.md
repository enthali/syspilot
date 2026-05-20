# Change Document: pm-owns-branch-and-change-setup

**Status**: in-progress
**Branch**: feature/pm-owns-branch-and-change-setup
**Created**: 2026-05-21
**Author**: PM
**Authoring Mode**: instance-first (author in `.github/agents/`; sync to `syspilot/agents/` before close)

---

## Summary

Clarify and enforce the ownership boundary between PM and CM for branch
creation and Change Document initialization. PM owns the `development`
branch and is responsible for creating the feature branch and the Change
Document header (Summary, WHY, ACs) before CM starts work. CM receives a
ready-made branch and document and fills in the engineering detail. PM
performs the merge to `development` — CM only signals readiness. Feature
branches are retained after merge (for forensic/bisect purposes) and
cleaned up by the Release Agent at release time.

**WHY**: In practice, CM was inferring branch names and creating Change
Documents without clear ownership rules. This caused CM to create files
in wrong locations (versioned subdirectories instead of flat
`docs/changes/`). Structural ownership boundaries eliminate this class of
error without requiring additional guardrails.

**Acceptance Criteria (user-visible):**
1. PM agent file describes PM's responsibility to create the feature branch
   and Change Document header before sending a CR to CM.
2. CM agent file states that CM receives branch + Change Document path from
   PM — CM never creates the branch or the initial Change Document.
3. CM agent file states CM never merges to `development` — CM signals
   readiness; PM performs the merge.
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
