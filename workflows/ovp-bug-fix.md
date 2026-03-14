---
description: Systematic workflow for fixing bugs including issue creation, branch management, and PR submission
category: version-control-git
argument-hint: <bug_description>
allowed-tools: Bash(git *), Bash(gh *)
---

1. **Context Initialization (Explicit Memory Read)**: 
   - Read `.agents/continuity-<agent-name>.md` and check `.agents/memories/` to identify if this bug relates to recent changes or known environment issues.

2. Understand the bug: $ARGUMENTS

3. Before Starting:
   - GITHUB: create an issue with a short descriptive title.
   - GIT: checkout a branch and switch to it.

4. Fix the Bug

5. On Completion:
   - GIT: commit with a descriptive message.
   - GIT: push the branch to the remote repository.
   - GITHUB: create a PR and link the issue.

6. **Memory Synchronization (Explicit Memory Update)**: 
   - Update `.agents/continuity-<agent-name>.md` with the bug fix details and resolution.
   - Persist any root cause discovery or environment quirk to `.agents/memories/` via Serena.
