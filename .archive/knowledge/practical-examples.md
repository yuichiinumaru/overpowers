# Exemplos Práticos: Integração Híbrida (awesome-opencode + context-engineering-kit)

## Caso de Uso 1: Desenvolver Nova Feature (E-commerce Checkout)

### Contexto
- Empresa: E-commerce startup
- Feature: Sistema de checkout com pagamento
- Time: 3 developers
- Deadline: 5 dias
- Prioridade: Qualidade (payment = security-critical)

### Workflow Passo-a-Passo

#### Passo 1: Análise (Hora 0-1)

**Input**: PRD do produto owner
```
Feature: Checkout com múltiplos pagamentos
- Suportar Stripe, PayPal, Apple Pay
- Suportar parcelamento 3x, 6x, 12x
- Validação de fraude em tempo real
- Compliance: PCI-DSS, GDPR
```

**Ferramenta**: context-engineering-kit First Principles Framework

**Comando**:
```bash
claude-code --skill first-principles-framework \
  --input "checkout-feature.md" \
  --output ddr-checkout.md
```

**Output: Design Rationale Record**
```markdown
# DRR: E-commerce Checkout System

## Decision
- Use Stripe as primary payment processor
- Implement fraud detection via Stripe Radar
- Store minimal PCI data (tokens only)
- Architecture: Backend-driven, not client-side payment handling

## Alternatives Evaluated
1. ❌ Implement own fraud detection: Too complex, false positives
2. ❌ Use PayPal for everything: Limited local payment methods
3. ❌ Client-side payment (browser): PCI compliance nightmare
4. ✅ Stripe Radar (ML-based fraud): Industry standard, maintained

## Constraints
- PCI-DSS Level 1: No card numbers in DB
- GDPR: European customers = special handling
- Legacy app: Already using Stripe for subscriptions

## Risk Mitigation
- Risk: Stripe API rate limits
  → Mitigation: Queue-based payment processing
- Risk: Fraud false positives
  → Mitigation: Retry logic + human review at $100+ orders

## Approval Status
- Backend Lead: Jane (✅)
- Security Officer: Ahmed (✅)
- Finance: Robert (pending)
```

---

#### Passo 2: Task Breakdown (Hora 1-2)

**Ferramenta**: context-engineering-kit Spec-Driven Development

**Input**: PRD + DRR

**Output**: 6 subtasks independentes

```yaml
tasks:
  - id: "payment-gateway-integration"
    description: "Stripe API integration, webhook handlers"
    dependencies: []
    estimated_tokens: 15000
    estimated_cost: $0.50
    
  - id: "fraud-detection-service"
    description: "Implement Stripe Radar rules, scoring logic"
    dependencies: [payment-gateway-integration]
    estimated_tokens: 12000
    estimated_cost: $0.40
    
  - id: "frontend-checkout-form"
    description: "React checkout component, Stripe Elements, error handling"
    dependencies: [payment-gateway-integration]
    estimated_tokens: 18000
    estimated_cost: $0.60
    
  - id: "order-confirmation-workflow"
    description: "Email notifications, order status updates, invoice generation"
    dependencies: [payment-gateway-integration]
    estimated_tokens: 10000
    estimated_cost: $0.35
    
  - id: "test-suite"
    description: "Unit tests, integration tests, E2E tests"
    dependencies: [payment-gateway-integration, frontend-checkout-form]
    estimated_tokens: 16000
    estimated_cost: $0.55
    
  - id: "documentation-and-runbooks"
    description: "API docs, deployment guide, incident response playbook"
    dependencies: [payment-gateway-integration]
    estimated_tokens: 8000
    estimated_cost: $0.25
```

---

#### Passo 3: Setup Kanban & Discord (Hora 2-3)

**Ferramenta**: awesome-opencode Vibe Kanban + Kimaki Discord Bot

**Ação 1**: Criar Vibe Kanban board
```
Backlog (6 tasks listed above)
  ↓
Ready (all tasks ready, waiting for agentes)
  ↓
[Agentes consomem conforme disponibilidade]
```

**Ação 2**: Configurar Kimaki Discord notifications
```bash
# ~/.kimaki/config.yaml
project: checkout-feature
channel: #ai-coding
notifications:
  - event: task_started
    message: "🚀 {task_name} started by {agent_name}"
  - event: quality_gate_pass
    message: "✅ {task_name} passed review! Score: {score}/10"
  - event: quality_gate_fail
    message: "🔄 {task_name} needs revision: {issues}"
  - event: cost_alert
    condition: "cost > $0.60 per task"
    message: "💰 {task_name} costing more than estimated: ${cost}"
```

**Discord Output esperado**:
```
[14:32] 🚀 payment-gateway-integration started by Subagent-1
[14:45] 🚀 frontend-checkout-form started by Subagent-2
[14:52] 🚀 test-suite waiting (depends on payment-gateway)

[15:18] ✅ payment-gateway-integration passed review! Score: 8.7/10
        - No issues found by Bug Hunter
        - Zero security vulnerabilities (Security Auditor)
        - 92% test coverage (exceeds 80% minimum)
        
[15:34] 🔄 fraud-detection-service needs revision
        - Type mismatch in FraudScore interface (Type Design)
        - Missing rate limiting on Radar API calls (Performance)
        - Feedback: Implement exponential backoff for API calls
```

---

#### Passo 4: Implementação Paralela (Hora 3-9)

**Ferramenta**: context-engineering-kit Subagent-Driven Development + awesome-opencode Subtask2

**Cenário**: Tasks 1, 2, 3 em paralelo (independent)

```
Timeline:
Hour 3-5: Task 1 (Stripe integration) → Subagent-1
          Task 2 (Fraud detection)    → Subagent-2  [waits on Task 1]
          Task 3 (Frontend)           → Subagent-3  [waits on Task 1]

Hour 5-6: Quality Gate Reviews (parallel)
          Each completed task → Code Review Multi-Agent
          
Hour 6-8: Task 4 (Order confirmation) → Subagent-4
          Task 5 (Tests)              → Subagent-5  [waits on Tasks 1, 3]
          Task 6 (Docs)               → Subagent-6  [waits on Task 1]
          
Hour 8-9: Final quality reviews
```

**Isolation Pattern** (context-engineering-kit):
```
Task 1: payment-gateway-integration
├─ Context provided:
│  ├─ PRD excerpt (payments section)
│  ├─ DRR (decision rationale)
│  ├─ Tech stack guide (Node.js, Express, PostgreSQL)
│  ├─ Stripe API docs (excerpt)
│  └─ Example from existing codebase (subscription system)
│
├─ Context EXCLUDED:
│  ├─ Frontend code (Task 3)
│  ├─ Test files (Task 5)
│  └─ Documentation (Task 6)
│
└─ Output: stripe-integration.js, stripe-webhooks.js

Task 2: fraud-detection-service
├─ Context provided:
│  ├─ Output from Task 1 (stripe-integration.js)
│  ├─ Stripe Radar documentation
│  ├─ ML model examples
│  └─ DRR (fraud detection decision)
│
├─ Context EXCLUDED:
│  ├─ Frontend details
│  ├─ Tests (hasn't been written yet)
│  └─ Other tasks' outputs
│
└─ Output: fraud-detector.js, radar-rules.yaml
```

---

#### Passo 5: Code Review Multi-Agent (Hora 5-9)

**Ferramenta**: context-engineering-kit Code Review (6+ especialistas)

**Exemplo Real**: Task 1 completa, entra em Code Review

**Input Code** (stripe-integration.js):
```javascript
// Task 1 output: Stripe integration
const stripe = require('stripe')(process.env.STRIPE_SECRET);

app.post('/api/payments', async (req, res) => {
  const { amount, currency, metadata } = req.body;
  
  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency,
      metadata
    });
    
    res.json({ clientSecret: paymentIntent.client_secret });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

app.post('/api/webhooks/stripe', express.raw({type: 'application/json'}), 
  async (req, res) => {
    // Webhook handler
    const sig = req.headers['stripe-signature'];
    
    try {
      const event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        process.env.STRIPE_WEBHOOK_SECRET
      );
      
      if (event.type === 'payment_intent.succeeded') {
        // Handle success
      }
    } catch (err) {
      res.status(400).json({ error: `Webhook error: ${err.message}` });
    }
  }
);
```

**Code Review Output** (6 agentes):

```
┌─────────────────────────────────────────────────────┐
│ CODE REVIEW RESULTS: stripe-integration.js          │
├─────────────────────────────────────────────────────┤
│                                                     │
│ 🐛 BUG HUNTER (Score: 9/10)                        │
│ ✅ No logical errors found                         │
│ ⚠️  Edge case: What if metadata is > 50KB?         │
│    (Stripe metadata limit)                         │
│    Recommendation: Add validation before create()  │
│                                                     │
│ 🔐 SECURITY AUDITOR (Score: 6/10)                  │
│ ❌ CRITICAL: Missing webhook signature verification│
│    Line 32-37: event = construct_event() can fail  │
│    if sig doesn't match. No error handling.        │
│ ❌ HIGH: Missing rate limiting                     │
│    /api/payments endpoint can be abused           │
│    Recommendation: Add req.rateLimit() middleware  │
│ ✅ Good: Using environment variables for secrets  │
│                                                     │
│ 🧪 TEST COVERAGE (Score: 7/10)                     │
│ ⚠️  No tests provided yet (Task 5 will do)         │
│ Recommendation: Add unit tests for:               │
│  - Valid payment creation                         │
│  - Invalid metadata handling                      │
│  - Webhook signature validation                   │
│  - Error cases (network timeout, etc)             │
│                                                     │
│ ⚡ PERFORMANCE (Score: 9/10)                        │
│ ✅ Async/await proper                             │
│ ✅ No N+1 queries                                  │
│ ⚠️  Consider: DB transaction for payment recording │
│    After stripe.paymentIntents.create()          │
│                                                     │
│ 📘 TYPE DESIGN (Score: 8/10)                       │
│ ⚠️  Missing TypeScript types                       │
│ Recommendation: Add interfaces for:               │
│  interface PaymentRequest {                       │
│    amount: number;                                │
│    currency: string;                              │
│    metadata?: Record<string, string>;             │
│  }                                                 │
│                                                     │
│ ♻️  CODE SIMPLIFICATION (Score: 9/10)              │
│ ✅ Code is clear and maintainable                  │
│ ⚠️  Extract webhook handler to separate file      │
│                                                     │
├─────────────────────────────────────────────────────┤
│ OVERALL SCORE: 7.8 / 10.0                          │
│                                                     │
│ STATUS: 🔄 REVISE REQUIRED                         │
│ Minimum score for pass: 8.0                        │
│ Issues blocking: 2 critical (rate limit, webhook)  │
│                                                     │
│ Next Step: Subagent-1 will receive feedback +      │
│            fresh context and fix issues           │
└─────────────────────────────────────────────────────┘
```

**Discord Notification**:
```
[15:47] 🔄 payment-gateway-integration needs revision
Code Review Score: 7.8/10 (minimum required: 8.0)

❌ Critical Issues:
  - Missing rate limiting on /api/payments
  - Webhook signature verification incomplete

⚠️  Warnings:
  - TypeScript types missing
  - Metadata validation required

Subagent-1 will revise and resubmit with fresh context.
ETA: 20 minutes
```

**Subagent-1 Receives**:
```
Fresh Context for Revision:
✓ Original task spec
✓ Code Review feedback (7.8/10)
✓ Specific issues (2 critical, 2 warnings)
✗ Removed: Details from other tasks
✗ Removed: Cancelled ideas (audit trail not needed)
✗ Removed: Initial implementation attempts

Task: Fix rate limiting and webhook issues, 
      add TypeScript types, validate metadata.
      Must achieve 8.0+ score on re-review.
```

---

#### Passo 6: Task 2 Processa (Paralelamente)

**Enquanto** Task 1 em revisão, Task 2 avança:

```
Task 2 Inicia: fraud-detection-service
├─ Entrada: Output de Task 1 (versão anterior, good enough)
├─ Entrada: DRR sobre Stripe Radar
├─ Saída: fraud-detector.js (detecta fraude)
│
└─ Code Review Multi-Agent:
   Score: 8.9/10 ✅ PASS
   - Only warning: Add mocking for Radar API in tests
   
   ✅ Approved! Moving to Done
```

**Discord**:
```
[16:15] ✅ fraud-detection-service passed review! Score: 8.9/10
   Only suggestion: Mock Stripe Radar in test suite
   Status: ✅ APPROVED → Ready for production
```

---

#### Passo 7: Consolidação & Deploy (Hora 9)

**Após todos tasks ≥8.0 score**:

```
Step 1: Dynamic Context Pruning (awesome-opencode)
  └─ Remove intermediate reviews, keep only final code + DRR

Step 2: Merge all tasks
  ├─ stripe-integration.js (Task 1, revised)
  ├─ fraud-detector.js (Task 2)
  ├─ checkout-form.jsx (Task 3)
  ├─ order-confirmation.js (Task 4)
  ├─ __tests__/ (Task 5)
  └─ docs/ (Task 6)

Step 3: Tokenscope Final Report (awesome-opencode)
```

**Final Report**:
```
═══════════════════════════════════════════════════════
    CHECKOUT FEATURE: EXECUTION SUMMARY
═══════════════════════════════════════════════════════

⏱️  TIMELINE
├─ Analysis: 1 hour
├─ Design + Kanban: 1 hour
├─ Implementation: 4 hours (parallelized)
├─ Review cycles: 2 hours (Task 1 revision, others parallel)
└─ Total: 8 hours (vs ~40 hours if sequential)

💰 COST BREAKDOWN (Tokenscope)
├─ Analysis + Design: $1.20
├─ Implementation (6 tasks): $3.25
├─ Reviews (6 reviews, 2 revisions): $1.85
├─ Dynamic pruning savings: -$0.45
├─ Total: $6.85
└─ Per feature: $6.85 (vs est. $8.00, +14% savings!)

📊 QUALITY METRICS
├─ Avg code review score: 8.6/10
├─ First-pass rate: 67% (4/6 tasks passed first time)
├─ Security issues prevented: 3
├─ Bug count: 0 (none reached code review stage!)
├─ Test coverage: 91% (exceeded 80% requirement)
├─ Type coverage: 100% (all TypeScript)

✅ APPROVALS
├─ Security Officer (Ahmed): ✅
├─ Backend Lead (Jane): ✅
├─ Frontend Lead (Marcus): ✅
├─ QA Manager (Lisa): ✅
└─ Ready for production ✅

🚀 DEPLOYMENT
├─ Timestamp: 2026-01-17 18:00 UTC
├─ Regression tests: All passing
├─ Stripe sandbox test: ✅ Success
├─ Fraud detection test: ✅ Caught 5/5 test-fraud cases
└─ Live: YES (confidence: VERY HIGH)

═══════════════════════════════════════════════════════
```

---

## Caso de Uso 2: Quick Bug Fix (Opencode Only Path)

### Contexto
- Bug: Users see checkout amount multiplied by 100
- Root cause: cents conversion error
- Fix time: ~5 minutes
- Risk: LOW (single function)

### Workflow Simplificado

```
1. Product owner reports bug in Discord:
   "Checkout shows $1,000 instead of $10"

2. Developer opens Opencode (awesome-opencode CLI):
   $ opencode "Fix checkout amount conversion"
   
3. Opencode analyzes codebase → finds bug in formatPrice():
   ```javascript
   // Bug:
   const formatPrice = (cents) => (cents * 100).toFixed(2);
   // Fix:
   const formatPrice = (cents) => (cents / 100).toFixed(2);
   ```

4. Subagent-1 fixes in 2 minutes

5. Skip code review? (context-engineering-kit would say NO)
   But for single-line fix, maybe acceptable...
   
   Better: Run quick security check only:
   $ context-engineering-kit --lite-review formatPrice() → ✅ Pass
   
6. Merge directly
   
7. Discord notification:
   ✅ Checkout amount conversion fixed
   Cost: $0.02
   Risk: LOW
   Deployed: YES
```

**Key Difference**: No need for full Code Review Multi-Agent for trivial fixes.

---

## Caso de Uso 3: Legacy System Refactor (Full Hybrid Path)

### Contexto
- Legacy codebase: 10 years old
- Task: Migrate from Mongoose to Prisma ORM
- Team: 2 developers (junior + senior)
- Timeline: 2 weeks
- Criticality: VERY HIGH (20+ endpoints)

### Workflow

```
Week 1: ANALYSIS PHASE
├─ First Principles Framework (context-engineering-kit)
│  └─ Why Prisma? (vs Sequelize, TypeORM, etc)
│  └─ Risk assessment (20 endpoints = high complexity)
│  └─ Output: DRR with migration strategy
│
├─ Tech Stack Plugin (context-engineering-kit)
│  └─ Map 50+ Mongoose schemas
│  └─ Identify patterns (middleware, virtuals, plugins)
│  └─ Output: Schema equivalence table
│
└─ Customaize Agent (awesome-opencode)
   └─ Create migration checklist

Week 2: IMPLEMENTATION PHASE
├─ Subagent-Driven Development (context-engineering-kit)
│  └─ Break into 8 independent tasks:
│     Task 1: Setup Prisma + schema definition
│     Task 2: User model migration
│     Task 3: Product model migration
│     Task 4: Order model migration
│     Task 5: Update 10 API endpoints (User)
│     Task 6: Update 5 API endpoints (Product)
│     Task 7: Update 5 API endpoints (Order)
│     Task 8: Migration script + rollback plan
│
├─ Parallel execution (Subtask2, awesome-opencode)
│  └─ Tasks 2, 3, 4 in parallel (no dependencies)
│  └─ Tasks 5, 6, 7 wait on Tasks 2, 3, 4
│  └─ Task 8 last (after all migrations)
│
├─ Quality Gates (context-engineering-kit)
│  └─ Each task reviewed by:
│     - Bug Hunter (schema migrations correct?)
│     - Type Design (Prisma types match?)
│     - Performance (N+1 queries removed?)
│     - Test Coverage (all endpoints tested?)
│
└─ Monitoring (awesome-opencode)
   └─ Tokenscope: Track cost per model
   └─ Vibe Kanban: Visual progress
   └─ Kimaki: Discord alerts

Result:
├─ 20 endpoints migrated
├─ 0 regressions (caught by review gates)
├─ 100% test coverage on new code
├─ Rollback plan ready
├─ Cost: ~$35
└─ Timeline: 5 days (2 weeks estimate → 5 days!)
```

---

## Resumo: Quando Usar Qual Ferramenta

| Situação | Ferramenta | Razão |
|----------|-----------|-------|
| **Quick one-line bug** | awesome-opencode CLI | Rápido, zero overhead |
| **New feature (3+ tasks)** | Full hybrid stack | Qualidade + paralelismo |
| **Security-critical code** | context-engineering-kit Full review | Zero regressions |
| **Legacy migration** | Full hybrid stack | Risk management |
| **Cost optimization** | awesome-opencode Tokenscope | Track spending |
| **Team collaboration** | awesome-opencode Discord + Kanban | Visibility |
| **Reasoning audit trail** | context-engineering-kit DRR | Compliance |

