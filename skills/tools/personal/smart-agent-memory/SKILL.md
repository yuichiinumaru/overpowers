---
name: ops-memory-smart-agent-memory
version: 2.0.0
description: Advanced cross-platform long-term memory system for agents. Features layered context delivery, temperature modeling, skill experience tracking, structured storage (Markdown/JSON/SQLite), and automated archiving. Optimized for context efficiency and token savings.
tags: [memory, agent-memory, long-term-storage, context-management, knowledge-base]
category: ops
---

# Smart Agent Memory 🧠 v2.0

**Cross-Platform Long-Term Memory System** — Layered context delivery + Skill experience memory + Temperature model + Automatic archiving.

## ⚡ Core Principles: Layered Loading, On-Demand Delivery

> **Never load all memory at once!** Read the index first, then drill down as needed. This is key to saving tokens.

### Memory Usage Flow (Whenever memory is needed)

```
1. index    → Read concise index (overview, <500 tokens)
2. Judge    → Determine which memory parts are needed based on the current task
3. context  → Load specific context by tag/skill/time
4. Act      → Execute task based on loaded context
```

### Skill Experience Memory Flow (After tool invocation)

```
Tool call successful/encountered a pitfall → remember "Experience summary" --skill <skill-name>
Before calling this tool next time → skill-mem <skill-name> to load experience
```

## CLI Reference

```bash
CLI=~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js

# ★ Layered Context (Core, prioritize usage)
node $CLI index                              # Concise memory index (read this first!)
node $CLI context --tag <tag>                # Load context by tag
node $CLI context --skill <skill-name>       # Load experience + related facts by Skill
node $CLI context --days 7                   # Memory from the last N days
node $CLI context --entity-type person       # Load by entity type

# ★ Skill Experience Memory
node $CLI remember "The time parameter for this API must be in ISO format" --skill api-tool
node $CLI skill-mem <skill-name>             # Read experience for a specific Skill
node $CLI skill-list                         # List all Skills with experience memory

# Basic Memory Operations
node $CLI remember <content> [--tags t1,t2] [--skill name] [--source conversation]
node $CLI recall <query> [--limit 10]
node $CLI forget <id>
node $CLI facts [--tags t1] [--limit 50]

# Lessons and Entities
node $CLI learn --action "..." --context "..." --outcome positive --insight "..."
node $CLI lessons [--context topic]
node $CLI entity "Alex" person --attr role=CTO
node $CLI entities [--type person]

# ★ Conversation Lifecycle
node $CLI session-start                      # Conversation start: load memory overview + recent context
node $CLI session-end "Discussed XX, decided on YY"  # Conversation end: save session summary

# Maintenance
node $CLI gc [--days 30]                     # Archive cold data
node $CLI reflect                            # Nightly reflection
node $CLI stats                              # Memory health
node $CLI search <query>                     # Full-text search .md
node $CLI temperature                        # Temperature report
node $CLI extract <lesson-id> --skill-name x # Extract Skill
```

## Agent Behavioral Guidelines

### 🔄 Memory Recall

**All agents automatically search `memory/*.md` via `memory_search`.**
The dual-layer storage ensures that every write operation synchronously generates a Markdown file, so `memory_search` can naturally find all structured data.

When deeper dives into a specific direction are needed, use the CLI for drilling down:
```bash
node $CLI context --tag <tag>       # By tag
node $CLI context --skill <name>    # By Skill experience
node $CLI context --days 7          # By time
```

### 📝 Memory Writing

```bash
node $CLI remember "Key information" --tags tag1,tag2    # Facts
node $CLI learn --action "..." --context "..." --outcome positive --insight "..."  # Lessons
node $CLI session-end "Discussed XX, decided on YY"    # Session summary
```
> ⚠️ **Don't wait until the end!** Write content as it becomes available; it won't be lost if the process is interrupted.

### ✅ MUST DO
- **Every time historical information is needed**: First, run `index` to see the overview, then decide which part to load.
- **After encountering a pitfall during tool invocation**: `remember "Experience" --skill <name>` to consolidate the experience.
- **Before calling an unfamiliar tool**: `skill-mem <name>` to check if there's any historical experience.
- **When recording new information**: Apply appropriate tags for easy retrieval later.

### ❌ NEVER DO
- Do not load all facts at once with `facts --limit 999`.
- Do not load all memory in every conversation turn.
- Do not ignore `index` and directly use `recall`.

## Storage Layout

```
~/.openclaw/workspace/memory/
├── YYYY-MM-DD.md           ← Daily logs
├── skills/                 ← ★ Skill experience memory
│   ├── api-tool.md
│   └── deploy.md
├── lessons/                ← Lessons Markdown
├── decisions/              ← Decisions Markdown
├── people/                 ← People profiles
├── reflections/            ← Reflection records
├── .data/                  ← JSON structured data
├── .archive/               ← Archived cold data
└── .index.json             ← Temperature index + statistics
```

## Recommended Cron Jobs

### Nightly Reflection (Recommended)

```json
{
  "name": "memory-reflect",
  "schedule": { "kind": "cron", "expr": "45 23 * * *", "tz": "Asia/Shanghai" },
  "payload": {
    "kind": "agentTurn",
    "message": "Run memory reflection: node ~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js reflect, then summarize today's memory changes."
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```

### Weekly Sunday GC Archiving (Recommended)

```json
{
  "name": "memory-gc",
  "schedule": { "kind": "cron", "expr": "0 2 * * 0", "tz": "Asia/Shanghai" },
  "payload": {
    "kind": "agentTurn",
    "message": "Run memory GC: node ~/.openclaw/skills/smart-agent-memory/scripts/memory-cli.js gc --days 30, report how many memories were archived."
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```
