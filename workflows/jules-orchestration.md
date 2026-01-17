# Jules Swarm Orchestration Workflow

Maximize output by running **parallel work streams** using Jules accounts with local agent coordination.

## Overview

This workflow leverages the Jules Swarm skill set to:
1. Dispatch work to multiple Jules accounts
2. Harvest and review all branches in parallel
3. Integrate the best work with proper attribution

## Prerequisites

- Multiple Jules accounts configured
- Jules Swarm skills installed:
  - `jules-dispatch`
  - `jules-harvest`
  - `jules-triage`
  - `jules-integrate`

## Workflow Steps

### 1. Task Preparation

```
/invoke task-decomposition-expert

Break work into Jules-compatible chunks:
- Each task should be 1-4 hours of work
- Clear acceptance criteria
- Minimal cross-dependencies
- Define verification steps
```

### 2. Dispatch Phase

```
/skill jules-dispatch

For each task:
1. Select optimal Jules account (rotation)
2. Prepare context-rich prompt
3. Submit with tracking ID
4. Log to .jules/tracking.md
```

**Dispatch Checklist:**
- [ ] Task clearly defined
- [ ] Repository context included
- [ ] Branch naming convention set
- [ ] Expected deliverables listed

### 3. Monitor & Harvest

Wait for Jules branches to be ready, then:

```
/skill jules-harvest

Actions:
1. Fetch all remote jules/* branches
2. Create local worktrees for each
3. Generate catalog at .jules/branches.md
4. Note completion status
```

### 4. Parallel Triage

Use local agents to review branches in parallel:

```
/skill jules-triage

For each branch:
- /invoke code-reviewer → Code quality
- /invoke security-auditor → Security check
- /invoke test-automator → Test coverage

Output: .jules/triage-report.md with ratings
```

**Triage Categories:**
| Grade | Action |
|-------|--------|
| A | Direct integration |
| B | Minor fixes needed |
| C | Needs rework |
| D | Reject |

### 5. Selective Integration

```
/skill jules-integrate

For Grade A/B branches:
1. Create integration branch
2. Cherry-pick or merge changes
3. Resolve conflicts
4. Add attribution comments
5. Run verification
```

### 6. Cleanup & Attribution

```
After integration:
- Delete completed worktrees
- Archive branch catalog
- Update changelog with Jules credits
- Push integrated changes
```

## Jules Account Rotation

Distribute work across accounts to maximize parallelism:

```
Account 1 → Infrastructure tasks
Account 2 → Feature work
Account 3 → Testing & documentation
```

## Related Skills

| Skill | Purpose |
|-------|---------|
| `jules-dispatch` | Send tasks |
| `jules-harvest` | Fetch branches |
| `jules-triage` | Rate branches |
| `jules-integrate` | Merge work |
| `swarm-orchestration` | Agent coordination |

## Directory Structure

```
.jules/
├── tracking.md      # Dispatched task tracking
├── branches.md      # Harvested branch catalog
├── triage-report.md # Quality ratings
├── worktrees/       # Local working copies
└── archive/         # Completed work logs
```

## Success Metrics

| Metric | Target |
|--------|--------|
| Parallel utilization | 3+ streams |
| Accept rate | >70% A/B grades |
| Integration conflicts | <10% |
| Turnaround time | <24h dispatch-to-merge |
