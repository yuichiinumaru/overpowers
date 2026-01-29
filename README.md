[<img width="3168" height="1344" alt="Gemini_Generated_Image_e9pigpe9pigpe9pi" src="https://github.com/user-attachments/assets/0ebf9eaa-3226-4be3-b012-589f6d5ea6e0" />](https://www.youtube.com/watch?v=M_XwzBMTJaM)

# Overpowers 🚀

**Overpowers** is a consolidated, opinionated, and massively expanded toolkit for OpenCode/Claude Code. Built upon the foundation of [Superpowers](https://github.com/obra/superpowers) by [Jesse Vincent](https://github.com/obra), it centralizes agents, skills, commands, hooks, scripts, workflows, and services into a single, highly capable repository.

> **Note**: This is a fork with personal touches, curated integrations, and additional components based on my own workflow and preferences. The original Superpowers is an excellent starting point—this version adds opinionated expansions.

## 📊 Inventory

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 396+ | Specialized AI personas for every task |
| **Personas** | 13 | Pre-configured MCP bundles by role |
| **Commands** | 230+ | Shorthand operations for common tasks |
| **Skills** | 173+ | Complex workflow automation |
| **Hooks** | 29 | Pre/post action notifications |
| **Scripts** | 90 | DevOps & automation helpers |
| **Workflows** | 21+ | Complete process guides |
| **Services** | 13 | External service integrations |

**Total: 960+ components!**

## 🙏 Credits & Attribution

### Original Superpowers
This project is based on [**Superpowers**](https://github.com/obra/superpowers) by **Jesse Vincent** ([@obra](https://github.com/obra)), an agentic skills framework and software development methodology. We extend our deepest gratitude for establishing the patterns and architecture that make this enhanced version possible.

### Jules Swarm
The Jules integration is powered by [**jules-swarm**](https://github.com/yuichiinumaru/jules-swarm), included as a submodule for seamless task distribution across multiple Google Jules accounts.

### Additional Sources
Components were curated and integrated from various open-source projects in the Claude Code/OpenCode ecosystem, including:
- [buildwithclaude](https://github.com/anthropics/buildwithclaude) - Additional agents, commands, and hooks
- [claude-flow](https://github.com/ruvnet/claude-flow) - Advanced swarm and orchestration skills
- [awesome-legal-skills](https://github.com/malik-taier/awesome-legal-skills) - Multi-language legal document skills
- And many more from the awesome Claude Code community

## 🌟 What's Different from Superpowers?

| Feature | Superpowers | Overpowers |
|---------|-------------|------------|
| Agents | ~50 | 390+ |
| Skills | ~30 | 149+ |
| Commands | ~30 | 228+ |
| Hooks | ❌ | 29 |
| Scripts | ❌ | 90 |
| Workflows | ❌ | 16 |
| Services | ❌ | 13 |
| Jules Integration | ❌ | Full Swarm (4-stage) |
| Legal Skills | ❌ | 9 (multi-language) |

## 🔧 Jules Swarm Integration

The [jules-swarm](https://github.com/yuichiinumaru/jules-swarm) submodule enables parallel task processing with multiple Google Jules accounts.

### Setup

```bash
# Initialize the submodule after cloning
git submodule update --init --recursive
```

### Usage

The Jules Swarm provides a 4-stage workflow:

1. **`/skill jules-dispatch`** - Send tasks to Jules accounts with prompt optimization
2. **`/skill jules-harvest`** - Fetch completed branches into local worktrees
3. **`/skill jules-triage`** - Parallel review and rating of branches
4. **`/skill jules-integrate`** - Selective merge with attribution

See `workflows/jules-orchestration.md` for the complete workflow guide.

## 🛠 Structure

```
Overpowers/
├── agents/           # 390+ specialized AI agents
├── commands/         # 228+ shorthand operations
├── skills/           # 149+ workflow automations
│   ├── jules-dispatch/
│   ├── jules-harvest/
│   ├── jules-triage/
│   └── jules-integrate/
├── hooks/            # 29 notification integrations
├── scripts/          # 90 DevOps/automation helpers
├── workflows/        # 16 complete process guides
├── services/         # 13 external service configs
├── packages/         # Submodules
│   └── jules-swarm/  # Jules integration SDK
└── .opencode/        # Plugin configuration
```

## 🚀 Getting Started

### 1. Clone with Submodules

```bash
git clone --recursive https://github.com/yuichiinumaru/overpowers.git ~/.config/opencode/Overpowers

# Or if already cloned:
cd ~/.config/opencode/Overpowers
git submodule update --init --recursive
```

## 🎭 Personas (NEW!)

**Personas** are pre-configured MCP bundles that automatically load the right tools for your role. Each persona consolidates multiple agents into a role-specific configuration with **YAAMCPL-validated MCP winners**.

### Quick Install

```bash
# List available personas
./install-personas.sh

# Install a specific persona
./install-personas.sh devops-engineer
```

### Available Personas

| Persona | Agents | MCPs | Best For |
|---------|--------|------|----------|
| **devops-engineer** | 14 | 7 | K8s, Docker, CI/CD, monitoring |
| **fullstack-developer** | 39 | 6 | Web dev, GitHub, filesystem |
| **security-auditor** | 11 | 4 | Pentesting, vulnerability assessment |
| **ai-ml-engineer** | 21 | 5 | ML pipelines, vector memory |
| **database-specialist** | 15 | 5 | MySQL, Redis, universal gateway |
| **comprehensive-researcher** | 23 | 6 | Research, web scraping, memory |
| **qa-engineer** | 14 | 4 | Testing, coverage analysis |
| **system-architect** | 16 | 4 | Design, architecture review |
| **documentation-writer** | 9 | 4 | Technical writing, API docs |
| **mobile-developer** | 8 | 4 | iOS, Android, Flutter |
| **product-manager** | 9 | 4 | Planning, agile, research |
| **language-specialist** | 19 | 4 | Language-specific development |
| **general-assistant** | 198 | 2 | General purpose |

### With HyperTool

```bash
npx -y @toolprint/hypertool-mcp mcp run --persona devops-engineer
```

### Advanced Configuration

For granular control over which MCPs are enabled (security-conscious users):

```bash
./configure-persona.sh devops-engineer
```

This interactive wizard:
- 🔒 Shows **risk levels** for each MCP (HIGH/MEDIUM/LOW)
- ✅ Lets you **enable/disable** individual MCPs
- 🔑 Prompts for **API keys** and environment variables
- 💾 Saves custom config with disabled MCPs preserved

**Risk Levels:**
| Level | MCPs | Description |
|-------|------|-------------|
| 🔴 HIGH | `filesystem`, `terminal` | Direct system access |
| 🟡 MEDIUM | `github`, `docker`, `kubernetes`, `mysql` | External service access |
| 🟢 LOW | `serena`, `vibe-check`, `context7`, etc. | Read-only or sandboxed |

---

## 🎯 Antigravity Skills Installer

Install Overpowers skills directly into **Google Antigravity IDE**!

### Quick Install

```bash
bash ~/.config/opencode/Overpowers/install-antigravity-skills.sh
```

### Features

- 🌐 **Multi-language**: English / Português (BR)
- 📦 **Curated profiles**: Essential, Productivity, Advanced, Developer
- ☢️ **Nuclear Mode**: Install ALL 500+ components (skills, agents, workflows)
- 🔄 **Auto-conversion**: 392 OpenCode agents → Antigravity skills
- 📋 **Workflows included**: 16 complete process guides

### Installation Profiles

| Profile | Components | Best For |
|---------|------------|----------|
| Essential | 6 skills | Core development |
| Productivity | 5 skills | Research & docs |
| Advanced Agents | 5 skills | Multi-agent orchestration |
| Developer | 5 skills | Language-specific |
| All Curated | 21 skills | Recommended |
| **Nuclear** | 500+ | Everything! |

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
# Invoke an agent
/invoke code-reviewer

# Use a skill
/skill jules-dispatch

# Follow a workflow
/workflow security-hardening

# List available skills
/skills:list
```

## 🔧 Recommended Configuration

### Key Orchestrator Agents

For optimal multi-agent coordination, configure these in your `opencode.json`:

```json
{
  "agent": {
    "task_decomposition_expert": {
      "mode": "primary",
      "description": "Breaks complex tasks into parallelizable sub-tasks"
    },
    "code_reviewer": {
      "mode": "subagent",
      "description": "Code quality and security review"
    },
    "security_auditor": {
      "mode": "subagent",
      "description": "Security vulnerability detection"
    },
    "deployment_engineer": {
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

### Agent Chaining Patterns

```
Research → Implementation:
  comprehensive_researcher → task_decomposition_expert → backend_architect → code-reviewer

Security Audit:
  security_auditor → api_security_audit → incident_responder → code-reviewer

Full Stack Feature:
  database_optimizer → backend_architect → frontend_developer → test_automator → deployment-engineer
```

### Finding Agents & Skills

```bash
# Search agents by name
ls ~/.config/opencode/Overpowers/agents/ | grep "security"

# Search skills
ls ~/.config/opencode/Overpowers/skills/

# Count totals
echo "Agents: $(ls Overpowers/agents/ | wc -l)"
echo "Skills: $(ls Overpowers/skills/ | wc -l)"
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📜 License

MIT License - Based on [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent.

See [LICENSE](LICENSE) for details.

---
*Built with 💜 upon the foundation of Superpowers by Jesse Vincent*

## Architecture

See [docs/CODEMAPS/INDEX.md](docs/CODEMAPS/INDEX.md) for detailed architecture.
Also see [JULES_ARCHITECTURAL_DIGEST.md](JULES_ARCHITECTURAL_DIGEST.md) for a high-level architectural digest.

### Key Components
- **Agents**: See [docs/CODEMAPS/agents.md](docs/CODEMAPS/agents.md)
- **Source**: See [docs/CODEMAPS/source.md](docs/CODEMAPS/source.md)
