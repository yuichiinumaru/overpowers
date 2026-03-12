#!/bin/bash
# Scaffold a project based on Zenith architecture (Next.js + FastAPI)

PROJECT_NAME=${1:-"my-zenith-project"}

echo "Scaffolding project: $PROJECT_NAME"

mkdir -p "$PROJECT_NAME"/{frontend/src/{app/api,components/{ui,forms,layouts},hooks,lib,types,config},backend/{routers,services,tests},deploy,docs,scripts}

# Frontend boilerplate
cat > "$PROJECT_NAME"/frontend/package.json <<EOF
{
  "name": "$PROJECT_NAME-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest",
    "test:e2e": "playwright test"
  }
}
EOF

# Backend boilerplate
cat > "$PROJECT_NAME"/backend/pyproject.toml <<EOF
[tool.poetry]
name = "$PROJECT_NAME-backend"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.115.0"
pydantic = "^2.9.0"
supabase = "^2.9.0"
anthropic = "^0.34.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0.0"
httpx = "^0.27.0"
pytest-asyncio = "^0.23.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# Root README
cat > "$PROJECT_NAME"/README.md <<EOF
# $PROJECT_NAME

Project based on Zenith architecture.

## Structure
- \`frontend/\`: Next.js 15 App Router
- \`backend/\`: FastAPI
- \`deploy/\`: Deployment configurations
- \`docs/\`: Documentation
EOF

echo "Done. Project $PROJECT_NAME scaffolded."
