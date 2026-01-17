# Workflows Guide

Overpowers includes **16 multi-step workflows** that orchestrate complex development tasks by coordinating agents, skills, and scripts.

## What are Workflows?

Workflows are structured guides for accomplishing complex tasks. They define a sequence of steps, specify which agents and skills to use, and provide decision points for handling different scenarios.

## Available Workflows

### Development Workflows

| Workflow | Description |
|----------|-------------|
| `feature-development.md` | End-to-end feature implementation |
| `full-stack-feature.md` | Full-stack feature (DB, API, UI, tests) |
| `bug-fixing.md` | Systematic bug investigation and fix |
| `code-review.md` | Comprehensive code review process |
| `swarm-development.md` | Multi-agent parallel development |

### Release & Versioning

| Workflow | Description |
|----------|-------------|
| `release-process.md` | Complete release workflow |
| `release-improvements.md` | Post-release improvement cycle |
| `versioning.md` | Semantic versioning management |

### Research & Discovery

| Workflow | Description |
|----------|-------------|
| `research-to-product.md` | Transform research into features |
| `agent-discovery.md` | Navigate 390+ agents and 149 skills |

### Quality & Security

| Workflow | Description |
|----------|-------------|
| `security-hardening.md` | Security audit and hardening |
| `error-feedback.md` | Error analysis and resolution |

### Specialized Workflows

| Workflow | Description |
|----------|-------------|
| `jules-orchestration.md` | Jules Swarm parallel task coordination |
| `marketing-launch.md` | Product launch coordination |
| `legal-review.md` | Legal document review automation |
| `multi-repo-workspace.md` | Multi-repository management |

## Workflow Structure

Each workflow follows this format:

```markdown
---
name: workflow-name
description: Brief description of what this workflow accomplishes
---

# Workflow Name

## Overview
What this workflow does and when to use it.

## Prerequisites
- Required tools, agents, or skills
- Environment setup

## Steps

### Step 1: [Name]
- Actions to take
- Agents to invoke: `@agent-name`
- Skills to use: `use_skill Overpowers:skill-name`

### Step 2: [Name]
...

## Decision Points
- If X happens, do Y
- If Z happens, do W

## Verification
How to verify the workflow completed successfully.

## Related
- Links to related workflows, agents, or skills
```

## Using Workflows

### In OpenCode/Claude

Simply reference the workflow:

```
Follow the feature-development workflow for implementing user authentication.
```

Or load it explicitly:

```
Read and follow Overpowers/workflows/feature-development.md
```

### Workflow Invocation Patterns

**Sequential execution:**
```
1. Follow step 1 of the code-review workflow
2. Wait for my feedback
3. Continue with step 2
```

**Full automation:**
```
Execute the complete security-hardening workflow on this codebase.
```

**Partial execution:**
```
Run only the "Static Analysis" and "Dependency Scan" steps from security-hardening.
```

## Example: Feature Development Workflow

```markdown
## Steps

### 1. Requirements Analysis
- Review the feature request
- @comprehensive-researcher: Research similar implementations
- Document acceptance criteria

### 2. Design
- @architect-review: Propose architecture
- use_skill Overpowers:writing-plans
- Create implementation plan

### 3. Implementation
- @task-decomposition-expert: Break into subtasks
- Implement in TDD style
- use_skill Overpowers:test-driven-development

### 4. Review
- @code-reviewer: Review implementation
- @security-auditor: Security review
- Fix any issues found

### 5. Integration
- Run full test suite
- @deployment-engineer: Prepare deployment
- Merge and deploy
```

## Creating New Workflows

1. Create a new `.md` file in `workflows/`:

```markdown
---
name: my-workflow
description: What this workflow accomplishes
---

# My Workflow

## Overview
Describe the purpose and scope.

## Prerequisites
- List required tools and setup

## Steps

### Step 1: Initialize
- First action
- Second action

### Step 2: Execute
- Main workflow logic

### Step 3: Verify
- Verification steps

## Troubleshooting
Common issues and solutions.
```

2. Test the workflow manually first.

3. Refine based on actual usage.

## Best Practices

1. **Clear steps** - Each step should be actionable
2. **Specify agents** - Name which agents to use with `@mention`
3. **Reference skills** - Note relevant skills with `use_skill`
4. **Decision points** - Handle branching scenarios
5. **Verification** - Always end with how to verify success
6. **Keep it focused** - One workflow per objective
