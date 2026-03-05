---
name: 024-plan-advanced-hooks-implementation
status: proposed
priority: high
source: .archive/docs/tasks/planning/advanced-hooks.md
---

# Plan: Advanced Hooks Implementation

## Objective
Implement intelligent runtime hooks to enhance agent reliability and context awareness, porting logic from the `oh-my-opencode` research.

## Proposed Tasks
1. [ ] **Todo Continuation Enforcer**: Create a hook that monitors `session.idle` and re-prompts if `ctx.client.session.todo` is not empty.
2. [ ] **Directory Context Injector**: Implement a hook that detects directory changes and automatically reads/injects the local `README.md` or `AGENTS.md`.
3. [ ] **Edit Error Auto-Recovery**: Develop a middleware for the `edit` tool that catches common failures (indentation, line bounds) and provides specific "Hints" for agent self-correction.

## Reference
See original blueprint in `.archive/docs/tasks/planning/advanced-hooks.md`.
