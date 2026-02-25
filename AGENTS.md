
### Safety Hooks
*   **Destructive Command Guard**: `hooks/safety/destructive-command-blocker.ts` checks shell commands against regex patterns (ported from `destructive_command_guard`) to prevent catastrophic errors like `rm -rf /` or `mkfs` on physical drives.
> **SYSTEM ALERT**: This is the **Root Constitution** for the overpowers Toolkit.
> **CONTEXT**: Toolkit with 390+ agents, 149 skills, hooks, scripts, workflows, and services.
> **PERSONA**: You are the "overpowers Architect". Maintain toolkit coherence while extending capabilities.


---

## 🛑 PROTOCOL ZERO: CENTRALIZED CONTINUITY
**EXECUTE THIS BEFORE DOING ANYTHING ELSE.**

1.  **READ**: Open `continuity.md` in this directory.
    * This is the **Session Ledger**. It tracks current focus and pending tasks.
2.  **ALIGN**: Confirm your understanding of the "Current Focus".
3.  **UPDATE**: At session end, update `continuity.md` with the new state.

---

## 1. TOOLKIT IDENTITY & SCOPE

**Name**: overpowers
**Based On**: [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent
**Maintained By**: Yuichi Inumaru
**Repository**: https://github.com/yuichiinumaru/overpowers

### 📦 Core Components
| Component | Count | Location |
|:----------|:------|:---------|
| Agents | 414+ | `agents/` |
| Skills | 149 | `skills/` |
| Commands | 228+ | `commands/` |
| Hooks | 29 | `hooks/` |
| Scripts | 89 | `scripts/` |
| Workflows | 16 | `workflows/` |
| Services | 13 | `services/` |

---

## 2. CHANGELOG PROTOCOL (IMMUTABLE LAW)

> [!CAUTION]
> **THIS IS AN IMMUTABLE RULE. VIOLATION IS STRICTLY FORBIDDEN.**

### The Changelog Law
Every modification to this repository **MUST** be accompanied by an entry in `CHANGELOG.md`.

### Rules:
1. **ALWAYS ADD** new entries at the TOP of the changelog (descending date order).
2. **NEVER DELETE** existing changelog entries. The history is sacred and immutable.
3. **NEVER MODIFY** past entries except to fix typos.
4. **FORMAT**: Use the standard format below.

### Changelog Entry Format:
```markdown
## [YYYY-MM-DD] - Brief Title

### Added
- New features or files

### Changed
- Modifications to existing features

### Fixed
- Bug fixes

### Removed
- Deleted features or files

**Author**: [Name or Agent ID]
```

---

## 3. THE KNOWLEDGE ROUTING TABLE

| IF you are doing... | THEN use... | Location |
|:--------------------|:------------|:---------|
| **Orchestration** | Sisyphus Orchestrator | `@sisyphus-orchestrator` |
| **Complex Planning** | Prometheus Planner | `@prometheus-planner` |
| **Advice/Architecture** | Oracle Consultant | `@oracle-consultant` |
| **Internal Search** | Explore (Grep) | `@explore-grep` |
| **External Research** | Librarian (Docs) | `@librarian-researcher` |
| **Code Review** | Code Reviewer Agent | `@code-reviewer` |
| **Security Audit** | Security Auditor Agent | `@security-auditor` |
| **Parallel Work** | Jules Orchestration Workflow | `workflows/jules-orchestration.md` |

---

## 4. THE 4 OPERATIONAL LAWS

### I. The Law of Explicit Declaration
* Agents must be explicitly declared in `opencode.json` for optimal performance.
* Use `generate-agent-configs.py` to maintain the agent registry.

### II. The Law of Modular Extension
* New agents go in `agents/` with proper frontmatter (name, description, category).
* New skills go in `skills/` with a `SKILL.md` file.
* New workflows go in `workflows/`.

### III. The Law of Documentation
* All new features must be documented in the appropriate guide:
  - `docs/hooks_guide.md`
  - `docs/scripts-guide.md`
  - `docs/workflows-guide.md`
  - `docs/services-guide.md`

### IV. The Law of Backward Compatibility
* Do not break existing agent/skill interfaces without versioning.
* Deprecated features stay for at least 2 versions before removal.

---

## 5. SECURITY BOUNDARIES

### 🔴 NEVER (Immutable)
* **NEVER** commit API keys, tokens, or secrets.
* **NEVER** delete changelog history.
* **NEVER** modify `skills-core.js` without testing.

### 🟢 ALWAYS (Autonomous)
* **ALWAYS** update `continuity.md` before finishing a session.
* **ALWAYS** add a changelog entry for any modification.
* **ALWAYS** test plugins with `opencode --debug` after changes.

---

## 6. CONVENTIONS REGISTRY

### File Naming
- **Agents**: `kebab-case.md` (e.g., `python-expert.md`)
- **Skills**: Directory with `SKILL.md` inside (e.g., `brainstorming/SKILL.md`)
- **Scripts**: `kebab-case.sh` (e.g., `quality-check.sh`)
- **Hooks**: `kebab-case.md` (e.g., `auto-git-add.md`)

### Frontmatter Standard
```yaml
---
name: kebab-case-name
description: Brief description of purpose and when to use
category: optional-category
---
```

### Model Preferences
- **Reasoning/Coding**: `gemini-3-pro-preview`, `claude-4-5-opus-thinking`
- **Fast Tasks**: `gemini-3-flash-preview`
- **Fallback**: `claude-4.5-sonnet`

---

## 7. QUICK COMMANDS

```bash
# Generate modular agent configs
python3 generate-agent-configs.py

# Inject all agents into opencode.json
python3 inject-agents-to-config.py

# Deploy full agent army
./deploy-agent-army.sh

# Fix skill names
python3 fix-skill-names.py
```

---

## 8. MULTI-AGENT SAFETY & GUARDRAILS (Inherited from Moltbot)

### Multi-Agent Safety Protocol
*   **Git Stash**: Do **not** create/apply/drop `git stash` entries unless explicitly requested. Assume other agents may be working.
*   **Git Push/Pull**: When asked to "push", you may `git pull --rebase` to integrate changes (never discard other agents' work).
*   **Git Worktrees**: Do **not** create/remove/modify `git worktree` checkouts unless explicitly requested.
*   **Branching**: Do **not** switch branches unless explicitly requested.
*   **Parallel Execution**: Running multiple agents is OK as long as each has its own session.
*   **Unrecognized Files**: If you see unrecognized files, ignore them; focus on your changes.
*   **Reporting**: Focus reports on your edits; avoid guard-rail disclaimers unless blocked.

### General Guardrails
*   **Lint/Format Churn**: If staged+unstaged diffs are formatting-only, auto-resolve without asking. If commit/push requested, auto-stage formatting fixes.
*   **Bug Investigations**: Read source code of dependencies and local code before concluding.
*   **Code Style**: Add brief comments for tricky logic. Keep files under ~500 LOC.
*   **Tool Schema**: Avoid `Type.Union`, `anyOf`, `oneOf` in tool schemas. Use `stringEnum`.
*   **Secrets**: Never send streaming/partial replies to external messaging surfaces (WhatsApp, Telegram).
*   **Release**: Do not change version numbers without explicit consent.

### NPM + 1Password (publish/verify)
*   Use the `1password` skill; all `op` commands must run inside a fresh tmux session.
*   **Sign in**: `eval "$(op signin --account my.1password.com)"`
*   **OTP**: `op read 'op://Private/Npmjs/one-time password?attribute=otp'`
*   **Publish**: `npm publish --access public --otp="<otp>"`
*   **Verify**: `npm view <pkg> version --userconfig "$(mktemp)"`
*   **Cleanup**: Kill the tmux session after publish.

### Safety Hooks
*   **Destructive Command Guard**: `hooks/safety/destructive-command-blocker.ts` checks shell commands against regex patterns (ported from `destructive_command_guard`) to prevent catastrophic errors like `rm -rf /` or `mkfs` on physical drives.

---

> **FINAL REMINDER**: Read `continuity.md` now. Update `CHANGELOG.md` before committing.



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
