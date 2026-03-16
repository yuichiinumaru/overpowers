---
name: sulada-habit-tracker
description: "AI skill for sulada habit tracker"
version: "1.0.0"
tags: ["skill", "ai"]
---

# Habit Tracker

> Track habit formation, remind to check in, maintain self-discipline

## Features

1. **Add Habit** - Define new habits to cultivate
2. **Daily Check-in** - Record completion status
3. **Statistics** - Consecutive check-in days statistics
4. **Reminders** - Remind when not checked in

## Usage

### Add Habit
```
Please add a new habit: [Habit Name]
Frequency: Daily / X times per week
Reminder Time: HH:MM
```

### Check-in
```
Please complete today's [Habit Name] check-in
```

### View Progress
```
Please view habit tracking progress
```

## Habit List

Recorded in `memory/habits.json`:

```json
{
  "Habit Name": {
    "creation_date": "2026-03-02",
    "frequency": "daily",
    "consecutive_days": 0,
    "total_completions": 0,
    "last_check_in": null
  }
}
```

## Preset Habits (Editable)

- 💪 Wake up early - Wake up before 7 AM daily
- 🏃 Exercise - 30 minutes daily
- 📖 Read - 30 minutes daily
- 💻 Study - 1 hour of AI/programming daily
- 😴 Sleep early - Go to bed before 11 PM daily
