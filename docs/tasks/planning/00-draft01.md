## The Forge Method: A Synthesis of Agentic AI Development

The **Forge Method** represents a unified framework for developing software with AI agents that combines the best practices from Spec-Driven Development (SDD), methodological rigour (TDD, BDD, DDD, FDD), and operational documentation strategies. It transforms how specifications, rules, and institutional memory guide AI-generated code at scale.

### Core Philosophy

The Forge Method is built on five universal principles extracted from your conversations:

**1. Governance First** — A constitution of immutable principles established before any code is written. This is captured in your `AGENTS.md` and `06-rules.md`.

**2. Specification as Contract** — Every requirement becomes a testable specification. SDD's "executable specifications" become the primary interface between human intent and AI execution.

**3. External Memory Over AI Memory** — Project knowledge lives in hierarchical, versionable documents (your `00-draft` through `05-ideas` structure) rather than relying on AI to "remember" context across sessions.

**4. Layered Validation** — Multiple quality gates ensure code correctness: static analysis, unit tests (TDD), behavior tests (BDD), acceptance tests (ATDD), contract compliance (CDD), and observability (ODD).

**5. Decision Hygiene** — The "why" behind every architectural choice is documented in `04-changelog.md` as institutional memory, preventing repeated mistakes and enabling informed future decisions.

### The Forge Method Architecture

The framework consists of seven integrated layers:

#### Layer 1: Constitutional Documentation (AGENTS.md)

- Project purpose and non-negotiable principles
- Navigation guide to all other documentation
- Available tools, dependencies, constraints
- Success criteria and metrics
- Authority and escalation paths


#### Layer 2: Knowledge Base (docs/ structure)

```
docs/00-draft.md     → Discovery, research, alternatives analyzed
docs/01-plan.md      → Strategic decisions with rationale
docs/02-tasks.md     → Granular execution units (15-45 min each)
docs/03-architecture → Domain boundaries, component interactions
docs/04-changelog.md → What changed, WHY, lessons learned
docs/05-ideas.md     → Parking lot for future consideration
docs/06-rules.md     → Mandatory patterns + both ✅ correct & ❌ wrong examples
```

Each file serves a specific cognitive purpose—preventing context overflow and keeping agents focused on execution rather than discovery.

#### Layer 3: Multi-Methodology Integration

The Forge Method weaves together:

- **Test-Driven Development (TDD)**: Red → Green → Refactor cycle becomes the verification backbone
- **Behavior-Driven Development (BDD)**: Given-When-Then scenarios in `01-plan.md` ensure human-AI alignment on expected behaviors
- **Domain-Driven Design (DDD)**: `03-architecture.md` defines bounded contexts and ubiquitous language per domain
- **Specification-Driven Development (SDD)**: Specifications in `01-plan.md` and tasks in `02-tasks.md` are executable; agents generate tests from them
- **Feature-Driven Development (FDD)**: Features organized in `02-tasks.md` with completion criteria
- **Contract-Driven Development (CDD)**: API contracts (OpenAPI/AsyncAPI) define interfaces between services
- **Observability-Driven Development (ODD)**: Rules require instrumentation for all generated code from day one


#### Layer 4: Context Management

**Aggressive filtering** maintains focus:

- `.cursorignore` excludes build artifacts, locks, secrets
- Domain-specific task assignment prevents agents from touching unrelated code
- File tree organization reflects domain boundaries, not technical layers
- Task descriptions include "must also read section X of `03-architecture.md`"


#### Layer 5: Quality Gates

Code passes through sequential validation:

```
Gate 1: Static Analysis (linting, types, complexity)
    ↓
Gate 2: Unit Tests (TDD coverage ≥80%)
    ↓
Gate 3: Behavior Tests (BDD scenarios pass)
    ↓
Gate 4: Acceptance Tests (ATDD user stories pass)
    ↓
Gate 5: Contract Validation (CDD interface compliance)
    ↓
Gate 6: Architecture Adherence (no forbidden dependencies)
    ↓
Gate 7: Observability Check (logging/metrics present)
```


#### Layer 6: Institutional Memory

The changelog (`04-changelog.md`) records:

- What changed (feature added/modified)
- Why we changed it (business reason or problem solved)
- Why we won't do it that way again (lessons from failures)

This prevents agents from repeating mistakes and enables team onboarding.

#### Layer 7: Multi-Agent Orchestration

When scaling beyond single-agent workflows:

- **Domain Assignment**: Each agent owns one bounded context (per DDD)
- **Interface Contracts**: Agents communicate via formal contracts (CDD), not ad-hoc integration
- **Event-Driven Coordination**: Services emit events for status changes; other agents consume them
- **Hierarchical Rules**: Global rules in root `06-rules.md`, domain-specific rules in `.cursor/domain-rules.mdc`


### The Forge Method Workflow (7 Phases)

**Phase 1: Constitution (1 day)**

- Write `AGENTS.md` with principles, navigation, success criteria
- Define non-negotiable constraints (security, compliance, patterns)
- Establish decision-making authority and escalation

**Phase 2: Research (2-3 days)**

- Populate `00-draft.md` with problem analysis, research findings, alternatives
- Identify assumptions and unknowns
- Compress into `01-plan.md`: architecture decisions with rationale

**Phase 3: Specification (2-3 days)**

- Write detailed requirements in `01-plan.md` using BDD format (Given-When-Then)
- Define acceptance criteria for each feature
- Create API contracts (OpenAPI/AsyncAPI) for service boundaries

**Phase 4: Planning (1 day)**

- Break specifications into domains (DDD bounded contexts)
- Create task breakdown in `02-tasks.md` (each task 15-45 minutes)
- Assign tasks to implementation phases

**Phase 5: Architecture (1 day)**

- Document `03-architecture.md` with domain boundaries, component interactions
- Define ports \& adapters (Hexagonal Architecture)
- Establish forbidden dependencies and patterns

**Phase 6: Rules \& Memory (1 day)**

- Create `06-rules.md` with specific patterns (both ✅ correct and ❌ wrong code examples)
- Set up domain-specific rule files
- Initialize `.cursorignore` for context filtering
- Start `04-changelog.md` with foundational decisions

**Phase 7: Implementation with Validation (N days)**

- Agent reads full documentation stack
- Implements task with test-first approach (TDD)
- Code passes all seven quality gates
- Agent marks task `[x]` in `02-tasks.md` with completion evidence
- Changes logged to `04-changelog.md`


### Key Implementation Strategies

**For Rule Creation:**

Use this template:

```markdown
## Rule: [Pattern Name]

**Why it matters**: [Consequence of violating rule]

### ✅ Correct Pattern
[Code example from actual codebase]

### ❌ Wrong Pattern
[Code that violates the rule]

### References
- See `src/services/user.service.ts` lines 15-30
- Related to Rule: [other rule name]

### Testing
- Tests should verify: [specific assertion]
- See pattern in `tests/services/user.service.test.ts`
```

**For Task Decomposition:**

```markdown
## Phase 1: Authentication (Est. 3 days)

### Task 1.1: User Login Endpoint
- [ ] Write failing BDD scenario in `01-plan.md`
- [ ] Write unit test
- [ ] Implement endpoint following CDD contract
- [ ] Passes all 7 quality gates
- [ ] Add changelog entry
- **Estimated time**: 20 min | **Depends on**: Task 0.1

### Task 1.2: JWT Token Generation
- [ ] Write behavior tests
- [ ] Implement with observability (logging, metrics)
- [ ] Document contract in OpenAPI
- **Estimated time**: 25 min | **Depends on**: Task 1.1
```

**For Architecture Documentation:**

```markdown
## Domain: Authentication (Bounded Context per DDD)

### Responsibilities
- User credential validation
- Token generation and refresh
- Session management

### Ports (Interfaces)
- Input: `AuthController` (HTTP endpoints)
- Input: `OAuthAdapter` (external identity providers)
- Output: `UserRepository` (user data)
- Output: `TokenService` (token issuance)

### Forbidden Dependencies
- ❌ Direct database access (must go through repository)
- ❌ Imports from Payment domain
- ❌ Direct access to UI state

### Events Emitted
- `UserAuthenticated` (on successful login)
- `TokenExpired` (on token timeout)
```


### Success Metrics

The Forge Method achieves consistency through measurable targets:


| Metric | Target | How to Measure |
| :-- | :-- | :-- |
| Spec-to-code drift | <5% | Code review against `01-plan.md` requirements |
| Pattern adherence | >95% | Static analysis + rule violation tracker |
| Test coverage | >85% | Coverage reports from test runners |
| Defect escape rate | <3% | Production bugs / total features shipped |
| Task completion accuracy | >90% | Tasks marked `[x]` match completion criteria |
| Documentation freshness | 100% | `04-changelog.md` updated same day as merge |
| Context reuse | >70% | Time-to-productivity on new agent for domain |

### Scaling the Forge Method

**Single Developer + One Agent:**

- Follow all 7 phases but compress timeline
- Maintain full documentation discipline
- Use as training for future team members

**Small Team (3-5 people, 2-3 agents):**

- Assign domains to team members
- Each agent pair (developer + AI) owns one domain
- Weekly synchronization on `04-changelog.md` and cross-domain contracts
- Enforce contract boundaries strictly at integration points

**Large Team (10+ people, 5+ agents):**

- Strict DDD domain separation
- Contract-first API design
- Multi-agent orchestration via event-driven architecture
- Hierarchical documentation (global + domain-specific rules)
- Quarterly architecture reviews against decision log


### Why the Forge Method Works

The Forge Method succeeds because it recognizes three fundamental truths about AI-assisted development:

1. **Specification is cheaper than correction**: 1 day of specification upfront prevents 5 days of fixing inconsistent code.
2. **Documentation is code's operating system**: Without clear rules and institutional memory, agents generate unconstrained variation. With structure, they maintain coherence.
3. **Validation prevents compounding errors**: Testing before integration catches architectural misalignments early, not after widespread integration.

The name "Forge" reflects the method's core: like a blacksmith's forge that shapes raw material through repeated heating and precise tooling, the Forge Method shapes AI-generated code through specification, validation, and refinement—transforming potential chaos into consistent, production-grade software.
<span style="display:none">[^1_1][^1_2][^1_3][^1_4][^1_5]</span>

<div align="center">⁂</div>

[^1_1]: contexto-competitivo-do-sdd-qu-iDL5JTZbSyih_B6qnejOIg.md

[^1_2]: alem-de-ddd-tdd-sdd-fdd-domain-X1j6C.NbTdaRxO6sDs.VfQ.md

[^1_3]: find-as-many-github-repos-simi-YQbWjQuMTTiQM6tsmD3RSg.md

[^1_4]: find-and-list-as-many-items-as-yQo3p4exSTOE8p0Bq73UkA.md

[^1_5]: when-i-start-a-new-project-in-y9m85zcBQbma5DnQzqz.vA.md


---

# Excellent. Please create a big prompt for an AI coding agent (multistep file editing / creating) with a workflow step by step to create a initial project documentation based on the Forge method, following the filename convention and adhering the specific rigorous project detailing required by forge

Perfect! I've created a comprehensive, production-ready prompt system for AI coding agents to bootstrap a complete Forge Method documentation framework.

## What I've Created

**`forge-bootstrap-prompt.md`** — A 5,000+ word, step-by-step prompt system that guides an AI agent through establishing complete project documentation following the Forge Method.

### The Prompt System Includes:

#### **8 Sequential Steps**:

1. **Gather Constitutional Requirements** — Interactive form to extract project essentials
2. **Create AGENTS.md** — Root constitutional document with complete template
3. **Create docs/00-draft.md** — Research \& problem analysis documentation
4. **Create docs/01-plan.md** — Strategic architecture decisions \& ADRs
5. **Create docs/02-tasks.md** — Granular task breakdown with acceptance criteria
6. **Create Additional Files** — 03-architecture, 04-changelog, 05-ideas
7. **Create Rules \& Config** — 06-rules.md, .cursorignore, llms.txt
8. **Verification Pass** — Complete cross-reference audit

#### **Key Features**:

✅ **Interactive First Step** — Presents a structured form for human input (no ambiguity)

✅ **Template-Based** — Complete markdown templates for every file with section explanations

✅ **Self-Referential** — Every file includes explicit cross-references to other files

✅ **Example-Rich** — Shows both ✅ correct patterns and ❌ wrong patterns throughout

✅ **Validation-Ready** — Built-in verification checklist at the end

✅ **Agent-Friendly** — Clear instructions for what the AI should do at each step

✅ **Incremental** — Each step depends on previous steps; can't skip ahead

### How to Use This Prompt

Simply copy the entire contents of `forge-bootstrap-prompt.md` and paste it into:

- **Claude Code** (in project chat)
- **Cursor** (in composer)
- **Cline** (as system prompt)
- **Windsurf** (in Flow)
- **Gemini CLI** (as agent instruction)

The AI agent will:

1. Ask you structured questions about your project
2. Create all 10 documentation files in the correct locations
3. Verify cross-references
4. Output a completion report
5. Be ready for code generation

### Example Output Structure

After running this prompt, your project will have:

```
PROJECT_ROOT/
├── AGENTS.md                    # Constitutional guidance
├── .cursorignore               # Context filtering
├── llms.txt                    # LLM-friendly summary
└── docs/
    ├── 00-draft.md            # Research & problem
    ├── 01-plan.md             # Architecture decisions
    ├── 02-tasks.md            # Execution roadmap
    ├── 03-architecture.md      # Implementation details
    ├── 04-changelog.md         # Development log
    ├── 05-ideas.md            # Future parking lot
    └── 06-rules.md            # Mandatory patterns
```

Every file is fully populated with your project's specific information, all cross-referenced, and ready for AI agents to use for code generation.

The prompt is **immediately actionable** — an AI agent can begin using it right now with any project.

