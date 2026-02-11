# Skill: Presenting Choices via Selection Menus

> **Implements**: SPEC_AGENT_INTERACTION
> **Requirements**: REQ_DX_AGENT_SELECTION_MENUS, REQ_DX_AGENT_SKILL_FILES

When presenting choices to the user, use VS Code's `ask_questions` tool
(quick-pick selection menus) instead of plain-text numbered lists.

## When to Use `ask_questions`

- Workflow transitions (level navigation, agent handoffs within session)
- Decisions with 2–6 discrete options
- Confirmations where alternatives exist (approve / revise / pause)

## When NOT to Use

- Free-form questions requiring typed answers (use normal conversation)
- Single yes/no confirmations with no meaningful alternatives

## Format

```
ask_questions({
  questions: [{
    header: "≤12 chars",        // Quick-pick title, unique ID
    question: "Full context",    // Explains what is being decided
    options: [
      { label: "Option A", description: "Brief detail" },
      { label: "Option B", description: "Brief detail", recommended: true }
    ],
    allowFreeformInput: false    // true when custom response is expected
  }]
})
```

## Rules

1. **`recommended`** marks the agent's suggested default — the user sees it pre-selected
2. **`allowFreeformInput: true`** when the user may want a custom response beyond listed options
3. **Max 4 questions** per call, **2–6 options** each
4. **Batch related questions** into a single call
5. **Every option** must include a `label` and a `description`

## Examples

### Level Transition (Change Agent)

```
ask_questions({
  questions: [{
    header: "Continue?",
    question: "Level 1 is saved to the Change Document. Where do you want to continue?",
    options: [
      { label: "Proceed to Level 2 (Design)", description: "Analyze design specs", recommended: true },
      { label: "Revise Level 1", description: "Go back and revise requirements" },
      { label: "Pause here", description: "Save progress and continue later" }
    ]
  }]
})
```

### Approval with Alternatives

```
ask_questions({
  questions: [{
    header: "Approval",
    question: "Release notes preview ready. How do you want to proceed?",
    options: [
      { label: "Approve and proceed", description: "Continue with release", recommended: true },
      { label: "Edit manually", description: "I'll make changes first" },
      { label: "Cancel release", description: "Abort the release process" }
    ]
  }]
})
```

### Decision with Free-form Input

```
ask_questions({
  questions: [{
    header: "Approach",
    question: "How should we handle the conflict between REQ_A and REQ_B?",
    allowFreeformInput: true,
    options: [
      { label: "Keep REQ_A", description: "Remove REQ_B as redundant" },
      { label: "Keep REQ_B", description: "Remove REQ_A as superseded" },
      { label: "Merge both", description: "Combine into a single requirement" }
    ]
  }]
})
```

### File Conflict (Setup Agent)

```
ask_questions({
  questions: [{
    header: "File Merge",
    question: "syspilot.change.agent.md has been modified. How do you want to handle this?",
    options: [
      { label: "Overwrite", description: "Replace with new syspilot version (lose your changes)" },
      { label: "Keep", description: "Keep your version (may miss new features)" },
      { label: "Show diff", description: "See complete comparison before deciding" }
    ]
  }]
})
```
