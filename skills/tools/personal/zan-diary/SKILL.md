---
name: zan-diary
description: Zan's personal diary system. Used for recording schedules, managing to-dos, and tracking annual goals. Used when the user wants to write a diary, view a diary, manage to-dos, or update goal progress.
---

# Zan's Diary System

## File Location
- Diary directory: `~/.zan-diary/`
- One file per year: `~/.zan-diary/2026.md`

## File Structure

```markdown
# 2026 Annual Goals
- Goal: Earn 2 million
- Current Progress: xx million (xx%)

---

# To-Do List
- [ ] To-do 1
- [ ] To-do 2

---

# Diary Body

## 2026-02-22
Today's content...

---

## 2026-02-21
Previous day's content...
```

## Operation Rules

### Add Diary Entry
1. Read the current year's file (e.g., `~/.zan-diary/2026.md`)
2. Insert the new date paragraph at the very top of the "Diary Body"
3. If the current year's file does not exist, create a new file

### Add To-Do Item
1. Read the file
2. Add a new item under "To-Do List"
3. Maintain the original order

### Complete To-Do Item
1. Remove the item from the "To-Do List"
2. Add "✅ Completed: xxx" at the end of the diary body for the current day

### Update Goal Progress
1. Modify the "Current Progress" line
2. Automatically calculate the percentage

### View Diary
1. Directly read the corresponding year's file
2. Display the latest 30 days' content by default
