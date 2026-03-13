# Sandbox & Execution Guidelines

**Source**: `references/moltbot/src/process/`

## Overview
Safe execution of code and commands is critical for an agentic system. This protocol outlines how to handle child processes and execution lanes.

## Execution Lanes (Concurrency Control)
To prevent race conditions and output interleaving, use **Execution Lanes**.

*   **Main Lane**: Default for most tasks. Serial execution.
*   **Background/Cron Lane**: For low-priority, long-running tasks.
*   **Probe Lane**: For quick checks (e.g., `git status`) that shouldn't block main work.

### Implementation Pattern
```typescript
// Queue structure
type QueueEntry = {
  task: () => Promise<unknown>;
  resolve: (value: unknown) => void;
  reject: (reason?: unknown) => void;
}

// Logic
// 1. Enqueue task
// 2. If lane is not draining, start draining
// 3. Execute one by one (or up to maxConcurrent)
```

## Safe Spawning
When using `spawn` or `execFile`:

1.  **Timeouts**: ALWAYS set a timeout (e.g., 10s for simple commands, 60s for installs).
2.  **Signal Killing**: If timeout executes, use `SIGKILL` to ensure process death.
3.  **Stdio**: Inherit `stdio` only when interactivity is strictly needed. Otherwise capture buffers.
4.  **Environment Sanitization**:
    *   Suppress `npm` funding messages (`NPM_CONFIG_FUND=false`).
    *   Ensure PATH includes necessary binaries.

## Best Practices
*   **Input**: Write input to `stdin` and end stream immediately.
*   **Verbosity**: Log `stdout`/`stderr` only in verbose/debug mode, unless error occurs.
*   **Error Handling**: Wrap all execution in try/catch and log the exact command that failed.

## Reference Implementation
See `scripts/compound/` or `moltbot/src/process/exec.ts` for concrete examples of `runCommandWithTimeout`.
