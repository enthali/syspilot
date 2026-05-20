# Case Study: Self-Optimizing Agents

**Context:** syspilot development, ongoing  
**Topic:** Using an Analyst agent to diagnose quality degradation in a running multi-agent workflow

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.121 |
| Jarvis | 0.5.11 |
| syspilot | 0.5.5 |
| Sphinx | 9.1.0 |
| sphinx-needs | 8.0.0 |

---

## The Observation

At some point during active syspilot development I noticed something odd: the Quality Manager was raising more findings per change than in earlier sessions. The number was creeping up — not dramatically, but consistently.

I couldn't explain it. Three hypotheses:

1. **QM was getting stricter** — its prompts or context had drifted toward more aggressive checking
2. **CM was making more mistakes** — the growing codebase meant more things to get wrong
3. **I was formulating CRs differently** — maybe as PM I was starting changes with less clarity

The problem with all three: I had no data. I was watching outputs but not patterns.

## The Response: Adding an Analyst

I added a fourth agent session — the **Analyst**. Its role is not to change anything, not to approve anything. It sits outside the change flow and observes.

The Analyst receives copies of messages from QM (findings reports) and from PM (CR submissions, merge decisions). Over time it builds a picture:

- Are findings clustered around certain types of changes?
- Are findings concentrated on specific spec levels (L0/L1/L2)?
- Is there a correlation between CR formulation quality and finding count?
- Are the same elements appearing in findings repeatedly?

The Analyst doesn't fix anything. It reports patterns and hypotheses back to PM. PM decides whether to act — adjust the CM workflow, refine how I write CRs, or update QM's check scope.

## What Makes This Interesting

The agents are now watching themselves. QM checks the work. Analyst checks the pattern of QM findings. PM evaluates both.

No single agent has the full picture — that's intentional. QM shouldn't know it's being monitored for drift. CM shouldn't adjust its behavior based on Analyst feedback directly. The separation keeps each agent honest.

This is a first step toward a system that can identify its own failure modes without me having to notice them first.

## Status

Early experiment. The Analyst concept works — pattern observation over a message stream is well within what an LLM session handles. Whether the patterns it identifies are always meaningful is a different question. That's what the next few sessions will tell.

---

*See also:* [Auto Agent Messaging with Jarvis Sessions](auto-agent-messaging.md)
