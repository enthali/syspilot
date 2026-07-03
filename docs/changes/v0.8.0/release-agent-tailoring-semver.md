# Change Document: release-agent-tailoring-semver

**Status**: complete
**Branch**: feature/release-agent-tailoring-semver
**Created**: 2026-07-02
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

The Release Agent currently hardcodes a specific versioning scheme (CalVer, `vYYYY.MM.DD`) directly into its product spec, with no mechanism for a project to override it — unlike other agents (e.g. PM), the Release Agent has no Preflight/Tailoring Workflow step at all. This caused a real incident: CalVer silently applied to a customer project (Jarvis) whose `package.json` requires semver for VS Code extension packaging, breaking their release tooling (see GH #44). Motivation: give the Release Agent the same Tailoring Workflow pattern already used by PM, so the versioning scheme (and any other release convention that legitimately varies per project) becomes a per-project tailoring decision instead of a product-wide prescription. As part of this change, syspilot's own project instance is tailored back to semantic versioning (semver), reverting its prior CalVer choice. Acceptance criteria: the Release Agent spec defines a generic, tailorable approach to determining the next version rather than hardcoding one scheme; a missing tailoring file triggers the same Tailoring Workflow interview PM already uses; syspilot's own tailoring file specifies semver; no project's versioning scheme can silently apply to a different project again.

**Note for CM:** the user has requested interactive checkpoints only at the System Designer (L2 Design) stage of this change — all other stages (UAT, Implementation, Verification, Documentation) should proceed without stopping for approval.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_RELEASE | Release Engineer Agent | modified | Duties/Workflow/ACs genericized: validation moved first and made tailorable; version read from `docs/changes/` archive (not syspilot's own framework version); version write-target tailorable; branch retention delegated to branching skill (default retain) |
| SYSP_US_SKILL_ARCH | Skill Architecture | modified | +AC-8/9: generic Skill Tailoring capability (`tailoring.md` sibling file, no RESPOND-escalation — every Skill convention has a safe default) |
| SYSP_US_SKILL_BRANCHING | Clear Branching Rules for Agents | modified | +AC-6: feature-branch retention default flipped to retain; deletion is an explicit tailoring opt-in |

### New User Stories

None.

### Decisions

- **Version source-of-truth correction:** syspilot's own framework version marker (`version:` in `syspilot.setup.agent.md`) was a category error as the Release Engineer's version source — it identifies which syspilot release is installed, not the customer project's own product version. Corrected to read from the latest `docs/changes/<version>/` archive folder, universal across all syspilot projects.
- **Feature-branch retention default flipped to retain** (was: delete). Consistent with this codebase's established caution around not destroying customer artifacts without explicit configuration (cf. installer-scoped-cleanup CR). Deletion is now an explicit tailoring opt-in.
- **Generic Skill Tailoring introduced** as a reusable architecture-level concept (`SYSP_US_SKILL_ARCH` / `SYSP_REQ_SKILL_ARCH_TAILORING` / `SYSP_SPEC_SKILL_ARCH_TAILORING`), applied concretely to the branching skill in this CR. Simpler semantics than Agent tailoring: no RESPOND-escalation, since every Skill convention has a safe default.
- **Design guideline established:** agent/skill prose (Preflight/Workflow/Duties) must stay minimal and project-neutral — no embedded spec/req IDs, no concrete illustrative examples (file paths, tool names, scheme names). That content gets copied near-verbatim into the actual `.agent.md`/`SKILL.md`, which has zero access to the spec repo. Saved to System Designer's persistent memory.
- **Scope expansion (user-approved, twice):** (1) branching-skill review, justified because Release Engineer's delegated steps (merge, back-merge, retention) don't work if the skill itself can't be tailored; (2) removal of the branching skill's "Workflow Sequence" section — Skills define static conventions/permissions, not agent-attributed sequential workflows (that's Agent-file territory).
- **Stale fact corrections (fold-ins, CM/PM-approved):** (a) branch creation is `@syspilot.pm`'s responsibility, not `@syspilot.design`'s — fixed in L1 Naming req and L2 Permissions table; (b) Hard Rule clarified: feature branches are created from `development`, not ambiguously; (c) `@syspilot.setup` Permissions row was stale (`update/v{version}` branch creation no longer exists — Installer uses a pre-install/final-commit transactional model on whichever branch is checked out, no dedicated branch) — corrected to `@syspilot.installer`.
- **Flagged, not fixed (per CM's scope boundary):** the `update/v{version}` branch-naming convention itself (L1 `SYSP_REQ_SKILL_BRANCHING_NAMING`) may also be vestigial given the Permissions-table finding above, but auditing/fixing that is explicitly out of this CR's scope. Recommended as a candidate follow-up CR for a systematic Trace/MECE Engineer audit of the whole branching-permissions table, since two stale rows were found by inspection rather than systematic review.
- **Mermaid vs. ASCII diagrams:** user prefers Mermaid diagrams in spec RSTs (already used in deployed instance files, e.g. `SKILL.md`'s gitGraph) over the ASCII art currently used in spec RSTs (e.g. `SYSP_SPEC_SKILL_BRANCHING_STRATEGY`'s diagram). Flagged to PM as a separate backlog item — not in this CR's scope.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_RELEASE_DUTIES | SYSP_US_RELEASE | modified | Generic validation suite; archive-based version identity; tailored branch retention |
| SYSP_REQ_RELEASE_WORKFLOW | SYSP_US_RELEASE | modified | Validate-first ordering; archive-based version source + tailored write-target; branching-skill delegation; new :links: to SYSP_REQ_SKILL_BRANCHING_CHAINED/_RETENTION |
| SYSP_REQ_SKILL_ARCH_TAILORING | SYSP_US_SKILL_ARCH | new | Generic Skill Tailoring Contract |
| SYSP_REQ_SKILL_BRANCHING_RETENTION | SYSP_US_SKILL_BRANCHING | new | Feature-branch retention policy (default: retain) |
| SYSP_REQ_SKILL_BRANCHING_NAMING | SYSP_US_SKILL_BRANCHING | modified | Fixed stale attribution: `@syspilot.pm` creates feature branches (was `@syspilot.design`); clarified feature branches are created from `development` |
| SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION | SYSP_US_SKILL_BRANCHING | modified | AC-4 clarified: feature branch created from `development` |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_SKILL_ARCH_TAILORING | Skill Tailoring Contract | SYSP_US_SKILL_ARCH | mandatory |
| SYSP_REQ_SKILL_BRANCHING_RETENTION | Feature Branch Retention Policy | SYSP_US_SKILL_BRANCHING; SYSP_REQ_SKILL_ARCH_TAILORING | mandatory |

### Conflicts Detected

None.

### Decisions

- See L0 Decisions — same rationale cascades to L1.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_RELEASE_DUTIES | SYSP_REQ_RELEASE_DUTIES | modified | Duties bullets genericized (Build Validity, Consistent Version Identity, Tailored Branch Retention) |
| SYSP_SPEC_RELEASE_WORKFLOW | SYSP_REQ_RELEASE_WORKFLOW | modified | Full redesign: Preflight added; Validate moved to Step 2; archive-based version source (Step 3); tailored write-target (Step 5); branching-skill delegation (Steps 7/9/10); all prose stripped of embedded spec IDs and concrete examples |
| SYSP_SPEC_SKILL_ARCH_TAILORING | SYSP_REQ_SKILL_ARCH_TAILORING | new | Generic tailoring-file convention for Skills (`tailoring.md` colocated with `SKILL.md`) |
| SYSP_SPEC_SKILL_BRANCHING_STRATEGY | SYSP_REQ_SKILL_BRANCHING_CHAINED | modified | "Workflow Sequence" section removed entirely (agent-attributed sequencing is Agent-file territory, not Skill territory); Key Properties retained as-is |
| SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS | SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION; SYSP_REQ_SKILL_BRANCHING_NAMING | modified | Fixed two stale rows: `@syspilot.design`→`@syspilot.pm` for feature-branch creation; `@syspilot.setup`→`@syspilot.installer` with corrected pre-install/final-commit description (no dedicated branch); Hard Rule clarified (branch from `development`) |
| SYSP_SPEC_SKILL_BRANCHING_RETENTION | SYSP_REQ_SKILL_BRANCHING_RETENTION | new | Feature-branch retention policy spec (default: retain; tailorable to delete) |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_SKILL_ARCH_TAILORING | Skill Tailoring File | SYSP_REQ_SKILL_ARCH_TAILORING |
| SYSP_SPEC_SKILL_BRANCHING_RETENTION | Feature Branch Retention Policy | SYSP_REQ_SKILL_BRANCHING_RETENTION; SYSP_SPEC_SKILL_ARCH_TAILORING |

### Conflicts Detected

None.

### Decisions

- See L0 Decisions for full rationale (version source-of-truth correction, retention default flip, Skill Tailoring architecture, Workflow Sequence removal, stale-fact fold-ins, project-neutrality prose guideline).

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements
- [x] Branching skill's static conventions (Definition, Key Properties, Permissions, Retention) are cleanly separated from Agent-file workflow concerns

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_RELEASE | SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW | SYSP_SPEC_RELEASE_DUTIES, SYSP_SPEC_RELEASE_WORKFLOW | ✅ |
| SYSP_US_SKILL_ARCH | SYSP_REQ_SKILL_ARCH_TAILORING | SYSP_SPEC_SKILL_ARCH_TAILORING | ✅ |
| SYSP_US_SKILL_BRANCHING | SYSP_REQ_SKILL_BRANCHING_RETENTION, SYSP_REQ_SKILL_BRANCHING_NAMING, SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION | SYSP_SPEC_SKILL_BRANCHING_STRATEGY, SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS, SYSP_SPEC_SKILL_BRANCHING_RETENTION | ✅ |

sphinx-build `-W` passes clean (EXIT=0) across every incremental change in this CR, including the CM/PM fold-in fixes. All traceability links resolve.

### Artefakt-Removal-Check

This CR removes no artefact (file, field, configuration key, or REQ-ID). It genericizes existing behavior (Release Engineer versioning/validation/retention) and removes one section ("Workflow Sequence" from `SYSP_SPEC_SKILL_BRANCHING_STRATEGY`) that duplicated Agent-file content — not a product artefact in the removal-check sense.

- [x] N/A — no artefact removed

### Issues Found

- **Flagged for follow-up (not fixed, per CM's explicit scope boundary):** the `update/v{version}` branch-naming convention (`SYSP_REQ_SKILL_BRANCHING_NAMING`) may be vestigial alongside the Permissions-table finding already fixed in this CR. Two stale rows were found by inspection, not systematic review — recommend a follow-up CR routing a full Trace/MECE Engineer audit of `SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS` and related naming conventions.
- **Scope bleed (discarded by CM):** working tree carried uncommitted, out-of-scope, unrelated changes to `.github/agents/syspilot.pm.agent.md` and `.github/agents/syspilot.pm.tailoring.md` (an unrelated "Parallel CR Drafting" feature, likely stray state from another session). The `.agent.md` diff additionally contained a corruption bug — `syspilot.branching` truncated to `syspilot.` in three places. Both files discarded via `git restore` before committing this CR's spec work; no committed history affected.
- **Second scope bleed (discarded by CM):** after Dev Engineer's implementation commit, working tree carried a stray uncommitted change to `.github/agents/syspilot.setup.agent.md` adding a `name:` field — Dev Engineer correctly identified it as pre-existing and out of scope and left it uncommitted, but it also **contradicts** `SYSP_REQ_AGENT_ARCH_FRONTMATTER` AC-7 (Setup Bootloader is exempt from session-identity frontmatter). Discarded via `git restore`; no committed history affected.
- **Implementation tasks for Dev Engineer (not done by System Designer, per established precedent):**
  - `.github/agents/syspilot.release.tailoring.md` (syspilot's own instance file, specifying semver)
  - `.github/skills/syspilot.branching/tailoring.md` (syspilot's own instance file, if any override is desired)
  - Update deployed `.github/skills/syspilot.branching/SKILL.md` to match the spec: remove "Workflow Sequence", add Retention policy section, fix stale attributions, remove embedded spec-ID citations
  - Update deployed `.github/agents/syspilot.release.agent.md` to match the redesigned `SYSP_SPEC_RELEASE_WORKFLOW`

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation (with the flagged items above disclosed for CM/PM routing)

---

## UAT

**Status**: ✅ completed

### Summary

Commit `3a9f228`. `SYSP_US_UAT_RELEASE_TAILORING_SEMVER` (+ req/spec) — 7 executable scenarios: no-hardcoded-scheme, archive-based version source-of-truth, missing-tailoring-file escalation, syspilot's own semver tailoring, GH #44 cross-project isolation regression test, Skill Tailoring architecture genericity, feature-branch retention default.

### Issues Found

- None.

---

## Implementation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `syspilot/agents/syspilot.release.agent.md` | Product source — Tailoring Workflow, validate-first ordering, archive-based version source, branching-skill delegation |
| `.github/agents/syspilot.release.agent.md` | Installed instance — kept in sync |
| `syspilot/skills/syspilot.branching/SKILL.md` | Product source — Skill Tailoring applied, retention section, fixed attributions |
| `.github/skills/syspilot.branching/SKILL.md` | Installed instance — kept in sync |
| `.github/agents/syspilot.release.tailoring.md` | New, instance-only — syspilot's own semver tailoring |

### Issues Found

- Two scope-bleed incidents (unrelated stray changes to `syspilot.pm.agent.md`/`syspilot.pm.tailoring.md`, and to `syspilot.setup.agent.md`) discarded by CM mid-pipeline — see Issues Found under Final Consistency Check for full disclosure. Verified absent from all committed history by Verify Engineer.

---

## Documentation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `docs/architecture.md` | New "Skill Tailoring" section documenting `SYSP_SPEC_SKILL_ARCH_TAILORING` (closes GH #43 documentation AC) |
| `docs/workflows.md` | Corrected stale version-source claim (Release Workflow step 1) and stale branch-cleanup claim (Branching Strategy table + step 8) |

### Reviewed, No Change Needed

- `README.md` — no versioning-scheme claims
- `docs/methodology.md` — no tailoring-pattern references yet to update

### Issues Found

- None.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** Quality Manager
**Review date:** 2026-07-02
**Scope:** Full targeted check — scope-expansion legitimacy, GH #44 regression test genuineness, independent scope-bleed verification, Skill Tailoring genericity, L0/L1/L2 traceability, schema.

#### Findings

No findings.

#### Validation Notes

- **Scope expansion legitimacy**: Both disclosed expansions (branching-skill review; removal of "Workflow Sequence" from the branching skill) are coherent extensions of the core intent — the Release Engineer's delegated retention/merge steps cannot function without a tailorable branching skill underneath them, and moving sequence-of-work content out of a Skill (which defines static conventions, not agent-attributed workflows) is an architectural correction consistent with the Agent/Skill separation already established elsewhere. Both were disclosed as user-approved at the L2 checkpoint per the CD's own "Note for CM." Not retrospective scope creep. ✅
- **GH #44 regression test genuineness**: Independently reviewed `SYSP_US_UAT_RELEASE_TAILORING_SEMVER` AC-5. The scenario recreates the actual incident conditions — two independent projects, each with its own tailoring file specifying a different versioning scheme, verified to produce isolated release artifacts with no cross-project leakage. This directly targets the root cause (previously: one hardcoded scheme in product spec, forced onto every installed project) and would have caught the original incident had it existed beforehand. Genuine, not superficial. ✅
- **Scope-bleed independent verification**: Ran `git diff experimental...feature/release-agent-tailoring-semver` for `syspilot/agents/syspilot.pm.agent.md`, `.github/agents/syspilot.pm.agent.md`, `.github/agents/syspilot.pm.tailoring.md`, `syspilot/agents/syspilot.setup.agent.md`, `.github/agents/syspilot.setup.agent.md` — **zero diff** across the entire branch, confirmed independently (not just trusting the CD narrative). `git log --all` confirms the last commits touching these files all pre-date this CR. Working tree (`git status --short`) carries no stray uncommitted changes to these files either. Both disclosed scope-bleed incidents are genuinely and fully discarded. ✅
- **Skill Tailoring architecture genericity**: `SYSP_SPEC_SKILL_ARCH_TAILORING` and `SYSP_REQ_SKILL_ARCH_TAILORING` define the tailoring mechanism (file location, absent/empty/present-with-content behavior, instance-only ownership, no-escalation rationale) with zero branching-specific assumptions in the normative text — the only mention of branching is a labeled illustrative example (`.github/skills/syspilot.branching/tailoring.md`), which is appropriate and does not leak into the generic contract. ✅
- **L0/L1/L2 traceability**: All new and modified elements verified via `needs.json` — `SYSP_US_RELEASE`, `SYSP_US_SKILL_ARCH`, `SYSP_US_SKILL_BRANCHING`, all six impacted/new REQs, all six impacted/new SPECs, and the full UAT chain (`SYSP_US_UAT_RELEASE_TAILORING_SEMVER` → REQ → SPEC) all resolve with correct parent links. ✅
- **Deployed artefacts match spec**: `.github/skills/syspilot.branching/SKILL.md` confirmed to have "Workflow Sequence" fully removed, Retention section present, Permissions table correctly attributes `@syspilot.pm` (feature-branch creation) and `@syspilot.installer` (pre-install/final-commit, no dedicated branch). `.github/agents/syspilot.release.tailoring.md` confirmed present and correctly specifies semver with a clear MAJOR/MINOR/PATCH rubric. `syspilot/agents/syspilot.release.agent.md` confirmed free of embedded spec IDs and concrete scheme names (CalVer/semver), consistent with the CD's stated project-neutrality prose guideline. ✅
- **Known, disclosed inconsistency confirmed (not a new finding)**: `SYSP_REQ_SKILL_BRANCHING_NAMING` and the deployed SKILL.md's "Branch Naming Conventions" table both still attribute `update/v{version}` branch creation to `@syspilot.setup` — which the now-corrected Permissions table's own reasoning suggests is likely vestigial (no dedicated `update/v{version}` branch is created under the corrected Installer model). This is exactly the item the CD explicitly flags as "not fixed, per CM's scope boundary" with a recommended follow-up CR. QM independently confirms the disclosure is accurate and complete — this is not a hidden gap. No new finding needed; recommend PM prioritize the suggested follow-up CR (systematic Trace/MECE audit of `SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS` and related naming conventions).
- **Schema**: sphinx-needs validation — 0 warnings. ✅

**Verdict: CLEAN. All acceptance criteria met. No findings.**

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| — | — | — | No findings — no decisions required. |

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
