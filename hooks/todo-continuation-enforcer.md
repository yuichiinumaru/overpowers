# Todo Continuation Enforcer

This hook ensures that agents do not stop working while there are pending items in the active plan.

## Logic (extracted from oh-my-opencode)

1.  **Monitor Session Idle**: When the session becomes idle (agent stops generation).
2.  **Check Todo State**: Look for the active plan (e.g., via `update_plan` or `todoWrite` history).
3.  **Identify Pending Items**: Are there unchecked boxes `[ ]`?
4.  **Auto-Prompt**: If pending items exist, automatically inject a user message:
    > "You have pending todos. Please continue working on the next item: [Next Item]. If you are stuck, ask for help."

## Implementation Guide

To implement this in overpowers (which is script/config based, not a runtime plugin):

1.  **Agent Prompt Instruction**: The `sisyphus-orchestrator` agent already includes strong instructions to "obsessively track work".
2.  **Pre-Commit Check**: Use `scripts/devops/check-pending-todos.sh` (to be created) to scan the plan file before allowing submission.
3.  **Manual Trigger**: If the agent stops, the user (or supervisor agent) should run `/invoke todo-enforcer` to verify status.

## Future Automation

To fully automate this without a TypeScript runtime plugin, we would need a wrapper around the `opencode` CLI that parses output and re-prompts if the plan isn't done.
