---
name: syspilot.branching
description: "Git branching strategy and commit conventions for syspilot. Development branch with feature branches, main = releases only. Who may create/commit to which branches. USE FOR: any git operation, branch creation, committing, pushing, merging."
---

# Skill: Git Branching Strategy & Commit Conventions

## Instructions

## HARD RULE

**ONLY `@syspilot.release` may commit to, merge to, or push to `main`. No exceptions.**

If you are on `main` and need to make any change, create `feature/<name>` from `development` first.
Main always equals the latest release — any non-release commit on main is a violation.

## Development Branch Strategy

syspilot uses a permanent `development` integration branch with short-lived feature branches:

```mermaid
gitGraph
   commit id: "v0.2.3" tag: "v0.2.3"
   branch development
   checkout development
   commit id: "dev-start"
   branch feature/CR7
   checkout feature/CR7
   commit id: "CR7: specs"
   commit id: "CR7: implement"
   commit id: "CR7: verify"
   checkout development
   merge feature/CR7 id: "squash CR7"
   branch feature/CR8
   checkout feature/CR8
   commit id: "CR8: specs"
   commit id: "CR8: implement"
   commit id: "CR8: verify"
   checkout development
   merge feature/CR8 id: "squash CR8"
   checkout main
   merge development id: "v0.2.4" tag: "v0.2.4"
```

**Key Properties:**

- One branch per change — isolates each change for independent review
- `development` as integration target — all features merge here
- Squash-merge everywhere — clean history on `development` and `main`
- Main = releases only — main always equals the latest release
- Tag on main — `v{version}` tags mark published releases
- Back-merge after release — `git checkout development && git merge main` prevents conflicts on next release
- Conflict guidance — squash-merge conflicts resolve with `-X theirs` (development wins)

## Branch Permissions

| Agent | May create | May commit to |
|-------|-----------|--------------|
| `@syspilot.release` | (none) | `main` (squash merge from `development` + tag); `development` (prep + back-merge) |
| `@syspilot.pm` | `feature/<name>` | `feature/<name>` (the branch it created) |
| `@syspilot.installer` | (none) | pre-install and final commit on the branch that was checked out when invoked (no dedicated branch created) |
| `@syspilot.implement` | (none) | current feature branch |
| `@syspilot.verify` | (none) | current feature branch |
| `@syspilot.docu` | (none) | current feature branch |
| All other engineers | (none) | current feature branch |

`development` is a permanent branch that all feature branches merge into. No agent creates `development` — it exists permanently.

## Branch Naming Conventions

| Pattern | Created by | Purpose |
|---------|-----------|---------|
| `development` | (permanent) | Integration branch, all features merge here |
| `feature/<name>` | `@syspilot.pm` | Feature work, fixes, refactors |
| `main` | (protected) | Release-only, always latest release |

## Feature Branch Retention

After a feature branch is squash-merged into `development` and the release
that includes it completes, the default policy is to **retain** the branch
(locally and on remote) rather than delete it.

A project MAY opt into automatic deletion of merged feature branches by
stating so in `tailoring.md`, e.g.:

> Delete feature branches after they are merged into development and
> released — do not retain them.

Absent such an override, branches are retained indefinitely; retaining
them costs nothing and preserves forensic/bisect history.

The Release Engineer applies this policy during its branch-retention
workflow step.

## Commit Message Conventions

Format: `<type>: <short description>`

| Type | When to use | Example |
|------|------------|---------|
| `feat` | New feature or specification | `feat: add branching skill RST specs` |
| `fix` | Bug fix or correction | `fix: correct traceability link in REQ_123` |
| `docs` | Documentation changes (non-spec) | `docs: update PM context with CR5 status` |
| `chore` | Maintenance, cleanup, tooling | `chore: archive v0.2.2 change documents` |
| `refactor` | Restructuring without behavior change | `refactor: reorganize index.rst toctrees` |

**Rules:**

- Type is lowercase
- Description is lowercase, no period at end
- Keep description under 72 characters
- Reference spec IDs in description when relevant

## Rules

* MUST NOT commit to, merge to, or push to `main` — only `@syspilot.release` may. No exceptions.
* Commit type MUST be lowercase.
* Commit description MUST be lowercase with no trailing period.
* Commit description MUST be ≤ 72 characters.
* Reference spec IDs in description when relevant.
