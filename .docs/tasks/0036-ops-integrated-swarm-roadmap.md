# 🗺️ Roadmap de Orquestração Integrada: Missão Overpowers v3

Este documento consolida as 13 tarefas críticas para a evolução do ecossistema Overpowers. O objetivo é transformar este Roadmap em um plano de execução sinérgico através de 10 iterações de Heavy Reasoning.

---

## 📋 Visão Geral das Tarefas

# Task 0023: Advanced Hooks Implementation

**Status**: [ ]
**Priority**: HIGH
**Type**: feature

## Objective
Implement intelligent runtime hooks to enhance agent reliability and context awareness, porting logic from the `oh-my-opencode` research.

## Sub-tasks
- [ ] **Todo Continuation Enforcer**: Create a hook that monitors `session.idle` and re-prompts if `ctx.client.session.todo` is not empty.
- [ ] **Directory Context Injector**: Implement a hook that detects directory changes and automatically reads/injects the local `README.md` or `AGENTS.md` into the system prompt.
- [ ] **Edit Error Auto-Recovery**: Develop a middleware for the `edit` tool that catches common failures (indentation, line bounds) and provides specific "Hints" for agent self-correction.

## References
- Plan: `docs/tasks/0023-ops-advanced-hooks-feature-plan.md`
- Design: `docs/tasks/0023-ops-advanced-hooks-technical-design.md`
# Task 0024: Agent Reasoning BDI (Research)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: research
## Objective
Evaluate BDI (Belief-Desire-Intention) as a foundational paradigm.
# Task 0025: EvDD (Feature)
**Status**: [ ]
**Priority**: HIGH
**Type**: feature
## Objective
QA framework for skills using JSON schemas.
# Task 0026: Moltbot Memory (Feature)
**Status**: [ ]
**Priority**: HIGH
**Type**: feature
## Objective
Integrate hybrid search (sqlite-vec).
# Task 0027: Skill Decision Trees (Research)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: research
## Objective
Design guidance based on model/task/context.
# Task 0028: Memory Lifecycle (Ops)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: ops
## Objective
Explicit memory read/update in workflows.
# Task 0029: Claude Templates (Ops)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: ops
## Objective
Incorporate missing agent templates.
# Task 0030: Omnara Monitoring (Feature)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: feature
## Objective
PTY-based Flight Recorder.
# Task 0031: Mindmodel Context (Feature)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: feature
## Objective
Graph-based .agents/continuity-<agent-name>.md.
# Task 0032: Model Fallback System (Feature)

**Status**: [ ]
**Priority**: HIGH
**Type**: feature

## Objective
Implement automatic fallback and load balancing across model providers to ensure reliable execution when hit by rate limits.

## Sub-tasks
- [ ] **Script Fallback**: Update `run-subagent.sh` with a fallback chain (Opus -> Sonnet -> Flash -> GLM).
- [ ] **Health Monitor**: Implement `model_selector.py` to track rate limits and cooldowns.
- [ ] **CEO Intelligence**: Train CEO agent to select models based on task complexity.
# Task 0033: Skill Standardization Phase 2

**Status**: [ ]
**Priority**: HIGH
**Type**: ops

## Objective
Apply metadata standardization and standard templates to all 1200+ skills following the initial reorganization.

## Sub-tasks
- [ ] **Metadata Sweep**: Standardize YAML frontmatter (name, description, tags, version).
- [ ] **Workflow Template**: Implement standard 'Inputs/Process/Outputs' sections in `SKILL.md`.
- [ ] **Translation Sweep**: Translate Portuguese skills to English.
- [ ] **Integrity Fix**: Repair or archive 82 invalid skills identified in audit.
# Task 0034: Installer UX and Modularity

**Status**: [ ]
**Priority**: HIGH
**Type**: ops

## Objective
Refactor install.sh and unify deployment scripts (deploy-to-*.sh) into a modular engine using core utilities.

## Sub-tasks
- [ ] **Unify Deploys**: Extract symlink engine to `scripts/utils/create-symlinks.sh`.
- [ ] **Interactive UI**: Upgrade `install.sh` with `gum` for menus and confirmations.
- [ ] **Global Agent Support**: Expand deployment to all 9 supported coding agents (Cursor, Claude Code, etc.).
- [ ] **Environment Validation**: Add strict `.env` checks and directory detection before deployment.
# Task 0035: Containerized Sandbox (Feature)
**Status**: [ ]
**Priority**: MEDIUM
**Type**: feature
## Objective
Isolated Docker execution environment.


## Iteration 1 - Senior Architect (System Integration & Global Vision)

### Architectural Synthesis of the Overpowers v3 Roadmap
The transition from a collection of scripts to an industrial-grade agentic environment (Overpowers v3) requires a shift from linear task execution to an **Autonomous Ecosystem**. The 13 tasks identified are not discrete units but interdependent components of a larger architecture.

#### The Five Pillars of Overpowers v3
1. **Resilient Execution Layer (Tasks 0023, 0032, 0035)**: 
   - *Objective*: Ensure that agents never stop and never fail silently. 
   - *Mechanism*: Advanced Hooks (0023) provide the "nervous system" for task continuation and error recovery. Model Fallback (0032) provides the "energy backup" against rate limits. Containerized Sandbox (0035) provides the "isolated laboratory" for safe execution.
2. **High-Density Memory & Context (Tasks 0026, 0031, 0028)**: 
   - *Objective*: Solve context degradation and information loss. 
   - *Mechanism*: Moltbot Memory (0026) introduces vector-search capabilities for long-term project knowledge. Micode Mindmodel (0031) transforms the linear `.agents/continuity-<agent-name>.md` into a semantic graph. Standardized Memory Lifecycles (0028) ensure every agent action is recorded and retrieved correctly.
3. **Cognitive Evolution (Tasks 0024, 0027, 0029)**: 
   - *Objective*: Elevate agent reasoning from reactive to intentional.
   - *Mechanism*: BDI Paradigm (0024) moves agents to goal-oriented states. Skill Decision Trees (0027) guide model selection based on task complexity. Harvested Templates (0029) fill gaps in the orchestrator's persona library.
4. **Industrial Quality Assurance (Task 0025, 0033)**: 
   - *Objective*: Guarantee skill reliability at scale.
   - *Mechanism*: Evaluation-Driven Development (0025) enforces 100% pass rates for all skills. Skill Standardization (0033) ensures that 1200+ skills follow a uniform, discoverable, and bilingual structure.
5. **Deployment & UX (Task 0034, 0030)**: 
   - *Objective*: Seamless distribution and accountability.
   - *Mechanism*: Installer UX Modularity (0034) unifies the deployment engine for all 9 supported coding agents. Omnara Monitoring (0030) provides the "Flight Recorder" for auditing every bit of agent thought.

#### Architectural Risk Mitigation
- **Dependency Circularity**: Task 0023 (Hooks) depends on 0035 (Sandbox) for safe tool execution. We must implement the Sandbox *before* the hooks are deployed to production.
- **Fragmentation**: Standardization (0033) must run concurrently with Feature implementation to prevent "AI-Debt" from accumulating in the new modules.

#### Strategic Recommendation
The **Master Sequence** should be: 0034 (Installer) → 0033 (Standardization) → 0032 (Fallback) → 0035 (Sandbox) → 0023 (Hooks). This builds the infrastructure before the intelligence, ensuring a solid foundation for the enxame.


## Iteration 2 - First Principles (Fundamental Value & Deconstruction)

### First Principles Analysis: The v3 Tasklist

#### Deconstruction
- **Constituent Parts**: 1. Reliability Infrastructure (Hooks, Fallback, Sandbox). 2. Information Integrity (Moltbot, Mindmodel, Memory standard). 3. Agent Intelligence (BDI, Decision Trees, Templates). 4. Quality Control (EvDD, Standardization). 5. Operation Audit (Omnara).
- **Actual Values**: The core of Overpowers is **Trustworthy Autonomy**. Every task that doesn't directly increase the probability of an agent succeeding on its first try is "Form". Tasks that prevent the agent from crashing or hallucinating are "Function".

#### Constraint Classification
| Constraint | Type | Evidence | Challenge | 
|------------|------|----------|-----------| 
| Manual 8h Approval | Soft | Policy | Why wait for humans? Can we use a "Senior Model" as a temporary proxy? | 
| 1200+ Skills Load | Hard | Context Window | Do we really need 1200 skills active? (Progressive Disclosure physics) | 
| Vector Memory Cost | Soft | Market Price | Can we run high-quality local embeddings to eliminate dependency? | 
| Sandbox Isolation | Hard | Security/Host Safety | Required for autonomous shell execution. | 

#### Reconstruction
- **Fundamental Truths**: 1. Agents must have a continuous memory of the project state. 2. Failure points must be caught before they reach production. 3. System complexity must not exceed agent context.
- **Optimal Solution**: Merge Tasks 0026 (Moltbot) and 0031 (Mindmodel) into a single **"Unified Context Engine"**. The Mindmodel *is* the graph that guides the vector search. Treat Tasks 0023 (Hooks) and 0030 (Omnara) as the **"Autonomy Safety Suite"**.

#### Key Insight
We are currently treating "Memory" and "Control" as separate tasks. First principles show that **Control is a function of Memory**. An agent fails because it *forgets* or *never knew* a constraint. By unifying the context engine first, we simplify the implementation of hooks and fallback systems.

### ⚡ Strategic Refinement of Deliverables
- **Task 0023/0030 Synthesis**: The Flight Recorder (Omnara) should feed directly into the Error Recovery middleware (Hooks). 
- **Task 0032 (Fallback)**: Instead of just falling back models, fallback should include "Reasoning Strategies" (e.g., if Opus fails at 1000 lines, Flash should try a 100-line chunking strategy).


## Iteration 3 - Workflow Orchestration Patterns (Resilient State & Saga Execution)

### Orchestration Architecture for the v3 Roadmap
To transform the 13 tasks into a production-grade operation, we must apply **Temporal-style Orchestration**. The roadmap is a parent workflow, and each task is a child workflow or an activity.

#### Workflow vs. Activity Mapping
- **Workflows (Orchestration Logic)**: Tasks 0032 (Fallback), 0027 (Decision Trees), 0023 (Hooks). These contain decision-making logic and coordinate multiple agents. They must be **deterministic**.
- **Activities (External Interactions)**: Tasks 0033 (Standardization), 0034 (Installer), 0035 (Sandbox). These touch the filesystem, network, or external APIs. They must be **idempotent**.

#### Resilience Patterns Applied
1. **Saga Pattern for Mission-Critical Tasks**: 
   - *Step*: Apply Global Skill Standardization (0033). 
   - *Compensation*: Revert from backup if integrity check (0025) fails. 
   - *Step*: Deploy Containerized Sandbox (0035).
   - *Compensation*: Rollback to local shell execution if docker-compose fails.
2. **Fan-Out/Fan-In for Skill Standardization**: Task 0033 (1200+ skills) is too large for a single agent. We must spawn 12 child workflows (one per category), each processing ~100 skills in parallel, then fan-in to a global integrity report.
3. **Async Callback for Human-in-the-loop**: Task 0034 (Installer) and 0023 (Hooks) require manual validation of safety boundaries. The workflow will send a signal and wait for an external approval before proceeding to the next Wave.

#### Determinism Guardrails
| Task | Deterministic Brain | Idempotent Hands | 
|------|---------------------|-------------------| 
| 0023 (Hooks) | Python Hook logic | File edits via `jj` | 
| 0032 (Fallback) | Model selector script | API call retries | 
| 0033 (Standard) | Metadata sweep script | `sed`/`awk` replacements | 

### ⚡ New Orchestration Requirements
- **Task 0036 (Self-Monitoring)**: The Roadmap itself needs a "Heartbeat" mechanism. If no task progress is detected in 1 hour, the orchestrator must trigger a "Session Learning Capture" to diagnose the stall.
- **Compensation Registry**: Every new feature added in v3 must include a `compensation.md` file describing how to revert its impact without losing project state.


## Iteration 4 - Decision Helper (Prioritization & Trade-off Matrix)

### Strategic Decision: The v3 Execution Sequence

#### Decision
In what order should the 13 tasks be executed to minimize risk and maximize the success probability of the autonomous enxame?

#### Options

**Option 1: Infrastructure First (The Safety Shield)**
- **Pros**: Prevents crashes, secures the environment, creates fallbacks for expensive models.
- **Tasks**: 0034 (Installer), 0032 (Fallback), 0035 (Sandbox).
- **Cons**: High initial effort with no visible "intelligence" improvement.
- **Risk**: Low | **Effort**: High

**Option 2: Memory & Context First (The Neural Foundation)**
- **Pros**: Solves the biggest cause of agent failure: context loss. Improves performance of all other tasks.
- **Tasks**: 0026 (Moltbot), 0031 (Mindmodel), 0028 (Lifecycle).
- **Cons**: Requires complex database setup and embedding management.
- **Risk**: Medium | **Effort**: High

**Option 3: Quality & Standardization First (The Clean House)**
- **Pros**: Fixes technical debt, translates skills, prepares the project for scale.
- **Tasks**: 0033 (Standardization), 0025 (EvDD).
- **Cons**: Repetitive, high token cost for mass editing.
- **Risk**: Low | **Effort**: Medium

#### ICE Framework Analysis (Impact × Confidence × Ease)

| Opportunity | Impact (1-10) | Confidence (1-10) | Ease (1-10) | ICE Score |
|-------------|---------------|-------------------|-------------|-----------|
| Option 1 (Infra) | 9 | 9 | 4 | **81** |
| Option 2 (Memory) | 10 | 7 | 3 | **70** |
| Option 3 (Quality) | 7 | 10 | 6 | **76** |

#### Recommendation
**Option 1: Infrastructure First** is the recommended path. Without the **Sandbox (0035)** and **Fallback (0032)**, implementing complex features like **Moltbot Memory (0026)** or **Advanced Hooks (0023)** risks unrecoverable state corruption or massive token burn during failures.

### ⚡ Strategic Decision Matrix for v3 Implementation

| Criteria | Weight | Infra-First | Memory-First | Quality-First |
|----------|--------|-------------|--------------|---------------|
| System Stability | 40% | 10 | 6 | 7 |
| Agent Productivity | 30% | 5 | 10 | 8 |
| Failure Recovery | 20% | 9 | 4 | 5 |
| Ease of Implementation| 10% | 4 | 3 | 8 |
| **Total Weighted** | | **7.7** | **6.5** | **7.1** |

#### Next Steps
1. Finalize the modular deploy engine (0034) to allow safe testing of the Sandbox (0035).
2. Apply basic standardization (0033) only to the "Infrastructure" skills first to ensure they pass EvDD (0025).


## Iteration 5 - Gepetto (Self-Contained Execution Units & Slices)

### Implementation Blueprint: The v3 Execution Slices
To implement the roadmap without human intervention at every step, we must apply the **Gepetto Slice Pattern**. Each task must be broken into a `section-*.md` file that is completely self-contained, allowing any sub-agent to execute it without reading the entire roadmap.

#### Slice 1: The Unified Deployment Engine (Task 0034)
- **Background**: Fragmented `deploy-to-*.sh` scripts lead to inconsistent states across 9 agents.
- **Implementation**: Create `scripts/utils/create-symlinks.sh` as the single source of truth for symlink logic. Update all platform-specific scripts to import this core utility.
- **Acceptance Criteria**: [ ] `install.sh` supports all 9 agents. [ ] Conflict policy is enforced via a single central flag.

#### Slice 2: The Neural Knowledge Graph (Tasks 0026, 0031)
- **Background**: `.agents/continuity-<agent-name>.md` is too small for v3 scale. We need semantic memory.
- **Implementation**: Initialize `sqlite-vec` in `.agents/memory.db`. Create a script `scripts/sync-mindmodel.py` that parses all `docs/tasks/` and builds a graph of dependencies.
- **Acceptance Criteria**: [ ] Vector search returns relevant task context. [ ] Mindmodel visualizes the current "War Room" state of the project.

#### Slice 3: The Autonomy Nervous System (Task 0023)
- **Background**: Agents stall when idle with pending tasks.
- **Implementation**: Deploy `hooks/runtime/todo_enforcer.py`. It must intercept the `session.idle` event from the OpenCode/Gemini runtime and inject the "CONTINUE" prompt if tasks are open.
- **Acceptance Criteria**: [ ] Agent resumes working automatically after a 5s idle period if `tasklist.md` has unchecked items.

#### External Review Protocol (Review/)
Every Slice must be reviewed by two independent agents (one Gemini, one Claude) before being marked as "Ready for Implementer". This ensures the technical design is resilient to "IA-Debt" before code is even written.

### ⚡ Execution Files Requirements
- **`claude-ralph-loop-prompt.md`**: Must be generated for the entire Roadmap. It should embed all 13 tasks as executable sections, with a clear dependency order: **Slice 1 (Installer) -> Slice 2 (Memory) -> Slice 3 (Safety) -> Slice 4 (Intelligence)**.
- **Section Isolation**: No section file should reference `0036-master-roadmap.md`. All context required for implementation (paths, constants, schemas) must be duplicated or referenced via global docs inside each section.


## Iteration 6 - Task Coordination Strategies (Swarm Topology & Collision Avoidance)

### Swarm Coordination Plan: Parallelizing the Roadmap
To execute 13 major tasks without generating merge hell or recursive reasoning loops, we must define a **Diamond Dependency Graph** and strict **File Ownership Boundaries**.

#### Dependency Graph (v3 Core)
```
    [ 0034: Installer ] ─────────┐
          │                      │
    [ 0033: Standardization ] ───┼───┐
          │                      │   │
    ┌─────┴──────────────┐       │   │
    ▼                    ▼       ▼   ▼
[ 0032: Fallback ]  [ 0035: Sandbox ] [ 0025: EvDD ]
    │                    │           │
    └─────┬──────────────┴─────┬─────┘
          ▼                    ▼
    [ 0023: Hooks ]      [ 0026: Memory ]
```

#### File Ownership Boundaries
- **Implementer A (Infra)**: Owns `scripts/`, `sandbox/`, `hooks/runtime/`. (Tasks 0034, 0032, 0035, 0023, 0030).
- **Implementer B (Knowledge)**: Owns `.agents/knowledge/`, `scripts/knowledge/`. (Tasks 0026, 0031, 0028, 0029).
- **Implementer C (Quality)**: Owns `skills/*/SKILL.md`, `evaluations/`. (Tasks 0033, 0025, 0027, 0024).

#### Interface Contracts between Swarms
1. **Hooks-Sandbox Contract**: Task 0023 (Hooks) must not call any tool directly; it must request an execution via the Sandbox API (0035).
2. **Memory-Logic Contract**: Agents performing Task 0024 (BDI) must consume context only through the Mindmodel Graph (0031).
3. **Quality-Release Contract**: No task is marked complete in `tasklist.md` unless its associated EvDD schema (0025) has a 100% pass rate.

#### Swarm Monitoring Signals
| Signal | Meaning | Action |
|--------|---------|--------|
| `session.blocked` > 1h | Human Approval Bottleneck | Trigger fallback to Senior Model Proxy |
| `edit.error` > 3 | Prompt Drift in Wave 1 | Halt Wave, refine technical design |
| `tasklist.unchecked` > 50 | Agent Overload | Spawn sub-swarm for horizontal scaling |

### ⚡ Strategic Coordination Checkpoints
- **Gate 1: Infra-Freeze**: Implementation of 0034 and 0035 must be verified by a human before any logic translation begins.
- **Wave Pruning**: If Task 0026 (Memory) delays more than 3 days, Wave 2 (Hooks) will proceed using a "Legacy Grep" fallback to maintain global velocity.


## Iteration 7 - Scientific Critical Thinking (Validation Rigor & Success Metrics)

### Scientific Critique of the v3 Roadmap Success Signals
The current roadmap relies on "Task Completion" as its primary metric. From a scientific perspective, this suffers from **Construct Validity** issues: does checking a box in `tasklist.md` actually mean the system is more resilient? We need objective, measurable **Validation Signals** for each pillar.

#### Methodology Enhancement: Empirical Validation Gates
1. **Resiliency Validation (Tasks 0023, 0032)**:
   - *Metric*: "Mean Time To Recovery" (MTTR) for simulated agent stalls.
   - *Experiment*: Injetar 10 falhas de rede propositais durante uma Wave. O sucesso é definido como o agente retomando a tarefa em <30s sem intervenção humana.
2. **Memory Validity (Tasks 0026, 0031)**:
   - *Metric*: "Context Retrieval Accuracy" (CRA).
   - *Experiment*: Ask the agent a question about a decision made 5 Waves ago. Compare the answer against the Mindmodel graph. Goal: >95% accuracy.
3. **Skill Reliability (Task 0025, 0033)**:
   - *Metric*: "EvDD Pass Rate".
   - *Experiment*: Run 100 random queries against 10 standardized skills. All must follow the "Inputs/Process/Outputs" template exactly and return schema-valid results.

#### Systematic Bias Review
| Bias Type | Risk in v3 Roadmap | Mitigation Strategy |
|-----------|--------------------|---------------------|
| Confirmation Bias | Agents assuming their hooks work | Mandatory "Chaos Monkey" testing in the Sandbox (0035) |
| Survivorship Bias | Only logging successful agent turns | Omnara Flight Recorder (0030) must capture 100% of failed turns |
| Measurement Bias | Inconsistent skill frontmatter | Automated CI/CD linting of SKILL.md files |

### ⚡ New Success Criteria (Scientific Protocol)
- **The Isomorphism Test**: After standardization (0033), a skill must produce identical functional behavior as its original version, but with <50% of the original prompt size (Efficiency Metric).
- **The Null Hypothesis for Fallback**: We must prove that Task 0032 (Fallback) actually saves money. *Hypothesis*: "Using GLM 4.7 for simple tasks reduces monthly token burn by >30% without increasing the error rate by >1%."


## Iteration 8 - Codebase Investigator (Impact Mapping & Sibling Dependencies)

### Physical Code Mapping: The v3 Infrastructure Surface
The v3 mission targets specific architectural nodes within the repository. The investigation has identified the following **Primary Targets** and their sibling dependencies.

#### 📁 Impact Analysis: Infrastructure & Scripts
1. **Unified Installer (Task 0034)**:
   - *Target*: `install.sh` (Current state: Monolithic).
   - *New Artifact*: `scripts/utils/create-symlinks.sh`. This script will consolidate logic found across `deploy-to-*.sh` files.
   - *Sibling Dependency*: `scripts/install-mcps.sh` must be updated to use the same symlink engine to ensure consistent MCP registration.
2. **Model Fallback (Task 0032)**:
   - *Target*: `skills/subagent_orchestration/scripts/run-subagent.sh`.
   - *New Artifact*: `scripts/utils/model_selector.py`. A stateful health monitor using `~/.config/opencode/model_status.json`.
   - *Logic Integration*: The `run-subagent.sh` script must transition from a simple loop to a Python-mediated call that respects cooldowns.
3. **Autonomy Hooks (Task 0023)**:
   - *Target Area*: `hooks/` directory (New `runtime/` subfolder).
   - *Symbol Impact*: Interaction with `ctx.client.session.todo` via the OpenCode API. This is the most complex integration point as it hooks into the agent's internal state machine.

#### 🔍 Symbol & Schema Dependencies
| Component | Source Symbol | Consumer Symbol | Link Mechanism |
|-----------|---------------|-----------------|----------------|
| Sandbox | `sandbox/Dockerfile` | `hooks/runtime/` | Subprocess / Docker Exec |
| Mindmodel | `docs/tasks/*.md` | `memory.db` | Python Parser (Task 0031) |
| EvDD | `schema.json` | `skills/*/SKILL.md`| YAML Linting (Task 0025) |

#### Discovery findings on Circular Dependencies
- The **Sandbox (0035)** must expose a lightweight API or CLI so that **Hooks (0023)** can trigger safety checks without adding circular dependency on the main `install.sh` script.
- **Skill Standardization (0033)** will modify 1200+ files. This is a "High-Blast Radius" operation that must be executed using isolated `jj workspaces` to prevent snapshot corruption during parallel execution of other features.

### ⚡ Implementation Guardrails (Physical)
- **The JJ-Workspace Rule**: Tasks 0033 and 0034 must never run in the same workspace simultaneously. 
- **The Absolute Path Enforcement**: All new scripts in `scripts/utils/` must use the project-root detection logic from `install.sh` to ensure they work across all 9 supported coding agents (Cursor, Windsurf, etc.).


## Iteration 9 - Ensemble Solving (Memory Architecture Alternatives)

### Multi-Perspective Analysis: The Unified Context Engine (Tasks 0026, 0031)

#### Approach 1: The RAG Purist (Focus on Retrieval)
- **Mechanism**: Use `sqlite-vec` to store all file chunks. Use Gemini's `RETRIEVAL_DOCUMENT` embeddings.
- **Pros**: High accuracy for finding specific code snippets. Simple implementation.
- **Cons**: High token cost for continuous indexing. Lacks understanding of *relationships* between tasks.

#### Approach 2: The Graph Architect (Focus on Relationships)
- **Mechanism**: Implement Task 0031 as a NetworkX graph. Nodes are Tasks/Files, Edges are Dependencies. 
- **Pros**: Perfect for roadmap orchestration. Understands that "Task A blocks B". Low token overhead.
- **Cons**: Harder to search for unstructured text or logic patterns.

#### Approach 3: The Recursive Synthesizer (Focus on Compression)
- **Mechanism**: Use a hierarchy of `.agents/continuity-<agent-name>.md` files (root, directory, sub-directory). Agents summarize their work at each level.
- **Pros**: Zero external dependencies. Extremely context-efficient.
- **Cons**: Information loss is inevitable over long durations.

#### Evaluation Matrix
| Criterion | Weight | RAG Purist | Graph Architect | Rec. Synthesizer |
|-----------|--------|------------|-----------------|------------------|
| Correctness | 35% | 9 | 8 | 6 |
| Performance | 25% | 7 | 10 | 9 |
| Simplicity | 20% | 8 | 5 | 10 |
| Integration | 20% | 6 | 9 | 7 |
| **Total** | | **7.7** | **8.0** | **7.7** |

#### Winning Recommendation
The **Graph Architect approach (8.0)** is the primary choice for v3. Given the complexity of 13+ interdependent tasks, knowing the *state of the mission* is more valuable than simple text retrieval. However, we should implement a **Hybrid Solution**: The Mindmodel (0031) manages the "Task Graph", while Moltbot (0026) provides the "Logic Search" for specific code patterns.

### ⚡ Integration Strategy for the Hybrid Engine
- **Mindmodel as Indexer**: The Mindmodel should serve as the high-level map that tells Moltbot *where* to search. If Task 0023 is active, the Mindmodel instructs Moltbot to prioritize the `hooks/` and `sandbox/` indices.
- **Automatic Context Priming**: When an agent starts a task, the framework should automatically inject the 3 closest nodes from the Mindmodel graph into the initial prompt.


## Iteration 10 - Knowledge Synthesis (Mission Command & Holistic Strategy)

### Synthesis Report: The v3 Unified Command Strategy
After 9 iterations of deep reasoning, the Overpowers v3 Roadmap has evolved from a list of tasks into a **Synchronized Mission Command**. This synthesis integrates the technical requirements of infrastructure with the cognitive needs of the enxame.

#### 1. The Critical Path Fusion
- **Baseline Intelligence**: The "Neural Foundation" (Memory 0026 + Mindmodel 0031) must be initialized during the "Infra Wave". Without semantic memory, the Advanced Hooks (0023) will operate on stale or hallucinated context.
- **Quality-by-Design**: Evaluation-Driven Development (0025) is not a post-task step; it is the **Input Signal** for all Wave execution. No code is generated until the EvDD schema is defined.

#### 2. Resource & Token Strategy (Tokenomics Synthesis)
- **Hybrid Model Aloccation**: Use models as functional layers. 
  - *Layer 1 (Logic)*: Flash/Sonnet for repetitive translation.
  - *Layer 2 (Integrity)*: Pro models for cross-domain RFA (Request for Amendment) mediation.
  - *Layer 3 (Strategy)*: Local models for high-frequency status checking and linting to preserve cloud quota.
- **Escalation Protocol**: If an agent hits a rate-limit, the Fallback System (0032) automatically triggers a "Reasoning Compression" mode, where the agent uses local resources to summarize the current state and wait for a secondary provider.

#### 3. Swarm Integrity & Accountability
- **The DNA Rule**: Every commit generated during v3 implementation must carry its "Commit DNA" (Prompt version, Agent ID, Mindmodel node). This allows for mass-recall if a pattern is later found to be flawed.
- **Swarm Sovereignty**: Lead Agents (Actors) maintain domain state in the Sandbox (0035), preventing the overhead of re-loading context at every sub-task.

#### Consolidated Operational Guardrails
| Domain | Combined Mitigation | Authority |
|--------|---------------------|-----------|
| System Stability | Sandbox (0035) + Circuit Breakers (0023) | senior-architect |
| Memory Fidelity | Mindmodel Graph (0031) + Vector Sync (0026) | knowledge-synthesis |
| Agent Ethics/Logic| BDI Paradigm (0024) + Decision Trees (0027) | reasoning |
| User Confidence | Unified Installer (0034) + Flight Recorder (0030) | ops-infra |

### ⚡ Final v3 Mission Statement
Overpowers v3 is not just an update; it is the creation of a **Self-Healing Agentic Operating System**. The success of this mission is measured by the agent's ability to maintain **Zero-Loss Continuity** across thousands of independent execution turns. The roadmap is now ready for physical implementation starting with the **Modular Deploy Engine (0034)**.
