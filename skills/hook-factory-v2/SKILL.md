---
name: hook-factory-v2
description: - **Validation**: Ensure the hook doesn't introduce side effects or security risks.
---

# hook-factory-v2

Advanced hook creation with validation and lifecycle management.

## Hook Lifecycle
- **Trigger**: Define the event that activates the hook (e.g., file edit, command completion).
- **Condition**: Optional logic to determine if the hook should execute.
- **Action**: The specific bash command or script to run.
- **Validation**: Ensure the hook doesn't introduce side effects or security risks.

## Best Practices
- Keep hooks lightweight to avoid slowing down workflows.
- Log hook activities for transparency.
- Provide clear error messages when a hook fails.

