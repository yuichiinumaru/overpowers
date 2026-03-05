---
name: todo-enforcer
description: Enforces continuation of tasks when pending items exist in tasklist.md
trigger: SessionIdle
matcher: .*
---

# Todo Enforcer

## Implementation

```bash
#!/bin/bash
python3 "${OVERPOWERS_PATH:-$(pwd)}/hooks/runtime/todo_enforcer.py"
```
