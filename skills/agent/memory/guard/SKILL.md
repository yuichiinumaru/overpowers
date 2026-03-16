---
name: subagent-isolation-guard
description: "All subagents must be configured with independent 'agentDir':"
---

#🛡️ Subagent Isolation GuardConsolidate subagent physical isolation and semantic routing bypass.

## 🎯 Solved Issues1. **Context contamination**: Prevent different subagents from sharing the same workspace, which can cause file read/write conflicts and context interference.
## 🛠️ Core Mechanisms

### 1. Physical Isolation (Workspace Isolation)
All subagents must be configured with independent `agentDir`:
- `agents/pm/workspace/`
- `agents/architect/workspace/`
- ...

### 2. Semantic Routing Bypass
In `semantic-webhook-server.py` the automatic bypass is implemented via `session_key` feature code detection:
- Identify feature: `:subagent:`
- Action: directly return `continue`, do not inject statements, do not execute model suggestions.

## 📝 Consolidated Rules (AGENTS.md)

When creating or modifying a subagent, you must ensure:
- `allowAgents` list is complete.
- Each subagent has a clear, non-overlapping `agentDir`.
- Subagent session ID must include `:subagent:` identifier.
