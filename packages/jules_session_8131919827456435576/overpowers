#!/bin/bash
# Overpowers Unified Installer & Manager
# The one script to rule them all.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Header
show_header() {
    clear
    echo -e "${CYAN}"
    echo "   ____                                                            "
    echo "  / __ \_   _____  _________  ____ _      _____  __________        "
    echo " / / / / | / / _ \/ ___/ __ \/ __ \ | /| / / _ \/ ___/ ___/        "
    echo "/ /_/ /| |/ /  __/ /  / /_/ / /_/ / |/ |/ /  __/ /  (__  )         "
    echo "\____/ |___/\___/_/  / .___/\____/|__/|__/\___/_/  /____/          "
    echo "                    /_/                                            "
    echo -e "${NC}"
    echo -e "${BLUE}        The Ultimate Agentic Toolkit Manager${NC}"
    echo "================================================================"
}

# Wait for user
pause() {
    echo -e "\n${YELLOW}Press [Enter] to continue...${NC}"
    read -r
}

# Main Loop
while true; do
    show_header
    echo -e "\nSelect an operation:"
    echo "1) 🚀 Deploy Agent Army (Generate Configs)"
    echo "2) 🧠 Install Skills (Antigravity Integration)"
    echo "3) 🎭 Install Personas (Role Bundles)"
    echo "4) 📦 Manage Development Sandbox (Docker)"
    echo "5) 🌐 Setup Browser Automation"
    echo "6) 📚 Knowledge System (Save/Search)"
    echo "7) 🔍 Run Diagnostics"
    echo "8) 🚪 Exit"
    echo
    read -p "Option [1-8]: " choice

    case $choice in
        1)
            echo -e "\n${GREEN}>> Deploying Agent Army...${NC}"
            cd "$PROJECT_ROOT"
            ./deploy-agent-army.sh
            pause
            ;;
        2)
            echo -e "\n${GREEN}>> Installing Antigravity Skills...${NC}"
            cd "$PROJECT_ROOT"
            ./install-antigravity-skills.sh
            pause
            ;;
        3)
            echo -e "\n${GREEN}>> Managing Personas...${NC}"
            cd "$PROJECT_ROOT"
            ./install-personas.sh
            pause
            ;;
        4)
            echo -e "\n${GREEN}>> Development Sandbox Manager${NC}"
            echo "   1) Start Sandbox (Background)"
            echo "   2) SSH into Sandbox"
            echo "   3) Rebuild Sandbox"
            echo "   4) Stop Sandbox"
            read -p "   Action [1-4]: " sb_choice
            cd "$PROJECT_ROOT"
            case $sb_choice in
                1) ./scripts/sandbox-launcher.sh up ;;
                2) ./scripts/sandbox-launcher.sh ssh ;;
                3) ./scripts/sandbox-launcher.sh build ;;
                4) ./scripts/sandbox-launcher.sh down ;;
                *) echo "Invalid option" ;;
            esac
            pause
            ;;
        5)
            echo -e "\n${GREEN}>> Setting up Browser Automation...${NC}"
            cd "$PROJECT_ROOT"
            ./scripts/setup-browser-use.sh
            pause
            ;;
        6)
            echo -e "\n${GREEN}>> Knowledge System${NC}"
            echo "   1) Search Knowledge"
            echo "   2) Save Learning"
            read -p "   Action [1-2]: " kn_choice
            cd "$PROJECT_ROOT"
            case $kn_choice in
                1)
                    read -p "   Search Query: " query
                    python3 scripts/knowledge/search-knowledge.py "$query"
                    ;;
                2)
                    read -p "   Learning Note: " note
                    python3 scripts/knowledge/save-knowledge.py "$note"
                    ;;
            esac
            pause
            ;;
        7)
            echo -e "\n${GREEN}>> Running Diagnostics...${NC}"
            cd "$PROJECT_ROOT"
            # Assuming a diagnostic script exists or just checking basic things
            echo "Agents: $(ls agents/ | wc -l)"
            echo "Skills: $(ls skills/ | wc -l)"
            echo "Disk Usage: $(du -sh .)"
            pause
            ;;
        8)
            echo -e "\n${BLUE}Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "\n${RED}Invalid option.${NC}"
            pause
            ;;
    esac
done
