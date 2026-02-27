# Skill vs Agent Classification

> Classification of ADOPT/ADAPT recommendations from antigravity repository comparisons.
> Generated: 2026-01-18

## Summary

| Metric | Count |
|--------|-------|
| Items reviewed | 127 |
| Classified as AGENT | 6 |
| Classified as SKILL | 103 |
| Other (scripts/templates/commands/workflows) | 18 |
| Already exists in Overpowers | 31 |

---

## Classification Criteria

- **AGENT**: Defines a persona/role (e.g., "security_auditor", "code_reviewer", "typescript_pro")
- **SKILL**: Defines a methodology/workflow (e.g., "test_driven_development", "code_refactoring", "debugging")

---

## Classification Results

### Should be AGENTS (persona/role): 6 items

| Item | Source Repo | Reason | Exists in Overpowers? |
|------|-------------|--------|----------------------|
| `factory-guide` | alirezarezvani-claude-code-skill-factory | Orchestrator persona that delegates to specialist agents | No |
| `skills-guide` | alirezarezvani-claude-code-skill-factory | Skills builder specialist persona with interactive Q&A | No |
| `prompts-guide` | alirezarezvani-claude-code-skill-factory | Prompts generator specialist persona | No |
| `agents-guide` | alirezarezvani-claude-code-skill-factory | Agents creator specialist persona | No |
| `hooks-guide` | alirezarezvani-claude-code-skill-factory | Hooks builder specialist persona | No |
| `claude-md-guardian` | alirezarezvani-claude-code-skill-factory | Background maintenance agent persona for CLAUDE.md files | No |

---

### Should remain SKILLS (methodology/workflow): 103 items

#### From 00003-alexjiaguo-AntigravitySkills (26 items)

| Item | Reason | Exists in Overpowers? |
|------|--------|----------------------|
| `docx-processing-v1` | Document creation/editing methodology | Yes (`docx` skill) |
| `docx-js-v1` | API reference for document creation workflow | No (as reference) |
| `docx-ooxml-v1` | OOXML editing methodology reference | No (as reference) |
| `docx-redlining-v1` | Tracked changes workflow methodology | No |
| `doc-coauthoring-v1` | Collaborative editing workflow | Yes (`doc-coauthoring` skill) |
| `pptx-processing-v1` | Presentation processing methodology | Yes (`pptx` skill) |
| `pptx-ooxml-v1` | OOXML structure reference | No (as reference) |
| `pptx-html-conversion-v1` | HTML-to-PPTX conversion workflow | No |
| `pptx-template-creation-v1` | Template-based creation workflow | No |
| `pdf-processing-v1` | PDF processing methodology | Yes (`pdf` skill) |
| `pdf-forms-v1` | PDF forms workflow methodology | No |
| `pdf-reference-v1` | PDF specification reference | No (as reference) |
| `deep-research-v1` | Deep research protocol methodology | No |
| `brainstorming-v1` | Interactive design refinement methodology | Yes (`brainstorming` skill) |
| `systematic-debugging-v1` | Root cause debugging methodology | Yes (`systematic-debugging` skill) |
| `tdd-v1` | Test-driven development methodology | Yes (`test-driven-development` skill) |
| `verification-v1` | Pre-completion verification methodology | Yes (`verification-before-completion` skill) |
| `receiving-code-review` | Code review reception workflow | Yes (`receiving-code-review` skill) |
| `requesting-code-review` | Code review request workflow | Yes (`requesting-code-review` skill) |
| `finishing-a-development-branch` | Branch completion workflow | Yes (`finishing-a-development-branch` skill) |
| `using-git-worktrees` | Git worktree usage methodology | Yes (`using-git-worktrees` skill) |
| `dispatching-parallel-agents` | Parallel agent orchestration methodology | Yes (`dispatching-parallel-agents` skill) |
| `executing-plans` | Plan execution methodology | Yes (`executing-plans` skill) |
| `using-superpowers` | Meta-skill for skill discovery | Yes (`using-overpowers` skill) |
| `writing-skills` | Skill creation methodology | Yes (`writing-skills` skill) |
| `writing-plans-v1` | Plan writing methodology | Yes (`writing-plans` skill) |

#### From 00005-alirezarezvani-claude-code-skill-factory (10 items)

| Item | Reason | Exists in Overpowers? |
|------|--------|----------------------|
| `agent-factory` | Agent generation methodology (creates agents, isn't one) | No |
| `prompt-factory` | Prompt generation methodology with 69 presets | No (we have `prompt-optimizer`) |
| `hook-factory-v2` | Hook creation methodology with validation | No (we have basic `hooks-automation`) |
| `slash-command-factory` | Command generation methodology | No |
| `claude-md-enhancer` | CLAUDE.md/AGENTS.md quality scoring methodology | No |
| `codex-cli-bridge` | Cross-tool interoperability methodology | No |
| `AGENTS_FACTORY_PROMPT` | Template/reference for agent generation | No |
| `SKILLS_FACTORY_PROMPT` | Template/reference for skill generation | No |
| `MASTER_SLASH_COMMANDS_PROMPT` | Template/reference for command patterns | No |
| `HOOKS_FACTORY_PROMPT` | Template/reference for hook creation | No |

#### From 00007-antigravity-awesome-skills (40 items)

| Item | Reason | Exists in Overpowers? |
|------|--------|----------------------|
| `ui-ux-pro-max` | Design system methodology (50 styles, 97 palettes, etc.) | No |
| `workflow-automation` | N8n-inspired automation patterns methodology | No |
| `top-web-vulnerabilities` | OWASP Top 100 security reference methodology | No |
| `sql-injection-testing` | SQLi testing methodology | No |
| `linux-privilege-escalation` | Linux privesc testing methodology | No |
| `metasploit-framework` | MSF usage methodology | No |
| `burp-suite-testing` | Burp Suite workflow methodology | No |
| `cloud-penetration-testing` | Multi-cloud security testing methodology | No |
| `active-directory-attacks` | AD attack testing methodology | No |
| `api-fuzzing-bug-bounty` | API security testing methodology | No |
| `aws-penetration-testing` | AWS security testing methodology | No |
| `broken-authentication` | Session testing methodology | No |
| `ethical-hacking-methodology` | Pentesting lifecycle methodology | No |
| `file-path-traversal` | Directory traversal testing methodology | No |
| `html-injection-testing` | HTML injection testing methodology | No |
| `idor-testing` | IDOR testing methodology | No |
| `linux-shell-scripting` | Production shell script patterns | No |
| `network-101` | Network configuration reference | No |
| `pentest-checklist` | Security assessment methodology | No |
| `pentest-commands` | Security tool reference | No |
| `privilege-escalation-methods` | Cross-platform privesc methodology | No |
| `red-team-tools` | Bug bounty methodology | No |
| `xss-html-injection` | XSS testing methodology | No |
| `agent-manager-skill` | Tmux-based multi-agent management methodology | No |
| `app-store-optimization` | ASO methodology | No |
| `autonomous-agent-patterns` | Agent design patterns methodology | No |
| `blockrun` | LLM micropayments methodology | No |
| `bun-development` | Bun runtime development methodology | No |
| `claude-code-guide` | Claude Code mastery methodology | No |
| `notebooklm` | Google NotebookLM integration methodology | No |
| `planning-with-files` | File-based planning methodology | No |
| `javascript-mastery` | JS educational reference | No |
| `react-best-practices` | React development methodology (45 Vercel rules) | Yes (but theirs is better) |
| `mcp-builder` | MCP server creation methodology | Yes (`mcp-builder` skill) |
| `frontend-design` | Frontend design methodology | Yes (`frontend-design` skill) |
| `web-design-guidelines` | Web design methodology | Yes (`web-design-guidelines` skill) |
| `playwright-skill` | Browser automation methodology | Yes (`playwright-skill` skill) |
| `generate_index.py` | Skill indexing script (NOT skill) | N/A |
| `validate_skills.py` | Skill validation script (NOT skill) | N/A |

#### From 00009-as4584-antigravity-skills (27 items - Major Categories)

| Item | Reason | Exists in Overpowers? |
|------|--------|----------------------|
| `kubernetes-operations` (4 skills) | K8s management methodology with scaffolding | No |
| `cloud-infrastructure` (8 skills) | Multi-cloud patterns methodology | No |
| `cicd-automation` (4 skills) | CI/CD automation methodology | No |
| `security-scanning` (5 skills) | STRIDE/threat modeling methodology | No |
| `accessibility-compliance` (2 skills) | WCAG audit methodology | No |
| `incident-response` (3 skills) | Runbook/postmortem methodology | No |
| `observability-monitoring` (4 skills) | Distributed tracing/SLO methodology | No |
| `llm-application-dev` (8 skills) | RAG/embedding development methodology | Yes (basic version) |
| `machine-learning-ops` (1 skill) | ML pipeline methodology | No |
| `backend-development` (9 skills) | CQRS/event sourcing/saga patterns | Yes (basic version) |
| `frontend-mobile-development` (4 skills) | Next.js/React Native patterns | Yes (basic version) |
| `python-development` (5 skills) | Async/testing/packaging patterns | Yes (basic version) |
| `javascript-typescript` (4 skills) | Advanced types/testing patterns | Yes (basic version) |
| `systems-programming` (3 skills) | Rust/Go patterns methodology | No |
| `shell-scripting` (3 skills) | Bash defensive patterns methodology | No |
| `data-engineering` (4 skills) | Airflow/dbt/Spark methodology | No |
| `conductor` (3 skills) | Context-driven development methodology | No |
| `blockchain-web3` (4 skills) | DeFi/NFT/Solidity patterns | No |
| `payment-processing` (4 skills) | Stripe/PayPal/PCI methodology | No |
| `framework-migration` (4 skills) | Angular/React migration methodology | No |
| `documentation-generation` (3 skills) | ADR/changelog/OpenAPI methodology | No |
| `comprehensive-review` | Multi-perspective review methodology | No |
| `game-development` (2 skills) | Unity/Godot patterns | No |
| `quantitative-trading` (2 skills) | Backtesting/risk methodology | No |
| `reverse-engineering` (4 skills) | Binary analysis methodology | No |
| `startup-business-analyst` (5 skills) | Market/competitive analysis methodology | No |
| `deployment-strategies` | Blue/green/canary patterns | No |

---

### Other Items (scripts/templates/commands/workflows): 18 items

| Item | Type | Source Repo |
|------|------|-------------|
| `smart-sync.yml` | GitHub Workflow | alirezarezvani |
| `plan-to-tasks.yml` | GitHub Workflow | alirezarezvani |
| `task-to-subtasks.yml` | GitHub Workflow | alirezarezvani |
| `plan-auto-close.yml` | GitHub Workflow | alirezarezvani |
| `plan-validator.yml` | GitHub Workflow | alirezarezvani |
| `/build` | Slash Command | alirezarezvani |
| `/validate-output` | Slash Command | alirezarezvani |
| `/install-skill` | Slash Command | alirezarezvani |
| `/install-hook` | Slash Command | alirezarezvani |
| `/cm, /cp, /pr, /rv, /sc` | Git Commands | alirezarezvani |
| `/ci-guard` | CI/CD Command | alirezarezvani |
| `auto-sync-plan-to-github` | Hook | alirezarezvani |
| `generate_index.py` | Python Script | antigravity-awesome |
| `validate_skills.py` | Python Script | antigravity-awesome |
| `skills_manager.py` | Python Script | antigravity-awesome |
| `PR_TEMPLATE.md` | GitHub Template | antigravity-awesome |
| `bug_report.md` | Issue Template | antigravity-awesome |
| `feature_request.md` | Issue Template | antigravity-awesome |

---

### Duplicates (already covered in Overpowers): 31 items

| Item | Already covered by |
|------|-------------------|
| `docx-processing-v1` | `docx` skill |
| `doc-coauthoring-v1` | `doc-coauthoring` skill |
| `pptx-processing-v1` | `pptx` skill |
| `pdf-processing-v1` | `pdf` skill |
| `brainstorming-v1` | `brainstorming` skill |
| `systematic-debugging-v1` | `systematic-debugging` skill |
| `tdd-v1` | `test-driven-development` skill |
| `verification-v1` | `verification-before-completion` skill |
| `receiving-code-review` | `receiving-code-review` skill |
| `requesting-code-review` | `requesting-code-review` skill |
| `finishing-a-development-branch` | `finishing-a-development-branch` skill |
| `using-git-worktrees` | `using-git-worktrees` skill |
| `dispatching-parallel-agents` | `dispatching-parallel-agents` skill |
| `executing-plans` | `executing-plans` skill |
| `using-superpowers` | `using-overpowers` skill |
| `writing-skills` | `writing-skills` skill |
| `writing-plans-v1` | `writing-plans` skill |
| `mcp-builder` | `mcp-builder` skill |
| `frontend-design` | `frontend-design` skill |
| `web-design-guidelines` | `web-design-guidelines` skill |
| `playwright-skill` | `playwright-skill` skill |
| `react-best-practices` | `react-best-practices` skill (ADAPT: theirs is better) |
| `llm-application-dev` | `llm-application-dev` skill (ADAPT: theirs is better) |
| `backend-development` | `backend-development` skill (ADAPT: theirs adds 9 sub-skills) |
| `frontend-mobile-development` | `frontend-design` + framework experts (ADAPT: adds patterns) |
| `python-development` | `python-development` skill (ADAPT: adds 5 sub-skills) |
| `javascript-typescript` | `javascript-typescript` skill (ADAPT: adds 4 sub-skills) |
| `prompt-factory` | `prompt-optimizer` skill (different focus) |
| `hooks-automation` | `hooks-automation` skill (ADAPT: theirs is better) |
| `subagent-driven-development` | `subagent-driven-development` skill |
| `skill-creator-v1` | `skill-creator` skill |

---

## Key Findings

### 1. Almost All Recommendations Are SKILLS, Not AGENTS

Out of 127 items reviewed:
- Only **6 items (4.7%)** should be agents
- **103 items (81%)** are methodologies/workflows = SKILLS
- **18 items (14%)** are other types (scripts, templates, commands, workflows)

### 2. The 6 New Agents Are All Factory Guides

All agent recommendations come from `alirezarezvani-claude-code-skill-factory`:
- `factory-guide` (orchestrator)
- `skills-guide` (skills specialist)
- `prompts-guide` (prompts specialist)
- `agents-guide` (agents specialist)
- `hooks-guide` (hooks specialist)
- `claude-md-guardian` (maintenance agent)

These form a cohesive "Factory Guide System" for interactive asset generation.

### 3. Major New Skill Domains

Skills filling gaps in Overpowers:
- **Security/Pentesting**: 23 skills (OWASP, SQLi, XSS, privilege escalation, etc.)
- **Infrastructure/DevOps**: 20 skills (K8s, cloud, CI/CD, observability)
- **Design System**: 1 skill (`ui-ux-pro-max` with 50 styles, 97 palettes)
- **LLM/AI Development**: 9 enhanced skills (RAG, embeddings, evaluation)
- **Specialized Domains**: 15 skills (blockchain, payments, game dev, trading)

### 4. Significant Overlaps to ADAPT (not duplicate)

These exist but should be enhanced with antigravity versions:
- `test-driven-development` → stronger enforcement
- `systematic-debugging` → iron law, 4-phase process
- `react-best-practices` → 45 Vercel rules vs 23 lines
- `llm-application-dev` → adds 7 sub-skills
- `backend-development` → adds CQRS, event sourcing, sagas

---

## Recommendations

### For Agents (6 items)
Copy to `Overpowers/agents/`:
```
factory-guide.md
skills-guide.md  
prompts-guide.md
agents-guide.md
hooks-guide.md
claude-md-guardian.md → agents_md_guardian.md (renamed)
```

### For Skills (103 items)
Copy to `Overpowers/skills/` following existing directory structure.

**Priority 1 - New Domains:**
- Security skills → `Overpowers/skills/security/`
- Infrastructure skills → `Overpowers/skills/infrastructure/`
- `ui-ux-pro-max` → `Overpowers/skills/ui_ux_pro_max/`
- Factory skills → `Overpowers/skills/[factory-name]/`

**Priority 2 - Enhancements:**
- Replace/merge existing skills with superior versions
- Add sub-skill expansions (LLM, backend, frontend, Python, JS/TS)

---

## Status

**Classification Complete** ✓

This is a classification-only report. No implementation changes have been made.
