# Change Document: agent-arch-duties-workflow-definition

**Status**: done
**Branch**: feature/agent-arch-duties-workflow-definition
**Created**: 2026-05-06
**Author**: Analyst (outside-loop repair — see "Process Note" below)

---

## Process Note — Read this first

This change document is **not** the product of the standard
PM → CM → Designer → Implement → QM loop. It is an **outside-loop repair**
performed by the Analyst session.

**What happened:**

1. Analyst (F-003) identified the architecture defect and recommended a
   narrow, spec-only CR to PM.
2. PM created this branch and this change document — and pre-filled the
   Impact Analysis (with verdicts), the Change Log (with phrasing), and the
   AC Verification (with checkmarks) **before any subagent had run**. PM
   also edited the RST files directly. None of this was visible from the CR
   text alone.
3. This is a textbook instance of Analyst observation **Obs-F (pre-baked
   specs antipattern)** — and it occurred *while authoring the very CR meant
   to remediate the antipattern's root cause*.

**Why Analyst stepped in:**

Asking PM/CM to redo this following the proper choreography would simply
reproduce the same antipattern (Analyst F-002 Finding 3: "more spec text in
agent files does not stick — the rules get read but not enforced"). The
defect-bearing system cannot author its own fix. Single explicit Analyst
intervention chosen over recursive failure.

**Scope of this intervention is strictly limited to:**

- The two REQs and two SPECs in the original CR scope.
- Honest authorship of this change document.
- No agent files touched. No process changes. No further out-of-loop edits.

**This intervention is logged as a follow-up Finding (F-004) in
`.jarvis/analyst/context.md`.** The behavioural defect this exposes is *not*
fixed by this CR and remains an open item for a future PM/CM agent rewrite.

---

## Summary

The meta-spec requirements `SYSP_REQ_AGENT_ARCH_DUTIES` and
`SYSP_REQ_AGENT_ARCH_WORKFLOW` did not establish a clear conceptual
separation between the two sections. Both described "customer-customizable
lists of agent behaviour", with the only operational distinction being
ordered vs. unordered — a notational convention, not a conceptual one. This
ambiguity structurally forced agent authors to duplicate content across both
sections (verified concretely on the freshly-written Setup Bootloader: 4
Duties = 4 Workflow steps, verbatim).

This CR corrects the definitions so each section answers a distinct,
non-overlapping question, and adds an explicit Mutual Exclusion constraint.

---

## Change Request (Intent Only) — original PM-commissioned scope

### WHAT

Clarify the definitions of `SYSP_REQ_AGENT_ARCH_DUTIES` and
`SYSP_REQ_AGENT_ARCH_WORKFLOW` so that each section answers a distinct,
non-overlapping question:

- **Duties** answers: *What is this agent accountable for?* (outcomes and
  responsibilities — short, unordered)
- **Workflow** answers: *How does this agent execute its work?* (ordered
  sequence of execution steps)

Add an explicit constraint to both requirements: a single behavioural item
SHALL appear in exactly one of the two sections, never both.

### WHY

Evidence from the newly written Setup Bootloader shows the defect in concrete
form: its 4 Duties have the same headlines as its 4 Workflow steps, verbatim.
Identical information lives in two mandatory sections because the spec does not
forbid — and in fact invites — this duplication.

Consequences of leaving the defect in place:

1. Every agent refactored before this spec is corrected will be authored
   against the wrong definition, accumulating rework.
2. Drift between the two copies of the same rule is built into the structure
   (root cause of "more spec text doesn't stick").
3. Agent instructions become longer without becoming clearer, degrading LLM
   instruction adherence.

### Scope

**In scope:** `SYSP_US_AGENT_ARCH` (the originating misnomer), the two
requirements `SYSP_REQ_AGENT_ARCH_DUTIES` / `SYSP_REQ_AGENT_ARCH_WORKFLOW`,
their corresponding SPECs, and this change document.

> **Scope expanded after CR creation:** the original CR scope omitted L0.
> Re-reading `SYSP_US_AGENT_ARCH` showed the root misnomer lives there:
> *"Duties (tasks)"* and *"Duties — customer-customizable task list"*. The
> downstream REQs/SPECs only carried the error forward. Fixing only L1/L2
> would have left the L0 source of the confusion intact, and any future
> agent author reading L0 first would have re-introduced the conflation.
> L0 added to scope on user decision (2026-05-06).

**Out of scope:** All agent files (CM, Bootloader, PM, QM, etc.). They
almost certainly violate the new Mutual Exclusion property — that is by
design. The follow-up CRs that bring agent files into conformance with the
corrected spec are NOT part of this CR.

### User-Visible Acceptance Criteria

1. An agent author reading the spec can unambiguously place any given
   behavioural item in exactly one section (Duties or Workflow) without
   consulting examples.
2. The spec explicitly states that a single behavioural item must not appear
   in both sections.
3. The definitions of Duties and Workflow answer different questions:
   accountability/outcomes vs. execution sequence.
4. No existing user stories are invalidated; traceability links are preserved.

### Target Release

Next available release after v0.5.3 (non-blocking).

---

## Record of Changes Made

> **What this section is:** A neutral, factual record of the diffs that
> reached this branch — written by Analyst after the fact. **It is not a
> Change Log in the standard sense** (which would be authored by the engineer
> who performed each phase). The standard Impact Analysis, AC Verification,
> and MECE Advisory sections are intentionally absent: they require subagent
> execution that did not occur on this branch.

### Files modified

- `docs/syspilot/userstories/us_agent_arch.rst`
- `docs/syspilot/requirements/req_agent_arch.rst`
- `docs/syspilot/design/spec_agent_arch.rst`
- `docs/changes/agent-arch-duties-workflow-definition.md` (this file)

### Level 0 — User Story (`us_agent_arch.rst`)

**`SYSP_US_AGENT_ARCH`:**

- **"As a / I want to"** sentence: `Duties (tasks)` → `Duties
  (accountability)`; `Workflow (process)` → `Workflow (execution sequence)`.
  Removes the originating misnomer at its source.
- **Three-section list** in the Context: `Duties — customer-customizable
  task list` → `Duties — customer-customizable list of responsibilities
  and outcomes (unordered; what the agent is accountable for)`. Workflow
  bullet sharpened symmetrically. Added a one-sentence note that a single
  behavioural item belongs in exactly one section, plus a brief mention
  that Frontmatter and Prompt File are covered by their own requirements
  (so AC-1 below stops being inconsistent with the rest of the spec set).
- **AC-1** rewritten: was *"has exactly three sections: Soul, Duties,
  Workflow"* (factually wrong — Frontmatter and Prompt File are also
  mandatory per their own REQs). Now: *"contains the three behavioural
  sections Soul, Duties, and Workflow (additional structural elements
  such as Frontmatter and Prompt File are governed by their own
  requirements)"*.
- **AC-5 added**: *"Given any behavioural item describing the agent's
  work, When placed in the agent definition, Then it appears in exactly
  one of Duties or Workflow — never both."* The L0 mirror of the
  Mutual Exclusion property added at L1/L2.

### Level 1 — Requirements (`req_agent_arch.rst`)

**`SYSP_REQ_AGENT_ARCH_DUTIES`:**

- Description rephrased to lead with the guiding question *"What is this
  agent accountable for?"* and to explicitly bound Duties to responsibilities
  and outcomes.
- Rationale rewritten to motivate the accountability vs. execution-sequence
  distinction.
- AC-2 changed from "discrete, independently addressable tasks" to "discrete,
  independently addressable responsibilities or outcomes".
- AC-5 added: *"A single behavioural item SHALL appear in exactly one of
  Duties or Workflow — never both."*

**`SYSP_REQ_AGENT_ARCH_WORKFLOW`:**

- Description rephrased to lead with the guiding question *"How does this
  agent execute its work?"* and to explicitly bound Workflow to ordered
  execution steps.
- Rationale rewritten symmetrically to the Duties REQ.
- AC-2 expanded from "Workflow steps are ordered and numbered" to "Workflow
  steps are ordered, numbered, and describe execution actions" (added 'and
  describe execution actions' so AC-2 alone disambiguates from a hypothetical
  ordered Duties list).
- AC-5 added: *"A single behavioural item SHALL appear in exactly one of
  Workflow or Duties — never both."*

### Level 2 — Design Specs (`spec_agent_arch.rst`)

**`SYSP_SPEC_AGENT_ARCH_DUTIES`:**

- Definition rewritten to open with the guiding question.
- Bullet list reordered to lead with "Accountability" instead of "Task list".
- Properties tightened: "Duties describe outcomes and responsibilities, not
  execution steps"; "Written as short, unordered responsibility statements".
- New "Mutual Exclusion" property bullet added with explicit SHALL language
  and a placement rule (outcome/accountability → Duties; execution step →
  Workflow).

**`SYSP_SPEC_AGENT_ARCH_WORKFLOW`:**

- Definition rewritten to open with the guiding question.
- "Steps — numbered, sequential actions" tightened to "numbered, sequential
  execution actions".
- Properties tightened: "Steps describe execution sequence, not
  accountability or outcomes".
- New "Mutual Exclusion" property bullet added (mirror of the Duties SPEC).


---

## What this CR does NOT do

To prevent the same drift that produced this CR, the boundaries are stated
explicitly:

- **Does not refactor any agent file.** Existing agents (CM, Setup
  Bootloader, PM, QM, etc.) almost certainly contain Duties↔Workflow
  duplication. They remain non-conformant after this CR. That is intentional.
- **Does not run formal QM, MECE, or Trace.** Those gates were skipped on
  this branch because of the outside-loop repair situation. A follow-up
  decision is required: do we run them retrospectively, or do we accept the
  branch as-is on the basis that the change is small and self-contained?
- **Does not address the behavioural root cause.** PM produced an antipattern
  instance while authoring the CR meant to fix the architectural pressure
  toward that antipattern. That root cause sits in PM/CM agent behaviour and
  remains open. See Analyst F-004.

---

## Open Questions for PM

(*"Open Questions for PM" pattern proposed in F-002 — first concrete use.*)

1. **Acceptance vs. retroactive QM:** Do you accept this branch as-is given
   the Process Note, or do you want a retroactive QM/MECE/Trace pass before
   merge?
2. **Naming the next CR:** What should the follow-up CR that brings existing
   agent files into conformance with the new Mutual Exclusion property be
   called? Suggestion: `agent-files-duties-workflow-mutex-cleanup`.
3. **F-004 follow-up:** The behavioural defect this exposes (PM authoring
   pre-baked Impact Analysis / Change Log / AC Verification before subagents
   run) is the actual high-leverage CR. Do you want Analyst to draft an
   intent-only message for that, or will you scope it directly?
