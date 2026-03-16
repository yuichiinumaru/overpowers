---
name: life-todo-reminder
description: Automatically checks and reminds the user of pending home tasks when they interact via the web dashboard.
tags: [life, personal, todo, reminder, automation]
version: 1.0.0
---

# Home Todo

Check and remind the user of tasks to be handled after returning home.

## Scenario

When the user returns home and opens the Dashboard, remind them of tasks to be handled automatically.

## Todo File Location

```
~/.openclaw/workspace/.home-todos.md
```

## Trigger Conditions

Automatically triggered when the user sends any message through the Dashboard (webchat).

## Execution Steps

1. Read the todo file.
2. Parse todo items (exclude completed ones).
3. Add reminders at the end of the reply.

## Reminder Format

```
---

🏠 Home Todos:

1. [ ] Change bed sheets
2. [ ] Water plants
3. [ ] Tidy up the wardrobe
```

## Recording Method

When the user says "Need to do xxx when I get home" in **any channel** (Feishu, iMessage, etc.), it will be recorded in the todo file.

## Notes

- Use `[ ]` to indicate incomplete tasks.
- Users can delete items after checking them off.
- Automatically check every time a Dashboard message is sent.
