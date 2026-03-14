# Feature Plan: Containerized Sandbox

## 1. Overview
The **Containerized Sandbox** provides an isolated, reproducible environment for AI agents to execute code, run tests, and perform research without risking the host system's stability or security. It uses Docker to create a "clean room" with all necessary development tools pre-installed.

## 2. Goals & Success Criteria
- **Goal:** Provide a safe execution environment for agent-generated code.
- **Success Criteria:**
  - A Docker image with Python, Node.js, and Playwright dependencies is buildable.
  - A single command can launch and enter the sandbox with the current project mounted.
  - The sandbox correctly maps the host user to avoid permission issues.

## 3. Vertical Slices & Milestones

### Slice 1: Sandbox Infrastructure Validation
- **Objective:** Verify the `sandbox/Dockerfile` and `docker-compose.yml` work as expected.
- **Deliverables:** A functional Docker image `overpowers:dev`.

### Slice 2: CLI Integration (Launcher)
- **Objective:** Refine `scripts/orchestration/sandbox-launcher.sh` for multi-platform support and better UX.
- **Deliverables:** Updated `sandbox-launcher.sh`.

### Slice 3: Agent Skill / Documentation
- **Objective:** Create a guide for agents on when to escalate to the sandbox.
- **Deliverables:** `docs/guides/containerized-sandbox.md`.

## 4. Risks & Mitigations
- **Resource Usage:** Docker can be heavy. -> **Mitigation:** Provide clear commands to stop the sandbox (`./scripts/orchestration/sandbox-launcher.sh down`).
- **Permission Mapping:** User ID mismatches between host and container. -> **Mitigation:** Use `HOST_UID`/`HOST_GID` environment variables in the entrypoint script.

## 5. Exit Conditions
- [x] Sandbox image builds successfully.
- [x] Sandbox launches and allows SSH connection.
- [x] Documentation is complete and linked in `AGENTS.md`.
