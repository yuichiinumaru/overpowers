---
name: ai-research-zeelin-deep-research
description: Asynchronous deep research skill using Zeelin Deep Research API. Features automated outline confirmation, periodic status polling, and automatic result saving. Requires user input for thinking mode and search scope.
tags: [deep-research, zeelin, ai-research, asynchronous, automated-reporting]
version: 1.0.0
---

# Zeelin Deep Research Skill

This skill is used to call the Zeelin Deep Research API to execute deep research tasks, using a completely asynchronous processing mode.

## ⚠️ Important: Ask the user before use

When a user requests a research task, you **must first ask for the following information**:

1.  **Thinking Mode** (Required):
    | Mode | Description | Use Case |
    | :--- | :--- | :--- |
    | smart | Normal mode | Quick and simple questions |
    | deep | Deep mode (~5000 words) | Papers, competitive research, medium reports |
    | major | Expert mode (~10000+ words) | In-depth research reports |

2.  **Search Scope** (Required):
    | Scope | Description |
    | :--- | :--- |
    | web | Search across the entire web |
    | academic | Academic search |
    | selected | Selected sources |

3.  **Research Topic** (Required): The specific question or topic the user wants to research.

## Configure API Key

### Method 1: Command line setting (Recommended)
```bash
python3 scripts/async_runner.py --set-key "YOUR_API_KEY"
```

### Method 2: Configuration file
```bash
echo '{"api_key": "YOUR_API_KEY"}' > ~/.openclaw/zeelin-config.json
```

Get API Key: https://desearch.zeelin.cn

## How to Use

### 1. Check API Key
```bash
python3 scripts/async_runner.py --check-key
```

### 2. Submit Task
```bash
python3 scripts/async_runner.py -q "Research Topic" -t deep -sr web
```

## Features

1.  **Asynchronous Submission**: Returns immediately after task submission without blocking.
2.  **Automatic Outline Confirmation**: Background process automatically calls `confirmOutline`.
3.  **Periodic Checking**: Checks task status every 30 seconds.
4.  **Automatic Notification**: A cron job (every 2 minutes) checks for task completion and notifies the user once finished.
5.  **Automatic Saving**: Automatically saves the Markdown (.md) file once complete.

## Result Files

After task completion, the Markdown file is automatically saved to:
```
skills/ai-research-zeelin-deep-research/reports/zeelin_TOPIC_TIMESTAMP.md
```

## Cron Timer

- **Interval**: Every 1 minute.
- **Function**: Check task completion status.
- **Notification**: Proactively notify the user when the task is finished.
