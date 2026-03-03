# Task 0040: ACP & A2A Orchestration Research

**Status**: [x]
**Priority**: MEDIUM
**Type**: ai

## Objective
Research and define modern, optimal methods for orchestrating agents using Agent Client Protocol (ACP) and Agent-to-Agent (A2A) paradigms.

## Subtasks (mandatory):
- [x] Review Gemini CLI remote agents (`https://geminicli.com/docs/core/remote-agents/`).
- [x] Review Gemini CLI subagents (`https://geminicli.com/docs/core/subagents/`).
- [x] Evaluate OpenCode ACP integration (`https://opencode.ai/docs/acp/`).
- [x] Study ACP standard via `https://agentclientprotocol.com/get-started/registry`.
- [x] Synthesize findings into a new integration architecture plan.

## Research Findings & Integration Architecture Plan

### 1. The Protocols
- **A2A (Agent-to-Agent - Gemini CLI)**: Gemini CLI supports experimental remote subagents defined via Markdown frontmatter (`kind: remote`, `agent_card_url`). This allows the main Gemini CLI agent to delegate to specific remote agents natively.
- **ACP (Agent Client Protocol)**: A standardized, LSP-like protocol for Agents to communicate with Clients (editors like Zed, Neovim, etc.). Supported by **OpenCode**, **Gemini CLI**, **Cline**, and others. OpenCode can run as an ACP server using `opencode acp` (via stdio or nd-JSON).

### 2. Integration Architecture Strategy
To leverage both A2A and ACP in the Overpowers ecosystem, we should adopt a **Dual-Layer Orchestration Architecture**:

#### Layer A: The Client-Agent Bridge (ACP)
- **Standard**: All user-facing interaction occurs over ACP.
- **Implementation**: The user runs an ACP-compatible editor (Zed, Neovim + CodeCompanion) which connects to an orchestrator agent (like OpenCode running in `acp` mode, or Gemini CLI).
- **Benefit**: Decouples the UI from the agent runtime. The toolkit is no longer tied strictly to terminal commands; it becomes a native editor citizen.

#### Layer B: The Swarm Mesh (A2A)
- **Standard**: Inter-agent delegation and problem breakdown occurs over A2A (or tool-calling proxies if A2A is unavailable).
- **Implementation**: The primary ACP orchestrator (e.g., Gemini CLI) defines its swarm of 900+ agents as `.gemini/agents/*.md` remote definitions. When the user makes a complex request via the editor (ACP), the primary orchestrator parses it and delegates it to specialized agents via A2A.

### 3. Proposed Next Steps
1. Configure `opencode acp` as an experimental proxy to test editor integrations.
2. Build an automated script generator that produces remote agent definition files (`agent_card_url`) for the entire `agents/` and `skills/` directory to construct the Gemini A2A mesh.
3. Create an overarching "Swarm Coordinator" agent whose only job is to receive ACP requests and dispatch A2A tasks.
