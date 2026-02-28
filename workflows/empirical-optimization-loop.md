---
description: A workflow enforcing a "measure before you merge" policy for AI-generated code.
category: performance
---

# Empirical Optimization Loop Workflow

This workflow addresses the core flaw that AI models optimize for correctness over performance, often introducing inefficient algorithms (e.g., O(n²)), memory leaks, API over-fetching, and suboptimal data structures (like arrays instead of sets). It enforces a strict "measure before you merge" methodology.

## Pre-requisites
You should have the `performance-benchmarking` skill available to write custom `perf_hooks` (Node), `timeit` (Python), or Bash benchmarks.

## Phase 1: Feature Implementation (The Baseline)
1. **Analyze Requirements:** Understand the feature request. Identify areas that might become "hot paths" (loops, heavy parsers, search algorithms, API calls).
2. **Implement for Correctness:** Write the initial implementation focused purely on getting the logic right. Ensure it passes existing unit tests.
3. **Hypothesize Bottlenecks:** Review the code. Look for:
    * Recomputing values on every iteration (e.g., redundant source byte conversions).
    * `O(n)` lookups in loops (e.g., scanning strings instead of using index tables or HashMaps).
    * Synchronous file blocking or CPU-heavy sync tasks.
    * In UI logic: missing memoization causing massive re-renders.

## Phase 2: Empirical Benchmarking
Before considering the code finished, you **must** prove its speed.
1. **Write a Benchmark Script:** Using the `performance-benchmarking` skill, create a temporary script (e.g., `benchmark.js` or `bench.py`).
2. **Execute Baseline:** Run the script against a simulated large dataset (e.g., an array of 10,000 items) and record the execution time.
3. **If the execution time is significant (e.g. >100ms for a local micro-op), proceed to Phase 3. If it is instantly resolved (<5ms), you may skip optimization.**

## Phase 3: The Optimization Refactor
1. **Apply Countermeasures:** Refactor the baseline code to address the hypothesized bottlenecks.
    * Use sets/maps for lookups instead of arrays.
    * Move computations out of loops and build lookup tables.
    * Replace recursive string manipulation with trees or optimized standard library features.
    * Add `React.memo` or `useMemo` if targeting UI re-render issues.
2. **Re-Execute Benchmark:** Run the benchmark script against the new optimized implementation.
3. **Compare Results:** Ensure the execution time is quantifiably faster (e.g., "19x speedup").

## Phase 4: Finalization and Cleanup
1. **Verify Correctness:** Ensure the optimized code still passes all behavioral tests.
2. **Document Performance Gain:** In the PR description or commit message, document the empirical speedup (e.g., "Refactored byte conversion, moving from O(n²) to O(log n), decreasing execution time by 80% based on micro-benchmark.").
3. **Cleanup:** Delete the temporary benchmark script from the workspace before submitting the PR.