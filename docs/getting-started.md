# Getting Started with Your Project

This guide helps project leads apply Syspilot to their own projects. Setup
follows the Contract included in the Syspilot release you choose.

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
- `enthali.jarvis-core` 0.32.0 or newer for persistent actors and messaging;
  Setup can install it for you, with your consent;
- Python 3.13 or newer and `uv`;
- Sphinx for the rendered information space; and
- Sphinx-Needs 4.1.0 or newer for ontology-backed Needs and traceability.

For this reference stack, Sphinx, Sphinx-Needs, and the project ontology are
part of the supported Change workflow. They are not installed automatically by
an extension. The Setup Contract preserves an existing Sphinx-Needs environment
or installs a project-local environment when one is absent. When Setup itself has
to bind an ontology and the environment's Sphinx-Needs is older than 4.1.0, it
records the version and stops with a blocker; an ontology your project already
configures is left alone whatever the version.

## Install Syspilot Into Your Project

There is nothing to clone and nothing to install by hand. Open a GitHub Copilot
chat session in your own project and send this prompt:

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

That is the whole entry point, and it is deliberately this small. The prompt
settles exactly one question — which release — and then hands over. Everything
version-specific lives in the Contract that ships with that release, so the
prompt itself never goes out of date. A bootstrap that knew how to install
Syspilot would have to be updated in lockstep with it forever.

From there, the Setup Contract guides the installation. It checks the release,
preserves existing project content, and asks which example Contracts to
include. It creates the Actor and Contract folders using a project name you
confirm, and asks before resolving file conflicts. If Setup cannot proceed, it
records a blocker and explains how to continue.

Setup checks for Jarvis Core 0.32.0 or newer in the VS Code instance hosting
your session. If needed, it explains why Jarvis is required and asks your
permission to install it. If Setup cannot verify or install Jarvis, it records
a blocker and explains how to continue. If an installation it performs requires
a reload, Setup gives you a prompt to resume in a new chat.

Setup creates the nine Actors and leaves any existing Actors unchanged. If the
session cannot create Actors, Setup stops and offers two ways forward: enable
Actor creation in the Chat tool picker or create them by hand as the Contract
describes.

An ordinary chat session does not offer the Jarvis messaging tools. In that case
Setup creates the other eight Actors, transfers its record to the Admin actor,
and then creates the Admin last, with the request for it as the first message.
When an Admin already exists and you accept it, its files stay unchanged and
Setup asks whether it may append the request to `.jarvis/messages/queue.json`
itself; without your consent it writes nothing to the queue and gives you the
manual prompt instead. For a newly created Admin, Setup never writes the queue:
the request reaches it through Jarvis as the first message. In both cases Setup
adds the Admin to `.jarvis/messages/autodelivery.json`. Jarvis does not lock
either file. Jarvis writes `autodelivery.json` itself only when a person enables
or disables delivery in its menu, so an overwrite needs such an action within
the milliseconds of Setup's write. For `queue.json`, which only the existing-Admin
path writes, Jarvis's own writers are the risk: heartbeat jobs, reminders, and
Actors. An entry another writer adds at that moment can be overwritten, and no
read-back can show it. Setup keeps the entries it read, states this limit to you
and records it, and treats it as a limit, not a guarantee. The request is
written in the language you used with the session, or in English when that
language is ambiguous.

The only evidence that the Admin continued is its acknowledgement row in the
Setup record, which Setup waits for up to 120 seconds. A queue entry that is
still present means at most that Jarvis announced it, not that the Admin acted
on it. Without the row, Setup reports the failure and gives you a prompt: open
the Admin's chat from the ACTORS view and paste it. The Admin then continues
from the first open phase. Whoever executes records each transfer, and the
handover to the Project Manager, in the Handover log of the Setup record.

The Contract cannot claim success until every mandatory gate has passed. A gate
is either `pending`, `passed`, or `failed`. While any gate is not `passed`,
including Actor discovery that has not yet listed all nine Actors and a
documentation build with warnings, the baseline stays unverified and nothing is
handed to the Project Manager. Git integration follows the passed gates. The
record then reads `verified` with the Project Manager named and the handoff
pending; it reads `handed off` only after the Project Manager has acknowledged
it, and Setup reports completion only then. If the message cannot be sent, the
record stays unchanged and Setup tells you to give the Project Manager's chat the
path of the record.

The documentation Setup generates is deliberately plain. Its `docs/conf.py` has
no Syspilot project metadata, loads only the two extensions the installed
requirements provide, and binds the ontology with a literal `needs_from_toml`
setting, because Syspilot's skills read that setting directly. Its
`docs/index.rst` lists only the Actor and Contract registries. Setup does not
install Syspilot's own ontology reference page, and Change Contracts stay out of
the rendered site.

That handoff identifies the selected ontology and its configured path. The
Project Manager first re-reads its own context, its role card, and the Setup
record, and checks that the committed header names it. Then it explains the
ontology's artifact types, statuses, and relationships, and asks whether it fits
the project. If the User accepts it, normal project intake
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
2. **Syspilot Contracts** for Contract Documents and the Change process.
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
A project that runs a version before 0.10 finds a starting checklist in
[Upgrading to 0.10](upgrade.md).