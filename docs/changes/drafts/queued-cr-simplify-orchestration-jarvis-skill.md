# Queued CR Draft: simplify-orchestration-jarvis-skill

**GH Issue**: #47
**Status**: queued (not yet branched)
**Proposed Operation Mode**: autonomous (well-specified, small, mechanical)

---

## Summary (draft)

The `syspilot.orchestration-jarvis` skill (`SKILL.md`) carries three kinds of content that no longer belong in it:

1. **Runtime RESPOND mode-detection logic** — the file currently explains how an agent should decide, at runtime, whether to SEND its result back to a sender or emit direct structured output, based on whether RECEIVE found a pending message. This is unnecessary: the *skill variant itself* (this Jarvis skill vs. the traditional/subagent skill) is what determines the mode, statically, at install time. A project either installs this skill (every agent is a persistent session, RESPOND always means SEND-back) or the other one (RESPOND always means direct output) — never both. No runtime branching logic is needed.
2. **The `agents:` frontmatter / `runSubagent` exception section** — describes a carve-out for the Setup Bootloader's synchronous `runSubagent` call to the Installer. This was never actually this skill's concern: if an agent (the Setup Bootloader) needs a specific tool for a specific structural reason, that belongs in the agent's own spec/tools list, not documented as an exception inside the shared orchestration vocabulary skill. Removing it here doesn't remove the capability — it just stops misplacing its documentation.
3. **Traceability header prose** (`> Implements:`, `> Requirements:`) — this is build/tooling metadata irrelevant to an LLM reading the skill to act on it. Should move into structured YAML frontmatter fields, not the Markdown body.

Motivation: the skill has accumulated documentation for concerns (runtime mode detection, a specific agent's tool exception) that don't belong in a shared, reusable orchestration vocabulary skill. Trimming these makes the skill purely about SEND/RECEIVE/RESPOND, and reduces the context an LLM has to parse to use it correctly.

Acceptance criteria:
- `SKILL.md` body contains only: skill description, SEND/RECEIVE/RESPOND definitions, and concrete tool-call syntax for each verb — no runtime mode-detection logic, no `agents:`/`runSubagent` exception content
- Traceability metadata (`Implements`/`Requirements`) moved to YAML frontmatter, not Markdown body prose
- No agent (including Setup Bootloader) loses functionality — `runSubagent` documentation, if still needed, lives in the Setup Bootloader's own agent spec/tools list instead
- sphinx-build `-W` passes clean

---

## Next steps once branch is safe to create

1. `git checkout experimental && git pull && git checkout -b feature/simplify-orchestration-jarvis-skill`
2. Copy `syspilot/templates/change-document.md` to `docs/changes/simplify-orchestration-jarvis-skill.md`
3. Fill header + Summary (content above) — Operation Mode: autonomous
4. Commit + push branch
5. SEND to Change Manager
