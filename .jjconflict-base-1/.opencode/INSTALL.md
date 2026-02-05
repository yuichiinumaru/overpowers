# Installing overpowers for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Node.js installed
- Git installed

## Installation Steps

### 1. Install overpowers

```bash
mkdir -p ~/.config/opencode/overpowers
git clone https://github.com/yuichiinumaru/overpowers.git ~/.config/opencode/overpowers
```

### 2. Register the Plugin

Create a symlink so OpenCode discovers the plugin:

```bash
mkdir -p ~/.config/opencode/plugin
ln -sf ~/.config/opencode/overpowers/.opencode/plugin/overpowers.js ~/.config/opencode/plugin/overpowers.js
```

### 3. Restart OpenCode

Restart OpenCode. The plugin will automatically inject overpowers context via the chat.message hook.

You should see overpowers is active when you ask "do you have overpowers?"

## Usage

### Finding Skills

Use the `find_skills` tool to list all available skills:

```
use find_skills tool
```

### Loading a Skill

Use the `use_skill` tool to load a specific skill:

```
use use_skill tool with skill_name: "overpowers:brainstorming"
```

### Personal Skills

Create your own skills in `~/.config/opencode/skills/`:

```bash
mkdir -p ~/.config/opencode/skills/my-skill
```

Create `~/.config/opencode/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: Use when [condition] - [what it does]
---

# My Skill

[Your skill content here]
```

Personal skills override overpowers skills with the same name.

### Project Skills

Create project-specific skills in your OpenCode project:

```bash
# In your OpenCode project
mkdir -p .opencode/skills/my-project-skill
```

Create `.opencode/skills/my-project-skill/SKILL.md`:

```markdown
---
name: my-project-skill
description: Use when [condition] - [what it does]
---

# My Project Skill

[Your skill content here]
```

**Skill Priority:** Project skills override personal skills, which override overpowers skills.

**Skill Naming:**
- `project:skill-name` - Force project skill lookup
- `skill-name` - Searches project → personal → overpowers
- `overpowers:skill-name` - Force overpowers skill lookup

## Updating

```bash
cd ~/.config/opencode/overpowers
git pull
```

## Troubleshooting

### Plugin not loading

1. Check plugin file exists: `ls ~/.config/opencode/overpowers/.opencode/plugin/overpowers.js`
2. Check OpenCode logs for errors
3. Verify Node.js is installed: `node --version`

### Skills not found

1. Verify skills directory exists: `ls ~/.config/opencode/overpowers/skills`
2. Use `find_skills` tool to see what's discovered
3. Check file structure: each skill should have a `SKILL.md` file

### Tool mapping issues

When a skill references a Claude Code tool you don't have:
- `TodoWrite` → use `update_plan`
- `Task` with subagents → use `@mention` syntax to invoke OpenCode subagents
- `Skill` → use `use_skill` tool
- File operations → use your native tools

## Getting Help

- Report issues: https://github.com/yuichiinumaru/overpowers/issues
- Documentation: https://github.com/yuichiinumaru/overpowers
