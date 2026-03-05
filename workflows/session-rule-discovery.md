---
description: Scan the current session to discover new business rules or organizational changes.
argument-hint: None
---

# /session-rule-discovery

**Goal**: Systematically scan the conversation history, tasks, and code modifications of an ongoing or completed session to identify implicit or explicit business rules, configuration changes, or architectural decisions that have not yet been formalized.

## Actions

1. **Session History Retrieval**:
   - Read the recent conversation logs.
   - Analyze intermediate thoughts (`.agents/thoughts/`), `task.md` executions, and git/jujutsu diffs from the session.

2. **Rule Extraction & Filtering**:
   - Extract patterns, instructions, and constraints established by the user (e.g., "always do this", "never use that library", "from now on format X like Y").
   - Filter out isolated bug fixes, temporary constraints, or project-specific edge cases. Retain only generic, repository-wide, or broadly applicable business and technical rules.
   - Evaluate whether these rules represent a permanent organizational change or a new "sculpting" constraint.

3. **Rule Formalization**:
   - Write out the distilled rules in a concise, authoritative format matching the `AGENTS.md` or `.agents/rules/` styling.
   - Follow the "never open-ended" philosophy, favoring negative constraints where applicable.

4. **Proposal Generation (Non-Destructive)**:
   - **Do not make arbitrary or destructive edits** directly.
   - Format the findings as a formal proposal or diff in a temporary markdown file or present it directly to the user via a review mechanism (`notify_user`).

5. **Approval & Integration**:
   - Await the user's approval.
   - Once approved, explicitly update `AGENTS.md` (or the relevant rules file) and commit the addition via Jujutsu.
