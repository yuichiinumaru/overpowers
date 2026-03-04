# Task Management Rules

## Task File Structure
- All tasks live in `docs/tasks/` with naming convention `nnn-type-name.md`
- Planning documents go in `docs/tasks/planning/`
- The master index is `docs/tasklist.md`

## Task Lifecycle
1. **Proposal** → `docs/tasks/planning/` (no code generated)
2. **Approved Task** → `docs/tasks/nnn-type-name.md` (with Exit Conditions)
3. **In Progress** → Mark `[/]` in tasklist.md (only by human/orchestrator)
4. **Complete** → Mark `[x]` in tasklist.md (only by human/orchestrator)

## Rules
- **Jules agents NEVER modify `docs/tasklist.md`** — multiple concurrent agents cause merge conflicts
- Jules only marks checkboxes inside its own task file (e.g. `docs/tasks/009-rebuild-mcp-infrastructure.md`)
- Task archival is done by the human operator or an isolated orchestrator script

## Naming Convention
- `nnn` — zero-padded sequential number (e.g. `009`)
- `type` — one of: `feature`, `refactor`, `fix`, `chore`, `rebuild`, `reorganize`, `audit`
- `name` — kebab-case descriptive name

## Report Convention
- Agent progress reports go in `.agents/reports/`
- Filename format: `agent-task_name-hex.md` (e.g. `foreman-009-rebuild-a3f2.md`)
- **NEVER use dates/times in filenames** — LLMs hallucinate them
