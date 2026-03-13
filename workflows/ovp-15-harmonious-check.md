---
description: Sweep the workspace for violations of Jujutsu VCS boundaries and validate agent configuration schemas.
argument-hint: Optional
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Act as an internal health-check layer to guarantee that the project isn't slowly accumulating broken state (e.g., Git detaching from JJ, malformed agent frontmatter).

## Execution Flow

1. **VCS Integrity Check.**
   - Run `jj status` and `git status`.
   - Detect if `.git/HEAD` is detached in a way that implies someone used `git checkout` manually (violating Regra 10.1).
   - Detect unresolved conflicts stuck in Git that JJ can't see properly.
   - If severe issues are found, recommend using `harmonious-jujutsu-merge` skill to recover.

2. **Agent Schema Validation.**
   - Traverse the `agents/` and `.agents/` directories.
   - For every `.md` file with YAML frontmatter:
     - Verify that the `tools` field is a dictionary (record) and not an array (Regra 6).
     - Verify that the `color` field uses double-quoted valid hex code (Regra 6).
     - Verify valid models are specified (`gemini-3.1-pro`, `claude-4.6-opus-thinking`, etc.) and no deprecated models are hardcoded.

3. **Orphan Control.**
   - Check for loose code files unexpectedly dropped in root directory or `.agents/tmp/` that haven't been touched in 24h.

4. **Reporting and Auto-Fix.**
   - Attempt to auto-fix YAML formatting (quotes in hex colors, dict conversion).
   - Generate a single brief markdown report `.agents/reports/harmonious-check.md`.
   - Print a summary to the user highlighting any critical VCS state corrections needed.
