# Ontology Reference

This page describes the ontology that Syspilot uses for its own specification: which kinds of
artifacts exist, which statuses they can hold, and which named links connect them. The strict
documentation build enforces the ontology file `ontology.toml` beside this page, and the Impact,
MECE and Trace skills read the same file. This page is maintained by hand and is reviewed in
version control together with the file it describes.

The ontology describes the shape of the graph. It does not assign artifacts to actors: the
applicable Contract declares ownership, current responsibility, decisions and evidence for each
change.

## Type Catalogue

| Directive | Title | Prefix | Question it answers |
|-----------|-------|--------|---------------------|
| `root` | Graph Root | `ROOT_` | Where does the graph start? The single anchor; every story traces to it. |
| `story` | User Story | `US_` | Why? The user need a requirement serves. |
| `req` | Requirement | `REQ_` | What? An observable obligation of the product. |
| `ac` | Acceptance Criterion | `AC_` | Did we build the right thing? User-facing, judged by a human, linked to the story it validates. |
| `vc` | Verification Criterion | `VC_` | Did we build it right? Testable, linked to the requirement it verifies. |
| `doc` | User Documentation | `DOC_` | Where is it explained? A user-facing documentation surface; `realized_by` points to a document without Needs markup. |

## Link Diagram

Arrows show stored outgoing links. The diagram is written by hand, because `[[needs.extra_links]]`
does not name endpoint types; a test compares its edges with the links of the built graph.

```{mermaid}
flowchart BT
    root["root: Graph Root"]
    story["story: User Story"]
    req["req: Requirement"]
    ac["ac: Acceptance Criterion"]
    vc["vc: Verification Criterion"]
    doc["doc: User Documentation"]

    story -->|tracked_by| root
    req -->|implements| story
    req -->|specializes| req
    ac -->|validates| story
    vc -->|verifies| req
    doc -->|includes| req
```

## Links

A link is stored on the Need it starts from and points outward. Sphinx-Needs also exports the
incoming side, so every link can be followed in both directions.

| Link | From | To | Incoming name | Meaning |
|---|---|---|---|---|
| `tracked_by` | `story` | `root` | `tracks` | The story declares its membership in the graph. |
| `implements` | `req` | `story` | `is implemented by` | The requirement realizes the story's reason. |
| `specializes` | `req` | `req` | `is specialized by` | A concrete requirement applies a more general one; it points from concrete to general, never sideways. |
| `validates` | `ac` | `story` | `is validated by` | The criterion shows that the story's intent is satisfied. |
| `verifies` | `vc` | `req` | `is verified by` | The criterion shows that the requirement is correctly implemented. |
| `includes` | `doc` | `req` | `included_in` | The surface explains the requirement in user-oriented form; the incoming side shows which documents to review when the requirement changes. |

## Required Links

The strict documentation build fails when a minimum link is missing:

| Need | Required incoming links | Required outgoing links |
|---|---|---|
| `story` | At least one `validates` from an `ac` and at least one `implements` from a `req` | none from these checks |
| `req` | At least one `verifies` from a `vc` | At least one `implements` to a `story` |

`includes`, `specializes` and `tracked_by` carry no presence obligation here. The endpoint types of
`validates`, `implements` and `verifies` are checked by `[[needs.schema_definitions.schemas]]`
rules, so a link from or to a wrong type also fails the strict build. The checks establish minimum
presence and permitted endpoint types, not whether the relationship is semantically correct.

## Options

Every Need type accepts these additional options:

| Option | Use |
|---|---|
| `priority` | The relative importance of the Need. |
| `rationale` | The reason behind the Need. |
| `realized_by` | A plain path to the file that is the realization, such as code, configuration or a document kept outside the specification graph. It is a path, not a link to another Need. |

## Statuses

| Status | Meaning |
|---|---|
| `draft` | Work in progress. |
| `open` | Identified but not yet started. |
| `approved` | Ready for implementation. |
| `implemented` | Code exists. |
| `verified` | Tested and validated. |
| `deprecated` | No longer used. |
