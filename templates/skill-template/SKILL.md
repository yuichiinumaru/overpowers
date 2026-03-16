---
name: template-skill
description: Brief description of what this skill enables and when to use it
tags:
  - category-tag
version: 1.0.0
category: general
---

# Skill Name

One-paragraph summary of the skill's purpose.

## ⚠️ YAML Frontmatter Rules (MANDATORY)

> **CRITICAL**: Every `SKILL.md` file MUST begin with valid YAML frontmatter enclosed in `---` delimiters.
> Violations cause silent loading failures in Codex CLI, Gemini CLI, and other agent frameworks.

### Required Fields
- **`description`** — MANDATORY. Must NOT be empty. One-line plain text summary.
- **`name`** — Recommended. Lowercase, hyphenated identifier.

### Forbidden Patterns in Frontmatter
| ❌ Forbidden | ✅ Correct | Why |
|:---|:---|:---|
| `description: "Use \"search\" to find"` | `description: Use 'search' to find | Nested double-quotes break YAML |
| `description:` (empty) | `description: A real description` | Empty descriptions silently skip |
| Missing opening `---` | `---` on first line | Frontmatter must start at line 1 |
| `# comment` as field name | `name: value` | YAML comments `#` are not fields |
| `version: "1.0` (unclosed) | `version: 1.0.0` | All quotes must be balanced |
| Entire frontmatter as string | `name: x\ndescription: y` | Must be key-value pairs |

### Safe Description Writing Rules
1. **NEVER** use double-quotes `"` inside description values
2. **PREFER** unquoted descriptions: `description: My skill does X and Y`
3. If quoting is needed, use **single quotes only**: `description: 'My skill does X'`
4. **NEVER** nest quotes: `description: "Use 'this' for \"that\""` is INVALID
5. Keep descriptions to a single line (no multi-line YAML blocks)

## When to Use

- Trigger phrase 1
- Trigger phrase 2

## Prerequisites

- Dependency 1
- Dependency 2

## Instructions

### Step 1: Setup
Description of setup steps.

### Step 2: Execution
Description of main execution flow.

### Step 3: Verification
How to verify the skill worked correctly.

## Examples

```bash
# Example usage
example-command --flag value
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Issue 1 | Fix 1 |
| Issue 2 | Fix 2 |
