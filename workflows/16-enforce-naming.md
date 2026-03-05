---
description: Verify and enforce the strict filename conventions across the docs/ directory as defined in AGENTS.md.
argument-hint: Optional sub-directory (e.g., docs/tasks)
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Ensure all files in `docs/` and its subdirectories adhere to the strict `type-subtype-nnnn-names.md` and `nnnn-type-subtype-names.md` conventions, identifying outliers and safely renaming them.

## Execution Flow

1. **Extract Validation Rules.**
   - Read `AGENTS.md` -> "5. FILENAME & NAMING CONVENTIONS".
   - Rule A (General Files): `type-subtype-nnnn-names.md` (lowercase, hyphens).
   - Rule B (Tasks in `docs/tasks/`): `nnnn-type-subtype-names.md`.
   - Rule C (No Spaces/CamelCase/Underscores): Lowercase and hyphens only.
   - Rule D (Task SDD Companions): Must end in `-feature-plan.md` or `-technical-design.md`.

2. **Scan the Documentation.**
   - Recursively list all files in `docs/`.
   - If `$ARGUMENTS` specifies a folder, restrict to that folder.

3. **Identify Violations.**
   - For each file, check against the regex/rules.
   - Flag files with spaces, underscores, uppercase letters, or camelCase.
   - Flag task files in `docs/tasks/` missing the 4-digit chronological prefix (`nnnn`).
   - Identify files that clearly look like tasks but are missing the structure.

4. **Propose Renames (Auto-Fix Plan).**
   - For every flagged file, generate a proposed new name.
     - Example: `Auth System Design.md` -> `0021-feature-auth-system-design.md` (inferring next number).
     - Example: `feature_plan_legacy.md` -> `feature-plan-0001-legacy.md`.
   - Map existing references: Before renaming, search the codebase for references to the old filename.

5. **Execution and Redirection.**
   - Present the list of proposed renames to the user.
   - If the user approves, execute the `mv` command for each file.
   - Simultaneously, run a search-and-replace to update any links pointing to the renamed files in `tasklist.md`, `README.md`, or other docs.
   - Log the mass rename operation to `CHANGELOG.md`.

6. **Summary.**
   - Inform the user of files renamed and references updated.
