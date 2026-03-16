---
name: research-iteration-idea-storm
description: An automated iterative laboratory for engineering problems. Given an idea or engineering problem, it automatically researches solutions, designs implementations, verifies effects, iterates optimizations, and stores results in Notion.
tags: research, iteration, engineering, automation, notion
version: 1.0.0
---

# Idea Storm

Automated Design -> Verification -> Iteration loop for engineering problems. Runs in the background without blocking the main session.

## Running Architecture

Uses a segmented spawn mode: work between checkpoints runs in independent sub-agents, with state passed via files.

```
Main Session                        Sub-agent (isolated)
  │                                    │
  ├─ Create experiment.yaml            │
  ├─ spawn("idea-storm: research+design") ─→ │
  │   (Continue chat)                  ├─ Phase 2: Research
  │                                    ├─ Phase 3: Solution Design
  │                                    ├─ Update experiment.yaml
  │  ◄─ announce solution summary ─────┤  ✅ Checkpoint 1
  │                                    └─ (Exit)
  │
  ├─ User confirms solution
  ├─ spawn("idea-storm: impl+verify") ─→ │
  │   (Continue chat)                  ├─ Read experiment.yaml to restore state
  │                                    ├─ Phase 4: Implementation
  │                                    ├─ Phase 5: Verification
  │                                    ├─ Phase 6: Evaluation
  │                                    ├─ Update experiment.yaml
  │  ◄─ announce iteration results ────┤  ✅ Checkpoint 2
  │                                    └─ (Exit)
  │
  ├─ User confirms (continue/converge)
  ├─ spawn("idea-storm: iteration N") ─→ ... (Repeat until convergence)
  │
  ├─ spawn("idea-storm: convergence report") ─→ │
  │  ◄─ announce final report ─────────┤  ✅ Checkpoint 3
  └─ Done
```

### spawn Task Template

Each spawn task must include:
1. Experiment state file path: `experiments/<id>/experiment.yaml`
2. Current phase to execute
3. User confirmation/feedback (if any)

Example:
```
sessions_spawn(task="Execute idea-storm experiment.
Read experiment state: experiments/facial-gan-20260213/experiment.yaml
Phase: Phase 4-6 (Implementation -> Verification -> Evaluation)
User feedback: Solution OK, use StyleGAN3 route.
Follow idea-storm skill process, update experiment.yaml and report results when done.")
```

Sub-agent startup:
1. Read idea-storm SKILL.md for process guidance.
2. Read experiment.yaml to restore state.
3. Execute specified phases.
4. Update experiment.yaml + Notion.
5. announce results summary.

---

## Memory Management

Three-layer storage to ensure no state loss:

### Layer 1: Hot State (SESSION-STATE.md)

The main session's SESSION-STATE.md records current active experiment summary:

```yaml
idea_lab:
  active_experiment: "facial-gan-20260213"
  experiment_path: "experiments/facial-gan-20260213/"
  current_phase: "Waiting for user checkpoint 2"
  last_spawn_label: "idea-storm-facial-gan-iter2"
```

### Layer 2: Experiment Workspace

Each experiment has a separate directory under workspace:

```
experiments/<experiment-id>/
├── experiment.yaml          # Full experiment state (Core)
├── research/                # Research materials
│   └── findings.md
├── design/                  # Solution design
│   └── plan.md
├── src/                     # Implementation code
├── data/                    # Input data, references, etc.
├── results/                 # Verification results per round
│   ├── iter-1/
│   ├── iter-2/
│   └── ...
└── report.md                # Final report (local copy)
```

### Layer 3: Notion Long-term Record

Structured experiment reports organized by time and category.

### experiment.yaml Specification

```yaml
id: "facial-gan-20260213"
title: "Generating facial micro-expressions with GAN"
created: "2026-02-13T12:00:00+08:00"
status: "running"  # running | paused | completed | abandoned

# Current Progress
phase: "Phase 5: Verification"
iteration: 2
max_iterations: 5

# Problem Definition
problem:
  description: "Need to generate realistic facial micro-expression animations"
  constraints: "Real-time rendering, latency < 50ms"

# Verification Config
validation:
  mode: "B"  # A=Image Comparison B=Metric Optimization C=Functional Verification D=Custom
  description: "Optimize FID score"
  threshold: 50
  current_best: 67.3

# Checkpoint Records
checkpoints:
  - phase: 3
    time: "2026-02-13T13:00:00+08:00"
    status: "approved"
    user_feedback: "Solution confirmed, use StyleGAN3"
  - phase: 6
    iteration: 1
    time: "2026-02-13T14:30:00+08:00"
    status: "continue"
    user_feedback: "FID 67.3, continue optimizing learning rate"

# Iteration History
iterations:
  - round: 1
    changes: "Initial implementation, lr=0.001"
    result: "FID 67.3"
    decision: "Continue, adjust learning rate"
  - round: 2
    changes: "lr=0.0003, increase data augmentation"
    result: "pending"

# Notion
notion_page_id: "xxx-xxx-xxx"
```

---

## Core Process

### Phase 1: Problem Definition (Main Session)

User inputs engineering problem or idea. Extract and confirm:
1. **Description**: What to solve.
2. **Success Criteria**: What defines "solved".
3. **Constraints**: Tech stack, resource limits.
4. **Verification Mode**: See [Verification Modes](#verification-modes).

After confirmation:
1. Create directory `experiments/<id>/`.
2. Write `experiment.yaml`.
3. Create Notion page.
4. Update SESSION-STATE.md.
5. spawn sub-agent for Phase 2-3.

### Phase 2: Research (Sub-agent)

Engineering-oriented search priority:
1. GitHub open source projects.
2. Tech blogs, Stack Overflow, engineering practices.
3. Product/API docs.
4. Papers (only if engineering docs are insufficient).

Tools: `web_search` + `web_fetch`.

Output:
- `research/findings.md`
- Update experiment.yaml
- Update Notion

### Phase 3: Solution Design (Sub-agent)

Design technical solution based on research:
- Overall architecture.
- Key tech selection.
- Implementation steps.
- Expected effects.

Output:
- `design/plan.md`
- Update experiment.yaml (phase -> "Waiting for Checkpoint 1")
- Update Notion
- announce summary to main session.

### ✅ Checkpoint 1: Solution Confirmation (Main Session)

After user confirmation, spawn new sub-agent for Phase 4-6.

### Phase 4: Implementation (Sub-agent)

Execute per solution. May include: coding, environment config, asset generation, API calls.

Output:
- Code under `src/`
- Update Notion lab logs.

### Phase 5: Verification (Sub-agent)

Execute per verification mode defined in experiment.yaml.

Output:
- `results/iter-N/`
- Update Notion verification results.

### Phase 6: Evaluation & Iteration Decision (Sub-agent)

| Situation | Action |
|-----------|--------|
| Target met | Mark converged, announce result |
| Close to target, tunable | Auto-iterate parameters, back to Phase 4 (max iterations apply) |
| Fundamental issues | announce suggestion to change solution |

Update experiment.yaml and announce to main session.

### ✅ Checkpoint 2: Iteration Confirmation (Main Session)

Report content:
- Round summary.
- Data/screenshots.
- Suggestions for next steps.

User confirms to spawn next round or converge.

### Phase 7: Convergence Report (Sub-agent)

Generate final report:
- `report.md` (local copy)
- Update Notion final report block.
- announce summary.

### ✅ Checkpoint 3: Final Confirmation (Main Session)

---

## Verification Modes

### Mode A: Image Comparison
User provides reference images + input set. Agent generates output and compares.
- Tools: `scripts/compare_images.py` or `image` tool.

### Mode B: Metric Optimization
User defines evaluation function or metrics. Agent optimizes implementation to improve metrics.
- Threshold-based convergence.

### Mode C: Functional Verification
User defines test cases or acceptance criteria. Agent verifies item by item.

### Mode D: Custom
User describes verification method. Agent follows description.

---

## Claude Code Integration

Phase 4 (Implementation) prefers using Claude Code in Docker sandboxes.

### Docker Sandbox Architecture

Each experiment runs in an independent Docker container:
- Isolated from host.
- Non-root user (`coder`).
- Auto-skip permissions.
- API config injected via env.

Build: `docker build -t idea-storm-sandbox -f scripts/Dockerfile .`

### Usage in Sub-agent

Sub-agent calls Phase 4 via `exec` + `pty:true`:

```bash
docker run --rm -t \
  -e ANTHROPIC_AUTH_TOKEN="$API_KEY" \
  -e ANTHROPIC_BASE_URL="$BASE_URL" \
  -v experiments/<id>:/workspace \
  idea-storm-sandbox \
  bash -c 'cd /workspace && git init -q 2>/dev/null; claude --print --dangerously-skip-permissions "<prompt>"'
```
