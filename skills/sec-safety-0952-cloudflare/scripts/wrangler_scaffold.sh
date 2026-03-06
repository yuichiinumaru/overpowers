#!/bin/bash
# Scaffold a basic Cloudflare Worker

PROJECT_NAME=${1:-"my-worker"}

echo "Creating Cloudflare Worker: $PROJECT_NAME"
npx wrangler generate "$PROJECT_NAME"

cd "$PROJECT_NAME"
echo "Project created. Don't forget to review wrangler.toml!"
