---
name: elite-memory-skill
description: "Ultimate AI Memory System - WAL Protocol + Daily Memory + Long-Term Memory + GitHub Auto Sync + Lark Notification"
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'memory', 'knowledge']
    version: "1.0.0"
---

# Elite Memory - Ultimate AI Memory System

A complete memory management system for AI Agents, supporting a dual-layer memory architecture, automatic GitHub synchronization, and Feishu notifications.

## Core Features

### Dual-Layer Memory Architecture

```
Today's Conversation → memory/YYYY-MM-DD-temp.md (Temporary memory, real-time write)
              ↓
         Next Day 08:00
              ↓
    Analyze Temporary Memory → Extract Key Points
              ↓
    ┌───────────┴───────────┐
    ↓                       ↓
memory/YYYY-MM-DD.md   MEMORY.md
(Formal Diary)          (Long-term Memory Refinement)
```

### Automated Tasks

| Time           | Task                                 | Script                     |
|----------------|--------------------------------------|----------------------------|
| **Daily 23:55**| Git Sync to GitHub                   | `sync-memory-to-github.sh` |
| **Daily 08:00**| Read Yesterday's Memory + Create Today's Memory | `morning-memory-read.sh`   |
| **After Each Conversation** | Real-time write to temporary memory | Manually call `analyze-memory.sh` |

## Usage

### Initialize Memory System

```bash
# 1. Create memory directory
node scripts/init.mjs

# 2. Configure GitHub remote
gh repo create ai-memory --private
git remote add memory git@github.com:username/ai-memory.git

# 3. Configure Feishu Notification (Optional)
export FEISHU_USER_ID="ou_xxxxx"
```

### Memory Operations

```bash
# Analyze conversation and write to temporary memory
node scripts/analyze.mjs "Conversation content" --topic "Topic"

# Manually sync to GitHub
node scripts/sync.mjs

# View memory status
node scripts/status.mjs
```

### Scheduled Task Configuration

```bash
# Add to crontab
crontab -e

# Daily 23:55 sync
55 23 * * * ~/.openclaw/workspace/scripts/sync-memory-to-github.sh

# Daily 08:00 read
0 8 * * * ~/.openclaw/workspace/scripts/morning-memory-read.sh
```

## Memory File Structure

```
workspace/
├── MEMORY.md                      # Long-term memory (curated)
├── SESSION-STATE.md               # Session state
└── memory/
    ├── YYYY-MM-DD-temp.md         # Temporary memory (current day)
    ├── YYYY-MM-DD.md              # Formal memory (after archiving)
    ├── projects/
    │   └── [project-name].md      # Project memory
    ├── skills/
    │   └── [skill-name].md        # Skill learning memory
    └── people/
        └── [person-name].md       # People memory
```

## Feishu Notifications

After configuring the `FEISHU_USER_ID` environment variable, notifications will be automatically sent upon successful synchronization:

- ✅ Sync Successful: Includes details of changes
- ❌ Sync Failed: Includes error information

## WAL Protocol (Write-Ahead Logging)

Memory writing rules:

1. **User expresses preference** → Immediately write to `MEMORY.md` → Then respond
2. **User makes a decision** → Immediately write to today's memory + `MEMORY.md` → Then respond
3. **Discover errors/lessons learned** → Immediately write to today's memory → Then respond
4. **Project-related context** → Write to `memory/projects/[project].md`

## Troubleshooting

### Log Locations

```bash
# Sync logs
tail -f ~/.openclaw/workspace/logs/memory-sync.log

# Morning read logs
tail -f ~/.openclaw/workspace/logs/memory-morning.log
```

### Common Issues

**Q: Git push failed**
A: Check network connection, run `git pull --rebase memory main` and try again.

**Q: Feishu notifications not sending**
A: Check if `FEISHU_USER_ID` is configured correctly.

**Q: Memory files lost**
A: Recover from GitHub: `git pull memory main`

## Related Resources

- GitHub Repository: https://github.com/renguanjie/ai-memory
- Documentation: https://docs.openclaw.ai/memory
