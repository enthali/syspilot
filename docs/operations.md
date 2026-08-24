# Operating Syspilot

Syspilot v2 currently has two operational modes: developing the product from
this repository, and previewing its documentation and traceability model. A
supported customer installation and update flow is still pending.

## Current Tooling

For local development and documentation builds, use:

- VS Code with GitHub Copilot;
- the `enthali.jarvis-core` extension for actor identity and messaging;
- `uv` available on your `PATH`;
- Python 3.10 or newer; and
- the Python packages in `docs/requirements.txt`.

Build from the repository root:

```powershell
python docs/docs-build.py clean
```

The command runs a strict Sphinx build, validates the Needs schema, exports the
Needs graph, and writes the site to `docs/_build/html`.

Run the focused documentation tests with Python's built-in test runner:

```powershell
python docs/test_docs_build.py -v
```

## Installation and Updates

The Syspilot Setup actor owns installation and updates in customer
environments. The target v2 experience is Contract-based: Setup makes the
desired environment explicit, performs the owned work, records evidence, and
hands back a checkable outcome.

That end-to-end bootstrap is not implemented yet. Until it is, avoid presenting
repository checkout steps as a supported installation procedure. They are a
developer preview, documented in [Getting started](getting-started.md).

## Release Responsibility

The Release actor owns packaging, release delivery, preflight checks, and
release-facing user documentation. A release should not move because the
calendar is impatient; it moves when its artifacts and evidence say it is
ready.

Release notes remain release-facing documentation rather than part of the
Technical Writer's six-guide ownership map. The Technical Writer may still
review linked explanations for clarity when a Change includes user
documentation.

## When the Documentation Build Fails

Start with the first warning or error, not the final cascade.

Common checks:

1. Confirm the virtual environment is active and dependencies are installed.
2. Run the clean build so stale generated output cannot hide the real state.
3. For an unknown Need ID, inspect the source directive and its link fields.
4. For a schema warning, check `.syspilot/ontology.toml` and the relevant Need
   type rather than patching generated output.
5. For a broken page, confirm it appears in a toctree and its links are relative
   to the source file.

Generated files under `docs/_build/` are evidence, not source. Fix the source
and rebuild.

## When Actor Messaging Fails

Check that Jarvis Core is installed and that its messaging tools are enabled
for the active agent. Confirm the destination uses the exact actor or session
name. A failed message does not authorize editing another actor's memory or
pretending a handoff occurred.

## Operational Ownership

- Setup owns customer installation and updates.
- Release owns packaging and delivery.
- The process owner owns each canonical Contract template.
- The Technical Writer owns these user guides and their `doc` Needs.
- The factual owner of a source artifact remains the authority on its behavior.

This division is useful during incidents: route the problem to the owner of the
affected outcome, keep the current blocker visible, and resist the urge to fix
an authority problem with a longer troubleshooting page.