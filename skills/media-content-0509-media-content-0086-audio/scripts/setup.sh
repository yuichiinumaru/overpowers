#!/bin/bash
# Install @remotion/media depending on the package manager in use

if [ -f "package-lock.json" ]; then
    npx remotion add @remotion/media
elif [ -f "bun.lockb" ]; then
    bunx remotion add @remotion/media
elif [ -f "yarn.lock" ]; then
    yarn remotion add @remotion/media
elif [ -f "pnpm-lock.yaml" ]; then
    pnpm exec remotion add @remotion/media
else
    echo "No known package manager lockfile found. Using npm..."
    npx remotion add @remotion/media
fi
