#!/bin/bash
# Script para atualizar modelos nos agentes OpenCode
# Uso: ./update_models.sh

AGENTS_DIR="/home/sephiroth/.config/opencode/agents"
cd "$AGENTS_DIR" || exit 1

# Função para atualizar modelo em arquivo
update_model() {
    local file="$1"
    local model="$2"
    if [[ -f "$file" ]]; then
        sed -i "s/^model:.*/model: $model/" "$file"
        echo "✓ $(basename "$file") → $model"
    fi
}

echo "═══════════════════════════════════════════════════════════════"
echo "🧠 TIER 1 - Gemini 3 Pro High (Brainstorm & Criatividade)"
echo "═══════════════════════════════════════════════════════════════"
for f in ai_engineer architect_reviewer business_analyst cloud_architect \
         competitive_analyst llm_architect market_researcher microservices_architect \
         multi_agent_coordinator platform_engineer product_manager prompt_engineer \
         research_analyst trend_analyst ux_researcher workflow-orchestrator; do
    update_model "${f}.md" "gemini-3-pro-preview"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🔍 TIER 2 - Claude Opus 4.5 (Revisão & Planejamento)"
echo "═══════════════════════════════════════════════════════════════"
for f in code_reviewer code_quality_reviewer performance_reviewer security_code_reviewer \
         security_auditor compliance_auditor refactoring_specialist legacy_modernizer \
         risk_manager context_manager dependency_manager error_detective error_coordinator \
         debugger incident_responder pr_readiness_reviewer test-coverage-reviewer; do
    update_model "${f}.md" "claude-opus-4-5"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✍️ TIER 3 - Claude 4.5 Sonnet (Documentação & Código Geral)"
echo "═══════════════════════════════════════════════════════════════"
for f in technical_writer documentation_engineer api_documenter release_notes_writer \
         knowledge_synthesizer git_summarizer test_plan_writer todo_fixme_scanner \
         seo_specialist content_marketer documentation_accuracy_reviewer \
         python_pro django_developer backend_developer api_designer \
         java_architect kotlin_specialist spring_boot_engineer \
         csharp_developer dotnet_core_expert dotnet_framework_4_8_expert \
         frontend_developer react_specialist vue_expert angular_architect nextjs_developer \
         fullstack_developer graphql_architect \
         mobile_developer mobile_app_developer flutter_expert swift_expert \
         database_administrator database_optimizer postgres_pro sql_pro \
         mcp_developer websocket_engineer data-engineer; do
    update_model "${f}.md" "claude-sonnet-4-5"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "⚡ TIER 4 - Gemini 3 Flash High (Performance & Debug)"
echo "═══════════════════════════════════════════════════════════════"
for f in performance_engineer performance_monitor chaos_engineer sre_engineer \
         rust_engineer cpp_pro golang_pro embedded_systems \
         kubernetes_specialist terraform_engineer devops_engineer security_engineer \
         machine_learning_engineer ml_engineer mlops_engineer data_scientist nlp_engineer \
         qa_expert test_automator devops_incident_responder \
         fintech_engineer payment_integration penetration_tester scrum_master \
         project_manager legal_advisor customer_success_manager sales-engineer; do
    update_model "${f}.md" "gemini-3-flash-preview"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5a - grok-code (JS/TS Ecosystem)"
echo "═══════════════════════════════════════════════════════════════"
for f in javascript_pro typescript_pro electron_pro cli_developer \
         search_specialist accessibility-tester; do
    update_model "${f}.md" "grok-code"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5b - glm-4.7-free (PHP/WordPress)"
echo "═══════════════════════════════════════════════════════════════"
for f in php_pro laravel_specialist wordpress_master git_workflow_manager \
         tooling-engineer; do
    update_model "${f}.md" "glm-4.7-free"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5c - big-pickle (Ruby/Rails & Misc)"
echo "═══════════════════════════════════════════════════════════════"
for f in rails_expert blockchain_developer game_developer task_distributor \
         agent_organizer quant-analyst; do
    update_model "${f}.md" "big-pickle"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5d - minimax-m2.1-free (Operacional)"
echo "═══════════════════════════════════════════════════════════════"
for f in iot_engineer network_engineer build_engineer deployment_engineer \
         dx_optimizer data_analyst data_researcher ui-designer; do
    update_model "${f}.md" "minimax-m2.1-free"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "📊 RESUMO"
echo "═══════════════════════════════════════════════════════════════"
echo "Contagem por modelo:"
grep -l "model: gemini-3-pro-preview" *.md 2>/dev/null | wc -l | xargs printf "  🧠 Gemini 3 Pro:     %s agentes\n"
grep -l "model: inherit" *.md 2>/dev/null | wc -l | xargs printf "  🔍 Claude Opus 4.5:  %s agentes\n"
grep -l "model: claude-sonnet-4-5" *.md 2>/dev/null | wc -l | xargs printf "  ✍️ Claude Sonnet 4.5:%s agentes\n"
grep -l "model: gemini-3-flash-preview" *.md 2>/dev/null | wc -l | xargs printf "  ⚡ Gemini 3 Flash:   %s agentes\n"
grep -l "model: grok-code" *.md 2>/dev/null | wc -l | xargs printf "  🆓 grok-code:        %s agentes\n"
grep -l "model: glm-4.7-free" *.md 2>/dev/null | wc -l | xargs printf "  🆓 glm-4.7-free:     %s agentes\n"
grep -l "model: big-pickle" *.md 2>/dev/null | wc -l | xargs printf "  🆓 big-pickle:       %s agentes\n"
grep -l "model: minimax-m2.1-free" *.md 2>/dev/null | wc -l | xargs printf "  🆓 minimax-m2.1-free:%s agentes\n"
grep -l "model: inherit" *.md 2>/dev/null | wc -l | xargs printf "  ⚪ inherit (inalterado): %s agentes\n"
echo ""
echo "✅ Atualização concluída!"
