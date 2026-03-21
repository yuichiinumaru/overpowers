---
name: rust-review
description: Multi-tiered Rust-specific code review protocol. Use for auditing ownership safety, async cancellation safety, lifetime variance, and memory-safe abstractions.
tags:
  - rust
  - review
  - safety
  - async
version: 2.0.0
category: coding
subtype: review
---

# Rust Code Review Engineering Standard

Multi-tiered protocol for reviewing Rust code with maximum rigor and minimum reviewer fatigue. Identifies irreducible safety truths (axioms), common vulnerability areas (heat maps), and proves correctness via structural invariant audits.

## When to Use

- Reviewing PRs or changesets in Rust projects
- Auditing `unsafe` blocks, FFI boundaries, or async code
- Performing pre-merge safety verification
- Evaluating library dependencies for soundness
- Assessing code quality against a 0-100 scoring rubric

## Core Axioms (Non-Negotiable)

Every review starts by checking these five irreducible truths:

| # | Axiom | Violation = | Check |
|---|-------|-------------|-------|
| 1 | **Ownership** | Aliasing + Mutation = UB | Every `&mut` is exclusive; no shared mutability without `Cell`/`Mutex` |
| 2 | **Type-State** | Invalid states are representable | Use enums/newtypes to make impossible states uncompilable |
| 3 | **Zero-Cost** | Runtime penalty from abstraction | No unnecessary `Box`, `dyn Trait`, or allocation where static dispatch suffices |
| 4 | **Safety Boundary** | Missing `// SAFETY:` | Every `unsafe` block MUST have a `// SAFETY:` comment justifying invariants |
| 5 | **Cancellation Safety** | Resource leak on `Future` drop | Any `.await` point must be safe to drop — use RAII/`Drop` guards for rollback |

## Phase 1: Security Heat Map (Adversarial Audit)

Audit these high-risk areas for logic and memory exploits:

### 1.1 Unsound Safe Abstractions
- Does a `pub` API hide an `unsafe` block that could be violated by specific input combinations?
- Can a caller construct inputs that break the `unsafe` block's preconditions?

### 1.2 FFI Boundary Fragility
- Audit every `extern "C"` block
- Ensure raw pointer wrappers correctly implement `Send`/`Sync` (or explicitly opt out)
- Check for null pointer dereference in FFI return values
- Verify lifetime of data passed across the FFI boundary

### 1.3 Async Race Conditions (TOCTOU)
- Check for logic-level races in `tokio::spawn` or `async_std::task::spawn`
- Pattern: state is checked, then `.await`, then state is used — the state may have changed
- Use `ast-grep` to find TOCTOU candidates:

```bash
# Find spawned tasks that capture mutable references
sg -p 'tokio::spawn(async move { $$$BODY })' -l rust

# Find select! blocks (cancellation hazard zones)
sg -p 'tokio::select! { $$$ARMS }' -l rust
```

### 1.4 Lifetime Variance
- Types wrapping `&T` in `Cell`/`UnsafeCell` must be **invariant**, not covariant
- Audit generic parameters on structs containing raw pointers
- Check for `PhantomData` usage (or lack thereof) on types with lifetime parameters

## Phase 2: Async Cancellation Safety Audit

For every `async fn` or `select!` block, perform a **Drop-Proof Audit**:

### Checklist

- [ ] If this task is dropped at each `.await` point, does it leak resources?
- [ ] Is there a `Drop` guard that rolls back partial writes?
- [ ] Are database transactions wrapped in a guard that aborts on drop?
- [ ] Do `select!` branches clean up the losing branch's side effects?
- [ ] Are `tokio::sync::Mutex` guards held across `.await` points? (deadlock risk)

### ast-grep Patterns for Cancellation Hazards

```bash
# Find async fns with multiple await points (higher cancellation surface)
sg -p 'async fn $NAME($$$PARAMS) $RET { $$$BODY }' -l rust

# Find mutex guards held across await (deadlock risk)
sg -p 'let $GUARD = $MUTEX.lock().await' -l rust
```

## Phase 3: Idiomatic & Zero-Cost Audit

### Error Handling
- [ ] No `unwrap()` or `expect()` in production paths (test-only is acceptable)
- [ ] Error types use `thiserror` (library) or `anyhow` (application)
- [ ] Error context is preserved via `.context()` or `.map_err()`
- [ ] No silent error swallowing (`let _ = fallible_op()`)

### Allocations & Performance
- [ ] No unnecessary `Box<dyn Trait>` when `impl Trait` or generics suffice
- [ ] No redundant `.clone()` — check if borrowing is possible
- [ ] `String` vs `&str` — prefer borrowed unless ownership is needed
- [ ] `Vec` pre-allocation with `Vec::with_capacity()` for known sizes
- [ ] No `collect()` into intermediate `Vec` when iterator chaining suffices

### ast-grep Patterns for Idiomatics

```bash
# Find all unwrap() calls
sg -p '$EXPR.unwrap()' -l rust

# Find all expect() calls
sg -p '$EXPR.expect($MSG)' -l rust

# Find Box<dyn Trait> (potential static dispatch candidate)
sg -p 'Box<dyn $TRAIT>' -l rust

# Find unnecessary clones
sg -p '$EXPR.clone()' -l rust
```

## Phase 4: Logical Proof Architecture

Instead of guessing, build a proof for critical invariants:

### Steps
1. **Define Invariant**: State the rule (e.g., "Struct X is always sorted after construction")
2. **Audit Boundary**: Verify all mutation paths (`&mut self` methods) enforce the rule
3. **Proof of Soundness**: Document why the implementation physically prevents violations
4. **Type-Level Encoding**: Where possible, use the type system to make violations uncompilable

### Template

```markdown
### Invariant: [Name]
- **Rule**: [What must always be true]
- **Mutation Points**: [List all `&mut self` methods that could break it]
- **Enforcement**: [How each mutation point preserves the invariant]
- **Proof**: [Why it is impossible to violate — or what `unsafe` justification exists]
```

## Scoring Rubric (0-100)

| Range | Level | Criteria |
|-------|-------|----------|
| 0-30 | **Critical** | Safety axiom violations: missing `// SAFETY:`, unsound safe wrappers, memory unsafety |
| 31-50 | **Serious** | Logic-level TOCTOU, unchecked FFI returns, silent error swallowing |
| 51-70 | **Debt** | Zero-Cost violations (excessive allocs), non-idiomatic error handling, missing tests |
| 71-85 | **Good** | Safe and performant, but missing cancellation audit or variance analysis |
| 86-99 | **Elite** | Everything audited, minor improvements possible (docs, naming, test coverage) |
| 100 | **Perfect** | Most constrained proof possible, documented Proof of Soundness, all invariants type-encoded |

## Output Format

```markdown
## Rust Review: [Module / PR Name]

### Score: [0-100] — [Level]

### Axiom Compliance
| Axiom | Status | Notes |
|-------|--------|-------|
| Ownership | ✅/❌ | [Details] |
| Type-State | ✅/❌ | [Details] |
| Zero-Cost | ✅/❌ | [Details] |
| Safety Boundary | ✅/❌ | [Details] |
| Cancellation Safety | ✅/❌ | [Details] |

### Findings
#### Critical (Score < 50)
- [Finding with file:line reference]

#### Debt (Score 50-80)
- [Finding with file:line reference]

#### Improvements (Score 80-99)
- [Finding with file:line reference]

### Proofs of Soundness
[For each critical invariant, the proof template filled in]

### Path to 100
[Prioritized list of changes needed to reach perfect score]
```

## Tool Integration

- **`ast-grep` / `sg`**: Structural search for patterns listed above (see `skills/coding/review/ast-grep`)
- **`cargo clippy --all-targets --all-features -- -D warnings`**: Tier 1 lint gate
- **`cargo audit`**: Known vulnerability scan
- **`cargo deny check`**: License and advisory check
- **`cargo-geiger`**: Unsafe density measurement
- **`cargo-expand`**: Macro expansion audit (filter with `grep` to avoid context bloat)

## Integration with Other Skills

- **`skills/coding/review/ast-grep`** — Structural search patterns and YAML rule definitions
- **`skills/reasoning/first-principles`** — First-principles decomposition for architectural decisions
- **`skills/anti-hallucination`** — Verify technical claims about safety properties
- **`skills/research-protocol`** — Research Rust RFCs or unstable features before recommending
