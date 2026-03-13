# Task: 003-refactor-moltbot-memory

## Objective

Refactor Moltbot memory integration patterns based on planning analysis.

## Test Requirements

Memory persistence must survive session restarts and be queryable via AgentDB or equivalent.

## Exit Conditions (GDD/TDD)

- [ ] Review `docs/tasks/planning/moltbot-memory.md` for requirements.
- [ ] Implement or update memory persistence patterns.
- [ ] Verify cross-session memory retrieval works.

## Details

### What

Improve the memory subsystem used by Moltbot agents to ensure reliable persistence and retrieval.

### Where

Skills and services related to memory (`skills/memory-systems/`, `services/`).

### How

Align with patterns in `docs/tasks/planning/moltbot-memory.md` and existing AgentDB skills.

### Why

Reliable memory is critical for long-running agent sessions and multi-agent coordination.
