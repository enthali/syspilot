# Pristine Syspilot Setup

**Status:** preparing | blocked | verified | handed off<br>
**Executor:** initiating Copilot session<br>
**Current responsibility:** initiating Copilot session | Syspilot Project Manager<br>
**Current blocker:** none | {unmet condition and required action}<br>
**Target project root:** {path}<br>
**Provided release tag:** {exact SemVer tag}<br>
**Verified commit:** pending | {full SHA}<br>

## Phase 1: Establish Target And Prerequisites

Do not modify the target project in this phase.

1. Identify the writable, version-controlled project root. Verify and record that `.syspilot/setup-contract.md` is the only tracked, staged, or untracked working-tree change.
2. Read `.syspilot/project.toml` when present. A confirmed Syspilot baseline stops pristine Setup. Show other Syspilot-like paths to the User and record whether to preserve them, integrate with them, or stop.
3. Ask the User to approve a dedicated Setup branch, then create it from the selected project state.
4. Verify that the provided release tag identifies one full commit and use only that commit tree as the installation source.
5. Verify VS Code with GitHub Copilot, Git, Python 3.13 or newer, `uv`, and Jarvis Core 0.25 or newer are available.
6. Record `jarvis_listActors` and `jarvis_listChatSessions` before installation.

Existing committed project content is allowed and remains untouched unless the User approves an additive integration edit.

## Phase 2: Verify Contract Inventory

Read the installation inventory below. Verify that every destination is unique and stays inside the target root, every copied source belongs to the verified commit, every generated artifact has a complete definition, and every mandatory entry is present.

## Phase 3: Generate And Audit Setup Script

Generate a release-specific Setup script from the Contract inventory. The script must support `--dry-run` and use the same planning and execution path in both modes; dry-run suppresses writes but reports every planned create, copy, generation, verification, and collision.

### Installation Jobs

The following list is the Contract-owned installation inventory. Directory jobs recurse over all release-owned files below the source path while excluding generated build output, virtual environments, caches, and Change instances.

| Job | Mode | Source or input | Destination | Class | Required verification |
|---|---|---|---|---|---|
| Actor role cards | copy eight files | The eight role cards listed below | `docs/Syspilot Actors/` | release-owned | Exactly the eight listed persistent role cards exist |
| Actor registry | generate | Eight-actor list below | `docs/Syspilot Actors/index.md` | generated instance | Registry links exactly the eight installed role cards |
| Contract processes | copy directory | `docs/Syspilot Processes/` | `docs/Syspilot Processes/` | release-owned | Process registry, Contract Documents, Change Process, and Setup Process exist |
| Syspilot skills | copy directory | `.github/skills/` | `.github/skills/` | release-owned | Every release skill contains `SKILL.md` and declared supporting files |
| Setup record | retain materialized file | This runbook | `.syspilot/setup-contract.md` | generated instance | Status, responsibility, blockers, and evidence remain available with the installed project |
| Documentation build | inspect, then preserve or generate | Existing project build, or verified-commit `docs/docs-build.py` | Existing build paths, or `docs/docs-build.py`, `docs/conf.py`, and `docs/index.rst` | user-owned or generated instance | The recorded target build command succeeds with the configured ontology and zero warnings |
| Sphinx-Needs environment | preserve or install | Existing project environment, or verified-commit `docs/requirements.txt` | Existing environment, or project-local `.venv/` | user-owned or generated instance | Existing Sphinx-Needs remains unchanged, or `uv venv .venv` and `uv pip install --python .venv -r {verified commit tree}/docs/requirements.txt` succeed |
| Project baseline | generate | Provided release tag, verified commit, and Contract state | `.syspilot/project.toml` | generated instance | Required baseline fields parse and match the provided release |
| Syspilot actor persistence | inspect then ask if ignored | Git ignore result and User decision | Project Git policy | user-owned | User explicitly decides whether the eight generated Syspilot actor directories are versioned; resulting rules match that decision |
| Project ontology | detect, then preserve or copy | Existing configured ontology, or verified-commit `.syspilot/ontology.toml` | Existing configured path, or `.syspilot/ontology.toml` | user-owned or generated instance | Existing ontology remains unchanged, or baseline TOML is copied only when no ontology exists; the target documentation build succeeds |
| Setup script | generate temporarily | This inventory and Contract rules | Executor-selected system temporary path | transient | Platform-appropriate script supports `--dry-run`; dry-run and execution share one planning path; file remains available for inspection |
| Syspilot actors | generate eight folders | Actor definitions below | `.jarvis/actors/<name>/` | generated instance | Eight YAML entities and contexts exist; Jarvis lists all eight |

Generate `.syspilot/project.toml` as:

```toml
schema_version = 1
source_repository = "https://github.com/enthali/syspilot"
release_tag = "{provided tag}"
commit_sha = "{full commit SHA for provided tag}"
baseline_status = "preparing"
```

Apply the persistence choice to each of the eight generated Syspilot actor directories as one unit, including `actor.yaml`, `context.md`, and all memory files stored below that actor directory.

Inspect the target independently for its configured ontology, Sphinx-Needs availability, dependency files, documentation structure, and build command.

1. Detect an ontology in `conf.py`, `ubproject.toml`, or another TOML source. Preserve it unchanged when present. Copy the verified commit's `.syspilot/ontology.toml` only when no ontology exists.
2. Detect Sphinx-Needs independently. Preserve its environment when available. When unavailable, run `uv venv .venv` and `uv pip install --python .venv -r {verified commit tree}/docs/requirements.txt`.
3. Preserve existing dependency and documentation files. Ask the User to approve the exact additive dependency, configuration, and navigation edits required to use the selected environment and ontology and expose installed Syspilot documentation. Copy `docs/docs-build.py` and generate minimal `docs/conf.py` or `docs/index.rst` only where those build or documentation files are absent. Never overwrite an existing file.
4. Run the target documentation build with the selected ontology and require zero warnings.

Ontology evaluation or modification is not part of Setup.

### Syspilot Actor Setup

Generate exactly these eight actors:

| Actor name | Public role card |
|---|---|
| Syspilot Project Manager | `docs/Syspilot Actors/Syspilot Project Manager.md` |
| Syspilot Architect | `docs/Syspilot Actors/Syspilot Architect.md` |
| Syspilot Developer | `docs/Syspilot Actors/Syspilot Developer.md` |
| Syspilot Tester | `docs/Syspilot Actors/Syspilot Tester.md` |
| Syspilot Quality | `docs/Syspilot Actors/Syspilot Quality.md` |
| Syspilot Release | `docs/Syspilot Actors/Syspilot Release.md` |
| Syspilot Research | `docs/Syspilot Actors/Syspilot Research.md` |
| Syspilot Technical Writer | `docs/Syspilot Actors/Syspilot Technical Writer.md` |

Each actor folder contains:

- `actor.yaml` with at least the exact actor `name`;
- `context.md` whose first durable instruction links to that actor's public role card; and
- a second durable instruction to read `docs/Syspilot Processes/index.md` at session start and follow every applicable Contract process.

Setup writes these files directly and does not call `jarvis_createActor`. The generated context contains no machine-specific path, session history, or preloaded project decisions.

Perform actor setup in this order:

1. Inspect existing `.jarvis/actors/` contents. Show colliding target actor paths to the User for disposition; unrelated actors remain untouched.
2. Use `git check-ignore` on each of the eight target actor directories.
3. If the directories are ignored, ask the User whether the complete eight generated Syspilot actor directories shall be committed.
4. If the User chooses persistence, add only the specific Git negation rules required to make those eight directories versionable.
5. If the User declines persistence, preserve an existing ignore rule or add ignore rules for exactly those eight directories when none applies.
6. Generate the eight `actor.yaml` and initial `context.md` pairs.
7. Install the remaining Contract inventory.
8. Allow up to 60 seconds for the Jarvis actor rescan, then use `jarvis_listActors` to verify that it includes all eight expected entities; unrelated actors are allowed.
9. Record generated paths, Git treatment, registration result, and any blocker as Contract evidence.

Run `--dry-run` and classify every destination: create absent files, retain identical files, apply only User-approved additive integration edits, and block on other differing files. Audit the generated script and complete plan before execution.

## Phase 4: Execute Setup Script

Execute the audited platform-appropriate temporary script without `--dry-run` on the dedicated Setup branch. Record its exit status and every created, retained, skipped, and failed destination as Contract evidence.

On script failure, stop and keep the branch for inspection. Git is the cleanup boundary: the user may discard the Setup branch to return to the exact starting project state. The script must not implement a second destructive rollback mechanism.

## Phase 5: Verify Installed Outcome

| Gate | Proposed pass condition |
|---|---|
| Integrity | Every release-owned destination matches the source identity or verification rule declared by the Contract inventory |
| Inventory | Compare the script operation log with the inventory; every declared destination exists and every written path is declared or an approved integration edit |
| Structure | Required Syspilot skill, process, ontology, and documentation integration entry points exist |
| Jarvis actor discovery | Compare before/after snapshots: `jarvis_listActors` includes all eight expected Syspilot actors, no Setup actor was generated, and `jarvis_listChatSessions` contains no session opened by Setup |
| Actor files | Exactly eight expected actor folders contain valid `actor.yaml` and initial `context.md` |
| Documentation | The target project's documentation builds successfully with its selected ontology and zero warnings |
| Baseline | `project.toml` reads back the provided SemVer tag and corresponding commit |
| Project preservation | Git status and approved integration evidence show only the initial Setup Contract, declared Setup outputs, and approved integration edits changed from the starting commit |

Record each command, exit status, and concise result. One failed mandatory gate leaves the Setup branch and Contract `blocked`; Setup does not mark the baseline verified or continue to handoff.

## Phase 6: Seal Project State

1. Set `baseline_status = "verified"` after all mandatory gates pass.
2. Ask the User how to commit and merge the installation.
3. Stage only declared Setup outputs and approved integration edits, commit them, and merge the Setup branch into the User-selected target branch without absorbing unrelated changes.

## Phase 7: Hand Off To Project Manager

1. Set current responsibility to `Syspilot Project Manager`, set Contract status to `handed off`, and commit the final Setup record on the target branch.
2. Send `Installation complete, welcome to this project` to the Syspilot Project Manager with:
	- the installation completion summary; and
	- instructions to visualize and evaluate the ontology with the User and, when appropriate, propose updating it as the first Change.
3. If delivery fails, record the delivery blocker in the durable Setup record without claiming successful receipt and commit that evidence. Keep the verified integrated installation.

## Failure And Resume Rules

- Before target writes, failure leaves only the materialized Contract and status `blocked`.
- After target writes, failure leaves status `blocked`, an exact path disposition, and the dedicated branch for inspection or deletion.
- Open mandatory gates prohibit `verified`, success messaging, and PM handoff.
- Cleanup discards the dedicated Setup branch for versioned changes and removes only untracked actor paths that this Setup run demonstrably created; it never deletes pre-existing or user-owned content.

## Evidence Summary

| Area | Result | Evidence or blocker |
|---|---|---|
| Prerequisites | pending | pending |
| Contract inventory | pending | pending |
| Script dry-run and audit | pending | pending |
| Script execution | pending | pending |
| Mandatory verification | pending | pending |
| Project commit | pending | pending |
| PM handoff | pending | pending |
