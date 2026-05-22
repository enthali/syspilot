# syspilot

Requirements engineering toolkit for AI-assisted development using sphinx-needs traceability.

## Specification Hierarchy

```
Level 0: User Stories (WHY)     docs/syspilot/userstories/    SYSP_US_*
         ▲ :links:
         │
Level 1: Requirements (WHAT)    docs/syspilot/requirements/   SYSP_REQ_*
         ▲ :links:
         │
Level 2: Design Specs (HOW)     docs/syspilot/design/         SYSP_SPEC_*
```

## Product vs. Instance

- `.github/` — these are the agents, prompts, and skills we **run** (installed instance)
- `syspilot/` — these are the agents, prompts, and skills we **work on and ship** (product)

Changes go into `syspilot/`. The Setup Agent installs them into `.github/`.

## Language

All documents, specs, commit messages, and code comments shall be in English.

## Dogfooding

This project develops itself using its own agents and skills.
The agents you are running ARE the product being developed.
Be aware of circular dependencies — changes to agent specs affect your own (future) behavior.

## Culture

**No blame language.** Change Documents, CRs, findings, and commit messages describe structural gaps and improvements — not causes or actors. Every gap is an opportunity to improve the system. Every mistake is a chance to learn.
