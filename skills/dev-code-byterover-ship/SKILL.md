---
name: byterover-ship
description: "Complete milestones with retrospective and archival, or pause work with handoff context for seamless resumption. For shipping: gathers stats, extracts accomplishments, evolves the project record, and optionally creates a git tag. For pausing: compresses work state into a resumable handoff stored via brv curate."
---

# ByteRover Ship & Handoff

A structured workflow for wrapping up work — either completing a milestone (shipping) or pausing work mid-phase (handoff). Shipping produces a retrospective with stats and archives the milestone. Pausing compresses current state so a future session can resume seamlessly.

## When to Use

- All phases in a milestone are complete and ready to ship
- When `byterover-progress` indicates the milestone is ready for completion
- When you need to pause work mid-phase and resume later
- Before starting a new milestone cycle
- At the end of a sprint or development cycle

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

## Process

### Phase 1: Determine Intent

Ask the user: **"Are you completing a milestone (shipping) or pausing work (handoff)?"**

- **Ship** — Proceed to Phase 2 (Milestone Completion)
- **Pause** — Skip to Phase 5 (Work Handoff)

### Phase 2: Pre-Flight Audit (Ship Only)

Verify the milestone is ready to ship:

```bash
brv query "What is the current milestone, its requirements, and roadmap?"
brv query "What phases have been completed and their summaries?"
brv query "What pending items or unresolved concerns exist?"
```

Check readiness:
- All phases in the milestone are marked complete
- No critical pending items remain
- Run project tests if applicable (`npm test`, `pytest`, etc.)

Present pre-flight summary:

```
Pre-flight check for Milestone v[X.Y]:
- Phases: [N/N] complete
- Requirements: [M/M] covered
- Pending items: [count]
- Tests: [pass/fail/not run]
```

If not ready, present blockers and suggest which phases or items to address first.

### Phase 3: Retrospective and Stats (Ship Only)

Gather milestone statistics:

```bash
git log --oneline --since="[milestone start date]" | wc -l
git diff --stat $(git log --oneline --since="[milestone start date]" --reverse | head -1 | cut -d' ' -f1)..HEAD | tail -1
```

Extract accomplishments from phase knowledge:

```bash
brv query "What were the key accomplishments for each phase in milestone v[X.Y]?"
```

Present retrospective:

```
Milestone v[X.Y] Retrospective:
- Phases: [X]
- Commits: [N]
- Files changed: [M]
- Key accomplishments:
  1. [from phase summaries]
  2. [from phase summaries]
  3. [from phase summaries]
```

### Phase 4: Project Evolution and Archival (Ship Only)

Review and evolve the project record:

1. **Requirements migration** — Move shipped MVP requirements to "Validated"
2. **Project description** — Update if the product has meaningfully changed
3. **Tech debt** — Note any known issues or deferred work for the next milestone
4. **Key decisions** — Record architectural decisions and their outcomes

Store the milestone record:

```bash
brv curate "Milestone v[X.Y] [Name] COMPLETED. Shipped: [accomplishments]. Phases: [N]. Stats: [commits, files]. Requirements validated: [REQ-IDs]. Tech debt carried: [items]" -f [key files]
brv curate "Project status: Milestone v[X.Y] shipped. Next: define next milestone using byterover-milestone. Deferred requirements: [list]" -f [key files]
```

Optionally create a git tag (ask user first):

```bash
git tag -a v[X.Y] -m "Milestone v[X.Y] [Name] — [one-line summary]"
```

### Phase 5: Work Handoff (Pause Only)

Gather the current work state from the user:

- **Position** — Which phase and task are you on?
- **Completed** — What has been done this session?
- **Remaining** — What still needs to be done?
- **Decisions** — Key decisions made during this session
- **Blockers** — Any issues preventing progress
- **Next action** — What specific step should be taken when resuming

Compress into a handoff and store:

```bash
brv curate "WORK PAUSED. Phase: [N] — [name]. Task: [X] of [Y]. Completed: [list]. Remaining: [list]. Decisions: [list]. Blockers: [list]. Next action: [specific first step when resuming]" -f [modified files, max 5]
```

### Completion

**For Ship:**
```
Milestone v[X.Y] [Name] shipped.
- [N] phases, [M] requirements validated
- Tagged: v[X.Y] (if tagged)
- Knowledge base updated with milestone record
- Next step: run byterover-milestone to plan the next milestone
```

**For Pause:**
```
Work paused at Phase [N], Task [X]/[Y].
- Handoff stored in knowledge base
- To resume: run byterover-progress
```

## Important Rules

1. **Verify before shipping** — All phases must be complete, tests should pass
2. **Accomplishments are specific** — "Implemented JWT auth with refresh tokens" not "Did auth"
3. **Track requirement status** — Move shipped requirements to Validated, note deferred ones
4. **Handoffs must be resumable** — Include enough context for a fresh agent to continue
5. **Git tags are optional** — Ask the user, do not force tagging
6. **Store milestone records permanently** — Curate with enough detail for future reference
7. **Max 5 files per curate** — Break down milestone summaries into multiple commands
8. **Never read secrets** — Skip `.env`, credential files, and similar
9. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
