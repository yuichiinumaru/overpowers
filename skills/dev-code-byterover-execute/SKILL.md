---
name: byterover-execute
description: "Execute a phase plan task by task with verification. Loads the plan from the knowledge base, implements each task sequentially, verifies against success criteria, records progress, and transitions to the next phase. Stores execution results via brv curate."
---

# ByteRover Phase Execution

A structured workflow for executing implementation plans created by `byterover-plan`. Works through tasks sequentially, verifies each one, tracks progress in the knowledge base, and validates the phase goal before transitioning to the next phase.

## When to Use

- After creating a plan with `byterover-plan` and ready to implement
- When `byterover-progress` routes you to execute a planned phase
- To resume execution of a partially completed phase
- When you need structured task tracking with verification

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

A plan must exist in the knowledge base (created via `byterover-plan`). If no plan is found, recommend running `byterover-plan` first.

## Process

### Phase 1: Load Phase Context

Query the knowledge base for the plan and all relevant context:

```bash
brv query "What is the implementation plan for the current phase?"
brv query "What tasks have been completed in the current phase?"
brv query "What are the success criteria for the current phase?"
brv query "What implementation decisions were made for this phase?"
brv query "What conventions and patterns should be followed?"
```

Present phase overview to the user:

```
Phase [N]: [Name]
Goal: [from roadmap]
Tasks: [X] of [Y] complete
Success criteria:
- [criterion 1]
- [criterion 2]
```

If tasks were previously completed, show which ones and start from the next incomplete task.

### Phase 2: Execute Tasks

For each task in the plan (sequentially):

**1. Describe** — Tell the user what you are about to implement and why

**2. Implement** — Use standard tools (Read, Write, Edit, Bash, Glob, Grep) to:
- Create or modify the specified files
- Follow patterns and conventions from the knowledge base
- Reference implementation decisions from Phase 1

**3. Verify** — Prove the task is complete:
- Run the verification step specified in the plan (test, build, behavior check)
- If verification fails, debug and fix before moving on

**4. Commit** — Create an atomic git commit for the task:
```bash
git add [specific files]
git commit -m "feat(phase-[N]): [task description]"
```

**5. Record** — Store task completion in the knowledge base:
```bash
brv curate "Phase [N] task [X] complete: [task name]. Files: [modified files]. Verification: [result]" -f [modified files, max 5]
```

After each task, briefly report progress: "[X]/[Y] tasks complete. Next: [next task name]"

### Phase 3: Verify Phase Goal

After all tasks are complete, verify the phase goal was achieved:

```bash
brv query "What are the success criteria for phase [N]?"
```

For each success criterion:
1. Check if the criterion is observably true (read files, run tests, check behavior)
2. Record the result: **PASS**, **FAIL**, or **NEEDS HUMAN TESTING**

Present verification report:

```
Phase [N] Verification:
- [Criterion 1]: PASS
- [Criterion 2]: PASS
- [Criterion 3]: NEEDS HUMAN TESTING — [what to check manually]
```

If any criterion fails:
- Describe what is missing or broken
- Ask the user whether to create fix tasks or defer to the next phase

### Phase 4: Phase Summary and Transition

Store the phase summary in the knowledge base:

```bash
brv curate "Phase [N] [Name] COMPLETE. Goal achieved: [yes/partial]. Tasks: [X] completed. Key accomplishments: [list]. Decisions made: [list]. Issues encountered: [list]" -f [key files, max 5]
```

Update project status for the next phase:

```bash
brv curate "Project status: Phase [N] complete. Next: Phase [N+1] — [name] — [goal]. Milestone progress: [N/Total] phases done" -f [key files]
```

If requirements were addressed, mark them:

```bash
brv curate "Requirements [REQ-IDs] addressed by Phase [N]. Status: implemented and verified" -f [key files]
```

### Completion

Present to the user:

1. **Accomplishments** — What was built in this phase
2. **Verification** — Which criteria passed, which need human testing
3. **Next phase** — Name, goal, and recommendation to run `byterover-plan`
4. **Milestone progress** — [N/Total] phases complete

## Important Rules

1. **One task at a time** — Complete and verify each task before starting the next
2. **Atomic commits** — One commit per task with a descriptive message
3. **Verify against criteria** — Check success criteria, not just task completion
4. **Record everything** — Curate task completions, phase summaries, and decisions
5. **Report gaps honestly** — If a criterion fails, report it, do not fake a pass
6. **Follow the plan** — Implement what the plan specifies, raise concerns before deviating
7. **Max 5 files per curate** — Break down task and phase summaries
8. **Never read secrets** — Skip `.env`, credential files, and similar
9. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
