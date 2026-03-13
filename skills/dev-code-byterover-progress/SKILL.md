---
name: byterover-progress
description: "Check project progress, resume paused work, and route to the next action. Loads project state from the knowledge base, presents a status report, detects incomplete work or handoffs, and suggests the most logical next workflow to invoke."
---

# ByteRover Project Progress

A structured workflow for understanding where a project stands and what to do next. Loads all project state from the knowledge base, detects paused work or incomplete phases, and intelligently routes to the appropriate next action.

## When to Use

- Starting a new session and need to pick up where you left off
- After being away from a project and need to regain context
- When unsure what to work on next
- To check overall milestone progress and phase completion
- To review pending items or deferred ideas

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

## Process

### Phase 1: Load Project State

Query the knowledge base for complete project context:

```bash
brv query "What is the project definition and current milestone?"
brv query "What is the current project status and last activity?"
brv query "What is the project roadmap and phase completion status?"
brv query "Is there paused work, handoff context, or incomplete tasks to resume?"
brv query "What pending items, deferred ideas, or todos exist?"
```

If no project knowledge exists, inform the user and recommend running `byterover-milestone` to define a project.

### Phase 2: Assess Current Position

From the retrieved knowledge, determine:

- **Milestone** — Current version, name, and goal
- **Phase position** — Which phase is active, how many completed vs remaining
- **Phase status** — Not started, planned, in progress, or complete
- **Paused work** — Whether a handoff exists with context for resumption
- **Pending items** — Count of deferred ideas, todos, or unresolved concerns
- **Last activity** — What was done last and when
- **Blockers** — Any known issues preventing progress

### Phase 3: Present Status Report

Format a clear status summary:

```
# [Project Name] — Progress Report

Milestone: v[X.Y] [Name]
Phase: [N] of [Total] — [Phase Name] — [Status]
Last activity: [description]

Completed Phases:
- Phase 1: [Name] — [one-line summary]
- Phase 2: [Name] — [one-line summary]

Current Phase:
Phase [N]: [Name] — [Goal]
Status: [Not started / Planned / In progress / Blocked]

Pending Items: [count] items
[Top 3-5 items if any]

Paused Work: [Yes/No]
[Handoff context if paused]
```

### Phase 4: Route to Next Action

Based on the assessed state, recommend the most logical next step:

| State | Recommended Action |
|-------|-------------------|
| Paused work exists | Resume from handoff — describe what was in progress and next steps |
| Phase has a plan, not yet executed | Run `byterover-execute` to begin phase execution |
| Phase needs a plan | Run `byterover-plan` for the current phase |
| Current phase complete, more remain | Run `byterover-plan` for the next phase |
| All phases complete | Run `byterover-ship` to complete the milestone |
| Pending items need attention | Present items, let user choose: work on it, defer, or add to phase |
| No project defined | Run `byterover-milestone` to start a new project |

Present the recommendation with reasoning. If multiple options are valid, list them in priority order and let the user choose.

If the user wants to review pending items:
- List all items with brief descriptions
- For each selected item, show full context
- Offer actions: work on it now, defer to next milestone, add to current phase plan

### Phase 5: Update Status

After the routing decision, update the knowledge base:

```bash
brv curate "Project status: Session resumed. Current position: Phase [N] — [status]. Next action: [what user chose]. Pending items: [count]" -f [relevant files]
```

### Completion

Clearly state:
1. What the user should do next
2. Which workflow skill to invoke (if any)
3. Key context for the next action

## Important Rules

1. **Query before presenting** — Always load state from the knowledge base, never assume
2. **Be honest about gaps** — If knowledge is incomplete, say what is missing
3. **Route intelligently** — Present the most logical action, not a generic menu
4. **Update status every session** — Curate project status so the next session can resume
5. **Pending items are knowledge** — Store and retrieve them via `brv curate` / `brv query`
6. **Max 5 files per curate** — Break down large status updates
7. **Never read secrets** — Skip `.env`, credential files, and similar
8. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
