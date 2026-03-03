[<img width="3168" height="1344" alt="Gemini_Generated_Image_e9pigpe9pigpe9pi" src="https://github.com/user-attachments/assets/0ebf9eaa-3226-4be3-b012-589f6d5ea6e0" />](https://www.youtube.com/watch?v=M_XwzBMTJaM)

# Overpowers 🚀

**Overpowers** is a consolidated, opinionated, and massively expanded toolkit for AI coding assistants. Built upon the foundation of [overpowers](https://github.com/obra/overpowers) by [Jesse Vincent](https://github.com/obra), it centralizes agents, skills, commands, hooks, scripts, workflows, and services into a single, highly capable repository.

Works with **OpenCode**, **Gemini CLI**, **Google Antigravity**, and **Kilo Code** out of the box.

> **Note**: This is a fork with curated integrations, personal touches, and additional components based on my own workflow. The original overpowers is an excellent starting point — this version adds opinionated expansions.

## 📊 Inventory

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 467+ | Specialized AI personas for every task |
| **Skills** | 333+ | Complex workflow automation (SKILL.md) |
| **Workflows** | 263+ | Complete process guides (also serve as commands) |
| **Scripts** | 110+ | DevOps, automation & setup helpers |
| **Hooks** | 29 | Pre/post action notifications |
| **Services** | 13 | External service integrations |

**Total: 1200+ components!**

---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yuichiinumaru/overpowers.git ~/Work/overpowers
```

### 2. Run the installer

```bash
cd ~/Work/overpowers
./install.sh
```

The interactive installer will ask which platforms you want to deploy to:

| Platform | What gets deployed | Config directory |
|----------|--------------------|------------------|
| **OpenCode** | agents, skills, commands, hooks, AGENTS.md | `~/.config/opencode/` |
| **Gemini CLI** | skills, hooks, GEMINI.md | `~/.gemini/` |
| **Antigravity** | skills, workflows | `~/.gemini/antigravity/` |
| **Kilo Code** | skills, workflows, rules | `~/.kilocode/` |

It also optionally installs **MCP servers** across all platforms with an interactive `.env` configuration wizard.

### 3. (Optional) Install community plugins

```bash
./scripts/install-plugins.sh
```

Interactive menu with 50+ plugins and themes from the [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) community list.

---

## 🛠 Structure

```
overpowers/
├── install.sh                # ⭐ Master installer
├── agents/                   # 467+ specialized AI agents (.md)
├── skills/                   # 333+ skills (skill-name/SKILL.md)
├── workflows/                # 263+ process guides / commands (.md)
├── hooks/                    # 29 notification integrations
├── commands/                 # Shorthand operations
├── scripts/                  # 110+ DevOps/automation helpers
│   ├── deploy-to-opencode.sh     # Symlink to OpenCode
│   ├── deploy-to-gemini-cli.sh   # Symlink to Gemini CLI
│   ├── deploy-to-antigravity.sh  # Symlink to Antigravity
│   ├── deploy-to-kilo.sh         # Symlink to Kilo Code
│   ├── install-mcps.sh           # Unified MCP installer
│   └── install-plugins.sh        # Community plugin installer
├── services/                 # 13 external service configs
├── templates/                # Skill/agent templates
├── docs/                     # Documentation
├── opencode-example.json     # Reference OpenCode config
├── .env.example              # API keys & paths template
├── AGENTS.md                 # Global rules (constitution)
└── CHANGELOG.md              # Immutable change history
```

---

## 🔧 Scripts Reference

### Deployment Scripts

| Script | Purpose |
|--------|---------|
| `install.sh` | Master installer — orchestrates all deploys + MCPs |
| `scripts/deploy-agent-army.sh` | Automatically generates configs and injects hundreds of agents |
| `scripts/deploy-to-opencode.sh` | Symlinks agents, skills, commands, hooks → `~/.config/opencode/` |
| `scripts/deploy-to-gemini-cli.sh` | Symlinks skills, hooks, AGENTS.md → `~/.gemini/` |
| `scripts/deploy-to-antigravity.sh` | Symlinks skills, workflows → `~/.gemini/antigravity/` |
| `scripts/deploy-to-kilo.sh` | Symlinks skills, workflows, rules → `~/.kilocode/` |

### Configuration Scripts

| Script | Purpose |
|--------|---------|
| `scripts/install-mcps.sh` | Unified MCP installer across platforms |
| `scripts/install-plugins.sh` | Interactive community plugin/theme installer |
| `scripts/install-personas.sh` | Installs system personas |
| `scripts/install-antigravity-skills.sh` | Installs specific Antigravity skills |
| `scripts/setup-browser-use.sh` | Sets up browser automation |
| `scripts/setup-local-api-keys.sh` | Sets up local API keys safely |
| `scripts/setup-vibe-kanban.sh` | Sets up Vibe Kanban board |

### How the symlinks work

All deploy scripts create **absolute symlinks** from the repo into each platform's config directory. This means:

- Changes to the repo are **instantly reflected** in all platforms
- `git pull` updates everything everywhere at once
- Re-running the installer is **idempotent** — it skips already-correct links

---

## 🔗 MCP Server Configuration

The `opencode-example.json` contains pre-configured MCP servers. The `install-mcps.sh` script handles:

1. **Schema translation**: Converts between OpenCode format (`command` array + `environment`) and Antigravity format (`command` string + `args` array + `env`)
2. **Non-destructive merge**: Never overwrites existing MCP entries
3. **Centralized `.env`**: All API keys and paths live in a single `.env` file at the repo root
4. **Interactive setup**: Optionally enter values during installation or fill them in later

### Included MCP Servers

| Server | Description |
|--------|-------------|
| Serena | Semantic code analysis |
| Vibe Check | Code quality assessment |
| Hyperbrowser | Browser automation |
| Genkit | Firebase AI toolkit |
| Memcord | Memory coordination |
| Semgrep | Static analysis |
| In Memoria | Persistent memory |
| Playwright | Browser testing |
| Context7 | Documentation lookup |
| NotebookLM | Google NotebookLM integration |

---

## 🔀 Jules Swarm Integration

The [jules-swarm](https://github.com/yuichiinumaru/jules-swarm) enables parallel task processing with multiple Google Jules accounts.

### 4-Stage Workflow

1. **`/skill jules-dispatch`** — Send tasks to Jules with prompt optimization
2. **`/skill jules-harvest`** — Fetch completed branches into local worktrees
3. **`/skill jules-triage`** — Parallel review and rating of branches
4. **`/skill jules-integrate`** — Selective merge with attribution

See `workflows/jules-orchestration.md` for the complete guide.

---

## 🎯 YouTube Skill Mining

The `youtube-ripper` agent autonomously mines YouTube channels for procedural content and converts it into skills.

```bash
# Invoke the agent
@youtube-ripper

# Or follow the workflow
/workflow youtube-skill-mining
```

Uses `youtube-link-extractor` and `youtube-skill-creator` skills in a cyclic batch loop.

---

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

### Finding Components

```bash
# Search agents by name
ls agents/ | grep "security"

# Search skills
ls skills/ | grep "aws"

# Count totals
echo "Agents: $(find agents/ -name '*.md' | wc -l)"
echo "Skills: $(find skills/ -name 'SKILL.md' | wc -l)"
echo "Workflows: $(find workflows/ -name '*.md' | wc -l)"
```

---

## 🙏 Credits & Attribution

### Original overpowers
Based on [**overpowers**](https://github.com/obra/overpowers) by **Jesse Vincent** ([@obra](https://github.com/obra)), an agentic skills framework and software development methodology.

### Additional Sources
Components curated from various open-source projects including:
- [buildwithclaude](https://github.com/anthropics/buildwithclaude) — Additional agents, commands, and hooks
- [claude-flow](https://github.com/ruvnet/claude-flow) — Advanced swarm and orchestration skills
- [awesome-legal-skills](https://github.com/malik-taier/awesome-legal-skills) — Multi-language legal document skills
- [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) — Community plugin catalog
- And many more from the community

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
4. **Always update `CHANGELOG.md`** (it's an immutable law here)

## 📜 License

MIT License — Based on [overpowers](https://github.com/obra/overpowers) by Jesse Vincent. See [LICENSE](LICENSE) for details.

---

*Built with 💜 upon the foundation of overpowers by Jesse Vincent*
