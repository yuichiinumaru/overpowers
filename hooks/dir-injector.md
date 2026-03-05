---
name: dir-injector
description: Injects local README.md or AGENTS.md automatically when navigating directories
trigger: PreToolUse
matcher: (bash|run_command|cd)
---

# Directory Context Injector

## Implementation

```bash
#!/bin/bash
python3 "${OVERPOWERS_PATH:-$(pwd)}/hooks/runtime/dir_injector.py"
```
