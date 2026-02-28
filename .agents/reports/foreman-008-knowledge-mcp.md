# Foreman Run: 008-feature-knowledge-mcp

## Sync & Select
- Task selected: 008-feature-knowledge-mcp
- Branch created: foreman-008-knowledge-mcp
- Objective: Create an MCP server for the knowledge base.

## Discover
- The repository has a `docs/` directory containing knowledge files.
- The task requires an MCP server to read, list, and search these files.
- The project has python and javascript roots.
- I will implement the MCP server using Node.js and the official `@modelcontextprotocol/sdk`, inside a new `packages/knowledge-mcp` folder.

## Execute
- [x] Create Node.js package in `packages/knowledge-mcp`.
- [x] Add dependencies (`@modelcontextprotocol/sdk`, `zod`, TypeScript tools).
- [x] Write the server script (`src/index.ts`) to expose `list_knowledge_files`, `read_knowledge_file`, `search_knowledge`.
- [x] Implement path security checks to prevent traversing outside the `docs/` dir.
- [x] Build script (`pnpm build`).
- [x] Create a run script or instructions (Added `README.md`).

## Verify & Review
- [x] Build passes (`tsc`).
- [x] The stdio server starts correctly and waits for stdin.
- [x] Path resolution correctly identifies `../../../docs` from `dist/index.js`.

## Deliver
- [x] Marked task as done in `docs/tasks/008-feature-knowledge-mcp.md`.
- [ ] Push branch and prepare PR.

