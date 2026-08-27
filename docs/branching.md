# Branching

Every Change runs on its own branch, and the Contract for that Change records
which one in its `Branch:` field. That is the only place a branch name is
binding.

This page collects the shape the Syspilot repository itself uses. A project
adopting Syspilot can choose a different one — what matters is that its
Contracts say which branch the work belongs to, so that a reader can always find
the work from the document that governs it.

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

Feature branches stay local and are not pushed. What other actors need in order
to continue is the committed Contract, and later the squashed commit that lands
on `development` — not a remote copy of work that is still moving.

## Merged Branches Are Kept

Feature branches are not deleted after they merge. Squashing gives
`development` a readable history, but it also collapses the steps that produced
the result — and those steps are frequently the interesting part when something
turns out to be wrong months later. The branch keeps them available for
`git bisect` and for reading the actual sequence of decisions.

## Setup Uses Its Own Branch

[Pristine Setup](Syspilot%20Processes/setup.md) brings stricter branch rules,
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
