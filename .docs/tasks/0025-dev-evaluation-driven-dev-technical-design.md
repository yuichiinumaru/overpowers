# Technical Design: EvDD QA Framework

## Architecture
The framework consists of a set of static JSON schemas and a Python-based validation engine.

### Directory Structure
```
.agents/schemas/
├── skill_frontmatter.schema.json
├── evals.schema.json
└── openai_yaml.schema.json

scripts/
└── evdd_validate.py

commands/
└── evdd/
    └── validate.toml
```

## Component Details

### 1. JSON Schemas
Schemas will be defined using JSON Schema Draft 7+.

#### `skill_frontmatter.schema.json`
Validates the YAML frontmatter of `SKILL.md`.
- Required fields: `name`, `description`.
- Constraints: `name` must be hyphen-case, max 64 chars. `description` max 1024 chars.

#### `evals.schema.json`
Validates `evals/evals.json`.
- Structure: `{ "skill_name": string, "evals": [ { "id": int, "prompt": string, "expectations": [string] } ] }`.

#### `openai_yaml.schema.json`
Validates `agents/openai.yaml`.
- Validates the `interface` and `dependencies` blocks.

### 2. Validation Engine (`evdd_validate.py`)
- **Inputs**: Path to a skill directory.
- **Process**:
    1.  Parse `SKILL.md` frontmatter using `PyYAML`.
    2.  Load and validate frontmatter against `skill_frontmatter.schema.json` using `jsonschema` library.
    3.  If `evals/evals.json` exists, validate against `evals.schema.json`.
    4.  If `agents/openai.yaml` exists, validate against `openai_yaml.schema.json`.
- **Output**: JSON or human-readable report of pass/fail and specific errors.

### 3. Command Integration (`/evdd:validate`)
- Wraps the `evdd_validate.py` script.
- Support arguments: `[path]` (defaults to all skills if omitted).

## Implementation Details

### Dependency Management
- The script will require `jsonschema` and `PyYAML`.
- It will check for these dependencies and provide instructions if missing.

### Error Handling
- The engine will use a "collector" pattern to report all errors in a single pass rather than failing on the first one.

## Alternatives Considered
- **Zod (TypeScript)**: Rejected because many Overpowers tools are Python-based and we want a lightweight CLI tool that doesn't necessarily require a Node environment.
- **Pydantic**: Considered, but JSON Schema is more portable and language-agnostic for the definition of the standards themselves.

## Security Considerations
- The script only reads files and performs schema validation. No external network calls (except optionally to fetch schemas if not local, but we will store them locally).
- Path traversal protection: Ensure provided paths are within the workspace.
