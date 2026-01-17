---
name: jules-dispatch
description: Use when you need to prepare and dispatch tasks to Jules (Google's async AI coding agent)
---

# Jules Dispatch

Prepare optimized task prompts and dispatch work to Jules for parallel cloud execution.

**Core principle:** Jules works best with modular, isolated tasks that don't require integration. Prepare prompts that maximize success rate and minimize manual cleanup.

## When to Use

```dot
digraph when_to_use {
    "Task parallelizable?" [shape=diamond];
    "Needs cloud compute?" [shape=diamond];
    "Can be modular?" [shape=diamond];
    "jules-dispatch" [shape=box style=filled fillcolor=lightgreen];
    "Use local agents instead" [shape=box];
    "Break down first" [shape=box];

    "Task parallelizable?" -> "Needs cloud compute?" [label="yes"];
    "Task parallelizable?" -> "Use local agents instead" [label="no"];
    "Needs cloud compute?" -> "Can be modular?" [label="yes"];
    "Needs cloud compute?" -> "Use local agents instead" [label="no - local is fine"];
    "Can be modular?" -> "jules-dispatch" [label="yes"];
    "Can be modular?" -> "Break down first" [label="no"];
}
```

**Ideal for:**
- Research and analysis tasks (compare repos, analyze patterns)
- Documentation generation (forge methodology, technical docs)
- Exploratory coding (prototypes, POCs, experiments)
- Test generation for existing code
- Refactoring proposals (modular, isolated)

**Avoid for:**
- Tightly integrated changes (needs local context)
- Real-time collaboration (async by nature)
- Quick fixes (overhead not worth it)

## The Process

```dot
digraph process {
    rankdir=TB;
    
    "Analyze task requirements" [shape=box];
    "Generate Jules-optimized prompt" [shape=box];
    "Set constraints (modular, no integration)" [shape=box];
    "Create dispatch record (.jules/pending/)" [shape=box];
    "Dispatch via API or manual" [shape=diamond];
    "API: python runners/generic_swarm.py" [shape=box];
    "Manual: Copy prompt to jules.google.com" [shape=box];
    "Update dispatch record with session ID" [shape=box];
    
    "Analyze task requirements" -> "Generate Jules-optimized prompt";
    "Generate Jules-optimized prompt" -> "Set constraints (modular, no integration)";
    "Set constraints (modular, no integration)" -> "Create dispatch record (.jules/pending/)";
    "Create dispatch record (.jules/pending/)" -> "Dispatch via API or manual";
    "Dispatch via API or manual" -> "API: python runners/generic_swarm.py" [label="automated"];
    "Dispatch via API or manual" -> "Manual: Copy prompt to jules.google.com" [label="manual"];
    "API: python runners/generic_swarm.py" -> "Update dispatch record with session ID";
    "Manual: Copy prompt to jules.google.com" -> "Update dispatch record with session ID";
}
```

## Prompt Template

Use this template for Jules tasks:

```markdown
# Task: [TITLE]

## Context
[Brief project context - what repo, what stage, what matters]

## Objective
[Clear, specific objective]

## Constraints
- Write modular code that doesn't require integration
- Place output in a new directory: `jules-output/[task-name]/`
- Do NOT modify existing project files
- Include comprehensive README explaining your work
- Include tests for any code produced

## Deliverables
1. [Specific deliverable 1]
2. [Specific deliverable 2]
3. README.md explaining approach and usage
4. Tests (if applicable)

## Success Criteria
- [ ] Output is self-contained in jules-output/
- [ ] README explains what was done
- [ ] Code is clean and documented
- [ ] Tests pass (if applicable)
```

## Dispatch Record Format

Create `.jules/pending/{task-id}.json`:

```json
{
  "id": "2025-01-17-auth-research",
  "title": "Research OAuth2 patterns",
  "prompt_file": ".jules/prompts/2025-01-17-auth-research.md",
  "dispatched_at": "2025-01-17T14:30:00Z",
  "session_id": null,
  "status": "pending",
  "account": "account-1@gmail.com",
  "repo": "user/project",
  "branch_pattern": "jules/auth-research-*",
  "expected_completion": "2025-01-17T16:00:00Z",
  "tags": ["research", "auth", "security"]
}
```

## Account Rotation Strategy

With 6 Pro accounts (15 concurrent × 100 daily each):

```
Account 1: Tasks 1-100 (day quota)
Account 2: Tasks 101-200
...
Account 6: Tasks 501-600

Within each account:
- Max 15 concurrent tasks
- Round-robin for load balancing
```

Track in `.jules/accounts.json`:
```json
{
  "accounts": [
    {"email": "acc1@gmail.com", "daily_used": 45, "concurrent": 12},
    {"email": "acc2@gmail.com", "daily_used": 23, "concurrent": 8}
  ],
  "last_reset": "2025-01-17T00:00:00Z"
}
```

## Best Practices

**Do:**
- Be extremely specific about deliverables
- Set modular output constraints
- Include success criteria checklist
- Track all dispatches with metadata
- Batch related tasks to same account

**Don't:**
- Ask Jules to integrate with existing code
- Dispatch without tracking
- Exceed account limits
- Forget output location constraints

## Example Workflow

```
You: I want to dispatch OAuth research to Jules

[Read project context]
[Generate optimized prompt using template]
[Create .jules/pending/2025-01-17-oauth-research.json]
[Save prompt to .jules/prompts/2025-01-17-oauth-research.md]

Options:
1. Automated: python runners/generic_swarm.py --task-file .jules/prompts/...
2. Manual: Copy prompt, paste at jules.google.com, record session ID

[Update dispatch record with session ID]
[Set reminder for expected completion]

Done! Use jules-harvest when branches are ready.
```

## Integration

**Next skill:** Use `Overpowers:jules-harvest` when Jules completes work
**Tracking:** All dispatches recorded in `.jules/pending/`
**Cleanup:** Move to `.jules/completed/` after harvest
