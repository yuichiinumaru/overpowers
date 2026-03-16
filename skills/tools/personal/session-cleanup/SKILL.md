---
name: session-cleanup
description: "Periodically cleans up expired sessions, evaluates and saves valuable information, and automatically cleans up valueless sessions."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Session Cleanup

Periodically check and clean up expired sessions, evaluate session value, and save important information.

## Capability Profile

- **Input**: Session directory path
- **Output**: Cleanup report + Saved valuable sessions
- **Core**: Expiration Detection → Value Assessment → Selective Cleanup

## Workflow

```
1. Scan session directory
2. Check for expired sessions (7 days of inactivity)
3. Evaluate session value (keyword matching)
4. Save valuable sessions to memory
5. Clean up valueless sessions
6. Generate report
```

## Target Directories

| Directory | Description |
|------|------|
| ~/.openclaw/cron/runs/ | Scheduled task run records |
| ~/.openclaw/delivery-queue/ | Message delivery queue |
| ~/.openclaw/telegram/ | Telegram session data |
| ~/.openclaw/subagents/ | Sub-agent sessions |

## Expiration Rules

- **cron runs**: Over 3 days
- **delivery-queue**: Over 1 day (completed/failed)
- **telegram**: Over 7 days
- **subagents**: Over 7 days

## Value Assessment Keywords

| Category | Keywords |
|------|--------|
| Important Decisions | decision, important, remember, 重要, 决策 |
| Learning | learn, study, understand, 学习, 理解 |
| Problem Solving | fix, bug, error, 修复, 问题, 错误 |
| Creation | create, build, new, 创建, 新建 |

## Proactiveness

- Executes once a week
- Automatically evaluates and saves valuable content
- Reports cleanup results

## Usage

```bash
# Manual execution
~/.openclaw/workspace/skills/session-cleanup/cleanup.sh

# Configure scheduled task (every Sunday at 3 AM)
cron job add session-cleanup "0 3 * * 0" ~/.openclaw/workspace/skills/session-cleanup/run.sh
```
