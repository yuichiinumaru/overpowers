---
title: "Inventory & Discoverability Enhancement"
status: open
priority: P1
type: ops
assignee: jules
created: 2026-03-15
---

# 0131 - Inventory & Discoverability Enhancement

## Objective
Improve asset discoverability across the Overpowers toolkit by enhancing inventory reports, integrating the skills graph builder into the install pipeline, and adding inventory references to `AGENTS.md`.

## Exit Conditions
- [ ] `generate-inventory.py` runs correctly and outputs to `.docs/inventory.md`
- [ ] `build_skill_graph.py` runs successfully (may need `kuzu` dependency handling)
- [ ] Install script calls `generate-inventory.py` after deploying to ALL platforms
- [ ] `AGENTS.md` references inventory and graph files for agent consultation
- [ ] Inventory sections exist in `.docs/` for: agents, skills, hooks, scripts, workflows
- [ ] Skills graph JSON export exists in `.agents/` (updated)

## Subtasks

### 1. Validate & Run Inventory Generator
- Run `uv run scripts/generators/generate-inventory.py` to regenerate `.docs/inventory.md`
- Verify output is correct and includes all component types
- Fix any remaining issues in the generator

### 2. Integrate Graph Builder
- Review `scripts/knowledge/build_skill_graph.py` — it uses `kuzu` (graph DB)
- Ensure it can be run via `uv run` (add `kuzu` as inline deps)
- Verify graph output in `.agents/skills_graph`
- Consider adding a JSON export for easier consultation

### 3. Install Pipeline Integration
- Add both `generate-inventory.py` and `build_skill_graph.py` calls to `install.sh` (Phase 2 or new Phase)
- Ensure they run after ALL platform deploys to capture the full picture
- Make them non-blocking (continue on error)

### 4. AGENTS.md References
- Add a "Toolkit Discovery" section to `AGENTS.md` pointing agents to:
  - `.docs/inventory.md` for a quick lookup
  - `.agents/skills_graph` for semantic skill queries
  - `scripts/generators/generate-inventory.py` for manual refresh

## Context
- The `generate-inventory.py` path was already fixed (was hardcoded to old OpenCode path).
- The `build_skill_graph.py` uses Kùzu graph DB, which may need special dependency handling.
- The user's pain point: too many skills/tools to remember what's already available.

**Author**: Antigravity Agent
