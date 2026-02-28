---
name: gemini-cli-delegation
description: Teaches how to delegate tasks to Gemini CLI agents in headless/YOLO mode
---

# 🤖 Gemini CLI Delegation Skill

This skill allows an agent to seamlessly delegate tasks to another `gemini` CLI subagent running in headless mode. Useful for parallel execution, background tasks, or fanning out large workloads.

## 📌 Headless & YOLO Mode

To delegate a task programmatically without an interactive UI, use the **headless mode** by passing the prompt directly with the `-y` (YOLO) flag so the subagent auto-approves actions.

```bash
gemini -y "Analyze this directory and write a summary in summary.txt"
```

### Passing Input via STDIN
You can pipe or redirect input directly into the `gemini` command:

```bash
cat error.log | gemini -y "Find the root cause and explain the exception"
git diff | gemini -y "Write a commit message based on this diff"
```

### Specifying Models
To ensure the correct model is used for a delegated task, pass the `-m` flag with the model alias:

```bash
gemini -y -m flash "Quickly lint this file"
gemini -y -m pro "Refactor this architecture thoroughly"
```

## 🔄 Output Formats

By default, the headless CLI outputs standard text. For programmatic processing, you can request JSON using `-o`:

```bash
gemini -y -o json "Generate a JSON configuration for Docker"
```

*(Note: The JSON schema contains `response`, `stats`, and `error` objects).*

## ✅ Exit Codes

When delegating tasks in bash scripts, you MUST check the exit code (`$?`) to determine success:

- `0`: Success. The subagent completed its task.
- `1`: General error or API failure.
- `42`: Input error (invalid prompt/arguments).
- `53`: Turn limit exceeded.

**Example script delegating tasks:**
```bash
if gemini -y "Run unit tests and fix any failing files"; then
    echo "Subagent succeeded."
else
    echo "Subagent failed with exit code $?"
fi
```
