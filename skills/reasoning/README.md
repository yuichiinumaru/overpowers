# Reasoning Skills

Agent reasoning and architecture patterns for building sophisticated AI systems.

## Overview

This collection covers advanced patterns for agent reasoning, planning, and cognitive architecture:

- **BDI (Belief-Desire-Intention)**: Formal cognitive architecture patterns
- **Planning**: File-based planning systems for complex tasks
- **Hosted Agents**: Infrastructure for sandboxed agent execution

## Skills

### bdi-mental-states
> **Status**: Optional/Experimental

Transform external RDF context into agent mental states using formal BDI ontology patterns. Enables agents to reason through cognitive architecture with:
- Belief formation from perception
- Desire generation from beliefs
- Intention commitment and planning
- Traceable reasoning chains for explainability

**Use when**: Implementing formal cognitive structures, neuro-symbolic AI integration, or multi-agent coordination with shared mental state models.

### hosted-agents

Infrastructure patterns for running agents in remote sandboxed environments. Covers:
- Pre-built environment images with warm pool strategies
- Session-isolated state management
- Multiplayer collaboration support
- Self-spawning sub-agent patterns

**Use when**: Building background coding agents, sandboxed execution environments, or multi-client agent interfaces.

### planning-with-files

Manus-style file-based planning for complex multi-step tasks. Creates persistent markdown files (`task_plan.md`, `findings.md`, `progress.md`) as "working memory on disk":
- Phase tracking with status updates
- Research findings capture
- Error logging and resolution tracking
- Session continuity across context limits

**Use when**: Complex tasks requiring 5+ tool calls, research projects, or any work requiring persistent state.

## Integration

These skills work together with:
- **context-engineering/** - Context management for agent sessions
- **swarm-orchestration** - Multi-agent coordination patterns
- **agentdb-memory-patterns** - Persistent memory systems

## Source

Adopted from `guanyang-antigravity-skills` agent reasoning collection with patterns from:
- BDI ontology research (Zuppiroli et al., 2025)
- Manus planning methodology
- Ramp's background agent architecture
