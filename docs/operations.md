# Operating Syspilot

Syspilot defines a release-bound Pristine Setup process alongside product
development and repository preview workflows. The User has reported successful
Setup runs; this does not establish coverage of every practical scenario.

## Current Tooling

For local development and documentation builds, use:

- VS Code with GitHub Copilot;
- the `enthali.jarvis-core` extension, version 0.32.0 or newer, for actor identity
  and messaging;
- `uv` available on your `PATH`;
- Python 3.13 or newer; and
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
[Setup Contract](Syspilot%20Contracts/setup.md). A bootstrap prompt loads that
Contract, materializes it as `.syspilot/setup-contract.md`, and asks the
initiating Copilot session to execute it. The session is a temporary Contract
executor; Setup is not a persistent actor. When the session lacks the Jarvis
messaging tools, the record transfers to the Admin actor, which becomes the
executor until the handoff to the Project Manager; only one session executes it
at a time.

The Contract verifies prerequisites, including Jarvis Core 0.32.0 or newer in
the instance that hosts the session, which Setup may install after the User's
consent, and release identity, audits a dry run,
preserves existing project-owned configuration, installs the Syspilot role cards,
creates nine persistent Syspilot actors through Jarvis, validates the target
build, and completes User-guided Git
integration before handoff. A mandatory gate that is `pending` or `failed`, such
as Actor discovery or a documentation build with warnings, blocks the verified
baseline and the handoff. Setup's direct writes to the Jarvis message files are
short but not concurrency-safe; the Contract states that limit to the adopting
User and records it, and asks for consent before appending to an existing
Admin's queue. It records the exact release and commit in
`.syspilot/project.toml`, permanently pinning the project's approved baseline.
When it asks for the Setup branch approval it opens the Contract in the User's
editor, and the executor records each transfer of the record, to the Admin when
it occurs and to the Project Manager, in its own Handover log. If a User decision widens the approved scope after a gate has
passed, the executor sets the affected gates back to open and passes them again
before sealing the project state.

The successful handoff identifies the selected ontology and its configured
path. The Project Manager explains its artifact types, statuses, and
relationships and asks the User whether it fits. Acceptance continues normal
project intake without an ontology Change. A requested adjustment starts a
normal Change before modification and uses the existing Ontology skill only as
technical guidance.

Deferred practical scenarios remain undemonstrated. Automated text, scaffold,
and fixture checks are not end-to-end runtime proof, and a reported Setup run
does not establish which individual scenarios passed. Keep those evidence
limits separate from the supported installation steps in
[Getting Started](getting-started.md).

## Updates Are Separate Changes

A project does not routinely track the newest Syspilot version. Its approved
baseline remains pinned for the project lifetime. A later update requires a
separate project-specific Change containing the old and proposed baselines,
impact analysis, revalidation scope, User authorization, and an assigned
technical executor.

Jarvis installation, compatibility, and extension updates have their own
lifecycle and are outside Syspilot's project-update policy.

A project that runs a Syspilot version before 0.10 can use the
[upgrade checklist](upgrade.md) as input for that Change. The checklist does
not replace the Change: the Change still owns the baselines, the impact
analysis, and the User's authorization.

## Release Responsibility

The Release actor owns packaging, release delivery, preflight verification, and
the release notes. The Technical Writer owns the guides and project portal;
Release checks that owner's completed artifact rather than writing it. A release
should not move because the calendar is impatient; it moves when its artifacts
and evidence say it is ready.

Each publication runs under a Release Contract, defined by the
[Release process](Syspilot%20Contracts/release.md). Its preflight runs on the
`development` commit to be released, with release notes and user documentation
already committed. Four local checks run in order: documentation tests, the
strict clean documentation build, release QA suites, and the version check
(`uv run python scripts/check_release_version.py v{version}`). The strict build
needs network access to `docs.python.org`. The first failure stops the release
before `main` or a tag moves and becomes an open quality issue for its owner.

The newest release-notes version heading is the version source.
`docs/conf.py` derives the documentation's `release` from it. The same checker
is used locally and by the tag workflow to reject a malformed tag, a missing or
duplicate heading, an older heading, or inconsistent documentation metadata.

A separate validation-only workflow run is required only when workflow inputs
changed since the last successful tag run, Admin records an environment change,
or the immediately preceding release has no successful tag run. Release checks
Admin's trigger list and environment evidence at release start. A triggered run
needs a pushed branch and the User's explicit authorization. Local checks do not
prove execution on the Linux runner or publication; platform-specific failures
may first appear after the tag exists. The User's push authorization acknowledges
that trade-off. Failed validation or documentation-build prerequisites publish
nothing, but publication is not atomic: Pages may already be deployed when
GitHub Release creation fails. Any failure after the tag, including partial
publication, stops the release, becomes a recorded blocker and is escalated to
the User; the tag stays in place.

Commit the push authorization in the release record after the preflighted
commit P and before merging to release commit R. The separate, write-free check
`uv run python scripts/check_release_record.py P R v{version}` checks the
ancestor/path rule, protected content, version, P's full SHA and required
template headings. It does not establish evidence-only changes: Quality and
Release must review the complete P-to-R diff before publication, including
unprotected procedure and failure-rule text. Non-evidence changes are rejected
or require a new preflight. Evidence unavailable in R is recorded after the tag
in a later record-only commit, without moving the tag.
[Branching](branching.md) explains the sequence and comparison in more detail.

Release notes remain release-facing documentation rather than part of the
Technical Writer's documentation ownership map. The Technical Writer may still
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

Check that Jarvis Core 0.32.0 or newer is installed in the VS Code instance and
profile that host the session; an extension list read through another `code`
command is not evidence. An installed extension does not guarantee that the
session offers its tools; a window reload may be needed. An ordinary chat session
does not offer the Jarvis messaging tools; Actor chats do. Confirm the
destination uses the exact actor name. A message queued for automatic delivery
is announced to the Actor's chat once Jarvis marks its entry `notified`; that does
not show that the Actor has acted on it. A failed message does not
authorize editing another actor's memory or pretending a handoff occurred.

## Operational Ownership

- The release-bound Setup Contract owns pristine installation behavior while
   its initiating Copilot session or, after a transfer, the Admin executes the
   current instance.
- Release owns packaging, delivery, and what the release gate checks and
  publishes. It is the mandatory consultee on every change to a release
  workflow definition and decides whether a gate change is acceptable.
- Admin owns build, test, and documentation tooling, workflow and CI
  definitions, and repository conflicts outside the development flow. That
  includes the wiring of release workflows: jobs, steps, runners, and
  dependencies.
- The process owner owns each canonical Contract template.
- The Technical Writer owns these user guides and their `doc` Needs.
- The factual owner of a source artifact remains the authority on its behavior.

This division is useful during incidents: route the problem to the owner of the
affected outcome, keep the current blocker visible, and resist the urge to fix
an authority problem with a longer troubleshooting page.