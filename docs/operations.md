# Operating Syspilot

Syspilot v2 defines a release-bound Pristine Setup process alongside product
development and repository preview workflows. The Setup process has passed
semantic and blocker review, but its end-to-end runtime path has not yet been
executed in an isolated Jarvis or VS Code Extension Host environment.

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

## Pristine Installation

Pristine setup uses the selected release's canonical
[Setup Contract](Syspilot%20Processes/setup.md). A bootstrap prompt loads that
Contract, materializes it as `.syspilot/setup-contract.md`, and asks the
initiating Copilot session to execute it. The session is a temporary Contract
executor; Setup is not a persistent actor.

The Contract verifies prerequisites and release identity, audits a dry run,
preserves existing project-owned configuration, installs eight persistent
Syspilot actors, validates the target build, and completes User-guided Git
integration before handoff. It records the exact release and commit in
`.syspilot/project.toml`, permanently pinning the project's approved baseline.

These steps define supported behavior, not completed runtime evidence. Until a
follow-up Change executes the deferred target scenarios, use the repository
checkout only as the [reference preview](getting-started.md)
and do not claim that a customer installation has completed successfully.

## Updates Are Separate Changes

A project does not routinely track the newest Syspilot version. Its approved
baseline remains pinned for the project lifetime. A later update requires a
separate project-specific Change containing the old and proposed baselines,
impact analysis, revalidation scope, User authorization, and an assigned
technical executor.

Jarvis installation, compatibility, and extension updates have their own
lifecycle and are outside Syspilot's project-update policy.

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

- The release-bound Setup Contract owns pristine installation behavior while
   its initiating Copilot session executes the current instance.
- Release owns packaging and delivery.
- The process owner owns each canonical Contract template.
- The Technical Writer owns these user guides and their `doc` Needs.
- The factual owner of a source artifact remains the authority on its behavior.

This division is useful during incidents: route the problem to the owner of the
affected outcome, keep the current blocker visible, and resist the urge to fix
an authority problem with a longer troubleshooting page.