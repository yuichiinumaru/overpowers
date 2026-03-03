# 🤖 KHALA AGENTS CONSTITUTION

> **Status**: Active
> **Version**: 2.3
> **Last Updated**: 2026-02-10

This document serves as the **Constitution** for all AI Agents working on the Khala project. It defines the core principles, architectural constraints, and operational workflows that you **MUST** follow.

## 0. 🧠 PRIME DIRECTIVES (Metaprompt)

### 0.0. 🔑 SESSION INITIALIZATION PROTOCOL (MANDATORY)
**At the start of EVERY session, regardless of the task, you MUST perform these steps in order BEFORE doing anything else:**
1. **Read your Memories/Knowledge**: Read ALL memories and knowledge items you have about this repository. This is your accumulated institutional knowledge. Do not skip this. Use memcord MCP, serena MCP, and native Antigravity 'Knowledge'. Then, assess the availability of Skills and other tools and MCPs.
2. **Map the Repository Structure**: Run `tree -d -L 3 -I 'node_modules|__pycache__|.git|.jj|.pytest_cache|*.egg-info' > docs/tree.md` to understand the current folder structure. Read the output.
3. **Read the Constitution**: Read this file (`AGENTS.md`) in full.
4. **Read the Tasklist**: Read `docs/tasklist.md` to understand the current priorities, blockers, and parallelizable tasks.
5. **Scan Active Tasks**: Skim `docs/tasks/` (only the filenames and headers) to understand what detailed implementation plans exist.

**Why**: Without this initialization, you will lose context, repeat mistakes, create files in wrong locations, and waste the user's time. This protocol exists because these failures have happened many times.

1. **USER IS KING**: The user's explicit request in the current prompt **ALWAYS** overrides any instruction in this file or memory.
2. **CONTEXT IS KEY**:
   - `docs/tasklist.md` = **The Single Source of Truth** for project status.
   - `docs/tasks/` = **How to Implement** (Detailed Plans for open tasks).
   - `docs/tasks/complete/` = **Already Done** (Completed task files, for reference only).
   - `docs/architecture/specs/` = **What to Implement** (Technical Specs).
3. **GRANULARITY**: Write tasks as detailed as possible. Use subtasks and sub-subtasks.
4. **NO DETAIL LEFT BEHIND**: Every technical detail counts. Use multi-step edits if necessary.
5. **HIERARCHICAL SCALING**: If a document exceeds 800 lines, create a subdirectory (e.g., `docs/01-plans/`) and move details there, keeping a synthetic version in the main file.
6. **ARCHIVE FIRST**: Never delete files. Move them to `docs/archive/` before refactoring.
7. **PER-TASK REPORTS**: Agent reports go in `.agents/reports/` using the pattern `{agent}-{task-id}.md` (e.g., `foreman-101-agno-dump-cleanup.md`). NEVER write to a shared monolithic file — this causes merge conflicts with parallel agents.
8. **EXTRACTION PROTOCOL**: Archive first, then extract information to new files.
8. **EDIT(VITAL_FILE) $\implies$ ASK(USER)** (Vital files: `AGENTS.md`, `README.md`, `.env*`).

---

## 1. 🏗️ CANONICAL STRUCTURE

### Source Code (`khala/`)
- `domain/`: Pure business logic and entities. No external dependencies.
- `application/`: Service orchestration and use cases.
- `infrastructure/`: External adapters (Gemini, SurrealDB, CLI).
- `interface/`: Entry points (REST API, CLI, MCP).

### Documentation (`docs/`)
- `tasklist.md`: **THE SINGLE SOURCE OF TRUTH** for all project tasks. Always check this first.
- `tasks/`: Detailed implementation plans for each task block.
- `architecture/`: System design and structure documents.
- `specs/`: Technical specifications and theory.
- `analysis/`: Reports, audits, and external repository analysis.
- `archive/`: Deprecated plans and documentation.
- `sops/`: Standard Operating Procedures.
- `thoughts/`: Developer notes and context dumps.

## 📜 RULES OF ENGAGEMENT

1. **CHECK TASKLIST FIRST**: Before starting any work, read `docs/tasklist.md` to understand the current priorities and context.
2. **NEVER DELETE**: Do not delete documentation. Move outdated files to `docs/archive/`.
3. **SEPARATE CONCERNS**: Keep "Plans" (Why/How) in `docs/tasks/` and "Specs" (What) in `docs/architecture/specs/`.

---

## 2. 🏗️ SYSTEM STATUS (v2.0 - Production Ready)
**Overall Completion**: 87%
**Verification**: 22/22 Core Strategies Implemented

### ✅ IMPLEMENTED & VERIFIED
- **Storage**: Vector (HNSW), Graph, Document, 3-Tier Hierarchy.
- **Advanced Features**: Multimodal (Image/Text), MCP Server, Human-in-the-Loop (Approval Service), Skill Library.
- **Reasoning**: **Refinement Loop (SOAR)**, **Product of Experts (PoE)**.
- **Infrastructure**: SurrealDB v2.0, Agno, Gemini 2.5 Pro.

### ⚠️ CRITICAL GAPS (Needs Integration)
These components exist in the codebase but require wiring into the main pipeline:
1.  **Self-Verification Gate**: `VerificationGate` logic exists but is not called in `MemoryLifecycleService`.
2.  **Distributed Consolidation**: Consolidation logic is currently in-process (`asyncio.gather`). Needs Redis/Queue worker separation for scale.
3.  **Intent Classification**: `IntentClassifier` exists but is disabled by default in search.
4.  **LLM Cascading**: Logic exists in `GeminiClient` but some services use hardcoded model IDs.

---

## 3. 🤖 MODEL STANDARDS
All agents and services MUST adhere to these model configurations:

| Role | Model ID | Use Case |
| :--- | :--- | :--- |
| **Reasoning / Logic** | `gemini-3.1-pro-preview` | Complex analysis, debate, consolidation (thinking=high). |
| **Fast / Routine** | `gemini-3-flash-preview` | Classification, simple summaries. |
| **Embeddings** | `models/gemini-embedding-001` | 768d text embeddings (Compatibility mode). |
| **Multimodal** | `models/multimodal-embedding-001` | Image/Vision embeddings. |

**RESTRICTIONS**:
- **NO GPU ACCELERATION**: Do not implement CUDA/ONNX local embeddings. Use Gemini API only.
- **NO HARDCODED MODELS**: Use `ModelRegistry` for model selection whenever possible.
- **NO DEPRECATED LIBS**: Never, under ABSOLUTE ANY circunstance, use the **deprecated** lib `google-generativeai` - instead, use ALWAYS `google-genai` (lib generativeai is deprecated for a long time).

---

## 4. 🛠️ ENGINEERING KERNEL (VIVI OS v2.2 Integration)

### A. ARCHITECTURE (Two-Layer Graph)
**Directives:**
1.  **Separation:** Frontend $\cap$ Backend = $\emptyset$.
2.  **Flow:** $User \to L_1 \to L_2 \to L_{Worker} \to L_2 \to L_1 \to User$.
3.  **Constraint:** Direct SQL in Controllers = $\bot$ (Forbidden).

### B. OPERATIONAL MODES
The Agent MUST switch states based on `Task_Type`.

*   **Mode A: PROACTIVE (Default)**
    *   **Trigger:** Feature | Refactor | Docs
    *   **Algorithm:** Read Docs -> Plan -> Test (Red) -> Code (Green) -> Verify.
    *   **Constraint:** No chatter ("I will do..."). Just Code.

*   **Mode B: PARANOID DETECTIVE (Debug)**
    *   **Trigger:** Error | Bug | Crash
    *   **Protocol:** Deconstruct -> Doubt -> Suspects -> Stakeout -> Verdict.
    *   **Constraint:** No Guesswork.

### C. CODING STANDARDS (The Stack)
- **Stack:** Python (Agno), TypeScript (Mastra).
- **Async First**: All I/O must be asynchronous (`async def`).
- **Type Hints**: Strict typing required.
- **Dependency Integrity**: Use lockfiles.
- **Security**: No secrets in code. Use `SurrealConfig` and env vars.

### D. WORKFLOW ALGORITHM (RPG Ritual)
1.  **Init (Discovery):** `ls -R`, Read Docs, Assert Knowledge.
2.  **Proposal (Structure):** If Impact > 1 File $\implies$ Update `docs/tasklist.md`.
3.  **CodeGen (TDD):** While Test Fails -> Analyze -> Fix Minimal -> Stop Loss (3 retries).
4.  **Scale (Doc Sync):** Update Changelog, Update Tasks.

### E. COGNITIVE WORKFLOW & MEMORY MANAGEMENT

**1. THOUGHTS (Cognitive Offloading Protocol)**:
- **Usage**: You MUST use the `.agents/thoughts/` folder freely and abundantly. It is your:
    1.  **Notebook**: For random ideas, observations, and hypotheses.
    2.  **Log**: For recording execution steps, failures, and successes.
    3.  **Context Dump**: To offload complexity so you can focus on the immediate task without losing the "Big Picture".
- **Filename Convention**: Use `.agents/thoughts/nnn-type-title.md` (e.g., `001-analysis-auth_service.md`, `002-plan-refactor_user_model.md`).
- **Structure**:
    -   You may create subfolders if complex. If you do, create a local `AGENTS.md` or `index.md` inside that subfolder explaining its structure.
    -   **Maintenance**: If you create a structure, you MUST maintain it.
- **Habit Formation**:
    -   *Trigger*: Before starting a complex task, ask: *"Should I log a thought about this?"*
    -   *Trigger*: When switching contexts, dump your current context to a thought file.
    -   *Trigger*: Every ~30 tool calls, write a partial report.
    -   **Warning**: Users become extremely frustrated when agents repeat mistakes or lose context. Abundant use of `.agents/thoughts/` is the primary defense against this.
- **Session Init**: **MANDATORY**: At the start of every session, you MUST read `.agents/thoughts/` (and its files) and then `docs/tasklist.md` before executing any user request.

**2. TREE (File Exploration)**:
- **Rule**: Whenever you need to "read all files" or explore a directory structure, **ALWAYS** generate a tree first: `tree -I 'node_modules|__pycache__|.git|.pytest_cache' > tree.md`.
- **Usage**: Use the generated `tree.md` as your map to systematically read files. Do not guess file paths.

**3. DETAILING (Information Fidelity)**:
- **Rule**: Never over-compact information when editing `AGENTS.md` or writing thoughts. **Details exist for a reason.**
- **Preservation**: You may systematize or structure information (bullet points, tables), but **NEVER OMIT** technical details, constraints, or user preferences.
- **Batching**:
    -   *Reading*: If a task is too large, break it into batches. Read batch A -> Note in `thoughts/` -> Read batch B.
    -   *Writing*: Use multi-step editing. Add content block by block rather than trying to rewrite the universe in one shot.

**4. CODE REVIEW (Self-Correction)**:
- **Rule**: **ALWAYS** review your code before committing.
- **Process**: After writing code, pause and analyze:
    -   *Is this the BEST possible solution?*
    -   *Does it respect the Architecture defined in `docs/architecture/architecture.md`?*
    -   *Did I break any existing tests?*
- **Constraint**: **NEVER** commit without this explicit self-review step.

---

## 🚀 ROADMAP (Immediate Priorities)

See `docs/tasklist.md` for the comprehensive, ordered list.

1.  **Phase 1: Stability Fixes** (Persistence, Caching, Agno Integration).
2.  **Phase 2: Agno Migration & MCP Gateway**.
3.  **Phase 3: Core Features** (Decay, Parallel Search, Consolidation).
4.  **Phase 4: Advanced Strategies**.

---

## 🚫 FORBIDDEN ACTIONS
- Do NOT delete `AGENTS.md` (Integrate edits only).
- Do NOT add binary files to git.
- Do NOT use synchronous database calls.
- Do NOT implement local GPU embedding models.
 

# Behavioral guidelines to reduce common LLM coding mistakes

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
