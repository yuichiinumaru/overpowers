# EvDD (Evaluation-Driven Development) QA Framework

The EvDD QA Framework provides a formal, schema-based validation layer for Overpowers skills. It ensures that every skill in the toolkit adheres to strict structural and metadata standards, enabling high-reliability orchestration and automated testing.

## Core Components

### 1. JSON Schemas
The framework relies on a set of formal JSON schemas located in `.agents/schemas/`:

- **`skill_frontmatter.schema.json`**: Validates the mandatory YAML frontmatter in `SKILL.md`.
- **`evals.schema.json`**: Validates the `evals/evals.json` file used for skill testing.
- **`openai_yaml.schema.json`**: Validates the `agents/openai.yaml` metadata file.

### 2. Validation Script
The `scripts/evdd_validate.py` tool executes the validation logic. It can be run manually or as part of a CI/CD pipeline.

**Usage:**
```bash
# Validate a single skill
python3 scripts/evdd_validate.py skills/my-skill

# Validate all skills
python3 scripts/evdd_validate.py
```

### 3. CLI Command
The `/evdd:validate` command provides a convenient way to trigger validation directly from the Gemini CLI.

**Usage:**
```
/evdd:validate [path]
```

## Standards

### SKILL.md Frontmatter
Every `SKILL.md` must contain a YAML frontmatter block with:
- `name`: Lowercase, hyphenated unique identifier (max 64 chars).
- `description`: Detailed explanation of the skill's purpose and triggers (max 1024 chars).

### agents/openai.yaml
Recommended for all skills to support UI integrations:
- `interface.display_name`: Human-friendly name.
- `interface.short_description`: Concise blurb (25-64 chars).
- `interface.default_prompt`: A sample starting prompt that includes `$skill-name`.

## Workflow for Skill Developers

1.  **Initialize**: Use `scripts/init_skill.py` to bootstrap your skill.
2.  **Implement**: Write your `SKILL.md` and add resources.
3.  **Validate**: Run `/evdd:validate skills/your-skill`.
4.  **Remediate**: Fix any reported schema violations.
5.  **Iterate**: Add evaluations to `evals/evals.json` and validate again.
