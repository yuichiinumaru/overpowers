# Task: Skill Redundancy Consolidation

## Objective
Identify and merge redundant skills to reduce technical debt and simplify the toolkit.

## Test Requirements
- [x] List of redundant skills identified in `.agents/thoughts/consolidation_plan.json`.
- [x] Consolidated skills verified to contain all relevant functionality from merged counterparts.

## Exit Conditions (GDD/TDD)
- [x] Duplicate Mermaid, news, and search skills merged (archived).
- [x] Deprecated skill folders moved to `.archive/skills/`.
- [x] `Related Skills` links concept established.

## Details

### What
Manual and semi-automated review of skills with overlapping functionality.

Subtasks:
- [x] Group skills by name and description similarity.
- [x] Review Mermaid diagramming skills.
- [x] Review news aggregation skills.
- [x] Review generic search skills.
- [x] Perform merge/archive operations.

### Where
- `skills/` directory.

### How
Comparative analysis followed by manual consolidation of instructions and tools into a single 'master' skill per category.

### Why
Redundancy increases maintenance overhead and leads to agent confusion when multiple similar options are available.
