---
description: Multi-tiered Rust review workflow including deterministic automata, surgical structural audits, and deep domain reasoning.
argument-hint: Path to the Rust crate or specific file(s) to review.
---

# /ovp-rust-review — Rust Code Quality Workflow

**Goal**: Achieve a **perfect 100/100** Rust code quality score through a three-tier system that eliminates reviewer fatigue by automating what can be automated (Tiers 1-2) and focusing human/agent reasoning on what only intelligence can catch (Tier 3).

> [!IMPORTANT]
> This workflow invokes the `ovp-rust-code-reviewer` agent for Tier 3.
> Ensure the agent definition exists at `agents/ovp-rust-code-reviewer.md`.
> The agent uses the skill at `skills/coding/review/rust-review/SKILL.md`.

## Steps

### 1. Tier 1: Deterministic Automata (The Gate)

Run all lint and audit tools. If any fail, the review stops immediately — no cognitive energy is spent on unpolished code.

```bash
# Lint with all warnings as errors
cargo clippy --all-targets --all-features -- -D warnings

# Known vulnerability scan
cargo audit

# License and advisory check
cargo deny check
```

> [!CAUTION]
> **Exit Strategy**: If ANY command above returns a non-zero exit code, STOP HERE.
> Report: `FAIL (Tier 1) — [tool name]: [error summary]`.
> Do NOT proceed to Tier 2 until Tier 1 is clean.

### 2. Tier 2: Surgical Structural Audit (Hotspot Identification)

Use structural search tools to identify high-risk areas that require deep reasoning.

#### 2.1 Unsafe Block Inventory

```bash
# Find all unsafe blocks
sg -p 'unsafe { $$$BODY }' -l rust

# Find unsafe blocks WITHOUT a preceding SAFETY comment
# (manual review — check for // SAFETY: above each match)
sg -p 'unsafe { $$$BODY }' -l rust --json | head -50
```

#### 2.2 Async Cancellation Surfaces

```bash
# Find all async functions
sg -p 'async fn $NAME($$$PARAMS) $RET { $$$BODY }' -l rust

# Find tokio::spawn calls (concurrency entry points)
sg -p 'tokio::spawn($FUTURE)' -l rust

# Find select! blocks (cancellation danger zones)
sg -p 'tokio::select! { $$$ARMS }' -l rust

# Find mutex guards that might be held across await
sg -p 'let $GUARD = $MUTEX.lock().await' -l rust
```

#### 2.3 Idiomatic Problem Patterns

```bash
# Find unwrap() in non-test code
sg -p '$EXPR.unwrap()' -l rust

# Find expect() calls  
sg -p '$EXPR.expect($MSG)' -l rust

# Find Box<dyn Trait> (possible static dispatch candidates)
sg -p 'Box<dyn $TRAIT>' -l rust

# Find .clone() calls (possible unnecessary copies)
sg -p '$EXPR.clone()' -l rust
```

#### 2.4 Unsafe Density Report

```bash
# Run cargo-geiger for unsafe usage statistics
cargo geiger --output-format ascii 2>&1 | head -100
```

#### 2.5 Macro Expansion Audit (if macros found)

```bash
# Expand macros for a specific module and filter to the relevant struct/fn
cargo expand module_name 2>/dev/null | grep -A 50 'fn target_function'
```

**Output of Tier 2**: A list of **Hotspots** — specific files, functions, unsafe blocks, and async patterns that require deep analysis. Document them as:

```markdown
## Hotspots for Tier 3
- [ ] `src/foo.rs:42` — unsafe block without SAFETY comment
- [ ] `src/bar.rs:100` — tokio::spawn with shared mutable state
- [ ] `src/baz.rs:200` — select! with 3 branches, cancellation risk
- [ ] `src/lib.rs:50` — Box<dyn Handler> potential static dispatch
```

### 3. Tier 3: Domain & Logic Audit (Agentic)

**Agent**: Invoke `ovp-rust-code-reviewer` with the Hotspot list from Tier 2.

**Provide the agent with**:
1. The Hotspot list from Tier 2
2. The relevant source files
3. Any module dependency context (callers, dependents)

The agent will:
- Perform adversarial simulation on each Hotspot
- Verify invariants using the Proof Architecture
- Score the code 0-100
- Produce a report with a **Path to 100**

### 4. Implementation & Iteration

Based on the reviewer's report:

1. **Critical findings (score < 50)**: Fix immediately — these are safety issues
2. **Debt findings (score 50-80)**: Fix in this cycle — these are quality issues
3. **Elite findings (score 80-99)**: Fix if time permits — these improve perfection

**For each fix**:
- Implement the specific change recommended in the report
- Ensure the fix includes a `// SAFETY:` comment or Proof of Soundness as applicable
- Add or update tests covering the fixed area

### 5. The Perfection Loop

After implementing fixes, repeat from **Step 1** (Tier 1).

> [!WARNING]
> **Iteration Limit**: Maximum **3 full loops** (Tier 1 → Tier 2 → Tier 3 → Fix → Repeat).
> If score has not reached 100 after 3 loops, report the current score and remaining Path to 100.
> The user decides whether to continue or accept the current score.

**Loop exit conditions** (any one):
- Score reaches **100/100**
- **3 iterations** completed
- No new findings between consecutive iterations (plateau)

## Verification

Success is achieved when ALL of the following are true:
- Tier 1 passes with zero warnings
- Tier 3 results in a **100/100 score** (or maximum 3 iterations completed)
- All `unsafe` blocks have verified `// SAFETY:` justification
- All async cancellation points have documented drop safety
- A final report is produced following the Output Format from the `rust-review` skill
