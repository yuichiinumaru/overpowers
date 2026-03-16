#!/bin/bash
# AgentDB Learning Helper Script
# Helps manage AgentDB plugins and templates

set -e

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  create <type> <name>  - Create a new learning plugin"
    echo "  list-plugins          - List installed plugins"
    echo "  info <name>           - Get information about a plugin"
    echo "  list-templates        - List available templates"
    echo ""
    echo "Available Plugin Types:"
    echo "  decision-transformer, q-learning, sarsa, actor-critic,"
    echo "  active-learning, adversarial-training, curriculum-learning,"
    echo "  federated-learning, multi-task-learning"
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

# Default npx command (can be overridden by environment variable)
AGENTDB_CMD=${AGENTDB_CMD:-"npx agentdb@latest"}

case "$COMMAND" in
    create)
        if [ -z "$1" ] || [ -z "$2" ]; then
            echo "Error: Plugin type and name required."
            echo "Example: $0 create decision-transformer my-dt-agent"
        else
            TYPE=$1
            NAME=$2
            echo "Creating $TYPE plugin named $NAME..."
            $AGENTDB_CMD create-plugin -t "$TYPE" -n "$NAME"
        fi
        ;;

    list-plugins)
        echo "Listing AgentDB plugins..."
        $AGENTDB_CMD list-plugins
        ;;

    info)
        if [ -z "$1" ]; then
            echo "Error: Plugin name required."
        else
            NAME=$1
            echo "Getting info for plugin $NAME..."
            $AGENTDB_CMD plugin-info "$NAME"
        fi
        ;;

    list-templates)
        echo "Listing AgentDB templates..."
        $AGENTDB_CMD list-templates
        ;;

    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
