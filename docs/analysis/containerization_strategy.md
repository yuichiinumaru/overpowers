# Sanity Gravity Containerization Analysis

**Source**: `references/external_source/sanity-gravity`
**Target**: `sandbox/`

## Core Architecture
Sanity Gravity uses a "fat container" approach managed by `supervisord`. Unlike microservices (one process per container), it treats the container as a full Virtual Machine replacement.

### Key Components
1.  **Dynamic User Mapping**:
    *   The `entrypoint.sh` accepts `HOST_UID` and `HOST_GID` env vars.
    *   It creates a user inside the container matching the host's ID.
    *   This ensures files created in the mounted `/workspace` are owned by the host user, not root.

2.  **Supervisord**:
    *   Used as the init process (`PID 1`).
    *   Manages SSH, XFCE (desktop), VNC, and other background services.
    *   Allows the container to run "headless" or "GUI" modes simultaneously.

3.  **Application Wrapping**:
    *   **Chrome/Electron Fixes**: It wraps `google-chrome` and `antigravity` binaries with scripts that force `--no-sandbox`. This is critical for running Electron apps (like VS Code or Antigravity IDE) inside Docker without the unsafe `--privileged` flag.

4.  **Variants**:
    *   `core`: Basic CLI + XFCE libs + SSH.
    *   `kasm`: Web-based streaming desktop (KasmVNC).
    *   `vnc`: Traditional VNC.

## Implementation Plan for Overpowers
We will adapt the **Core** variant but enhance it for Agentic Development.

### Proposed Changes
1.  **Base Image**: Stick to `ubuntu:22.04` (stable).
2.  **Dependencies**:
    *   Add **Python 3.10+** (for our Python agents).
    *   Add **Node.js 20+** (for TS agents/MCPs).
    *   Add **Playwright** dependencies (browsers) for `browser-use`.
    *   Add **GitHub CLI (`gh`)**.
3.  **Structure**:
    ```
    sandbox/
    ├── docker-compose.yml
    ├── Dockerfile
    ├── entrypoint.sh
    └── config/
        └── supervisord.conf
    ```
4.  **Launcher**: A script to auto-detect UID/GID and run `docker compose up`.

## Value Add
This isolates the complex dependency chain (Python venv, Node modules, system deps for Playwright) into a disposable environment, preventing "it works on my machine" issues.
