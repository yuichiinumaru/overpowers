# Extraction Master Plan: Legacy Code Assimilation

**Target**: Assimilate valuable capabilities from `antigravity-skills` and `andy-universal-agent-rules` into `Overpowers`.

## 1. Skills Assimilation
**Strategy**: Direct copy with potential naming adaptation if needed.
**Source**: `references/external_source/antigravity-skills/skills/`
**Target**: `skills/`

| Skill Name | Action | Notes |
|------------|--------|-------|
| `advanced-evaluation` | Copy | New evaluation logic. |
| `bdi-mental-states` | Copy | BDI architecture support. |
| `context-compression` | Copy | Advanced context management. |
| `context-degradation` | Copy | Simulation of context loss. |
| `context-fundamentals` | Copy | Core context libs. |
| `context-optimization` | Copy | Optimization algorithms. |
| `evaluation` | Copy | General evaluation. |
| `filesystem-context` | Copy | Context derived from FS. |
| `hosted-agents` | Copy | Remote agent patterns. |
| `json-canvas` | Copy | Obsidian Canvas support. |
| `memory-systems` | Copy | Advanced memory patterns. |
| `multi-agent-patterns` | Copy | Swarm patterns. |
| `notebooklm` | Copy | NotebookLM integration. |
| `obsidian-bases` | Copy | Obsidian base config. |
| `obsidian-markdown` | Copy | Obsidian MD flavor. |
| `planning-with-files` | Copy | File-based planning (Micode style). |
| `project-development` | Copy | Project lifecycle. |
| `remotion` | Copy | Video generation support. |
| `tool-design` | Copy | Tool building patterns. |

**Exclusions**:
- `using-superpowers` (Redundant with `using-overpowers`).

## 2. Knowledge Scripts Assimilation
**Strategy**: Extract Python scripts into `scripts/knowledge/`.
**Source**: `references/external_source/andy-universal-agent-rules/.agent/scripts/`
**Target**: `scripts/knowledge/`

| Script Name | Action | Notes |
|-------------|--------|-------|
| `save-knowledge.py` | Copy | Core knowledge saving. |
| `search-knowledge.py` | Copy | Knowledge retrieval. |
| `validate-index.py` | Copy | Index maintenance. |
| `backup-memory.py` | Copy | Memory backup. |
| `detect-environment.py` | Copy | Env detection. |

## 3. Execution Steps
1. Create `scripts/knowledge/` directory.
2. Copy all selected skills recursively.
3. Copy all selected scripts.
4. Verify file permissions (chmod +x for scripts).
5. Update `skills/checklist.md` (if exists) or generate a new inventory.

## 4. Dependencies
- No new external pip packages required (Standard library only).
