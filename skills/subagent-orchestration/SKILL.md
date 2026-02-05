---
name: subagent-orchestration
description: Launch parallel subagents via OpenCode CLI for distributed task execution
---

# Subagent Orchestration Skill

Launch multiple OpenCode subagents in parallel to distribute complex tasks across specialized agents.

## Key Discovery

- **OpenCode `run` command** works in non-interactive mode with `OPENCODE_PERMISSION='"allow"'`
- **Restriction**: Cannot access OpenCode's own config directory (`.config/opencode`)
- **Works from**: Any regular directory (e.g., `/home/user/work`, `/tmp`)
- **Architecture**: Antigravity → OpenCode → Subagents → (optional) More Subagents

## Quick Start

```bash
# From any NON-config directory
cd /home/sephiroth/work

# Single subagent
OPENCODE_PERMISSION='"allow"' opencode run "Your task here" --model google/antigravity-claude-sonnet-4-5-thinking

# Using the orchestrator script
./scripts/run-subagent.sh "Analyze this codebase" output.md
```

## Scripts Available

| Script | Purpose |
|--------|---------|
| `run-subagent.sh` | Run single subagent with auto-permissions |
| `parallel-tasks.sh` | Run multiple subagents in parallel |
| `batch-analyze.sh` | Analyze multiple directories/repos |

## Usage Patterns

### Pattern 1: Single Task Delegation

```bash
./scripts/run-subagent.sh "Refactor the auth module for better security" result.md
```

### Pattern 2: Parallel Analysis

```bash
./scripts/parallel-tasks.sh tasks.txt results/
```

Where `tasks.txt` contains:
```
Analyze backend/ for security vulnerabilities
Review frontend/ for performance issues  
Check database/ for N+1 queries
```

### Pattern 3: Multi-Repo Scanning

```bash
./scripts/batch-analyze.sh /path/to/repos/*.git reports/
```

## Important Constraints

> [!CAUTION]
> **DO NOT run from `.config/opencode/` directory** - subagents cannot access this path in non-interactive mode.

> [!TIP]
> Copy scripts to your working directory or run from `/home/$USER/work` or similar.

## Model Selection

| Use Case | Recommended Model |
|----------|-------------------|
| Fast analysis | `google/antigravity-claude-sonnet-4-5-thinking` |
| Complex reasoning | `google/antigravity-claude-opus-4-5-thinking` |
| Code generation | `google/antigravity-claude-sonnet-4-5-thinking` |

## Environment Variables

```bash
export OPENCODE_PERMISSION='"allow"'  # Required for non-interactive
export SUBAGENT_MODEL="google/antigravity-claude-sonnet-4-5-thinking"
export SUBAGENT_TIMEOUT=300  # 5 minutes max per task
```

## Integration with Antigravity

This skill works in Antigravity IDE! From Antigravity, you can:

1. Call these scripts via terminal
2. Delegate tasks to OpenCode subagents
3. Collect results back into your session

```
Antigravity (Master)
    └── OpenCode Agent 1 → Subagent A
    └── OpenCode Agent 2 → Subagent B  
    └── OpenCode Agent 3 → Subagent C
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "ruleset validation error" | Run from non-config directory |
| "permission denied" | Ensure `OPENCODE_PERMISSION` is set |
| Empty output | Check model availability with `opencode status` |
| Timeout | Increase `SUBAGENT_TIMEOUT` or simplify task |
