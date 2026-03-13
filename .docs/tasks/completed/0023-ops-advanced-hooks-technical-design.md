# Technical Design: Advanced Hooks Implementation

## 1. Architecture
The hooks will be implemented as Python scripts in `hooks/runtime/` or as wrapper scripts around the core agent call.

## 2. Components

### A. Todo Enforcer (`hooks/runtime/todo_enforcer.py`)
- **Input**: Current session state + Todo list.
- **Mechanism**: Use `opencode` API or scan `tasklist.md` for `[ ]` markers.
- **Output**: Inject instruction: "PENDING TASKS: [list]. CONTINUE."

### B. Directory Injector (`hooks/runtime/dir_injector.py`)
- **Input**: `CWD` (Current Working Directory).
- **Mechanism**: Shell `cd` hook or periodic poll.
- **Action**: Check for `README.md`, `AGENTS.md`, or `.opencode/CONTEXT.md`.

### C. Edit Guard Middleware
- **Logic**: Intercept `tool.edit` results.
- **Error Mapping**: Map standard errors to human-readable (and agent-readable) recovery hints.

## 3. Data Flow
`Agent Call` -> `Middleware Check` -> `Tool Execution` -> `Result Analysis` -> `Post-Hook Feedback` -> `Agent Resume`.
