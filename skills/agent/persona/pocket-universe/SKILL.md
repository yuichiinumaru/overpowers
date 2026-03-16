---
name: pocket-universe
description: Simulate multi-agent interactions, test concurrent behavior, inter-agent
  broadcasting, and deep nesting to validate swarm architecture health.
tags:
- ai
- llm
version: 1.0.0
category: general
---
# 🌌 Pocket Universe Simulator

The `pocket-universe` skill is a testing sandbox intended for orchestrator agents and AI engineers to validate the operational health of multi-agent communication frameworks (like `claude-flow`, `gemini-cli` with subagents, or `antigravity`).

Its main purpose is to test if agents can talk to each other correctly, run in parallel without race conditions, and spawn child agents properly.

## 🎯 When to Use This Skill
- When debugging "lost in the middle" or cross-talk issues between agents.
- To verify that the `broadcast` or `announce` tools operate correctly across independent agent processes.
- To test deep-nesting capabilities (an agent spawning an agent that spawns another agent).
- Whenever pushing a major update to the swarm/orchestrator core that might break inter-agent coordination.

## 📦 What's Inside?

The scenarios are located in the `skills/pocket-universe/scenarios/` directory. You can use these files as prompt templates when kicking off tasks:

### 1. Broadcast Ping-Pong (`sibling-01.md` / `sibling-02.md`)
Validates that two agents running in parallel can exchange information dynamically.
- **Agent A** uses `broadcast` to send questions.
- **Agent B** sleeps, waits for messages, and uses `broadcast` with the `reply_to` parameter to answer them.
- *Checks:* Context leakage, `sleep` / delay mechanics, and specific targeting of agents.

### 2. Nested Spawning (`spawn.md` / `spawn-02.md`)
Validates vertical multi-agent delegation. 
- **Agent A** creates **Agent B**, asking it to perform a task or create **Agent C**.
- Meanwhile, Agent A continues executing other sequential or parallel tasks.
- *Checks:* Task tool invocation, nested prompts, and parallel vs sequential execution boundaries.

### 3. Session Resume (`session-resume.md`)
Validates specific command ordering and strict prompt adherence across session re-invocations.

## 🚀 How to Execute a Pocket Universe Test

1. **Select a Scenario:** Find the appropriate test inside `skills/pocket-universe/scenarios/`.
2. **Read the Rules:** Read the prompt text using `view_file`.
3. **Dispatch the Swarm:** Use your framework's task orchestration mechanism (e.g., `/skill subagent-orchestration` or simply the `task` tool) and plug the exact prompt text from the scenario into the subagents.
4. **Observe the Verdict:** Validate that the subagents obeyed constraints (e.g., executing sequentially, not using parallel tools where forbidden, or correctly returning VERBATIM text).

**Example Invocation (if you have task creation tools):**
*"I am initiating the Pocket Universe Ping-Pong scenario. Spawning Agent 1 with the prompt from `sibling-01.md` and Agent 2 with the prompt from `sibling-02.md`."*
