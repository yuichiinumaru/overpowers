# Hooks Guide

overpowers includes **29 event-driven hooks** that automate tasks triggered by specific events during your development workflow.

## What are Hooks?

Hooks are automated actions that run when specific events occur (file changes, session start, before commands, etc.). They integrate with OpenCode and Claude Code to provide real-time automation.

## Available Hooks

### Notifications

| Hook | Description |
|------|-------------|
| `discord-notifications.md` | Basic Discord webhook notifications |
| `discord-detailed-notifications.md` | Detailed Discord notifications with context |
| `discord-error-notifications.md` | Error-only Discord alerts |
| `slack-notifications.md` | Basic Slack webhook notifications |
| `slack-detailed-notifications.md` | Detailed Slack notifications |
| `slack-error-notifications.md` | Error-only Slack alerts |
| `telegram-notifications.md` | Basic Telegram bot notifications |
| `telegram-detailed-notifications.md` | Detailed Telegram notifications |
| `telegram-error-notifications.md` | Error-only Telegram alerts |
| `simple-notifications.md` | Generic notification template |

### Git Automation

| Hook | Description |
|------|-------------|
| `auto-git-add.md` | Automatically stage changed files |
| `git-add-changes.md` | Stage changes after edits |
| `smart-commit.md` | Generate intelligent commit messages |

### Code Quality

| Hook | Description |
|------|-------------|
| `lint-on-save.md` | Run linter when files are saved |
| `format-javascript-files.md` | Auto-format JS/TS files |
| `format-python-files.md` | Auto-format Python files |
| `smart-formatting.md` | Context-aware code formatting |

### Testing & Quality

| Hook | Description |
|------|-------------|
| `run-tests-after-changes.md` | Automatically run tests after edits |
| `test-runner.md` | Generic test execution hook |
| `build-on-change.md` | Trigger builds on file changes |
| `dependency-checker.md` | Check for outdated dependencies |

### Security & Protection

| Hook | Description |
|------|-------------|
| `file-protection.md` | Prevent accidental file overwrites |
| `file-protection-hook.md` | Enhanced file protection |
| `security-scanner.md` | Scan for security vulnerabilities |

### Monitoring & Utility

| Hook | Description |
|------|-------------|
| `change-tracker.md` | Track all file changes |
| `file-backup.md` | Automatic file backups |
| `performance-monitor.md` | Monitor execution performance |
| `notify-before-bash.md` | Notification before bash commands |

## Hook Structure

Each hook follows this format:

```markdown
---
name: hook-name
description: What this hook does
trigger: SessionStart | PreToolUse | PostToolUse | FileChange
matcher: Optional regex pattern for filtering
---

# Hook Name

## Configuration

Required environment variables or settings.

## Implementation

The actual hook logic (usually shell commands).
```

## Using Hooks

### OpenCode

Hooks are configured in your `opencode.json`:

```json
{
  "hooks": {
    "SessionStart": ["./overpowers/hooks/session-start.sh"],
    "PostToolUse": {
      "matcher": "Write|Edit",
      "command": "./overpowers/hooks/auto-git-add.md"
    }
  }
}
```

### Claude Code

Hooks are defined in `hooks/hooks.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

## Creating New Hooks

1. Create a new `.md` file in `hooks/`:

```markdown
---
name: my-custom-hook
description: What my hook does
trigger: PostToolUse
matcher: Write
---

# My Custom Hook

## Configuration

- `MY_VAR`: Description of required variable

## Implementation

\`\`\`bash
#!/bin/bash
# Your hook logic here
echo "Hook triggered!"
\`\`\`
```

2. Register the hook in `hooks.json` or your config file.

3. Test the hook by triggering the relevant event.

## Cross-Platform Considerations

For Windows compatibility, use the polyglot wrapper pattern:

```cmd
: << 'CMDBLOCK'
@echo off
"C:\Program Files\Git\bin\bash.exe" -l -c "$(cygpath -u \"$CLAUDE_PLUGIN_ROOT\")/hooks/my-hook.sh"
exit /b
CMDBLOCK

# Unix shell runs from here
"${CLAUDE_PLUGIN_ROOT}/hooks/my-hook.sh"
```

See `hooks/run-hook.cmd` for a reusable wrapper.

## Best Practices

1. **Keep hooks fast** - They run synchronously and can slow down workflows
2. **Handle errors gracefully** - Don't break the workflow on hook failure
3. **Use environment variables** - Keep secrets out of hook code
4. **Log sparingly** - Too much output clutters the interface
5. **Test in isolation** - Verify hooks work before deploying
