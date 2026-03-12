#!/bin/bash
# Agent Migration Helper
# Assists with migrating command files to agent definition files

set -e

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  init        - Create the .claude/agents/ directory structure"
    echo "  convert     - Convert a command file to an agent definition file"
    echo "  validate    - Validate an agent definition file"
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

case "$COMMAND" in
    init)
        echo "Creating .claude/agents/ directory structure..."
        mkdir -p .claude/agents/core
        mkdir -p .claude/agents/workflows
        mkdir -p .claude/agents/testing
        mkdir -p .claude/agents/analysis
        mkdir -p .claude/agents/memory
        mkdir -p .claude/agents/automation
        mkdir -p .claude/agents/optimization
        mkdir -p .claude/agents/monitoring
        echo "Directory structure created successfully."
        ;;

    convert)
        if [ -z "$1" ] || [ -z "$2" ]; then
            echo "Error: Source command file and target agent file required."
            echo "Example: $0 convert .claude/commands/core/task-decomposition.md .claude/agents/core/task-decomposition.md"
        else
            SRC_FILE=$1
            DEST_FILE=$2

            echo "Converting $SRC_FILE to $DEST_FILE..."
            # Basic conversion script

            # Ensure destination directory exists
            mkdir -p "$(dirname "$DEST_FILE")"

            cat << 'YAML' > "$DEST_FILE"
---
role: orchestrator
name: Converted Agent
responsibilities:
  - Inherited from command file
capabilities:
  - auto-converted
triggers:
  - pattern: "converted"
---
YAML
            cat "$SRC_FILE" >> "$DEST_FILE"
            echo "Conversion complete. Please manually review the YAML frontmatter in $DEST_FILE."
        fi
        ;;

    validate)
        if [ -z "$1" ]; then
            echo "Error: Agent definition file required."
        else
            AGENT_FILE=$1
            echo "Validating $AGENT_FILE..."
            if ! grep -q "^---" "$AGENT_FILE"; then
                echo "Error: Missing YAML frontmatter."
            elif ! grep -q "^role:" "$AGENT_FILE"; then
                echo "Error: Missing 'role' in frontmatter."
            elif ! grep -q "^name:" "$AGENT_FILE"; then
                echo "Error: Missing 'name' in frontmatter."
            else
                echo "Basic validation passed for $AGENT_FILE."
            fi
        fi
        ;;

    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
