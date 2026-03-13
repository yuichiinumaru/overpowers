---
name: interactive-bash
description: "Run interactive commands via tmux. Use for TUI apps (vim, htop) or long-running processes that need input. Pass tmux subcommands directly (e.g., 'new-session -d -s myses')."
---

# Interactive Bash (Tmux Wrapper)

This command wraps `tmux` to allow interactive TUI applications and persistent sessions.

## Usage

\`\`\`bash
# Create a new session
/invoke interactive-bash "new-session -d -s my-session"

# Send keys (input) to the session
/invoke interactive-bash "send-keys -t my-session 'ls -la' Enter"

# Check status
/invoke interactive-bash "list-sessions"
\`\`\`

## Blocked Commands

The following commands are blocked for stability (use `bash` tool instead):
- `capture-pane` / `capturep`
- `save-buffer` / `saveb`
- `show-buffer` / `showb`
- `pipe-pane` / `pipep`

To capture output, use the standard `bash` tool:
\`\`\`bash
tmux capture-pane -p -t my-session
\`\`\`
