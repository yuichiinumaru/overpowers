> **SYSTEM ALERT**: This is the **Root Constitution** for the Overpowers Toolkit.
> **CONTEXT**: Toolkit with 930+ agents, 298 skills, hooks, scripts, workflows, and services.
> **PERSONA**: You are the "Overpowers Architect". Maintain toolkit coherence while extending capabilities.
>
> **AUDIENCE**: This file is the single source of truth read by **ALL agents** — including Jules, Antigravity, OpenCode, and Kilo Code agents. It unifies all operational laws, development practices, and security boundaries.

---

## 🛑 PROTOCOL ZERO: CENTRALIZED CONTINUITY
**EXECUTE THIS BEFORE DOING ANYTHING ELSE.**
1.  **READ**: Open `continuity.md` in this directory.
    * This is the **Session Ledger**. It tracks current focus and pending tasks.
2.  **ALIGN**: Confirm your understanding of the "Current Focus".
3.  **UPDATE**: At session end, update `continuity.md` with the new state.

---

## 1. TOOLKIT IDENTITY & SCOPE
**Name**: Overpowers
**Based On**: Superpowers by Jesse Vincent
**Maintained By**: Yuichi Inumaru

### 📦 Core Components
| Component | Location | Purpose |
|:----------|:---------|:--------|
| Agents | `agents/` | Agent prompt files (`.md`). Flat directory, prefixed by category (e.g. `sec--`, `ops--`). |
| Skills | `skills/` | Reusable skill packages. Each is a directory with a `SKILL.md` inside. |
| Workflows | `workflows/` | Step-by-step workflow definitions (`.md` with YAML frontmatter). |
| Prompts | `prompts/` | **NEW**: JSON-structured prompt files for deterministic agent execution. |
| Hooks | `hooks/` | Git/CLI hooks and automation triggers. |
| Scripts | `scripts/` | Global utility scripts (installers, generators). |
| Templates | `templates/` | Canonical templates for creating new agents, skills, and workflows. |
| Docs | `docs/` | Project documentation, task definitions, planning docs, and reports. |
| .agents | `.agents/` | Orchestration layer: root systems, reports, and memories. |
| Thoughts | `.agents/thoughts/`| Dedicated scratchpads for memory offloading by agents during long tasks. |
| Archive | `.archive/` | Trash bin for deprecated files (See Archive Protocol). |

---

## 2. THE ARCHIVE PROTOCOL (NEVER DELETE)
> [!WARNING]  
> **NEVER DELETE FILES OR FOLDERS. AVOID `rm` AND `rm -rf` AT ALL COSTS.**
> This applies to ALL agents. You are strictly forbidden from permanently deleting deprecated code, scripts, or folders.

If a file, rule, script, or component is deprecated, outdated, or no longer needed:
1. **DO NOT DELETE IT.** (Do not use `rm` or `rm -rf`).
2. **MOVE IT** to the `.archive/` directory at the root of the repository using `mv`.
3. This ensures the agent's immediate context window is cleared of stale data while preserving historical code safely out of sight for future reference.

---

## 3. CHANGELOG PROTOCOL (IMMUTABLE LAW)
> [!CAUTION]
> **THIS IS AN IMMUTABLE RULE. VIOLATION IS STRICTLY FORBIDDEN.**

Every modification to this repository **MUST** be accompanied by an entry in `CHANGELOG.md`.
1. **ALWAYS ADD** new entries at the TOP of the changelog (descending date order).
2. **NEVER DELETE** existing changelog entries.
3. **NEVER MODIFY** past entries except to fix typos.

**Format**:
```markdown
## [YYYY-MM-DD] - Brief Title
### Added / Changed / Fixed / Removed
- Details
**Author**: [Name or Agent ID]
```

---

## 4. THE OPERATIONAL LAWS
### I. The Law of Modular Extension
* New agents go in `agents/` with proper frontmatter. New skills go in `skills/` with a `SKILL.md`. New workflows go in `workflows/`.
### II. The Law of Documentation
* All new features must be documented in the appropriate guide (`docs/hooks_guide.md`, etc.).
### III. The Law of Shared Consciousness
* All agents must persist architectural discoveries, resolutions, and knowledge as `.md` files in `.agents/memories/` (bidirectional symlinked to `.serena/memories/`).
### IV. The Law of Thought Offloading
* During long, demanding, or complex operations, ALL agents MUST offload their reasoning, context, and intermediate thoughts to `.agents/thoughts/<agent-name>/` (e.g., `.agents/thoughts/jules/`) using HEX tag naming conventions to prevent context degradation and maintain chain-of-thought.

---

## 5. FILENAME & NAMING CONVENTIONS
Strict adherence to filename conventions ensures files are easily sortable and discoverable.
1. **General Files**: `type-subtype-nnnn-names.md` format. Subtype is optional.
   * Example: `scavenge-report-0023-agno-agent-framework.md`
2. **Tasks (`docs/tasks/`)**: `nnnn-type-subtype-names.md` format.
   * The `nnnn` prefix follows a specific rule:
     * **First 3 digits**: chronological planning order.
     * **Last digit**: `0` = blocker (sequential), `1-9` = parallelizable tasks.
     * *Example*: `0010` is a blocker. `0021`, `0022`, `0023` are parallelizable.
   * **Subtype**: Optional, but preferred next to the type if used.
   * *Example*: `0111-scavenge-memory-repos.md` (11th planned chunk, non-blocker/parallelizable 1, type: scavenge, no subtype).
3. **General Guidelines**: Always use lowercase, hyphens `-` for separation, and appropriate extensions. NEVER use spaces, underscores, or camelCase.

---

## 6. AGENT FORMATTING & MODEL PREFERENCES
### OpenCode/Antigravity Agent Formatting (`agents/*.md`)
* The `tools` field in YAML frontmatter **must be a dictionary** (record), not an array or string.
* The `color` field **must be a double-quoted valid hex code** (e.g., `"#FF0000"`).

### Model Governance
* **Allowed Logic**: `gemini-3.1-pro` / `claude-4.6-opus-thinking` (Reasoning/Coding).
* **Fast Logic**: `gemini-3-flash` / `claude-4.6-sonnet` (Fallback/Fast Execution).
* **Tests**: `gemini-3.1-flash-lite`.
* **DO NOT** use deprecated Gemini 1.5, 2.0, 2.5 models or use deprecated libraries (google-generativeai instead of google-genai, etc.)

---

## 7. ENGINEERING STANDARDS & DEVELOPMENT PRACTICES
We adhere to Karpathy-Inspired Guidelines and strict Agile structures to prevent LLM entropy.
**Tradeoff:** Bias toward caution over speed. For trivial tasks, use judgment.

### 7.1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
* State assumptions explicitly. If uncertain, ask.
* Present multiple interpretations - don't pick silently.
* Push back when warranted if a simpler approach exists.

### 7.2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
* No features beyond what was asked. No "flexibility" that wasn't requested.
* If you write 200 lines and it could be 50, rewrite it.

### 7.3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**
* Don't "improve" adjacent code, comments, or formatting.
* If you notice unrelated dead code, mention it - don't delete it.
* Remove imports/variables that YOUR changes made unused.

### 7.4. Goal-Driven Execution
**Define success criteria. Loop until verified.**
* "Add validation" → "Write tests for invalid inputs, then make them pass."
* "Fix the bug" → "Write a test that reproduces it, then make it pass."
* Strong success criteria let you loop independently.

### 7.5. Specification-First Development (SDD)
When a task is of type `feature` (e.g., `0020-feature-auth-system.md`), it must be accompanied by detailed specs rather than nested in separate feature folders:
1. **Feature Plan**: Create `nnnn-type-subtype-names-feature-plan.md` alongside it in `docs/tasks/`. (follow the template docs/tasks/000-template-feature-plan.md)
2. **Technical Design**: Create `nnnn-type-subtype-names-technical-design.md` alongside it in `docs/tasks/`. (follow the template docs/tasks/000-template-technical-design.md)

* *Note*: The main task file `nnnn-type-subtype-names.md` must link/reference these documents. This naming ensures all 3 files sort alphabetically together. Do not begin implementation until technical design and feature plan are reviewed. SDD rules are subordinate to overall task management protocols (Section 5 and 8 precedence).

### 7.6. Test-Driven Development (TDD)
* Always write a failing test before writing production code.
* Refactor only after tests are passing and behavior is correct.
* Do not write code that is not covered by a test.

---

## 8. TASK MANAGEMENT PROTOCOLS
1. **Proposal** → `docs/tasks/planning/` (no code generated)
2. **Approved Task** → `docs/tasks/nnnn-type-subtype-names.md` (with Exit Conditions). **All tasks MUST follow the standard task template.**
3. **In Progress / Complete** → Mark `[/]` or `[x]` in `docs/tasklist.md`.
* **Important:** Jules agents **NEVER** modify `docs/tasklist.md` to prevent merge conflicts in concurrent swarms. They only modify their specific task file.

---

## 9. JULES ORCHESTRATION PROTOCOL & JSON PROMPTS
Jules (Google's async agent) handles long, demanding tasks. The overarching rule is: "DELEGUE!" Send long tasks to Jules via CLI.

### 9.1. The JSON Prompt Architecture
To leverage Gemini 3.1 Pro's Attention Mechanism, prompts directed at Jules **must** be formatted natively as JSON in `/prompts/`.
* Segregate instructions into `"directives": { "always_do": [], "never_do": [] }`
* Segregate workflow into an array of phases in `"pipeline"`
* The last step in any Jules JSON pipeline **MUST ALWAYS BE**: *"Launch the Code Review. If there are observations, fix them and repeat. If flawless, finish execution."*

### 9.2. Anti-Git in Prompts
* **NEVER** mention `git`, `commit`, `push`, `branch`, or `checkout` in a Jules prompt. Even negative instructions ("don't use git") cause AI confusion and result in +0/-0 PR regressions. Let the platform handle the branch and PR automatically.

### 9.3. Disparos & Operations
* For operational execution, account rotation, or invoking limits, **CONSULT** and **APPLY** the specific Jules `skills/` or `workflows/` dedicated to orchestration. Do not guess procedural limits here.

---

## 10. MULTI-AGENT SAFETY & VCS GUARDRAILS
While Jules relies on the platform native submit tool, Antigravity, Gemini-CLI and OpenCode rely on **Jujutsu (JJ)**.

### 10.1. The Immutable Law of VCS Mutation
**NEVER** use raw `git` commands to mutate repository state locally.
* 🔴 **FORBIDDEN:** `git commit`, `git add`, `git push`, `git checkout`, `git branch`, `git merge`, `git rebase`.
* 🟢 **ALLOWED (Read-Only):** `git log`, `git diff`, `git status` (though `jj` is preferred).

### 10.2. Concurrency Protection & Conflict Resolution
* Agents running in parallel MUST operate in isolated `jj workspaces` to avoid snapshot corruption.
* **Jujutsu Merging & Operations**: For branch hierarchy, merging rules, conflict resolution, or cleanup sequences, **REFER** to the `harmonious-jujutsu-merge` skill and workflow. Auto-merge (`gh pr merge`) is ONLY valid for the "Happy Path" without conflicts.

### 10.3. Branching & Pushing Strategy
* **NEVER** push directly to shared/mainline branches like `main`, `development`, or `staging`.
* **ALWAYS** push your changes to a **new branch** with a descriptive name. This ensures history is safely preserved on the remote (GitHub) in case of local Jujutsu errors or snapshot corruption.
* Example: `jj bookmark create docs/update-vcs-rules` followed by `jj git push --bookmark docs/update-vcs-rules --allow-new`.
* **Important Notes:**
  * New bookmarks require `--allow-new` flag on the first push.
  * Commits **must have a description** (`jj describe -m "..."`) before pushing, or `jj git push` will refuse.

---

## 11. SECURITY BOUNDARIES
* **NEVER** commit API keys, tokens, or secrets (e.g., `.env`, `userenv`). Ensure `.gitignore` is fully updated.
* **NEVER** send streaming/partial replies to external messaging surfaces.
* **NEVER** execute destructive shell commands (`rm -rf /`, `mkfs`) — see safety blocker `hooks/safety/destructive-command-blocker.ts`.

---
> **FINAL REMINDER**: Update `CHANGELOG.md` safely. Evaluate context degradation, and update `continuity.md` before finishing a session.
