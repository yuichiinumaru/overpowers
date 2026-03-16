---
name: loop
description: "AI autonomous implementation methodology. Automatically applied when implementation/development/coding is requested. Main spawns a Mother sub-agent, and the Mother manages workers. specs/ → IMPLEMENTATION_PLAN.md → implement 1 task at a time → 2-stage review → test → repeat."
---

## Methodology Details

### Architecture

The **kj-ralph-loop** follows a hierarchical agent structure:

### Workflow

```
User Request
    │
    ▼
┌─────────┐
│  Main    │ ── spawns ──▶ ┌──────────┐
└─────────┘                │  Mother   │
                           └────┬─────┘
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
               ┌────────┐ ┌────────┐ ┌────────┐
               │Worker 1│ │Worker 2│ │Worker N│
               └────────┘ └────────┘ └────────┘
```

### Step-by-Step Process
---

# Ralph Loop v2

Geoffrey Huntley's AI Autonomous Development Methodology + Critical Absorption of Superpowers.

## Absorbed (from Superpowers)
- ✅ **2-Stage Review**: Spec Compliance → Code Quality (Previously: Mother directly verified without review)
- ✅ **Verification First**: Must confirm evidence of test execution before declaring "Done" (Previously: Trusted worker's self-report)
- ✅ **Systematic Debugging**: 3 failures trigger architecture re-evaluation (Previously: Infinite retries)
- ✅ **YAGNI Enforcement**: No implementation unless specified (Previously: Implicit)
- ✅ **Red Flags List**: Explicitly list antipatterns

## Not Absorbed (Critique)
- ❌ **Strict TDD Enforcement**: Overkill for HTML5 games/single-file tools. Our primary output is single HTML games/tools — TDD slows us down. Selectively applied only for complex projects (Rust/Godot).
- ❌ **Git Worktrees**: Unnecessary in OpenClaw environment. Sub-agents already isolate context.
- ❌ **Separate Code Review Sub-agent Spawn**: Prohibitive cost. Mother performs 2-stage review directly.
- ❌ **Brainstorming 200-300 word chunks**: We have Master instructions → immediate execution. Socratic questioning is unnecessary.
- ❌ **Claude Code Plugin Dependency**: Operates natively within OpenClaw.

## Core Principles

## Agent Structure

```
┌─────────────────────────────────────────────┐
│  Main Agent (Main)                        │
│  • Interacts with user                       │
│  • Spawns Ralph Loop Mother                 │
│  • Overall coordination and decision making  │
└──────────────────┬──────────────────────────┘
                   │ spawn (label: ralph-mother)
                   ▼
┌─────────────────────────────────────────────┐
│  Mother Agent (Mother)                      │
│  • Creates and manages specs/ folder          │
│  • Creates/updates IMPLEMENTATION_PLAN.md   │
│  • Spawns Worker sub-agents                 │
│  • Performs 🆕 2-Stage Review (Spec Compliance → Quality) |
│  • Reports progress to Main                 │
└──────────────────┬──────────────────────────┘
                   │ spawn (label: ralph-worker-N)
                   ▼
┌─────────────────────────────────────────────┐
│  Worker Agent (Worker)                      │
│  • Implements single task                    │
│  • Performs 🆕 Self-Verification (Tests/curl/browser) |
│  • Reports with verification evidence        │
│  • Reports result to Mother                 │
└─────────────────────────────────────────────┘
```

## Workflow

### Main Agent Role

When user requests implementation/development:
1. Understand and clarify requirements
3. Receive reports from Mother and relay progress to user
4. Make decisions and adjust direction as needed

### Mother Agent Role

With requirements passed during spawn:

**Phase 1: Define Requirements**
```
specs/
├── feature-a.md
├── feature-b.md
└── ...
```
- Write spec documents for each feature
- 1 topic = 1 file (should be explainable in a single sentence without "and")

**Phase 2: Planning**
```markdown
# IMPLEMENTATION_PLAN.md
## TODO
- [ ] Task 1 (Estimated 2-5 mins)
- [ ] Task 2 (Estimated 2-5 mins)
## DONE
- [x] Completed task ✅ Spec Compliance ✅ Quality
```
- Analyze gap between specs vs current code
- Prioritized task list
- 🆕 **Task Size**: 2-5 minute increments. Split if larger.

**Phase 3: Building (Iterative)**
```
1. Read IMPLEMENTATION_PLAN.md
2. Select highest priority task
3. Spawn Worker sub-agent (pass specific task + relevant specs)
4. Receive Worker completion report
5. 🆕 2-Stage Review:
   a) Verify Spec Compliance — Compare Worker output vs. specs
      - Are any requirements missing?
      - Did it add anything not in the specs? (YAGNI violation)
   b) Verify Quality — Code quality, error handling, edge cases
6. 🆕 Verify Evidence — Is there actual output for the "tests passed" claim?
7. If review passes → Update plan + commit
   If review fails → Instruct Worker to fix (same sub-agent)
8. Repeat for next task or report completion
```

### Worker Agent Role

Single task assigned by Mother:
1. Analyze specs and relevant code
2. Implement
3. 🆕 **Execute Verification and Collect Evidence**:
   - If tests exist → Run them and capture output
   - If web app → Verify with curl/browser
   - If CLI → Run and capture output
4. Report result to Mother (Success/Failure + **Evidence**)

## 🆕 Systematic Debugging Protocol

When bugs/errors/unexpected behavior occur:

### Phase 1: Root Cause Investigation (Mandatory before attempting fixes)
1. Read error message completely (including stack trace)
2. Verify reproducibility
3. Check recent changes (git diff)
4. Trace data flow

### Phase 2: Hypothesis and Minimal Test
1. Single Hypothesis: "X is the root cause because Y"
2. Verify hypothesis with minimal changes
3. Change one thing at a time

### Phase 3: 3-Strike Rule
- 3 failed attempts to fix the same issue → **Halt immediately**
- High likelihood of architectural/design problem
- Report to Mother → Mother escalates to Master
- **Never attempt a 4th patch**

## 🆕 Red Flags (Antipatterns — Halt Immediately)

| 🚫 Red Flag | ✅ Correct Action |
|-------------|---------------|
| "It'll probably work" | Execute verification and judge by results |
| "Just fix this" (3rd time) | Re-evaluate architecture |
| Declare "Done" without tests | Attach verification evidence |
| Add features not in specs | YAGNI — Implement only specs |
| Multiple fixes at once | One change at a time |
| Trust worker report alone | Verify evidence directly |
| "Test later" | Verify now or mark as incomplete |

## Project Scale Application

| Scale | TDD | 2-Stage Review | 3-Tier Structure |
|------|-----|-----------|------------|
| **Single HTML Game/Tool** | ❌ Unnecessary | ✅ Mother quickly | ⚠️ Mother only (Worker can be omitted) |
| **Multi-file Project** | ⚠️ Core logic only | ✅ Mandatory | ✅ Mandatory |
| **Rust/WASM/Godot** | ✅ Mandatory | ✅ Mandatory | ✅ Mandatory |

## Sub-agent Spawn Examples

**Main → Mother:**
```
label: ralph-mother
task: "Implement [summary of requirements]. Write specs/ → IMPLEMENTATION_PLAN.md → implement via worker → 2-stage review → report on completion"
```

**Mother → Worker:**
```
label: ralph-worker-1
task: "Task: [specific task]. Specs: [full text]. Execute verification after implementation, report with evidence."
```

## Context Management

- **Main**: Maintain minimal context (focus on user conversation)
- **Mother**: Track only overall plan and progress
- **Worker**: Focus solely on the single task (40-60% smart zone)
- 🆕 **Pass full specs to Worker** — Eliminate file reading overhead (Superpowers pattern)

## Detailed Guide

For complex projects, refer to [references/workflow.md](references/workflow.md).
