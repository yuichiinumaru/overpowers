# Master Integration Plan - Overpowers Repository Recycling

> Generated: 2026-01-18
> Scope: Repositories 00001-00025 (First 25 analyzed)
> Status: READY FOR IMPLEMENTATION

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Repositories Analyzed | 25 |
| TIER 1 (Game Changers) | 9 |
| TIER 2 (High Value) | 10 |
| TIER 3 (Targeted/Limited) | 4 |
| DISCARD (No Value) | 2 |
| **New Skills to Add** | ~80+ |
| **New Agents to Add** | 6 |
| **Skills to Enhance** | 12 |
| **New Commands** | 20-30 |
| **New Hooks** | 10+ |

### Current Overpowers Inventory
- Agents: 389
- Skills: 148
- Commands: 227
- Workflows: 16
- Hooks: 0
- Services: 3

### Projected After Integration
- Agents: 395+ (+6)
- Skills: 230+ (+80)
- Commands: 257+ (+30)
- Workflows: 20+ (+4)
- Hooks: 10+ (+10)

---

## Phase 0: Quick Wins (Day 1-2)

### 0.1 Complete Skills (Copy As-Is)

These require zero modification - direct copy to `Overpowers/skills/`:

| Skill | Source | Gap Filled |
|-------|--------|------------|
| `cloudflare` | dmmulroy-cloudflare-skill | 100% Cloudflare ecosystem (60 products, 265 files) |
| `x-search` | ChihiroNishioka | Twitter search without API (DuckDuckGo site-scoping) |
| `ios-simulator-skill` | conorluddy | Already exists, verify parity |

### 0.2 New Agents (6 Factory Guides)

Copy to `Overpowers/agents/`:

| Agent | Source | Purpose |
|-------|--------|---------|
| `factory-guide` | alirezarezvani | Orchestrator for asset generation |
| `skills-guide` | alirezarezvani | Interactive skills builder |
| `prompts-guide` | alirezarezvani | Prompts generator specialist |
| `agents-guide` | alirezarezvani | Agents creator specialist |
| `hooks-guide` | alirezarezvani | Hooks builder specialist |
| `agents-md-guardian` | alirezarezvani | Background AGENTS.md maintenance |

### 0.3 High-Value Commands

Copy to `Overpowers/commands/`:

| Command | Source | Purpose |
|---------|--------|---------|
| `/commit` | davepoon-buildwithclaude | Git workflow automation |
| `/interview` | davepoon-buildwithclaude | Interactive requirement gathering |
| `/tdd` | davepoon-buildwithclaude | Test-driven development workflow |
| `/context-prime` | davepoon-buildwithclaude | Project context loading |
| `/build` | alirezarezvani | Build validation |
| `/validate-output` | alirezarezvani | Output validation |

---

## Phase 1: Security Domain (Days 3-5)

### 1.1 Security Skills Suite

New directory: `Overpowers/skills/security/`

| Skill | Source | Coverage |
|-------|--------|----------|
| `top-web-vulnerabilities` | antigravity-awesome | OWASP Top 100 reference |
| `sql-injection-testing` | antigravity-awesome | SQLi methodology |
| `xss-html-injection` | antigravity-awesome | XSS testing methodology |
| `linux-privilege-escalation` | antigravity-awesome | Linux privesc testing |
| `broken-authentication` | antigravity-awesome | Session testing |
| `idor-testing` | antigravity-awesome | IDOR testing methodology |
| `file-path-traversal` | antigravity-awesome | Directory traversal testing |
| `api-fuzzing-bug-bounty` | antigravity-awesome | API security testing |
| `ethical-hacking-methodology` | antigravity-awesome | Pentesting lifecycle |
| `pentest-checklist` | antigravity-awesome | Security assessment checklist |
| `pentest-commands` | antigravity-awesome | Security tool reference |
| `red-team-tools` | antigravity-awesome | Bug bounty methodology |

### 1.2 Advanced Security

| Skill | Source | Coverage |
|-------|--------|----------|
| `cloud-penetration-testing` | antigravity-awesome | Multi-cloud security |
| `aws-penetration-testing` | antigravity-awesome | AWS-specific security |
| `active-directory-attacks` | antigravity-awesome | AD attack testing |
| `metasploit-framework` | antigravity-awesome | MSF usage methodology |
| `burp-suite-testing` | antigravity-awesome | Burp Suite workflow |
| `privilege-escalation-methods` | antigravity-awesome | Cross-platform privesc |
| `security-researcher` | cp09x | Platform-specific security |

### 1.3 Security Infrastructure

| Asset | Source | Purpose |
|-------|--------|---------|
| `security.md` | BreezeAllen-aidevops | Security standards doc |
| `secretlint-helper.sh` | BreezeAllen-aidevops | Secret detection |
| `quality-check.sh` | BreezeAllen-aidevops | Multi-platform validation |
| `security-scanning` (5 skills) | as4584 | STRIDE/threat modeling |

---

## Phase 2: Infrastructure Domain (Days 6-8)

### 2.1 Kubernetes & Cloud

New directory: `Overpowers/skills/infrastructure/`

| Skill | Source | Coverage |
|-------|--------|----------|
| `kubernetes-operations` (4 skills) | as4584 | K8s management with scaffolding |
| `cloud-infrastructure` (8 skills) | as4584 | Multi-cloud patterns |
| `cloud-architect` | cp09x | Multi-cloud design |

### 2.2 CI/CD & DevOps

| Skill | Source | Coverage |
|-------|--------|----------|
| `cicd-automation` (4 skills) | as4584 | CI/CD automation patterns |
| `observability-monitoring` (4 skills) | as4584 | Distributed tracing/SLO |
| `incident-response` (3 skills) | as4584 | Runbook/postmortem |
| `deployment-strategies` | as4584 | Blue/green/canary patterns |

### 2.3 DevOps Infrastructure

| Asset | Source | Purpose |
|-------|--------|---------|
| `feature-development.md` | BreezeAllen-aidevops | Feature workflow |
| `release-process.md` | BreezeAllen-aidevops | Release workflow |
| `version-manager.sh` | BreezeAllen-aidevops | Version management |

---

## Phase 3: Design & Frontend (Days 9-11)

### 3.1 UI/UX Pro Max

Priority: HIGH - This is a game-changer

| Skill | Source | Content |
|-------|--------|---------|
| `ui-ux-pro-max` | antigravity-awesome | 50 styles, 97 palettes, complete design system |

### 3.2 Frontend Enhancements

| Skill | Action | Enhancement |
|-------|--------|-------------|
| `react-best-practices` | MERGE | Add 45 Vercel rules (current has 23 lines) |
| `frontend-design` | ENHANCE | Add visual collaboration protocol |
| `frontend-ui-ux` | ADOPT | "Show before code" methodology |

### 3.3 Mobile Development

| Skill | Source | Coverage |
|-------|--------|----------|
| `mobile-developer` | cp09x | Mobile-first patterns |
| `frontend-mobile-development` (4 skills) | as4584 | Next.js/React Native patterns |

---

## Phase 4: Backend & AI/ML (Days 12-14)

### 4.1 Backend Enhancements

| Skill | Action | Enhancement |
|-------|--------|-------------|
| `backend-development` | MERGE | Add CQRS, event sourcing, saga patterns (9 sub-skills) |
| `python-development` | MERGE | Add 5 sub-skills (async, testing, packaging) |
| `javascript-typescript` | MERGE | Add 4 sub-skills (advanced types, testing) |

### 4.2 LLM/AI Development

| Skill | Action | Enhancement |
|-------|--------|-------------|
| `llm-application-dev` | MERGE | Add 7 sub-skills (RAG, embeddings, evaluation) |
| `machine-learning-ops` | ADOPT | ML pipeline methodology |

### 4.3 Specialized Domains

New directories as needed:

| Skill | Source | Domain |
|-------|--------|--------|
| `blockchain-web3` (4 skills) | as4584 | DeFi/NFT/Solidity |
| `payment-processing` (4 skills) | as4584 | Stripe/PayPal/PCI |
| `data-engineering` (4 skills) | as4584 | Airflow/dbt/Spark |
| `game-development` (2 skills) | as4584 | Unity/Godot |
| `quantitative-trading` (2 skills) | as4584 | Backtesting/risk |
| `reverse-engineering` (4 skills) | as4584 | Binary analysis |

---

## Phase 5: Meta & Coordination (Days 15-17)

### 5.1 Multi-Agent Coordination

| Asset | Source | Purpose |
|-------|--------|---------|
| `multi-agent-file-coordination` | Dicklesworthstone | Lock-based file claiming (20+ agents) |
| `studio-coach` | contains-studio | Meta-agent that coaches other agents |
| `workflow-optimizer` | contains-studio | Human-AI collaboration science |
| `whimsy-injector` | contains-studio | Proactive UX delight |

### 5.2 Factory Skills

| Skill | Source | Purpose |
|-------|--------|---------|
| `agent-factory` | alirezarezvani | Agent generation methodology |
| `prompt-factory` | alirezarezvani | 69 role presets |
| `hook-factory-v2` | alirezarezvani | Hook creation with validation |
| `slash-command-factory` | alirezarezvani | Command generation |
| `claude-md-enhancer` | alirezarezvani | CLAUDE.md quality scoring |

### 5.3 Hooks Infrastructure

New directory: `Overpowers/hooks/`

| Hook | Source | Purpose |
|------|--------|---------|
| `auto-git-add` | davepoon | Automatic staging |
| `file-protection` | davepoon | Prevent accidental edits |
| `slack-notifications` | davepoon | Slack integration |
| `auto-sync-plan-to-github` | alirezarezvani | GitHub sync |
| + 6 more hooks | davepoon | Various automation |

---

## Phase 6: Quality & Methodology (Days 18-20)

### 6.1 Progressive Disclosure Framework

**Strategic Priority** - 50-80% token reduction

| Pattern | Source | Implementation |
|---------|--------|----------------|
| 3-level loading | DougTrajano-pydantic-ai | Level 1: Metadata, Level 2: Instructions, Level 3: Resources |
| Anthropic-compatible validation | DougTrajano-pydantic-ai | Standardize frontmatter |
| Programmatic skill creation | DougTrajano-pydantic-ai | Script-based generation |

### 6.2 Evaluation-Driven Development

| Pattern | Source | Implementation |
|---------|--------|----------------|
| JSON evaluation schema | czlonkowski-n8n | Query + expected_behavior + expected_content |
| 100% pass requirement | czlonkowski-n8n | Skill validation gate |
| Skill size limits | czlonkowski-n8n | <500 lines guideline |

### 6.3 Enhanced Existing Skills

| Skill | Enhancement | Source |
|-------|-------------|--------|
| `test-driven-development` | Stronger enforcement | alexjiaguo |
| `systematic-debugging` | Iron law, 4-phase process | alexjiaguo |
| `hooks-automation` | Better validation | alirezarezvani |

---

## Phase 7: Documentation & Workflows (Days 21-22)

### 7.1 Document Processing Suite

| Skill | Source | Enhancement |
|-------|--------|-------------|
| `docx` | DonggangChen + ComposioHQ | OOXML validation |
| `pptx` | DonggangChen | Template creation |
| `pdf` | ComposioHQ | 8 form scripts |

### 7.2 GitHub Workflows

Copy to `Overpowers/workflows/`:

| Workflow | Source | Purpose |
|----------|--------|---------|
| `smart-sync.yml` | alirezarezvani | Smart sync automation |
| `plan-to-tasks.yml` | alirezarezvani | Plan conversion |
| `task-to-subtasks.yml` | alirezarezvani | Task decomposition |
| `plan-auto-close.yml` | alirezarezvani | Auto-close completed plans |

### 7.3 Templates

| Template | Source | Purpose |
|----------|--------|---------|
| `SPECIFICATION.md` | conorluddy | 817-line spec template |
| `PR_TEMPLATE.md` | antigravity-awesome | PR template |
| `bug_report.md` | antigravity-awesome | Issue template |
| `feature_request.md` | antigravity-awesome | Feature request template |

---

## DISCARD List (No Action)

| Repository | Reason |
|------------|--------|
| 00001 - 0xfurai-claude-code-subagents | 100% duplicates, zero unique value |
| 00014 - codeF1x-antigravity-skills | Completely redundant with existing |

---

## Implementation Checklist

### Pre-Flight
- [ ] Backup current Overpowers state
- [ ] Create integration branch
- [ ] Verify archive/ contains all 25 source folders

### Phase 0 (Quick Wins)
- [ ] Copy cloudflare skill
- [ ] Copy x_search skill
- [ ] Copy 6 factory guide agents
- [ ] Copy high-value commands

### Phase 1 (Security)
- [ ] Create `skills/security/` directory
- [ ] Copy 17+ security skills
- [ ] Copy security infrastructure scripts

### Phase 2 (Infrastructure)
- [ ] Create `skills/infrastructure/` directory
- [ ] Copy K8s/cloud skills
- [ ] Copy CI/CD/DevOps skills

### Phase 3 (Design/Frontend)
- [ ] Copy ui-ux-pro-max
- [ ] Merge react-best-practices
- [ ] Copy mobile development skills

### Phase 4 (Backend/AI)
- [ ] Merge backend_development enhancements
- [ ] Merge llm_application_dev enhancements
- [ ] Copy specialized domain skills

### Phase 5 (Meta/Coordination)
- [ ] Copy multi-agent coordination
- [ ] Copy factory skills
- [ ] Create hooks/ directory and copy hooks

### Phase 6 (Quality)
- [ ] Implement progressive disclosure
- [ ] Create evaluations/ structure
- [ ] Merge enhanced existing skills

### Phase 7 (Docs/Workflows)
- [ ] Enhance document processing
- [ ] Copy GitHub workflows
- [ ] Copy templates

### Post-Flight
- [ ] Update inventory.md
- [ ] Run validation scripts
- [ ] Move docs/00001-00025* to archive/docs/
- [ ] Commit and tag release

---

## Risk Mitigation

### Naming Conflicts
- Check for existing files before copying
- Use `_v2` suffix for enhanced versions during transition
- Merge rather than replace when possible

### Quality Assurance
- Each skill should be tested after copy
- Run any validation scripts from source repos
- Verify frontmatter compatibility

### Instruction Budget (Note from User)
- Keep 500-line soft limit for now
- Do NOT prune based on old instruction budget research
- Models are improving; await proper testing setup

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Skills added | 80+ |
| New domains covered | 6+ (security, infra, design, blockchain, etc.) |
| Token reduction | 50-80% via progressive disclosure |
| Test coverage | 100% pass on validation |
| Zero regressions | No broken existing functionality |

---

## Next Steps After This Plan

1. **Begin Phase 0** - Quick wins first
2. **Check batch 26-75** - Review incoming analysis from parallel agent
3. **Continue with Phases 1-7** - Systematic integration
4. **Final validation** - Run all tests, update inventory
5. **Archive and document** - Move completed work to archive/

---

*Plan Version: 1.0*
*Last Updated: 2026-01-18*
