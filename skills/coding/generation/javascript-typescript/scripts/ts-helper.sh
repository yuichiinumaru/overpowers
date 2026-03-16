#!/bin/bash

# TypeScript Helper
# Requirement: npx, typescript (tsc)

usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  check      Run TypeScript type checking (no emit)"
    echo "  build      Run TypeScript compilation"
    echo "  lint       Run ESLint if configured"
    echo ""
}

case "$1" in
    check)
        echo "Running TypeScript type check..."
        npx tsc --noEmit
        ;;
    build)
        echo "Building project..."
        npx tsc
        ;;
    lint)
        if [ -f "package.json" ] && grep -q '"lint"' "package.json"; then
            echo "Running configured lint script..."
            npm run lint
        else
            echo "Running ESLint..."
            npx eslint . --ext .js,.jsx,.ts,.tsx
        fi
        ;;
    *)
        usage
        exit 1
        ;;
esac
