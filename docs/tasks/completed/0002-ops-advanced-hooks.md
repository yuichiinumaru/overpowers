# Task: 002-feature-advanced-hooks

## Objective

Implement advanced hook patterns described in the planning phase to add richer automation triggers.

## Test Requirements

Hooks must execute without errors in both OpenCode and Gemini CLI environments.

## Exit Conditions (GDD/TDD)

- [x] Review `docs/tasks/ planning/0023-ops-advanced-hooks-feature-plan.md` for requirements.
- [x] Implement or scaffold the proposed hooks.
- [x] Verify hooks fire correctly in at least one platform.

## Progress (Session 2026-03-04)
- Enhanced `todo_enforcer.py` to check both `tasklist.md` and `continuity.md`.
- Enhanced `dir_injector.py` to find root `AGENTS.md` and be selective with local context.
- Enhanced `edit_guard.py` with specific recovery hints for common tool errors.


## Details

### What

Create new hook scripts or enhance existing ones based on the advanced patterns planned.

### Where

`hooks/` directory and related documentation in `docs/hooks-guide.md`.

### How

Follow existing hook conventions in `hooks/` and reference `docs/hooks-guide.md`.

### Why

Advanced hooks will reduce manual steps and improve the developer experience for power users.
