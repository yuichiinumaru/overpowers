Perfect. Now I have the comprehensive information. Let me provide a detailed answer about non-interactive mode capabilities.

## OpenCode Non-Interactive Mode: CLI Arguments & Capabilities

OpenCode has two primary ways to use the CLI: the TUI (default) and non-interactive mode via the `run` command. Here's what you can and cannot do in non-interactive mode versus the TUI. [opencode](https://opencode.ai/docs/cli/)

### Non-Interactive Mode (`opencode run`)

Non-interactive mode is designed for **scripting, automation, and CI/CD pipelines**. You pass a prompt directly as an argument and OpenCode processes it, outputs the result to stdout, and exits. [dev.opencode](https://dev.opencode.ai/docs/cli/)

**Basic usage:**
```bash
opencode run "Explain the most common uses of 'awk' with examples"
```

### Available Flags in Non-Interactive Mode

| Flag | Short | Purpose |
|------|-------|---------|
| `--model` | `-m` | Specify LLM (e.g., `anthropic/claude-3-5-sonnet`)  [opencode](https://opencode.ai/docs/cli/) |
| `--agent` | | Choose agent: `build` (default) or `plan` (read-only)  [opencode](https://opencode.ai/docs/cli/) |
| `--continue` | `-c` | Continue the last session  [opencode](https://opencode.ai/docs/cli/) |
| `--session` | `-s` | Resume a specific session by ID  [opencode](https://opencode.ai/docs/cli/) |
| `--share` | | Generate shareable link for the session  [opencode](https://opencode.ai/docs/cli/) |
| `--file` | `-f` | Attach file(s) to the message  [opencode](https://opencode.ai/docs/cli/) |
| `--format` | | Output format: `default` (formatted) or `json` (raw events)  [opencode](https://opencode.ai/docs/cli/) |
| `--title` | | Custom session title  [opencode](https://opencode.ai/docs/cli/) |
| `--attach` | | Connect to running server (e.g., `http://localhost:4096`)  [opencode](https://opencode.ai/docs/cli/) |
| `--port` | | Port for local server (random if omitted)  [opencode](https://opencode.ai/docs/cli/) |
| `--command` | | Use a custom command template instead of a raw prompt  [opencode](https://opencode.ai/docs/cli/) |

### What You Can Do in Non-Interactive Mode

✅ **Code analysis & explanation** — Ask OpenCode to analyze, explain, or explore codebases (especially useful with `--agent plan` for read-only analysis) [opencode](https://opencode.ai/docs/cli/)

✅ **Single-turn prompts** — Get answers without TUI overhead; ideal for one-shot automation tasks [opencode](https://opencode.ai/docs/cli/)

✅ **Session continuity** — Continue previous conversations using `--continue` or `--session <ID>` to maintain context [opencode](https://opencode.ai/docs/cli/)

✅ **Piping & redirection** — Output to files or pipe into other commands; JSON output (`--format json`) is machine-readable for parsing [opencode](https://opencode.ai/docs/cli/)

✅ **Custom agents** — Leverage the `plan` agent for safe, read-only code exploration [opencode](https://opencode.ai/docs/cli/)

✅ **File attachments** — Include relevant files with `--file` to provide context [opencode](https://opencode.ai/docs/cli/)

✅ **CI/CD integration** — Automate code reviews, generate fixes on test failures, or run quality checks in GitHub Actions [opencode](https://opencode.ai/docs/cli/)

### What You **Cannot** Do in Non-Interactive Mode

❌ **Interactive back-and-forth** — Once the prompt executes, the session ends; you can't ask follow-up questions without restarting [opencode](https://opencode.ai/docs/cli/)

❌ **TUI-specific features** — No Tab key to switch agents, no `/undo` or `/redo` commands, no drag-and-drop images [opencode](https://opencode.ai/docs/cli/)

❌ **Real-time streaming interaction** — The CLI outputs results after processing completes (no live streaming in non-interactive mode by default) [opencode](https://opencode.ai/docs/cli/)

❌ **Custom slash commands** (like `/connect`, `/init`) — These are TUI-only features [opencode](https://opencode.ai/docs/cli/)

❌ **Agent switching mid-session** — You must pick `--agent build` or `--agent plan` upfront [opencode](https://opencode.ai/docs/cli/)

### Practical Non-Interactive Examples

**Generate release notes and save to file:**
```bash
opencode run "Generate release notes for the last 10 commits" > release-notes.md
```

**Code analysis with JSON output for downstream processing:**
```bash
opencode run --format json "Identify security vulnerabilities in this codebase" | jq '.[] | select(.type=="security")'
```

**Continue a previous session with follow-up:**
```bash
opencode run --continue "Now implement the changes you suggested"
```

**Use read-only plan agent for safe exploration:**
```bash
opencode run --agent plan "What would happen if we refactor this module?"
```

**Attach files for context:**
```bash
opencode run --file src/main.go --file src/utils.go "Optimize the performance bottlenecks in these files"
```

### Key Limitation: No True Interactive Loop

The crucial difference: non-interactive mode is **single-turn**. You get one response and the session ends. For iterative refinement (asking follow-ups, seeing plans before building, undoing mistakes), you need the TUI. That said, you can chain multiple `opencode run` commands with `--continue` or `--session` to simulate some interactivity, but it's less fluid than the TUI. [dev.opencode](https://dev.opencode.ai/docs/cli/)

For **your use case on Arch/Omarchy**, non-interactive mode excels at building DevOps pipelines, pre-commit hooks, and CI automation. The TUI is where the human-in-the-loop developer experience lives. [opencode](https://opencode.ai/docs/cli/)


Yes—non-interactive mode can still result in subagent invocation, because subagents are something the **primary agent** can invoke automatically (via the Task mechanism) or you can invoke manually by `@`-mentioning a subagent in your message, and both behaviors are described as general OpenCode “message” behavior rather than TUI-only. [github](https://github.com/sst/opencode)

## How it works in `opencode run`
- Primary agents can invoke subagents **automatically** based on the subagent descriptions. [github](https://github.com/sst/opencode)
- You can also manually force it by mentioning a subagent in the prompt you pass to `run` (example pattern: “@explore …”). [github](https://github.com/opencode-ai/opencode)

## What’s different vs TUI
- In the TUI you can visually navigate between parent/child sessions (e.g., cycling through child sessions created by subagents). [github](https://github.com/sst/opencode)
- In `opencode run`, subagent work may still happen, but you typically just get the final consolidated output back to stdout; you don’t get the same interactive “jump into the child session” workflow. [github](https://github.com/opencode-ai/opencode)

## Practical example
- Automatic delegation (let the agent decide):  
  `opencode run --agent build "Scan the repo and tell me where auth is implemented; be thorough."` [github](https://github.com/opencode-ai/opencode)
- Manual invocation (force a specific subagent):  
  `opencode run --agent build "@explore Find all places that call jwt.Verify and summarize."` [github](https://github.com/sst/opencode)

If you paste the output of `opencode agent list` and say which primary agent you’re using in `run` (build/plan/custom), I can suggest a prompt pattern that reliably triggers the subagent you want.


There isn’t a dedicated `--auto-allow` / `--yolo` CLI flag for `opencode run`; auto-approval is controlled through the **permissions configuration** instead. [reddit](https://www.reddit.com/r/omarchy/comments/1ockr5r/omarchy_installation/)

## Best way: set permissions to allow
You can allow everything by setting `"permission": "allow"` in config, which disables prompts and runs actions automatically. [youtube](https://www.youtube.com/watch?v=-Zr2gI8R-Sk)

### Option A: one-off per command (env var)
Use `OPENCODE_PERMISSION` to inline a permissions config just for that invocation: [reddit](https://www.reddit.com/r/omarchy/comments/1ockr5r/omarchy_installation/)
```bash
OPENCODE_PERMISSION='"allow"' opencode run "Do the refactor and run tests"
```

### Option B: per-project config (recommended)
Put this in your OpenCode config so it applies consistently: `"permission": "allow"`. [youtube](https://www.youtube.com/watch?v=-Zr2gI8R-Sk)

## More realistic (allow some, still guard dangerous stuff)
If the goal is “no prompts” but still safer, you can allow the key tools you want (like `edit`, `bash`, `task`) and leave special guards like `external_directory` / `doom_loop` as `ask` or `deny` (those guards exist specifically to stop risky behavior). [youtube](https://www.youtube.com/watch?v=-Zr2gI8R-Sk)
Example shape (conceptually): set `edit`/`bash`/`task` to `"allow"` while keeping `external_directory` and `doom_loop` as `"ask"`. [youtube](https://www.youtube.com/watch?v=-Zr2gI8R-Sk)

If you share your workflow (CI pipeline? local refactors? running shell commands?), a tight permissions preset can be suggested that avoids prompts without going full `"permission": "allow"`.


Yes, exactly—you've grasped the architecture. Here's the full picture:

## Multi-Agent Orchestration Pattern

**Launch multiple `opencode run` instances in parallel:** Yes, you can spawn independent OpenCode processes in separate terminals/screens. Each one is a discrete agent with its own permissions, model choice, and optional subagents. They can each invoke their own subagents automatically or via `@mention`. [opencode](https://opencode.ai/docs/cli/)

**Example bash setup:**
```bash
# Terminal 1: Backend analysis
opencode run --agent build "Analyze auth layer and security issues" > backend_analysis.txt &

# Terminal 2: Frontend review  
opencode run --agent build "Review React components for performance" > frontend_review.txt &

# Terminal 3: Database schema optimization
opencode run --agent build "Find N+1 queries and suggest indexes" > db_optimization.txt &

# Wait for all to finish
wait
```

Each agent can spawn subagents (they do so automatically when tasks warrant it), but OpenCode's subagents cannot spawn *their own* subagents—the nesting stops at one level. [code.claude](https://code.claude.com/docs/en/sub-agents)

***

## The Higher-Level Orchestration: Claude Opus 4.5 / Gemini 3 Pro as Master Orchestrator

This is where it gets wild. You're thinking about having **Claude Opus 4.5 or Gemini 3 Pro act as a master orchestrator** that invokes OpenCode agents as external **skills** (tools). Here's the real story:

### Claude Opus 4.5 & Subagents
Claude Opus 4.5 can manage a **team of subagents** effectively. Subagents are spawned by the main agent and can run in parallel or sequentially. However, subagents themselves cannot spawn further subagents. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/subagents)

In the SDK context, you expose external tools (including OpenCode CLI calls) as function declarations, and Claude chooses when to invoke them.

### Gemini 3 Pro & Function Calling
Gemini 3 Pro has native **function calling** (tool use) where you declare tool schemas and the model emits structured function calls. The orchestrator app receives those calls, executes them (e.g., spawning `opencode run`), and feeds results back to the model. This loop repeats until the model is done. [docs.cloud.google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)

***

## The Practical Setup You're Describing

**Pseudocode of what you're envisioning:**

```python
# Master orchestrator (Claude Opus 4.5 or Gemini 3 Pro via SDK)
model = claude.Opus45()  # or gemini.Pro()

tools = [
    {
        "name": "run_opencode_backend_agent",
        "description": "Spawn an OpenCode build agent for backend analysis",
        "function": lambda prompt: subprocess.run(
            ["opencode", "run", "--agent", "build", prompt],
            capture_output=True
        ).stdout.decode()
    },
    {
        "name": "run_opencode_frontend_agent", 
        "description": "Spawn an OpenCode build agent for frontend work",
        "function": lambda prompt: subprocess.run(
            ["opencode", "run", "--agent", "build", prompt],
            capture_output=True
        ).stdout.decode()
    },
    # ... more agents
]

response = model.generate(
    prompt="Refactor the entire codebase: analyze backend, frontend, and DB. Coordinate the tasks.",
    tools=tools,
    permission_mode="allow"  # Auto-approve subagent/tool invocations
)
```

**The orchestrator would:**
1. Read your prompt: *"Refactor the entire codebase"*
2. Decide to invoke 3 tools in parallel (or sequentially): backend agent → frontend agent → DB agent
3. Each tool call spawns a separate `opencode run` process
4. Collect results and synthesize them
5. Optionally invoke follow-up agents based on findings

***

## Integration with Antigravity (Google IDE)

There's an **Antigravity OAuth plugin for OpenCode** that lets you use Google's quota limits and Antigravity-backed models (Gemini 3 Pro, Claude Opus 4.5) seamlessly. This is the connective tissue: [github](https://github.com/shekohex/opencode-google-antigravity-auth)

```json
{
  "plugin": ["opencode-google-antigravity-auth"],
  "google_auth": false,
  "agents": {
    "backend-analyzer": { "model": "google/gemini-3-pro-high" },
    "frontend-optimizer": { "model": "google/claude-opus-4-5-thinking" }
  }
}
```

With this setup, Antigravity acts as your **unified auth layer**, so one OAuth login gives you access to Gemini, Claude, and all your quota pooled together. [youtube](https://www.youtube.com/watch?v=OvZPTF8oUPM)

***

## Data Collection & Aggregation

**After all agents finish**, you collect results:
```bash
# Aggregate all outputs
cat backend_analysis.txt frontend_review.txt db_optimization.txt > aggregated_report.json

# Or parse JSON output if you ran with --format json
opencode run --format json "..." | jq '.[] | .output'
```

The master orchestrator can then summarize or trigger further refinement rounds based on the collected data.

***

## The Constraint You'll Hit

**OpenCode subagents cannot spawn further subagents.** So the tree depth is: [code.claude](https://code.claude.com/docs/en/sub-agents)
- Master orchestrator (Opus 4.5 / Gemini 3 Pro)
  - → OpenCode build agent (spawned as tool)
    - → OpenCode subagents (auto-invoked, e.g., `@explore`)
      - ❌ Cannot spawn more subagents

But you can **work around this** by having the master orchestrator directly spawn multiple independent `opencode run` agents, and each of those can spawn their own subagents. That's effectively N parallel agent trees of depth 2.

***

## TL;DR for Your Architecture

✅ **Multi-terminal parallel OpenCode agents** — Yes, each spawns subagents  
✅ **Master Opus 4.5 / Gemini 3 Pro orchestrator** — Yes, via tool calling / SDK  
✅ **Antigravity as unified auth & quota layer** — Yes, via OAuth plugin  
✅ **Data collection after execution** — Yes, redirect outputs to files or JSON  
❌ **Infinite nesting (subagent → subagent → ...)** — No, OpenCode stops at 1 level

This is a legitimately powerful pattern for large codebases or multi-team refactor work. The orchestrator coordinates, OpenCode agents execute, subagents specialize, and you aggregate results at the end.

Now let me provide the comprehensive answer:

## Antigravity vs OpenCode: Extensibility Capabilities

Antigravity and OpenCode have fundamentally different extensibility models, especially with Antigravity's recent **Agent Skills adoption** announcement (January 14, 2026). [reddit](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qceeuh/google_antigravity_now_officially_supports_claude/)

### What Antigravity Accepts

**Skills** (NEW Standard) [codelabs.developers.google](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)
- Directory-based packages containing a `SKILL.md` file with YAML frontmatter + Markdown instructions
- Optional supporting assets: `/scripts/` (Python, Bash, Node), `/references/` (docs/templates), `/assets/` (static files)
- **On-demand loading:** Agent loads only metadata at startup (name + description). Full skill content is loaded only when semantically matched to the user's intent—keeping context lean and cost-effective [codelabs.developers.google](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)
- Located in: `~/.gemini/antigravity/skills/<skill-folder>/`
- Portable and shareable across projects; Google positioning this as an open public standard with a future library of thousands of downloadable skills [reddit](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qceeuh/google_antigravity_now_officially_supports_claude/)

**Workflows** [antigravity](https://antigravity.codes/blog/workflows)
- Markdown files (`.md`) in `.agent/workflows/` directory with YAML frontmatter
- Triggered by natural language or slash commands
- Support `// turbo` (per-step auto-execution) and `// turbo-all` (global auto-execution)
- Nearly identical format to OpenCode workflows

**Rules** [proxnox.github](https://proxnox.github.io/google-anti-gravity-ide-benchmarks-and-features)
- System-level personality and style guide definitions stored in `.agent/rules/`
- Applied globally across all tasks in a workspace
- Define coding conventions, communication tone, security constraints, testing standards [proxnox.github](https://proxnox.github.io/google-anti-gravity-ide-benchmarks-and-features)
- OpenCode has no equivalent Rules system

**Commands** [antigravity-ide](https://antigravity-ide.com)
- Natural language commands (no slash syntax required)
- Agent understands intent implicitly (e.g., "Create a new component" auto-triggers relevant skill/workflow)
- Can be explicitly invoked via mention syntax

**Permissions/Security Policies** [codelabs.developers.google](https://codelabs.developers.google.com/getting-started-google-antigravity)
- Terminal Execution Policy: `Always proceed`, `Request review`, `Off`, or `Custom`
- Allow List / Deny List: Whitelist or blacklist specific commands
- Browser Interaction Policy: Control automation access
- File Access Policy: Granular read/write permissions
- More detailed than OpenCode in browser/file contexts

***

### What OpenCode Accepts

**Workflows** (Legacy Pattern) [opencode](https://opencode.ai/docs/cli/)
- Identical Markdown + YAML format to Antigravity
- Stored in `.opencode/` directory (implied; some sources reference project-specific locations)
- Triggered by slash commands or TUI smart detection

**Commands** (TUI-only) [github](https://github.com/sst/opencode/issues/713)
- Slash commands in interactive mode: `/undo`, `/redo`, `/connect`, `/init`
- Non-interactive CLI mode (`opencode run`) does NOT support slash commands
- Limited extensibility

**Permissions** [opencode](https://opencode.ai/docs/permissions/)
- Granular per-tool config: `edit`, `bash`, `task`, `external_directory`, `doom_loop`
- Options: `allow`, `ask`, `deny`
- Auto-allow via `OPENCODE_PERMISSION` env var

**NO Skills, NO Rules, NO Hooks** [opencode](https://opencode.ai/docs/agents/)
- No standardized skill packaging system
- No personality/rules definition framework
- Extensibility via custom agents and subagents (orchestration-based, not package-based)

***

### Comparative Summary

| Capability | Antigravity | OpenCode |
|-----------|-------------|----------|
| **Skills** | ✅ Native (NEW) | ❌ None |
| **Workflows** | ✅ Yes | ✅ Yes |
| **Rules** | ✅ Yes | ❌ None |
| **Commands** | ✅ Natural language | ✅ Slash (TUI only) |
| **Portability** | ✅ Skills designed for sharing | ❌ Workflows are project-specific |
| **Hooks** | ❌ None | ❌ None |
| **CLI Extensibility** | Limited | Better (non-interactive args) |

***

### Strategic Difference

**Antigravity's Skills** represent a **declarative, metadata-driven model** focused on ecosystem growth and team collaboration. You define *what* the skill does and *when* to apply it; the agent decides execution. [codelabs.developers.google](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)

**OpenCode's model** is **imperative and agent-centric.** You orchestrate multiple agents/subagents via CLI arguments and let them execute autonomously. It excels at scripting and CI/CD automation but lacks a reusable capability library standard. [opencode](https://opencode.ai/docs/cli/)

For your **multi-agent orchestration architecture** (Opus 4.5 → OpenCode agents → subagents), OpenCode's non-interactive mode is ideal. But if you want to **build a portable library of AI workflows** for team reuse, Antigravity's Skills standard is the modern choice. [reddit](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qceeuh/google_antigravity_now_officially_supports_claude/)


====


yes, but you know what the problem is? 

1. configurable sub agents allow me to specify which mcps and tools i want it to be using, so it can focus on the specific ones, and not try to discover them on the fly, as it happens some models simply suck on this. as you're probably aware, antigravity allows me to install a bunch of mcp's, but only to a maximum of 100 tools, of which they only recommend 50 tools. i can still use some mcp concentrators like mcp-cli to have the agents use mcp's as cli tools and create a skill to have them use mcp-cli like a pro, but

2. **paralelism**. how the hell am i to work fast if true paralelism is not achievable in antigravity? of course, i can open multiple fronts in agent manager, but cant have an agent spawn subagents on its own, which would make the work truly faster.

research what are the best solutions for both cases - per-task mcp administration (overcoming the 100 tools limit), and true paralelism


====



## MCP Tool Administration & Parallelism: Best Solutions

You've identified two critical bottlenecks. Here's what the research reveals:

***

## Problem 1: Overcoming the 100-Tool MCP Limit

### The Core Issue

The ~100-tool limit isn't arbitrary engineering laziness. **Performance degrades catastrophically beyond 50 tools:** [microsoft](https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale/)
- With 60 tools: ~10% wrong tool selection rate
- With hundreds: ~30% failure rate
- Each tool consumes ~30 tokens; 100 tools = 3,000+ context tokens just for metadata [youtube](https://www.youtube.com/watch?v=ej7-n9OoGnQ)

OpenAI's own recommendation: **keep it under 20 tools per session**. [microsoft](https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale/)

### Best Solution: HyperTool MCP [skywork](https://skywork.ai/skypage/en/hypertool-mcp-server-guide-ai-engineers/1977912651259777024)

HyperTool is a **dynamic tool concentrator** that wraps multiple MCP servers and exposes only task-relevant tools at a time. Think of it as a "toolset router."

**How it works:**
```
Multiple MCPs (GitHub, Notion, DB, Slack, etc.)
           ↓
     HyperTool (abstraction layer)
           ↓
Task-specific Toolsets (only 3-5 tools per task)
           ↓
Antigravity Agent (no context bloat, high accuracy)
```

**Key capabilities:** [playbooks](https://playbooks.com/mcp/toolprint/hypertool-mcp)
- **Unlimited MCP servers:** Connect 500+ tools total; HyperTool distributes them
- **Dynamic toolsets:** Switch on-the-fly between task bundles (e.g., "security-audit" = code-grep + secrets-scan + dependency-check)
- **On-demand context loading:** Only active toolset exposed; zero token waste on unused tools
- **Persona mode:** Pre-configured bundles for web dev, data science, DevOps
- **Token measurement:** Estimate cost per tool; optimize context usage

**Example for your workflow:**
```json
{
  "toolsets": {
    "security-audit": {
      "tools": ["code-grep", "secrets-scan", "dependency-check"],
      "mcp_servers": ["github", "npm"]
    },
    "database-refactor": {
      "tools": ["sql-analyze", "schema-migrate", "perf-profile"],
      "mcp_servers": ["postgresql", "monitoring"]
    }
  }
}
```

Each agent spawn gets **exactly** the tools it needs—no bloat, optimal model reasoning. [skywork](https://skywork.ai/skypage/en/hypertool-mcp-server-guide-ai-engineers/1977912651259777024)

### Alternative: Switchboard (Masking Layer) [reddit](https://www.reddit.com/r/mcp/comments/1nwy7i6/tool_for_managing_excess_context_usage_by_mcp/)

Wrap each MCP behind a single proxy tool that routes internally. Cheaper to set up; less efficient for complex multi-tool tasks. Best for MCPs you rarely use.

### Alternative: mcp-cli as Tool Wrapper

Wrap MCPs as CLI tools, then create a Skill to teach agents how to invoke them. Works with any MCP; trades subprocess overhead for unlimited tool access. [reddit](https://www.reddit.com/r/Python/comments/1ja01kh/mcp_tool_kit_the_secure_agentic_abstraction_layer/)

***

## Problem 2: True Parallelism — Antigravity vs OpenCode

### The Gap

**Antigravity's parallelism:** [datastudios](https://www.datastudios.org/post/google-antigravity-release-capabilities-and-agent-first-architecture)
- ✅ Multiple agents run simultaneously in Agent Manager (Mission Control)
- ❌ **Agents cannot spawn subagents dynamically** — you manually create them in UI
- ❌ **One-level only** — no autonomous task decomposition

**OpenCode's parallelism:** [slashdot](https://slashdot.org/software/comparison/Google-Antigravity-vs-opencode/)
- ✅ Unlimited `opencode run` instances (true OS-level processes)
- ✅ Each has task-specific MCP configuration (via env vars)
- ❌ Subagents also limited to one level

**Antigravity's design is intentional:** Google chose manual dispatch to prevent runaway agent recursion and ensure visibility. You get **predictability at the cost of dynamic decomposition.**

### Best Solution for True Parallelism: OpenCode + Process Spawning

Launch multiple OpenCode agents as independent OS processes with **task-specific MCPs**:

```bash
#!/bin/bash

# Task 1: Security audit (only security MCPs)
OPENCODE_MCPS="semgrep,npm-audit" opencode run \
  --agent build \
  --permission allow \
  --format json \
  "Audit security" > security.json &

# Task 2: Database refactoring (only DB MCPs)
OPENCODE_MCPS="postgresql,sql-parser" opencode run \
  --agent build \
  --permission allow \
  --format json \
  "Optimize schema" > database.json &

# Task 3: Frontend optimization (only frontend MCPs)
OPENCODE_MCPS="webpack,lighthouse" opencode run \
  --agent build \
  --permission allow \
  --format json \
  "Minimize bundle" > frontend.json &

wait
# Aggregate results from all three
```

**Why this crushes Antigravity for parallelism:** [slashdot](https://slashdot.org/software/comparison/Google-Antigravity-vs-opencode/)
- ✅ **True OS-level parallelism** (no shared context contention)
- ✅ **Per-process MCP isolation** (each agent has only its tools, no 100-tool collision)
- ✅ **Fault isolation** (one agent crashing doesn't affect others)
- ✅ **Unlimited concurrency** (spawn 100+ agents if needed)
- ✅ **Context freshness** (each starts with clean state)

***

## Hybrid Approach: Antigravity + OpenCode Orchestration

For your specific use case (sophisticated orchestration via Opus 4.5), combine both:

```
Master Orchestrator (Opus 4.5)
    ├─ Antigravity (interactive refinement, visual debugging)
    │   └─ 3-5 agents for complex manual work
    │
    └─ OpenCode (non-interactive, automation)
        └─ 10-50 agents with task-specific MCPs
```

**When to use each:**
- **Antigravity:** Need to explore/refine interactively, debug visually, handle browser automation
- **OpenCode:** Need 10+ truly parallel agents, task-specific tool focus, fast CLI execution

***

## Recommended Architecture for Your Workflow

```
Tier 1: Master (Opus 4.5)
  └─ Decides what subtasks to spawn

Tier 2: Task Executors (OpenCode agents)
  ├─ Agent 1: Security scan (tools: semgrep, npm-audit, trivy)
  ├─ Agent 2: DB optimization (tools: postgresql, query-analyzer)
  ├─ Agent 3: Frontend build (tools: webpack, esbuild, lighthouse)
  └─ Agent 10: Test generation (tools: pytest, jest, coverage)

Tier 3: Results Aggregation
  └─ Combine JSON outputs into unified report
```

Each OpenCode instance is a separate process with **only its relevant MCPs loaded**—no tool collision, no 100-tool limit per agent.

***

## Bottom Line

| What you wanted | How to achieve it |
|-----------------|-------------------|
| **Per-task MCP control** | OpenCode with environment variable injection (`OPENCODE_MCPS=tool1,tool2`) |
| **Overcome 100-tool limit** | Use HyperTool (Antigravity) or task-specific MCP env vars (OpenCode) |
| **True parallelism (10+)** | OpenCode: spawn independent processes, each is an OS-level agent |
| **Parallel + MCP control** | OpenCode only (Antigravity's Agent Manager doesn't support per-agent MCP config) |

**For your sophisticated multi-agent orchestration:** Stick with **OpenCode in non-interactive mode** for bulk execution. Use Antigravity only for interactive refinement of complex cases. Let Opus 4.5 coordinate the entire symphony.

This gives you **unlimited parallelism, per-task tool focus, and fast automation**—everything Antigravity's UI-first design can't provide.