# Technical Design: Installer UX and Modularity

## 1. Architecture Overview
The refactored deployment system will follow a "Base-and-Platform" pattern. A central `deploy-utils.sh` will define the UI and core symlink logic, while individual `deploy-to-*.sh` scripts will define platform-specific constants and custom hooks.

## 2. API Signatures & Data Contracts

### Core Utilities (`scripts/utils/deploy-utils.sh`)
- `deploy_banner(name)`: Prints a unified Cyan banner for the platform.
- `setup_env()`: Resolves `REPO_ROOT` and `SCRIPT_DIR`.
- `validate_dir(path)`: Ensures directory exists or creates it.
- `run_deploy(target_dir, mappings[])`: Orchestrates the `create_symlinks` call.

### Shared Constants (`scripts/utils/shared-constants.sh`)
- Reuse existing colors and basic logging functions.

## 3. Modular Implementation

### `scripts/utils/deploy-utils.sh`
```bash
# Common setup for all deployment scripts
setup_deploy_env() { ... }
# Unified banner
print_deploy_banner() { ... }
# Final summary
print_deploy_summary() { ... }
```

### `scripts/deploy-to-X.sh` (Example)
```bash
source scripts/utils/deploy-utils.sh
setup_deploy_env "Platform Name" "$HOME/.platform"
# Define mappings
SYMLINKS=("src:tgt" ...)
# Run core engine
create_symlinks "$PLATFORM_DIR" "${SYMLINKS[@]}"
# Platform specific overrides
[[ -f "$REPO_ROOT/AGENTS.md" ]] && ln -sf "$REPO_ROOT/AGENTS.md" "$PLATFORM_DIR/rules.md"
print_deploy_summary
```

## 4. System Dependencies
- `gum`: Optional, used for interactive UI.
- `bash`: Core execution environment.
- `python3`: Used for advanced tasks like agent sanitization.

## 5. Security & Performance Considerations
- **Validation:** Always check if `$HOME` is writable and if required directories are detected.
- **Backups:** The symlink engine already supports `.bak` creation; this will be strictly enforced.

## 6. Testing Strategy
- **Mock Deployment:** Run scripts with `DRY_RUN=1` (to be added to `create-symlinks.sh`) to verify paths without mutating the filesystem.
- **Manual Verification:** Execute `install.sh` on a test machine/container to verify the `gum` UI and symlink correctness.
