---
description: Perform a harmonious merge or rebase in Jujutsu VCS, resolving conflicts without artifacts.
category: utilities-vcs
argument-hint: "<source-rev> <destination-rev>"
allowed-tools: Bash(jj *), Read
---

# Jujutsu Harmonious Merge Command

This workflow guides you through the process of performing a harmonious merge or rebase in Jujutsu VCS. It ensures that any conflicts are resolved cleanly, preserving the integrity of your code.

## Steps

1.  **Initiate Merge/Rebase**
    -   Run `jj rebase -s $1 -o $2` (or `jj merge $1 $2` if a merge is required).
    -   Identify if any conflicts have appeared in the output.

2.  **Safety First**
    -   Run `jj oplog` to see the current history of operations. If things go wrong, you can always use `jj op restore <id>` to instantly revert the repository to the precise state before you started working.
3.  **Analyze Conflicts**
    -   Run `jj log` and `jj st` to see conflicted files.
    -   If the commit is doing too much and conflicts are sprawling, use `jj split <conflicted-rev>` to peel apart independent changes into separate commits.

4.  **Start Resolution Protocol**
    -   You can either resolve inline on the current conflicted commit, or create a new commit on top of the first conflicted revision: `jj new <conflicted-rev>`.
    -   Iterate through each conflicted path.

5.  **Execute Harmonious Resolution**
    -   For each conflicted file, analyze the markers and reconcile changes.
    -   Edit the file inline to produce the desired conflict-free state.
    -   Use `jj describe` or `jj commit -m "resolution"` if you created a separate commit for the resolution.

6.  **Finalize and Squash**
    -   If you made a separate commit to resolve the conflict, run `jj squash` to integrate the resolutions into the history seamlessly.
    -   Check `jj log` to ensure no `(conflict)` markers remain.

7.  **Verification**
    -   Run your project's test suite to ensure the merge has not introduced functional regressions.
    -   Review the final diff with `jj diff`.

## Success Criteria

-   ✅ No conflict markers remain in the codebase.
-   ✅ The history shows a clean resolution.
-   ✅ All tests pass.
