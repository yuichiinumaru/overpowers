---
name: harmonious-jujutsu-merge
description: Specialized skill for resolving Jujutsu VCS conflicts harmoniously, preserving content without introducting markers or artifacts.
metadata:
  version: "1.0.0"
  author: "Antigravity - Overpowers"
---

# Harmonious Jujutsu Merge Skill

This skill is designed to guide AI agents through the process of resolving merge conflicts in Jujutsu VCS. Unlike traditional Git, Jujutsu treats conflicts as first-class citizens in the DAG, allowing for "harmonious" resolutions that are clean and artifact-free.

## When to Use

- When a `jj rebase` or `jj merge` results in a conflict.
- When you need to resolve conflicts while preserving the integrity of both branches.
- When you want to avoid manual marker editing and use Jujutsu's built-in resolution tools.

## The Harmonious Protocol

1.  **Identify Conflicted Commits**: Use `jj log -r 'conflicts()'` to list all commits with unresolved conflicts.
2.  **Safety First**: Consider using `jj oplog` to record the state of the repository before making changes. Provide `jj op restore <id>` as an emergency hatch if needed.
3.  **Start Resolution**: Edit the files inline or create a new commit on top of the conflicted commit: `jj new <conflicted-id>`.
4.  **Analyze Conflict**: Read the conflicted files. Jujutsu's conflict markers show exactly where the divergence happened.
5.  **Execute Resolution**: Create the correct file structure inline. Use `jj resolve` for automated resolutions or manually edit the file to the desired final state.
    -   *Harmonious Tip*: Use the version of the file that correctly integrates changes from both branches without introducing debugging markers.
    -   *Advanced Conflict DAG Tip*: If the commit handles too much at once, `jj split` to break up independent pieces.
5.  **Finalize Resolution**: Once the file is correct, run `jj squash` to move the resolution into the original conflicted commit.
6.  **Verify Result**: Check `jj log` and `jj diff` to ensure the conflict has been resolved and the history is clean.

## Troubleshooting

-   **Multiple Path Conflicts**: Run `jj resolve --list` to see all paths that need resolution.
-   **Accidental Markers**: If you find conflict markers (`<<<<<<< conflict`) in a finalized commit, you have failed the harmonious protocol. Rewind the operation log with `jj op restore` or `jj undo` and start over.
-   **Complex Merges**: If the conflict is too large, consider breaking the task into smaller PRs or using `jj split` to isolate the conflict into smaller discrete parts before resolution.
