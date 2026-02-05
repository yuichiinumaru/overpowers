#!/bin/bash
# install-personas.sh
# Install a persona bundle to ~/.config/opencode/
#
# Usage: ./install-personas.sh <persona-name>
#        ./install-personas.sh --all   # Merge all personas
# Example: ./install-personas.sh devops-engineer

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PERSONAS_DIR="$SCRIPT_DIR/personas"
TARGET_MCP="$HOME/.config/opencode/.mcp.json"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo "🎭 overpowers Persona Installer"
echo "================================"

# Handle --all flag
if [ "$1" = "--all" ]; then
    echo ""
    echo -e "${CYAN}🔥 Merging ALL personas into one super-config...${NC}"
    echo ""
    
    # Backup existing
    if [ -f "$TARGET_MCP" ]; then
        BACKUP="$TARGET_MCP.bak.$(date +%Y%m%d%H%M%S)"
        cp "$TARGET_MCP" "$BACKUP"
        echo -e "${YELLOW}📦 Backed up existing config to: $(basename $BACKUP)${NC}"
    fi
    
    # Start with empty mcpServers
    MERGED='{"mcpServers":{}}'
    
    # Merge all persona mcp.json files
    for dir in "$PERSONAS_DIR"/*/; do
        name=$(basename "$dir")
        if [ -f "$dir/mcp.json" ]; then
            echo "  ⊕ Merging: $name"
            MERGED=$(echo "$MERGED" | jq --slurpfile new "$dir/mcp.json" '.mcpServers += $new[0].mcpServers')
        fi
    done
    
    # Write merged config
    echo "$MERGED" | jq '.' > "$TARGET_MCP"
    
    # Count unique MCPs
    MCP_COUNT=$(jq -r '.mcpServers | keys | length' "$TARGET_MCP")
    
    echo ""
    echo -e "${GREEN}✅ Merged all personas! Total MCPs: $MCP_COUNT${NC}"
    echo ""
    echo "📋 MCPs configured:"
    jq -r '.mcpServers | keys[]' "$TARGET_MCP" | sort | while read mcp; do
        echo "  • $mcp"
    done
    echo ""
    echo -e "${YELLOW}⚠️  Remember to configure API keys for MCPs that require them!${NC}"
    echo "   Run: ./configure-persona.sh --check"
    exit 0
fi

# List available personas if no argument
if [ -z "$1" ]; then
    echo ""
    echo "Available personas:"
    echo ""
    for dir in "$PERSONAS_DIR"/*/; do
        name=$(basename "$dir")
        agents=$(grep -c "^\-" "$dir/README.md" 2>/dev/null || echo "?")
        desc=$(head -3 "$dir/README.md" | tail -1)
        echo "  📋 $name"
        echo "     $desc"
        echo ""
    done
    echo ""
    echo "Usage: $0 <persona-name>"
    echo "       $0 --all   # Merge ALL personas into one config"
    exit 0
fi

PERSONA=$1
SOURCE_DIR="$PERSONAS_DIR/$PERSONA"

# Check if persona exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}❌ Persona not found: $PERSONA${NC}"
    echo ""
    echo "Available personas:"
    ls -1 "$PERSONAS_DIR"
    exit 1
fi

# Backup existing
if [ -f "$TARGET_MCP" ]; then
    BACKUP="$TARGET_MCP.bak.$(date +%Y%m%d%H%M%S)"
    cp "$TARGET_MCP" "$BACKUP"
    echo -e "${YELLOW}📦 Backed up existing config to: $(basename $BACKUP)${NC}"
fi

# Install
cp "$SOURCE_DIR/mcp.json" "$TARGET_MCP"
echo -e "${GREEN}✅ Installed persona: $PERSONA${NC}"

# Show configured MCPs
echo ""
echo "📋 MCPs configured:"
jq -r '.mcpServers | keys[]' "$TARGET_MCP" | while read mcp; do
    note=$(jq -r ".mcpServers[\"$mcp\"].note // empty" "$TARGET_MCP")
    if [ -n "$note" ]; then
        echo "  • $mcp ($note)"
    else
        echo "  • $mcp"
    fi
done

echo ""
echo "💡 To switch personas, run:"
echo "   $0 <another-persona>"
echo ""
echo "🚀 You can also use HyperTool:"
echo "   npx -y @toolprint/hypertool-mcp mcp run --persona $PERSONA"
