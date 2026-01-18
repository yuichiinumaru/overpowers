#!/bin/bash
# ============================================================================
# Overpowers Skills Installer for Google Antigravity
# ============================================================================
# Installs curated skills from the Overpowers toolkit into Antigravity
# Compatible with Linux, macOS, and Windows (via Git Bash/WSL)
# ============================================================================

set -e

VERSION="1.0.0"
REPO_URL="https://github.com/yuichiinumaru/overpowers"
TEMP_DIR="/tmp/overpowers-installer-$$"

# Colors (works on most terminals)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Language (set by user)
LANG_CODE="en"

# ============================================================================
# Internationalization (i18n)
# ============================================================================

# English strings
declare -A EN=(
    ["detected_os"]="Detected OS"
    ["enter_username"]="Enter your username (or press Enter for"
    ["username"]="Username"
    ["default_path"]="Default Antigravity skills path"
    ["enter_custom_path"]="Enter custom path (or press Enter for default)"
    ["creating_dir"]="Creating directory"
    ["install_path"]="Install path"
    ["searching_local"]="Searching for local Overpowers installations..."
    ["found_local"]="Found local Overpowers at"
    ["local_detected"]="Local installation detected."
    ["use_local"]="Use local Overpowers instead of downloading? [Y/n]"
    ["using_local"]="Using local source"
    ["downloading"]="Downloading Overpowers toolkit from GitHub..."
    ["download_complete"]="Download complete"
    ["no_source"]="No source available (Git failed and no local copy selected)."
    ["select_profile"]="Select installation profile:"
    ["essential"]="Essential (6 skills) - Core development skills"
    ["productivity"]="Productivity (5 skills) - Research & documentation"
    ["advanced"]="Advanced Agents (5 skills) - Multi-agent orchestration"
    ["developer"]="Full Developer (5 skills) - Language-specific skills"
    ["all_curated"]="All curated (21 skills)"
    ["workflows_only"]="Workflows only (16 workflows)"
    ["custom"]="Custom selection"
    ["nuclear"]="NUCLEAR MODE - Install EVERYTHING (500+ skills, agents, workflows)"
    ["enter_choice"]="Enter choice [1-8]"
    ["installing"]="Installing"
    ["skills"]="skills"
    ["installed"]="Installed"
    ["not_found"]="not found in repo"
    ["already_exists"]="already exists, skipping..."
    ["cleaning"]="Cleaning up..."
    ["done"]="Done!"
    ["complete"]="Installation Complete!"
    ["skills_installed_to"]="Skills installed to"
    ["available_skills"]="Available skills"
    ["open_antigravity"]="Open Antigravity and start using your new skills!"
    ["nuclear_activated"]="NUCLEAR MODE ACTIVATED"
    ["nuclear_warning"]="WARNING: This will install EVERYTHING:"
    ["existing_skills"]="existing skills"
    ["converted_agents"]="agents converted to skills"
    ["workflows"]="workflows"
    ["nuclear_confirm"]="ARE YOU SURE ABOUT THIS, BUDDY? WHOA!"
    ["type_confirm"]="Type 'YES I WANT' to continue"
    ["confirm_phrase"]="YES I WANT"
    ["cancelled"]="Operation cancelled. Phew!"
    ["starting_nuclear"]="Starting NUCLEAR installation..."
    ["installing_all_skills"]="Installing ALL skills..."
    ["skills_installed"]="Skills installed"
    ["converting_agents"]="Converting agents to skills..."
    ["agents_converted"]="Agents converted"
    ["installing_workflows"]="Installing workflows..."
    ["workflows_installed"]="Workflows installed"
    ["nuclear_complete"]="NUCLEAR INSTALLATION COMPLETE!"
    ["invalid_choice"]="Invalid choice"
)

# Portuguese (Brazil) strings
declare -A PTBR=(
    ["detected_os"]="Sistema detectado"
    ["enter_username"]="Digite seu usuário (ou Enter para"
    ["username"]="Usuário"
    ["default_path"]="Caminho padrão do Antigravity"
    ["enter_custom_path"]="Digite caminho customizado (ou Enter para padrão)"
    ["creating_dir"]="Criando diretório"
    ["install_path"]="Caminho de instalação"
    ["searching_local"]="Buscando instalações locais do Overpowers..."
    ["found_local"]="Overpowers encontrado em"
    ["local_detected"]="Instalação local detectada."
    ["use_local"]="Usar Overpowers local ao invés de baixar? [S/n]"
    ["using_local"]="Usando fonte local"
    ["downloading"]="Baixando Overpowers do GitHub..."
    ["download_complete"]="Download completo"
    ["no_source"]="Nenhuma fonte disponível (Git falhou e cópia local não selecionada)."
    ["select_profile"]="Selecione o perfil de instalação:"
    ["essential"]="Essencial (6 skills) - Skills de desenvolvimento core"
    ["productivity"]="Produtividade (5 skills) - Pesquisa & documentação"
    ["advanced"]="Agentes Avançados (5 skills) - Orquestração multi-agente"
    ["developer"]="Desenvolvedor Full (5 skills) - Skills específicas por linguagem"
    ["all_curated"]="Todas curadas (21 skills)"
    ["workflows_only"]="Apenas workflows (16 workflows)"
    ["custom"]="Seleção customizada"
    ["nuclear"]="MODO NUCLEAR - Instalar TUDO (500+ skills, agentes, workflows)"
    ["enter_choice"]="Digite sua escolha [1-8]"
    ["installing"]="Instalando"
    ["skills"]="skills"
    ["installed"]="Instalado"
    ["not_found"]="não encontrado no repo"
    ["already_exists"]="já existe, pulando..."
    ["cleaning"]="Limpando..."
    ["done"]="Pronto!"
    ["complete"]="Instalação Completa!"
    ["skills_installed_to"]="Skills instaladas em"
    ["available_skills"]="Skills disponíveis"
    ["open_antigravity"]="Abra o Antigravity e comece a usar suas novas skills!"
    ["nuclear_activated"]="MODO NUCLEAR ATIVADO"
    ["nuclear_warning"]="ATENÇÃO: Isso vai instalar TUDO:"
    ["existing_skills"]="skills existentes"
    ["converted_agents"]="agentes convertidos para skills"
    ["workflows"]="workflows"
    ["nuclear_confirm"]="TEM CERTEZA DISSO, BICHO? OLOKO!"
    ["type_confirm"]="Digite 'SIM EU QUERO' para continuar"
    ["confirm_phrase"]="SIM EU QUERO"
    ["cancelled"]="Operação cancelada. Ufa!"
    ["starting_nuclear"]="Iniciando instalação NUCLEAR..."
    ["installing_all_skills"]="Instalando TODAS as skills..."
    ["skills_installed"]="Skills instaladas"
    ["converting_agents"]="Convertendo agentes para skills..."
    ["agents_converted"]="Agentes convertidos"
    ["installing_workflows"]="Instalando workflows..."
    ["workflows_installed"]="Workflows instalados"
    ["nuclear_complete"]="INSTALAÇÃO NUCLEAR COMPLETA!"
    ["invalid_choice"]="Escolha inválida"
)

# Get translated string
t() {
    local key="$1"
    if [ "$LANG_CODE" = "pt" ]; then
        echo "${PTBR[$key]}"
    else
        echo "${EN[$key]}"
    fi
}

select_language() {
    echo ""
    echo -e "${CYAN}🌐 Select language / Selecione o idioma:${NC}"
    echo ""
    echo "  1) 🇺🇸 English"
    echo "  2) 🇧🇷 Português (Brasil)"
    echo ""
    echo -n "Choice / Escolha [1-2]: "
    read lang_choice
    
    case "$lang_choice" in
        2) LANG_CODE="pt" ;;
        *) LANG_CODE="en" ;;
    esac
}

# Selected skills to install (curated best-of)
CORE_SKILLS=(
    "subagent-orchestration"
    "code-review"
    "code-refactoring"
    "test-driven-development"
    "systematic-debugging"
    "verification-quality"
)

PRODUCTIVITY_SKILLS=(
    "brainstorming"
    "changelog-generator"
    "codebase-documenter"
    "technical-doc-creator"
    "web-research"
)

ADVANCED_SKILLS=(
    "dispatching-parallel-agents"
    "ensemble-solving"
    "swarm-orchestration"
    "flow-nexus-swarm"
    "v3-swarm-coordination"
)

DEV_SKILLS=(
    "backend-development"
    "database-design"
    "python-development"
    "javascript-typescript"
    "react-best-practices"
)

# ============================================================================
# Helper Functions
# ============================================================================

print_banner() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                                                                   ║"
    echo "║   ⚡ OVERPOWERS Skills Installer for Antigravity v${VERSION}        ║"
    echo "║                                                                   ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_step() {
    echo -e "${BLUE}▶${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

detect_os() {
    case "$(uname -s)" in
        Linux*)     OS="linux";;
        Darwin*)    OS="macos";;
        CYGWIN*|MINGW*|MSYS*) OS="windows";;
        *)          OS="unknown";;
    esac
    echo $OS
}

get_default_install_path() {
    local os=$(detect_os)
    local user="${USER:-$USERNAME}"
    
    case "$os" in
        linux|macos)
            echo "/home/$user/.gemini/antigravity/skills"
            ;;
        windows)
            # Try common Windows paths
            if [ -n "$USERPROFILE" ]; then
                echo "$USERPROFILE/.gemini/antigravity/skills"
            else
                echo "/c/Users/$user/.gemini/antigravity/skills"
            fi
            ;;
        *)
            echo "$HOME/.gemini/antigravity/skills"
            ;;
    esac
}

# ============================================================================
# Main Installation Logic
# ============================================================================

install_skills() {
    local install_path="$1"
    local skills=("${@:2}")
    local installed=0
    local failed=0
    
    for skill in "${skills[@]}"; do
        local source_path="$TEMP_DIR/overpowers/skills/$skill"
        local dest_path="$install_path/$skill"
        
        if [ -d "$source_path" ]; then
            if [ -d "$dest_path" ]; then
                print_warning "Skill '$skill' already exists, skipping..."
            else
                cp -r "$source_path" "$dest_path"
                print_success "Installed: $skill"
                ((installed++))
            fi
        else
            print_warning "Skill '$skill' not found in repo"
            ((failed++))
        fi
    done
    
    echo ""
    print_success "Installed $installed skills"
    if [ $failed -gt 0 ]; then
        print_warning "$failed skills not found"
    fi
}

# ============================================================================
# Interactive Menu
# ============================================================================

show_menu() {
    echo ""
    echo -e "${CYAN}$(t select_profile)${NC}"
    echo ""
    echo "  1) 🚀 $(t essential)"
    echo "  2) 📚 $(t productivity)"
    echo "  3) 🤖 $(t advanced)"
    echo "  4) 💻 $(t developer)"
    echo "  5) ⭐ $(t all_curated)"
    echo "  6) 📋 $(t workflows_only)"
    echo "  7) 🎯 $(t custom)"
    echo ""
    echo -e "  ${RED}8) ☢️  $(t nuclear)${NC}"
    echo ""
    echo -n "$(t enter_choice): "
}

# ============================================================================
# Main Script
# ============================================================================

main() {
    print_banner
    
    # Select language first
    select_language
    
    # Detect OS
    local os=$(detect_os)
    print_step "$(t detected_os): $os"
    
    # Get username
    echo ""
    echo -n "$(t enter_username) '${USER:-$USERNAME}'): "
    read input_user
    local username="${input_user:-${USER:-$USERNAME}}"
    print_success "$(t username): $username"
    
    # Get install path
    local default_path=$(get_default_install_path)
    default_path="${default_path/\$user/$username}"
    
    echo ""
    echo "$(t default_path): $default_path"
    echo -n "$(t enter_custom_path): "
    read input_path
    local install_path="${input_path:-$default_path}"
    
    # Create directory if needed
    if [ ! -d "$install_path" ]; then
        print_step "$(t creating_dir): $install_path"
        mkdir -p "$install_path"
    fi
    print_success "$(t install_path): $install_path"

    # --- Local Detection ---
    echo ""
    print_step "$(t searching_local)"
    
    LOCAL_PATHS=(
        "/home/$username/.config/opencode/Overpowers"
        "/home/$username/.claude/Overpowers"
        "/home/$username/Overpowers"
        "$(pwd)"
    )
    
    FOUND_LOCAL=""
    for path in "${LOCAL_PATHS[@]}"; do
        if [ -d "$path/skills" ]; then
            FOUND_LOCAL="$path"
            print_success "$(t found_local): $FOUND_LOCAL"
            break
        fi
    done

    # --- Source Selection ---
    mkdir -p "$TEMP_DIR"
    SOURCE_READY=false

    if [ -n "$FOUND_LOCAL" ]; then
        echo ""
        echo -e "${CYAN}$(t local_detected)${NC}"
        echo -n "$(t use_local): "
        read use_local
        if [[ "$use_local" =~ ^[Nn]$ ]]; then
            echo "Skipping local, will download..."
        else
            cp -r "$FOUND_LOCAL" "$TEMP_DIR/overpowers"
            SOURCE_READY=true
            print_success "$(t using_local)"
        fi
    fi

    if [ "$SOURCE_READY" = false ]; then
        echo ""
        print_step "$(t downloading)"
        if command -v git &> /dev/null; then
            if git clone --depth 1 "$REPO_URL" "$TEMP_DIR/overpowers" 2>/dev/null; then
                SOURCE_READY=true
                print_success "$(t download_complete)"
            fi
        fi
    fi

    if [ "$SOURCE_READY" = false ]; then
        print_error "$(t no_source)"
        exit 1
    fi
    
    # Show menu
    show_menu
    read choice
    
    # Install based on choice
    echo ""
    case "$choice" in
        1)
            print_step "Installing Essential skills..."
            install_skills "$install_path" "${CORE_SKILLS[@]}"
            ;;
        2)
            print_step "Installing Productivity skills..."
            install_skills "$install_path" "${PRODUCTIVITY_SKILLS[@]}"
            ;;
        3)
            print_step "Installing Advanced Agent skills..."
            install_skills "$install_path" "${ADVANCED_SKILLS[@]}"
            ;;
        4)
            print_step "Installing Developer skills..."
            install_skills "$install_path" "${DEV_SKILLS[@]}"
            ;;
        5)
            print_step "Installing ALL curated skills..."
            install_skills "$install_path" "${CORE_SKILLS[@]}"
            install_skills "$install_path" "${PRODUCTIVITY_SKILLS[@]}"
            install_skills "$install_path" "${ADVANCED_SKILLS[@]}"
            install_skills "$install_path" "${DEV_SKILLS[@]}"
            ;;
        6)
            # Workflows only
            print_step "Installing workflows..."
            local workflow_src="$TEMP_DIR/overpowers/workflows"
            local workflow_dest="$install_path/../workflows"
            mkdir -p "$workflow_dest"
            if [ -d "$workflow_src" ]; then
                cp -r "$workflow_src"/*.md "$workflow_dest/" 2>/dev/null || true
                print_success "Workflows installed to: $workflow_dest"
                ls -1 "$workflow_dest" 2>/dev/null | head -10
            else
                print_warning "No workflows found in source"
            fi
            ;;
        7)
            # Custom selection
            echo ""
            echo "Available skills:"
            ls -1 "$TEMP_DIR/overpowers/skills" 2>/dev/null | head -30
            echo "..."
            echo ""
            echo "Enter skill names separated by spaces:"
            read -a custom_skills
            install_skills "$install_path" "${custom_skills[@]}"
            ;;
        8)
            # NUCLEAR MODE
            echo ""
            echo -e "${RED}╔═══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${RED}║  ☢️  $(t nuclear_activated)                                       ║${NC}"
            echo -e "${RED}╚═══════════════════════════════════════════════════════════════════╝${NC}"
            echo ""
            echo -e "${YELLOW}⚠️  $(t nuclear_warning)${NC}"
            echo "   - 146+ $(t existing_skills)"
            echo "   - 392 $(t converted_agents)"
            echo "   - 16 $(t workflows)"
            echo ""
            echo -e "${RED}$(t nuclear_confirm) 🔥${NC}"
            echo ""
            echo -n "$(t type_confirm): "
            read confirm
            
            if [ "$confirm" != "$(t confirm_phrase)" ]; then
                print_warning "$(t cancelled) 😅"
                exit 0
            fi
            
            echo ""
            print_step "☢️ $(t starting_nuclear)"
            
            # 1. Install ALL existing skills
            print_step "$(t installing_all_skills)"
            for skill_dir in "$TEMP_DIR/overpowers/skills"/*/; do
                if [ -d "$skill_dir" ]; then
                    skill_name=$(basename "$skill_dir")
                    dest_path="$install_path/$skill_name"
                    if [ ! -d "$dest_path" ]; then
                        cp -r "$skill_dir" "$dest_path"
                    fi
                fi
            done
            skills_count=$(ls -1d "$install_path"/*/ 2>/dev/null | wc -l)
            print_success "$(t skills_installed): $skills_count"
            
            # 2. Convert and install agents
            print_step "$(t converting_agents)"
            local agents_dir="$TEMP_DIR/overpowers/agents"
            if [ -d "$agents_dir" ]; then
                for agent_file in "$agents_dir"/*.md; do
                    if [ -f "$agent_file" ]; then
                        agent_name=$(basename "$agent_file" .md)
                        skill_dest="$install_path/agent-$agent_name"
                        if [ ! -d "$skill_dest" ]; then
                            mkdir -p "$skill_dest"
                            # Create simple SKILL.md from agent
                            {
                                echo "---"
                                echo "name: agent-$agent_name"
                                echo "description: Agent converted from $agent_name"
                                echo "---"
                                echo ""
                                cat "$agent_file"
                            } > "$skill_dest/SKILL.md"
                        fi
                    fi
                done
            fi
            agents_count=$(ls -1d "$install_path"/agent-*/ 2>/dev/null | wc -l)
            print_success "$(t agents_converted): $agents_count"
            
            # 3. Install workflows
            print_step "$(t installing_workflows)"
            local workflow_src="$TEMP_DIR/overpowers/workflows"
            local workflow_dest="$install_path/../workflows"
            mkdir -p "$workflow_dest"
            if [ -d "$workflow_src" ]; then
                cp -r "$workflow_src"/*.md "$workflow_dest/" 2>/dev/null || true
            fi
            wf_count=$(ls -1 "$workflow_dest"/*.md 2>/dev/null | wc -l)
            print_success "$(t workflows_installed): $wf_count"
            
            echo ""
            echo -e "${GREEN}☢️ $(t nuclear_complete)${NC}"
            echo "   Skills: $skills_count"
            echo "   $(t agents_converted): $agents_count"
            echo "   Workflows: $wf_count"
            ;;
        *)
            print_error "$(t invalid_choice)"
            exit 1
            ;;
    esac
    
    # Cleanup
    print_step "$(t cleaning)"
    rm -rf "$TEMP_DIR"
    print_success "$(t done)"

    
    # Summary
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  ✅ $(t complete)                                              ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "$(t skills_installed_to): $install_path"
    echo ""
    echo "$(t available_skills):"
    ls -1 "$install_path" 2>/dev/null | head -10
    [ $(ls -1 "$install_path" 2>/dev/null | wc -l) -gt 10 ] && echo "..."
    echo ""
    echo -e "${CYAN}$(t open_antigravity)${NC}"
}

# Run main
main "$@"
