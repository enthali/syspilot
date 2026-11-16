# Ontology

This ontology defines what the project can trace: which kinds of artifacts exist,
which statuses they can hold, and which named links connect them. The strict
documentation build enforces it, and the Impact, MECE, and Trace skills read the
same file. It is a starting point. The project owns it and changes it through a
normal Change, because a change to the ontology reaches back through everything
the project has recorded so far.

The ontology describes the shape of the graph. It does not assign artifacts to
actors: the applicable Contract declares ownership, current responsibility,
decisions, and evidence for each change.

## The Chain

Most work follows one chain from the reason for the work to its evidence. Each
arrow names a link that points from the first type to the second:

- `story` tracked_by `root`
- `req` implements `story`
- `design` details `req`
- `ac` validates `story`
- `vc` verifies `req` or `design`
- `doc` includes `req`

A `req` may also specialize another `req`.

```{mermaid}
flowchart BT
    root["root: Graph Root"]
    story["story: User Story"]
    req["req: Requirement"]
    design["design: Detailed Design"]
    ac["ac: Acceptance Criterion"]
    vc["vc: Verification Criterion"]
    doc["doc: User Documentation"]

    story -->|tracked_by| root
    req -->|implements| story
    req -->|specializes| req
    design -->|details| req
    ac -->|validates| story
    vc -->|verifies| req
    vc -->|verifies| design
    doc -->|includes| req
```

Arrows show stored outgoing links.

## Need Types

| Type | Prefix | Question it answers | Meaning |
|---|---|---|---|
| `root` | `ROOT_` | Where does the graph start? | The single graph anchor. Exactly one exists per project. Every story traces to it, so impact analysis and orphan detection start from one deterministic node. |
| `story` | `US_` | Why? | The user need a requirement serves. |
| `req` | `REQ_` | What? | An observable obligation of the product. |
| `design` | `DES_` | How, in detail? | The detailed design that realizes one requirement. |
| `ac` | `AC_` | Did we build the right thing? | An acceptance criterion: user-facing and judged by a human, one per Given/When/Then, linked to the story it validates. |
| `vc` | `VC_` | Did we build it right? | A verification criterion: testable, linked to the requirement or design it verifies. |
| `doc` | `DOC_` | Where is it explained? | A user-facing documentation surface. The Need stays in the graph while `realized_by` points to a document that carries no Needs markup. |

Every Need carries an explicit ID, and IDs are unique across the project.

## Links

A link is stored on the Need it starts from and points outward. Sphinx-Needs also
exports the incoming side, so every link can be followed in both directions.

| Link | From | To | Incoming name | Meaning |
|---|---|---|---|---|
| `tracked_by` | `story` | `root` | `tracks` | The story declares its membership in the graph. |
| `implements` | `req` | `story` | `is implemented by` | The requirement realizes the story's reason. |
| `specializes` | `req` | `req` | `is specialized by` | A concrete requirement applies a more general one. It always points from concrete to general, never sideways between two unrelated concrete requirements. |
| `details` | `design` | `req` | `is detailed by` | The design elaborates how one requirement is realized. |
| `validates` | `ac` | `story` | `is validated by` | The criterion shows that the story's intent is satisfied. |
| `verifies` | `vc` | `req` or `design` | `is verified by` | The criterion shows that the requirement or design is correctly implemented. |
| `includes` | `doc` | `req` | `included_in` | The surface explains the requirement in user-oriented form. The incoming side exposes which documents deserve review when the requirement changes. |

A `design` that details no requirement, or a requirement that implements no
story, shows up when Trace reviews the observed links.

## Options

Every Need type accepts these additional options:

| Option | Use |
|---|---|
| `priority` | The relative importance of the Need. |
| `rationale` | The reason behind the Need. |
| `realized_by` | A plain path to the file that is the realization, such as code, configuration, or a document the project keeps outside the specification graph. It is a path, not a link to another Need. |

## Statuses

| Status | Meaning |
|---|---|
| `draft` | Work in progress. |
| `open` | Identified but not yet started. |
| `approved` | Ready for implementation. |
| `implemented` | Code exists. |
| `verified` | Tested and validated. |
| `deprecated` | No longer used. |

## Changing It

Treat an adjustment as technical Contract work. Preserve unrelated project
content, change only the schema surfaces the file already represents, and run the
strict documentation build afterward. Resolve every ontology warning before the
artifact is complete.
