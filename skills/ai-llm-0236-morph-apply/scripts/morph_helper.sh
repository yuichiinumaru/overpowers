#!/bin/bash

# Morph Fast Apply helper script
# Usage: ./morph_helper.sh --file "path/to/file" --instruction "description" --code_edit "snippet"

uv run python -m runtime.harness scripts/mcp/morph_apply.py "$@"
