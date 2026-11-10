# Pristine Syspilot Setup

**Status:** preparing | blocked | verified | handed off<br>
**Executor:** initiating Copilot session | Admin<br>
**Current responsibility:** initiating Copilot session | Admin | Project Manager<br>
**Current blocker:** none | {unmet condition and required action}<br>
**Target project root:** {path}<br>
**Provided release tag:** {exact SemVer tag}<br>
**Verified commit:** pending | {full SHA}<br>
**Project name:** pending | {confirmed project name}<br>

## Handover log

The executor is one session at a time, named by `Executor` in the header: the initiating session, or the Admin Actor after the transfer of Phase 3. The executor appends one line as the last act before every transfer of the record, namely the transfer to the Admin when it occurs and the handoff to the Project Manager, in the same commit that changes `Executor` and `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the executor did and the facts that change the next owner's situation; evidence stays in the Evidence Summary. The log explains the transition; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|

## Phase 1: Establish Target And Prerequisites

Do not modify the target project in this phase.

1. Identify the writable, version-controlled project root. Verify and record that `.syspilot/setup-contract.md` is the only tracked, staged, or untracked working-tree change.
2. Read `.syspilot/project.toml` when present. A confirmed Syspilot baseline stops pristine Setup. Show other Syspilot-like paths to the User and record whether to preserve them, integrate with them, or stop.
3. Ask the User to approve a dedicated Setup branch, and in that same step open `.syspilot/setup-contract.md` in the User's editor, because the User reviews the Contract before deciding; then create the branch from the selected project state.
4. Verify that the provided release tag identifies one full commit and use only that commit tree as the installation source.
5. Verify VS Code with GitHub Copilot, Git, Python 3.13 or newer, and `uv` are available, and establish Jarvis Core 0.32.0 or newer in the VS Code instance and profile that host this session, with no Jarvis tool. Jarvis Core 0.32.0 is the first release whose messaging tools are bound to Actor chats and which no longer offers `jarvis_listChatSessions`.
   - Identify the hosting instance before reading any extension list, from evidence about the running host and not from the first `code` command on the search path, because that command may address another installation: find the process that hosts this session's shell from the shell's ancestry, and record the installation it runs from, the `--user-data-dir` and `--extensions-dir` on its command line or the platform defaults when the command line carries none, and the profile in use. A version read through a `code` command that does not belong to the host is not evidence: an earlier test run recorded Jarvis Core 0.32.0 for a target whose own extension directory held no Jarvis package.
   - When the hosting instance cannot be identified with such evidence, as in a window attached to a remote host or container, stop with a recorded blocker, install nothing, claim no version, and give the User the manual path: install `enthali.jarvis-core` from the Extensions view of that window and tell the session to continue.
   - Read the extension list with the command line tool of the identified installation and the recorded directories, for example `--list-extensions --show-versions`, and accept no version read anywhere else. Record the version.
   - When Jarvis Core is absent or older than 0.32.0, explain to the User in one step its purpose for Syspilot (persistent Actors and their messaging), the extension identifier `enthali.jarvis-core`, the Marketplace as its source, and the instance and profile that receive it, and ask for consent there. Install nothing without it. When the User refuses, stop with a recorded blocker and the manual path above.
   - After consent, install only `enthali.jarvis-core` with the command line tool and directories that identified the instance, with `--profile` when the instance uses a profile other than the default, and edit no User or project setting. Record the exit status of each command. When the installation fails, record the exit status and the tool's output as a blocker, give the manual path, and do not continue as if it had succeeded.
   - Read the extension list again with the same tool and directories and require version 0.32.0 or newer; an installed extension is not an available tool, so step 8 still establishes the tools that the session offers.
   - Record the instance evidence, the versions before and after, and the consent or refusal in the Evidence Summary. A missing or older Jarvis Core that remains after these steps is a blocker.
6. Confirm the project name before the Actors folder scan and the tool check, and before any destination is verified or written, so that every `summary` the manual Actor path shows is composed with the confirmed name. Propose the name of the target project folder, ask the User to confirm or change it, and record the confirmed name in the `Project name` header field of this record. Accept only letters, digits, spaces, hyphens, underscores, and dots that are neither leading nor trailing; no name that consists of dots only; and no reserved Windows device name (`CON`, `PRN`, `AUX`, `NUL`, `COM1` to `COM9`, `LPT1` to `LPT9`, with or without an extension). The name becomes a folder name, a Sphinx table-of-contents entry, and a Markdown path on every platform. A name that is not accepted is asked for again and never altered. The name is the one source for the folders `docs/<Project name> Actors/` and `docs/<Project name> Contracts/`, the documentation scaffold, and every reference that follows from it. A resumed Setup keeps the recorded name. The name stays fixed once the first write to an installed destination in Phase 4 has happened, and not before: the branch, the header of this record, and the dry run are not such a write. A later change is a widened scope, after which the affected gates are set back to `pending` as the Failure And Resume Rules state.
7. Record the Actors folder scan, before the tool check so that it exists whichever way that check ends: resolve the Actors folder from `jarvis.actors.folder` (default `.jarvis/actors`) and list the folder and name of every `actor.yaml` below it. This is a scan and not a listing; the ordinary session has no listing tool, and this Contract claims no equivalence between the two. A resumed Setup keeps this recorded scan as the before state. Tell the User that Jarvis opens the chat of a new Actor while `jarvis.actors.openSessionOnCreate` is enabled and that this setting turns it off; do not edit the User's or the project's settings.
8. Record, per tool name and without assuming any, whether this session offers `jarvis_createActor`, `jarvis_listActors`, `jarvis_sendMessage`, and `jarvis_receiveMessage`, and record the Jarvis version. Jarvis binds the three messaging tools to Actor chats, so an ordinary Copilot session does not offer them, while `jarvis_createActor` is a tool of the ordinary chat.
   - When the session offers all four, it stays executor and no transfer happens.
   - When it lacks `jarvis_createActor`, stop with a recorded blocker before any write to the target other than this record, because Setup creates Actors only through Jarvis. Give the User two ways forward: enable `jarvis_core_createActor` in the Chat tool picker and tell the session to continue, or, when the tool is not offered at all, the manual creation path of Syspilot Actor Setup.
   - When it offers `jarvis_createActor` but lacks a messaging tool, the record transfers to the Admin as Phase 4 describes.
   - When step 5 installed Jarvis Core in this run and the session lacks `jarvis_createActor`, report an installed extension whose tools the session does not offer as a distinct condition and not as success, and ask the User to reload the window only then, in place of the blocker above. Record that the reload was requested and that the resume prompt was given. The resume prompt is composed under the language rule of the Transfer To The Admin section (the User's language, English when that language is ambiguous, with paths and tool names unchanged) and tells a new chat in the reloaded window to continue the Pristine Syspilot Setup recorded in `.syspilot/setup-contract.md` and to read that record first, because a reload ends the chat session and nothing else tells a new session how to continue. The resumed session reads the Jarvis version and its tools again, resumes from the recorded state, and keeps the recorded before scan. When the tools are offered after the installation, continue without a reload; one reported run in which Actor creation became available without a reload is not a guarantee.
9. Run `git check-ignore` on `.github/instructions/` and `.github/skills/`. An existing ignore rule that would silently exclude a generated destination is a blocker; an occupied destination with unrelated existing files is not — those files are preserved during the additive copy.

Existing committed project content is allowed and remains untouched unless the User approves an additive integration edit.

## Phase 2: Verify Contract Inventory

Read the installation inventory below. Verify that every destination is unique and stays inside the target root, every copied source belongs to the verified commit, every generated artifact has a complete definition, and every mandatory entry is present.

## Phase 3: Generate And Audit Setup Script

Generate a release-specific Setup script from the Contract inventory and the Contract selection. The script must support `--dry-run` and use the same planning and execution path in both modes; dry-run suppresses writes but reports every planned create, copy, generation, verification, and collision.

### Contract Selection

Before generating the script, ask the User which example Contracts to install, recommend starting with the Change Process alone, and say that adding the others later is the project's own task, starting from `docs/Example Contracts/` of its pinned release. Contract Documents is always installed, because every Contract process links to it as its method. When a selected Contract requires another, add the required Contract to the selection and tell the User which one was added; the reason is that the target's zero-warning documentation build reports a link that does not resolve. Record the final selection in the Evidence Summary.

| Contract | File in `docs/Example Contracts/` | Selection | Requires |
|---|---|---|---|
| Contract Documents | `contract-documents.md` | always installed | none |
| Change Process | `change.md` | recommended first | Contract Documents |
| Release Process | `release.md` | optional | Contract Documents |
| Process Maintenance | `process-maintenance.md` | optional | Contract Documents, Change Process |

The nine role cards are installed whichever Contracts are selected, because a role card names no Contract process. An actor whose process is not installed, such as Release without the Release Process, has no assignment from that process until the project adopts it.

### Installation Jobs

The following list is the Contract-owned installation inventory. The `Class` column is the only statement of who owns an installed artifact, and section headings name no artifact owner; the executor named in the header holds the Setup record until handoff. A `seeded copy` is copied from the example folders of the verified commit, is identical to its source when Setup verifies it, and belongs to the project from the handoff on; later adaptation is not a deviation, and Setup does not check it again. Directory jobs recurse over all release-owned or seeded files below the source path while excluding generated build output, virtual environments, caches, and Change instances.

| Job | Mode | Source or input | Destination | Class | Required verification |
|---|---|---|---|---|---|
| Actor role cards | copy nine files | The nine role cards listed below, taken from `docs/Example Actors/` | `docs/<Project name> Actors/` | seeded copy | Exactly the nine listed persistent role cards exist, each identical to its source |
| Actor registry | generate | Nine-actor list below | `docs/<Project name> Actors/index.md`, titled `<Project name> Actors` | generated instance | Registry links exactly the nine installed role cards and carries a hidden table of contents naming exactly those cards |
| Contract processes | copy selected files | The files named by the Contract selection, directly below `docs/Example Contracts/`; `index.md` and `setup.md` of `docs/Syspilot Contracts/` are not among them | `docs/<Project name> Contracts/`, each under its own file name | seeded copy | `contract-documents.md` and every selected Contract exist, each identical to its source; no unselected Contract file exists |
| Contract registry | generate | Preamble of `docs/Example Contracts/index.md` above its `Processes` heading, and the Contract selection | `docs/<Project name> Contracts/index.md`, titled `<Project name> Contracts` | generated instance | Registry links exactly the installed Contracts and carries a hidden table of contents naming exactly those Contracts |
| Syspilot skills | copy directory, additive | `.github/skills/` | `.github/skills/` | release-owned | Every release skill contains `SKILL.md` and declared supporting files; existing unrelated files in an occupied directory are preserved |
| Syspilot instructions | copy directory, additive | `.github/instructions/` | `.github/instructions/` | release-owned | Every release instruction matches its verified-commit source identity and `syspilot.contract-handling.instructions.md` exists; existing unrelated files in an occupied directory are preserved |
| Setup record | retain materialized file | This runbook | `.syspilot/setup-contract.md` | generated instance | Status, responsibility, blockers, and evidence remain available with the installed project |
| Documentation build | inspect, then preserve or generate | Existing project build, or verified-commit `docs/docs-build.py` and the scaffold definitions below | Existing build paths, or `docs/docs-build.py`, `docs/conf.py`, and `docs/index.rst` | user-owned or generated instance | The recorded target build command succeeds with the configured ontology and zero warnings; a generated `docs/conf.py` and `docs/index.rst` match the scaffold definitions |
| Sphinx-Needs environment | preserve or install | Existing project environment, or verified-commit `docs/requirements.txt` | Existing environment, or project-local `.venv/` | user-owned or generated instance | Existing Sphinx-Needs remains unchanged, or `uv venv .venv` and `uv pip install --python .venv -r {verified commit tree}/docs/requirements.txt` succeed; the Sphinx-Needs version of the environment in use is recorded |
| Project baseline | generate | Provided release tag, verified commit, and Contract state | `.syspilot/project.toml` | generated instance | Required baseline fields parse and match the provided release |
| Syspilot actor persistence | inspect then ask | Git ignore result and User decision | Project Git policy | user-owned | User explicitly decides whether the nine generated Syspilot actor directories are versioned; resulting rules match that decision |
| Project ontology | detect, then preserve or copy | Existing configured ontology, or verified-commit `.syspilot/ontology.toml` | Existing configured path, or `.syspilot/ontology.toml` | user-owned or generated instance | Existing ontology remains unchanged, or baseline TOML is copied only when no ontology exists; the target documentation build succeeds |
| Setup script | generate temporarily | This inventory and Contract rules | Executor-selected system temporary path | transient | Platform-appropriate script supports `--dry-run`; dry-run and execution share one planning path; file remains available for inspection |
| Syspilot actors | create nine Actors through Jarvis | Actor definitions below | The Actors folder, at the path `jarvis_createActor` returns for each Actor it creates or finds, or the path the second folder scan finds for an Actor the User created | generated instance | Nine Actors exist, each recorded as created or pre-existing with its recorded path; each created `context.md` names both project-root-relative paths and they resolve to installed files; Jarvis lists all nine |

Generate `.syspilot/project.toml` as:

```toml
schema_version = 1
source_repository = "https://github.com/enthali/syspilot"
release_tag = "{provided tag}"
commit_sha = "{full commit SHA for provided tag}"
baseline_status = "preparing"
```

Inspect the target independently for its configured ontology, Sphinx-Needs availability, dependency files, documentation structure, and build command.

1. Detect an ontology in `conf.py`, `ubproject.toml`, or another TOML source. Preserve it unchanged when present. Copy the verified commit's `.syspilot/ontology.toml` only when no ontology exists.
2. Detect Sphinx-Needs independently. Preserve its environment when available. When unavailable, run `uv venv .venv` and `uv pip install --python .venv -r {verified commit tree}/docs/requirements.txt`. Record the Sphinx-Needs version of the environment in use. When Setup itself has to bind an ontology through `needs_from_toml`, namely in a generated `docs/conf.py` or an approved additive edit, and that version is older than 4.1.0, the first release with that configuration, stop with a recorded blocker and User guidance, and bind nothing against that environment. An existing configured ontology and its environment stay untouched whatever the version.
3. Preserve existing dependency and documentation files. Ask the User to approve the exact additive dependency, configuration, and navigation edits required to use the selected environment and ontology and expose installed Syspilot documentation; in the same step show the confirmed project name from the header of this record, which the scaffold uses, and let the User change it only as Phase 1 step 6 allows. Copy `docs/docs-build.py` and generate `docs/conf.py` or `docs/index.rst` from the scaffold definitions below only where those build or documentation files are absent. Never overwrite an existing file.
4. Run the target documentation build with the selected ontology and require zero warnings.

Ontology evaluation or modification is not part of Setup.

### Documentation Scaffold

The generated `docs/conf.py` carries no Syspilot project name, author, release, copyright, logo, or other Syspilot metadata, and refers only to files and settings that the target has after installation: no template folder, static folder, logo, stylesheet, source-project path, or intersphinx inventory fetched from the network. It loads only `myst_parser` and `sphinx_needs`, which the installed `docs/requirements.txt` provides, and has no hook that writes `docs/ontology-reference.md`; that page is Syspilot's own internal reference, and the closed Change `sphinx-needs-graph-alignment` decided not to deliver it to installed projects. `needs_from_toml` is a literal string assignment, because the shipped Impact, MECE, and Trace skills read that literal without executing `conf.py` and fail on a computed binding. `changes/*` is excluded, because Change Contracts are process records and not pages. `needs.deprecated` is suppressed, because the shipped `.syspilot/ontology.toml` uses Needs options that Sphinx-Needs reports as deprecated and the strict build would fail on them, as Syspilot's own `docs/conf.py` also suppresses.

```python
project = "{confirmed project name}"

extensions = ["myst_parser", "sphinx_needs"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv", "changes/*"]

needs_from_toml = "{ontology path relative to conf.py}"

suppress_warnings = ["needs.deprecated"]
```

The generated `docs/index.rst` has the project name as title and one table of contents that lists only `<Project name> Actors/index` and `<Project name> Contracts/index`, with the recorded name and its space in each entry. Each generated registry has the title `<Project name> Actors` or `<Project name> Contracts` and also carries a hidden table of contents, so the build with `-W` has no orphaned page:

````markdown
```{toctree}
:hidden:

{one entry per installed role card, or per installed Contract}
```
````

Install no `docs/ontology-reference.md`. For a target that already has a documentation build, offer the registries and the changed navigation entries only as additive edits that the User approves.

### Syspilot Actor Setup

Create exactly these nine Actors through Jarvis. Each public role card is the seeded copy of `docs/Example Actors/<name>.md`:

| Actor name | Domain | Public role card |
|---|---|---|
| Project Manager | Strategy, intake, portfolio management | `docs/<Project name> Actors/Project Manager.md` |
| Architect | Technical architecture, design guidelines | `docs/<Project name> Actors/Architect.md` |
| Developer | Implementation, unit testing | `docs/<Project name> Actors/Developer.md` |
| Tester | Adversarial testing | `docs/<Project name> Actors/Tester.md` |
| Quality | Quality review | `docs/<Project name> Actors/Quality.md` |
| Release | Packaging, release delivery | `docs/<Project name> Actors/Release.md` |
| Research | Investigation, technical due diligence | `docs/<Project name> Actors/Research.md` |
| Technical Writer | User-facing product documentation | `docs/<Project name> Actors/Technical Writer.md` |
| Admin | Tools, repository infrastructure, process maintenance | `docs/<Project name> Actors/Admin.md` |

`<Project name>` is the name recorded in the header of this record under Phase 1 step 6; every path above and below carries that name, followed by one space and `Actors` or `Contracts`. Setup writes no `actor.yaml` or `context.md` itself. Jarvis writes the `summary` as the body of the new `context.md` and offers no other input for its content, so the two durable instructions travel in the `summary`. Compose each `summary` as one paragraph that names the Actor's domain, states that its role card is the file at the project-root-relative path from the table with the recorded name, and instructs the Actor to read the project-root-relative path `docs/<Project name> Contracts/index.md` at the start of every session, with the recorded name, and follow every applicable Contract process. Write both paths as code spans that state they are relative to the project root, never as relative links, because the depth of an Actor folder below the project root depends on `jarvis.actors.folder`. The summary contains no machine-specific path, session history, or preloaded project decisions.

Perform Actor setup in Phase 4, after the audited script has run, so that the role cards and the registry exist, in this order:

1. Show the User every target Actor that already exists in the before scan. Unrelated Actors remain untouched.
2. Call `jarvis_createActor` once per Actor, from a session that offers it, with the exact name and the `summary`, and without `initialMessage`; skip an Actor that the manual creation path below has created. When the record transfers to the Admin, create the other eight Actors here and leave the Admin to the Transfer To The Admin section, which creates it last with the request as `initialMessage`. An Actor reported as `created: false` is left unchanged and recorded as pre-existing with its returned path; it is not claimed as configured by Setup.
3. Record per Actor whether it was created or pre-existing, and its path: the path `jarvis_createActor` returned for an Actor it created or found, and the path the second folder scan finds for an Actor the User created. Use these recorded paths, not assumed ones, for every later step.
4. Use `git check-ignore` on each recorded Actor directory, show the result, and ask the User whether the complete nine Actor directories shall be versioned or kept private and ignored. If the User chooses persistence, add only the specific Git negation rules required; if the User declines, preserve an existing ignore rule or add ignore rules for exactly those nine directories when none applies. When the Admin is created later, check its returned path against the same decision.
5. Verify for each created Actor that both paths in its `context.md` resolve against the project root to installed files.
6. Record the paths, Git treatment, and any blocker as Contract evidence. The after state comes from `jarvis_listActors`, with up to 60 seconds allowed for the Jarvis rescan; the executor that offers the tool records it, and unrelated Actors are allowed in both states.

Manual creation path, offered when the session does not offer `jarvis_createActor`, in this order: Setup has recorded the before scan in Phase 1 step 7, before the tool check, and then stops with the blocker of step 8 and shows the User the nine exact names with their `summary` paragraphs. The User creates each Actor with the `+` command of the Jarvis ACTORS view, which uses the same routine, and enters the paragraph at its Summary prompt. The resumed Setup keeps the recorded before scan, scans the folder again for the after observation, and writes nothing to these Actors, because Jarvis leaves the `context.md` of an Actor to the Actor itself. The path that the folder scan finds for each Actor the User created serves as its recorded path for the persistence decision and the ignore check. Setup counts an Actor as created for this Setup only when it was absent from the before scan, has one of the nine names, its `context.md` names both paths, and the User confirms explicitly, name by name, that the User created it for this Setup. Any other Actor, and any ambiguous or colliding state, is a recorded blocker and is not claimed. A `context.md` without both paths fails the Actor gate and the correction stays with the User. An Admin that the User created this way is an existing Admin in the sense of the Transfer To The Admin section.

Setup calls no messaging tool and writes no message to any queue, except the one request to an existing Admin that the User consents to in the Transfer To The Admin section; the only other request to an Actor is the Admin's `initialMessage`, which Jarvis queues. Setup opens no Actor session itself. Setup creates no Setup actor.

Apply the persistence choice to each of the nine Actor directories as one unit, including `actor.yaml`, `context.md`, and all memory files stored below that directory.

Run `--dry-run` and classify every destination: create absent files, retain identical files, apply only User-approved additive integration edits, and block on other differing files. Audit the generated script and complete plan before execution.

## Phase 4: Execute Setup Script

Execute the audited platform-appropriate temporary script without `--dry-run` on the dedicated Setup branch. Record its exit status and every created, retained, skipped, and failed destination as Contract evidence. Then perform the Actor setup of Syspilot Actor Setup.

On script failure, stop and keep the branch for inspection. Git is the cleanup boundary: the user may discard the Setup branch to return to the exact starting project state. The script must not implement a second destructive rollback mechanism.

### Transfer To The Admin

A session that offered all four Jarvis tools at Phase 1 step 8 stays executor and skips this section. Otherwise transfer the record to the Admin after the other eight Actors exist and the script has run, before the first Phase 5 gate that needs a tool the session lacks.

1. Show the User whether an Admin Actor already exists in the recorded scan. An existing Admin's files stay unchanged; when the User declines to use it, stop without a transfer. For an existing Admin, ask the User in this step whether Setup may append the request to `.jarvis/messages/queue.json` directly, and state the limit of that write: Jarvis writes this file without a lock from heartbeat jobs, reminders, and Actors, so an entry written between Setup's read and write is overwritten and no read back can show it; the User decided on 2026-11-09 that this risk is very small in a freshly installed project.
2. Add `Admin` to `.jarvis/messages/autodelivery.json` unless it is listed: read the existing content, add the name, write the whole content once, and read it back to show that every earlier name is unchanged. When the file exists and is not a JSON array, stop with a recorded blocker and do not rewrite it. State in the record as a limit that a concurrent write in this short interval could overwrite the file, which Jarvis writes only for a User's context-menu command; this is a limit and not a safe path.
3. Make the transfer: set `Executor` and `Current responsibility` to `Admin`, append the Handover-log entry, and commit the record, so that a request never exists for a record that does not name the Admin.
4. Create the Admin through `jarvis_createActor` with its `summary` and the request text as `initialMessage`. Jarvis itself appends the request to `.jarvis/messages/queue.json` within its own process; Setup never writes the queue file, because a separate read-modify-write of the shared queue can overwrite an entry that another writer added between Setup's read and write, which a read back cannot detect. After a created Admin, the initiating session changes the record only to record a delivery blocker.
5. When the Admin already exists and the User accepts it, Jarvis offers no supported function to send the request, because it drops an `initialMessage` for an existing Actor. After the commit of step 3 and with the User's consent from step 1, append one entry with destination `Admin`, sender `Setup`, the request text, and an ISO 8601 UTC timestamp to `.jarvis/messages/queue.json`: read the existing content once, add the entry, write the whole content once, and read it back to show that every entry read before the write is unchanged. When the file exists and is not a JSON array, stop with a recorded blocker and do not rewrite it. When the User withholds the consent, write nothing to the queue, claim no queued request, and give the User the manual path of step 9 with the manual prompt in the same step.
6. The request text contains these elements and no other instruction: that it continues a Pristine Syspilot Setup whose initiating session lacks the Jarvis messaging tools; the absolute paths of the target project root and the Setup record; the instruction to re-read its own `context.md`, its role card, and the Setup record and to verify that the header names the Admin as executor before acting; the instruction to continue from the first open phase of the record as its executor; and the statement that Jarvis, and no Actor, sent the request, so that the acknowledgement is a row in the Evidence Summary of the record and not a message.
7. Compose the request and the manual prompt in the language the User used with the initiating session, and in English when that language is ambiguous, with paths, tool names, and file names unchanged. Record the language chosen and why. The Setup record holds the manual prompt, which is the request text.
8. The only evidence of continuation is the Admin's acknowledgement row in the Evidence Summary, committed to the record; wait up to 120 seconds after creating the Admin or appending the request for it. The 120 seconds are a chosen bound, not a measurement. Read the queue only as a diagnostic, because the Admin's receipt removes the queue entry and with it its `notified` flag. Without an acknowledgement, an entry that is present and `notified` means announced and not yet acted on, an entry that is present and not `notified` means automatic delivery has not run, and an entry that is absent means consumed or deleted, which cannot be told apart. No case is reported as delivered, and a consumed request is never reported as a failed delivery once the row exists.
9. When Actor creation, automatic delivery, or continuation is unavailable or not evidenced in time, record a delivery blocker without claiming receipt, keep the committed header, and give the User the manual path: open the chat of the Admin Actor from the ACTORS view and paste the manual prompt that the Setup record holds.

The Admin, as executor, holds every later gate alone, runs the discovery check and the handoff to the Project Manager with its own messaging tools, and appends the Handover-log entry for that handoff.

## Phase 5: Verify Installed Outcome

| Gate | Status | Pass condition |
|---|---|---|
| Integrity | pending | Every release-owned destination matches the source identity or verification rule declared by the Contract inventory, and every seeded destination is identical to its example source at this verification |
| Inventory | pending | Compare the script operation log with the inventory; every declared destination exists and every written path is declared or an approved integration edit |
| Structure | pending | Required Syspilot instruction, skill, process, ontology, and documentation integration entry points exist, including the two folders `docs/<Project name> Actors/` and `docs/<Project name> Contracts/` and no folder named after Syspilot; `syspilot.contract-handling.instructions.md` is installed |
| Jarvis actor discovery | pending | Compare the recorded folder scan with `jarvis_listActors`, allowing up to 60 seconds for the Jarvis rescan: the listing includes all nine expected Syspilot Actors, no Setup actor was generated, and Setup wrote no message to any queue except the consented request to an existing Admin |
| Actor files | pending | Each of the nine Actors is recorded as created or pre-existing with its recorded path, each created `context.md` names both project-root-relative paths and they resolve to installed files, and no other Syspilot Actor files exist |
| Documentation | pending | The target project's documentation builds successfully with its selected ontology; the observed number of warnings is recorded as evidence and must be zero |
| Baseline | pending | `project.toml` reads back the provided SemVer tag and corresponding commit |
| Project preservation | pending | Git status and approved integration evidence show only the initial Setup Contract, declared Setup outputs, and approved integration edits changed from the starting commit |

The Executor owns every gate in this table and alone records its evidence and passes it; the User owns none of them. This holds for the executor that the header names at that time, and the gate pass of the initiating session stays valid after a transfer.

Each gate has exactly one status: `pending`, `passed`, or `failed`, recorded in the Evidence Summary with its command, exit status, and concise result. The mandatory gates are exactly the rows of the table above; the Evidence Summary row `PM handoff` is a delivery row outside them, so status `verified` with the Project Manager named and `PM handoff` `pending` does not contradict the rule that every mandatory gate is `passed`. No other status exists, such as `conditional`. While any gate is `pending` or `failed`, including the discovery gate while the Actors are not listed after the allowed wait and the documentation gate with a warning count above zero, the Contract status stays `blocked`, `baseline_status` stays `"preparing"`, and `Current blocker` names the gate and the required action; Setup does not mark the baseline verified or continue to handoff. A blocker that survives a transfer stays visible in the header, so that the next executor starts from it.

## Phase 6: Seal Project State

1. Re-read this record and `.syspilot/project.toml`. Stop when they disagree about the baseline status or when a gate is not `passed`.
2. Set the Contract status to `verified` and `baseline_status = "verified"` only after every gate is `passed`.
3. Ask the User how to commit and merge the installation.
4. Stage only declared Setup outputs and approved integration edits, commit them, and merge the Setup branch into the User-selected target branch without absorbing unrelated changes.

## Phase 7: Hand Off To Project Manager

1. Complete the Git integration of Phase 6. Then re-read this record and `.syspilot/project.toml` and stop when they disagree about the baseline status or when a gate is not `passed`. Otherwise keep Contract status `verified`, set `Current responsibility` to `Project Manager`, append the Handover-log entry, record the Evidence Summary row `PM handoff` as `pending`, and commit the Setup record on the target branch in one commit, which Contract handling requires before the message is sent. Status `handed off` is not set here, because it claims a receipt that does not yet exist; `PM handoff` is a delivery row and not a Phase 5 gate, so it stays `pending` while the status is `verified`. When the Admin is executor, it does this with its own messaging tools.
2. Send `Installation complete, welcome to this project` to the Project Manager with:
	- the installation completion summary;
	- the selected ontology and its configured path;
	- the installed Contracts and the actors that have no installed process yet;
	- the project-root-relative paths of the two installed folders, `docs/<Project name> Actors/` and `docs/<Project name> Contracts/`, with the recorded name; and
	- instructions to explain the selected ontology's artifact types, statuses, and relationships to the User and ask whether it fits the project.
3. The Project Manager re-reads its `context.md`, its role card, and this Setup record, and verifies that the committed header names it, before it acts on the message. After it has acknowledged the message, the Project Manager's own first commit on the record sets Contract status `handed off` and the row `PM handoff` to `passed`.
4. The executor reports completion to the User only after that acknowledgement. Before it, the executor says that the message was sent and that the acknowledgement is awaited.
5. If the User accepts the selected ontology, continue normal project intake without creating an ontology Change.
6. If the User requests an adjustment, start a normal Change before modifying the ontology. Use the existing `syspilot.ontology` skill only as technical guidance inside that Change.
7. If sending the message fails, leave the record unchanged, because the executor makes no change to a record it no longer holds: status `verified` with the Project Manager named and `PM handoff` `pending` is the visible state of an unacknowledged handoff. Report the failure to the User with the manual path: tell the chat of the Project Manager the path of this Setup record and ask it to perform the refresh and header check. Keep the verified integrated installation.

## Failure And Resume Rules

- Before target writes, failure leaves only the materialized Contract and status `blocked`.
- After target writes, failure leaves status `blocked`, an exact path disposition, and the dedicated branch for inspection or deletion.
- Open mandatory gates prohibit `verified`, success messaging, and PM handoff. The statuses `pending` and `failed` both block; no `conditional` result exists.
- A failed Actor creation, automatic delivery, or continuation records a blocker and gives the User the manual path of Phase 1 step 8 or of the Transfer To The Admin section; it is never reported as done.
- When a User decision widens the approved scope after a gate has passed, such as an additional integration edit, a changed persistence choice, a changed Contract selection, or a changed project name, the executor sets the affected gates back to `pending` and passes them again before sealing the project state.
- Cleanup discards the dedicated Setup branch for versioned changes and removes only untracked Actor paths that this Setup run demonstrably created; it never deletes pre-existing or user-owned content. Actors created through Jarvis are removed by the User from the ACTORS view.

## Evidence Summary

The mandatory gates are the Phase 5 rows. The row `PM handoff` is a delivery row outside them: the executor leaves it `pending` in the handoff commit, and the Project Manager sets it `passed` with status `handed off` after its acknowledgement.

| Area | Result | Evidence or blocker |
|---|---|---|
| Prerequisites | pending | pending |
| Jarvis Core instance and installation | pending | pending |
| Jarvis tools and version | pending | pending |
| Actors folder scan before | pending | pending |
| Contract inventory | pending | pending |
| Contract selection | pending | pending |
| Script dry-run and audit | pending | pending |
| Script execution | pending | pending |
| Actor creation | pending | pending |
| Transfer to Admin and delivery | pending | pending |
| Mandatory verification | pending | pending |
| Project commit | pending | pending |
| PM handoff | pending | pending |
