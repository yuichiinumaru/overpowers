# Agent & Skill Discovery Workflow

Navigate our **390+ agents and 149 skills** to find the right tool for any task.

## Quick Reference

### Agent Categories

| Category | Count | Example Agents |
|----------|-------|----------------|
| **Engineering** | 100+ | `backend-architect`, `frontend-developer`, `nodejs-specialist` |
| **Security** | 15+ | `security-auditor`, `api-security-audit`, `incident-responder` |
| **Research** | 20+ | `comprehensive-researcher`, `academic-researcher`, `technical-researcher` |
| **Design** | 15+ | `ui-ux-designer`, `visual-storyteller`, `whimsy-injector` |
| **Marketing** | 15+ | `growth-hacker`, `tiktok-strategist`, `reddit-community-builder` |
| **QA/Testing** | 20+ | `test-automator`, `qa-engineer`, `performance-engineer` |
| **DevOps** | 30+ | `deployment-engineer`, `devops-troubleshooter`, `ci-cd-specialist` |
| **Product** | 10+ | `product-manager`, `feedback-synthesizer`, `sprint-prioritizer` |
| **Data** | 15+ | `database-optimizer`, `elasticsearch-specialist`, `ml-specialist` |
| **Legal** | 5+ | Via legal skills (NDA, privacy policy, contracts) |

### Skill Categories

| Category | Count | Key Skills |
|----------|-------|------------|
| **Jules Swarm** | 4 | `jules-dispatch`, `jules-harvest`, `jules-triage`, `jules-integrate` |
| **DevOps** | 35+ | `github-workflow-automation`, `swarm-orchestration` |
| **Research** | 10+ | `web-research`, `arxiv-search` |
| **Legal** | 9 | Multi-language NDA review, privacy policies |
| **Productivity** | 20+ | `brainstorming`, `task-decomposition` |

## Finding the Right Agent

### By Task Type

**"I need to build/implement..."**
```
→ backend-architect (APIs)
→ frontend-developer (UI)
→ database-optimizer (data layer)
→ devops-troubleshooter (infrastructure)
```

**"I need to review/audit..."**
```
→ code-reviewer (code quality)
→ security-auditor (vulnerabilities)
→ architect-review (architecture)
→ api-security-audit (API security)
```

**"I need to research/analyze..."**
```
→ comprehensive-researcher (broad)
→ technical-researcher (docs/tutorials)
→ market-research-analyst (competition)
→ trend-researcher (industry)
```

**"I need to test..."**
```
→ test-automator (write tests)
→ qa-engineer (quality assurance)
→ performance-engineer (benchmarks)
```

**"I need to deploy..."**
```
→ deployment-engineer (releases)
→ ci-cd-specialist (pipelines)
→ devops-troubleshooter (issues)
```

### By Technology

| Tech | Primary Agent | Secondary |
|------|---------------|-----------|
| React | `react-guru` | `frontend-developer` |
| Vue | `vue3-specialist` | `frontend-developer` |
| Node.js | `nodejs-specialist` | `backend-architect` |
| Python | `python-architect` | `ml-specialist` |
| Go | `golang-specialist` | `backend-architect` |
| Rust | `rust-specialist` | `backend-architect` |
| Docker | `docker-specialist` | `devops-troubleshooter` |
| Kubernetes | `kubernetes-specialist` | `devops-troubleshooter` |
| PostgreSQL | `database-optimizer` | `backend-architect` |
| Elasticsearch | `elasticsearch-specialist` | `database-optimizer` |

## Finding the Right Skill

### List Available Skills
```bash
ls ~/.config/opencode/Overpowers/skills/
```

### Search by Keyword
```bash
grep -r "keyword" ~/.config/opencode/Overpowers/skills/*/SKILL.md
```

### Common Skill Patterns

**Automation:**
- `github-workflow-automation` - CI/CD
- `swarm-orchestration` - Multi-agent
- `pair-programming` - Collaborative

**Research:**
- `web-research` - Web scraping
- `arxiv-search` - Academic papers
- `langsmith-fetch` - LLM debugging

**Legal:**
- `nda-review-*` - NDA analysis
- `privacy-policy-*` - Privacy review
- `contract-clause-extraction` - Contracts

## Agent Chaining Patterns

### Research → Implementation
```
comprehensive-researcher → task-decomposition-expert → backend-architect → code-reviewer
```

### Idea → Launch
```
brainstorming → rapid-prototyper → test-automator → deployment-engineer → growth-hacker
```

### Bug → Fix → Deploy
```
qa-engineer → devops-troubleshooter → code-reviewer → deployment-engineer
```

### Security Audit
```
security-auditor → api-security-audit → incident-responder → code-reviewer
```

## Best Practices

1. **Start with task decomposition** - Always break down complex work
2. **Use specialized agents** - Don't use generic when specific exists
3. **Chain agents logically** - Follow natural flow: research → plan → build → test → deploy
4. **Leverage skills for repetitive tasks** - Skills are optimized for specific operations
5. **Review before deploying** - Always include code-reviewer or security-auditor

## Quick Commands

```bash
# List all agents
ls ~/.config/opencode/Overpowers/agents/

# List all skills
ls ~/.config/opencode/Overpowers/skills/

# List all workflows
ls ~/.config/opencode/Overpowers/workflows/

# Search agents by name
ls ~/.config/opencode/Overpowers/agents/ | grep "keyword"

# Count totals
echo "Agents: $(ls ~/.config/opencode/Overpowers/agents/ | wc -l)"
echo "Skills: $(ls ~/.config/opencode/Overpowers/skills/ | wc -l)"
echo "Workflows: $(ls ~/.config/opencode/Overpowers/workflows/ | wc -l)"
```
