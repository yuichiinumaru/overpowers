# Future Integration: MCP Tools (Oh My OpenCode)

**Source**: `references/oh-my-opencode/src/mcp/`

## 1. grep.app (Code Search)
**Purpose**: Fast regex search across all public GitHub repositories.
**Usage**: Essential for `librarian-researcher` to find usage examples.

### Configuration (MCP)
```json
{
  "grep_app": {
    "type": "remote",
    "url": "https://mcp.grep.app",
    "enabled": true,
    "oauth": false
  }
}
```

## 2. Context7 (Doc Search)
**Purpose**: RAG (Retrieval Augmented Generation) over official documentation.
**Usage**: `librarian-researcher` uses this to read docs like "React", "Next.js", etc.

### Configuration (MCP)
```json
{
  "context7": {
    "type": "remote",
    "url": "https://context7.io/mcp",
    "enabled": true
  }
}
```

## 3. Web Search
**Purpose**: General web access for agents.
**Source**: `websearch.ts`

### Logic
*   Uses Exa (formerly Metaphor) or Google Search API.
*   Provides `web_search` and `web_fetch` tools.
*   Agents use this to verify facts or find new libraries.
