# Queued CR Draft: experience-harvest

**Status**: queued (not yet branched)
**Proposed Operation Mode**: user-guided (introduces template memories and a new Contract kind)
**Origin**: Research finding from an external method review (2026-11-10/11)

---

## Problem

An actor's session is disposable; its memory graph is what makes it the actor.
After a few Changes, when the base architecture stands, the memories hold the
knowledge that lets later Changes run autonomously. That knowledge is the asset
a new project should start from.

A single actor cannot decide in its own situation whether a lesson belongs to
its project or holds in general. Generality is a property of several projects,
so it is judged by someone who sees several sources. Attempts to let each actor
classify its own entries did not converge for that reason.

Today Research distills general lessons from several memories only when the User
starts it by hand. No Contract contains that work.

## Principles

- **Only artifacts are evidence.** Safety, quality, and traceability rest on
  Contracts, specifications, code, and test results in git. Sessions and adapted
  project memories are not needed as evidence and are not collected.
- **A project's memories stay with the project and its SME.** The SME adapts
  template memories to the project; the organization has no need to see the
  adapted result.
- **Experience flows back by choice.** Lessons reach the templates through
  voluntary review and feedback rounds, and through sources released for
  harvest.

## Proposal

### 1. Template memories per role

For each role, a released and versioned template memory graph that a new project
starts from, alongside the Example Actors. Projects bind a template version;
safety-relevant projects change the bound memory only through a released Change.

### 2. Feedback rounds feed the templates

The people working with the actors share experience voluntarily in review and
feedback rounds. The agreed lessons enter the template memories through a normal
Change.

### 3. Research harvest over released sources

Research analyses memory graphs whose owners released them for harvest, such as
the maintainers' own projects. Provenance notes and logical names from the Jarvis
memory discipline (Jarvis draft `queued-cr-memory-provenance-logical-names.md`)
make this analysis possible. Research classifies each candidate along two axes:

| Axis | Values | Evidence |
|---|---|---|
| Scope | project / general | An entry that names Need IDs, signal names, paths, or terms from the project's `needs.json` or repository is project-bound (script check). An entry that recurs across several sources is a general candidate (semantic comparison). |
| Confidentiality | public / internal | An entry that contains only logical names and method knowledge is a public candidate. Everything else stays internal. |

SME corrections in the provenance notes are the strongest general candidates.
The script check supports the review; the SME's judgment decides.

### 4. An Experience Harvest Contract

A new Contract kind, owned by Research, started with a release or at project
closure:

| Artifact or gate | Owner | Completion evidence |
|---|---|---|
| Source release | User | The memory graphs and versions released for this harvest |
| Memory analysis | Research | Scope and confidentiality classification per candidate, script results and their limits |
| Template proposal | Research | Proposed entries for the template memories, per role |
| Upstream proposal | Research | Generic method lessons as Syspilot Change drafts, containing only public candidates |
| Template release | User / SME | Explicit release of the template proposal |
| Upstream release | User | Explicit release of each upstream proposal before it is published |

## Observable Outcome

- Template memories per role exist next to the Example Actors and are versioned.
- A canonical Experience Harvest Contract template exists in the process registry.
- A Research skill reports scope and confidentiality candidates for released memory graphs, with its limits.
- One harvest over at least two released sources is run and its proposals are reviewed.

## Open Questions

- How Setup installs a template memory and records its version.
- How the skill reads memory graphs kept in a repository separate from the project.
- Whether memory written by one model is read the same way by another; a first
  measure is whether questions per Change drop faster in a project that starts
  from a template.
