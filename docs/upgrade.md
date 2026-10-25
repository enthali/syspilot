# Upgrading to Syspilot 0.10

This checklist is for a project that already works with actors, Contracts, and
skills from an earlier Syspilot version, or from a comparable earlier setup, and
wants to move to 0.10. The [Setup Contract](Syspilot%20Contracts/setup.md)
installs into pristine projects only, so there is no automated upgrade path.
Version 0.10 is not released yet; check the [release notes](releasenotes.md)
before you rely on any step here.

The checklist is distilled from one completed migration. The adopter who made
that migration reviewed it for accuracy. That review did not include running the
0.10 skills, and nobody who has not migrated has read it cold, so treat it as a
guide, not as a proven procedure. It
feeds the project-specific update Change described in
[Operations](operations.md) under "Updates Are Separate Changes"; it does not
replace that Change. The Change still owns the old and proposed baselines, the impact
analysis, the revalidation scope, the User's authorization, and the named
technical executor.

## Before You Start

1. Open the update as a normal Change on its own feature branch.
2. Record the old baseline and the proposed 0.10 baseline in the Contract.
3. Make a list of everything the old setup placed in the repository: agent
   files, role and process definitions, skills, instructions, actor memory, and
   ontology configuration. Steps 2, 3, and 10 use this list.

## Steps

The order below is the one the field migration followed, except that agent files
leave before new actors arrive, for the reason given under Pitfalls.

1. **Clean actor memory.** Move active next steps and process rules out of
   actor memory. A next step that belongs to a piece of work goes into that
   work's Contract; a rule that belongs to a role goes into the role card. An
   item that belongs to neither, such as a backlog entry, a watch item, or a
   deferred finding, goes into the Project Manager's memory.
2. **Take an inventory.** Map, merge, or drop each old role against the nine
   0.10 roles in the [actor registry](Syspilot%20Actors/index.md). In the field
   migration, a change-manager role was carried by the Contract, a
   setup-engineer role was dropped, and a quality-manager and a
   verification-engineer role were merged into Quality. For every item in the
   list from *Before You Start*, decide whether to drop it, move it into a
   Contract, or move it into actor memory. The table under "Put Knowledge in
   the Right Place" in [Customization](customization.md) shows where each kind
   of knowledge belongs.
3. **Remove old agent files and tailoring files.** Tailoring files are the
   files in which the old setup kept a project's role-specific adaptations; in
   Syspilot v1 they were the `syspilot.<name>.tailoring.md` files. Do this
   before creating any 0.10 actor.
4. **Decide where actor memory lives.** Versioned with the project or private is
   a project decision. Keep all actor folders in one place, under one
   decision, and apply it to each generated actor directory as one unit.
5. **Create the nine actors.** Each `context.md` starts with two durable
   instructions: read the actor's role card, and read the Contract registry at
   session start. The [Setup Contract](Syspilot%20Contracts/setup.md) lists the
   roles and the files each actor folder holds.
6. **Derive your Contracts and role cards** from the 0.10 canonical templates in
   `docs/Syspilot Contracts/` and `docs/Syspilot Actors/`. Install
   `syspilot.contract-handling.instructions.md`, and keep project-specific
   knowledge in actor memory or in the project-owned levels that
   [Customization](customization.md) describes.
7. **Replace old skills** with the 0.10 skills for impact, MECE, trace, and the
   ontology. Copy each skill's `SKILL.md` and runtime scripts only. You can copy
   them before step 8, but they run only once the binding from step 8 exists,
   or when you pass `--ontology` with a path to an existing TOML file.
8. **Move the ontology** out of `conf.py` into its own TOML file that
   `conf.py` reads through a top-level literal string `needs_from_toml` binding.
   Each `needs_<name>` setting in `conf.py`, such as `needs_types`,
   `needs_statuses`, `needs_extra_links`, and `needs_extra_options`, becomes the
   matching entry without the prefix under the `[needs]` table, for example
   `[[needs.types]]`. The ontology skill describes the format. The Impact, MECE,
   and Trace scripts read `docs/conf.py`, take the ontology path from that
   literal, and resolve a relative path against the directory of `conf.py`. If
   your binding is computed, pass `--ontology` explicitly; `--ontology` always
   bypasses the discovery. The first check below proves that the move changed
   nothing.
9. **Reduce `copilot-instructions.md`** to facts about the project itself.
10. **Remove the old in-repo actor memory.** Then squash-integrate the branch
    into your development branch. Commits made to the old in-repo memory on the
    development branch while the migration ran produce modify/delete conflicts
    at the merge; resolve them by deleting the files.
11. **Run a check-in.** Ask each actor to state its role in one sentence and to
    report every contradiction between its memory and its role card. Say in the
    request who receives the reports. Confirm that every actor answered,
    because silence reads as no contradictions. Act on what the actors report.

## Checks

- Run the strict documentation build after the ontology move, and compare the
  exported Needs with a baseline taken before the move. The exported Needs file
  carries `created` timestamps at the top level and per version; remove both
  before comparing. Nothing else should differ.
- Run `git check-ignore` on the ontology file, the instruction files, and the
  skill folders.
- Read each actor's memory against its role card. The check-in in step 11
  surfaces real contradictions, so do not skip it.
- Run an impact analysis for specifications that describe the old process as
  product behavior. Those need their own Change.
- Search for scripts that still copy old templates.

## Pitfalls

- **Agent files bind by name.** A leftover agent file can give a new actor the
  old persona. Remove old agent files before you create the new actors.
- **Ignore rules can hide required files.** A broad pattern such as a shared
  name prefix can exclude the ontology file. To keep files under an otherwise
  ignored directory, ignore its contents with `dir/*`, because Git cannot
  re-include a file whose parent directory is excluded with `dir/`. The Setup
  Contract treats an ignore rule that silently excludes a generated destination
  as a blocker.
- **Occupied destinations.** Setup copies Syspilot's files alongside unrelated
  files that already sit in `.github/instructions/` or `.github/skills/`. A
  different file at a path Syspilot needs is integrated only with the User's
  approval, and otherwise blocks Setup. Existing role or agent files are not
  covered, so step 3 and step 6 are yours.
- **Typed links and `doc` Needs may be missing.** The Change template assumes
  them. A project without them adds the optional `Ontology Binding` subsection,
  which maps each Contract artifact to the project's own artifact kind.
- **Old negations and next steps survive cleanup.** The check-in found them
  after the cleanup had missed them. A check-in answered by a weaker model gives
  a weaker check, so run it with the model you use for real work.
- **Process content inside product specifications outlives the migration.**
  Plan its removal as a separate Change right after the merge. Specifications
  can also prescribe the content of `copilot-instructions.md`; one migration
  found five such elements. Step 9 makes them false, so include them in the
  impact analysis of that follow-up Change.
