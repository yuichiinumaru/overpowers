#!/bin/bash
set -e

function usage() {
    echo "Usage: ./nx-explore.sh <command> [options]"
    echo ""
    echo "Commands:"
    echo "  projects            List all projects"
    echo "  apps                List app projects"
    echo "  libs                List lib projects"
    echo "  affected [base]     List affected projects (default base: main)"
    echo "  targets <project>   List all targets for a project"
    echo "  dependents <lib>    Find projects that import <lib>"
    echo "  info <project>      Get full JSON info for <project>"
    echo ""
}

if [ -z "$1" ]; then
    usage
    exit 1
fi

CMD=$1
shift

case "$CMD" in
    projects)
        nx show projects
        ;;
    apps)
        nx show projects --type app
        ;;
    libs)
        nx show projects --type lib
        ;;
    affected)
        BASE=${1:-main}
        nx show projects --affected --base="$BASE"
        ;;
    targets)
        if [ -z "$1" ]; then echo "Missing project name"; exit 1; fi
        nx show project "$1" --json | jq '.targets | keys'
        ;;
    dependents)
        if [ -z "$1" ]; then echo "Missing library name (e.g. @myorg/lib)"; exit 1; fi
        echo "Searching for imports of $1 in apps/ and libs/..."
        grep -r "from '$1'" --include="*.ts" --include="*.tsx" apps/ libs/ || echo "No dependents found."
        ;;
    info)
        if [ -z "$1" ]; then echo "Missing project name"; exit 1; fi
        nx show project "$1" --json
        ;;
    *)
        usage
        exit 1
        ;;
esac
