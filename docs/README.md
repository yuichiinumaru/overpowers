# Overpowers Documentation

This directory contains guides for using and extending the Overpowers toolkit.

## Quick Links

| Guide | Description |
|-------|-------------|
| [Hooks Guide](hooks-guide.md) | Event-driven automation hooks (29 available) |
| [Scripts Guide](scripts-guide.md) | DevOps and automation scripts (89 available) |
| [Workflows Guide](workflows-guide.md) | Multi-step development workflows (16 available) |
| [Services Guide](services-guide.md) | External service integrations (13 available) |
<<<<<<< HEAD
| [Awesome References](references.md) | Curated list of 50+ plugins, agents, and tools |
| [PREVC Workflow](concepts/prevc-workflow.md) | Planning, Review, Execution, Validation, Confirmation workflow |
=======
>>>>>>> remotes/origin/jules-harvest-mega-session-16505481372407860250

## Installation

### OpenCode

```bash
# Clone the repository
git clone https://github.com/yuichiinumaru/overpowers ~/.config/opencode/Overpowers

# Create symlink for skills discovery
ln -sf Overpowers/skills ~/.config/opencode/skills

# Add plugin to opencode.json
# In the "plugin" array, add:
"./Overpowers/.opencode/plugin/Overpowers.js"
```

### Claude Code

```bash
# Clone to Claude plugins directory
git clone https://github.com/yuichiinumaru/overpowers ~/.claude/plugins/Overpowers

# Enable in settings.json
# Add to "enabledPlugins": { "Overpowers@Overpowers-dev": true }
```

### Codex (OpenAI)

```bash
# Clone to Codex directory
git clone https://github.com/yuichiinumaru/overpowers ~/.codex/Overpowers

# Use the bootstrap command
~/.codex/Overpowers/.codex/Overpowers-codex bootstrap
```

## Directory Structure

```
Overpowers/
├── agents/          # 390+ specialized AI agents
├── commands/        # 228+ slash commands
├── skills/          # 149 reusable skills
├── hooks/           # 29 event-driven hooks
├── scripts/         # 89 DevOps automation scripts
├── workflows/       # 16 multi-step workflows
├── services/        # 13 external service integrations
├── packages/        # Jules Swarm submodule
└── docs/            # This documentation
```

## Configuration

See [opencode-example.json](../opencode-example.json) for a complete configuration example including:

- Recommended plugins
- MCP server configurations
- Custom model providers
- Agent orchestration settings

## Getting Help

- **Issues**: https://github.com/yuichiinumaru/overpowers/issues
- **Main Repo**: https://github.com/yuichiinumaru/overpowers

## Credits

Based on [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent.
