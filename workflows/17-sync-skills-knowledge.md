---
description: Parses all existing skills into JSON codemaps and synchronizes the knowledge across project MCP memories.
---

This workflow generates a structured JSON knowledge base representing all available tools and skills in the repository, making them easily searchable and accessible for the agent without hallucination.

1. **Parse Skills using Node Script**
```bash
// turbo
node scripts/parse-skills.js
```

2. **Verify Output**
```bash
// turbo
ls -la docs/architecture/codemaps/003-arch-skills-map.json .agents/knowledge/kb_skills_mapping.json
```

3. **Update Agent Memories (Serena / Memcord)**
- **Memcord**: Ensure the current slot is `overpowers` (via `mcp_memcord_memcord_name` or `mcp_memcord_memcord_use`). Then, call `mcp_memcord_memcord_import` giving the source `.agents/knowledge/kb_skills_mapping.json` pointing to the `overpowers` slot.
- **Serena**: Call `mcp_serena_write_memory` for `memory_name` "knowledge/skills_map" with a short summary pointing to the new `.agents/knowledge/kb_skills_mapping.json` file, instructing agents to parse this file whenever they need to select specialized skills.

4. **Wrap-up**
Document execution and conclusion of this knowledge generation in `continuity.md` and check off related tasks if any.
