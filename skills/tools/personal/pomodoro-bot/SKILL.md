---
name: pomodoro-bot
description: "Focus Pomodoro Assistant. Starts a 25-minute work countdown + a 5-minute break countdown, supporting pause/skip. Triggered when the user says 'Start Pomodoro', 'Timer 25 minutes', 'Break time is over', etc."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Pomodoro Bot Skill Description

## Trigger Conditions
- User explicitly requests to start/stop/skip the Pomodoro timer.
- Keywords such as "pomodoro", "25 minutes", "focus", "break" are mentioned.
- Requires timed reminders but not for one-off tasks (distinguished from one-off cron reminders).

## Core Capabilities
1. Start work countdown (default 25m).
2. Work ends → automatically start break countdown (default 5m).
3. Supports `pause` / `skip` / `reset` commands.
4. Send a summary upon completion (e.g., ✅ Completed 1 Pomodoro session).

## Usage
- Direct invocation: `sessions_spawn agentId=pomodoro-bot task="Start Pomodoro, 25 minutes work + 5 minutes break"`
- Or automatically triggered by the main session based on semantics.

## Resource Description
- `scripts/start_pomodoro.sh`: Responsible for creating the cron task chain (work → break → notification).
- `references/config.md`: Configurable durations, sounds, message templates.
- `assets/timer-icon.png`: Optional UI icon (to be displayed in messages).

> 💡 Note: This skill relies on `openclaw cron` for countdowns and does not occupy main session resources.
