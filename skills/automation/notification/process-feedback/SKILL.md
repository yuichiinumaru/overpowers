---
name: automation-feishu-process-feedback
description: Automated Feishu message processing and progress feedback system. Monitors tasks in the background and provides real-time updates (confirmation, percentage, completion).
tags: automation, feishu, feedback, background-process, monitoring
version: 1.0.0
---

# Feishu Process Feedback Skill

Real-time task processing and progress feedback system for Feishu/Lark.

## Functions

- **Automated Background Monitoring**: Polls for new messages and identifies tasks.
- **Instant Confirmation**: Responds within 5s with task ID and subtask count.
- **Progress Tracking**: Real-time percentage updates (33%, 66%, 100%).
- **Process Isolation**: Each task runs in a separate Node.js process.
- **Fault Tolerance**: Automatic retries and persistence across restarts.

## Usage

### Installation
```bash
clawhub install feishu-process-feedback
```

### Start Service
```bash
node scripts/listener.js
```

### Configuration
| Variable | Description | Default |
|--------|------|--------|
| `FEISHU_POLL_INTERVAL` | Polling interval (ms) | 5000 |
| `FEISHU_MAX_CONCURRENT` | Max concurrent tasks | 5 |
| `FEISHU_PROCESS_TIMEOUT` | Task timeout (ms) | 300000 |
