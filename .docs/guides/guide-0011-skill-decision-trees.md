# Guide 0011: Skill Decision Trees

## Overview
Skill Decision Trees are structured logic blocks (tables or lists) embedded in `SKILL.md` or `references/` files. They serve as "Expert Brains" that help the Agent navigate complex choices based on the model, the specific task, or the available context.

## Why Use Decision Trees?
- **Efficiency**: Prevents redundant tool calls and unnecessary research.
- **Accuracy**: Guides the agent to the most robust model for the task.
- **Consistency**: Ensures different agents (or the same agent in different sessions) follow the same expert heuristics.

## Standard Formats

### 1. The Decision Matrix (Table)
Recommended for 2-4 variables with distinct outcomes.

| If [Situation] | Then [Strategy/Tool] | Why? |
| :--- | :--- | :--- |
| Single-file, no dependencies | Direct Tool (`replace`) | Speed & Simplicity |
| Large-scale refactor (>5 files) | Planning Mode + Subagents | Reliability & Context |
| Unclear requirements | `ask_user` | Avoids wasted work |

### 2. The Logic Flow (Nested List)
Recommended for sequential checks or deep branching.

1.  **Check Context**:
    - If `AGENTS.md` is present → Follow established protocols.
    - If missing → `google_web_search` for common best practices.
2.  **Evaluate Fragility**:
    - If fragile (e.g., specific indentation) → Read surrounding lines first.
    - If robust → Proceed with surgical edits.

## Overpowers Model Heuristics

When designing decision trees, refer to this standard model roster:

| Tier | Model Alias | Best For |
| :--- | :--- | :--- |
| **Reasoning** | `DEEP_REASONING` / Opus / Reasoning Pro | Logic bugs, new architecture, exploits, complex refactors. |
| **Broad Context** | `BROAD_CONTEXT` / Gemini Pro | Planning across many files, reading large docs. |
| **Fast** | `FAST` / Flash / Haiku | Search, validation, boilerplate, quick edits. |
| **Creative** | `CREATIVE` / Sonnet | UI/UX, documentation, creative writing. |

## Progressive Disclosure
- **Keep it Lean**: If a tree is < 15 lines, keep it in `SKILL.md`.
- **Offload Details**: If a tree is complex, move it to `references/decision_trees.md` and link it with a **MANDATORY** trigger in the workflow.

## Best Practices
- **Imperative Language**: Use "Do", "Check", "Invoke".
- **Non-Obvious Reasoning**: Include the "Why" to help the agent understand the trade-off.
- **Failure Paths**: Always include what to do if the preferred path fails.
