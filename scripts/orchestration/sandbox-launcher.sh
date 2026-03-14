#!/bin/bash
# Sandbox Launcher
# Starts the Overpowers Docker Sandbox with correct user mapping.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SANDBOX_DIR="$PROJECT_ROOT/sandbox"

echo "🔮 Preparing Overpowers Sandbox..."

# Detect User
export HOST_UID=$(id -u)
export HOST_GID=$(id -g)
export HOST_USER=$(whoami)

echo "   User: $HOST_USER ($HOST_UID:$HOST_GID)"

cd "$SANDBOX_DIR"

ACTION="${1:-up}"

if [ "$ACTION" == "build" ]; then
    echo "🏗️  Building sandbox image..."
    docker compose build
elif [ "$ACTION" == "down" ]; then
    echo "🛑 Stopping sandbox..."
    docker compose down
elif [ "$ACTION" == "exec" ]; then
    shift
    echo "⚡ Executing in sandbox: $@"
    docker exec overpowers-sandbox bash -c "$@"
elif [ "$ACTION" == "ssh" ]; then
    echo "🔑 Connecting to sandbox via SSH..."
    # Check if running
    if ! docker compose ps | grep -q "Up"; then
        echo "   Sandbox not running. Starting..."
        docker compose up -d
    fi
    ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$HOST_USER@localhost"
elif [ "$ACTION" == "up" ]; then
    echo "🚀 Starting sandbox..."
    docker compose up -d
    echo "✅ Sandbox running on port 2222 (SSH)."
    echo "   Connect: ssh -p 2222 $HOST_USER@localhost"
    echo "   Password: overpowers"
    echo "   Or use: ./scripts/orchestration/sandbox-launcher.sh ssh"
else
    echo "Usage: $0 [up|down|build|exec <command>|ssh]"
    exit 1
fi
