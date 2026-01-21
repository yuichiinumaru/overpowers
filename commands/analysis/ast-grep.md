---
name: ast-grep
description: "Instructions for using ast-grep (sg). Provides patterns for structural search and replace."
---

# ast-grep (sg) Usage

Overpowers does not bundle `ast-grep` binaries, but agents can use it if installed.

## Prerequisites
- Install `ast-grep`: `npm install -g @ast-grep/cli` or `brew install ast-grep`

## Common Patterns

### Search (`sg scan` or `sg run`)

\`\`\`bash
# Find console.log
sg scan -p 'console.log($ARGS)'

# Find specific function definition
sg scan -p 'function $NAME($ARGS) { $$$ }'

# Find React components
sg scan -p 'const $NAME = ($PROPS) => { $$$ return <$TAG>$$$</$TAG> }'
\`\`\`

### Rewrite (`sg run --rewrite`)

\`\`\`bash
# Replace console.log with logger.info
sg run -p 'console.log($ARGS)' --rewrite 'logger.info($ARGS)'
\`\`\`

## Agent Usage
If `sg` is available in the shell, use `run_in_bash_session` to execute these commands.
Always start with a dry-run or scan before rewriting.
