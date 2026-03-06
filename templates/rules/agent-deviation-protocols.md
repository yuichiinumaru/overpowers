# Agent Deviation Protocols

> **Context:** When operating autonomously, agents will inevitably encounter situations that aren't defined in their original task logic. To avoid analysis paralysis or unintended destructive changes, all agents in the Overpowers ecosystem must follow these 4 Deviation Rules.

## The 4 Rules of Deviation

Whenever you find an issue not originally stated in your `<objective>`, use this decision tree:

### RULE 1: Auto-fix Bugs
*   **Trigger:** The code does not work as intended (broken behavior, syntax errors, incorrect output).
*   **Examples:** Wrong queries, logic errors, type errors, null pointer exceptions, unhandled race conditions.
*   **Action:** Fix it inline silently. Run the local tests to ensure the fix is valid. Continue working.

### RULE 2: Auto-add Missing Critical Functionality
*   **Trigger:** The code is missing essential features for fundamental, safe operation.
*   **Examples:** Missing error handling, missing input validation, missing environment variables, lack of authorization on obvious protected routes.
*   **Action:** Add the minimal required safety guard. Do not over-engineer. Continue working.

### RULE 3: Auto-fix Blocking Issues
*   **Trigger:** A secondary dependency or configuration is preventing you from completing the *current* task.
*   **Examples:** Missing NPM/Pip dependency, broken imports, missing referenced files.
*   **Action:** Resolve the blocker (e.g., `npm install X`, rewrite the import statement). Ensure the build works, then continue.

### RULE 4: Ask About Architectural Changes
*   **Trigger:** The fix requires significant structural modification to the project.
*   **Examples:** Creating a new database table, making major schema changes, migrating to a different framework, establishing a new service layer, or performing breaking API changes.
*   **Action:** STOP EXECUTING. Generate a **Checkpoint** (see `checkpoint-protocol.md`). Document the issue found, propose the architectural shift, list the tradeoffs, and await human verification. **DO NOT GUESS.**

## Fix Attempt Limits
*   Track your auto-fix attempts per issue. 
*   If you fail to resolve an issue after **3 consecutive attempts**, DO NOT restart the build hoping for a different result.
*   **Action:** STOP. Document the remaining issues as a blocker using the Checkpoint Protocol and wait for human guidance.

## Scope Boundaries
*   Only fix issues that are DIRECTLY related to the files you are modifying or the tests you are running.
*   Pre-existing warnings, linting errors, or failures in unrelated files are out of scope. Do not touch them.
