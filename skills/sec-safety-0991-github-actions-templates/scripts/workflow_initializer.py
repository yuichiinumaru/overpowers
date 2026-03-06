#!/usr/bin/env python3
import sys
import os

TEMPLATES = {
    "test": """name: Test

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
    - uses: actions/checkout@v4

    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Run linter
      run: npm run lint

    - name: Run tests
      run: npm test
""",
    "build": """name: Build and Push

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
    - uses: actions/checkout@v4

    - name: Log in to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=semver,pattern={{major}}.{{minor}}

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
"""
}

def init_workflow(template_name):
    if template_name not in TEMPLATES:
        print(f"Error: Template '{template_name}' not found. Available: {', '.join(TEMPLATES.keys())}")
        return

    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)
    
    filename = os.path.join(workflow_dir, f"{template_name}.yml")
    with open(filename, 'w') as f:
        f.write(TEMPLATES[template_name])
    
    print(f"Successfully initialized workflow: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: workflow_initializer.py <template_name>")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)
    
    init_workflow(sys.argv[1])
