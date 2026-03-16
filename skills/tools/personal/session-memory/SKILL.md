---
name: openclaw-skill-session-memory
description: "Openclaw Skill Session Memory - Automatically records conversation content, stores it by date, and supports quick keyword search recall."
metadata:
  openclaw:
    category: "openclaw"
    tags: ['openclaw', 'agent', 'automation']
    version: "1.0.0"
---

# Session Memory Skill

Automatically records conversation content, stores it by date, and supports quick keyword search for retrieval.

## Features

- **Automatic Recording**: Automatically saves conversation content to an md file after each session.
- **Store by Date**: Files are saved in `memory/conversations/YYYY-MM-DD.md`.
- **Data Anonymization**: Automatically filters sensitive information such as account numbers, passwords, keys, and tokens.
- **Quick Search**: Supports keyword regex matching, no need to load the entire file.

## Usage

### Automatic Recording (Automatically called at the end of a session)

The skill will be automatically invoked at the end of a session to record the conversation content.

### Manual Search and Retrieval

```bash
# Search for keywords (defaults to the last 7 days)
python3 ~/.openclaw/workspace/skills/session-memory/search.py "keyword"

# Search for a specified number of days
python3 ~/.openclaw/workspace/skills/session-memory/search.py "keyword" --days 30

# List all recent conversation files
python3 ~/.openclaw/workspace/skills/session-memory/search.py --list
```

## Anonymization Rules

Automatically replaces the following content:
- Email: `xxx@xxx.com` → `[EMAIL]`
- Phone Number: 11-digit number → `[PHONE]`
- API Key/Token: Long strings containing `key`, `token`, `secret`, `password` → `[REDACTED]`
- ID Card Number: 18 digits → `[ID]`
- Bank Card Number: 16-19 digits → `[CARD]`
- IP Address: → `[IP]`

## File Format

```markdown
# 2026-03-02 Conversation Record

## Session 1
- Time: 19:13 - 19:20
- Channel: feishu
- Number of messages: 6

### Key Content
- User asked if Yan Yan was online
- Discussed session loss issues
- Requested the creation of a session memory skill

### Message Summary
- [19:13] User: "Yan Yan, are you there?"
- [19:15] Yan Yan: "It was probably a network delay just now."
...
```

## Technical Implementation

- Python scripts to process conversation logs
- Regular expressions for matching sensitive information
- File splitting by date for quick retrieval
