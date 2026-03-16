---
name: tool-productivity-todo-manager
description: Manages to-do items. Supports adding, viewing, completing, and deleting to-dos. Data is stored in the local `todos.md` file.
tags: [tool, productivity, todo, task-management]
version: 1.0.0
---

# Todo Manager

## Features

### Add Todo
```
/todo add <item>
/todo + <item>
```

### View Todos
```
/todo list
/todo ls
```

### Complete Todo
```
/todo done <number>
/todo <number> done
```

### Remove Todo
```
/todo rm <number>
```

## Storage

Todo file: `~/.openclaw/workspace/todos.md`

Format:
```markdown
# Todos

- [ ] Task 1
- [x] Task 2
- [ ] Task 3

## Completed
- Task 2 (2026-02-24)
```

## Usage Examples

User: "/todo add Go to the gym"
→ Added todo: Go to the gym

User: "/todo list"
→ Displaying all todos

User: "/todo done 1"
→ Marked the first todo as completed

---
*Todo Manager Skill*
