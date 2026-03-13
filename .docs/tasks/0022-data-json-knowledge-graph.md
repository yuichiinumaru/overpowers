# 022-task-json-knowledge-graph

> **Status**: APPROVED
> **Type**: task

## Objective
Convert the historical markdown-based knowledge graph (`SYSTEM_KNOWLEDGE_GRAPH.md`) and architectural digest (`JULES_ARCHITECTURAL_DIGEST.md`) into a structured JSON or JSONL format.

## Background
The previous text-based files have been moved to `.archive/docs/`. They should serve as the source material for the new JSON implementation. This will allow agents to parse relationships and nodes more definitively.

## Exit Conditions
- [ ] Parse information from `.archive/docs/SYSTEM_KNOWLEDGE_GRAPH.md`
- [ ] Parse information from `.archive/docs/JULES_ARCHITECTURAL_DIGEST.md`
- [ ] Create a new JSON/JSONL representation of the knowledge graph
- [ ] Place the new structured data in the appropriate directory (e.g., `.agents/` or `docs/knowledge/`)
- [ ] Mark this task as complete in `docs/tasklist.md`
