---
name: jules-dispatch
description: Prepare and dispatch tasks to Jules via CLI login, manage account rotation, and run the 4-stage pipeline (Launch, Harvest, Audit, Apply)
tags:
- fleet
- jules
- automation
---

# Jules Dispatch

Prepare optimized task prompts and dispatch work to Jules for parallel cloud execution.

**Authentication method:** Login via `jules login` (CLI). API key is NOT supported.

**Core principle:** Jules works best with modular, isolated tasks that don't require integration. Prepare prompts that maximize success rate and minimize manual cleanup.

## When to Use

- Task is parallelizable and can run async in the cloud
- Work can be decomposed into modular, isolated units
- Research, documentation, test generation, refactoring proposals

**Avoid for:** tightly integrated changes, real-time collaboration, quick fixes.

## The 4-Stage Pipeline

> **MANDATORY:** Read `GUIDE.md` in this directory before executing ANY command.

1. **Launch**: `./scripts/jules-launcher-v2.sh <plan.json>` — dispatches tasks, logs to `.agents/jules_sessions.json`
2. **Harvest**: `python3 scripts/jules-harvester.py` — pulls `.diff` files into `.archive/harvest/jules/`, generates report
3. **Audit**: `python3 scripts/jules-auditor.py` — generates preview markdown of harvested diffs
4. **Apply**: `./scripts/jj-jules-apply.sh <SESSION_ID>` — safely applies chosen diff via Jujutsu

## Account Rotation

Jules Pro accounts are limited by Google: **15 concurrent tasks**, **100 tasks/day** per account.

The launcher dispatches 2 jobs per task (redundancy). So 7 user tasks = 14 jobs, approaching the limit.
After every 7 tasks, the launcher pauses for account rotation.

### Rotation Process

1. Run `jules login` in the terminal
2. Follow the browser link — the browser opens automatically
3. Select a fresh Google account that has not reached its quota
4. Resume — the launcher continues dispatching

## Prompt Template

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

## Critical Rules

### The Anti-Git Prompts Rule
**NEVER** mention `git`, `commit`, `push`, `branch`, or `checkout` in a Jules prompt.
Even negative instructions ('don't use git') cause the AI to attempt internal git manipulation,
resulting in the platform submitting an empty (+0/-0) PR.

### Branch Target Workaround
`jules remote new` CLI always targets the remote default branch.
**Workaround:** In the Jules Web UI, change the target branch dropdown to `staging` once.
The system saves it as default for all future CLI invocations.

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
  "repo": "user/project"
}
```

## Integration

- **Next skill:** Use `fleet/jules/harvest` when Jules completes work
- **Then:** Use `fleet/jules/triage` to analyze branches
- **Finally:** Use `fleet/jules/integrate` to selectively merge
