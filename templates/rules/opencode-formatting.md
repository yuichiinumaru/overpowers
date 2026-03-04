# OpenCode Agent Formatting Rules

When creating or modifying agent files (`.md` files in the `agents/` directory) for OpenCode, it is strictly required to follow the OpenCode configuration schema, otherwise the CLI will fail to load the agents and crash.

## 1. The `tools` Field

The `tools` field in the YAML frontmatter **must be a dictionary (record)** of tool names mapped to boolean values.
It **CANNOT** be an array (like `["read", "write"]`) and it **CANNOT** be a comma-separated string (like `"Read, Write"`).

### ❌ Incorrect Formats:

```yaml
tools: "Read, Write, Grep"  # Wrong (String)
tools: ["read", "write"]    # Wrong (Array)
tools: ["*"]                # Wrong (Array)
```

### ✅ Correct Format:

```yaml
tools:
  read: true
  write: true
  grep: true
```

If you want to grant the agent all available tools, you can use the wildcard key:

```yaml
tools:
  "*": true
```

## 2. The `color` Field

The `color` field in the YAML frontmatter **must be a valid hex color code** wrapped in double quotes. 
It **CANNOT** be a named color word like `Navy`, `red`, `blue`, `orange`.

### ❌ Incorrect Formats:

```yaml
color: Navy
color: orange
color: '#FF0000' # Try to avoid single quotes, stick to double quotes
```

### ✅ Correct Format:

```yaml
color: "#000080"
color: "#FFA500"
color: "#FF0000"
```

## Reference Documentation
Always refer to the official OpenCode documentation for configuration schemas:
* Agents: https://opencode.ai/docs/agents/
* Tools: https://opencode.ai/docs/tools/
