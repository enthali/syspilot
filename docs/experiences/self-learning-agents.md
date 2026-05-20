# Self-Learning Agents

**Topic:** How I added an Analyst to diagnose quality degradation in a running multi-agent workflow

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.118 |
| Jarvis | 0.5.8 |
| syspilot | 0.5.3 |
| Sphinx | 9.1.0 |
| sphinx-needs | 8.0.0 |

---

## The Situation

At some point during active syspilot development I notice something odd: the Quality Manager raises more findings per change than it used to. The number creeps up — not dramatically, but consistently.

I can't explain it. Three hypotheses:

1. **QM is getting stricter** — its context has drifted toward more aggressive checking
2. **CM is making more mistakes** — the growing codebase means more things to get wrong
3. **I'm formulating CRs differently** — maybe as PM I'm starting changes with less clarity

The problem: I have no data. I'm watching outputs but not patterns.

## What I Did

I add a fourth agent session — the **Analyst**. Its role is not to change anything, not to approve anything. It sits outside the change flow and observes.

The Analyst receives copies of messages from QM (findings reports) and from PM (CR submissions, merge decisions). It looks for patterns:

- Are findings clustered around certain types of changes?
- Are findings concentrated on specific spec levels (L0/L1/L2)?
- Is there a correlation between CR formulation and finding count?
- Are the same elements appearing in findings repeatedly?

The Analyst reports patterns and hypotheses back to me as PM. I decide whether to act — adjust the CM workflow, refine how I write CRs, or update QM's check scope.

## What Makes This Work

The agents are now watching themselves. QM checks the work. Analyst checks the pattern of QM findings. PM evaluates both.

No single agent has the full picture — and that's intentional. QM doesn't know it's being monitored for drift. CM doesn't adjust its behavior based on Analyst feedback directly. The separation keeps each agent honest.

Jarvis message queuing is what makes this possible: the Analyst just subscribes to the same message stream that already exists. No changes to CM or QM needed — I add an observer without touching the workflow.

## What to Watch Out For

**The Analyst needs enough history.** A single finding means nothing. Patterns emerge over several changes. Don't act on the first Analyst report — give it time to accumulate signal.

**Correlation is not causation.** The Analyst finds patterns, not root causes. "Findings spike after L1-heavy CRs" is an observation, not an explanation. I still have to interpret.

## The Payoff

The system now tells me when something is drifting before it becomes a real problem. I don't have to notice it myself — I just read the Analyst report alongside the QM findings.

It's a small step toward a workflow that improves itself over time.

---

*For more details, feel free to read the full case study: [Self-Optimizing Agents](case-study-self-optimizing-agents.md)*
