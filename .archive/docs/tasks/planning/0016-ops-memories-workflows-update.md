# Memory Workflows and Sanitization Updates

This document tracks immediate improvements to be made to our memory management logic across agents and workflows. 

## Proposed Changes

### 1. Workflow Memory Lifecycle Updates
- Update all existing workflows so that they explicitly instruct the agent to **read memory** at the beginning of the execution and **update memory** at the end.
- In memory-specific workflows (such as `11-sync-memory`), add a reinforced confirmation that they must strictly enforce the `AGENTS.md` memory rules (using the correct Memcord slot, and unifying Serena + NotebookLM context).

### 2. Memcord Sanitization Workflow
- Create a new workflow (e.g. `workflows/18-sanitize-memories.md`) that cleans up fragmented project memories.
- The process will be:
  1. Let the agent scan all available Memcord slots.
  2. Identify slots that belong to the current project but are scattered or misnamed.
  3. Aggregate all relative memory entries and ingest them sequentially into the official unified slot (e.g. `overpowers`).
  4. Finally, securely delete the deprecated and "dirty" slots to avoid future confusion.
