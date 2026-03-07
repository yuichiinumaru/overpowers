# Feature Implementation State tracking

> **Context:** Complementary to the global user session (`continuity.md`), this template tracks the state of specific isolated features, epics, or waves during multi-agent asynchronous workflows.

## State Management

Whenever working on a multi-part Task or Epic (`docs/tasks/nnnn-type-names.md`), create or update a companion `STATE` block within the task file or as a distinct `docs/tasks/nnnn-type-names-STATE.md`.

This ensures that if Agent A gets cut off, Agent B can resume the feature without starting from scratch.

### Template format

```markdown
# STATE: [Feature / Epic Name]

## Current Status
[ ] Pending
[/] In Progress (Wave 1...)
[x] Completed

## Discoveries & Decisions
*   **[Date/Time]:** Decided to use `react-hook-form` over Formik due to native Zod integrations.
*   **[Date/Time]:** Found out that the upstream API v2 is deprecated; switching to v3 endpoints for the user payload.

## Active Blockers
*   [ ] Awaiting DevOps to provision an S3 bucket for the uploads integration.
*   [ ] Failing test in `Auth.spec.ts` line 140; it seems to be a race condition during seeding.

## Next Atomic Steps for Next Agent
1.  Fix the race condition in the Auth test.
2.  Implement the login throttling middleware.
```
