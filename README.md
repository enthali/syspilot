<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/syspilot-logo-dark.svg">
    <img src="assets/syspilot-logo.svg" alt="Syspilot" width="200">
  </picture>
</p>

<p align="center"><strong>Requirements engineering that scales with AI-assisted development.</strong></p>

Syspilot gives AI collaborators a traceable product model and durable process
state. Instead of asking an agent to rediscover your entire project on every
change, you hand it explicit links, owned artifacts, and an outcome somebody can
actually check.

> **Early research project:** Syspilot v2 is taking shape in public. The product
> model, Change process, and release-bound Setup Contract are there to be read
> and picked apart. End-to-end setup has not yet been demonstrated in an
> isolated target environment, and we are not going to pretend otherwise.
> Expect sharp edges and breaking changes.

## Install It

Nothing to clone, nothing to copy into place. Open a GitHub Copilot chat session
in your own project and send this:

```text
Install Syspilot into this project.

1. Look up the releases of https://github.com/enthali/syspilot, tell me the
   latest one, and ask me which version to install.
2. Fetch `docs/Syspilot Contracts/setup.md` from that exact tag.
3. Save it unchanged as `.syspilot/setup-contract.md` in this repository, and
   make sure it is the only change in the working tree.
4. Execute that Contract from top to bottom. It owns every further step,
   question, blocker, and the final handoff.

If the Contract does not describe a step you need, consult me on how to
proceed.
```

That is the entire entry point. It names a release and gets out of the way —
everything version-specific lives in the Contract that ships with that release.
See [Getting started](docs/getting-started.md) for what happens next, and for
the honest boundary on what has and has not been proven at runtime.

## Start Here

| You want to... | Read... |
|---|---|
| See what works today | [Getting started](docs/getting-started.md) |
| Understand why it works this way | [Contract Driven Development](docs/methodology.md) |
| Understand actors, Needs, and Contracts | [The product model](docs/product-model.md) |
| Run a change from intent to closure | [The Change Contract](docs/change-contract.md) |
| Know which branch your work belongs on | [Branching](docs/branching.md) |
| Tailor Syspilot to a project | [Customization](docs/customization.md) |
| Build, update, or troubleshoot it | [Operations](docs/operations.md) |
| Move a project from before 0.10 to 0.10 | [Upgrading to 0.10](docs/upgrade.md) |

The [rendered documentation](https://enthali.github.io/syspilot/index.html)
also includes the authoritative specifications, actor roles, process
definitions, traceability views, and historical Field Notes.

## The Short Version

Syspilot connects three kinds of truth:

- **Needs** describe why the product exists and what it must do.
- **Realized artifacts** are the files that make those requirements real.
- **Contract Documents** hold the current intent, ownership, evidence, and
  responsibility of one piece of work — so nobody has to reconstruct it from
  chat history later.

Nine persistent actors contribute through distinct areas of authority. There is
no giant scripted relay race, because a fixed sequence eventually prescribes a
step some change plainly does not need — and a rule nobody can follow is a rule
everybody learns to ignore. Instead, the open artifacts in the current Contract
decide who can make the next useful move.

## Current Reference Stack

- VS Code with GitHub Copilot.
- **[Jarvis](https://github.com/enthali/Jarvis)** — the framework that makes
  persistent actors possible in the first place. It gives each actor an
  identity, a memory that survives the session, and a way to message the
  others. Without it, Syspilot is a filing system with strong opinions. Install
  [`enthali.jarvis-core`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-core)
  and you have actors.
- Python 3.13 or newer, and `uv`.
- [Sphinx-Needs](https://sphinx-needs.readthedocs.io/) on top of Sphinx, which
  turns requirements into a linked, validated graph instead of a folder of
  hopeful prose.

Sphinx and Sphinx-Needs are the currently supported realization, and the Change
process expects their ontology and traceability model. Backend neutrality is an
intended direction rather than a feature you have today; a future Change has to
establish and verify it. Syspilot installs no Python packages behind your back —
the repository preview uses `docs/requirements.txt`.

The method itself travels, though. **[enthali/zonal-rc-car](https://github.com/enthali/zonal-rc-car)**
runs the same Contract-driven actor organisation on a SysML v2 model instead of
Sphinx-Needs — stakeholder intent, architecture, independent review and physical
evidence, on an actual RC vehicle. What is currently tied to this stack is
Syspilot's tooling, not the idea behind it.

## Optional Extensions

- **[`enthali.jarvis-flow`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-flow)**
  is highly recommended. It draws the messages travelling between actors, which
  turns "who is waiting on whom?" from a guess into a picture.
- **[`enthali.jarvis-kanban`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-kanban)**
  gives actors, projects, and events their own kanban boards as plain YAML in
  the entity folder. Handy for project management, and pleasantly hard to
  desynchronise from reality, since the board is a file the actors read and
  write like any other.
- **[`enthali.jarvis-syspilot`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-syspilot)**
  may automate the same Contract interfaces. Optional, and it adds no separate
  installation or update lifecycle to keep track of.

`enthali.jarvis-core` and the three optional extensions above are all developed
in the **[`enthali/Jarvis`](https://github.com/enthali/Jarvis)** repository.

## License

See [LICENSE](LICENSE).

