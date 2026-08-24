# Getting Started with Your Project

This guide is for project leads who want to apply Syspilot to their own project.
The eventual path starts with your project's outcomes, Contracts, ontology,
and documentation needs, then lets Setup install the actors and supporting
artifacts that realize that model.

That automated customer bootstrap is not implemented yet. For now, this page
does two useful things: it describes what a project setup needs to establish
and gives you a reproducible preview of the current reference implementation.

## What Your Project Setup Defines

A Syspilot project is not merely an extension installation. Its setup defines:

- the Contracts that describe how work reaches a checkable outcome;
- the project ontology: artifact types, statuses, and relationships;
- the specification and traceability sources that realize that ontology;
- the documentation matrix for independently maintained user information; and
- any specialist Actors the project needs beyond Syspilot's nine base roles.

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
Syspilot today.

## Preview the Reference Implementation

Until customer bootstrap exists, clone this repository and build Syspilot's own
model as a worked example. Create a virtual environment, explicitly install the
Python dependencies, and run the clean build:

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

When the customer bootstrap is implemented, this guide will replace the
preview with an executable path for defining and installing a new project's
Contracts, ontology, documentation matrix, and actors.