#!/bin/bash

# Flow Type Checking Helper
# Requirement: yarn

usage() {
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  check [renderer] Check types for a renderer (default: dom-node)"
    echo "  ci               Run comprehensive CI type checking (slow)"
    echo ""
    echo "Renderers: dom-node, dom-browser, native, fabric"
}

case "$1" in
    check)
        renderer="${2:-dom-node}"
        echo "Running Flow check for $renderer..."
        yarn flow "$renderer"
        ;;
    ci)
        echo "Running comprehensive Flow CI check..."
        yarn flow-ci
        ;;
    *)
        usage
        exit 1
        ;;
esac
