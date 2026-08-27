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
- Python 3.13 or newer and `uv`;
- Sphinx for the rendered information space; and
- Sphinx-Needs for ontology-backed Needs and traceability.

For this reference stack, Sphinx, Sphinx-Needs, and the project ontology are
part of the supported Change workflow. They are not installed automatically by
an extension. The Setup Contract preserves an existing Sphinx-Needs environment
or installs a project-local environment when one is absent.

## Install Syspilot Into Your Project

There is nothing to clone and nothing to install by hand. Open a GitHub Copilot
chat session in your own project and send this prompt:

```text
Install Syspilot into this project.

1. Look up the releases of https://github.com/enthali/syspilot, tell me the
   latest one, and ask me which version to install.
2. Fetch `docs/Syspilot Processes/setup.md` from that exact tag.
3. Save it unchanged as `.syspilot/setup-contract.md` in this repository, and
   make sure it is the only change in the working tree.
4. Execute that Contract from top to bottom. It owns every further step,
   question, blocker, and the final handoff.

If the Contract does not describe a step you need, consult me on how to
proceed.
```

That is the whole entry point, and it is deliberately this small. The prompt
settles exactly one question — which release — and then hands over. Everything
version-specific lives in the Contract that ships with that release, so the
prompt itself never goes out of date. A bootstrap that knew how to install
Syspilot would have to be updated in lockstep with it forever.

From there the Contract takes over. It verifies the release's full commit
identity, works on a dedicated User-approved branch, preserves existing
project-owned content, and records the release tag and commit in
`.syspilot/project.toml`. It may report an actionable blocker, but it cannot
claim success until every mandatory gate, Git integration, and Project Manager
handoff has completed.

That handoff identifies the selected ontology and its configured path. The
Project Manager explains its artifact types, statuses, and relationships, then
asks whether it fits the project. If the User accepts it, normal project intake
continues without an ontology Change. If the User requests an adjustment, the
Project Manager starts a normal Change before anyone modifies the ontology;
the existing Ontology skill supplies technical guidance inside that Change.

## Read the Reference Implementation

This is optional, and it is not how you install anything. Syspilot develops
itself with its own model, so its repository is the one worked example where
every Need, Contract, and actor decision is visible at once. Clone it, create a
virtual environment, install the Python dependencies, and run the clean build:

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

Open any file in `docs/changes/`. Each one is a Contract that actually governed
a piece of this project: approved intent, artifact owners, decisions, review
evidence, and the actor who was responsible at each point.

This is more representative than a perfect toy example. Real work has pending
reviews, explicit boundaries, and occasional sentences that improve after a
human reads them.

## Where to Go Next

- [The product model](product-model.md) explains the moving parts.
- [The Change workflow](change-contract.md) turns the process definition into a
  practical journey.
- [Customization](customization.md) shows where project knowledge belongs.
- [Operations](operations.md) collects build and maintenance guidance.

Later Syspilot updates are not routine setup work. Each update requires a
separate project-specific Change that records the old and proposed baselines,
impact analysis, revalidation scope, authorization, and technical executor.