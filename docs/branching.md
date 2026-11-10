# Branching

A Change states its branch in exactly one place: the version control row in its
Contract's artifact table. That row is owned by the Project Manager, its
completion evidence is the branch name together with the integration state, and
its status reads `active` while the branch carries the work or `merged` once the
branch has been squash-integrated.

One place, deliberately. A branch name repeated in a preamble and in a table is
a name that will eventually disagree with itself, and readers have no way to
know which copy was updated last.

A Change that needs no branch says so through the `Included` column, like every
other artifact that does not apply. There is no special branch value meaning
"none".

## What the Change Contract Decides

The [Change process](Syspilot%20Contracts/change.md) fixes the branch rules that
matter:

- the Project Manager creates the Change's feature branch from `development`,
  using the change name;
- the branch and the initialized Contract are committed together, before the
  first responsibility transfer;
- at closure the branch is squash-integrated into `development`; and
- that authority stops there. Promoting `development` to `main` is release
  publication, owned by the Release actor within a Release Contract — not
  something a Change may do on its way past.

That last boundary is the reason the others are worth writing down. A Change
that could reach `main` on its own would make every release an accident of
timing.

## The Shape

```{mermaid}
gitGraph
    commit id: "release v0.9.0" tag: "v0.9.0"
    branch development
    checkout development
    branch feature/contract-handling
    checkout feature/contract-handling
    commit id: "specify"
    commit id: "implement"
    commit id: "verify"
    checkout development
    merge feature/contract-handling id: "squash merge"
    checkout main
    merge development id: "release v0.9.1" tag: "v0.9.1"
```

## What Each Branch Means

| Branch | What lives there |
|---|---|
| `feature/<change-name>` | One Change, from its first commit to its last. The name matches the Contract in `docs/changes/`. |
| `development` | The integration branch. Each completed Change arrives as one squashed commit. |
| `main` | Released state only. Every commit is a release and carries its version tag. |

The one-Change-per-branch rule is what makes a Contract findable from history
and history findable from a Contract. Both directions matter: reviewers arrive
from either side.

## What This Repository Practices

The rest is how the Syspilot repository works today rather than something a
process prescribes. A project adopting Syspilot may reasonably decide otherwise.

Feature branches stay local and are not pushed. What other actors need in order
to continue is the committed Contract, and later the squashed commit that lands
on `development` — not a remote copy of work that is still moving.

Merged feature branches are kept rather than deleted. Squashing gives
`development` a readable history, but it also collapses the steps that produced
the result — and those steps are frequently the interesting part when something
turns out to be wrong months later. The branch keeps them available for
`git bisect` and for reading the actual sequence of decisions.

## Setup Uses Its Own Branch

[Pristine Setup](Syspilot%20Contracts/setup.md) brings stricter branch rules,
because it writes into a project that does not know Syspilot yet:

- Setup asks the User to approve a dedicated Setup branch and creates it from
  the selected project state.
- The installation runs only on that branch.
- A failed mandatory gate leaves the branch in place for inspection and the
  Contract `blocked`.
- Git is the cleanup boundary. Discarding the Setup branch returns the project
  to its exact starting state, which is why Setup deliberately implements no
  rollback mechanism of its own.
- Once every gate passes, Setup asks the User how to commit and merge, then
  merges into the branch the User selected.

## Releases

`main` only ever receives a released state, and the tag on that commit is what
publication reacts to. Pushing a `vMAJOR.MINOR.PATCH` tag publishes the
documentation and then creates the GitHub Release; manual workflow runs validate
and build without publishing anything.

That is why `main` is never a working branch. Its history is meant to read as a
list of releases and nothing else.

The [Release process](Syspilot%20Contracts/release.md) runs that promotion in a
Release Contract at `docs/changes/release-v{version}.md`. Its preflight runs on
the `development` commit to be released, with the release notes already
committed there, before `main` or a tag moves: the documentation tests, the
strict documentation build, the release QA suites, and the automated version
check. The newest release-notes heading supplies the version, and the
documentation metadata is derived from it.

The validation-only workflow run is conditional: it is required when the files
Admin lists as inputs of the Linux run changed, Admin records an environment
change, or the immediately preceding release has no successful tag run. Release
assesses the trigger evidence at release start. That run exercises validation and the
documentation build, not publication. It needs a pushed branch, which is the
exception to keeping feature branches local and needs the User's explicit
authorization naming the run.

Before the merge, commit the User's explicit authorization to push `main` and
the tag on `development`, after the preflighted commit P, changing only that
release's `docs/changes/release-v{version}.md`. This authorization is separate
from permission to start the release and acknowledges the local evidence
limits and any triggered validation-only run.

Publication then merges `development` into `main` as release commit R, so R
contains the authorization. Run
`uv run python scripts/check_release_record.py P R v{version}` with the two
commit references. It reads committed state and writes nothing. P must be an
ancestor of R, with exactly that record changed and no rename, mode change or
deletion. Both records must exist; R must contain P's full SHA in an evidence
row, a version matching the tag and newest release-notes heading, and every
second-level heading of the Release Contract template. The heading check
establishes presence, not order or content. Non-applicable artifact sections
stay with status `not applicable` and the reason in their artifact row. The
protected-content comparison covers scope, version, inventory, artifact owners,
start authorization, preflight commands, and verification version/tag. A failing check exits with
status 1 and names its condition on stderr.

This is bounded automation, not proof that every difference is evidence.
Quality and Release must review the complete P-to-R diff before publication,
including the push authorization and unprotected procedure, failure-rule and
narrative text. A change to release content, a procedure or a failure rule is
rejected or requires a new preflight; it cannot inherit the earlier results.

`main` is pushed first and the tag second, and the tag sits only on the release
commit on `main`, because the workflow publishes any pushed `v*.*.*` tag. The
workflow publishes nothing if validation or the documentation build fails.
Later failures can leave a partial publication: Pages may be deployed even
though GitHub Release creation fails. In either case the release stops with a
recorded blocker and the User decides; the tag stays where it is, and the usual
fix is a new patch version.

Evidence unavailable in R, such as R's SHA and the workflow/publication outcome,
is recorded after the tag in a later commit changing only the release record.
That commit does not move the tag. A successful tag run also records its
environment baseline for the next release.
