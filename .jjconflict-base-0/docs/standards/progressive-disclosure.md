# Progressive Disclosure Framework

The Progressive Disclosure Framework is a strategic design pattern for managing large numbers of skills and complex information in AI agent systems. It aims to reduce initial context size, improve token efficiency, and enable scalable capability discovery.

## The 3-Level Loading Pattern

Information is exposed to the agent in three distinct layers:

### Level 1: Discovery (Metadata)
- **Content**: Skill names and brief (1-2 sentence) descriptions.
- **Delivery**: Injected directly into the agent's initial instructions or system prompt.
- **Purpose**: Allows the agent to know *what* capabilities exist without being overwhelmed by *how* to use them.

### Level 2: Instructions (Execution)
- **Content**: The full `SKILL.md` content, including detailed usage instructions, triggers, and examples.
- **Delivery**: Loaded on-demand when the agent identifies a relevant skill (e.g., via `load_skill(name)`).
- **Purpose**: Provides the specific logic and process for performing a task once it has been selected.

### Level 3: Resources (Deep Context)
- **Content**: Extensive documentation, large data files, complex schemas, or specialized reference materials.
- **Delivery**: Loaded only if the agent explicitly needs more depth (e.g., via `read_skill_resource(name, resource)`).
- **Purpose**: Handles "heavy" content that would otherwise bloat the main skill instructions.

## Implementation Standards

### 1. Anthropic-Compatible Frontmatter
All skills MUST include YAML frontmatter in their `SKILL.md`:
```yaml
---
name: skill-identifier
description: Clear, action-oriented description with triggers.
version: 1.0.0
category: engineering
---
```

### 2. Instruction Limits
- **SKILL.md** should aim for under 500 lines.
- Complex skills should offload documentation to the `resources/` directory.

### 3. File Organization
Skills should follow a flat, one-level-deep directory structure:
```text
skill-name/
├── SKILL.md       # Level 2 instructions
├── scripts/       # Level 4 execution (optional)
└── resources/     # Level 3 deep context (optional)
```

## Benefits
- **50-80% Token Reduction**: Agents only carry the context they are actively using.
- **Scalability**: Systems can support hundreds of skills without hitting context limits.
- **Clarity**: High signal-to-noise ratio in the agent's working memory.
