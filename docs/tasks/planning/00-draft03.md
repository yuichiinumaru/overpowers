# FORGE v2: The Definitive AI-First Development Methodology

## Phase 0: Governance & Setup

### 1. File Structure & Naming Convention
The following structure is mandatory to ensure context precision for AI agents.

**Root Directory:**
- `AGENTS.md` (The Constitution: Project overview, governance, critical rules)
- `.cursorrules` / `.windsurfrules` (Symlinked from `docs/06-rules.md`)
- `.cursorignore` (Context filtering: exclude node_modules, dist, coverage)

**Documentation Directory (`docs/`):**
Order matters. Agents read sequentially.

| Filename | Purpose | Status |
| :--- | :--- | :--- |
| `00-draft.md` | Brainstorming, raw ideas, research notes. | Mutable |
| `01-plan.md` | **The "Why" & "How".** Strategic plan, tech stack choices. | Versioned |
| `02-tasks.md` | **The "What" & "When".** Granular task list with [ ] checkboxes. | Live |
| `03-architecture.md` | **The "Where".** Folder structure, domain boundaries (DDD). | Versioned |
| `04-changelog.md` | **Institutional Memory.** What changed + WHY. | Append-only |
| `05-ideas.md` | Parking lot for future features. | Mutable |
| `06-rules.md` | **The Law.** Coding patterns, dos/don'ts with examples. | Versioned |
| `07-errors.md` | (Optional) Known issues and workaround patterns. | Live |

### 2. The Governance "Constitution" (`AGENTS.md`)
Every project must have this file at the root. It is the first file any agent reads.

**Core Sections:**
1. **Mission:** One sentence describing the project goal.
2. **Context:** Brief summary of the domain.
3. **Governance:**
   - "No code without tests (TDD)."
   - "No new domains without updating `03-architecture.md`."
   - "If a task in `02-tasks.md` is checked [x], do not modify it."
4. **Methodology (FORGE):** Explicitly state the methodology used (RDD -> DDD -> TDD -> CDD).

---

## Phase 1: Specification & Architecture (The "Input Control")

### 1. RDD (Readme-Driven Development)
- **Action:** Write `01-plan.md` and `03-architecture.md` before any code.
- **Validation:** Ask the AI: *"Read these docs and explain the project back to me. Identify any missing edge cases."*

### 2. DDD (Domain-Driven Design)
- **Action:** Define Domains in `03-architecture.md`.
- **Rule:** "Code for 'Billing' must stay in `src/billing/`. It cannot import 'Auth' directly; it must use an interface."
- **Artifact:** TypeScript interfaces / Python ABCs defined *before* implementation.

### 3. Marching Questions (The Decision Matrix)
Use these questions to determine if you need extra layers (BDD, MDD, FDD).

1. **Stakeholder Approval?** Yes -> Add `specs/*.feature` (BDD).
2. **Complex Data?** Yes -> Create `docs/schema.mermaid` (MDD).
3. **Regulatory/Safety?** Yes -> Enable "Waterfall Gates" (Manual review before merge).

---

## Phase 2: The Development Loop (The "Execution Engine")

### 1. Task Intake (Kanban)
- **Source:** `docs/02-tasks.md`.
- **Rule:** AI works on **one task at a time**.
- **Process:**
  1. Read task.
  2. Read `06-rules.md`.
  3. Execute TDD loop.
  4. Mark task [x].

### 2. TDD (Test-Driven Development)
- **The Cycle:**
  1. **Red:** Write failing test.
  2. **Green:** Write minimal code to pass.
  3. **Refactor:** Optimize code (Human reviews here).
- **Safety Net:** If tests fail, revert. Do not debug blindly.

### 3. CDD (Component-Driven Development)
- **Constraint:** No file > 300 lines.
- **Constraint:** Components must be isolated (pure functions where possible).

### 4. Institutional Memory (`04-changelog.md`)
- **Critical Step:** After every feature, the agent writes to `04-changelog.md`:
  - *What changed?*
  - *Why?*
  - *What mistake did we make that we shouldn't repeat?*
- **Reason:** This prevents the "Loop of Death" where AI repeats the same error.

---

## Phase 3: Validation & Maintenance (The "Quality Gates")

### 1. Layered Validation
- **Gate 1 (Static):** Linter / Type Checker (Automated).
- **Gate 2 (Logic):** Unit Tests (TDD).
- **Gate 3 (Contract):** Integration Tests / API Contracts (CDD).
- **Gate 4 (Human):** Review against `01-plan.md`.

### 2. Context pruning
- **Weekly Ritual:** Move completed tasks from `02-tasks.md` to an archive.
- **Reason:** Keeps the context window clean for the AI.

---

## Quick Start: The "Day 1" Script

1. **Initialize:**
   `mkdir docs && touch AGENTS.md docs/00-draft.md docs/01-plan.md docs/02-tasks.md docs/03-architecture.md docs/04-changelog.md docs/06-rules.md`

2. **Define:**
   - Fill `AGENTS.md` with the "Constitution".
   - Brainstorm in `00-draft.md`.
   - Solidify in `01-plan.md`.

3. **Architect:**
   - Define folders in `03-architecture.md`.
   - Define rules in `06-rules.md`.

4. **Execute:**
   - Add first task to `02-tasks.md`.
   - Start AI Agent.

---

## Why FORGE Works
It treats the AI not as a magic genie, but as a **junior developer with amnesia**.
- **Structure (RDD/DDD)** gives it long-term memory.
- **Tests (TDD)** give it immediate feedback.
- **Tasks (Kanban)** give it focus.
- **Changelog** gives it wisdom.
