# Technical Design: Advanced Hooks Implementation

## 1. Architecture Overview
The system uses the Gemini CLI / Claude Code hook architecture. Hooks are defined in `hooks/*.md` (OpenCode format) and registered in `hooks/hooks.json` (Gemini CLI format).

New hooks are added as Python scripts in `hooks/runtime/` to leverage Python's string manipulation and file system capabilities.

## 2. API Signatures & Data Contracts

### Hooks Registration (`hooks/hooks.json`)
The following structures will be added:

```json
{
  "PreToolUse": [
    {
      "matcher": "bash|run_shell_command|cd",
      "hooks": [
        {
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/runtime/dir_injector.py"
        }
      ]
    }
  ],
  "PostToolUse": [
    {
      "matcher": "replace|write_file|edit_block",
      "hooks": [
        {
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/runtime/edit_guard.py"
        }
      ]
    },
    {
      "matcher": ".*",
      "hooks": [
        {
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/runtime/todo_enforcer.py"
        }
      ]
    }
  ]
}
```

## 3. Database & Schema Changes
- **N/A**: No databases are modified.

## 4. System Dependencies
- **Python 3.x**: Required to run the hook scripts.
- **Environment Variables**:
  - `OVERPOWERS_PATH`: Path to the repository root (defaults to CWD).
  - `CLAUDE_PLUGIN_ROOT`: Root path for hook discovery.

## 5. Security & Performance Considerations
- **Security Implications:** Hooks run arbitrary Python code. They are restricted to the local environment and do not transmit data externally.
- **Performance Impact:** Each hook adds ~100-300ms overhead for Python startup. Using specific matchers minimizes this.
- **Error Handling:** `edit_guard.py` specifically addresses graceful recovery from tool errors.

## 6. Testing Strategy
- **Unit Tests:** Verify individual Python scripts with mock file structures.
- **Manual Verification:**
  - Trigger `dir_injector` by running `cd` in a directory with a `README.md`.
  - Trigger `edit_guard` by inducing a fake indentation error in a tool call.
  - Trigger `todo_enforcer` by leaving a `[ ]` item in `continuity-omega.md`.
