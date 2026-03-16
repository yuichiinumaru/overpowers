---
name: secure-memory-stack
description: "A secure, localized memory system that combines Baidu Embedding semantic search, Git Notes structured storage, and the file system to ensure data privacy and security."
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'memory', 'knowledge']
    version: "1.0.0"
---

# Secure Memory Stack

A secure, localized memory system combining Baidu Embedding semantic search, Git Notes structured storage, and the file system to ensure data privacy and security.

## Features

- ✅ **Fully Localized** - All data is stored on the local device
- ✅ **Zero Data Upload** - No data is sent to any external services
- ✅ **Semantic Search** - Semantic similarity search based on Baidu Embedding
- ✅ **Structured Storage** - Git Notes provide structured memory management
- ✅ **File System** - Traditional file storage, easy to manage
- ✅ **Hybrid Search** - Semantic + Keyword + Tag Search
- ✅ **Privacy Protection** - Complete data sovereignty

## Quick Installation

```bash
clawdhub install secure-memory-stack
```

## One-Click Initialization

```bash
# Initialize the secure memory system
bash /root/clawd/create/secure-memory-stack/scripts/setup.sh
```

## API Configuration Guide

The system will automatically detect and guide you through configuring necessary API keys:

1. **Baidu Embedding API** (if required)
2. **Other Optional Services**

## Usage Guide

### 1. System Initialization
```bash
# First-time setup
secure-memory setup
```

### 2. Check System Status
```bash
# Check memory system status
secure-memory status
```

### 3. Add Memory
```bash
# Add structured memory via Git Notes
secure-memory remember "Important decision: Use a localized memory system" --tags decision,security --importance high

# Update MEMORY.md for long-term memory
secure-memory add-longterm "User preferences: Concise and efficient communication"
```

### 4. Search Memory
```bash
# Semantic search
secure-memory search "security configuration"

# Structured search
secure-memory find --tag security

# File search
secure-memory lookup "user preferences"
```

### 5. System Maintenance
```bash
# Check system health status
secure-memory health

# View statistics
secure-memory stats
```

## Error Handling

### Common Errors and Solutions

**Error 1**: "Baidu Embedding API connection failed"
- Solution: Check Baidu API key configuration
- Run: `secure-memory configure baidu`

**Error 2**: "Git Notes system unavailable"
- Solution: Ensure Git is installed and correctly configured
- Run: `secure-memory fix git`

**Error 3**: "File permission error"
- Solution: Check workspace permissions
- Run: `secure-memory fix permissions`

**Error 4**: "No search results"
- Solution: Confirm the index has been updated
- Run: `secure-memory refresh`

## Configuration Files

The system will create configuration files in the following locations:
- `/root/clawd/memory_config.json` - Main configuration
- `/root/clawd/MEMORY.md` - Long-term memory
- `/root/clawd/SESSION-STATE.md` - Session state
- `/root/clawd/memory/` - Daily logs

## Directory Structure

```
/root/clawd/
├── MEMORY.md              # Long-term memory
├── SESSION-STATE.md       # Active working memory
├── memory/                # Daily logs
│   ├── YYYY-MM-DD.md      # Daily memory log
│   └── ...                # Historical logs
├── notes/                 # Knowledge organization
│   ├── projects/          # Projects
│   ├── areas/             # Areas
│   ├── resources/         # Resources
│   └── archive/           # Archive
└── skills/secure-memory-stack/
    ├── scripts/           # Management scripts
    ├── configs/           # Configuration templates
    └── docs/              # Documentation
```

## Command Reference

### Main Commands
- `secure-memory setup` - Initialize the system
- `secure-memory status` - Check system status
- `secure-memory search <query>` - Semantic search
- `secure-memory remember <content>` - Add memory
- `secure-memory health` - Health check
- `secure-memory configure <service>` - Configure API
- `secure-memory fix <component>` - Fix component

### Advanced Commands
- `secure-memory refresh` - Refresh index
- `secure-memory backup` - Backup memory
- `secure-memory restore` - Restore memory
- `secure-memory export` - Export memory
- `secure-memory stats` - Statistics

## Security Features

- **Localized Storage**: All data is stored locally only
- **Zero Upload**: No data is transmitted to any external services
- **Access Control**: Local machine access only
- **Privacy Protection**: Complete data sovereignty
- **Encryption Support**: Optional local encryption

## Troubleshooting

If you encounter issues, run:
```bash
secure-memory diagnose
```

This will perform a full system diagnosis and provide solutions.

## Updating the System

```bash
clawdhub update secure-memory-stack
```

## Uninstalling the System

```bash
secure-memory cleanup
```

Note: This will delete all configuration files but will not delete your memory files.

## Contribution

Issues and Pull Requests are welcome to improve this skill.
