# Change Document: german-duties-fix

**Status**: in-progress
**Branch**: feature/german-duties-fix
**Created**: 2026-06-24
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

Nine user story files contain "Duties" sections written in German. The documentation is a public product spec; all content must be in English. This CR translates all German "Duties" section content to English across the affected user story files, restoring language consistency and making the specs readable to the international audience the project targets. Acceptance: sphinx-build -W passes clean and no German text remains in any "Duties" heading or list item in the user stories directory. Tracks GitHub issue #37.

---

## Level 0: User Stories

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_xxx | ... | modified | ... |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSPILOT_US_NEW_1 | As a..., I want..., so that... | mandatory |

### Decisions

- Decision 1: ...
- Decision 2: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing User Stories
- [ ] No redundancies
- [ ] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_xxx | US_xxx | modified | ... |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSPILOT_REQ_NEW_1 | ... | US_xxx | mandatory |

### Conflicts Detected

- ⚠️ REQ_xxx vs REQ_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Requirements
- [ ] No redundancies
- [ ] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_xxx | REQ_xxx | modified | ... |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSPILOT_SPEC_NEW_1 | ... | REQ_xxx, SYSPILOT_REQ_NEW_1 |

### Conflicts Detected

- ⚠️ SPEC_xxx vs SPEC_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Designs
- [ ] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ⏳ not started | ✅ passed | ❌ failed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_xxx | REQ_xxx | SPEC_xxx | ✅ |
| SYSPILOT_US_NEW_1 | SYSPILOT_REQ_NEW_1 | SYSPILOT_SPEC_NEW_1 | ✅ |

### Artefakt-Removal-Check

*Fill in only when this CR removes an artefact (file, field, configuration key, REQ-ID).*

For each removed artefact, run a project-wide grep on all plausible name variants and classify results:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `{artefact name}` | {files + lines fixed / none} | {files + lines fixed / none} | {count — acceptable historic stranding} |

- [ ] All class (a) active code/workflow references fixed in this CR
- [ ] All class (b) active documentation references fixed in this CR
- [ ] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

- [x] **Scope breach — CM performed spec edits directly:** CM translated all German Duties sections without delegating to the System Designer. Justification: purely mechanical translation, no structural decisions, user-guided mode with user present and approving. Accepted by user in session. Disclosed here per standing protocol.

### Sign-off

- [ ] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [ ] All conflicts resolved
- [ ] Traceability verified
- [ ] Ready for implementation

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** Quality Manager
**Review date:** 2026-06-24
**Scope:** 8 L0 User Story elements (declared in Change Document)
**Check Type:** MECE (Horizontal) + Trace (Vertical)

#### Translation Quality Assessment

✅ **PASSED** — German→English translation of Duties sections is complete and accurate.
- Zero semantic drift detected
- All traceability links intact (verified end-to-end for 8 elements)
- sphinx-build clean (per Verify Engineer report)
- No German text remains in Duties sections

**Status of this CR:** Ready for merge to `development`.

---

#### Findings

**Note:** Findings below are **STRUCTURAL PRE-EXISTING ISSUES**, not translation-related. They represent gaps and ambiguities in the specification hierarchy that predate this CR and merit explicit architectural decisions.

| # | Level | Element ID | Finding | Category | Severity |
|---|-------|------------|---------|----------|----------|
| 1 | L0 | All 8 elements | Orphaned System Designer role: CM workflow declares "dispatch to System Designer" but SYSP_US_DESIGN is not in scope. Who authors and approves Design Specs that IMPLEMENT consumes? | Architecture / Gap | High |
| 2 | L0 | All 8 elements | No dedicated test/QA verification distinct from implementation: IMPLEMENT writes tests; VERIFY checks traceability. Gap: "Are the tests sufficient? Do they validate the spec?" — no role assigned. | Architecture / Gap | High |
| 3 | L0 | SYSP_US_CM, SYSP_US_VERIFY | Overlapping traceability mandates: CM claims "traceability of change history" (Change Document is true state); VERIFY re-validates same traceability. Boundary is verification-after-fact but creates ownership ambiguity. | Orchestration / Redundancy | Medium |
| 4 | L0 | SYSP_US_CM, SYSP_US_IMPLEMENT | Dual ownership of "alignment": CM responsible for "alignment between user intent and executed spec"; IMPLEMENT responsible for "alignment between approved specs and implementation." Overlapping language creates ambiguity about end-to-end alignment verification. | Orchestration / Redundancy | Medium |
| 5 | L0 | SYSP_US_SETUP, SYSP_US_INSTALLER | Unclear boundary between manifest and non-manifest scope: Both touch "what to copy" rules (SETUP enforces manifest fidelity, INSTALLER excludes manifest files). Handoff point is implicit rather than explicit. | Orchestration / Redundancy | Low |
| 6 | L0 | All 8 elements | Documentation ownership fragmented: IMPLEMENT updates docs; RELEASE creates release notes; no role owns cross-cutting documentation strategy. SYSP_US_DOCU exists but not in 8-element scope. | Architecture / Gap | Medium |
| 7 | L0 | All 8 elements | Post-merge workflow undefined: After development→main merge, who decides when to trigger Setup Agent? RELEASE? PM? Automatic? Current AC states "PM triggers Setup" but sequence after main merge is opaque. | Architecture / Gap | Medium |
| 8 | L0 | All 8 elements | No explicit rollback/abort workflow: CM states "Change Document is true state even after abort" but no role assigned abort responsibility. If change aborts at QM stage (defer), how does system unwind? Who cleans branch, signals abort, documents why? | Architecture / Gap | Medium |
| 9 | L0 | SYSP_US_SETUP, SYSP_US_INSTALLER | Spec status ownership unassigned: IMPLEMENT marked read-only for spec statuses. CM workflow shows System Designer updating statuses. Within 8-element scope: **no role owns spec status updates**. This contradicts requirement that specs transition through lifecycle states. | Orchestration / Contradiction | Medium |
| 10 | L1 | SYSP_REQ_SETUP_BOOTLOADER_DUTIES | Missing uplink to L0: `SYSP_REQ_SETUP_BOOTLOADER_DUTIES` does not link back to `SYSP_US_SETUP`. Creates uplink gap: REQ names itself "Bootloader" while US claims "Setup"; connection is indirect through SPEC. | Traceability / Broken Link | Medium |
| 11 | L0/L1 | SYSP_US_SETUP, SYSP_US_INSTALLER | Setup/Installer bifurcation complexity: Both stories in same RST file; INSTALLER links to AGENT_ARCH + SETUP (asymmetric); Installer REQs intermixed with Setup REQs in `req_setup_engineer.rst`. Intentional but undocumented; creates indirect L0→L1 chain. | Orchestration / Traceability | Medium |

---

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | defer | System Designer scope extends beyond this CR. Document architectural dependency in SYSP_US_AGENT_ARCH epic; assign as separate CR. |
| 2 | 2 | defer | Test ownership and QA framework is architectural; assign as separate CR focusing on test discipline and coverage gates. |
| 3 | 3 | defer | CM/VERIFY orchestration refinement is separate CR work; current separation (intent→spec vs. spec→verification) is intentional, needs explicit documentation. |
| 4 | 4 | defer | Alignment ownership boundaries need explicit definition in agent specs; assign as separate CR refining CM and IMPLEMENT role descriptions. |
| 5 | 5 | defer | Setup/Installer handoff formalization is separate CR; current implicit boundary is workable but should be documented in acceptance criteria. |
| 6 | 6 | defer | Documentation strategy is product-level decision; assign as separate roadmap item for SYSP_US_DOCU epic. |
| 7 | 7 | defer | Post-merge automation workflow is infrastructure decision; defer to Setup Agent refinement CR. |
| 8 | 8 | defer | Abort/rollback workflow is process design; defer to PM + CM orchestration epic. |
| 9 | 9 | defer | Spec status ownership requires System Designer inclusion; defer with Finding #1 (System Designer scope). |
| 10 | 10 | fix-now | **ACTION REQUIRED:** Update `docs/syspilot/requirements/req_setup_engineer.rst`: Add `:links: SYSP_US_SETUP` to SYSP_REQ_SETUP_BOOTLOADER_DUTIES frontmatter to establish bi-directional traceability. |
| 11 | 11 | defer | Document intentional Setup/Installer bifurcation in SYSP_US_AGENT_ARCH; clarify orchestration layer design in separate CR. |

---

**Summary for PM:**
- ✅ **Translation CR is clean** — Verification passed; ready for merge.
- ⚠️ **Structural issues identified** — 10 deferred, 1 fix-now (traceability uplink).
- 📋 **Next steps:** Fix Finding #10 before merge. Remaining findings are architectural dependencies for future CRs.

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
