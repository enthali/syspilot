# Queued CR Draft: experience-harvest

**Status**: queued (not yet branched)
**Proposed Operation Mode**: user-guided (introduces a new Contract kind and changes memory discipline)
**Origin**: Research finding from an external method review (2026-11-10/11)

---

## Problem

Actor memories hold the distilled knowledge of a project: SME corrections,
design guidelines, and lessons that make later Changes run autonomously. They
are the asset that should carry over to the next project.

A single actor cannot decide in its own situation whether a lesson belongs to
the project or to the organization. Generality is a property of several
projects, so it can only be judged by someone who sees several projects.
Attempts to let each actor classify its own entries did not converge for that
reason.

Today Research distills project and organization knowledge from several
projects' memories only when the User starts it by hand with dedicated prompts.
No Contract contains that work, so nothing makes it happen.

## Proposal

### 1. Actors record the provenance of each memory entry

Each entry in an actor's memory records:

- date and Change in which it was learned;
- trigger: `SME correction`, `finding from <role>`, or `own observation`;
- the source as a role, never as a person.

Provenance is easy to decide in the moment; classification is not. SME
corrections are the strongest candidates for organization knowledge.

### 2. Actors record infrastructure by logical name

Actors refer to hosts, rigs, accounts, and environments by their logical name
(for example `test-rig-1`) and reference the configuration file that resolves
that name. Tool calls read the concrete address from that configuration.

This keeps memory shareable and is checkable: every logical name in a memory
file resolves in the referenced configuration.

### 3. Research analyses memories along two axes

| Axis | Values | Evidence |
|---|---|---|
| Scope | project / organization | An entry that names Need IDs, signal names, paths, or terms from the project's `needs.json` or repository is project-bound (script check). An entry that recurs in the memories of several projects is an organization candidate (semantic comparison). |
| Confidentiality | public / internal | An entry that contains only logical names and generic method knowledge is a public candidate. Everything else stays internal. |

The script check supports the review; the SME's judgment decides.

### 4. An Experience Harvest Contract

A new Contract kind, owned by Research, started at project closure or with each
release:

| Artifact or gate | Owner | Completion evidence |
|---|---|---|
| Memory analysis | Research | Analysed memory files with their versions, scope and confidentiality classification per candidate, script results and their limits |
| Organization memory proposal | Research | Proposed entries for the internal organization memory, per role |
| Upstream proposal | Research | Proposed generic method lessons as Syspilot Change drafts, containing only public candidates |
| SME release | User / SME | Explicit release of the organization memory proposal |
| Upstream release | User | Explicit release of each upstream proposal before it leaves the organization |

The organization memory is versioned and released like a product. Projects bind
a released version; safety-relevant projects change it only through a released
Change.

## Observable Outcome

- Memory instructions describe provenance notes and logical names.
- A canonical Experience Harvest Contract template exists in the process registry.
- A Research skill reports scope and confidentiality candidates for a set of memory files, with its limits.
- One harvest over at least two projects is run and its proposals are reviewed.

## Open Questions

- Where the organization memory lives and how projects bind its version.
- How the skill reads memory repositories that are kept outside the project repository.
- Whether memory written by one model is interpreted the same way by another;
  a first measure is whether questions per Change drop faster in the next project.
