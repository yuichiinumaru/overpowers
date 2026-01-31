# Raw Analysis Notes - Antigravity Extraction

## Target Repositories
1. `antigravity-skills`: **High Value**. Contains 20 unique skills not present in Overpowers.
2. `andy-universal-agent-rules`: **Medium Value**. Contains Python scripts for knowledge management (`save-knowledge.py`, etc.).
3. `sanity-gravity`: **Low Priority**. Container/Sandbox tools.
4. `AntigravityManager` & `antigravity-account-switcher`: **Low Priority**. Electron Apps.
5. `ellfarnaz-antigravity-agent-os`: **Low Priority**. Placeholder/Docs.

## Unique Skills Identified
The following 20 skills are unique to `antigravity-skills` and should be extracted:
1. `advanced-evaluation`
2. `bdi-mental-states`
3. `context-compression`
4. `context-degradation`
5. `context-fundamentals`
6. `context-optimization`
7. `evaluation`
8. `filesystem-context`
9. `hosted-agents`
10. `json-canvas`
11. `memory-systems`
12. `multi-agent-patterns`
13. `notebooklm`
14. `obsidian-bases`
15. `obsidian-markdown`
16. `planning-with-files`
17. `project-development`
18. `remotion`
19. `tool-design`
20. `using-superpowers`

## Knowledge Scripts Identified
Found in `andy-universal-agent-rules/.agent/scripts/`:
- `backup-memory.py`
- `search-knowledge.py`
- `save-knowledge.py`
- `validate-index.py`
- `detect-environment.py`

## Strategy
- **Skills**: Copy unique skills to `skills/`. Rename `using-superpowers` to `using-overpowers` (if applicable) or adapt it.
- **Scripts**: Extract knowledge scripts to `scripts/knowledge/` and create wrappers or aliases if needed.
