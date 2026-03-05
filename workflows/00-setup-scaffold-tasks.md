---
description: Scaffold the docs/tasks/ structure and copy task templates into a new or existing project.
argument-hint: Optional project path (defaults to current directory)
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Create the standard task management directory structure and populate it with the canonical templates from `templates/tasks/`.

## Execution Flow

1. **Determine target project.**
   - If `$ARGUMENTS` contains a path, use it. Otherwise, use the current working directory.

2. **Create directory structure.**
   - `docs/` (if missing)
   - `docs/tasks/` (if missing)
   - `docs/tasks/planning/` (if missing — this is where proposals go before approval)

3. **Copy task templates.**
   - Copy `templates/tasks/000-template.md` → `docs/tasks/000-template.md`
   - Copy `templates/tasks/000-template-feature-plan.md` → `docs/tasks/000-template-feature-plan.md`
   - Copy `templates/tasks/000-template-technical-design.md` → `docs/tasks/000-template-technical-design.md`
   - If any of these already exist, **do not overwrite**. Report which were skipped.

4. **Create tasklist tracker.**
   - If `docs/tasklist.md` does not exist, create it with:
     ```markdown
     # Task List
     
     > **Important:** Jules agents **NEVER** modify `docs/tasklist.md` to prevent merge conflicts in concurrent swarms. They only modify their specific task file.

     ## Active Tasks
     <!-- Mark [/] for in-progress, [x] for complete -->
     
     ## Completed Tasks
     ```

5. **Verify and report.**
   - List all files created.
   - List any files skipped (already existed).
   - Confirm the structure is ready for task management.
