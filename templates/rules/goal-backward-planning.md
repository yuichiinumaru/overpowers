# Goal-Backward Planning Methodology

> **Context:** Standard forward-planning asks "What should we build?" and often results in agents wandering aimlessly. Goal-Backward Planning asks "What must be TRUE for the goal to be achieved?", resulting in highly specific, testable constraints. Use this protocol when acting as a Planner Agent.

## The 5-Step Process

Whenever you are tasked with decomposing a feature into actionable tasks, follow these steps before generating the final `nnnn-type-name.md` files.

### Step 1: State the Goal (Outcome-Shaped)
Take the macro goal and define the desired outcome from the user's perspective.
*   *Bad:* Build an authentication system.
*   *Good:* A user can securely log in to the application and access protected routes.

### Step 2: Derive Observable Truths
Ask: "What must be TRUE for this goal to be achieved?" List 3-5 truths.
*   *Truth 1:* A user submitting valid credentials receives a valid JWT token.
*   *Truth 2:* A user submitting invalid credentials receives an HTTP 401 error.
*   *Truth 3:* Protected routes reject requests without a valid JWT token.

### Step 3: Derive Required Artifacts
For each truth, ask: "What file or system object must EXIST for this to be true?"
*   *Artifact 1:* A `User` model in `schema.prisma`.
*   *Artifact 2:* A login endpoint at `src/app/api/auth/login.ts`.
*   *Artifact 3:* An authentication middleware component protecting routes.

### Step 4: Derive Required Wiring
For each artifact, ask: "How must this be CONNECTED to function?"
*   *Wiring 1:* The login endpoint must query the Prisma client to verify password hashes.
*   *Wiring 2:* The frontend form must POST to the login endpoint on submit.

### Step 5: Identify Key Links (Failure Points)
Identify where the system is most likely to break during integration.
*   *Key Link:* The password hashing algorithm on registration must exactly match the verification hashing on the login phase.

## Formulating Tasks
Once the Goal-Backward process is complete, translate the Artifacts and Wiring into strict `<task>` blocks containing specific `<files_modified>` parameters and `<verify>` success criteria. 
*(See `wave-parallelism.md` and the `000-gsd-task-template.md` for output formatting).*
