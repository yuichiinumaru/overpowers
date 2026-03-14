---
name: edit-guard
description: Catches common tool errors and injects specific hints for agent self-recovery.
trigger: PostToolUse
matcher: (replace|write_file|edit_block)
---

# Edit Guard

## Implementation

```bash
#!/bin/bash
# Assuming the tool error output is piped here via stdin or as an environment variable by the orchestrator.
python3 "${OVERPOWERS_PATH:-$(pwd)}/hooks/runtime/edit_guard.py"
```
