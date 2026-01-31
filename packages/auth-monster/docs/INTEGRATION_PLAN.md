# Integration Plan: Harmonizing the Monster

## 1. Executive Summary
A rigorous 10-pass analysis of the repository's 4 feature branches reveals that **3 out of 4 branches are regression/stale states** that should be discarded. Only one branch (`jules-integrate-phase-5-features`) contains valuable, unmerged code.

**Key Findings:**
*   `master`: The most advanced state. Contains Phase 2 (Providers), Phase 4 (UI), and Phase 5 (Deep Research/Mark VI) code.
*   `phase-5-features`: **STALE/REGRESSION.** Diff shows it *removes* modern features (DeepSeek, Grok) and *adds* 6000+ lines of `.js` artifacts. Merging this would revert the project.
*   `phase2-providers-protocol`: **REDUNDANT.** Its features (new providers) are already present in `master`.
*   `feat-phase-4-ui`: **STALE/REGRESSION.** Diff shows it *removes* the Dashboard and core types.
*   `jules-integrate-phase-5-features`: **VALUABLE.** Contains small but critical logic improvements (Proactive Quota Check, Reasoning Enforcement, GitHub Token Support) that are missing from `master`.

## 2. Detailed Branch Analysis

### A. `jules-integrate-phase-5-features` (The "Gem")
*   **Status:** Unmerged.
*   **Changes:**
    *   `src/core/rotation.ts`: Adds proactive quota check (`remaining <= 0`).
    *   `src/index.ts`: Adds `enforceReasoning` middleware.
    *   `src/utils/github-sync.ts`: Adds `token` parameter for GH CLI auth.
*   **Recommendation:** **MERGE.**

### B. `phase-5-features` (The "Trap")
*   **Status:** Stale & Polluted.
*   **Changes:** Adds `src/**/*.js` artifacts. Removes `DeepSeek` from `endpoints.ts`.
*   **Recommendation:** **DISCARD.**

### C. `phase2-providers-protocol` (The "Ghost")
*   **Status:** Already Integrated.
*   **Recommendation:** **DISCARD.**

### D. `feat-phase-4-ui` (The "Zombie")
*   **Status:** Stale.
*   **Recommendation:** **DISCARD.**

## 3. Integration Procedure

### Step 1: Sanitation
Ensure we never commit artifacts again.

```bash
echo "src/**/*.js" >> .gitignore
git rm -r --cached src/**/*.js 2>/dev/null || true
```

### Step 2: Merge Valuable Features
We will cherry-pick the changes from `jules-integrate-phase-5-features`. Since we are in a clean analysis branch, we can manually apply these changes or merge them.

**Method:** `git merge origin/jules-integrate-phase-5-features-15337185734724250253`

### Step 3: Validation
1.  Verify `src/core/rotation.ts` has the new check.
2.  Run `npm test`.

## 4. Final State
The repository will be on the latest `master` baseline + the critical "missing link" fixes from `jules-integrate`. The polluted/stale branches will be ignored.
