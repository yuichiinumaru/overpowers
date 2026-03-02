#!/usr/bin/env bash

set -euo pipefail

# Colors and formatting
BOLD='\033[1m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
RED='\033[31m'
NC='\033[0m'

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGES_DIR="${REPO_ROOT}/packages"
KANBAN_DIR="${PACKAGES_DIR}/vibe-kanban"
KANBAN_REPO="https://github.com/BloopAI/vibe-kanban.git"

echo -e "${BOLD}${CYAN}================================================================${NC}"
echo -e "${BOLD}${CYAN}            Vibe Kanban Setup & Installation Script             ${NC}"
echo -e "${BOLD}${CYAN}================================================================${NC}"
echo ""

mkdir -p "${PACKAGES_DIR}"

# 1. Clone repository
if [ -d "${KANBAN_DIR}" ]; then
    echo -e "  ${CYAN}[~]${NC} Vibe Kanban repository already exists at ${KANBAN_DIR}."
    echo -e "  ${CYAN}[~]${NC} Pulling latest changes..."
    (cd "${KANBAN_DIR}" && git pull origin main || true)
else
    echo -e "  ${CYAN}[~]${NC} Cloning Vibe Kanban from ${KANBAN_REPO}..."
    git clone "${KANBAN_REPO}" "${KANBAN_DIR}"
fi

# 2. Install dependencies
echo -e "\n  ${CYAN}[~]${NC} Installing dependencies (this may take a minute)..."
(cd "${KANBAN_DIR}" && npm install)

# 3. Environment variables setup
echo -e "\n  ${CYAN}[~]${NC} Setting up environment variables..."
if [ ! -f "${KANBAN_DIR}/.env.local" ] && [ -f "${KANBAN_DIR}/.env.example" ]; then
    cp "${KANBAN_DIR}/.env.example" "${KANBAN_DIR}/.env.local"
    echo -e "  ${GREEN}[✓]${NC} Created .env.local from example. You may need to edit it."
else
    echo -e "  ${YELLOW}[i]${NC} .env.local already exists or .env.example not found."
fi

# 4. Build application
echo -e "\n  ${CYAN}[~]${NC} Building Vibe Kanban for production..."
(cd "${KANBAN_DIR}" && npm run build)

# 5. Create launcher script
LAUNCHER_PATH="${REPO_ROOT}/scripts/vibe-kanban.sh"
echo -e "\n  ${CYAN}[~]${NC} Creating launcher script at ${LAUNCHER_PATH}..."

cat > "${LAUNCHER_PATH}" << 'EOF'
#!/usr/bin/env bash
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KANBAN_DIR="${REPO_ROOT}/packages/vibe-kanban"

if [ ! -d "${KANBAN_DIR}" ]; then
    echo "Vibe Kanban is not installed. Run scripts/setup-vibe-kanban.sh first."
    exit 1
fi

echo "Starting Vibe Kanban..."
cd "${KANBAN_DIR}"
npm run start
EOF

chmod +x "${LAUNCHER_PATH}"

# Global alias hint
USER_BIN="${HOME}/.local/bin"
mkdir -p "${USER_BIN}"
ln -sf "${LAUNCHER_PATH}" "${USER_BIN}/vibe-kanban"

echo -e "\n${BOLD}${GREEN}================================================================${NC}"
echo -e "${BOLD}${GREEN}[✓] Vibe Kanban has been successfully installed!${NC}"
echo -e "================================================================"
echo -e "You can start the Kanban board by running either:"
echo -e "  1. ${CYAN}./scripts/vibe-kanban.sh${NC}"
echo -e "  2. ${CYAN}vibe-kanban${NC} (if ~/.local/bin is in your PATH)"
echo -e "================================================================\n"
