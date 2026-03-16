---
name: sync-memory-skills
description: "Tool to synchronize memory system skill files to the create directory"
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'memory', 'knowledge']
    version: "1.0.0"
---

# Memory System Skills Sync Tool

An automated tool for synchronizing memory system skill files to the create directory.

## Features
- Synchronizes memory system skill scripts from the main directory to the create directory
- Automatically sets correct file permissions
- Synchronizes related documentation files

## Usage
```bash
# Run sync manually
bash /root/clawd/skills/memory-skills-sync/sync_memory_skills.sh

# Or call via skill
# (Specific calling method depends on Clawdbot's skill execution mechanism)
```

## File Structure
```
skills/memory-skills-sync/
├── SKILL.md           # This documentation file
├── sync_memory_skills.sh  # Main synchronization script
├── README.md         # Detailed description
└── package.json      # Package definition
```

## Dependencies
- bash
- cp (copy command)
- chmod (permission setting)
- find (file searching)

## Verification
- The sync script has been verified to be executable in multiple directories
- Permissions are set correctly
- Target directory existence check is implemented
