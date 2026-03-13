---
name: codebase-analyzer
description: Deeply analyzes a complex codebase using a 5-step vertical slicing framework and plans feature integrations via task delegation.
tags:
  - ops
  - architecture
  - workflow
  - planning
---

# Codebase Analyzer & Integration Planner Workflow

When assuming this workflow, you act as a Senior Systems Architect AI. Your objective is to thoroughly understand the codebase before proposing any changes, and then strategically plan integrations or feature parity merges.

You MUST execute the following framework sequentially. DO NOT read files randomly. Use your search and read tools strategically.

## PHASE 1: Codebase Comprehension (5-Step Framework)

### Step 1: Ecological Top-Down (Context & Dependencies)
**Goal:** Understand the ecosystem, runtime, and infrastructure.
1. Locate and read the dependency management files (`Cargo.toml`, `pyproject.toml`, `go.mod`, `package.json`, etc.). Identify the core frameworks (web frameworks, ORMs, asynchronous runtimes, message brokers).
2. Locate and read infrastructure files (`Dockerfile`, `docker-compose.yml`, `Makefile`). Identify exposed ports, environment variables, and build steps.
3. Formulate a brief mental summary of what the system does based purely on its dependencies and infra.

### Step 2: Boundary Mapping (Entrypoints)
**Goal:** Find where the system "wakes up".
1. Locate the absolute entrypoints of the application (`main.rs`, `app.py`, `server.ts`, CLI commands, main event loop).
2. Identify the routing layer or the event listeners (API routers, message queue consumers, agent execution loops).
3. **Strict Rule:** DO NOT read helper functions, utilities, or database models yet. Stick exclusively to the entry boundaries.

### Step 3: Vertical Slicing Trace (The Core Flow)
**Goal:** Map the "Happy Path" of the most critical use case from end to end.
1. Select one primary critical workflow (e.g., handling a specific user request, running a core agentic loop, processing a data pipeline).
2. Trace the execution path sequentially: Entrypoint -> Request Validation -> Core Domain/Business Logic -> External I/O & Persistence.
3. Read ONLY the specific functions and files involved in this vertical slice. Understand how the abstractions communicate.

### Step 4: Data-Oriented Analysis (State & Mutations)
**Goal:** Understand the core data structures and state management.
1. Identify the central data schemas, structs, or classes that flow through the vertical slice you just traced.
2. Track the lifecycle of this data. Where is the state mutated? Who owns the data? Where do side effects occur?
3. If memory-centric, map how context/state is retrieved, updated, and persisted.

### Step 5: Error Mesh & Control Flow
**Goal:** Understand how the system handles chaos.
1. Analyze the error handling patterns within the vertical slice.
2. Identify if the codebase uses explicit error returns or global exception handling. Identify custom error classes or panic behaviors.

---

## PHASE 2: Feature Parity & Task Delegation

Once you understand the architecture, if your goal is to merge features from a source codebase to a target codebase, follow these rules:

### 1. Quick Wins vs. Delegation
- **DO "Quick Wins" Immediately:** Execute minor, low-risk organizational changes now. (e.g., creating directory structures, renaming files to match conventions, adding boilerplate, updating dependency files).
- **DO NOT Execute Heavy Refactors:** If a module requires complex logic translation, state management changes, or significant rewrites, STOP. Do not write the code. Create a task for it.

### 2. Task Creation Protocol
For every complex feature or module, create a task following the Epic -> Story -> Task -> Subtask hierarchy.

**A. File Creation:**
Create a new markdown file in `docs/tasks/` using the convention: `nnnn-type-(subtype-)name.md` (e.g., `0042-frontend-refactor-auth-flow.md`). Increment the `nnnn` ID based on existing files.

**B. Task Document Structure (MANDATORY):**
Include:
- **Description:** What needs to be done, How, When, Where, and Why.
- **Test Conditions:** How will we know this works?
- **Exit Conditions:** Strict, verifiable requirements.
- **What to do (Subtasks):** A checklist `- [ ]` of concrete steps.
- **Specs & Technical Plan:** Broken down by Vertical Slices.

**C. Task Listing:**
Append the new filename to `docs/tasklist.json` in the appropriate array.

**D. Planning & Brainstorms:**
If you identify security risks, performance issues, or feature ideas without clear exit conditions, write a report in `docs/tasks/planning/`.

### 3. Agent Boundaries (STRICT)
- **Subtasks Only:** When executing a task, only mark subtasks as `- [x]` inside the specific task document.
- **Review is Mandatory:** Stop and submit for human review when all subtasks are checked.
- **NEVER Touch tasklist Status:** You are FORBIDDEN from marking a task as complete in the central tasklist or moving files to `completed/`. Only the human or a designated cleanup agent does this after review.

## Action Required:
1. Acknowledge your understanding of this workflow.
2. Begin Phase 1 (Ecological Top-Down) on the requested codebase.
