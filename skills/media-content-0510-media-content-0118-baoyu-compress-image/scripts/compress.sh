#!/bin/bash
# Helper script to run the baoyu-compress-image main.ts
# Usage: ./compress.sh <input> [options]

SKILL_DIR=$(dirname $(dirname $(realpath $0)))
npx -y bun ${SKILL_DIR}/scripts/main.ts "$@"
