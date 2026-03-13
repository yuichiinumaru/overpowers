---
name: byterover-milestone
description: "Define project milestones with goals, scoped requirements, and phased roadmaps. Gathers user intent through questioning, assigns REQ-IDs for traceability, derives phases using goal-backward analysis, and optionally captures implementation decisions for gray areas. Stores everything via brv curate."
---

# ByteRover Milestone Planning

A structured workflow for defining what to build next. Gathers goals, scopes requirements, derives a phased roadmap, and optionally captures implementation decisions — all stored in the knowledge base for downstream planning and execution.

## When to Use

- Starting a new project or product initiative
- Beginning the next cycle of work after shipping a milestone
- When scope is unclear and needs structured requirements analysis
- When multiple features need to be organized into phases

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

The user must describe what they want to build or what the next milestone should achieve.

## Process

### Phase 1: Query Existing State

Check what already exists in the knowledge base:

```bash
brv query "What is the project definition, goals, and core value?"
brv query "What milestones have been completed and what was shipped?"
brv query "What is the current project status and roadmap?"
brv query "What requirements exist — validated, active, or out of scope?"
```

- If nothing returned: this is a new project. Proceed from scratch.
- If project exists: summarize what was shipped and what remains before asking what's next.

### Phase 2: Goal Gathering

Through conversation with the user, establish:

**For new projects:**
- Project name and purpose
- Core value proposition (one sentence: "This enables [user] to [outcome]")
- Target user or audience
- 3-7 high-level capabilities for the first milestone

**For existing projects:**
- Review previous milestone accomplishments
- Ask: "What do you want to build or ship next?"
- Determine milestone name and version (increment from last)
- Identify 3-7 new capabilities or improvements

### Phase 3: Requirements Scoping

For each capability area identified in Phase 2:

1. Break into specific, testable requirements
2. Assign REQ-IDs using `[CATEGORY]-[NUMBER]` format (e.g., `AUTH-01`, `FEED-02`)
3. Scope each requirement:
   - **MVP** — Must ship in this milestone
   - **Future** — Defer to a later milestone
   - **Out of Scope** — Explicitly excluded

Present the scoped requirements table to the user for confirmation. Adjust based on feedback.

### Phase 4: Phase Roadmap

Derive 3-7 phases from the MVP requirements:

1. State the milestone goal as an outcome: "When this is done, [observable result]"
2. Group related requirements into phases that can be built and verified independently
3. For each phase specify: name, goal, which REQ-IDs it covers, 2-5 success criteria
4. Order phases by dependency (data models first, integrations last)
5. Verify every MVP requirement maps to exactly one phase (100% coverage)

Present the roadmap table to the user for approval.

### Phase 5: Gray Area Discussion (Optional)

Ask the user if they want to discuss implementation decisions for any phases before planning begins.

For each selected phase:
- Identify gray areas — decisions that would change the outcome (not implementation details the agent can decide)
- Ask focused questions (3-5 per phase) about layout, behavior, data flow, or user experience
- Capture each decision clearly
- Redirect scope creep: if new capabilities surface, note them as "Deferred Ideas"

### Phase 6: Store Milestone

Curate all artifacts to the knowledge base:

```bash
brv curate "Project: [name]. Core value: [proposition]. Milestone v[Y] [name]: [goal]. MVP requirements: [REQ-ID list with descriptions]" -f [key project files]
brv curate "Roadmap v[Y]: [N] phases. Phase 1: [name] - [goal] - covers [REQ-IDs]. Phase 2: [name] - [goal] - covers [REQ-IDs]..." -f [key files]
brv curate "Project status: Milestone v[Y] defined. [N] requirements, [M] phases. Next action: plan Phase 1 using byterover-plan" -f [key files]
```

If gray area decisions were captured:
```bash
brv curate "Phase [N] decisions: [area]: [decision]. [area]: [decision]. Agent discretion: [areas]" -f [relevant files]
```

### Completion

Present to the user:

1. **Milestone** — Name, version, goal
2. **Requirements** — Count with REQ-ID table (MVP / Future / Out of Scope)
3. **Roadmap** — Phase table with goals, REQ-IDs, success criteria
4. **Decisions** — Any gray area resolutions captured
5. **Next step** — Run `byterover-plan` for Phase 1

## Important Rules

1. **Requirements must be testable** — "User can reset password via email" not "Handle passwords"
2. **Every requirement gets a REQ-ID** — Enables traceability across phases and milestones
3. **Goal-backward** — Derive phases from outcomes, not from tasks
4. **100% coverage** — Every MVP requirement must map to exactly one phase
5. **No scope creep** — Defer new capabilities discovered during discussion
6. **Store everything** — Curate project, requirements, roadmap, and decisions via `brv curate`
7. **Max 5 files per curate** — Break down large milestone definitions into multiple curate commands
8. **Never read secrets** — Skip `.env`, credential files, and similar
9. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
