# Getting Started with Your Project

This guide is for project leads who want to apply Syspilot to their own project.
The supported setup model starts with an exact Syspilot release and its
release-bound Setup Contract. The initiating Copilot session executes that
Contract as a temporary executor; no persistent Setup actor is installed.

The process, inventory, blockers, and verification gates are defined and
reviewed. End-to-end installation, actor discovery, target build, baseline
readback, Git integration, and Project Manager handoff have not yet been run in
an isolated Jarvis or VS Code Extension Host environment. This guide therefore
explains the supported interface without claiming operational runtime proof.

## What Your Project Setup Defines

A Syspilot project is not merely an extension installation. Its setup defines:

- the Contracts that describe how work reaches a checkable outcome;
- the project ontology: artifact types, statuses, and relationships;
- the specification and traceability sources that realize that ontology;
- the documentation matrix for independently maintained user information; and
- any specialist Actors the project needs beyond Syspilot's eight base roles.

The [Customization guide](customization.md) explains these four project-owned
levels. The [product model](product-model.md) shows how Syspilot applies the
same approach to its own development.

## First Supported Stack

Syspilot currently supports one concrete realization. Backend neutrality is an
intended direction that a future Change must establish and verify. The current
stack is:

- VS Code with GitHub Copilot for AI-assisted work;
- `enthali.jarvis-core` for persistent actors and messaging;
- Python 3.10 or newer and `uv`;
- Sphinx for the rendered information space; and
- Sphinx-Needs for ontology-backed Needs and traceability.

For this reference stack, Sphinx, Sphinx-Needs, and the project ontology are
part of the supported Change workflow. They are not installed automatically by
an extension. The Setup Contract preserves an existing Sphinx-Needs environment
or installs a project-local environment when one is absent.

## Pristine Setup Interface

For a project with no confirmed Syspilot baseline:

1. Select an exact Syspilot SemVer release.
2. Load that release's Setup Contract and materialize it as
  `.syspilot/setup-contract.md` in the version-controlled target project.
3. Execute the materialized Contract in the initiating Copilot session.

The Contract verifies the release's full commit identity, works on a dedicated
User-approved branch, preserves existing project-owned content, and records the
release tag and commit in `.syspilot/project.toml`. It may report an actionable
blocker, but it cannot claim success until every mandatory gate, Git integration,
and Project Manager handoff has completed.

## Preview the Reference Implementation

Until runtime setup acceptance is completed, clone this repository and build
Syspilot's own model as a worked example. Create a virtual environment,
explicitly install the Python dependencies, and run the clean build:

```powershell
python -m venv docs/.venv
docs/.venv/Scripts/Activate.ps1
python -m pip install -r docs/requirements.txt
python docs/docs-build.py clean
```

Open `docs/_build/html/index.html` after the build succeeds. The most useful
first stops are:

1. **Syspilot Actors** for the roster and shared actor model.
2. **Syspilot Processes** for Contract Documents and the Change process.
3. **Traceability** for the graph connecting stories, requirements, criteria,
   documentation, and realized artifacts.

## Follow One Real Contract

Open `docs/changes/documentation-foundation.md`. It shows the current state of
the work that produced this documentation: approved intent, artifact owners,
decisions, review evidence, and the actor currently responsible.

This is more representative than a perfect toy example. Real work has pending
reviews, explicit boundaries, and occasional sentences that improve after a
human reads them.

## Where to Go Next

- [The product model](product-model.md) explains the moving parts.
- [The Change workflow](change-workflow.md) turns the process definition into a
  practical journey.
- [Customization](customization.md) shows where project knowledge belongs.
- [Operations](operations.md) collects build and maintenance guidance.

Later Syspilot updates are not routine setup work. Each update requires a
separate project-specific Change that records the old and proposed baselines,
impact analysis, revalidation scope, authorization, and technical executor.