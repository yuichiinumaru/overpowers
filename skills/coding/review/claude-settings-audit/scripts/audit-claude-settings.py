#!/usr/bin/env python3
import os
import json

def detect_stack():
    stack = {
        "languages": [],
        "pkg_managers": [],
        "build_tools": [],
        "services": []
    }
    
    files = os.listdir('.')
    
    # Python
    if any(f in files for f in ['pyproject.toml', 'requirements.txt', 'poetry.lock', 'uv.lock']):
        stack["languages"].append("Python")
        if 'poetry.lock' in files: stack["pkg_managers"].append("poetry")
        if 'uv.lock' in files: stack["pkg_managers"].append("uv")
        if 'requirements.txt' in files: stack["pkg_managers"].append("pip")

    # Node.js
    if 'package.json' in files:
        stack["languages"].append("Node.js")
        if 'pnpm-lock.yaml' in files: stack["pkg_managers"].append("pnpm")
        elif 'yarn.lock' in files: stack["pkg_managers"].append("yarn")
        else: stack["pkg_managers"].append("npm")
        if 'tsconfig.json' in files: stack["languages"].append("TypeScript")

    # Go
    if 'go.mod' in files:
        stack["languages"].append("Go")
        stack["pkg_managers"].append("go mod")

    # Rust
    if 'Cargo.toml' in files:
        stack["languages"].append("Rust")
        stack["pkg_managers"].append("cargo")

    # Build Tools
    if 'Makefile' in files: stack["build_tools"].append("make")
    if 'Dockerfile' in files: stack["build_tools"].append("docker")
    if 'docker-compose.yml' in files: stack["build_tools"].append("docker-compose")
    if any(f.endswith('.tf') for f in files): stack["build_tools"].append("terraform")

    return stack

def generate_settings(stack):
    permissions = [
        "Bash(ls:*)", "Bash(pwd:*)", "Bash(find:*)", "Bash(cat:*)", "Bash(grep:*)",
        "Bash(git status:*)", "Bash(git log:*)", "Bash(git diff:*)",
        "Bash(gh pr list:*)", "Bash(gh issue list:*)"
    ]
    
    if "Python" in stack["languages"]:
        permissions.append("Bash(python3 --version:*)")
        if "poetry" in stack["pkg_managers"]: permissions.append("Bash(poetry show:*)")
        if "uv" in stack["pkg_managers"]: permissions.append("Bash(uv pip list:*)")
        if "pip" in stack["pkg_managers"]: permissions.append("Bash(pip list:*)")

    if "Node.js" in stack["languages"]:
        permissions.append("Bash(node --version:*)")
        if "pnpm" in stack["pkg_managers"]: permissions.append("Bash(pnpm list:*)")
        if "npm" in stack["pkg_managers"]: permissions.append("Bash(npm list:*)")
        if "yarn" in stack["pkg_managers"]: permissions.append("Bash(yarn list:*)")

    if "make" in stack["build_tools"]: permissions.append("Bash(make --version:*)")
    if "docker" in stack["build_tools"]: permissions.append("Bash(docker --version:*)")

    return {
        "permissions": {
            "allow": permissions,
            "deny": []
        }
    }

def main():
    print("Claude Settings Audit")
    print("=====================")
    stack = detect_stack()
    print(f"Detected Stack: {stack}")
    
    settings = generate_settings(stack)
    print("\nRecommended .claude/settings.json:")
    print(json.dumps(settings, indent=2))

if __name__ == "__main__":
    main()
