# Requirements Extraction Protocol

> **Context:** Before jumping straight into task planning or execution for a feature, agents must extract implementation decisions and address "grey areas" with the user. This ensures that the eventual plan is based on concrete decisions rather than hallucinations or unvalidated assumptions, adopting the "discuss-phase" philosophy from the GSD framework.

This protocol applies to all planning and orchestration agents in the Overpowers ecosystem.

## 1. Domain Boundary Definition
Before writing an implementation plan, clearly define the domain boundary of the feature request.
- **Scope Anchor:** What exactly does this feature deliver?
- **Anti-Scope Creep:** Identify any user-suggested ideas that fall outside this domain boundary and document them in a "Deferred Ideas" or "Future Roadmap" section. **Never** allow the current implementation plan to expand beyond its original boundaries.

## 2. Identify Grey Areas
Grey areas are implementation decisions the user cares about — things that could go multiple ways and would significantly change the end result.
- **Avoid Generic Categories:** Do not ask generic questions (e.g., "How should the UI look?").
- **Find Specific Ambiguities:** Identify concrete scenarios missing from the requirements. For example:
  - If building "User authentication": Ask about session handling lengths, specific error response structures, multi-device policy, and recovery flows.
  - If building a "Database backup CLI": Ask about output formatting (JSON vs Table), flag design, progress reporting mechanisms, and error recovery behavior.

## 3. Targeted Q&A Execution
When engaging the user to resolve these grey areas using the `notify_user` tool or interactive chat:
- **Bring Code Context:** Check the codebase for existing assets first. Frame options around them (e.g., "We already have a `Card` component, should we use it here?").
- **Offer Concrete Options:** Present 2-3 clear paths forward, plus an explicit "You decide (Agent Discretion)" option. Do not leave questions purely open-ended.
- **Limit Question Volume:** Do not overwhelm the user. If there are many questions, group them in batches of 3-4 and wait for responses before continuing.

## 4. Context Finalization
The core output of this phase is a structured set of locked decisions. Before generating tasks, you must have:
- **Phase Boundary:** The strictly defined scope.
- **Implementation Decisions:** The locked-in choices addressing the grey areas.
- **Agent Discretion:** Areas where the user explicitly gave you permission to use your best judgment.
- **Deferred Ideas:** Scope creep items safely stored for later.

Only proceed to the actual task breakdown (following the `goal-backward-planning.md` protocol) once the requirements extraction is complete and the context is absolute.
