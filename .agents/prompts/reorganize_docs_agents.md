## Role: Documentation & Task Architect
## Context: Project "Overpowers" is reorganizing its core strategy, transitioning legacy loose documents and agent lists into formal architectural workflows and actionable Jira-style tasks.

### Task Description: Reorganize `docs/` and `agents/` directories

The repository contains extensive `.md` files in `docs/` and `agents/`. Many of these files contain actionable feature requests, pending architectural plans, ideas, or strict reference guidelines. 

Your mission is to process these two directories and re-organize them into our new centralized system **WITHOUT LOSING A SINGLE DETAIL**.

### Action Plan & Rules
1. **Analyze `docs/` and `agents/`**: Read the contents of each file carefully.
   - If the file is strictly historical, architectural reference, or static knowledge, ensure it is moved/categorized properly within `docs/knowledge/` or its subfolders.
   - If the file contains actionable steps, feature requests, bugs, or ideas to be implemented, it must be converted into a formal Task.

2. **The `docs/tasklist.md` Master Index**:
   - Add every identified macro-task to `docs/tasklist.md`.
   - Use the exact naming convention for macro-tasks: `[ ] NNN-type-name-name-name` (e.g., `004-feature-mcp-integration` or `005-refactor-agents-core`).
   - Group them appropriately (Open, Completed).

3. **Detailed Task Files in `docs/tasks/`**:
   - For every macro-task added to the tasklist, create a corresponding markdown file in the `docs/tasks/` directory named exactly `NNN-type-name-name-name.md`.
   - Use the template structure found in `docs/tasks/000-template.md`.
   - **CRITICAL**: Migrate *all* the detailed rationale, steps, unfulfilled specs, and context from the original file into the `### Details` block (What, Where, How, Why) and map out the `## Exit Conditions (GDD/TDD)` accurately. No detail should be lost.

4. **Cleaning up Planning**:
   - Any files currently inside `docs/tasks/planning/` should also be converted into formal tasks inside `docs/tasks/` and then cleanly removed once securely migrated.

5. **Safe File Operations**:
   - Utilize standard Git/Jujutsu tracking for file moving (`mv`).
   - If a source file is entirely converted to a task, delete the old file so there is no duplicated lingering content. 
   - DO NOT edit `docs/tasklist.md` if you are acting as Foreman implementing code. However, **in this specific task**, your role is Planning & Reorganization, so modifying `docs/tasklist.md` is expected.

6. **Postamble**:
   - Confirm all content has been re-homed successfully.
   - Review your changes locally to ensure `tree.md` reflects a vastly cleaner `docs/` and `agents/` root. 
   - Save your final report indicating the mappings of moved files inside `.agents/reports/agent-NNN-docs-reorg.md`.
