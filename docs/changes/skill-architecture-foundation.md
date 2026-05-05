# Change Document: skill-architecture-foundation

**Status**: in-progress
**Branch**: feature/skill-architecture-foundation
**Created**: 2026-05-03
**Author**: syspilot.cm

---

## Summary

Skill Architecture is anchored as an architectural component in the
spec hierarchy alongside Agent Architecture. A new `SYSP_US_SKILL_ARCH`
User Story and `SYSP_REQ_SKILL_DEFINITIONS` Requirement are created.
`docs/syspilot/conventions.md` documents Agent and Skill conventions for
implementers, including the DEFINITIONS Dictionary pattern and Mutual
Exclusion per group.

---

## Change Request (from PM)

> **Mode:** autonomous
>
> **WHAT:** Skills are already used productively but lack an architectural
> anchor in the spec hierarchy. Skill Architecture shall be anchored as an
> equal architectural component alongside Agent Architecture. An official
> conventions document shall describe Agent and Skill conventions for
> implementers.
>
> The key insight from Research: Agents use generic verbs (`invoke`,
> `delegate to`), while Skills provide project-specific DEFINITIONS (always
> in uppercase). A static DEFINITIONS Dictionary at L1 is the contract
> between Agent and Skill.
>
> **WHY:** The Adapter Pattern (exchangeable Skill variants per group) is
> fully thought through and shall be anchored spec-side. Without an L0
> anchor for Skill Architecture, subsequent CRs (Impact Analysis,
> Orchestration, Release as Skills) cannot be specified cleanly. Users
> need a Conventions reference to create their own Skills correctly.
>
> **Acceptance Criteria:**
> 1. New User Story `SYSP_US_SKILL_ARCH` exists, describing Skills as
>    exchangeable specializations of Agents (goal + capability — no
>    implementation details like `group` or DEFINITIONS names)
> 2. `SYSP_US_SKILL_ARCH` links to `SYSP_US_AGENT_ARCH`
> 3. `SYSP_US_AGENT_ARCH` mentions that Agents can be specialized by Skills
> 4. New Requirement `SYSP_REQ_SKILL_DEFINITIONS` defines the DEFINITIONS
>    Dictionary concept: static contract between Agent and Skill, maintained
>    per Skill group with Name/Type/Required/Description per DEFINITION
> 5. `docs/syspilot/conventions.md` exists covering:
>    - Agent Conventions (roles, frontmatter fields, generic verbs invoke/delegate)
>    - Skill Conventions (frontmatter with name/group, DEFINITIONS pattern,
>      uppercase convention, Mutual Exclusion per group, variants)
>    - DEFINITIONS Dictionary reference (at least Release group as example)
>    - Note where already implemented and where still pending
> 6. Sphinx Build clean

---

## Impact Analysis (CM)

**Performed**: 2026-05-03
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_AGENT_ARCH.

**From SYSP_US_AGENT_ARCH (existing linked elements):**
- Existing REQs: SYSP_REQ_AGENT_ARCH_SOUL, _DUTIES, _WORKFLOW, _FRONTMATTER, _PROMPT
- Existing skill USes already present: SYSP_US_SKILL_IMPACT, SYSP_US_SKILL_ORCHESTRATION, etc.

**Modified existing elements:**
- `SYSP_US_AGENT_ARCH` — add mention of Skills specialization (AC-3)

**New elements to create:**
- `SYSP_US_SKILL_ARCH` — new User Story (AC-1, AC-2); expanded during review to cover inner Skill structure
- `SYSP_US_DOC_CONVENTIONS` — new User Story for conventions doc (AC-5)
- `SYSP_REQ_SKILL_ARCH_FRONTMATTER` — inner Skill structure (added during review)
- `SYSP_REQ_SKILL_ARCH_INSTRUCTIONS` — inner Skill structure (added during review)
- `SYSP_REQ_SKILL_ARCH_RULES` — inner Skill structure (added during review)
- `SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY` — group exchangeability guarantee (added during MECE fix)
- `SYSP_REQ_SKILL_DEFINITIONS` — global DEFINITIONS Dictionary (AC-4)
- `SYSP_REQ_DOC_CONVENTIONS` — conventions doc requirement (AC-5)
- `SYSP_SPEC_SKILL_ARCH_FRONTMATTER` — inner Skill structure design
- `SYSP_SPEC_SKILL_ARCH_INSTRUCTIONS` — inner Skill structure design
- `SYSP_SPEC_SKILL_ARCH_RULES` — inner Skill structure design
- `SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY` — group exchangeability design (added during trace fix)
- `SYSP_SPEC_SKILL_DEFINITIONS` — global DEFINITIONS Registry (needtable)
- `SYSP_SPEC_DOC_CONVENTIONS` — conventions doc design anchor
- `docs/syspilot/conventions.md` — plain Markdown reference doc (AC-5)
- `docs/conf.py` change: new need-type `def`, new extra link `defines`

**Where to create new specs:**
- SYSP_US_SKILL_ARCH → new file `docs/syspilot/userstories/us_skill_arch.rst`
  or add to existing skill US file
- SYSP_REQ_SKILL_DEFINITIONS → new or existing skill requirements file
- SYSP_SPEC_SKILL_DEFINITIONS → new or existing skill design file

**Research context:**
Full research at `.jarvis/project-manager/research-skill-adapter.md` —
contains DEFINITIONS examples, invoke/delegate semantics, group/mutual-exclusion
decisions.

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/skill-architecture-foundation |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | 740dd45 | us_skill_arch.rst created; us_agent_arch.rst updated |
| Design (L1) | syspilot.design | ✅ | 7cbcc22 | req_skill_definitions.rst created |
| Design (L2) | syspilot.design | ✅ | 9c8de6b | spec_skill_definitions.rst + conventions.md created |
| L2 SPEC_DOC_CONVENTIONS | CM | ✅ | bbe2775 | conventions.md anchored in DOC traceability chain |
| Sphinx exclude conventions.md | CM | ✅ | dac5770 | toctree warning resolved |
| L1+L2 refactor (global Registry) | CM | ✅ | 75b6330 | Per-group → global Dictionary; Release example removed |
| Refactor (drop Type/Required) | CM | ✅ | 17d8678 | Registry: DEFINITION/Group/Description only |
| 1-degree hub pattern | CM | ✅ | 061daa9 | Group Contract Spec as intermediary |
| def needs + defines link | CM | ✅ | 5e8867c | DEFINITIONS as `def` needs; `:defines:` extra link; needtable |
| Skill inner structure (REQ+SPEC) | CM | ✅ | e91de23 | FRONTMATTER/INSTRUCTIONS/RULES; US expanded; group optional |
| MECE fixes F-01..F-05 | CM | ✅ | 028736f | group optional, SUBSTITUTABILITY REQ, AC-4 realigned, Rules no-dup, AC-6 pointer |
| Trace fix (SUBSTITUTABILITY SPEC) | CM | ✅ | 1f76fdf | SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY added |
| Implement | syspilot.implement | — | — | No code changes; Sphinx infra only (conf.py) |
| MECE verify | syspilot.mece | ✅ | — | 8 findings; F-01..F-05 fixed; F-06..F-08 advisory/deferred |
| Trace verify | syspilot.trace | ✅ | — | 1 finding (SUBSTITUTABILITY SPEC); fixed in 1f76fdf |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_AGENT_ARCH` | Clean Agent Architecture | modified | Added paragraph: Agents can be specialized by Skills |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| `SYSP_US_SKILL_ARCH` | Skill Architecture | mandatory |
| `SYSP_US_DOC_CONVENTIONS` | Agent and Skill Conventions Reference | mandatory |

### Designer Section

**Decisions:**
- `SYSP_US_SKILL_ARCH` created in new file `docs/syspilot/userstories/us_skill_arch.rst`
- Links to `SYSP_US_AGENT_ARCH` via `:links:` field (downward link: skill US → agent US)
- Content stays at L0: describes goal (exchangeable specializations) and key capabilities
  (exchangeability, specialization, portability) — no mention of `group`, DEFINITIONS names,
  mutual exclusion mechanics, or uppercase convention (all L1/L2)
- `SYSP_US_AGENT_ARCH` updated: added one paragraph stating agents can be specialized by Skills
- `us_skill_arch` added to toctree immediately after `us_agent_arch`
- **Review expansion:** during review it became clear `SYSP_US_SKILL_ARCH` only described
  Skill exchangeability but not what a Skill *is*. US rewritten with two concern groups:
  (1) Inner Structure — Frontmatter/Instructions/Rules (ACs 1–4, mandatory for all Skills);
  (2) Group + DEFINITIONS (ACs 5–7, optional). Group and DEFINITIONS explicitly optional.
- `SYSP_US_DOC_CONVENTIONS` added to `docs/syspilot/userstories/us_documentation.rst`
  (links to `SYSP_US_DOC_EXTERNAL`, `SYSP_US_SKILL_ARCH`, `SYSP_US_AGENT_ARCH`)

---

## Level 1: Requirements

**Status**: ✅ done (refactored)

### New Requirements

| ID | Title | Links |
|----|-------|-------|
| `SYSP_REQ_SKILL_ARCH_FRONTMATTER` | Skill Frontmatter Definition | SYSP_US_SKILL_ARCH |
| `SYSP_REQ_SKILL_ARCH_INSTRUCTIONS` | Skill Instructions Definition | SYSP_US_SKILL_ARCH |
| `SYSP_REQ_SKILL_ARCH_RULES` | Skill Rules Definition | SYSP_US_SKILL_ARCH |
| `SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY` | Skill Group Substitutability | SYSP_US_SKILL_ARCH |
| `SYSP_REQ_SKILL_DEFINITIONS` | Global DEFINITIONS Dictionary | SYSP_US_SKILL_ARCH |
| `SYSP_REQ_DOC_CONVENTIONS` | Agent and Skill Conventions Documentation | SYSP_US_DOC_CONVENTIONS |

### Designer Section

**Decisions (initial):**
- `SYSP_REQ_SKILL_DEFINITIONS` created in new file
  `docs/syspilot/requirements/req_skill_definitions.rst`
- `req_skill_definitions` added to toctree after `req_agent_arch`

**Refactor (CM, after user review):**
- Initial design defined a *per-group* Dictionary. Discussion surfaced that
  Skills are loaded based on the DEFINITIONS they declare — if two groups
  declared the same DEFINITION name, Skill resolution would be ambiguous.
- Requirement reframed as **one global DEFINITIONS Dictionary** with global
  uniqueness of DEFINITION names as the load-time invariant.
- Group is the Mutual-Exclusion boundary and Interface contract: all Skills
  of the same group implement the same DEFINITIONS, only one installed.
- ACs updated multiple times across the session as the model sharpened.

**Further refactors during the session:**
- *Drop `Type`/`Required` columns:* both proved unhelpful. `Type` doesn't
  capture semantics (e.g. `git commit` vs. `git squash commit` are both
  `Command`). Every DEFINITION an Agent references is by definition
  required — there is no "half-required". Registry kept just three
  columns: DEFINITION / Group / Description.
- *1-degree hub pattern:* avoid Skills/Agents linking directly to the
  Registry (would make Registry a hub of all links). Introduced
  Group Contract Spec as intermediary. Registry has ≤ N inbound links
  (one per group); Skills link to Contract; Agents link to Contract.
- *DEFINITIONS as sphinx-needs `def` needs:* user observed the Registry
  table duplicated data that Group Contracts already had. Solution:
  publish each DEFINITION as a `def` need (ID `SYSP_DEF_<NAME>`) on the
  Registry page. Group Contracts reference them via a new `:defines:`
  extra link type. ID uniqueness is enforced structurally by sphinx-needs
  (collision → build fail). The Registry page renders all DEFINITIONS
  via `needtable` — no manual table to maintain. AC-2 reframed as a
  build-time invariant rather than a manual review step.

**SYSP_REQ_DOC_CONVENTIONS:**
- Added to `docs/syspilot/requirements/req_documentation.rst` to anchor the
  conventions doc in the existing DOC traceability chain (no separate
  documentation US needed — same pattern as External / Internal docs).

**Review expansion — Skill inner structure (commit e91de23):**
- After initial spec writing it became clear `SYSP_US_SKILL_ARCH` only described
  Skill exchangeability, not what a Skill *is*. Pattern: Agents have
  Soul/Duties/Workflow; Skills need an analogous structure.
- New file `docs/syspilot/requirements/req_skill_arch.rst` with:
    - `SYSP_REQ_SKILL_ARCH_FRONTMATTER` — `name`/`description` mandatory;
      `group`/`tools`/`triggers` optional; group absent for standalone Skills
    - `SYSP_REQ_SKILL_ARCH_INSTRUCTIONS` — LLM-facing body; imperative;
      names tools, describes outcome
    - `SYSP_REQ_SKILL_ARCH_RULES` — hard constraints; explicit no-rules
      statement required; no duplication of rules in Instructions
- `req_skill_arch` inserted in toctree after `req_agent_arch` and before
  `req_skill_definitions`

**MECE fix — SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY (commit 028736f):**
- MECE agent (F-02) found US AC-7 (substitutability guarantee) had no L1 REQ.
- Added `SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY`: any Skill implementing all
  DEFINITIONS of its Group Contract is substitutable; the Agent requires
  no modification on Skill swap.

---

## Level 2: Design

**Status**: ✅ done (refactored)

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| `SYSP_SPEC_SKILL_ARCH_FRONTMATTER` | Skill Frontmatter Structure | SYSP_REQ_SKILL_ARCH_FRONTMATTER |
| `SYSP_SPEC_SKILL_ARCH_INSTRUCTIONS` | Skill Instructions Section | SYSP_REQ_SKILL_ARCH_INSTRUCTIONS |
| `SYSP_SPEC_SKILL_ARCH_RULES` | Skill Rules Section | SYSP_REQ_SKILL_ARCH_RULES |
| `SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY` | Skill Group Substitutability | SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY |
| `SYSP_SPEC_SKILL_DEFINITIONS` | Global DEFINITIONS Registry (needtable) | SYSP_REQ_SKILL_DEFINITIONS |
| `SYSP_SPEC_DOC_CONVENTIONS` | Agent and Skill Conventions Reference Structure | SYSP_REQ_DOC_CONVENTIONS, SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_SKILL_DEFINITIONS |

### New Documentation

| File | Description |
|------|-------------|
| `docs/syspilot/conventions.md` | Agent + Skill conventions reference (excluded from Sphinx toctree via `conf.py`) |

### Designer Section

**Decisions (initial):**
- `SYSP_SPEC_SKILL_DEFINITIONS` created in `docs/syspilot/design/spec_skill_definitions.rst`
- Initial spec contained: column schema, Release group example Dictionary,
  group implementation status, Mutual Exclusion mechanism, UPPERCASE convention
- `conventions.md` created as plain Markdown
- `spec_skill_definitions` added to design toctree
- `conventions.md` excluded from toctree via `exclude_patterns` in `conf.py`

**Refactor (CM, after user review):**
- `SYSP_SPEC_SKILL_DEFINITIONS` reshaped multiple times during the session:
    - First: per-group example (Release Dictionary inline) — removed as
      premature, belongs in the Release Skill CR.
    - Then: global Registry as a manual table (DEFINITION/Group/Description).
    - Finally: Registry as a **`needtable`** that auto-renders all `def`
      needs on the page. DEFINITIONS are sphinx-needs first-class objects,
      not table rows.
- New mechanisms in `conf.py`:
    - Need-type `def` (directive `.. def::`, prefix `DEF_`).
    - Extra link type `defines` (incoming "is defined by", outgoing "defines").
- Group Contract Specs (created by future Skill CRs) will use
  `:defines: SYSP_DEF_X, SYSP_DEF_Y, ...` to declare which DEFINITIONS
  belong to the group. No content duplication — Contract just references
  the `def` needs.
- `conventions.md` updated to reflect the `def` need pattern with a
  concrete RST example for the next Skill author.

**SYSP_SPEC_DOC_CONVENTIONS:**
- Added to `docs/syspilot/design/spec_doc_scope.rst` to give the conventions
  doc its L2 anchor (parallel to other DOC specs like
  `SYSP_SPEC_DOC_NAMINGCONVENTIONS`).
- Lists required sections (Agent Conventions, Skill Conventions, DEFINITIONS
  Registry reference using `def` needs and `:defines:` link).
- Notes the doc is intentionally excluded from Sphinx output.

**Review expansion — Skill inner structure SPECs (commit e91de23):**
- New file `docs/syspilot/design/spec_skill_arch.rst` with:
    - `SYSP_SPEC_SKILL_ARCH_FRONTMATTER` — YAML schema with required/optional
      fields; annotated examples for standalone and group-member Skills
    - `SYSP_SPEC_SKILL_ARCH_INSTRUCTIONS` — required heading `## Instructions`;
      Purpose / Tools / Procedure / Outcome sub-structure; style rules
    - `SYSP_SPEC_SKILL_ARCH_RULES` — required heading `## Rules`; MUST/MUST NOT
      form; explicit no-rules statement; non-duplication constraint
- `spec_skill_arch` inserted in toctree after `spec_agent_arch` and before
  `spec_skill_definitions`

**Trace fix — SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY (commit 1f76fdf):**
- Trace agent found `SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY` had no covering SPEC.
- Added `SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY` to `spec_skill_arch.rst`:
  describes the mechanism (Agent → Contract → Skill), the substitution
  invariant (Group Contract unchanged; Agent unchanged; Skill B replaces Skill A),
  and enforcement (Setup Agent Mutual Exclusion check at install time).

---

## Final Consistency Check

**Status**: ✅ done

**Cross-level traceability:**
- `SYSP_US_SKILL_ARCH` → `:links: SYSP_US_AGENT_ARCH` (L0 horizontal link to anchor US)
- `SYSP_REQ_SKILL_DEFINITIONS` → `:links: SYSP_US_SKILL_ARCH` (L1 → L0)
- `SYSP_SPEC_SKILL_DEFINITIONS` → `:links: SYSP_REQ_SKILL_DEFINITIONS` (L2 → L1)

**MECE check (horizontal):**
- L0: `SYSP_US_SKILL_ARCH` is distinct from existing skill USes
  (SYSP_US_SKILL_ORCHESTRATION, _IMPACT, _BRANCHING, _ASK_QUESTIONS).
  Those describe individual skill capabilities; this describes the
  architectural pattern itself. No overlap.
- L1: `SYSP_REQ_SKILL_DEFINITIONS` is the only requirement for the
  DEFINITIONS Dictionary concept. Existing skill REQs do not overlap
  (they define skill-specific behavior, not the Dictionary contract).
- L2: `SYSP_SPEC_SKILL_DEFINITIONS` is the only spec for the Dictionary
  structure. `spec_agent_arch` covers agent structure, not DEFINITIONS.

**ACs verified against delivered state:**

| AC | Requirement | Delivered | Status |
|----|-------------|-----------|--------|
| AC-1 | `SYSP_US_SKILL_ARCH` exists, describes exchangeable specializations | ✅ — expanded to 7-AC US covering inner structure + group | ✅ + more |
| AC-2 | `SYSP_US_SKILL_ARCH` links to `SYSP_US_AGENT_ARCH` | ✅ | ✅ |
| AC-3 | `SYSP_US_AGENT_ARCH` mentions Skills | ✅ paragraph added | ✅ |
| AC-4 | `SYSP_REQ_SKILL_DEFINITIONS` with Name/Type/Required/Description | ⚡ Type+Required deliberately dropped (see refactor notes); `def`-needs + ID-uniqueness deliver a stronger guarantee | Deviation — accepted |
| AC-5 | `conventions.md` with Release group example | ⚡ Release example deferred to Release Skill CR (premature here); DEFINITIONS mechanism fully documented | Partial — Release example deferred |
| AC-6 | Sphinx Build clean | ✅ 0 warnings, 0 errors | ✅ |

**MECE findings summary:**
- F-01 critical ✅ fixed: `group` in conventions.md was marked mandatory; corrected to optional
- F-02 major ✅ fixed: `SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY` added
- F-03 major ✅ fixed: `SYSP_REQ_DOC_CONVENTIONS` AC-4 realigned to `def`-mechanism
- F-04 minor ✅ fixed: non-duplication constraint added to `SYSP_SPEC_SKILL_ARCH_RULES`
- F-05 minor ✅ fixed: AC-6 pointer to Group Status table made explicit
- F-06 advisory — deferred: PM AC-4 schema deviation undocumented (noted here instead)
- F-07 advisory — deferred: Setup Agent enforcement not forward-linked in SPEC
- F-08 advisory — deferred: conventions.md cross-references to spec rules

**Trace findings summary:**
- 1 blocker ✅ fixed: `SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY` was missing
- All links verified: L2→L1→L0 chains complete; all new USes covered; toctrees complete

---

## Sign-off

- [x] Design reviewed and approved by user (interactive session 2026-05-03..05)
- [x] MECE verify passed (F-01..F-05 fixed)
- [x] Trace verify passed
- [ ] PM approval received
- [ ] Merged to development
