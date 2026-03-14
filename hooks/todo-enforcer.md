---
name: todo-enforcer
description: Enforces continuation of tasks when pending items exist in docs/tasklist.md or .agents/continuity logs.
trigger: PostToolUse
matcher: .*
---

# Todo Enforcer

## Implementation

```bash
#!/bin/bash
python3 "${OVERPOWERS_PATH:-$(pwd)}/hooks/runtime/todo_enforcer.py"
```

## Notes
- Continuity source of truth: `.agents/continuity-<agent-name>.md`.
- Legacy fallback is supported for root-level `continuity-*.md` files.
