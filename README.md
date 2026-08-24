<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/syspilot-logo-dark.svg">
    <img src="assets/syspilot-logo.svg" alt="Syspilot" width="200">
  </picture>
</p>

<p align="center"><strong>Requirements engineering that scales with AI-assisted development.</strong></p>

Syspilot gives AI collaborators a traceable product model and durable process
state. Instead of asking an agent to rediscover an entire project for every
change, you give it explicit links, owned artifacts, and a checkable outcome.

> **Early research project:** Syspilot v2 is taking shape in public. The product
> model and Change process are available for review, but the supported v2
> bootstrap is not implemented yet. Expect sharp edges and breaking changes.

## Start Here

| You want to... | Read... |
|---|---|
| See what works today | [Getting started](docs/getting-started.md) |
| Understand actors, Needs, and Contracts | [The product model](docs/product-model.md) |
| Run a change from intent to closure | [The Change workflow](docs/change-workflow.md) |
| Tailor Syspilot to a project | [Customization](docs/customization.md) |
| Build, update, or troubleshoot it | [Operations](docs/operations.md) |

The [rendered documentation](https://enthali.github.io/syspilot/index.html)
also includes the authoritative specifications, actor roles, process
definitions, traceability views, and historical Field Notes.

## The Short Version

Syspilot connects three kinds of truth:

- **Needs** describe why the product exists and what it must do.
- **Realized artifacts** are the files that make those requirements real.
- **Contract Documents** keep the current intent, ownership, evidence, and
  responsibility of a piece of work visible.

Nine persistent actors contribute through distinct areas of authority. They do
not follow one giant scripted relay race. Open artifacts in the current
Contract determine who can make the next useful move.

## Current Reference Stack

- VS Code with GitHub Copilot
- The [`enthali.jarvis-core`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-core)
  VS Code extension for actor identity and messaging
- Python 3.10 or newer and `uv`
- Sphinx and Sphinx-Needs for the current specification, ontology, traceability,
  and documentation workflow

Sphinx and Sphinx-Needs are the currently supported realization, and the
current Syspilot Change process expects their ontology and traceability model.
Backend neutrality is an intended direction, not a currently supported
capability; a future Change must establish and verify broader support.
Syspilot does not install these Python packages automatically. The repository
preview installs them through `docs/requirements.txt`.

## Optional Extensions

- **[`enthali.jarvis-flow`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-flow)**
  is highly recommended. It visualizes the message flows between actors, which
  makes a busy collaboration much easier to follow.
- **[`enthali.jarvis-syspilot`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-syspilot)**
  can automate Syspilot updates. It is genuinely optional; Syspilot works
  perfectly well without it.

All three extensions are developed in the
[`enthali/Jarvis`](https://github.com/enthali/Jarvis) repository.

The Setup actor owns the future supported installation and update path for a
customer project. Until that bootstrap is delivered, use the repository
checkout to [preview the reference implementation](docs/getting-started.md#preview-the-reference-implementation).

## License

See [LICENSE](LICENSE).

