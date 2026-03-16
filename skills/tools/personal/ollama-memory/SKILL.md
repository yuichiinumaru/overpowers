---
name: ollama-memory
description: "|"
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'memory', 'knowledge']
    version: "1.0.0"
---

# Local Vector Memory System

This is an AI assistant memory system with local vector search, implemented using Markdown files + SQLite.

## Directory Structure

```
~/.openclaw/workspace/
├── memory/
│   └── YYYY-MM-DD.md      # Daily records
├── MEMORY.md               # Long-term memory (core cognition)
├── SOUL.md                 # AI personality definition
├── USER.md                 # User information
├── AGENTS.md               # Work specifications
└── scripts/memory-system/  # Memory system scripts
```

## Core Files

### 1. memory/YYYY-MM-DD.md - Daily Records

Records what happened today during each session:

```markdown
# 2026-03-09

## Session 1
- Topic: xxx
- Key Decisions: xxx
- To-dos: xxx

## Session 2
- ...
```

### 2. MEMORY.md - Long-Term Memory

Core cognition and important information, including:
- Core work principles
- User preferences
- Key lessons learned
- Prohibitions
- Habits

## Vector Search

Implements vector semantic search using local Ollama + `nomic-embed-text` model.

### Installing Ollama and Model

```bash
# Install Ollama
brew install ollama

# Start the service
ollama serve

# Download the embedding model
ollama pull nomic-embed-text
```

### Search Commands

```bash
# Search using Python script (recommended)
python3 ~/.openclaw/workspace/scripts/memory-system/context-memory.py search "keywords"

# Simple search
python3 ~/.openclaw/workspace/scripts/memory-system/memory-py.py search "keywords"
```

## Session Startup Flow

When a new session begins:

1. Read `SOUL.md` — AI personality
2. Read `USER.md` — User information
3. Read `memory/YYYY-MM-DD.md` (today + yesterday)
4. **Main Session**: Read `MEMORY.md`
5. Check the `knowledge/` directory

## Saving Memories

When the user says "Remember...":
- Update the record in `memory/YYYY-MM-DD.md`
- Synchronize important content to `MEMORY.md`
- Optional: Store in the vector database

```bash
# Add memory (with importance score)
python3 ~/.openclaw/workspace/scripts/memory-system/context-memory.py add "content" 8

# Add tags
python3 ~/.openclaw/workspace/scripts/memory-system/memory-py.py add "content" "tag1,tag2"
```

## Update Rules

### Files to Be Updated

1. **memory/YYYY-MM-DD.md** - Every session
2. **MEMORY.md** - New lessons/important information
3. **SOUL.md** - Personality changes
4. **USER.md** - User preference changes

### When to Update

- Upon task completion
- Significant discoveries or lessons learned
- Changes in user preferences
- Learning new skills

## Security Rules

- ❌ **Do not expose user personal information**
- ❌ Do not include real names/accounts/passwords in skill outputs
- ❌ Do not mention user privacy in public
- ✅ Read MEMORY.md only when necessary
- ✅ Load MEMORY.md only during the main session

## Configuration Example

Add in AGENTS.md:

```markdown
## Memory

### Daily Records (memory/YYYY-MM-DD.md)
- Record key content for each session
- Format: ## Session X / ### Topic / Decisions / To-dos

### Long-Term Memory (MEMORY.md)
- Core principles and preferences
- Important lessons
- Prohibitions
- Loaded only during the main session

### Vector Search
- Model: Ollama + nomic-embed-text
- Script: context-memory.py
```

## Advantages

| Feature | Description |
|------|------|
| Local Vectors | No API fees, available offline |
| Semantic Search | Understands similar meanings, not just keywords |
| Readable | Markdown can be directly edited by humans |
| Portable | Migrate by simply copying files |
| Secure | Stored locally, not uploaded to the cloud |

## Dependencies

- **Ollama**: Local LLM runtime
- **nomic-embed-text**: Local embedding model (274MB)
- **Python 3**: For running scripts
- **SQLite**: Vector storage

## Quick Start

```bash
# 1. Install Ollama
brew install ollama

# 2. Start and download model
ollama serve
ollama pull nomic-embed-text

# 3. Initialize database
python3 ~/.openclaw/workspace/scripts/memory-system/context-memory.py init

# 4. Add memory
python3 ~/.openclaw/workspace/scripts/memory-system/context-memory.py add "User prefers using Gemini" 8

# 5. Search memory
python3 ~/.openclaw/workspace/scripts/memory-system/context-memory.py search "model preference"
```
