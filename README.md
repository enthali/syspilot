<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/syspilot-logo-dark.svg">
    <img src="assets/syspilot-logo.svg" alt="syspilot" width="200">
  </picture>
</p>

<p align="center"><strong>Requirements Engineering that scales with AI.</strong></p>

> **⚠️ Early Research Project** — syspilot is under active development. Feel free to use it, fork it, or just study the approach. Updates may introduce breaking changes without migration paths.

> Your project has 5000 requirements. A change affects 5 of them.
> syspilot follows [sphinx-needs](https://sphinx-needs.readthedocs.io/) traceability links to find exactly those 5 — so your AI agent gets focused context, not the entire codebase.

Cover 100% of your specs with 6x less tokens. Links are deterministic — search is probabilistic. syspilot gives your agents the map, not the flashlight. Built on [sphinx-needs](https://sphinx-needs.readthedocs.io/) by [useblocks](https://useblocks.com). Powered by [GitHub Copilot](https://github.com/features/copilot).

## Installation

Install [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/), then
run the command for your harness from the root of the target Git repository.

Production harnesses: GitHub Copilot in VS Code, Claude Code, and OpenCode. Qoder is
available as an explicitly disclosed experimental, installable harness.

### GitHub Copilot in VS Code

```bash
uv run --no-project "https://raw.githubusercontent.com/hubertusgbecker/syspilot/main/syspilot/installer.py" install --harness vscode
```

### Claude Code

Install and authenticate Claude Code first, then run:

```bash
uv run --no-project "https://raw.githubusercontent.com/hubertusgbecker/syspilot/main/syspilot/installer.py" install --harness claude
```

### OpenCode

```bash
uv run --no-project "https://raw.githubusercontent.com/hubertusgbecker/syspilot/main/syspilot/installer.py" install --harness opencode
```

### Qoder (experimental, installable)

Install Qoder first, then run:

```bash
uv run --no-project "https://raw.githubusercontent.com/hubertusgbecker/syspilot/main/syspilot/installer.py" install --harness qoder
```

The Qoder command deterministically stages
`.syspilot/qoder/syspilot-qoder-plugin.zip`. Import that archive through
Qoder's documented UI. The import is external and is not performed or reported
as completed by the Installer. Native in-app import and autonomous
Manager-to-Engineer orchestration clearance for Qoder are deferred future
work, not part of this experimental, installable-only tier.

Run the same command again to update. Run one command for each harness used in
the repository. The defaults are the current directory, repository
`hubertusgbecker/syspilot`, and branch `main`. Synchronous orchestration is
installed deterministically.
For a fork or branch, change the URL and add `--repository <owner>/<repo>
--branch <branch>`.

The command writes only the explicitly selected harness target, the stable
`.syspilot/installer.py` runtime, shared resources in `.syspilot/skills/` and
`.syspilot/templates/`, and missing documentation bootstrap files.
Installed Setup uses that runtime directly for later updates. Installation
rejects target-path links and rolls back only syspilot-owned mutable paths, so
unrelated project files and concurrent unrelated changes remain untouched.

GitHub Copilot CLI has been evaluated for artifact compatibility but is not
production-certified. Production support for GitHub Copilot currently means
GitHub Copilot in VS Code.

## What You Get

Four **managers** that orchestrate the work, and seven **engineers** that execute it:

| Managers | What they do |
|----------|-------------|
| `@syspilot.pm` | Plans features, manages backlog, delegates change requests |
| `@syspilot.cm` | Orchestrates engineers through the change workflow |
| `@syspilot.qm` | Runs independent quality checks |
| `@syspilot.setup` | Installs/updates syspilot in your project |

| Engineers | What they do |
|-----------|-------------|
| `@syspilot.design` | Analyzes a change request, creates a Change Document |
| `@syspilot.implement` | Executes approved changes with traceability |
| `@syspilot.uat` | Generates user acceptance test artifacts |
| `@syspilot.verify` | Validates implementation against the Change Document |
| `@syspilot.docu` | Keeps project documentation current |
| `@syspilot.mece` | Finds gaps and redundancies in your specs |
| `@syspilot.trace` | Traces one item through all levels |
| `@syspilot.release` | Manages versioning and release process |

Agents are stable processes (WHAT to do). **Skills** are exchangeable tool bindings (HOW to do it) — customize syspilot by swapping skills, not agents.

## How It Works

```
User Story (WHY)  ──links──▶  Requirements (WHAT)  ──links──▶  Design Specs (HOW)
```

When you request a change, syspilot follows these links to find only the affected elements. **O(affected), not O(total).**

## Documentation

📖 **Full docs:** [hubertusgbecker.github.io/syspilot](https://hubertusgbecker.github.io/syspilot/index.html)

Includes methodology, naming conventions, and traceability matrices.

## Requirements

- **Git**
- **[uv](https://docs.astral.sh/uv/)**
- **GitHub Copilot in VS Code**, **Claude Code**, or **OpenCode** (production),
  or **Qoder** (experimental, installable)

Claude Code must be installed and authenticated before selecting it. Qoder
must be installed before its staged Plugin archive can be imported through the
documented Qoder UI.

`uv` resolves the exact Python and package dependencies declared by the remote
PEP 723 script. No project `.venv`, preinstalled Python packages, or `pip`
setup is required.

## License

This project is licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, provided that the copyright notice and this permission notice are included in all copies or substantial portions of the software. The software is provided "as is", without warranty of any kind. See [LICENSE](LICENSE) for the full license text.

