# Task: Implement Local Knowledge MCP Server

## Objective

Create a local MCP server (`knowledge-mcp`) within the `services/` directory to expose the Cognitive Fusion Architecture (CFA) Knowledge Base files located in `.agents/knowledge/`. This enables agents to query and update operational rules using "Progressive Disclosure", saving context window while retaining access to the full neuro-symbolic governance cluster.

## Test Requirements

- The MCP server must successfully start and register its tools.
- `list_cfa_knowledge` must return the list of available JSON files in `.agents/knowledge/` without returning their full contents.
- `get_cfa_knowledge` must return the exact JSON content of a requested KB file.
- `create_cfa_knowledge` and `update_cfa_knowledge` must function correctly and enforce loading of all existing KBs prior to execution (or require them in the context).

## Exit Conditions (GDD/TDD)

- [ ] `services/knowledge-mcp/` directory created with a valid initialized project (TypeScript or Python).
- [ ] Tools `list_cfa_knowledge`, `get_cfa_knowledge`, `create_cfa_knowledge`, and `update_cfa_knowledge` implemented.
- [ ] Safe read/write operations mapping explicitly to `.agents/knowledge/`.
- [ ] Instructions injected into the server explicitly telling the LLM that `create` and `update` require loading the full KB stack into context to operate as a "Synergy CFA Agent Full Power".
- [ ] MCP is added to the `opencode-example.json` under `mcpServers`.

## Details

### What

Implement a robust, lightweight MCP server to bridge the file system rules with agent tools. 

Subtasks:
- [ ] Scaffold the MCP server in `services/knowledge-mcp`.
- [ ] Implement `list_cfa_knowledge()` to return filenames and summaries (from metadata if needed) of `.agents/knowledge/*.json`.
- [ ] Implement `get_cfa_knowledge(kb_id)` to load specific rules into context.
- [ ] Implement `create_cfa_knowledge(filename, data)` and `update_cfa_knowledge(filename, data)`. These tools' descriptions **must explicitly enforce** that the agent must load all existing rules into its context *before* invoking this tool, to ensure holistic architectural harmony.

### Where

- `services/knowledge-mcp/`
- `opencode-example.json` (to register the server)

### How

Use either Python (`mcp` / `fastmcp`) or TypeScript (`@modelcontextprotocol/sdk`). Python might be faster to prototype, but follow the repository's dominant backend language for services if one exists. 
Ensure path resolution safely targets the root `.agents/knowledge/` folder.
Make sure the tool descriptions explicitly declare the requirement of loading the full KB context for mutations.

### Why

JSON KBs are token-heavy if pre-loaded into every prompt. Exposing them via MCP allows agents to dynamically pull only the operational rules they need for the current workflow stage (routing, reasoning, validation). Providing `create` and `update` tools ensures the system can autonomously evolve its own ruleset when operating at high cognitive capacity.
