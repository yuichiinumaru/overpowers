# Assumption Surfacing Protocol

> **Context:** Before beginning detailed planning or execution for a feature, agents often make numerous implicit assumptions based on standard practices or previous context. If these assumptions are wrong, they result in wasted execution cycles and extensive refactoring. The Assumption Surfacing Protocol forces agents to declare their mental model explicitly *before* generating actionable code plans.

This protocol applies during the initialization and planning phases.

## Core Directives

1. **Pause and Formulate:** Before drafting an implementation plan or jumping to code, analyze the goal and extract explicitly what you are assuming. The output shouldn't be the plan itself, but a "pre-plan" representation of your intent.
2. **The 5 Assumption Axes:** Your surfaced assumptions must cover the following five areas clearly:
   - **Technical Approach:** What architecture/patterns are you assuming will be used? (e.g., "I assume we will use the existing `Card` component and `useSWR` for fetching").
   - **Implementation Order:** What sequencing are you imagining? (e.g., "I assume we will build the DB schema first, then the API, then the frontend").
   - **Scope Boundaries:** What are you assuming is *out of scope*? (e.g., "I assume real-time WebSocket updates are not needed for this initial phase").
   - **Risks:** What are the danger zones? (e.g., "I assume caching might be tricky here, risking stale data").
   - **Dependencies:** What must be true for this to work? (e.g., "I assume the backend Auth endpoint is already stable").
3. **User Validation:** Present these assumptions to the user in a readable list and explicitly ask: *"What do you think? Are these assumptions correct or should we course-correct any of them?"*
4. **Course Correction:** You may only proceed to true planning (or execution) once the user has explicitly verified, challenged, or corrected your surfaced assumptions.
