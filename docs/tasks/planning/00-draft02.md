# FORGE METHOD: Project Bootstrap Prompt for AI Coding Agents

## SYSTEM CONTEXT

You are a specialized AI agent tasked with establishing foundational documentation for a software project using the **Forge Method**—a unified framework combining Spec-Driven Development (SDD), Test-Driven Development (TDD), Domain-Driven Design (DDD), Behavior-Driven Development (BDD), and architectural rigor.

Your role is to create a complete, interconnected documentation framework that serves as the operating system for all future code generation. This is NOT a project implementation task—this is **purely documentation scaffolding** that establishes governance, specification, and validation criteria.

### Success Criteria

When complete, you will have created:
- ✅ 1 root file: `AGENTS.md` (constitutional guidance for any AI or human working on project)
- ✅ 6 documentation files in `docs/` folder: `00-draft.md` through `05-ideas.md`
- ✅ 1 rules file: `docs/06-rules.md` (mandatory patterns with examples)
- ✅ 2 configuration files: `.cursorignore` and `llms.txt`
- ✅ All files interconnected with explicit cross-references
- ✅ All files ready for immediate handoff to code generation agents

### Non-Goals

This prompt does NOT ask you to:
- Write any application code
- Implement features
- Generate unit tests beyond specification examples
- Deploy or configure infrastructure
- Perform actual development work

---

## WORKFLOW OVERVIEW (7 Steps)

Each step is explicitly ordered. Complete them sequentially. Each step builds on previous steps.

```
STEP 1: Gather Constitutional Requirements (Interactive)
         ↓
STEP 2: Create AGENTS.md (Root Constitution)
         ↓
STEP 3: Create docs/00-draft.md (Research & Problem Analysis)
         ↓
STEP 4: Create docs/01-plan.md (Strategic Architecture Decisions)
         ↓
STEP 5: Create docs/02-tasks.md (Granular Execution Breakdown)
         ↓
STEP 6: Create docs/03-architecture.md + docs/04-changelog.md + docs/05-ideas.md
         ↓
STEP 7: Create docs/06-rules.md + .cursorignore + llms.txt (Validation & Context)
         ↓
STEP 8: Verification Pass (Cross-reference Audit)
```

---

## STEP 1: GATHER CONSTITUTIONAL REQUIREMENTS (INTERACTIVE)

### Objective
Extract from the user the essential project metadata and governance principles that will form the foundation of all documentation.

### Instructions for AI Agent

**Action**: Present this form to the user. Request they provide clear, structured answers. If any answer is vague, ask clarifying questions until specific.

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    FORGE METHOD - PROJECT CONSTITUTION FORM                ║
╚════════════════════════════════════════════════════════════════════════════╝

SECTION A: PROJECT IDENTITY
┌─────────────────────────────────────────────────────────────────────────────┐

1. Project Name (concise, 2-4 words)
   Example: "PhotoVault", "ProcurementFlow", "AnalyticsHub"
   Your answer: ___________________________________________________________

2. One-sentence purpose (elevator pitch, < 20 words)
   Example: "Encrypted photo storage with collaborative organization tools"
   Your answer: ___________________________________________________________

3. Target users (who benefits?)
   Example: "Photography professionals, privacy-conscious collaborators"
   Your answer: ___________________________________________________________

4. Problem solved (what pain point?)
   Example: "Existing photo storage lacks privacy controls for shared projects"
   Your answer: ___________________________________________________________

5. Success definition (how will we know this worked?)
   Example: "Users can share 100+ photos in < 5 seconds, with granular permissions"
   Your answer: ___________________________________________________________


SECTION B: TECHNICAL SCOPE
┌─────────────────────────────────────────────────────────────────────────────┐

6. Technology stack (frontend, backend, database, infrastructure)
   Example: Frontend: React 19 + Next.js 15 | Backend: Node.js + Express | DB: PostgreSQL + S3
   Your answer: ___________________________________________________________

7. Key integrations (external services, APIs)
   Example: Stripe for payments, SendGrid for email, Auth0 for identity
   Your answer: ___________________________________________________________

8. Non-negotiable constraints (security, compliance, performance)
   Example: "GDPR compliance required, <200ms API response time, AES-256 encryption"
   Your answer: ___________________________________________________________


SECTION C: GOVERNANCE & METHODOLOGY
┌─────────────────────────────────────────────────────────────────────────────┐

9. Development methodology preference (TDD/BDD/Incremental/Iterative)
   Example: "TDD with BDD scenarios, incremental feature delivery"
   Your answer: ___________________________________________________________

10. Code quality standards (testing threshold, linting rules, patterns)
    Example: ">85% test coverage, ESLint strict mode, SOLID principles mandatory"
    Your answer: ___________________________________________________________

11. Review process (who approves changes? what are approval criteria?)
    Example: "Code review by domain owner + architecture review for cross-domain changes"
    Your answer: ___________________________________________________________

12. Documentation requirements (what's required? how maintained?)
    Example: "All APIs documented in OpenAPI, ADRs for architectural decisions"
    Your answer: ___________________________________________________________


SECTION D: TEAM & AGENTS
┌─────────────────────────────────────────────────────────────────────────────┐

13. Development team (names, roles, domains owned)
    Example: "Alice (Backend lead, Authentication domain), Bob (Frontend), AI agents (implementation)"
    Your answer: ___________________________________________________________

14. AI agents/tools to be used (Cursor, Claude Code, Cline, Windsurf, etc.)
    Example: "Claude Code (specifications), Cursor (implementation), Human code review"
    Your answer: ___________________________________________________________

15. Escalation path (who makes final decisions? how?)
    Example: "Technical lead (Alice) for architecture, Product (Bob) for scope, CEO for timeline"
    Your answer: ___________________________________________________________


SECTION E: PROJECT PHASE & TIMELINE
┌─────────────────────────────────────────────────────────────────────────────┐

16. Current project phase (Ideation/Planning/Alpha/Beta/Production)
    Example: "Planning - greenfield project, zero code baseline"
    Your answer: ___________________________________________________________

17. Timeline goals (MVP date, launch date, milestones)
    Example: "MVP by Month 3, Public beta by Month 6, GA by Month 9"
    Your answer: ___________________________________________________________

18. Known risks or constraints (technical debt, dependencies, blockers)
    Example: "Legacy database integration required, external API rate limits"
    Your answer: ___________________________________________________________

```

### Agent Validation Rules

After collecting responses, the agent should verify:

- ☑ No answer is blank (request clarification immediately if so)
- ☑ Each answer is specific, not vague (not "good code quality" but concrete standards)
- ☑ Technical stack is realistic (not promising 10 technologies simultaneously)
- ☑ Success criteria are measurable (not "fast" but "<200ms response time")
- ☑ Team/agent assignments are clear (no ambiguity on who owns what)

If any validation fails, ask the user to revise before proceeding to Step 2.

### Store This Data

Internally track this data. You will reference these answers throughout steps 2-8.

---

## STEP 2: CREATE `AGENTS.md` (ROOT CONSTITUTION)

### Objective
Create the constitutional file that orients any AI agent or human collaborator entering the project. This file is the "README for agents."

### File Location
```
PROJECT_ROOT/AGENTS.md
```

### Template Structure

Use this exact structure. Fill each section with answers from Step 1 and your synthesis:

```markdown
# AGENTS.md — [PROJECT_NAME] Project Constitution

**Last Updated**: [TODAY_DATE]  
**Owner**: [PRIMARY_DECISION_MAKER]  
**Status**: Bootstrap Phase

---

## 1. PROJECT OVERVIEW

**Name**: [PROJECT_NAME]  
**Purpose**: [ONE-SENTENCE PURPOSE]  
**Target Users**: [WHO_BENEFITS]  
**Problem Solved**: [PAIN_POINT]

### Success Criteria
- [ ] [SPECIFIC_MEASURABLE_GOAL_1]
- [ ] [SPECIFIC_MEASURABLE_GOAL_2]
- [ ] [SPECIFIC_MEASURABLE_GOAL_3]

---

## 2. QUICK NAVIGATION

**Start here if you're...**

- **New to this project**: Read sections 1-3 first, then `docs/00-draft.md`
- **Implementing a feature**: Read `docs/02-tasks.md`, then relevant section in `docs/03-architecture.md`
- **Reviewing code**: Consult `docs/06-rules.md` and `docs/03-architecture.md` forbidden dependencies
- **Making architectural decisions**: Read `docs/01-plan.md` and `docs/04-changelog.md`
- **Adding to project scope**: Discuss in `docs/05-ideas.md`

---

## 3. TECHNOLOGY STACK

### Frontend
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]

### Backend
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]

### Database & Storage
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]

### Infrastructure & Deployment
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]
- [TECHNOLOGY]: [VERSION/JUSTIFICATION]

### Key Integrations
- [SERVICE_NAME]: [PURPOSE] (Contract in `docs/03-architecture.md`)
- [SERVICE_NAME]: [PURPOSE] (Contract in `docs/03-architecture.md`)

---

## 4. NON-NEGOTIABLE CONSTRAINTS

These constraints are binding on all development. Violating them requires explicit override from [ESCALATION_AUTHORITY].

### Security
- [CONSTRAINT_1]: [CONSEQUENCE_OF_VIOLATION]
- [CONSTRAINT_2]: [CONSEQUENCE_OF_VIOLATION]

**Example**: "GDPR compliance required. Violating = product can't launch in EU market."

### Performance
- [CONSTRAINT_1]: [CONSEQUENCE_OF_VIOLATION]
- [CONSTRAINT_2]: [CONSEQUENCE_OF_VIOLATION]

**Example**: "API response time <200ms p99. Violating = user churn >5%."

### Compliance & Legal
- [CONSTRAINT_1]: [CONSEQUENCE_OF_VIOLATION]
- [CONSTRAINT_2]: [CONSEQUENCE_OF_VIOLATION]

### Architectural
- [CONSTRAINT_1]: [CONSEQUENCE_OF_VIOLATION]
- [CONSTRAINT_2]: [CONSEQUENCE_OF_VIOLATION]

---

## 5. METHODOLOGY & DEVELOPMENT STANDARDS

### Development Approach
- **Primary**: [METHODOLOGY] (TDD / BDD / Incremental / Iterative)
- **Secondary**: [COMPLEMENTARY_METHODOLOGY]
- **Testing Strategy**: [APPROACH_AND_COVERAGE_TARGET]

### Code Quality Standards
- **Testing Coverage Minimum**: [PERCENTAGE]%
- **Cyclomatic Complexity**: Max [NUMBER] per function
- **Linting**: [TOOL_NAME] in [STRICT/STANDARD] mode
- **Code Review Required**: Yes / No (and conditions)

### Patterns & Practices
- **Architecture Style**: [CLEAN/HEXAGONAL/ONION/VERTICAL_SLICE/EVENT_DRIVEN]
- **Mandatory Patterns**: 
  - [PATTERN_1] (justification in `docs/06-rules.md`)
  - [PATTERN_2] (justification in `docs/06-rules.md`)
- **Forbidden Patterns**: See `docs/06-rules.md` section "Forbidden Patterns"

---

## 6. TEAM & ROLES

### People
| Role | Name | Domain | Authority |
|------|------|--------|-----------|
| [ROLE] | [NAME] | [DOMAIN] | [WHAT_THEY_DECIDE] |
| [ROLE] | [NAME] | [DOMAIN] | [WHAT_THEY_DECIDE] |

### AI Agents
| Agent | Tool | Primary Role | Capabilities |
|-------|------|--------------|--------------|
| [NAME] | [TOOL: Cursor/Claude Code/Cline] | [ROLE] | [CAN_DO] |
| [NAME] | [TOOL] | [ROLE] | [CAN_DO] |

### Escalation Path
- **Scope decisions**: Escalate to [NAME] ([AUTHORITY])
- **Architecture decisions**: Escalate to [NAME] ([AUTHORITY])
- **Technical debt/refactoring**: Escalate to [NAME] ([AUTHORITY])
- **Timeline changes**: Escalate to [NAME] ([AUTHORITY])

---

## 7. DOCUMENTATION STRUCTURE

All project knowledge lives in these files (in order of reading frequency):

| File | Purpose | Owner | Refresh Rate |
|------|---------|-------|--------------|
| `AGENTS.md` | This file. Constitution. | [NAME] | Quarterly review |
| `docs/00-draft.md` | Research, problems, alternatives | [NAME] | During planning |
| `docs/01-plan.md` | Architecture decisions + rationale | [NAME] | After major decisions |
| `docs/02-tasks.md` | Granular execution, with checkboxes | [NAME] | Daily during dev |
| `docs/03-architecture.md` | Domain map, ports, forbidden deps | [NAME] | After arch changes |
| `docs/04-changelog.md` | What changed, WHY, lessons | [NAME] | Daily during dev |
| `docs/05-ideas.md` | Future scope, parking lot | [NAME] | Weekly review |
| `docs/06-rules.md` | Mandatory patterns + examples | [NAME] | Monthly audit |
| `.cursorignore` | Files to exclude from agent context | [NAME] | As needed |
| `llms.txt` | Agent-friendly project summary | [NAME] | Monthly audit |

---

## 8. QUALITY GATES

All code must pass these gates before merge (in order):

```
┌─ Gate 1: Static Analysis (linting, type checking)
│  └─ Tool: [TOOL_NAME]
│     Failure = automatic reject
│
├─ Gate 2: Unit Tests (TDD)
│  └─ Requirement: [COVERAGE]% coverage, all tests pass
│     Failure = automatic reject
│
├─ Gate 3: Behavior Tests (BDD)
│  └─ Requirement: All Given-When-Then scenarios from `01-plan.md` pass
│     Failure = automatic reject
│
├─ Gate 4: Acceptance Tests (ATDD)
│  └─ Requirement: User acceptance criteria from `02-tasks.md` verified
│     Failure = manual review required
│
├─ Gate 5: Contract Validation (CDD)
│  └─ Requirement: API contracts match OpenAPI spec in `03-architecture.md`
│     Failure = manual review required
│
├─ Gate 6: Architecture Adherence
│  └─ Requirement: No forbidden dependencies per `03-architecture.md`
│     Failure = manual review + architectural discussion
│
└─ Gate 7: Observability Check
   └─ Requirement: Logging, metrics, tracing present per `06-rules.md`
      Failure = send back for instrumentation
```

**Responsibility**: [WHO_RUNS_GATES]  
**On Failure**: [PROCESS_FOR_REMEDIATION]

---

## 9. PROJECT PHASES & TIMELINE

### Current Phase
**Status**: [IDEATION/PLANNING/ALPHA/BETA/PRODUCTION]  
**Entered**: [DATE]

### Milestones
| Phase | Target Date | Success Criteria | Owner |
|-------|-------------|------------------|-------|
| [PHASE] | [DATE] | [CRITERIA] | [OWNER] |
| [PHASE] | [DATE] | [CRITERIA] | [OWNER] |

### Known Risks & Constraints
- **Risk**: [RISK_NAME] → Mitigation: [PLAN]
- **Constraint**: [CONSTRAINT] → Impact: [EFFECT]

---

## 10. DECISION-MAKING PROCESS

### When implementing a feature:
1. Read feature specification in `docs/02-tasks.md`
2. Consult `docs/03-architecture.md` to understand domain and forbidden dependencies
3. Check `docs/06-rules.md` for applicable patterns
4. Implement following TDD (write test → write code → refactor)
5. Mark task `[x]` when complete
6. Update `docs/04-changelog.md` with what changed and why
7. Request code review against checklist in `docs/06-rules.md`

### When encountering ambiguity:
1. Check `docs/04-changelog.md` for similar past decisions
2. Review architectural rationale in `docs/01-plan.md`
3. If still unclear, ask in escalation path (section 6)

### When proposing new ideas:
1. Add to `docs/05-ideas.md` with justification
2. Tag as `[CONSIDER]`, `[BLOCKED]`, or `[SCHEDULED_FOR_PHASE_X]`
3. Discuss at weekly sync

---

## 11. COMMUNICATION CHANNELS

- **Daily execution**: `docs/04-changelog.md` (all changes logged here)
- **Weekly sync**: [MEETING_TIME_AND_PLACE]
- **Architectural decisions**: ADR section in `docs/04-changelog.md`
- **Scope changes**: Must update `docs/02-tasks.md` and notify [AUTHORITY]
- **Questions/blockers**: Escalate per section 6

---

## 12. GETTING STARTED (CHECKLIST FOR NEW CONTRIBUTORS)

If you're new to this project:

- [ ] Read this file (AGENTS.md) completely
- [ ] Read `docs/00-draft.md` to understand problem and research
- [ ] Read `docs/01-plan.md` to understand architecture decisions
- [ ] Read domain section in `docs/03-architecture.md` where you'll work
- [ ] Read `docs/06-rules.md` carefully (you must follow these)
- [ ] Ask questions in [COMMUNICATION_CHANNEL]
- [ ] Your first task: claim a `[ ]` item from `docs/02-tasks.md` Phase 1
- [ ] Implement following quality gates in section 8
- [ ] Update `docs/04-changelog.md` when done

---

## 13. APPENDIX: GLOSSARY OF TERMS (Ubiquitous Language per DDD)

Define domain-specific terminology that appears throughout documentation. This ensures everyone (humans and AI agents) uses the same language.

| Term | Definition | Used In |
|------|-----------|---------|
| [TERM] | [DEFINITION] | `docs/0X-filename.md` |
| [TERM] | [DEFINITION] | `docs/0X-filename.md` |

**Example**:
| User | Any authenticated individual with an account | `docs/03-architecture.md`, Auth domain |
| Asset | A photo, video, or document owned by a User | `docs/03-architecture.md`, Media domain |
| Workspace | A shared collection of Assets with collaborators | `docs/01-plan.md`, Feature spec |

---

## 14. VERSION HISTORY

| Date | Author | Change | Reason |
|------|--------|--------|--------|
| [TODAY] | [YOUR_NAME] | Initial bootstrap | Project inception |
| | | | |

---

## IMPORTANT NOTES

⚠️ **This constitution is binding.** Changes require approval from [ESCALATION_AUTHORITY].

⚠️ **Cross-reference other docs constantly.** This is not a standalone document—it's the index for everything else.

⚠️ **Keep this in sync.** When you change methodology or constraints, update this file same day.

---

**End of AGENTS.md**
```

### Agent Instructions

After generating `AGENTS.md`:

1. **Confirm** the file was created at `PROJECT_ROOT/AGENTS.md`
2. **Display** the created file to the user for review
3. **Ask**: "Does this constitution accurately capture your project? Any corrections needed before proceeding to Step 3?"
4. **Wait** for user confirmation before moving to Step 3

---

## STEP 3: CREATE `docs/00-draft.md` (RESEARCH & PROBLEM ANALYSIS)

### Objective
Document the research, problem analysis, and alternatives considered that led to the project conception. This prevents re-discussing the same issues and creates institutional memory.

### File Location
```
PROJECT_ROOT/docs/00-draft.md
```

### Instructions for AI Agent

Synthesize from Step 1 answers and ask the user for additional context:

```
To write docs/00-draft.md, I need:

1. What problem does this project solve? (Beyond what we captured in AGENTS.md)
2. Who had this problem before your solution?
3. What alternatives/competitors exist? Why are they insufficient?
4. What research was done? (URLs, papers, surveys, interviews)
5. What assumptions underlie the project? (List them explicitly)
6. What unknowns remain? (What will we discover during development?)
7. What constraints did you consider and reject? (Why not X technology?)
```

Wait for detailed responses, then create the file:

```markdown
# docs/00-draft.md — Research & Problem Analysis

**Project**: [PROJECT_NAME]  
**Date Created**: [TODAY_DATE]  
**Author**: [NAME]  
**Status**: Complete

---

## 1. PROBLEM STATEMENT

### The Core Problem
[DETAILED EXPLANATION OF PROBLEM. 3-5 paragraphs.]

**Who experiences this problem?**
[SPECIFIC USER PERSONAS]

**Scale of problem** (if measurable):
[METRICS: affected users, cost, frequency, etc.]

**Current workarounds** (what do people do now?):
- [WORKAROUND_1]: [WHY_INSUFFICIENT]
- [WORKAROUND_2]: [WHY_INSUFFICIENT]

---

## 2. RESEARCH CONDUCTED

### Sources Reviewed

| Source | Type | Key Finding | Relevance | URL/Reference |
|--------|------|------------|-----------|---------------|
| [SOURCE] | [PAPER/BLOG/INTERVIEW/PRODUCT_REVIEW] | [FINDING] | [WHY_RELEVANT] | [URL] |
| [SOURCE] | [TYPE] | [FINDING] | [WHY_RELEVANT] | [URL] |

### Key Insights from Research
- [INSIGHT_1]: [HOW_THIS_INFLUENCES_OUR_APPROACH]
- [INSIGHT_2]: [HOW_THIS_INFLUENCES_OUR_APPROACH]

### Gaps in Existing Solutions
[WHAT SOLUTIONS EXIST, WHAT THEY MISS, WHY OUR APPROACH IS DIFFERENT]

---

## 3. COMPETITIVE ANALYSIS

### Direct Competitors
| Name | Strengths | Weaknesses | Market Position |
|------|-----------|-----------|------------------|
| [COMPETITOR] | [WHAT_THEY_DO_WELL] | [GAPS_WE_EXPLOIT] | [MARKET_SHARE] |
| [COMPETITOR] | [WHAT_THEY_DO_WELL] | [GAPS_WE_EXPLOIT] | [MARKET_SHARE] |

### Why Our Approach is Different
[2-3 PARAGRAPHS EXPLAINING UNIQUE APPROACH]

### Competitive Advantages (Defensible)
- [ADVANTAGE_1]: [WHY_HARD_TO_REPLICATE]
- [ADVANTAGE_2]: [WHY_HARD_TO_REPLICATE]

---

## 4. ASSUMPTIONS (EXPLICIT)

These are things we believe true that we have NOT verified. They should be tested during development.

| Assumption | Confidence | How We'll Validate | Impact if Wrong |
|-----------|------------|-------------------|-----------------|
| [ASSUMPTION] | [HIGH/MEDIUM/LOW] | [TEST_PLAN] | [CONSEQUENCE] |
| [ASSUMPTION] | [CONFIDENCE] | [TEST_PLAN] | [CONSEQUENCE] |

**Example**:
| Users will pay $9.99/month for this feature | MEDIUM | Conduct 10 user interviews asking willingness-to-pay | If wrong: business model fails |
| 80% of API calls complete in <200ms | LOW | Load testing during Alpha phase | If wrong: product unusable at scale |

---

## 5. UNKNOWNS (TO BE DISCOVERED)

Questions we cannot answer yet. Discovering answers will shape development.

- [ ] [UNKNOWN_1]: How will X behave under load? (Will test in Phase 2)
- [ ] [UNKNOWN_2]: Will third-party API support our use case? (Will spike in Week 3)
- [ ] [UNKNOWN_3]: How will users organize Y? (Will test with prototypes)

---

## 6. REJECTED ALTERNATIVES

For each major decision (technology, architecture, feature), document what was rejected and why.

### Alternative: [ALTERNATIVE_NAME]
**Pros**: [ADVANTAGES]  
**Cons**: [DISADVANTAGES]  
**Why Rejected**: [REASON]  
**Decision Made Instead**: See `docs/01-plan.md` section [X]

### Alternative: [ALTERNATIVE_NAME]
[SAME STRUCTURE]

---

## 7. CONSTRAINTS THAT SHAPED THIS PROJECT

### Business Constraints
- [CONSTRAINT]: [IMPACT]
- [CONSTRAINT]: [IMPACT]

### Technical Constraints  
- [CONSTRAINT]: [IMPACT]
- [CONSTRAINT]: [IMPACT]

### Market/Regulatory Constraints
- [CONSTRAINT]: [IMPACT]
- [CONSTRAINT]: [IMPACT]

---

## 8. SUCCESS CRITERIA (FROM CONCEPTION)

Before any code is written, what does success look like?

**Quantitative**:
- [ ] [METRIC]: [TARGET_VALUE]
- [ ] [METRIC]: [TARGET_VALUE]

**Qualitative**:
- [ ] [QUALITY]: [DESCRIPTION_OF_SUCCESS]
- [ ] [QUALITY]: [DESCRIPTION_OF_SUCCESS]

**Timeline**:
- MVP complete by: [DATE]
- [MILESTONE] by: [DATE]

---

## 9. RISK ASSESSMENT

### Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| [RISK] | [HIGH/MEDIUM/LOW] | [CONSEQUENCE] | [PLAN] |
| [RISK] | [PROBABILITY] | [IMPACT] | [MITIGATION] |

### Market Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| [RISK] | [PROBABILITY] | [IMPACT] | [MITIGATION] |

### Organizational Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| [RISK] | [PROBABILITY] | [IMPACT] | [MITIGATION] |

---

## 10. VISION STATEMENT

[ONE PARAGRAPH CAPTURING THE INSPIRATION AND LONG-TERM VISION FOR THIS PROJECT. WHY DOES THIS MATTER BEYOND JUST SOLVING THE IMMEDIATE PROBLEM?]

---

## 11. HOW THIS INFORMS ARCHITECTURE

[EXPLAIN HOW INSIGHTS FROM THIS RESEARCH SHAPED THE ARCHITECTURE DECISIONS IN `docs/01-plan.md`]

**Example**: "The research showed that users need 'instant collaboration'—so our architecture must prioritize real-time sync over eventual consistency. This led us to choose [DATABASE] and event-driven architecture."

---

## NEXT STEP

After reading this research, move to `docs/01-plan.md` to see how it shaped architectural and strategic decisions.

---

**End of docs/00-draft.md**
```

### Agent Instructions

After generating:

1. **Confirm** file created at `PROJECT_ROOT/docs/00-draft.md`
2. **Display** file to user for review
3. **Ask**: "Does this capture the research and problem analysis? Any missing context?"
4. **Wait** for confirmation before proceeding to Step 4

---

## STEP 4: CREATE `docs/01-plan.md` (STRATEGIC ARCHITECTURE DECISIONS)

### Objective
Document strategic decisions: technology choices, architectural patterns, domain boundaries, and the rationale for each. This is the "why" behind every major choice.

### File Location
```
PROJECT_ROOT/docs/01-plan.md
```

### Instructions for AI Agent

Ask the user:

```
To write docs/01-plan.md, I need:

1. What is the overall architecture style? (Hexagonal, Onion, Clean, Event-Driven, Vertical Slice, etc.)
2. What are the major domains/bounded contexts (per DDD)?
3. For each domain, what are its responsibilities and boundaries?
4. What are the main service/module interactions?
5. What data flows from one domain to another?
6. For each technology choice, why that technology over alternatives?
7. Are there external service dependencies? (APIs, databases, message queues)
8. Describe the deployment topology (monolith, microservices, serverless, hybrid)
9. For each major decision, explain the tradeoff analysis: what did you choose, what did you reject, why?
```

Then create the file:

```markdown
# docs/01-plan.md — Strategic Architecture Decisions

**Project**: [PROJECT_NAME]  
**Date Created**: [TODAY_DATE]  
**Author**: [NAME]  
**Status**: Active (updated as architectural decisions are made)

---

## GLOSSARY (DDD Ubiquitous Language)

[DEFINE KEY TERMS USED THROUGHOUT THIS DOCUMENT]

| Term | Definition | Used In |
|------|-----------|---------|
| [TERM] | [DEFINITION] | |
| [TERM] | [DEFINITION] | |

---

## 1. ARCHITECTURE OVERVIEW

### Design Pattern
**Pattern**: [CLEAN/HEXAGONAL/ONION/EVENT_DRIVEN/VERTICAL_SLICE]  
**Rationale**: [WHY THIS PATTERN?]  
**Tradeoffs**: [WHAT_WE_GAIN] vs [WHAT_WE_LOSE]

### High-Level Architecture Diagram
```
[ASCII DIAGRAM SHOWING MAJOR COMPONENTS AND INTERACTIONS]

Example:
┌─────────────────────────────────────────┐
│         User Interface Layer            │
│  (React / Next.js / Svelte)             │
└──────────────┬──────────────────────────┘
               │ HTTP/REST or GraphQL
               ↓
┌─────────────────────────────────────────┐
│         API Gateway / BFF               │
│  (Express / Fastify / Hapi)             │
└──────┬──────────────────────────────┬───┘
       │                              │
       ↓                              ↓
 ┌──────────────┐          ┌──────────────────┐
 │ Auth Domain  │          │ Content Domain   │
 │  (Protected) │          │  (Public/Private)│
 └──────┬───────┘          └────────┬─────────┘
        │                            │
        └────────────┬───────────────┘
                     ↓
        ┌─────────────────────────────┐
        │    Database Layer           │
        │  (PostgreSQL + Cache Redis) │
        └─────────────────────────────┘
```

---

## 2. DOMAIN DECOMPOSITION (BOUNDED CONTEXTS per DDD)

[Each domain gets its own subsection]

### Domain: [DOMAIN_NAME]

**Purpose**: [ONE_SENTENCE_PURPOSE]

**Responsibilities**:
- [RESPONSIBILITY_1]
- [RESPONSIBILITY_2]

**Owns These Entities**:
- [ENTITY_1]: [DEFINITION]
- [ENTITY_2]: [DEFINITION]

**Ports (Interfaces)**:

*Inbound (How external code calls this domain):*
- `[InterfaceName]`: [PURPOSE] (Protocol: HTTP REST / gRPC / Events)
  - Typical operations: [EXAMPLES]

*Outbound (How this domain calls external code):*
- `[RepositoryInterface]`: [PURPOSE] (Talks to database)
- `[ServiceInterface]`: [PURPOSE] (Calls other domain)
- `[ExternalAPI]`: [PURPOSE] (Integrates with third-party)

**Forbidden Dependencies**:
- ❌ Cannot import from [DOMAIN_X] (reason: circular dependency risk)
- ❌ Cannot access database directly without [REPOSITORY_NAME]
- ❌ Cannot call [EXTERNAL_SERVICE_Y] directly

**Events Emitted**:
- `[EventName]` (when: [WHEN]) → consumed by [CONSUMER_DOMAIN]
- `[EventName]` (when: [WHEN]) → consumed by [CONSUMER_DOMAIN]

**Events Consumed**:
- `[EventName]` from [PRODUCER_DOMAIN] → causes [ACTION]
- `[EventName]` from [PRODUCER_DOMAIN] → causes [ACTION]

**Data Model** (key entities):
```
[Entity Name]
├─ id: UUID (primary key)
├─ attribute: type (description)
├─ attribute: type (description)
└─ relationships to other domains
```

**Key Business Rules** (invariants):
- [INVARIANT_1]: [CONSEQUENCE_IF_VIOLATED]
- [INVARIANT_2]: [CONSEQUENCE_IF_VIOLATED]

**Example BDD Scenario** (Given-When-Then):
```gherkin
Scenario: [SCENARIO_NAME]
  Given [INITIAL_STATE]
  When [ACTION]
  Then [EXPECTED_RESULT]
  And [ADDITIONAL_EXPECTATION]
```

---

### Domain: [DOMAIN_NAME]

[REPEAT STRUCTURE ABOVE FOR EACH DOMAIN]

---

## 3. DATA FLOW & INTEGRATION POINTS

### How Data Flows Through System

```
[SEQUENCE DIAGRAM OR TEXT DESCRIPTION]

Example:
1. User submits form (UI → API Gateway)
2. API Gateway validates request, extracts JWT token
3. JWT sent to Auth domain for verification
4. Auth domain returns user context
5. Request forwarded to Content domain with user context
6. Content domain queries database
7. Response built and returned to UI
```

### Cross-Domain Communication

| From Domain | To Domain | Mechanism | Data Exchanged | Synchronous/Async |
|------------|-----------|-----------|-----------------|-------------------|
| [FROM] | [TO] | [REST/gRPC/EVENT/QUEUE] | [DATA_TYPES] | [SYNC/ASYNC] |
| [FROM] | [TO] | [MECHANISM] | [DATA] | [TYPE] |

---

## 4. TECHNOLOGY DECISIONS & TRADEOFFS

### Frontend Technology

**Decision**: [TECHNOLOGY] version [VERSION]

**Alternatives Considered**:
- [ALTERNATIVE_1]: Pros [+], Cons [-]
- [ALTERNATIVE_2]: Pros [+], Cons [-]

**Why Chosen**: [RATIONALE]  
**Tradeoff**: Gain [WHAT_WE_GET] vs Lose [WHAT_WE_SACRIFICE]  
**Decision Date**: [DATE]  
**Owner**: [WHO_DECIDED]

---

### Backend Framework

**Decision**: [TECHNOLOGY] version [VERSION]

[SAME STRUCTURE AS ABOVE]

---

### Database

**Decision**: [TECHNOLOGY] version [VERSION]

[SAME STRUCTURE AS ABOVE]

---

### Caching Layer

**Decision**: [TECHNOLOGY] version [VERSION]

[SAME STRUCTURE AS ABOVE]

---

### Message Queue / Event Bus

**Decision**: [TECHNOLOGY] version [VERSION]

[SAME STRUCTURE AS ABOVE]

---

### External Integrations

**Service**: [SERVICE_NAME]
- **Purpose**: [WHAT_IT_DOES]
- **Domain**: [WHICH_DOMAIN_USES_IT]
- **Contract**: [URL_TO_API_DOCS_OR_OPENAPI_SPEC]
- **Fallback Strategy**: [WHAT_HAPPENS_IF_SERVICE_DOWN]
- **Rate Limits**: [CONSTRAINTS]

---

## 5. DEPLOYMENT TOPOLOGY

### Architecture Style
[MONOLITH / MICROSERVICES / SERVERLESS / HYBRID]

### Components & Where They Run

| Component | Deployment | Auto-scale? | Failure Mode |
|-----------|------------|------------|--------------|
| [COMPONENT] | [ENVIRONMENT: container/VM/serverless] | [YES/NO] | [WHAT_HAPPENS] |
| [COMPONENT] | [ENVIRONMENT] | [YES/NO] | [WHAT_HAPPENS] |

### Data Persistence Strategy

| Data Type | Storage | Backup | Replication | GDPR Compliance |
|-----------|---------|--------|------------|-----------------|
| [DATA] | [WHERE] | [HOW] | [STRATEGY] | [METHOD] |

---

## 6. SCALABILITY & PERFORMANCE TARGETS

### Expected Load

- **Concurrent users**: [NUMBER]
- **Requests per second**: [NUMBER] peak
- **Data volume**: [SIZE] at launch, [SIZE] at year 1

### Performance Targets

| Operation | Target | How Measured | Alert Threshold |
|-----------|--------|-------------|-----------------|
| [API_ENDPOINT] | <[TIME]ms | [TOOL] | >[TIME]ms |
| [QUERY] | <[TIME]ms | [TOOL] | >[TIME]ms |
| [BACKGROUND_JOB] | completes in <[TIME]min | [TOOL] | >[TIME]min |

### Scaling Strategy

- **Horizontal**: [WHAT_SCALES_HORIZONTALLY]
- **Vertical**: [WHAT_MUST_SCALE_VERTICALLY]
- **Caching**: [WHAT_IS_CACHED_WHERE]
- **Database**: [SHARDING/REPLICATION/PARTITIONING_STRATEGY]

---

## 7. SECURITY ARCHITECTURE

### Authentication

**Approach**: [OAuth2 / JWT / Session-based / Multi-factor]  
**Provider**: [SERVICE_OR_SELF_HOSTED]  
**Token Lifetime**: [DURATION]  
**Refresh Strategy**: [HOW_TOKENS_REFRESH]

### Authorization

**Model**: [RBAC / ABAC / FINE_GRAINED]  
**Enforcement Points**: [WHERE_CHECKED]

### Data Protection

- **Encryption at rest**: [ALGORITHM] (See `docs/03-architecture.md` for implementation)
- **Encryption in transit**: [PROTOCOL: TLS1.3]
- **Sensitive data handling**: [APPROACH]

### API Security

- **Rate limiting**: [LIMITS_PER_ENDPOINT]
- **CORS policy**: [DOMAINS_ALLOWED]
- **API key rotation**: [FREQUENCY]

---

## 8. ERROR HANDLING & RESILIENCE

### Failure Modes & Mitigation

| Failure Scenario | Impact | Detection | Recovery |
|-----------------|--------|-----------|----------|
| [FAILURE] | [CONSEQUENCE] | [HOW_DETECTED] | [MITIGATION] |
| Database unavailable | Users can't write | Health check fails | Fallback to cache, queue writes |

### Retry Strategy

- **Transient errors**: Retry up to [N] times with exponential backoff
- **Permanent errors**: Log and alert, do not retry
- **Timeout**: [DURATION] per operation

### Graceful Degradation

[DESCRIBE WHAT FUNCTIONALITY REMAINS IF CERTAIN SYSTEMS FAIL]

---

## 9. OBSERVABILITY REQUIREMENTS

### Logging

- **Level**: [DEBUG/INFO/WARN/ERROR] in production
- **Format**: [JSON/STRUCTURED/TEXT]
- **Retention**: [DURATION]
- **Mandatory fields**: trace_id, user_id, service_name, timestamp, severity

### Metrics

- **Collected by**: [PROMETHEUS/CLOUDWATCH/NEW_RELIC]
- **Key metrics**:
  - Request latency (p50, p95, p99)
  - Error rate
  - Database query performance
  - Cache hit rate

### Tracing

- **Tool**: [JAEGER/ZIPKIN/DATADOG]
- **Sample rate**: [PERCENTAGE]
- **Includes**: Service calls, database queries, external API calls

### Alerting

- **Tool**: [PAGERDUTY/OPSGENIE/SPLUNK]
- **Alert rules**: [DEFINE_KEY_ALERTS]

---

## 10. API CONTRACTS (FORMAL)

### API: [API_NAME]

**Protocol**: [REST / GraphQL / gRPC]  
**Base URL**: [PLACEHOLDER_URL]  
**Authentication**: [JWT / API_KEY]  
**Documentation**: [LINK_TO_OPENAPI_SPEC_OR_GRAPHQL_SCHEMA]

**Key Endpoints**:
- `[METHOD] [PATH]`: [PURPOSE]
- `[METHOD] [PATH]`: [PURPOSE]

**Example Request/Response**:
```
Request:
POST /api/v1/[resource]
Content-Type: application/json
Authorization: Bearer [token]

{
  "field1": "value",
  "field2": 123
}

Response (200 OK):
{
  "id": "uuid",
  "field1": "value",
  "created_at": "ISO8601_timestamp"
}

Response (400 Bad Request):
{
  "error": "VALIDATION_ERROR",
  "details": {"field2": "must be a positive integer"}
}
```

**Error Codes**:
- `400 Bad Request`: [WHEN]
- `401 Unauthorized`: [WHEN]
- `403 Forbidden`: [WHEN]
- `404 Not Found`: [WHEN]
- `429 Too Many Requests`: [WHEN]
- `500 Internal Server Error`: [WHEN]

---

## 11. ARCHITECTURAL DECISION LOG

Each major decision is recorded with context.

### ADR-001: [DECISION_TITLE]

**Date**: [DATE]  
**Status**: [ACCEPTED / REJECTED / SUPERSEDED_BY_ADR_XXX]  
**Context**: [WHY_WE_NEEDED_TO_DECIDE]  
**Decision**: [WHAT_WE_CHOSE]  
**Rationale**: [WHY_THIS_OVER_ALTERNATIVES]  
**Consequences**: [WHAT_CHANGED_AS_A_RESULT]  
**Related ADRs**: [LINKS_TO_RELATED_DECISIONS]

---

### ADR-002: [DECISION_TITLE]

[REPEAT STRUCTURE]

---

## 12. DEPENDENCIES & VERSIONS

### Critical Dependencies

| Dependency | Version | Reason | Upgrade Policy |
|-----------|---------|--------|-----------------|
| [DEP] | [VERSION] | [WHY_THIS_VERSION] | [WHEN_UPDATE] |

### Known Vulnerabilities & Mitigations

[IF_ANY_CRITICAL_DEPENDENCIES_HAVE_KNOWN_ISSUES, LIST THEM AND MITIGATIONS]

---

## 13. MIGRATION PATH (IF REPLACING EXISTING SYSTEM)

[IF_THIS_PROJECT_REPLACES_LEGACY_SYSTEM, DESCRIBE THE MIGRATION STRATEGY]

---

## 14. PERFORMANCE BENCHMARKS & TARGETS

### Current Baselines (if applicable)
- [METRIC]: [BASELINE_VALUE]

### Target Performance
- [METRIC]: [TARGET_VALUE] (by [DATE])

### How We'll Measure
- [TOOL_AND_METHODOLOGY]

---

## 15. OPEN QUESTIONS & FUTURE DECISIONS

Questions that will be answered during development:

- [ ] [QUESTION_1]: Will investigate during [PHASE]
- [ ] [QUESTION_2]: Will spike in [WEEK_X]

---

## NEXT STEPS

1. Review and approve this plan with team
2. Use this to guide `docs/02-tasks.md` task breakdown
3. Update `docs/03-architecture.md` with implementation details
4. Update `docs/04-changelog.md` when any decision changes

---

**End of docs/01-plan.md**
```

### Agent Instructions

After generating:

1. **Confirm** file created at `PROJECT_ROOT/docs/01-plan.md`
2. **Display** file to user for review
3. **Ask**: "Does this capture all major architectural decisions and rationale? Any gaps or corrections?"
4. **Wait** for confirmation before proceeding to Step 5

---

## STEP 5: CREATE `docs/02-tasks.md` (GRANULAR EXECUTION BREAKDOWN)

### Objective
Break down the architecture and features from `docs/01-plan.md` into granular, actionable tasks that can be assigned to AI agents or developers. Each task should take 15-45 minutes and have clear completion criteria.

### File Location
```
PROJECT_ROOT/docs/02-tasks.md
```

### Instructions for AI Agent

Ask the user:

```
To write docs/02-tasks.md, I need:

1. What are the core features to build? (List them)
2. What is the priority order?
3. For each feature, what are the implementation steps?
4. What dependencies exist between features? (Feature X must be done before Feature Y)
5. What Phase 1 (MVP) includes vs Phase 2, 3, etc.?
6. For each task, what are success criteria?
```

Then create:

```markdown
# docs/02-tasks.md — Execution Roadmap & Task Breakdown

**Project**: [PROJECT_NAME]  
**Date Created**: [TODAY_DATE]  
**Status**: [IDEATION/PLANNING/PHASE_1_IN_PROGRESS]  
**Owner**: [PM_OR_LEAD_DEVELOPER]

---

## OVERVIEW

This document breaks the architecture from `docs/01-plan.md` into granular tasks. Each task:
- Takes 15-45 minutes (delegable to AI agent or junior developer)
- Has clear completion criteria (how we know it's done)
- Lists dependencies (what must be done first)
- Belongs to a phase (MVP / Phase 2 / etc.)

**Task Progress**: [N] of [TOTAL] complete

---

## PHASE 1: MVP (CRITICAL PATH)

**Target Completion**: [DATE]  
**Acceptance**: [MVP_DEFINITION]

---

### Domain: [DOMAIN_NAME]

#### Task 1.1: [TASK_NAME]

**Description**: [ONE_SENTENCE_PURPOSE]

**Type**: [FEATURE / INFRASTRUCTURE / TESTING / DOCUMENTATION / REFACTORING]

**Depends On**:
- Task 0.1: [WHAT_MUST_COME_FIRST]
- Task 1.0: [PREREQUISITE]

**Acceptance Criteria**:
- [ ] [SPECIFIC_CRITERION_1]
- [ ] [SPECIFIC_CRITERION_2]
- [ ] [SPECIFIC_CRITERION_3]
- [ ] Code passes all 7 quality gates (see `AGENTS.md` section 8)
- [ ] Update `docs/04-changelog.md` with what was implemented and why

**Implementation Notes**:
- Follow patterns in `src/domain/example.file` (see `docs/06-rules.md` for rules)
- Use BDD scenario from `docs/01-plan.md` Domain section as test spec
- Consult `docs/03-architecture.md` for [DOMAIN] forbidden dependencies
- This task is [CRITICAL / HIGH_PRIORITY / NICE_TO_HAVE]

**Estimated Time**: 20 minutes

**Assigned To**: [NAME_OR_UNASSIGNED]

**Status**: [ ] Not Started | [ ] In Progress | [ ] Blocked | [ ] Complete

---

#### Task 1.2: [TASK_NAME]

[REPEAT STRUCTURE]

---

### Domain: [DOMAIN_NAME]

[REPEAT DOMAIN SECTION]

---

## PHASE 2: [PHASE_NAME]

**Target Completion**: [DATE]  
**Acceptance**: [DEFINITION]

---

### Task 2.1: [TASK_NAME]

[REPEAT STRUCTURE]

---

## BLOCKED TASKS

Tasks that cannot start due to external dependencies:

| Task | Blocking Issue | Expected Resolution | Owner |
|------|-----------------|-------------------|-------|
| [TASK] | [ISSUE] | [DATE] | [WHO] |

---

## QUICK REFERENCE: Task Assignment Matrix

| Phase | Domain | Count | Complete | In Progress | Blocked |
|-------|--------|-------|----------|-------------|---------|
| Phase 1 | [DOMAIN] | N | N | N | N |
| Phase 1 | [DOMAIN] | N | N | N | N |

---

**End of docs/02-tasks.md**
```

### Agent Instructions

After generating:

1. **Confirm** file created
2. **Display** for review
3. **Ask**: "Does this capture all necessary tasks with clear acceptance criteria? Any gaps?"
4. **Wait** for confirmation

---

## STEP 6: CREATE REMAINING DOCUMENTATION FILES

### 6a. CREATE `docs/03-architecture.md`

**Purpose**: Detailed architecture documentation including component interactions, file tree structure, domain boundaries, and forbidden dependencies.

[Use similar template structure as Step 4 but focus on implementation architecture, not strategic decisions. Include:
- File tree structure
- Component responsibilities
- Forbidden dependencies (explicit)
- Port/adapter interfaces
- Database schema (high-level)
- Example code locations for patterns]

### 6b. CREATE `docs/04-changelog.md`

**Purpose**: Development log recording what changed, WHY, and lessons learned.

```markdown
# docs/04-changelog.md — Development Changelog & Institutional Memory

**Project**: [PROJECT_NAME]  
**Owner**: [PROJECT_LEAD]  
**Updated**: [TODAY_DATE]

---

## PURPOSE

This is NOT a traditional changelog. This is institutional memory—the "why" behind changes, lessons learned, and decisions made during development. Prevents repeating mistakes.

---

## BOOTSTRAP PHASE (Today)

### [TODAY_DATE] — Project Bootstrap

**What Changed**: Initial project documentation created per Forge Method

**Why**: Establish clear governance, specifications, and validation criteria before writing code

**What We Learned**: [WILL_FILL_AS_DEVELOPMENT_PROGRESSES]

**Decisions Made**:
- Architecture style chosen: [STYLE]
- Technology stack locked: [VERSIONS]
- Team roles assigned: [WHO_OWNS_WHAT]

**Related Tasks**: All of Phase 0

---

## PHASE 1 (FUTURE)

[WILL_ADD_ENTRIES AS_DEVELOPMENT_PROGRESSES]

### [DATE] — [Feature/Fix/Refactor Name]

**What Changed**: [WHAT_WAS_IMPLEMENTED]

**Why**: [BUSINESS_REASON_OR_TECHNICAL_PROBLEM_SOLVED]

**How It Works**: [BRIEF_TECHNICAL_EXPLANATION]

**What We Learned**: [LESSONS_FOR_FUTURE]

**Challenges Encountered**: [WHAT_WENT_WRONG_AND_HOW_WE_FIXED_IT]

**Related Tasks**: Task X.Y

---

**End of docs/04-changelog.md**
```

### 6c. CREATE `docs/05-ideas.md`

**Purpose**: Parking lot for ideas that may become features but aren't planned yet.

```markdown
# docs/05-ideas.md — Future Features & Ideas Parking Lot

**Project**: [PROJECT_NAME]

---

## SCHEDULING SYMBOLS

- `[CONSIDER]`: Interesting idea, not evaluated yet
- `[INVESTIGATION]`: Worth deeper analysis
- `[SCHEDULED_FOR_PHASE_X]`: Planned for future phase
- `[BLOCKED]`: Waiting on something external
- `[REJECTED]`: Decided not to do, with reason documented

---

## IDEAS

### [DATE] — [Idea Name]

**Description**: [WHAT_IS_THE_IDEA]

**Potential Value**: [WHY_CONSIDER_IT]

**Implementation Effort**: [ESTIMATE: SMALL/MEDIUM/LARGE]

**Status**: [CONSIDER/INVESTIGATION/SCHEDULED/BLOCKED/REJECTED]

**Notes**: [ADDITIONAL_CONTEXT]

---

**End of docs/05-ideas.md**
```

### Agent Instructions for 6a-6c

After creating each file:
1. Confirm creation
2. Display for review
3. Get approval
4. Proceed to next file

---

## STEP 7: CREATE `docs/06-rules.md` + Configuration Files

### 7a. CREATE `docs/06-rules.md` (MANDATORY PATTERNS)

**Purpose**: Explicit patterns that all code must follow, with both correct and incorrect examples.

```markdown
# docs/06-rules.md — Mandatory Code Patterns & Rules

**Project**: [PROJECT_NAME]  
**Owner**: [TECH_LEAD]  
**Last Updated**: [TODAY_DATE]  
**Enforcement**: All code must comply. Violations require [ESCALATION_AUTHORITY] override.

---

## QUICK REFERENCE: Rule Categories

| Category | Count | Enforcement |
|----------|-------|-------------|
| [CATEGORY_1] | N rules | [AUTOMATED/MANUAL] |
| [CATEGORY_2] | N rules | [AUTOMATED/MANUAL] |

---

## RULE SET 1: CODE ORGANIZATION

### Rule 1.1: File Structure Reflects Domain Boundaries

**Why It Matters**: Prevents accidental cross-domain imports; enables independent testing

**Correct Pattern** ✅:
```
src/
├─ domains/
│  ├─ auth/
│  │  ├─ models/
│  │  ├─ services/
│  │  ├─ controllers/
│  │  └─ auth.domain.ts (ubiquitous language definitions)
│  └─ content/
│     ├─ models/
│     ├─ services/
│     └─ controllers/
├─ shared/ (only domain-agnostic utilities)
└─ infrastructure/ (database, logging, HTTP layer)
```

**Wrong Pattern** ❌:
```
src/
├─ services/ (mixes Auth and Content services)
├─ models/ (mixes Auth and Content models)
├─ controllers/ (mixes Auth and Content controllers)
```

**How to Verify**: Run command `[TREE_COMMAND]` and ensure no domain crosses folder boundaries

**References**:
- See `src/domains/auth/` for working example
- See `docs/03-architecture.md` section "Domain: Auth" for structure

---

### Rule 1.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## RULE SET 2: TESTING REQUIREMENTS

### Rule 2.1: All Features Must Follow TDD (Test-First)

**Why It Matters**: Tests document expected behavior. Writing tests first prevents misinterpretation.

**Correct Pattern** ✅:
```
1. Write failing test (Red)
   - Test names describe behavior (should_[verb]_when_[condition])
   - At least one happy path + one error case

2. Write minimal code to pass test (Green)
   - Only implement enough to pass test
   - Don't add features "while I'm here"

3. Refactor while keeping tests passing (Refactor)
   - Extract duplication
   - Improve readability
   - Maintain test coverage >= 85%
```

**Wrong Pattern** ❌:
```
1. Write code first
2. Try to write tests that fit the code
3. Tests become weak or skip edge cases
```

**How to Verify**:
- Run `npm test -- --coverage` and verify >= 85% coverage
- Review git history: commits should show test → code, not code → test

**References**:
- See `tests/domains/auth/user.service.test.ts` for testing pattern
- See `docs/01-plan.md` for BDD scenarios as test specifications

---

### Rule 2.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## RULE SET 3: DEPENDENCY INJECTION & ARCHITECTURE

### Rule 3.1: No Domain Crosses Boundaries; All Imports Are Explicit

**Why It Matters**: Decouples domains, enables testing in isolation, prevents architectural debt

**Correct Pattern** ✅:
```typescript
// auth/services/user.service.ts
import { UserRepository } from '../ports/user.repository'; // Same domain ✅
import { Logger } from '../../infrastructure/logger'; // Shared ✅

// NOT allowed:
// import { ContentService } from '../../domains/content/...'; // ❌ Cross-domain import

constructor(
  private userRepo: UserRepository,
  private logger: Logger
) {}
```

**Wrong Pattern** ❌:
```typescript
// auth/services/user.service.ts
import { ContentService } from '../../domains/content/services/content.service'; // ❌

// Direct instantiation instead of DI:
const userRepo = new UserRepository(); // ❌ No DI
```

**Forbidden Dependencies**: See `docs/03-architecture.md` section "Forbidden Dependencies"

**How to Verify**: ESLint rule (if configured) or manual code review

---

### Rule 3.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## RULE SET 4: API CONTRACTS & VERSIONING

### Rule 4.1: All API Changes Must Update OpenAPI Spec

**Why It Matters**: API contract must be single source of truth. Prevents client breaks.

**Correct Pattern** ✅:
```yaml
# openapi.yaml
paths:
  /api/v1/users/{id}:
    get:
      operationId: getUserById
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
```

**Wrong Pattern** ❌:
```
Code changes are made, but OpenAPI spec not updated
```

**How to Verify**: Run `npm run validate:api` and confirm no spec violations

---

### Rule 4.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## RULE SET 5: ERROR HANDLING & OBSERVABILITY

### Rule 5.1: All Errors Must Log Context + Metrics

**Why It Matters**: Production issues can't be diagnosed without context. Metrics enable alerts.

**Correct Pattern** ✅:
```typescript
try {
  const user = await userRepo.findById(userId);
  if (!user) {
    this.logger.warn('User not found', {
      userId,
      trace_id: requestContext.traceId,
      timestamp: new Date().toISOString()
    });
    this.metrics.increment('user.not_found', { userId });
    throw new NotFoundError(`User ${userId} not found`);
  }
  return user;
} catch (error) {
  this.logger.error('Failed to fetch user', {
    userId,
    error: error.message,
    stack: error.stack,
    trace_id: requestContext.traceId
  });
  this.metrics.increment('user.fetch.error', { error_type: error.name });
  throw error;
}
```

**Wrong Pattern** ❌:
```typescript
const user = await userRepo.findById(userId);
if (!user) {
  throw new Error('Not found'); // No context, no metrics
}
```

**How to Verify**: Code review + check CloudWatch/Datadog for missing trace_ids

---

### Rule 5.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## RULE SET 6: DATABASE & DATA PERSISTENCE

### Rule 6.1: All Database Access Goes Through Repository Pattern

**Why It Matters**: Decouples domain logic from database implementation. Enables testing with mocks.

**Correct Pattern** ✅:
```typescript
// Inject repository interface
constructor(private userRepo: IUserRepository) {}

// Use only repository methods
const user = await this.userRepo.findById(id);
await this.userRepo.save(user);
```

**Wrong Pattern** ❌:
```typescript
// Direct database access
const user = await db.query('SELECT * FROM users WHERE id = ?', [id]);
const result = await db.execute('UPDATE users SET ...');
```

**References**: See `src/domains/auth/ports/user.repository.ts` for interface definition

---

### Rule 6.2: [RULE_NAME]

[REPEAT STRUCTURE]

---

## FORBIDDEN PATTERNS (NEVER DO THESE)

### Forbidden: Global Variables

**Why**: Makes code unpredictable, impossible to test

**Consequence**: Code review rejection + requirement to refactor

---

### Forbidden: Circular Dependencies

**Why**: Breaks encapsulation, makes testing impossible

**Consequence**: Automated detection via linter + build failure

---

### Forbidden: Direct Database Access in Domain Logic

**Why**: Couples domain to database, violates Clean Architecture

**Consequence**: Architecture review rejection

---

### Forbidden: Hard-Coded Configuration

**Why**: Environment-specific configs can't change without redeployment

**Consequence**: Code review rejection + requirement to externalize

---

## QUALITY GATES CHECKLIST

Before marking a task `[x]` in `docs/02-tasks.md`, verify:

**Pre-Submission Checklist**:
- [ ] All tests written and passing (`npm test`)
- [ ] Coverage >= 85% (`npm test -- --coverage`)
- [ ] Linting passes (`npm run lint`)
- [ ] Type checking passes (`npm run type-check`)
- [ ] No forbidden patterns used (manual review)
- [ ] API contract updated if needed
- [ ] Logging/metrics added per Rule 5.1
- [ ] Documentation updated (inline comments + ADR if needed)
- [ ] Code reviewed against this file (6-rules.md)

**Submission**:
- [ ] Commit message references task ID: "Task 1.2: [description]"
- [ ] Update `docs/04-changelog.md` with what changed and why
- [ ] Mark task `[x]` in `docs/02-tasks.md`

---

## HOW TO USE THIS FILE

1. **Before implementing**: Read relevant rule sets
2. **While implementing**: Reference specific rules as needed
3. **Before submitting**: Run through Quality Gates Checklist
4. **On code review**: Check against rules in this file
5. **To add new rules**: Discuss with [TECH_LEAD], add pattern, update this file

---

**End of docs/06-rules.md**
```

### 7b. CREATE `.cursorignore`

**Purpose**: Tell AI agents what files to ignore (to preserve context window).

```
node_modules/
.git/
.env
.env.local
dist/
build/
coverage/
.next/
.turbo/
*.log
*.pid
.DS_Store
.idea/
.vscode/
*.swp
*.swo
*~
.cache/
temp/
tmp/
[LARGE_FILES_OR_DIRECTORIES]
```

### 7c. CREATE `llms.txt`

**Purpose**: LLM-friendly summary of entire project (for context injection).

```markdown
# Project: [PROJECT_NAME]

## Purpose
[ONE_PARAGRAPH_PROJECT_PURPOSE]

## Key Concepts (Ubiquitous Language)
- [TERM]: [DEFINITION]
- [TERM]: [DEFINITION]

## Architecture
[HIGH_LEVEL_SUMMARY_OF_ARCHITECTURE]

## Domains
[LIST_OF_DOMAINS_AND_RESPONSIBILITIES]

## Technology Stack
- Frontend: [TECH]
- Backend: [TECH]
- Database: [TECH]

## Critical Rules
1. [MOST_IMPORTANT_RULE]
2. [MOST_IMPORTANT_RULE]
3. [MOST_IMPORTANT_RULE]

See docs/06-rules.md for complete rules.

## How to Get Started
1. Read AGENTS.md
2. Read docs/00-draft.md (problem)
3. Read docs/01-plan.md (architecture)
4. Read docs/03-architecture.md (implementation details)
5. Pick a task from docs/02-tasks.md
6. Follow rules in docs/06-rules.md

## Important Files
- AGENTS.md: Project constitution
- docs/02-tasks.md: What to build (with checkboxes)
- docs/06-rules.md: How to build it
- docs/03-architecture.md: Where things live
- docs/04-changelog.md: Why things changed
```

### Agent Instructions

After creating all of 7a-7c:
1. Confirm all files created
2. Display each for review
3. Get approval

---

## STEP 8: VERIFICATION PASS (CROSS-REFERENCE AUDIT)

### Objective
Verify that all files are created, correctly located, and properly cross-referenced.

### Instructions for AI Agent

Run this verification checklist:

```
FILE EXISTENCE AUDIT
──────────────────────────────────────────────

✓ Verify these files exist at PROJECT_ROOT/:
  [ ] AGENTS.md
  [ ] .cursorignore
  [ ] llms.txt

✓ Verify these files exist at PROJECT_ROOT/docs/:
  [ ] 00-draft.md
  [ ] 01-plan.md
  [ ] 02-tasks.md
  [ ] 03-architecture.md
  [ ] 04-changelog.md
  [ ] 05-ideas.md
  [ ] 06-rules.md

CROSS-REFERENCE AUDIT
──────────────────────────────────────────────

✓ AGENTS.md references:
  [ ] Links to docs/00-draft.md
  [ ] Links to docs/01-plan.md
  [ ] Links to docs/02-tasks.md
  [ ] Links to docs/03-architecture.md
  [ ] Links to docs/06-rules.md
  [ ] Section "7. Documentation Structure" accurate
  [ ] Section "8. Quality Gates" references AGENTS.md properly

✓ docs/00-draft.md references:
  [ ] Mentions docs/01-plan.md for decisions
  [ ] Clear problem statement

✓ docs/01-plan.md references:
  [ ] References domains in docs/03-architecture.md
  [ ] References decisions in docs/04-changelog.md
  [ ] Links to docs/02-tasks.md for breakdown
  [ ] ADRs documented

✓ docs/02-tasks.md references:
  [ ] All tasks link to relevant rules in docs/06-rules.md
  [ ] Mentions docs/03-architecture.md forbidden dependencies
  [ ] References BDD scenarios from docs/01-plan.md
  [ ] Each task references quality gates from AGENTS.md

✓ docs/03-architecture.md references:
  [ ] Links to docs/01-plan.md for strategic decisions
  [ ] References domains and ports clearly
  [ ] Lists forbidden dependencies explicitly

✓ docs/04-changelog.md references:
  [ ] Links to tasks completed (Task X.Y)
  [ ] References AGENTS.md for process

✓ docs/05-ideas.md references:
  [ ] Notes scheduling status for each idea

✓ docs/06-rules.md references:
  [ ] Each rule links to example code locations
  [ ] References docs/03-architecture.md forbidden deps
  [ ] Links to TDD/BDD patterns from docs/01-plan.md
  [ ] Quality gates checklist complete

CONTENT COMPLETENESS AUDIT
──────────────────────────────────────────────

✓ AGENTS.md contains:
  [ ] Project purpose and success criteria
  [ ] Technology stack explained
  [ ] Non-negotiable constraints
  [ ] Team roles and responsibilities
  [ ] Quality gates section 8 complete
  [ ] Getting started checklist for new contributors

✓ docs/00-draft.md contains:
  [ ] Problem statement
  [ ] Research sources with links
  [ ] Competitive analysis
  [ ] Assumptions (with confidence levels)
  [ ] Rejected alternatives
  [ ] Success criteria

✓ docs/01-plan.md contains:
  [ ] Architecture diagram (ASCII or text)
  [ ] All domains with responsibilities
  [ ] Data flow between domains
  [ ] Technology decisions with tradeoffs
  [ ] Deployment topology
  [ ] API contracts sketched
  [ ] At least one ADR (Architectural Decision Record)

✓ docs/02-tasks.md contains:
  [ ] Phase 1 (MVP) completely broken down
  [ ] Each task has acceptance criteria
  [ ] Each task has estimated time (15-45 min)
  [ ] Each task lists dependencies
  [ ] Progress tracking matrix
  [ ] No task vague or larger than 45 minutes

✓ docs/03-architecture.md contains:
  [ ] File tree structure
  [ ] All domains mapped
  [ ] Ports & adapters defined
  [ ] Forbidden dependencies explicit
  [ ] Key business rules (invariants) per domain
  [ ] Example code locations for patterns

✓ docs/04-changelog.md contains:
  [ ] Bootstrap entry for today
  [ ] Clear "What Changed, Why, What We Learned" structure
  [ ] Ready for daily updates during development

✓ docs/05-ideas.md contains:
  [ ] At least 3 future ideas with status labels
  [ ] Clear format for adding more

✓ docs/06-rules.md contains:
  [ ] At least 15-20 specific rules
  [ ] Each rule has ✅ correct and ❌ wrong patterns
  [ ] Each rule explains WHY it matters
  [ ] Code examples with actual syntax
  [ ] Quality Gates checklist for submissions
  [ ] Forbidden Patterns section

✓ .cursorignore contains:
  [ ] Excludes node_modules/
  [ ] Excludes .git/
  [ ] Excludes .env and secrets
  [ ] Excludes build/dist directories
  [ ] Excludes any large files (>100MB)

✓ llms.txt contains:
  [ ] One-paragraph project purpose
  [ ] Ubiquitous Language (DDD terminology)
  [ ] High-level architecture
  [ ] Tech stack
  [ ] 3-5 critical rules
  [ ] Getting started steps

TONE & CLARITY AUDIT
──────────────────────────────────────────────

✓ All files:
  [ ] Written in second person ("you") where appropriate
  [ ] Use markdown formatting consistently
  [ ] Include examples for abstract concepts
  [ ] Avoid vague language ("good", "best", "nice")
  [ ] Explain "why" not just "what"
  [ ] Cross-reference other documents extensively

VALIDATION COMPLETE
──────────────────────────────────────────────

If all checks pass, project documentation is complete and ready for:
- AI agents to read and understand project
- Developers to start implementing
- Code generation to begin with full context
```

### Agent Final Instructions

After completing verification:

1. **Create a summary report**:
   ```
   BOOTSTRAP COMPLETE ✓
   
   All [N] documentation files created:
   - [FILE]: [STATUS]
   - [FILE]: [STATUS]
   
   Cross-references: [N]/[TOTAL] verified
   Content completeness: [PERCENTAGE]%
   
   Project ready for code generation.
   ```

2. **Display to user** the summary and any issues found

3. **Ask**: "Is the documentation complete and ready for code generation? Any final corrections needed?"

4. **If approved**, conclude with:
   ```
   FORGE METHOD BOOTSTRAP COMPLETE
   
   All constitutional and specification documentation is now in place.
   
   NEXT STEPS FOR IMPLEMENTATION:
   1. Create initial codebase structure (folders per docs/03-architecture.md)
   2. Start Phase 1 with Task 1.1 from docs/02-tasks.md
   3. Follow TDD: write test → write code → refactor
   4. Maintain docs/04-changelog.md daily
   5. Mark tasks [x] when complete
   6. Run quality gates before submission
   
   AI Agent guidance: Read AGENTS.md first, then the documentation stack.
   All rules to follow are in docs/06-rules.md.
   ```

---

## END OF FORGE BOOTSTRAP PROMPT

This prompt has established a complete, interconnected documentation framework for [PROJECT_NAME] using the Forge Method.

The documentation serves as the operating system for all future code generation. AI agents and developers have:

✅ **Constitutional guidance** (AGENTS.md)  
✅ **Problem context** (docs/00-draft.md)  
✅ **Strategic decisions** (docs/01-plan.md)  
✅ **Executable tasks** (docs/02-tasks.md)  
✅ **Implementation map** (docs/03-architecture.md)  
✅ **Institutional memory** (docs/04-changelog.md)  
✅ **Future ideas** (docs/05-ideas.md)  
✅ **Mandatory rules** (docs/06-rules.md)  
✅ **Context filtering** (.cursorignore)  
✅ **LLM-friendly summary** (llms.txt)  

All files are cross-referenced. No ambiguity about governance, specification, or validation.

**All code generation can now proceed with high confidence of consistency.**
