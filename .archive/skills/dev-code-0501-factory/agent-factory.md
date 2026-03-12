# agent-factory

Agent generation methodology for creating specialized Claude Code agents.

## Workflow

1. **Analyze Requirements**: Understand the specific domain and tasks the agent needs to handle.
2. **Select Template**: Use the appropriate base template from the factory library.
3. **Customize Personality**: Define the agent's persona, tone, and specific instructions.
4. **Define Tools**: Select the optimal set of tools (Read, Write, Bash, etc.) for the agent's purpose.
5. **Generate Agent Document**: Create the `.md` file with proper YAML frontmatter.
6. **Validate**: Ensure the generated agent follows project conventions and safety rules.
