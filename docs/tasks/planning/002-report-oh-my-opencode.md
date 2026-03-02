# Oh My OpenCode Analysis Report

**Date:** 2026-01-19
**Source:** [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
**Version:** 3.0.0-beta.11

## Overview

`oh-my-opencode` is a comprehensive "batteries-included" plugin for OpenCode, heavily inspired by "Oh My Zsh". It transforms OpenCode into a powerful agentic IDE by introducing a multi-agent orchestration system led by "Sisyphus".

Unlike Overpowers, which is a collection of scripts and configs, `oh-my-opencode` is a **TypeScript plugin** that hooks deeply into the OpenCode runtime.

## Key Discoveries

### 1. Sisyphus Orchestration System
The core innovation is **Sisyphus**, an agent designed to be a "disciplined senior engineer".
- **Phase-Based Execution**: Sisyphus follows a strict 4-phase process (Intent Gate → Codebase Assessment → Exploration → Implementation).
- **Todo Enforcement**: Uses a `todo-continuation-enforcer` hook to prevent the agent from stopping halfway. If a todo list exists, the system forces the agent to continue until all items are checked.
- **Intent Classification**: Every user request is classified (Trivial, Refactoring, Build, etc.) to determine the strategy.

### 2. Specialized Agents
- **Prometheus (Planner)**: A "consultant" agent that *only* plans and *never* executes. It forces a clear separation of concerns.
- **Oracle (Advisor)**: A "high-IQ" read-only consultant for architectural decisions.
- **Librarian (Researcher)**: Specialized in finding external documentation and OSS examples.
- **Explore (Grep)**: Specialized in internal codebase search ("Contextual Grep").

### 3. Unique Features
- **Ralph Loop**: An infinite loop mechanism for tasks (similar to our `jules-swarm` but synchronous).
- **Interactive Bash**: A secure wrapper around `tmux` to allow agents to run interactive TUI apps (vim, htop) and persist sessions.
- **Context Injection**: Dynamically injects `AGENTS.md` and directory-specific READMEs into the context.

## Integration Actions

We have extracted and adapted the following components into Overpowers:

### Agents
- **`agents/sisyphus/sisyphus-orchestrator.md`**: A faithful recreation of the Sisyphus prompt logic, adapted for our markdown-based agent system.
- **`agents/prometheus/prometheus-planner.md`**: The planner persona.
- **`agents/oracle/oracle-consultant.md`**: The advisor persona.
- **`agents/explore/explore-grep.md`**: The internal search specialist.
- **`agents/librarian/librarian-researcher.md`**: The external research specialist.

### Tools
- **`commands/interactive/interactive-bash.md`**: A new command to expose `tmux` capabilities.
- **`scripts/devops/tmux-interactive.sh`**: A safe wrapper script for `tmux` that blocks dangerous commands (like `capture-pane` abuse), ported from the TypeScript implementation.

### MCPs
- Confirmed that `oh-my-opencode` uses:
  - **Exa** (Web Search)
  - **Context7** (Docs)
  - **Grep.app** (GitHub Code Search)
- These align with our existing `opencode-example.json` recommendations.

## Recommendations for Future

1.  **Todo Enforcer Implementation**: We should consider writing a Python script or OpenCode hook that replicates `todo-continuation-enforcer`. Currently, we only have the *prompt* instruction for Sisyphus to use todos, but no *system* enforcement.
2.  **Context Injection**: `oh-my-opencode` injects `AGENTS.md` dynamically. We rely on the user or the agent reading it. A script to auto-append relevant docs to the context window would be valuable.
3.  **Porting Ralph Loop**: The "infinite loop" concept is powerful. We could implement a `scripts/ralph-loop.sh` that calls `opencode` recursively until a condition is met.

## Conclusion

`oh-my-opencode` offers a sophisticated *runtime* approach to agent orchestration. Overpowers offers a *configuration* approach. By extracting the high-quality prompts and logic from `oh-my-opencode`, we have significantly upgraded our agent army's intelligence without introducing complex TypeScript dependencies.
