# Knowledge MCP Server

This is a Model Context Protocol (MCP) server that provides access to the project's knowledge base (the `docs/` directory).

## Usage

### Using with an MCP Client

You can run this server using Node.js:

```bash
node /path/to/repo/packages/knowledge-mcp/dist/index.js
```

Or configure it in your MCP client settings (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "knowledge-mcp": {
      "command": "node",
      "args": ["/absolute/path/to/repo/packages/knowledge-mcp/dist/index.js"]
    }
  }
}
```

## Available Tools

- `read_knowledge_file`: Read the content of a specific file in the `docs/` folder.
- `search_knowledge`: Search for a specific string or pattern in the knowledge base.
- `list_knowledge_files`: List available files in a specific knowledge category.
