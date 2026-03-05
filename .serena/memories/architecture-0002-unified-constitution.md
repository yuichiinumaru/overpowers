# Unified Constitution Architectural Shift

Date: 2026-03-03

## Context
The repository suffered from rule fragmentation across `rules/*.md`, with procedural bloat for Jujutsu and Jules. A major architectural simplification was executed.

## Key Decisions
1. **Unification**: All scattered `rules/` moved to `.archive/` and synthesized into a single, massive `AGENTS.md` Root Constitution.
2. **Archive Protocol**: **NEVER DELETE** files. Deprecated code/rules explicitly move to `.archive/` to clear immediate context without losing history.
3. **Sculpting Philosophy**: Root constitutional rules favor *negative constraints* (e.g. Jules anti-git). Positive, step-by-step procedures (e.g., how to rotate Jules accounts or hierarchical `jj new` sprint branches) are pushed down to specific `skills/` or `workflows/`.
4. **Law of Shared Consciousness**: The `memory-sync-protocol` workflow was established to enforce syncing session epiphanies across Memcord, Serena, and `.agents/memories/` global files.
