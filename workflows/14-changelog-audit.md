---
description: Sweep the Jujutsu operation log to detect undocumented changes and automatically commit structured updates to CHANGELOG.md.
argument-hint: Optional time boundary (e.g., 'last 4 hours')
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Enforce the "Immutable Law of Changelog" autonomously by reading version control history and appending missing entries to `CHANGELOG.md` safely.

## Execution Flow

1. **Extract Version Control Diff.**
   - Run `jj op log --no-graph --limit 20` to understand recent operations.
   - Extract the diff between the current state and the last known good commit/tag.
   - Identify added files, modified files, and deleted files.

2. **Analyze Existing Changelog.**
   - Read `CHANGELOG.md`.
   - Identify the most recent date entry `## [YYYY-MM-DD]`.
   - Check if the mutations found in Step 1 are already documented.

3. **Synthesize Missing Entries.**
   - Categorize undocumented changes into `### Added`, `### Changed`, `### Fixed`, or `### Removed`.
   - Abstract low-level file diffs into human-readable features or bug fixes.
   - Format the entry exactly as prescribed:
     ```markdown
     ## [CURRENT-DATE] - Auto-Audit Merge
     ### Added
     - Feature description
     **Author**: Agent System
     ```

4. **Prepend to Changelog.**
   - If changes are needed, insert the synthesized block directly underneath the main `# Changelog` header (above the previous entries).
   - DO NOT modify or delete past entries (Immutable Law).

5. **Commit the Audit.**
   - Alert the user about the changelog update.
   - Suggest a quick `jj describe -m "chore: automated changelog audit"` to seal the operation.
