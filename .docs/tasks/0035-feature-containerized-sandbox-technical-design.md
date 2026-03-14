# Technical Design: Containerized Sandbox

## 1. Architecture Overview
The sandbox is a Docker-based environment that mirrors the host's development tools while isolating the execution. It uses `docker-compose` for orchestration and an entrypoint script for dynamic user configuration.

## 2. Components

### Docker Image (`sandbox/Dockerfile`)
- **Base**: `ubuntu:22.04`
- **Languages**: Python 3.11, Node.js 20
- **Tools**: `gh` CLI, `zsh`, `playwright` dependencies, `supervisor`, `openssh-server`.
- **User**: Dynamically created at runtime to match host UID/GID.

### Launcher Script (`scripts/orchestration/sandbox-launcher.sh`)
- **Commands**:
  - `build`: Builds the image.
  - `up` (default): Starts the container in detached mode.
  - `down`: Stops and removes the container.
  - `ssh`: Enters the container via SSH.
  - `exec <cmd>`: Runs a command inside the container.

## 3. Data Contracts & Mapping

### Volume Mounts
- `../` (Project Root) -> `/home/${HOST_USER}/workspace`

### Port Mapping
- `2222` (Host) -> `22` (Container) - SSH access.
- `3000-3010` -> Web application testing.

## 4. Implementation Details

### User Mapping Logic
The `entrypoint.sh` script will:
1.  Read `HOST_UID`, `HOST_GID`, and `HOST_USER` from the environment.
2.  Check if the user exists in the container.
3.  If not, create the user with the matching IDs.
4.  Configure passwordless sudo for the user.
5.  Change ownership of the home directory.

## 5. Security Considerations
- **Isolation**: Prevents agent scripts from modifying host system files outside the mounted workspace.
- **SSH Security**: Default password is `overpowers` (changeable via `HOST_PASSWORD`). Access restricted to `localhost` by default in `docker-compose`.

## 6. Testing Strategy
- **Build Test**: `scripts/orchestration/sandbox-launcher.sh build`
- **Functional Test**:
  - Start sandbox.
  - Connect via SSH.
  - Verify `python --version` and `node --version`.
  - Verify project files are visible and writable in `/home/developer/workspace`.
