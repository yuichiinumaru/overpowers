
### Safety Hooks
*   **Destructive Command Guard**: `hooks/safety/destructive-command-blocker.ts` checks shell commands against regex patterns (ported from `destructive_command_guard`) to prevent catastrophic errors like `rm -rf /` or `mkfs` on physical drives.
