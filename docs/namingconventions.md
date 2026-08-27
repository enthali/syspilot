# Naming Conventions

Syspilot uses descriptive, human-readable IDs for specification elements:
`SYSP_REQ_IMPACT_QUERY` rather than `REQ_042`. This page explains why, what the
ontology actually enforces, and what this repository does by convention.

The distinction matters more than it sounds. Some of what follows is a rule the
build will enforce. The rest is a habit this repository keeps, and a customer
project is free to keep a different one.

## Why Descriptive IDs?

| Aspect | Sequential (`REQ_042`) | Descriptive (`SYSP_REQ_IMPACT_QUERY`) |
|--------|------------------------|---------------------------------------|
| Self-documenting | No — you have to look it up | Yes — readable where it appears |
| Inserting new items | Renumber, or leave gaps and hope | Just pick a name |
| Grep-friendly | Not really | `grep IMPACT_QUERY` finds everything |
| Link readability | Opaque | Clear |
| Ordering bias | Implies a priority or sequence | No false hierarchy |
| Duplicate safety | Manual tracking | Sphinx-Needs catches it at build time |

## What the Ontology Fixes

The project ontology decides three things, and the strict build enforces all of
them:

- **Every Need carries an explicit ID.** `id_required` is set, so nothing is
  auto-numbered behind your back.
- **IDs are globally unique.** Sphinx-Needs rejects a duplicate at build time
  rather than letting two elements quietly share a name.
- **Each type declares a `prefix`** — `ROOT_`, `US_`, `REQ_`, `AC_`, `VC_`,
  `DOC_` in the baseline ontology. Read the current values in the
  [Ontology Reference](ontology-reference.md).

That last point is easy to misread. Sphinx-Needs uses a type `prefix` when it
*generates* an ID. Because Syspilot requires explicit IDs, the prefix is not a
naming contract for the IDs you write. Nothing validates that an explicit ID
begins with its type prefix.

## What This Repository Does

Every active non-root ID in this repository follows one shape:

```
SYSP_<TYPE>_<SLUG>
```

for example `SYSP_US_SETUP`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_AC_SETUP_1`,
`SYSP_VC_RELEASE_1`, and `SYSP_DOC_README`. All 67 of them, without exception.

The graph root is the one different-looking ID: `ROOT_SYSPILOT` puts the type
first. That is deliberate rather than accidental — v2 introduced exactly one
deterministic root anchor, and this ID names it.

This shape is the current convention of the Syspilot product repository. It is
not a requirement, and no validator checks it.

## What Is Not Decided

Syspilot does not currently specify a universal project prefix or a full-ID
template for projects that adopt it. With the baseline ontology, a project
assigns explicit, globally unique, valid IDs — and that is the whole rule.

So a project may mirror `SYSP_<TYPE>_<SLUG>` with its own prefix, or use the
type prefixes alone, or something else entirely. Choosing one for your project
is a real decision that belongs in a Contract, not something to infer from this
page. Consistency inside a project is worth far more than matching Syspilot's
habits.

## Writing a Good Slug

1. **Keep slugs short**: 2–4 words maximum
2. **Be specific**: `ANALYZE` not `DO_ANALYSIS_OF_CHANGES`
3. **Use domain language**: terms stakeholders recognize
4. **Avoid ambiguity**: `NEW_PROJECT` vs `ADOPT_EXISTING`, not `INSTALL_1`
5. **ALL CAPS**: `SYSP_US_CHG_ANALYZE` not `sysp_us_chg_analyze`
6. **Underscores only**: no hyphens, no dots

## Renaming an ID

A rename is mechanical, and the build is the safety net:

1. Write down the complete old-to-new mapping before touching anything.
2. Rename the `:id:` fields.
3. Update every typed link that referenced the old ID — `implements`,
   `specializes`, `validates`, `verifies`, `includes`, `tracked_by`, and any
   project-defined link your ontology adds.
4. Update references outside the specification: skills, instructions, Contracts,
   scripts, and release notes.
5. Run the strict build. It fails on anything you missed, which is exactly what
   you want it to do.


