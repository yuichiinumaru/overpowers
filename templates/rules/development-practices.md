# Development Practices

## Specification-First Development
When starting a new feature:
1. Create `FEATURE_PLAN.md` — Break the implementation into small, testable steps with deliverables and test plans
2. Create `TECHNICAL_DESIGN.md` — Dependencies, data flow, API signatures, testing approach
3. Create `TASKS.md` — Step-by-step implementation plan as a todo list

Place these in the task's planning directory or inside `.feature/{feature-name}/`.
Only begin implementation after the specification is reviewed and agreed upon.

## Test-Driven Development
- Always write a failing test before writing production code
- Focus on one small behavior at a time
- Refactor only after tests are passing and behavior is correct
- All new features, bug fixes, and refactors must have tests
- Tests should be clear, isolated, and repeatable
