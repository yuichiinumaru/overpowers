## Pending Tasks (Priority Order)
1. **001** - Remote MCP integrations
2. **003** - Finalize persistent memory refactor
3. **Skill Naming Enforcement (Docs/Agents)** - Review and rename agent files in `agents/` and remaining documentation in `docs/` to strictly follow `type--` and `type-subtype-nnnn` conventions.
4. **Batch 040 Deployment** - Start Batch 040 (`sci-chem-0811` to `sci-chem-0830`).
5. **Deep Audit Phase 3** - Initiate Phase 3 of skill standardization.

## ✅ Completed Tasks (Session 2026-03-08)
- **GraphRAG Semantic Namespacing** - Initialized Kùzu database to extract concepts/tags from 1,277 skills. Used the graph to dynamically rename all skill folders to a `[domain]-[subdomain]-[slug]` pattern, eliminating arbitrary numbering.
- **Skill Conflict Resolution** - Resolved 731 skill name conflicts identified after Jujutsu merges. Archived redundant folders to `.archive/skills/`. Re-synchronized Gemini CLI environment.

