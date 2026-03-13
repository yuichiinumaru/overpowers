# Task: Skill Knowledge Base Mapping System

## Objective

Create a systematic knowledge base for the project's agent skills by parsing metadata and generating structured mapping files, paired with a reliable workflow to propagate this knowledge to active memory MCPs.

## Test Requirements

- The `parse-skills.js` script correctly traverses all skills inside `skills/` and creates maps retaining name, directory, and short descriptions extracted from `SKILL.md` frontmatter or content.
- Generates `docs/architecture/codemaps/003-arch-skills-map.json` and `.agents/knowledge/kb_skills_mapping.json`.
- The workflow correctly triggers the script and specifies instructions for tools (memcord, serena) to ingest the knowledge base folder into memory.

## Exit Conditions (GDD/TDD)

- [x] Script created successfully.
- [x] Script tested against `skills/` without errors.
- [x] Workflow created securely.

## Details

### What

- We have over 1200+ skills discovered and properly organizing this knowledge is necessary. We need to create a canonical script to generate and organize our knowledge base map of all skills to make discovery easier.

Subtasks:
- [x] Write `scripts/parse-skills.js` (or python equivalent) that reads `skills/*/SKILL.md`.
- [x] Save mapping to `docs/architecture/codemaps/003-arch-skills-map.json` and `.agents/knowledge/kb_skills_mapping.json`.
- [x] Write `workflows/17-sync-skills-knowledge.md` to run the mapping script and synchronize the changes to memory MCPs natively.

### Where

- `scripts/parse-skills.js` (or `.py`)
- `workflows/17-sync-skills-knowledge.md`

### How

- Parse YAML frontmatter or first descriptive line from each `SKILL.md` to extract information.
- Format it into a JSON dictionary/array and output.
- Workflow will wrap this execution and invoke memcord/serena tools to absorb `.agents/knowledge/`.

### Why

- Enables LLMs and humans to discover, triage, and map new agent skills dynamically instead of relying strictly on context window searching or local memories that get lost.
