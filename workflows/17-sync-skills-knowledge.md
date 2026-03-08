---
name: sync-skills-knowledge
description: Workflow to synchronize skill metadata into a structured JSON knowledge base and update active memory MCPs.
version: 1.0.0
author: System
---

# Sync Skills Knowledge Workflow

This workflow executes the skills parsing script to map out all discovered skills and generate structured JSON files for knowledge base consumption. It also ensures the active memory MCPs are instructed to ingest the updated information.

## Execution Requirements

- Python 3 with the `pyyaml` library installed.
- Access to the `skills/` directory and `.agents/knowledge/` and `docs/architecture/codemaps/` directories.

## Workflow Steps

### Step 1: Execute Parsing Script
Run the canonical skill mapping script to parse all `SKILL.md` frontmatter and extract metadata.

```bash
python3 scripts/parse-skills.py
```
*Expected Output*: "Successfully mapped N skills." and confirmations of saved JSON files.

### Step 2: Verify JSON Generation
Ensure that the mapping files were created successfully and contain valid JSON arrays.

```bash
ls -l docs/architecture/codemaps/003-arch-skills-map.json
ls -l .agents/knowledge/kb_skills_mapping.json
```

### Step 3: Trigger Knowledge Ingestion
Instruct tools (memcord, serena) to absorb the newly generated knowledge base mapping.

1. **Memcord Update**: Prompt the memcord tool to read `.agents/knowledge/kb_skills_mapping.json` and index the available skills for improved discovery.
2. **Serena Refresh**: Issue a command to serena to refresh its knowledge index referencing `docs/architecture/codemaps/003-arch-skills-map.json` to enable better context when analyzing skill utilization.

> **Note to Agents executing this workflow:** Ensure you use the appropriate available memory tools or context-injection methods to reload the `.agents/knowledge/` directory after running this workflow.
