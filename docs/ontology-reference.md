<!-- AUTO-GENERATED — do not edit manually. Regenerated on every sphinx-build. -->

# Ontology Reference

## Type Catalogue

| Directive | Title | Prefix | Color |
|-----------|-------|--------|-------|
| `story` | User Story | US_ | #E8D5B7 |
| `req` | Requirement | REQ_ | #BFD8D2 |
| `spec` | Design Specification | SPEC_ | #FEDCD2 |
| `def` | DEFINITION | DEF_ | #C8A4D4 |
| `impl` | Implementation | IMPL_ | #DF744A |
| `test` | Test Case (deprecated — use uat, unit_test, or test) | TEST_ | #DCB239 |
| `uat` | UAT Test Case | UAT_ | #A8E6CF |
| `unit_test` | Unit Test | UNIT_ | #FFD3B6 |

## Type Relationships

```{mermaid}
flowchart BT
    req -->|provides| story
    spec -->|implements| req
    impl -->|implements| spec
    test -->|verifies| req
    uat -->|validates| story
    unit_test -->|verifies| spec
    def -->|defines| spec
```

## Status Lifecycle

```{mermaid}
stateDiagram-v2
    draft --> approved
    draft --> open
    open --> draft
    open --> approved
    approved --> implemented
    implemented --> verified
    approved --> draft
    [*] --> deprecated : from any
```
