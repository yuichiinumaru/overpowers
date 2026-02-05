---
name: refactor
description: "Intelligent refactoring command. Uses 6-phase workflow: Intent Analysis -> Code Mapping -> Test Assessment -> Planning -> Execution -> Final Verification. Use when refactoring code to ensure safety and correctness."
---

# Intelligent Refactor Command

This command executes a disciplined refactoring workflow.

## Usage

\`\`\`bash
/invoke refactor "Extract authentication logic to a service"
/invoke refactor "Rename User class to Customer" --scope=project
\`\`\`

## 6-Phase Workflow

### Phase 1: Intent Analysis
- **Goal**: Understand WHAT and WHY.
- **Output**: Core refactoring goal defined.

### Phase 2: Code Mapping (Impact Analysis)
- **Tools**: \`explore\`, \`lsp\`, \`ast-grep\`
- **Output**: Dependency graph, impact zones (files affected).

### Phase 3: Test Assessment
- **Goal**: Ensure safety net exists.
- **Action**: Check coverage. If low, propose adding tests FIRST.

### Phase 4: Plan Generation
- **Action**: Create detailed step-by-step plan.
- **Output**: Granular TODOs.

### Phase 5: Execution
- **Strategy**: Deterministic steps.
- **Verification**: Run tests after EVERY change.
- **Commit**: Atomic commits at checkpoints.

### Phase 6: Final Verification
- **Action**: Full regression suite run.
- **Output**: Final summary.

## Critical Rules
- **Never** proceed with failing tests.
- **Never** use \`@ts-ignore\` or \`as any\` to suppress errors.
- **Always** verify after every change.
