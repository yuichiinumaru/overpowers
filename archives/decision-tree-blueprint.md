# Decision Tree & Implementation Blueprint: Hybrid Stack

## Quick Decision Tree

```
┌─ Você quer aproveitar MELHOR DE AMBOS?
│
├─ SIM → Continuar neste documento
│
└─ NÃO → Usar apenas um:
   ├─ awesome-opencode: Máxima flexibilidade, múltiplos backends
   └─ context-engineering-kit: Máxima qualidade, raciocínio auditável
```

---

## Parte 1: Architecture Decision Matrix

### Qual IDE escolher?

| IDE | awesome-opencode | context-engineering-kit | Recomendação |
|-----|------------------|-------------------------|--------------|
| **Claude Code** | ✅ Nativo | ✅✅ Native MCP | ⭐ BEST |
| **Cursor** | ✅ Plugins | ✅✅ MCP config | ⭐ BEST |
| **Windsurf** | ⚠️ Via proxy | ✅ MCP nativo | ✅ BOM |
| **Cline** | ⚠️ Suporte | ✅ MCP nativo | ✅ BOM |
| **VS Code** | ✅ Plugin | ⚠️ Plugin | ✅ BOM |
| **Opencode** | ✅✅ Native | ⚠️ Partial | ⚠️ OK |

**Recomendação**: Cursor ou Claude Code (suportam 100% de ambos)

---

### Qual backend de IA escolher?

| Backend | awesome-opencode Suporte | context-engineering-kit | Recomendação |
|---------|--------------------------|-------------------------|--------------|
| **Claude 3.5 Sonnet** | Via MCP | ✅ Nativo | ⭐ BEST |
| **GPT-4o** | ✅ Nativo (OpenAI Auth) | Via MCP | ✅ BOM |
| **Gemini 2.0** | ✅ Nativo (Gemini Auth) | Via MCP | ✅ BOM |
| **Local (Ollama)** | Via proxy | Via MCP | ⚠️ SLOW |

**Recomendação**: Claude 3.5 Sonnet (melhor qualidade raciocínio + ambos suportam)

---

## Parte 2: Layer-by-Layer Implementation Guide

### Layer 1: INPUT & PARSING
**Objetivo**: Converter requirement em spec estruturado

```
Entrada: PRD / Issue / Slack message
   ↓
Ferramenta: awesome-opencode Customaize Agent
   ├─ Parse natural language
   ├─ Extract constraints
   ├─ Identify dependencies
   └─ Output: Structured spec (JSON/YAML)
   ↓
Saída: Spec estruturado + task list inicial
```

**Implementação**:
```bash
# Comando (Cursor/Claude Code)
/customize-agent \
  --input "create a checkout system" \
  --output-format json \
  --include-constraints true
```

**Output esperado**:
```json
{
  "feature": "checkout-system",
  "requirements": [
    "Stripe integration",
    "Multiple payment methods",
    "Fraud detection"
  ],
  "constraints": [
    "PCI-DSS compliance",
    "GDPR for EU users"
  ],
  "estimated_tasks": 6,
  "complexity": "high"
}
```

---

### Layer 2: PLANNING & ARCHITECTURE
**Objetivo**: Decisões estruturadas + audit trail

```
Entrada: Spec estruturado
   ↓
Ferramenta 1: context-engineering-kit First Principles Framework
   ├─ Abduction: Gerar 3+ soluções
   ├─ Deduction: Validar logicamente
   └─ Induction: Coletar evidências
   ↓
Saída: Design Rationale Record (DRR)
   
Ferramenta 2: context-engineering-kit Tech Stack Plugin
   ├─ Mapear patterns existentes
   ├─ Identificar constraints arquiteturais
   └─ Garantir consistency
   ↓
Saída: Architecture decisions documented
```

**Implementação**:
```bash
# Via skill/command
/first-principles-framework \
  --spec checkout-spec.json \
  --output ddr-checkout.md \
  --alternatives 3 \
  --constraints-file architecture.yaml
```

**Output esperado**: DRR com decisões + alternativas descartadas + approval gates

---

### Layer 3: TASK BREAKDOWN
**Objetivo**: Converter spec em tarefas parallelizáveis

```
Entrada: DRR + Architecture decisions
   ↓
Ferramenta: context-engineering-kit Spec-Driven Development
   ├─ Identificar boundaries
   ├─ Minimizar dependencies
   ├─ Maximizar parallelism
   └─ Estimar tokens/custo
   ↓
Saída: Task breakdown (YAML with deps)
   
Setup Tool: awesome-opencode Vibe Kanban
   ├─ Criar board
   ├─ Popula Backlog com tasks
   └─ Set team access
   ↓
Saída: Kanban board ready
```

**Implementação**:
```bash
# Context-engineering-kit task breakdown
/spec-driven-development \
  --ddr ddr-checkout.md \
  --output tasks.yaml \
  --parallel-max 5

# awesome-opencode: sync to Kanban
vibe-kanban import tasks.yaml --project checkout-feature
```

**Output esperado**: 
```yaml
tasks:
  - id: payment-gateway
    depends: []
    tokens_est: 15000
    
  - id: fraud-detection
    depends: [payment-gateway]
    tokens_est: 12000
    
  - id: frontend-form
    depends: [payment-gateway]
    tokens_est: 18000
```

---

### Layer 4: IMPLEMENTATION (PARALLEL)
**Objetivo**: Executar tasks em paralelo com isolamento de contexto

```
Entrada: Task breakdown
   ↓
Ferramenta 1: context-engineering-kit Subagent-Driven Development
   ├─ Criar subagent fresco para cada task
   ├─ Passar APENAS o contexto necessário
   ├─ Manter tasks isoladas
   └─ Track outputs separadamente

Ferramenta 2: awesome-opencode Subtask2 (orchestration)
   ├─ Respeitar dependencies (Task B waits for Task A)
   ├─ Rodar paralelo quando possível
   ├─ Manage queueing se muitas tasks
   └─ Track execution timeline
   ↓
Saída: Implementação completada (por task)
```

**Implementação**:
```bash
# Subtask2: orchestrate execution
subtask2 run tasks.yaml \
  --parallel-factor 3 \
  --quality-gate code_review

# Logs/monitoring:
tokenscope watch --project checkout-feature
vibe-kanban watch --project checkout-feature
kimaki watch --discord-channel #ai-coding
```

**O que acontece**:
```
T+0:00  Task 1 (payment-gateway) starts     [fresh Subagent-1]
T+0:00  Task 2 (fraud-detection) waits      [blocked by Task 1]
T+0:00  Task 3 (frontend-form) waits        [blocked by Task 1]

T+0:30  Subagent-1 outputs code
        → Entra Code Review automática
        
T+0:45  Code Review resultado: 7.8/10 (FAIL, precisa 8.0)
        → Subagent-1 recebe feedback + fresh context
        
T+1:05  Task 1 revisado: 8.3/10 (PASS!)
        → Task 2 e 3 desbloqueadas
        → Subagent-2 e Subagent-3 começam
        
T+1:35  Task 2 output + Task 3 output
        → Ambas entram Code Review
        
T+1:50  Task 2: 8.9/10 ✅
        Task 3: 7.5/10 ❌ (revise needed)
        
T+2:20  Task 3 revisada: 8.4/10 ✅
        → Task 5 (tests) desbloqueada
        → All tasks now completed
```

---

### Layer 5: QUALITY GATES
**Objetivo**: Garantir qualidade antes de prosseguir

```
Entrada: Task output (código)
   ↓
Ferramenta: context-engineering-kit Code Review Multi-Agent
   ├─ Bug Hunter → Logical errors?
   ├─ Security Auditor → Vulnerabilities?
   ├─ Test Coverage → 80%+?
   ├─ Performance → O(n²) loops?
   ├─ Type Design → TypeScript correct?
   └─ Code Simplification → Refactor needed?
   ↓
Decisão:
   ├─ ✅ PASS (8.0+) → Próxima task
   ├─ 🔄 REVISE (6.0-7.9) → Subagent refaz com feedback
   └─ ❌ FAIL (<6.0) → Escalate human
   ↓
Saída: Aprovado ou feedback para revisão
```

**Implementação**:
```bash
# Automático (after each task completes)
context-engineering-kit code_review \
  --code task-output.js \
  --spec task-spec.md \
  --reviewers 6 \
  --threshold 8.0

# Se falhar:
if [ quality_score < 8.0 ]; then
  # Feedback automático + fresh context
  subagent-1 revise \
    --original task-output.js \
    --feedback code-review-feedback.md \
    --context task-spec.md
fi
```

---

### Layer 6: MONITORING & COLLABORATION
**Objetivo**: Visibilidade em tempo real + notificações

```
Entrada: Execução em progresso
   ↓
Ferramenta 1: awesome-opencode Vibe Kanban
   ├─ Backlog → Ready → In Progress → Review → Done
   ├─ Update automático com progresso
   ├─ Visualização por task/time/cost
   └─ Team access (visualiza tudo)

Ferramenta 2: awesome-opencode Kimaki Discord Bot
   ├─ Notificação por evento
   ├─ Task started: "🚀 payment-gateway started"
   ├─ Code review pass: "✅ fraud-detection passed! 8.7/10"
   ├─ Code review fail: "🔄 frontend-form needs revision"
   ├─ Cost alert: "💰 Task 3 cost exceeds estimate by 15%"
   └─ Deploy ready: "🚀 Ready for production!"

Ferramenta 3: awesome-opencode Tokenscope
   ├─ Track tokens/cost per task
   ├─ Trend analysis (quais tasks mais caras?)
   ├─ Budget alerts (se passar threshold)
   └─ ROI calculation (was AI cheaper than human dev?)
   ↓
Saída: Full visibility + team awareness
```

**Implementação**:
```bash
# Start monitoring (all 3 tools together)
kimaki watch --project checkout-feature --channel #ai-coding
vibe-kanban watch --project checkout-feature
tokenscope watch --project checkout-feature --alert-threshold 50

# Exemplo Discord output:
[14:32] 🚀 Started: payment-gateway-integration
        Subagent: Claude-3.5-Sonnet
        
[15:18] ✅ Passed: payment-gateway-integration
        Score: 8.7/10
        Cost so far: $1.20
        
[15:20] 🚀 Started: fraud-detection-service
[15:22] 🚀 Started: frontend-checkout-form
        (both parallel, depends on payment-gateway)
        
[16:05] 🔄 Revision needed: frontend-checkout-form
        Issues: Type mismatch, missing error handling
        Feedback sent to Subagent, retrying...
        
[16:25] ✅ Passed: frontend-checkout-form (revised)
        Total cost for this task: $0.62
```

---

### Layer 7: CONSOLIDATION & DEPLOY
**Objetivo**: Merge outputs + cleanup + ready for production

```
Entrada: Todos tasks ≥ 8.0 score
   ↓
Ferramenta 1: awesome-opencode Dynamic Context Pruning
   ├─ Remove histórico de reviews intermediários
   ├─ Keep apenas: código final + DRRs
   ├─ Reduce token usage em ~40%
   └─ Output: Limpo, pronto para merge

Ferramenta 2: awesome-opencode Tokenscope
   ├─ Relatório final de custos
   ├─ Breakdown por task
   ├─ Comparison vs estimativa
   └─ ROI vs human dev estimate

Ferramenta 3: context-engineering-kit Documentation
   ├─ Auto-generate API docs
   ├─ Link DRRs na documentação
   ├─ Create deployment runbook
   └─ Incident response playbook
   ↓
Saída: Pronto para deploy
```

**Implementação**:
```bash
# Consolidate outputs
git merge feature/checkout-system --quality-gates-passed

# Final report
awesome-opencode consolidate \
  --project checkout-feature \
  --output final-report.md

# Output esperado:
# ✅ All tasks passed quality gates
# 💰 Total cost: $6.85 (vs est. $8.00, -14% savings)
# 📊 Quality: 8.6/10 avg, 0 security issues
# ⏱️  Time: 8h (vs est. 40h sequential, 5x faster)
# 🚀 Ready for production: YES
```

---

## Parte 3: Decision Routes by Scenario

### Cenário A: "Preciso fazer TUDO certo (banca/healthcare)"

**Recomendação**: FULL HYBRID STACK

```
Layer 1 (Input)              ← awesome-opencode
  ↓
Layer 2 (Planning)           ← context-engineering-kit (FULL)
  - First Principles
  - DRRs for audit trail
  - Tech Stack analysis
  ↓
Layer 3 (Breakdown)          ← context-engineering-kit
  - Spec-driven workflow
  - Minimize dependencies
  ↓
Layer 4 (Implementation)     ← context-engineering-kit + awesome-opencode
  - Subagent-Driven (isolation)
  - Subtask2 orchestration
  ↓
Layer 5 (Quality)            ← context-engineering-kit (FULL)
  - Code Review Multi-Agent (6 specialists)
  - Quality gates 8.0+ minimum
  ↓
Layer 6 (Monitoring)         ← awesome-opencode (FULL)
  - Kanban + Discord + Tokenscope
  ↓
Layer 7 (Deploy)             ← Both
  - context-engineering-kit docs
  - awesome-opencode cost report
```

**Timeline**: 5-7 days
**Cost**: $30-50 (includes reviews)
**Risk**: ZERO (caught by reviews)

---

### Cenário B: "Preciso de velocidade + qualidade (startup)"

**Recomendação**: HYBRID LIGHT

```
Layer 1 (Input)              ← awesome-opencode (skip formal parsing)
  ↓
Layer 2 (Planning)           ← context-engineering-kit LITE
  - Skip formal DRRs
  - Tech Stack quick check
  ↓
Layer 3 (Breakdown)          ← context-engineering-kit
  - Spec-driven
  ↓
Layer 4 (Implementation)     ← Both (full parallel)
  ↓
Layer 5 (Quality)            ← context-engineering-kit (2-3 reviewers, not 6)
  - Bug Hunter + Security only
  - Threshold 7.5 (not 8.0)
  ↓
Layer 6 (Monitoring)         ← awesome-opencode
  ↓
Layer 7 (Deploy)             ← awesome-opencode focus (cost)
```

**Timeline**: 2-3 days
**Cost**: $15-25
**Risk**: Medium (less thorough review)

---

### Cenário C: "Preciso fazer RÁPIDO (hot fix)"

**Recomendação**: awesome-opencode ONLY

```
Layer 1: Parse input quickly (CLI)
  ↓
Layer 3: Skip planning/breakdown
  ↓
Layer 4: Single agent (not Subagent-Driven)
  ↓
Layer 5: Skip full review (maybe --lite-review)
  ↓
Layer 6: Minimal monitoring
  ↓
Layer 7: Deploy immediately
```

**Timeline**: 15-30 minutes
**Cost**: $0.50-2
**Risk**: High (no quality checks)

---

### Cenário D: "Múltiplos backends é crítico"

**Recomendação**: awesome-opencode PRIMARY + context-engineering-kit for quality

```
Ferramentas principais:
├─ awesome-opencode: OpenAI Auth + Gemini Auth + Custom proxies
│  └─ Switch backends mid-project
│  └─ Fallback if Claude unavailable
│
└─ context-engineering-kit: Quality gates (works with any backend via MCP)
   └─ Code review consistent regardless of backend
```

**Setup**:
```bash
# Cursor config
~/.cursor/mcp.json:
{
  "mcpServers": {
    "context_engineering": { ... },
    "awesome-opencode-proxy": {
      "backends": ["openai", "gemini", "claude"]
    }
  }
}
```

---

## Parte 4: Cost Breakdown Estimator

### Fórmula: Total Cost

```
Cost = (tokens_input + tokens_output) × price_per_token 
       + code_review_overhead × price_per_token
       + context_pruning_savings

Exemplo (Checkout Feature):
├─ Analysis: 5K tokens × $0.00003 = $0.15
├─ Implementation: 70K tokens × $0.00003 = $2.10
├─ Code review (6 specialists): 40K tokens × $0.00003 = $1.20
├─ Context pruning savings: -40% = -$1.08
└─ Total: $2.37

Vs contexto sem pruning: $3.45 (9% mais caro)
Vs não usar review: $2.10 (mas risco alto)
```

### Budget Tracking (awesome-opencode Tokenscope)

```bash
# Daily monitoring
tokenscope stats --period day

# Output:
Today's costs:
├─ awesome-opencode tools: $1.23
├─ context-engineering-kit tools: $2.45
├─ Code review overhead: $0.89
└─ Savings (pruning): -$0.35
  
Total: $4.22 / day

Monthly projection: ~$127
```

---

## Parte 5: Troubleshooting & Fallbacks

### Problema 1: Context token limit exceeded

**Solução**:
```bash
# awesome-opencode
dynamic-context-pruning --aggressive

# Output: Remove 60% of context, keep essentials
# Cost: Faster + cheaper, but risk of lower quality

# Better: context-engineering-kit
# Split task into smaller subtasks
# Each gets fresh, clean context
```

---

### Problema 2: Code review stuck (team disagreement)

**Solução**:
```bash
# context-engineering-kit escalation
code-review --mode debate \
  --reviewers [bug_hunter, security_auditor] \
  --resolution human_review

# Output: Debate results, escalate to human if tie
```

---

### Problema 3: Cost exceeding budget

**Solução**:
```bash
# awesome-opencode alert
tokenscope alert --threshold 50 \
  --action pause_non_critical

# Fallback:
# 1. Switch to lite-review (fewer reviewers)
# 2. Use cheaper backend (GPT-4o instead of Claude)
# 3. Reduce task granularity (merge tasks = less overhead)
```

---

## Parte 6: Metrics to Track

### Quality Metrics (context-engineering-kit)
- [ ] Avg code review score (target: 8.5+)
- [ ] First-pass rate (target: 70%+)
- [ ] Security issues prevented
- [ ] Test coverage (target: 85%+)
- [ ] Type coverage (target: 95%+)

### Performance Metrics
- [ ] Time to deploy (target: 5x faster than sequential)
- [ ] Parallelization factor
- [ ] Context pollution (target: <10% redundancy)

### Cost Metrics (awesome-opencode)
- [ ] Cost per task (target: $0.30-0.60)
- [ ] Total project cost vs budget
- [ ] ROI vs hiring human dev
- [ ] Cost trend (decreasing over time as team learns)

### Team Metrics
- [ ] Discord notifications (valuable?)
- [ ] Kanban board accuracy
- [ ] Human approvals required (target: minimal)
- [ ] Team satisfaction with workflow

---

## Summary: Quick Implementation Checklist

### Week 1: Setup
- [ ] Choose IDE (Cursor recommended)
- [ ] Install context-engineering-kit MCP
- [ ] Install awesome-opencode plugins
- [ ] Configure Kimaki Discord bot
- [ ] Create Vibe Kanban board
- [ ] Test first simple task

### Week 2: Integration
- [ ] Implement First Principles hook
- [ ] Configure Subagent-Driven setup
- [ ] Calibrate quality gates
- [ ] Create DRR templates
- [ ] Setup Tokenscope tracking

### Week 3: Scaling
- [ ] Run full feature with all layers
- [ ] Collect metrics
- [ ] Refine thresholds
- [ ] Document best practices
- [ ] Train team

### Week 4+: Operations
- [ ] Run in production
- [ ] Monitor ROI
- [ ] Adjust as needed
- [ ] Scale to team

