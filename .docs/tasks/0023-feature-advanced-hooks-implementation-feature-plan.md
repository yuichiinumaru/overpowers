# Feature Plan: Advanced Hooks Implementation

## 1. Overview
Implement a suite of intelligent runtime hooks to enhance agent reliability, ensure task completion, and provide automated context enrichment. These hooks are ported and adapted from the `oh-my-opencode` research.

## 2. Goals & Success Criteria
- **Goal:** Improve agent autonomy and context awareness during long sessions.
- **Success Criteria:**
  - Agent automatically continues working if pending tasks are found in `docs/tasklist.md` or `.agents/continuity-*.md`.
  - Local `README.md` and `AGENTS.md` context is automatically injected when the agent moves between directories.
  - Common tool failures (like indentation or match errors) provide actionable hints instead of generic error messages.

## 3. Vertical Slices & Milestones

### Slice 1: Script Validation & Standardization
- **Objective:** Ensure `todo_enforcer.py`, `dir_injector.py`, and `edit_guard.py` are robust and handle edge cases.
- **Deliverables:** Verified Python scripts in `hooks/runtime/`.

### Slice 2: Hook Metadata Definition
- **Objective:** Create/Update `.md` files in `hooks/` with correct triggers and matchers for Gemini CLI and OpenCode.
- **Deliverables:** `todo-enforcer.md`, `dir-injector.md`, `edit-guard.md`.

### Slice 3: Platform Integration
- **Objective:** Register the hooks in `hooks/hooks.json` so they are active in Gemini CLI.
- **Deliverables:** Updated `hooks/hooks.json`.

## 4. Risks & Mitigations
- **Infinite Loops:** The Todo Enforcer might re-prompt the agent too aggressively. -> **Mitigation:** Limit re-prompts or add a manual override.
- **Context Bloat:** Dir Injector might inject too much text if `AGENTS.md` is large. -> **Mitigation:** Truncate or summarize the injected content (implemented in `dir_injector.py`).
- **Tool Performance:** Hooks running on every tool use might slow down the experience. -> **Mitigation:** Use efficient matchers to only run hooks when relevant.

## 5. Exit Conditions
- [x] Hooks are successfully registered in `hooks/hooks.json`.
- [x] Manual verification confirms hooks trigger on relevant events.
- [x] Documentation in `.docs/hooks-guide.md` is updated.
