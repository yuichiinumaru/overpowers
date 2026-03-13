---
name: byterover-debug
description: "Investigate bugs using scientific method with persistent knowledge. Queries known issues and past bug fixes, applies hypothesis-driven investigation, and stores root cause analysis and fix patterns via brv curate for future reference."
---

# ByteRover Systematic Debugging

A structured workflow for investigating bugs using the scientific method, enhanced by ByteRover's knowledge of past issues and project patterns.

## When to Use

- When encountering a bug or unexpected behavior
- When a test fails unexpectedly
- When behavior does not match documented expectations
- When debugging a regression

## Prerequisites

Run `brv status` first. If errors occur, instruct the user to resolve them in the brv terminal. See the byterover skill's TROUBLESHOOTING.md for details.

The user must describe the symptom: what happened and what was expected.

## Process

### Phase 1: Query Known Issues

Before investigating, check if this problem (or something similar) has been seen before:

```bash
brv query "Are there known bugs or past fixes related to [affected area/symptom]?"
brv query "What is the architecture and implementation of [affected module]?"
brv query "What error handling patterns are used in [affected area]?"
```

If ByteRover returns a past fix for a similar symptom, check if the same root cause applies before investigating from scratch.

### Phase 2: Gather Evidence

Record precise symptoms — do not skip this step:

- **Expected behavior:** What should happen
- **Actual behavior:** What actually happens
- **Error messages:** Exact text, stack traces, log output
- **Reproduction steps:** How to trigger the bug
- **Scope:** Does it always happen, or only under specific conditions?

Read the relevant source files **completely**. Do not skim. Understanding the full context prevents false hypotheses.

### Phase 3: Form Hypotheses

Based on evidence and known patterns, form 2-3 specific, falsifiable hypotheses:

Each hypothesis must:
- Be **specific** — "The auth middleware skips validation when token is expired" not "auth is broken"
- Be **falsifiable** — There must be a way to prove it wrong
- **Predict an observable outcome** — "If this hypothesis is correct, then [X] should be true"

Rank hypotheses by likelihood, considering:
- Evidence strength (does data support it?)
- Past knowledge (have similar bugs occurred?)
- Simplicity (simpler explanations are more likely)

Example:
```
Hypothesis 1 (HIGH likelihood): Race condition in useEffect cleanup —
  the fetch completes after component unmounts.
  Prediction: Adding AbortController should prevent the stale data.

Hypothesis 2 (MEDIUM likelihood): Cache returning stale entry —
  the cache TTL is too long for this data type.
  Prediction: Clearing cache should show fresh data.

Hypothesis 3 (LOW likelihood): API returning incorrect data —
  the backend filter is wrong.
  Prediction: Direct API call should return wrong results too.
```

### Phase 4: Test Hypotheses

Test one hypothesis at a time. For each:

1. **Change one variable** — Make the minimal change to test this hypothesis
2. **Observe the result** — Does the prediction hold?
3. **Document the finding** — Record what was tested and what happened

If **confirmed**: Proceed to Phase 5 with this root cause.
If **eliminated**: Record why it was eliminated (prevents re-investigation) and move to the next hypothesis.

**Never change multiple things at once.** If a fix happens to work but you changed two things, you don't know which one fixed it — and the other change might cause problems later.

### Phase 5: Root Cause and Fix

Once the root cause is confirmed:

1. **Document the root cause** — Why does this happen? What's the mechanism?
2. **Apply the minimal fix** — Fix the root cause, not the symptom
3. **Verify the fix** — Confirm the original symptom is resolved
4. **Run regression tests** — Ensure the fix doesn't break other things

```bash
# Run relevant tests
npm test -- --grep "[affected area]"
# Or run the full test suite if the change is broad
npm test
```

### Phase 6: Curate for Future Reference

Store the debugging knowledge so future sessions can benefit:

```bash
brv curate "Bug: [symptom description]. Root cause: [why it happened]. Fix: [what was changed]. Pattern: [general lesson for similar bugs]" -f [affected files]
```

Include:
- What the symptom looked like (so future queries match)
- The confirmed root cause (not the hypotheses that were eliminated)
- The fix applied (specific changes)
- A general pattern or lesson (applicable beyond this specific bug)

Example:
```bash
brv curate "Bug: stale data after rapid navigation between pages. Root cause: useEffect cleanup not cancelling in-flight fetch requests. Fix: added AbortController with cleanup in useEffect return. Pattern: always abort async operations in useEffect cleanup to prevent state updates on unmounted components" -f src/hooks/useUserData.ts
```

### Completion

Report to the user:
1. **Root cause** — What caused the bug (with evidence)
2. **Fix applied** — What was changed and where
3. **Verification** — Test results confirming the fix
4. **Knowledge stored** — What was curated for future reference
5. **Eliminated hypotheses** — What was ruled out (for transparency)

## Important Rules

1. **Never guess** — Form hypotheses and test them; don't apply random fixes
2. **One variable at a time** — Change one thing, observe, document
3. **Read files completely** — Do not skim; missing context leads to wrong hypotheses
4. **Document eliminations** — Record why each hypothesis was eliminated to prevent re-investigation
5. **Check knowledge first** — Query known issues before investigating from scratch
6. **Always curate** — Store findings even for trivial bugs; they build institutional memory
7. **Fix the cause, not the symptom** — A try/catch that swallows the error is not a fix
8. **Verify the fix** — Run tests; an untested fix is an assumption
9. **Max 5 files per curate** — Break down findings into multiple curate operations if needed
10. **Verify curations** — After storing critical context, run `brv curate view <logId>` to confirm what was stored (logId is printed by `brv curate` on completion). Run `brv curate view --help` to see all options.
