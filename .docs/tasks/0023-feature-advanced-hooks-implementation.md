# Task 0023: Advanced Hooks Implementation

**Status**: [x]
**Priority**: HIGH
**Type**: feature

## Objective
Implement intelligent runtime hooks to enhance agent reliability and context awareness, porting logic from the `oh-my-opencode` research.

## Sub-tasks
- [x] **Todo Continuation Enforcer**: Create a hook that monitors session state and re-prompts if pending tasks exist in `tasklist.md` or `continuity-*.md`.
- [x] **Directory Context Injector**: Implement a hook that detects directory changes and automatically reads/injects the local `README.md` or `AGENTS.md` into the system prompt.
- [x] **Edit Error Auto-Recovery**: Develop a middleware for the `edit` tool that catches common failures (indentation, line bounds) and provides specific "Hints" for agent self-correction.

## References
- Plan: `.docs/tasks/0023-feature-advanced-hooks-implementation-feature-plan.md`
- Design: `.docs/tasks/0023-feature-advanced-hooks-implementation-technical-design.md`
