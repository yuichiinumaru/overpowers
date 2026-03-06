#!/bin/bash
# Install @remotion/three depending on the package manager in use

if [ -f "package-lock.json" ]; then
    npx remotion add @remotion/three
elif [ -f "bun.lockb" ]; then
    bunx remotion add @remotion/three
elif [ -f "yarn.lock" ]; then
    yarn remotion add @remotion/three
elif [ -f "pnpm-lock.yaml" ]; then
    pnpm exec remotion add @remotion/three
else
    echo "No known package manager lockfile found. Using npm..."
    npx remotion add @remotion/three
fi
