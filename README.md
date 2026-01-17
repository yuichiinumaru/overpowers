# Overpowers 🚀

**Overpowers** is a consolidated, optimized, and enhanced toolkit for OpenCode. It centralizes agents, skills, commands, hooks, scripts, workflows, and services into a single, massively capable repository.

## 📊 Inventory

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 390+ | Specialized AI personas for every task |
| **Commands** | 228+ | Shorthand operations for common tasks |
| **Skills** | 149+ | Complex workflow automation |
| **Hooks** | 29 | Pre/post action notifications |
| **Scripts** | 90 | DevOps & automation helpers |
| **Workflows** | 16 | Complete process guides |
| **Services** | 13 | External service integrations |

**Total: 900+ components!**

## ✨ Credits

This project is built upon the foundation of the original **OpenCode Superpowers** toolkit. We extend our deepest gratitude to the creators and community of Superpowers for establishing the patterns and capabilities that make this enhanced version possible.

## 🌟 Key Features

### Agent Categories
- **Engineering**: `backend-architect`, `frontend-developer`, `nodejs-specialist`, `react-guru`, `vue3-specialist`
- **Security**: `security-auditor`, `api-security-audit`, `incident-responder`
- **Research**: `comprehensive-researcher`, `academic-researcher`, `technical-researcher`
- **Design**: `ui-ux-designer`, `visual-storyteller`, `whimsy-injector`
- **Marketing**: `growth-hacker`, `tiktok-strategist`, `reddit-community-builder`
- **DevOps**: `deployment-engineer`, `ci-cd-specialist`, `docker-specialist`
- **Quality**: `code-reviewer`, `test-automator`, `qa-engineer`

### Skill Highlights
- **Jules Swarm**: 4-stage workflow (`dispatch → harvest → triage → integrate`)
- **Legal**: Multi-language NDA review (EN, ES, PT-BR, FR)
- **DevOps**: GitHub workflow automation, swarm orchestration
- **Research**: Web research, ArXiv search, LangSmith debugging

### Workflow Examples
- `swarm-development` - Parallel multi-agent coordination
- `security-hardening` - Complete security audit
- `marketing-launch` - Product launch coordination
- `jules-orchestration` - Jules account management

## 🛠 Structure

```
Overpowers/
├── agents/           # 390+ specialized AI agents
├── commands/         # 228+ shorthand operations
├── skills/           # 149+ workflow automations
├── hooks/            # 29 notification integrations
├── scripts/          # 90 DevOps/automation helpers
├── workflows/        # 16 complete process guides
├── services/         # 13 external service configs
├── packages/         # Submodules (jules-swarm)
└── .opencode/        # Plugin configuration
```

## 🚀 Getting Started

### 1. Install Overpowers

```bash
git clone https://github.com/yuichiinumaru/overpowers.git ~/.config/opencode/Overpowers
```

### 2. Configure OpenCode

Add to your `opencode.json`:

```json
{
  "plugin": [
    "./Overpowers/.opencode/plugin/Overpowers.js"
  ]
}
```

See `opencode-example.json` for a complete configuration reference with recommended plugins and MCP servers.

### 3. Quick Commands

```bash
# List available agents
ls ~/.config/opencode/Overpowers/agents/

# List available skills
/skills:list

# Invoke an agent
/invoke code-reviewer

# Use a skill
/skill jules-dispatch

# Follow a workflow
/workflow security-hardening
```

## 🔧 Recommended Configuration

### Key Orchestrator Agents

For optimal multi-agent coordination, configure these in your `opencode.json`:

```json
{
  "agent": {
    "task-decomposition-expert": {
      "mode": "primary",
      "description": "Breaks complex tasks into parallelizable sub-tasks"
    },
    "code-reviewer": {
      "mode": "subagent",
      "description": "Code quality and security review"
    },
    "security-auditor": {
      "mode": "subagent",
      "description": "Security vulnerability detection"
    },
    "deployment-engineer": {
      "mode": "subagent",
      "description": "Deployment and release coordination"
    }
  }
}
```

### Recommended Plugins

- `opencode-skills` - Skill loading and management
- `opencode-sessions` - Session persistence
- `opencode-optimal-model-temps` - Temperature optimization
- `opencode-background-agents` - Background agent execution
- `opencode-morph-fast-apply` - Fast code application

### Recommended MCP Servers

- `context7` - Documentation lookup
- `serena` - Code analysis
- `mult-fetch` - Web fetching
- `deepwiki` - AI documentation

## 📖 Usage Tips

### Finding the Right Agent

```bash
# Search by name
ls ~/.config/opencode/Overpowers/agents/ | grep "security"

# Search by content
grep -r "API" ~/.config/opencode/Overpowers/agents/*/
```

### Agent Chaining Patterns

```
Research → Implementation:
  comprehensive-researcher → task-decomposition-expert → backend-architect → code-reviewer

Security Audit:
  security-auditor → api-security-audit → incident-responder → code-reviewer

Full Stack Feature:
  database-optimizer → backend-architect → frontend-developer → test-automator → deployment-engineer
```

### Jules Swarm Workflow

1. `/skill jules-dispatch` - Send tasks to Jules accounts
2. `/skill jules-harvest` - Fetch completed branches
3. `/skill jules-triage` - Review and rate branches
4. `/skill jules-integrate` - Merge selected work

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

---
*Empowering your OpenCode environment with agentic excellence.*
