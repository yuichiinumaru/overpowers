# Task 0037: MCP Documentation Ingestion Workflow

**Status**: [x]
**Priority**: MEDIUM
**Type**: ops

## Objective
Create workflows to ingest and map comprehensive library/framework documentation into our memory systems.

## Subtasks (mandatory):
- [x] Build a workflow script that goes to a documentation site (e.g., Agno, SurrealDB) and fetches all page links.
- [x] Deduplicate links.
- [x] Create a NotebookLM notebook for the framework and upload links as sources.
- [x] Handle 200+ link cases by downloading to `.md` files, grouping them, and uploading groups.
- [x] Evaluate whether Serena, Memcord or NotebookLM performs best for documentation contexts.
