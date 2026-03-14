[<img width="3168" height="1344" alt="Gemini_Generated_Image_e9pigpe9pigpe9pi" src="https://github.com/user-attachments/assets/0ebf9eaa-3226-4be3-b012-589f6d5ea6e0" />](https://www.youtube.com/watch?v=M_XwzBMTJaM)

# Overpowers 

**Overpowers** is a consolidated, opinionated, and massively expanded toolkit for AI coding assistants. It centralizes agents, skills, commands, hooks, scripts, workflows, and services into a single, highly capable repository. It's "Power Overwhelming".

Works with **OpenCode**, **Gemini CLI**, **Google Antigravity**, **Kilo Code**, **Codex CLI**, **Claude Code**, **Cursor**, **Windsurf**, and **Factory** out of the box.

## What Overpowers Is (And Is Not)

- **Is**: a cross-project operating layer for coding agents. Install once, then use in any repository.
- **Is**: a safety and orchestration system for solo or parallel execution (manual multi-terminal runs, or provider-level orchestration via MCP/A2A/ACP patterns).
- **Is not**: a single app codebase where assets are meant to be used only inside this repository.
- **Rule of thumb**: this repo is the asset source; your target project is where agents apply those assets.

## 📊 Inventory

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 475+ | Specialized AI personas for every task |
| **Skills** | 1317+ | Complex workflow automation (SKILL.md) |
| **Commands/Workflows** | 303+ | Complete process guides (also serve as commands) |
| **Scripts** | 102+ | DevOps, automation & setup helpers |
| **Hooks** | 45 | Pre/post action notifications |

**Total: 2242+ components!**

---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yuichiinumaru/overpowers.git ~/path/overpowers
```

### 2. Run the installer

```bash
cd ~/path/overpowers
./install.sh
```

The interactive installer will ask which platforms you want to deploy to:

| Platform | What gets deployed | Config directory |
|----------|--------------------|------------------|
| **OpenCode** | agents, skills, commands, hooks, AGENTS.md | `~/.config/opencode/` |
| **Gemini CLI** | skills, hooks, commands, curated agents, GEMINI.md | `~/.gemini/` |
| **Antigravity** | skills, workflows | `~/.gemini/antigravity/` |
| **Kilo Code** | skills, workflows, rules | `~/.kilocode/` |
| **Codex CLI** | skills, AGENTS.MD | `~/.codex/` |
| **Claude Code** | skills, commands, CLAUDE.md | `~/.claude/` |
| **Cursor** | skills | `~/.cursor/` |
| **Windsurf** | skills (via `~/.agents/skills`) | `~/.codeium/windsurf/` |
| **Factory** | skills + droids + AGENTS.md | `~/.factory/` |

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
├── agents/                   # 475+ specialized AI agents (.md)
├── skills/                   # 1317+ skills (skill-name/SKILL.md)
├── workflows/                # 303+ process guides / commands (.md)
├── hooks/                    # 45 notification integrations
├── commands/                 # Shorthand operations
├── scripts/                  # 102+ DevOps/automation helpers
│   ├── deploy-to-opencode.sh     # Symlink to OpenCode
│   ├── deploy-to-gemini-cli.sh   # Symlink to Gemini CLI
│   ├── deploy-to-antigravity.sh  # Symlink to Antigravity
│   ├── deploy-to-kilo.sh         # Symlink to Kilo Code
│   ├── install-mcps.sh           # Unified MCP installer
│   └── install-plugins.sh        # Community plugin installer
├── services/                 # 13 external service configs
├── templates/                # Canonical templates (agents/skills/workflows/configs)
├── docs/                     # Documentation
├── templates/configs/        # MCP templates + policy templates
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
| `scripts/deploy-to-gemini-cli.sh` | Symlinks skills/hooks/commands + curated agents → `~/.gemini/` |
| `scripts/deploy-to-antigravity.sh` | Symlinks skills, workflows → `~/.gemini/antigravity/` |
| `scripts/deploy-to-kilo.sh` | Symlinks skills, workflows, rules → `~/.kilocode/` |
| `scripts/deploy-to-codex.sh` | Symlinks skills + AGENTS.MD → `~/.codex/` |
| `scripts/deploy-to-claude-code.sh` | Symlinks skills/commands + CLAUDE.md → `~/.claude/` |
| `scripts/deploy-to-cursor.sh` | Symlinks skills → `~/.cursor/` |
| `scripts/deploy-to-windsurf.sh` | Symlinks skills → `~/.agents/skills` (Windsurf) |
| `scripts/deploy-to-factory.sh` | Symlinks skills + workflows/toml + AGENTS.md → `~/.factory/` |

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

The MCP templates in `templates/configs/` contain pre-configured server definitions. The `install-mcps.sh` script handles:

1. **Schema translation**: Converts between OpenCode format (`command` array + `environment`) and Antigravity format (`command` string + `args` array + `env`)
2. **Non-destructive merge**: Never overwrites existing MCP entries
3. **Centralized `.env`**: All API keys and paths live in a single `.env` file at the repo root
4. **Interactive setup**: Optionally enter values during installation or fill them in later

### Included MCP Servers

| Server | Description |
|--------|-------------|
| Serena | Semantic code analysis |
| Vibe Check | Code quality assessment |
| Desktop Commander | Local OS automation |
| Hyperbrowser | Cloud browser automation |
| Genkit | Firebase AI toolkit |
| Memcord | Memory coordination |
| Playwright Browser | Local browser testing |
| Context7 | Up-to-date documentation |
| NotebookLM | Google NotebookLM integration |

Semgrep is installed as a CLI tool via `scripts/install-plugins.sh` (CLI Tools category), not as an MCP server.

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

## 📜 License

MIT License — See [LICENSE](LICENSE) for details.
