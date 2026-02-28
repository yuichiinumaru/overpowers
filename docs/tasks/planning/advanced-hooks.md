# Future Integration: Advanced Hooks (Oh My OpenCode)

**Source**: `references/oh-my-opencode/src/hooks/`

## Todo Continuation Enforcer
**Purpose**: Prevents agents from stopping halfway through a task list.

### Logic
1.  **Monitor**: Watches `session.idle` events.
2.  **Check**: Fetches current Todo list via API.
3.  **Detect**: If incomplete todos exist (>0), and agent is idle.
4.  **Inject**: Sends a system prompt: *"Incomplete tasks remain. Continue working..."*.
5.  **UI**: Shows a countdown toast to the user ("Resuming in 3s...").

### Implementation Requirements
*   Need access to OpenCode Client API (`ctx.client.session.todo`).
*   Need event listener for `session.idle`.
*   Need logic to parse "abort" signals to avoid forcing a stuck agent.

## Directory Readme Injector
**Purpose**: Automatically provides context when entering a directory.

### Logic
1.  **Monitor**: Watches for directory changes or session starts.
2.  **Read**: Checks for `README.md` or `AGENTS.md` in the new CWD.
3.  **Inject**: Adds a "Context" block to the next user message or system prompt.

## Edit Error Recovery
**Purpose**: Auto-fixes common mistakes agents make when editing files.

### Logic
1.  **Monitor**: `tool.error` events on `edit` tool.
2.  **Classify**: Identify error type (e.g., "Line number out of bounds", "Indentation mismatch").
3.  **Recover**:
    *   If simple (e.g., off by 1 line), re-try automatically.
    *   If complex, inject a "Hint" prompt explaining specifically *why* it failed so the agent can self-correct.
