# Swarm Development Workflow

Use this workflow for complex tasks that benefit from **parallel agent coordination** using our massive agent collection.

## When to Use

- Large-scale refactoring across multiple files
- Implementing features that span backend, frontend, and tests
- Multi-language projects needing specialized agents
- Time-critical development with parallelizable work

## Agent Teams

### Team Composition

| Phase | Agents | Purpose |
|-------|--------|---------|
| **Planning** | `architect-review`, `task-decomposition-expert` | Break down into parallelizable chunks |
| **Backend** | `backend-architect`, `database-optimizer`, `api-documenter` | API and data layer |
| **Frontend** | `frontend-developer`, `ui-ux-designer`, `accessibility-specialist` | UI implementation |
| **Quality** | `code-reviewer`, `security-auditor`, `test-automator` | Validation |
| **Integration** | `deployment-engineer`, `devops-troubleshooter` | Merge and deploy |

## Workflow Steps

### 1. Task Decomposition

```
/invoke task-decomposition-expert

Input: "Full feature description"
Output: Numbered sub-tasks with dependencies marked
```

**Prompt Template:**
```
Analyze this feature and break it into parallelizable sub-tasks:
- Mark which tasks can run simultaneously
- Identify dependencies between tasks
- Estimate complexity (S/M/L) for each
```

### 2. Parallel Development Phase

Launch agents for independent tasks:

```
# Terminal 1: Backend
/invoke backend-architect
Focus: API endpoints and data models

# Terminal 2: Frontend
/invoke frontend-developer  
Focus: UI components

# Terminal 3: Tests
/invoke test-automator
Focus: Test scaffolding
```

### 3. Integration Points

Use `code-reviewer` at merge points:

```
/invoke code-reviewer

Review changes from:
- [ ] Backend branch
- [ ] Frontend branch
- [ ] Test branch

Check for:
- API contract alignment
- Type consistency
- Integration test gaps
```

### 4. Quality Gate

Run in parallel:
- `security-auditor` → Security scan
- `performance-engineer` → Performance check
- `accessibility-specialist` → A11y audit

### 5. Deployment

```
/invoke deployment-engineer

Checklist:
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Changelog entry added
- [ ] Version bumped
```

## Related Skills

- `jules-dispatch` - Send work to Jules accounts
- `jules-triage` - Review Jules branches
- `swarm-orchestration` - Coordinate multiple agents
- `pair-programming` - Collaborative coding

## Success Metrics

| Metric | Target |
|--------|--------|
| Parallel efficiency | >70% concurrent work |
| Integration issues | <5 per merge |
| Quality gate pass | First attempt |
