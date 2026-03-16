---
name: siyuan-skill
description: "Siyuan Notes command-line tool, providing convenient command-line operations, supporting notebook management, document operations, content search, and other functions."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Core Values

**Provide a skill solution for AI Agents to quickly access Siyuan Notes**
**Offer a unified, structured, and searchable knowledge base for AI Agent teams**

## Applicable Scenarios
✅ Team standards, project knowledge, reusable skills
✅ Knowledge that needs to be shared by multiple agents
✅ Content requiring long-term storage and retrieval

## Inapplicable Scenarios
❌ Daily interaction logs, personal learning reflections
❌ Temporary notes, code version management
❌ Real-time collaborative editing

## Key Principles
- **Siyuan Notes** = Shared Knowledge Base
- **memory file** = Private Record
- **MEMORY.md** = Long-term Memory

---

# Important Constraints

**Must use CLI commands to operate Siyuan Notes**
**Do not automatically modify configuration files or environment variables related to this skill**
**Do not call the API directly**
**Do not use scripts to call or reference index.js**
**Do not use scripts to call or reference instruction files**

---

# Quick Start

## Usage

```bash
# Method 1: Run within the skill directory
cd <skills-directory>/siyuan-skill
node siyuan.js <command>

# Method 2: Global installation using npm link (recommended)
npm link -g
siyuan <command>

# Method 3: Run by specifying the path directly
node <skills-directory>/siyuan-skill/siyuan.js <command>
```

## View Help

```bash
# View all available commands
siyuan help

# View detailed help for a specific command
siyuan help search
siyuan help create
```

---

# Command List

Use `siyuan help` to view all available commands and detailed descriptions.

**Common Commands**:
- `nb` - Get notebook list
- `new` - Create document
- `edit` - Update document
- `rm` - Delete document
- `find` - Search content (supports vector search)
- `mv` - Move document
- `path` - Convert ID and path
- `index` - Index documents to vector database
- `nlp` - NLP text analysis

Detailed command documentation can be found in the [doc/commands/](doc/commands/) directory.

---

# Configuration

## Environment Variables (Highest Priority)

```bash
export SIYUAN_BASE_URL="http://127.0.0.1:6806"
export SIYUAN_TOKEN="your-api-token"
export SIYUAN_DEFAULT_NOTEBOOK="your-notebook-id"
export SIYUAN_PERMISSION_MODE="all"
export SIYUAN_NOTEBOOK_LIST="notebook-id1,notebook-id2"
```

## Configuration File

Edit the `config.json` file:

```json
{
  "baseURL": "http://127.0.0.1:6806",
  "token": "your-api-token",
  "defaultNotebook": "your-notebook-id",
  "permissionMode": "all"
}
```

**Get Configuration Information**:
1. Open Siyuan Notes → Settings → About → Copy API Token
2. Use `siyuan notebooks` to get notebook IDs

---

# Notes

1. **First-time use** requires configuring the Siyuan Notes API address and Token.
2. **Permission Mode**: `all` (unrestricted) / `whitelist` / `blacklist`.
3. **Caching Mechanism**: Notebook lists and document structures are automatically cached. Use `--force-refresh` to force a refresh.
4. **Vector Search**: Requires separate deployment of Qdrant and Ollama services. Otherwise, it will fall back to SQL search.
5. **Incremental Indexing**: The `index` command enables incremental indexing by default, only indexing changed documents. Use `--force` to rebuild, or `--no-incremental` to disable incremental indexing.

---

# Reference Documentation

- [Siyuan Notes API Documentation](https://github.com/siyuan-note/siyuan/blob/master/API_zh_CN.md) - Official API reference documentation
- [Siyuan Notes User Guide](https://github.com/siyuan-note/siyuan/blob/master/README_zh_CN.md) - Official user guide
