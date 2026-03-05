#!/bin/bash
# configure-persona.sh
# Interactive MCP configuration for Overpowers personas
#
# Features:
# - Select which MCPs to enable/disable
# - Configure API keys and environment variables
# - Risk warnings for filesystem/shell MCPs
# - Saves customized config to ~/.config/opencode/.mcp.json
#
# Usage: ./configure-persona.sh [persona-name]

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PERSONAS_DIR="$SCRIPT_DIR/personas"
TARGET_MCP="$HOME/.config/opencode/.mcp.json"
ENV_FILE="$HOME/.config/opencode/.mcp.env"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Risk levels for MCPs
declare -A MCP_RISK_LEVELS=(
    ["filesystem"]="HIGH"
    ["terminal"]="HIGH"
    ["github"]="MEDIUM"
    ["docker"]="MEDIUM"
    ["kubernetes"]="MEDIUM"
    ["mysql"]="MEDIUM"
    ["gateway"]="MEDIUM"
    ["browser"]="LOW"
    ["memory"]="LOW"
    ["serena"]="LOW"
    ["vibe-check"]="LOW"
    ["context7"]="LOW"
    ["deepwiki"]="LOW"
    ["mult-fetch"]="LOW"
    ["think-tank"]="LOW"
    ["hyperbrowser"]="LOW"
    ["grafana"]="LOW"
    ["redis"]="LOW"
)

# Required env vars per MCP
declare -A MCP_ENV_VARS=(
    ["context7"]="CONTEXT7_API_KEY"
    ["vibe-check"]="GEMINI_API_KEY"
    ["grafana"]="GRAFANA_URL,GRAFANA_API_KEY"
    ["github"]="GH_TOKEN"
)

# MCP descriptions
declare -A MCP_DESCRIPTIONS=(
    ["serena"]="Code analysis and symbol manipulation (safe)"
    ["vibe-check"]="AI behavior monitoring with Gemini"
    ["context7"]="Library documentation lookup"
    ["deepwiki"]="Remote documentation service"
    ["github"]="Full GitHub management (89 tools: issues, PRs, actions)"
    ["filesystem"]="⚠️ DIRECT filesystem read/write access"
    ["terminal"]="⚠️ Shell command execution (has audit logging)"
    ["docker"]="Docker container management"
    ["kubernetes"]="Kubernetes cluster operations"
    ["mysql"]="MySQL database connections"
    ["gateway"]="Universal database gateway"
    ["redis"]="Redis database operations"
    ["memory"]="ChromaDB vector memory"
    ["browser"]="Playwright browser automation"
    ["mult-fetch"]="Web page fetching"
    ["think-tank"]="Memory and reasoning"
    ["hyperbrowser"]="Remote browser automation"
    ["grafana"]="Grafana dashboards and alerts"
)

print_header() {
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC}     ${BOLD}🎭 Overpowers MCP Configuration Wizard${NC}                  ${CYAN}║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_risk_badge() {
    local risk=$1
    case $risk in
        "HIGH")
            echo -e "${RED}[HIGH RISK]${NC}"
            ;;
        "MEDIUM")
            echo -e "${YELLOW}[MEDIUM]${NC}"
            ;;
        "LOW")
            echo -e "${GREEN}[LOW]${NC}"
            ;;
        *)
            echo -e "${BLUE}[UNKNOWN]${NC}"
            ;;
    esac
}

ask_yes_no() {
    local prompt="$1"
    local default="${2:-y}"
    
    if [ "$default" = "y" ]; then
        prompt="$prompt [Y/n]: "
    else
        prompt="$prompt [y/N]: "
    fi
    
    read -p "$prompt" answer
    answer=${answer:-$default}
    
    case "${answer,,}" in
        y|yes) return 0 ;;
        *) return 1 ;;
    esac
}

ask_env_var() {
    local var_name="$1"
    local current_val="${!var_name:-}"
    
    if [ -n "$current_val" ]; then
        echo -e "  Current: ${CYAN}${current_val:0:10}...${NC}"
        if ask_yes_no "  Keep existing value?" "y"; then
            echo "$current_val"
            return
        fi
    fi
    
    read -p "  Enter $var_name: " new_val
    echo "$new_val"
}

configure_persona() {
    local persona=$1
    local source_file="$PERSONAS_DIR/$persona/mcp.json"
    
    if [ ! -f "$source_file" ]; then
        echo -e "${RED}❌ Persona not found: $persona${NC}"
        exit 1
    fi
    
    echo -e "\n${BOLD}📋 Configuring: $persona${NC}"
    echo -e "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    # Load env file if exists
    if [ -f "$ENV_FILE" ]; then
        source "$ENV_FILE"
    fi
    
    # Get list of MCPs
    local mcps=$(jq -r '.mcpServers | keys[]' "$source_file")
    
    # Build new config
    local new_config='{"mcpServers": {}}'
    local env_vars_to_save=""
    
    for mcp in $mcps; do
        local risk=${MCP_RISK_LEVELS[$mcp]:-"UNKNOWN"}
        local desc=${MCP_DESCRIPTIONS[$mcp]:-"No description"}
        local badge=$(print_risk_badge "$risk")
        
        echo -e "${BOLD}$mcp${NC} $badge"
        echo -e "  ${desc}"
        
        # Default based on risk
        local default_enable="y"
        if [ "$risk" = "HIGH" ]; then
            default_enable="n"
            echo -e "  ${YELLOW}⚠️  This MCP has elevated permissions. Recommended: disable unless needed.${NC}"
        fi
        
        if ask_yes_no "  Enable this MCP?" "$default_enable"; then
            # Get the MCP config
            local mcp_config=$(jq ".mcpServers[\"$mcp\"]" "$source_file")
            
            # Check for required env vars
            local required_vars=${MCP_ENV_VARS[$mcp]:-""}
            if [ -n "$required_vars" ]; then
                echo -e "\n  ${CYAN}Required environment variables:${NC}"
                IFS=',' read -ra vars <<< "$required_vars"
                for var in "${vars[@]}"; do
                    local val=$(ask_env_var "$var")
                    if [ -n "$val" ]; then
                        # Update environment in config
                        mcp_config=$(echo "$mcp_config" | jq ".environment[\"$var\"] = \"$val\"")
                        env_vars_to_save+="export $var=\"$val\"\n"
                    fi
                done
            fi
            
            # Add to new config with enabled=true
            mcp_config=$(echo "$mcp_config" | jq '.enabled = true')
            new_config=$(echo "$new_config" | jq ".mcpServers[\"$mcp\"] = $mcp_config")
            echo -e "  ${GREEN}✓ Enabled${NC}\n"
        else
            # Add to config but disabled
            local mcp_config=$(jq ".mcpServers[\"$mcp\"]" "$source_file")
            mcp_config=$(echo "$mcp_config" | jq '.enabled = false')
            new_config=$(echo "$new_config" | jq ".mcpServers[\"$mcp\"] = $mcp_config")
            echo -e "  ${RED}✗ Disabled${NC}\n"
        fi
    done
    
    # Summary
    echo -e "\n${BOLD}📊 Configuration Summary${NC}"
    echo -e "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    local enabled_count=$(echo "$new_config" | jq '[.mcpServers[] | select(.enabled == true)] | length')
    local disabled_count=$(echo "$new_config" | jq '[.mcpServers[] | select(.enabled == false)] | length')
    
    echo -e "  Enabled:  ${GREEN}$enabled_count${NC}"
    echo -e "  Disabled: ${RED}$disabled_count${NC}"
    echo ""
    
    echo "Enabled MCPs:"
    echo "$new_config" | jq -r '.mcpServers | to_entries[] | select(.value.enabled == true) | "  ✅ " + .key'
    
    echo ""
    echo "Disabled MCPs:"
    echo "$new_config" | jq -r '.mcpServers | to_entries[] | select(.value.enabled == false) | "  ❌ " + .key'
    
    echo ""
    
    if ask_yes_no "Save this configuration?" "y"; then
        # Backup existing
        if [ -f "$TARGET_MCP" ]; then
            cp "$TARGET_MCP" "$TARGET_MCP.bak.$(date +%Y%m%d%H%M%S)"
        fi
        
        # Save config
        echo "$new_config" | jq '.' > "$TARGET_MCP"
        echo -e "${GREEN}✅ Saved to $TARGET_MCP${NC}"
        
        # Save env vars
        if [ -n "$env_vars_to_save" ]; then
            echo -e "$env_vars_to_save" > "$ENV_FILE"
            echo -e "${GREEN}✅ Environment variables saved to $ENV_FILE${NC}"
            echo -e "${YELLOW}💡 Add 'source $ENV_FILE' to your shell profile${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️ Configuration not saved${NC}"
    fi
}

# Main
print_header

# List personas if no argument
if [ -z "$1" ]; then
    echo "Available personas:"
    echo ""
    for dir in "$PERSONAS_DIR"/*/; do
        name=$(basename "$dir")
        mcp_count=$(jq '.mcpServers | length' "$dir/mcp.json" 2>/dev/null || echo "?")
        desc=$(head -3 "$dir/README.md" 2>/dev/null | tail -1 || echo "")
        echo -e "  ${BOLD}$name${NC} ($mcp_count MCPs)"
        echo -e "    $desc"
        echo ""
    done
    
    read -p "Select a persona to configure: " persona
    if [ -z "$persona" ]; then
        echo "No persona selected. Exiting."
        exit 0
    fi
else
    persona="$1"
fi

configure_persona "$persona"

echo ""
echo -e "${CYAN}🚀 Configuration complete!${NC}"
echo -e "   Restart your MCP client to apply changes."
