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
for f in ai-engineer architect-reviewer business-analyst cloud-architect \
         competitive-analyst llm-architect market-researcher microservices-architect \
         multi-agent-coordinator platform-engineer product-manager prompt-engineer \
         research-analyst trend-analyst ux-researcher workflow-orchestrator; do
    update_model "${f}.md" "gemini-3-pro-preview"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🔍 TIER 2 - Claude Opus 4.5 (Revisão & Planejamento)"
echo "═══════════════════════════════════════════════════════════════"
for f in code-reviewer code-quality-reviewer performance-reviewer security-code-reviewer \
         security-auditor compliance-auditor refactoring-specialist legacy-modernizer \
         risk-manager context-manager dependency-manager error-detective error-coordinator \
         debugger incident-responder pr-readiness-reviewer test-coverage-reviewer; do
    update_model "${f}.md" "claude-opus-4-5"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✍️ TIER 3 - Claude 4.5 Sonnet (Documentação & Código Geral)"
echo "═══════════════════════════════════════════════════════════════"
for f in technical-writer documentation-engineer api-documenter release-notes-writer \
         knowledge-synthesizer git-summarizer test-plan-writer todo-fixme-scanner \
         seo-specialist content-marketer documentation-accuracy-reviewer \
         python-pro django-developer backend-developer api-designer \
         java-architect kotlin-specialist spring-boot-engineer \
         csharp-developer dotnet-core-expert dotnet-framework-4-8-expert \
         frontend-developer react-specialist vue-expert angular-architect nextjs-developer \
         fullstack-developer graphql-architect \
         mobile-developer mobile-app-developer flutter-expert swift-expert \
         database-administrator database-optimizer postgres-pro sql-pro \
         mcp-developer websocket-engineer data-engineer; do
    update_model "${f}.md" "claude-sonnet-4-5"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "⚡ TIER 4 - Gemini 3 Flash High (Performance & Debug)"
echo "═══════════════════════════════════════════════════════════════"
for f in performance-engineer performance-monitor chaos-engineer sre-engineer \
         rust-engineer cpp-pro golang-pro embedded-systems \
         kubernetes-specialist terraform-engineer devops-engineer security-engineer \
         machine-learning-engineer ml-engineer mlops-engineer data-scientist nlp-engineer \
         qa-expert test-automator devops-incident-responder \
         fintech-engineer payment-integration penetration-tester scrum-master \
         project-manager legal-advisor customer-success-manager sales-engineer; do
    update_model "${f}.md" "gemini-3-flash-preview"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5a - grok-code (JS/TS Ecosystem)"
echo "═══════════════════════════════════════════════════════════════"
for f in javascript-pro typescript-pro electron-pro cli-developer \
         search-specialist accessibility-tester; do
    update_model "${f}.md" "grok-code"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5b - glm-4.7-free (PHP/WordPress)"
echo "═══════════════════════════════════════════════════════════════"
for f in php-pro laravel-specialist wordpress-master git-workflow-manager \
         tooling-engineer; do
    update_model "${f}.md" "glm-4.7-free"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5c - big-pickle (Ruby/Rails & Misc)"
echo "═══════════════════════════════════════════════════════════════"
for f in rails-expert blockchain-developer game-developer task-distributor \
         agent-organizer quant-analyst; do
    update_model "${f}.md" "big-pickle"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🆓 TIER 5d - minimax-m2.1-free (Operacional)"
echo "═══════════════════════════════════════════════════════════════"
for f in iot-engineer network-engineer build-engineer deployment-engineer \
         dx-optimizer data-analyst data-researcher ui-designer; do
    update_model "${f}.md" "minimax-m2.1-free"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "📊 RESUMO"
echo "═══════════════════════════════════════════════════════════════"
echo "Contagem por modelo:"
grep -l "model: gemini-3-pro-preview" *.md 2>/dev/null | wc -l | xargs printf "  🧠 Gemini 3 Pro:     %s agentes\n"
grep -l "model: claude-opus-4-5" *.md 2>/dev/null | wc -l | xargs printf "  🔍 Claude Opus 4.5:  %s agentes\n"
grep -l "model: claude-sonnet-4-5" *.md 2>/dev/null | wc -l | xargs printf "  ✍️ Claude Sonnet 4.5:%s agentes\n"
grep -l "model: gemini-3-flash-preview" *.md 2>/dev/null | wc -l | xargs printf "  ⚡ Gemini 3 Flash:   %s agentes\n"
grep -l "model: grok-code" *.md 2>/dev/null | wc -l | xargs printf "  🆓 grok-code:        %s agentes\n"
grep -l "model: glm-4.7-free" *.md 2>/dev/null | wc -l | xargs printf "  🆓 glm-4.7-free:     %s agentes\n"
grep -l "model: big-pickle" *.md 2>/dev/null | wc -l | xargs printf "  🆓 big-pickle:       %s agentes\n"
grep -l "model: minimax-m2.1-free" *.md 2>/dev/null | wc -l | xargs printf "  🆓 minimax-m2.1-free:%s agentes\n"
grep -l "model: inherit" *.md 2>/dev/null | wc -l | xargs printf "  ⚪ inherit (inalterado): %s agentes\n"
echo ""
echo "✅ Atualização concluída!"
