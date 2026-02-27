#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
# OpenCode Agent Model Fallback Chain Manager
# ═══════════════════════════════════════════════════════════════════════════
# 
# Este script implementa cadeia de fallback de modelos baseado na pesquisa:
# - SWE-bench: Claude Opus (80.9%) > Gemini Flash (78%) > Sonnet (77.2%) > GLM-4.7 (73.8%)
# - Terminal-Bench: Opus (59.3%) > Gemini Flash (54.2%) > Sonnet (42.8%)
# - τ²-Bench (Tool Use): Gemini Pro (90.7%) > GLM-4.7 (87.4%) > Sonnet (87.2%)
#
# Uso: ./update_models_with_fallback.sh [--apply]
#   Sem --apply: apenas mostra as mudanças
#   Com --apply: aplica as mudanças nos arquivos
#
# ═══════════════════════════════════════════════════════════════════════════

set -euo pipefail

AGENTS_DIR="/home/sephiroth/.config/opencode/agents"
DRY_RUN=true

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --apply) DRY_RUN=false; shift ;;
        *) shift ;;
    esac
done

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Model definitions (provider/model-id format)
# Premium models (Antigravity)
M_OPUS="google/antigravity-claude-opus-4-5-thinking"
M_SONNET="opencode/kimi-k2.5"
M_GEMINI_PRO="google/antigravity-gemini-3-pro"
M_GEMINI_FLASH="google/antigravity-gemini-3-flash"

# Free models (OpenCode Zen)
M_GROK_CODE="opencode/grok-code-fast-1"
M_GLM="opencode/glm-4.7"
M_PICKLE="opencode/big-pickle"
M_MINIMAX="opencode/minimax-m2.1"
M_GROK_FAST="opencode/grok-4.1-fast"

# ═══════════════════════════════════════════════════════════════════════════
# FALLBACK CHAINS BY TASK CATEGORY
# ═══════════════════════════════════════════════════════════════════════════
# Format: "primary|fallback1|fallback2|fallback3"
# Based on model research benchmarks and task characteristics

# Tier 1: Critical/Review - Precision > Speed (SWE-bench priority)
CHAIN_CRITICAL="${M_OPUS}|${M_SONNET}|${M_GEMINI_FLASH}|${M_GLM}"

# Tier 2: Architecture/Planning - Reasoning + Creativity (Gemini Pro multimodal)
CHAIN_ARCHITECTURE="${M_GEMINI_PRO}|${M_OPUS}|${M_SONNET}|${M_GEMINI_FLASH}"

# Tier 3: General Coding - Balance speed/quality (Sonnet sweet spot)
CHAIN_CODING="${M_SONNET}|${M_GEMINI_FLASH}|${M_GLM}|${M_PICKLE}"

# Tier 4: Performance/Debug - Speed + iteration (Gemini Flash 3x faster)
CHAIN_PERFORMANCE="${M_GEMINI_FLASH}|${M_SONNET}|${M_GLM}|${M_GROK_CODE}"

# Tier 5: Tool-Heavy Tasks - Tool use priority (τ²-Bench)
CHAIN_TOOLING="${M_GLM}|${M_GEMINI_FLASH}|${M_PICKLE}|${M_GROK_CODE}"

# Tier 6: CLI/Terminal - Terminal-Bench priority
CHAIN_CLI="${M_OPUS}|${M_GEMINI_FLASH}|${M_GROK_CODE}|${M_GLM}"

# Tier 7: Frontend/UI - Visual + speed (vibe coding)
CHAIN_FRONTEND="${M_GEMINI_FLASH}|${M_GLM}|${M_SONNET}|${M_GROK_CODE}"

# Tier 8: Documentation - Accuracy + verbosity
CHAIN_DOCS="${M_SONNET}|${M_GEMINI_FLASH}|${M_OPUS}|${M_GLM}"

# Tier 9: Free tier (cost optimization)
CHAIN_FREE="${M_GLM}|${M_PICKLE}|${M_GROK_CODE}|${M_MINIMAX}"

# ═══════════════════════════════════════════════════════════════════════════
# AGENT TO CHAIN MAPPING
# ═══════════════════════════════════════════════════════════════════════════

declare -A AGENT_CHAINS

# CRITICAL (Code Review, Security, Compliance)
for agent in code_reviewer code_quality_reviewer security_auditor security_code_reviewer \
             compliance_auditor risk_manager penetration_tester incident_responder \
             pr_readiness_reviewer test_coverage_reviewer performance-reviewer; do
    AGENT_CHAINS["$agent"]="CRITICAL"
done

# ARCHITECTURE (Planning, Design, Research)
for agent in architect_reviewer cloud_architect microservices_architect platform_engineer \
             llm_architect ai_engineer business_analyst product_manager research_analyst \
             ux_researcher trend_analyst competitive_analyst market_researcher \
             workflow_orchestrator multi_agent_coordinator prompt-engineer; do
    AGENT_CHAINS["$agent"]="ARCHITECTURE"
done

# CODING (General Development)
for agent in python_pro java_architect kotlin_specialist spring_boot_engineer \
             csharp_developer dotnet_core_expert dotnet_framework_4_8_expert \
             backend_developer fullstack_developer api_designer graphql_architect \
             django_developer mobile_developer mobile_app_developer flutter_expert \
             swift_expert database_administrator database_optimizer postgres_pro sql_pro \
             websocket-engineer; do
    AGENT_CHAINS["$agent"]="CODING"
done

# PERFORMANCE (Debug, Optimization, ML)
for agent in performance_engineer performance_monitor chaos_engineer sre_engineer \
             rust_engineer cpp_pro golang_pro embedded_systems debugger error_detective \
             error_coordinator machine_learning_engineer ml_engineer mlops_engineer \
             data_scientist nlp_engineer scrum_master project-manager; do
    AGENT_CHAINS["$agent"]="PERFORMANCE"
done

# TOOLING (API Integration, MCP, Data Pipelines)
for agent in mcp_developer data_engineer dependency_manager legacy_modernizer \
             refactoring_specialist context_manager kubernetes_specialist terraform-engineer; do
    AGENT_CHAINS["$agent"]="TOOLING"
done

# CLI (Terminal, DevOps, Build)
for agent in devops_engineer devops_incident_responder deployment_engineer build_engineer \
             cli_developer qa_expert test_automator git-workflow-manager; do
    AGENT_CHAINS["$agent"]="CLI"
done

# FRONTEND (UI, JS/TS, Accessibility)
for agent in frontend_developer react_specialist vue_expert angular_architect nextjs_developer \
             javascript_pro typescript_pro electron_pro ui_designer accessibility_tester \
             search_specialist seo-specialist; do
    AGENT_CHAINS["$agent"]="FRONTEND"
done

# DOCUMENTATION (Technical Writing)
for agent in technical_writer documentation_engineer api_documenter release_notes_writer \
             knowledge_synthesizer git_summarizer test_plan_writer todo_fixme_scanner \
             documentation_accuracy_reviewer content-marketer; do
    AGENT_CHAINS["$agent"]="DOCS"
done

# FREE (Cost Optimization - PHP, Ruby, Misc)
for agent in php_pro laravel_specialist wordpress_master rails_expert \
             blockchain_developer game_developer iot_engineer network_engineer \
             fintech_engineer payment_integration quant_analyst \
             customer_success_manager sales_engineer legal_advisor \
             task_distributor agent_organizer tooling_engineer dx_optimizer \
             data_analyst data-researcher; do
    AGENT_CHAINS["$agent"]="FREE"
done

# ═══════════════════════════════════════════════════════════════════════════
# FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

get_chain() {
    local category="$1"
    case "$category" in
        CRITICAL)      echo "$CHAIN_CRITICAL" ;;
        ARCHITECTURE)  echo "$CHAIN_ARCHITECTURE" ;;
        CODING)        echo "$CHAIN_CODING" ;;
        PERFORMANCE)   echo "$CHAIN_PERFORMANCE" ;;
        TOOLING)       echo "$CHAIN_TOOLING" ;;
        CLI)           echo "$CHAIN_CLI" ;;
        FRONTEND)      echo "$CHAIN_FRONTEND" ;;
        DOCS)          echo "$CHAIN_DOCS" ;;
        FREE)          echo "$CHAIN_FREE" ;;
        *)             echo "$CHAIN_CODING" ;;  # Default
    esac
}

get_primary_model() {
    local chain="$1"
    echo "$chain" | cut -d'|' -f1
}

get_fallback_list() {
    local chain="$1"
    echo "$chain" | cut -d'|' -f2-
}

get_color_for_category() {
    local category="$1"
    case "$category" in
        CRITICAL)      echo "$RED" ;;
        ARCHITECTURE)  echo "$MAGENTA" ;;
        CODING)        echo "$GREEN" ;;
        PERFORMANCE)   echo "$CYAN" ;;
        TOOLING)       echo "$YELLOW" ;;
        CLI)           echo "$BLUE" ;;
        FRONTEND)      echo "$GREEN" ;;
        DOCS)          echo "$NC" ;;
        FREE)          echo "$YELLOW" ;;
        *)             echo "$NC" ;;
    esac
}

update_agent() {
    local file="$1"
    local chain="$2"
    local category="$3"
    
    local primary=$(get_primary_model "$chain")
    local fallbacks=$(get_fallback_list "$chain")
    local color=$(get_color_for_category "$category")
    local basename=$(basename "$file" .md)
    
    # Extract just the model name for display
    local primary_short=$(echo "$primary" | sed 's#.*/##')
    
    if [[ "$DRY_RUN" == "true" ]]; then
        printf "  ${color}%-35s${NC} → %-25s [%s]\n" "$basename" "$primary_short" "$category"
    else
        # Update model field (using # as delimiter to avoid issues with /)
        sed -i "s#^model:.*#model: $primary#" "$file"
        
        # Add or update model_fallback field (for documentation)
        if grep -q "^model_fallback:" "$file"; then
            sed -i "s#^model_fallback:.*#model_fallback: \"$fallbacks\"#" "$file"
        else
            # Insert after model: line
            sed -i "/^model:/a model_fallback: \"$fallbacks\"" "$file"
        fi
        
        # Add or update category field
        if grep -q "^category:" "$file"; then
            sed -i "s#^category:.*#category: $category#" "$file"
        else
            sed -i "/^model_fallback:/a category: $category" "$file"
        fi
        
        printf "  ${GREEN}✓${NC} ${color}%-35s${NC} → %-25s [%s]\n" "$basename" "$primary_short" "$category"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

cd "$AGENTS_DIR" || exit 1

echo ""
echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║     OpenCode Agent Model Fallback Chain Manager                        ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

if [[ "$DRY_RUN" == "true" ]]; then
    echo -e "${YELLOW}[DRY RUN]${NC} Mostrando mudanças. Use --apply para aplicar."
    echo ""
fi

# Process by category for organized output
for category in CRITICAL ARCHITECTURE CODING PERFORMANCE TOOLING CLI FRONTEND DOCS FREE; do
    color=$(get_color_for_category "$category")
    chain=$(get_chain "$category")
    primary_short=$(get_primary_model "$chain" | sed 's|.*/||')
    
    echo -e "${color}═══════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${color}  $category${NC} (Primary: $primary_short)"
    echo -e "${color}═══════════════════════════════════════════════════════════════════════════${NC}"
    
    for agent in "${!AGENT_CHAINS[@]}"; do
        if [[ "${AGENT_CHAINS[$agent]}" == "$category" ]]; then
            file="${agent}.md"
            if [[ -f "$file" ]]; then
                update_agent "$file" "$chain" "$category"
            fi
        fi
    done
    echo ""
done

# Summary
echo "════════════════════════════════════════════════════════════════════════════"
echo ""
echo -e "${GREEN}Fallback Chain Summary:${NC}"
echo ""
printf "  %-15s │ %-30s │ %s\n" "Category" "Primary Model" "Fallback Chain"
echo "  ───────────────┼────────────────────────────────┼─────────────────────────────"
for category in CRITICAL ARCHITECTURE CODING PERFORMANCE TOOLING CLI FRONTEND DOCS FREE; do
    chain=$(get_chain "$category")
    primary=$(get_primary_model "$chain" | sed 's|.*/||')
    fallbacks=$(echo "$chain" | tr '|' '→' | sed 's|google/antigravity-||g' | sed 's|opencode/||g')
    printf "  %-15s │ %-30s │ %s\n" "$category" "$primary" "$fallbacks"
done
echo ""

if [[ "$DRY_RUN" == "true" ]]; then
    echo -e "${YELLOW}[DRY RUN]${NC} Nenhuma mudança foi aplicada."
    echo "Execute com --apply para aplicar as mudanças."
else
    echo -e "${GREEN}✅ Mudanças aplicadas com sucesso!${NC}"
fi
echo ""
