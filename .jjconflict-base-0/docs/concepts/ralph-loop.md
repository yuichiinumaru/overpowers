# Ralph Loop Concept

The "Ralph Loop" is an autonomous recursive task execution pattern extracted from `oh-my-opencode`.

## Logic

1.  **Start Loop**: The user initiates a loop with a prompt and a maximum iteration count.
2.  **Execution**: The agent executes the prompt.
3.  **Completion Check**:
    *   The system checks for a completion marker (e.g., `<RALPH_LOOP_COMPLETE>`) in the output.
    *   If found, the loop terminates.
4.  **Continuation**:
    *   If not complete and max iterations not reached, the system re-prompts the agent with context:
        > "Iteration X/Y. Continue working on [Task]. Output <RALPH_LOOP_COMPLETE> when done."

## Implementation Note

In `oh-my-opencode`, this is implemented as a runtime hook (`src/hooks/ralph-loop`). Since overpowers is a configuration/script repository, this logic must be implemented via:
1.  **Agent Discipline**: Instructing the agent (via Prompt) to self-iterate.
2.  **CLI Wrappers**: A script that wraps `opencode` CLI and handles the loop logic (parsing stdout for the completion marker).

*See `scripts/devops/ralph-loop.sh` (template) for a starting point if implementing a CLI wrapper.*
