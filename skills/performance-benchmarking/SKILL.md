# Performance Benchmarking Skill

## Description
A skill designed to empower agents with the ability to empirically measure code execution speed. It addresses the issue of LLMs relying on single-pass "correctness" generation by providing tools to compare algorithms, identify slow paths, and confirm optimization hypotheses via micro-benchmarking.

## When to Use
- Whenever modifying a hot path or computationally heavy algorithm.
- Before merging a PR if the function is predicted to run frequently (e.g. data parsing, rendering loops).
- To definitively choose between two data structure implementations (e.g., Array vs. Set).
- As requested by the `empirical-optimization-loop.md` workflow.

## Tools and Languages

### Python (`timeit` & `cProfile`)
Agents should create standalone scripts utilizing `timeit` for micro-benchmarks or `cProfile` for deep tracing.

**Example `timeit` usage:**
```python
import timeit

# Implementation A (AI Generated, maybe slow)
def find_slow(items, target):
    return [i for i in items if i == target]

# Implementation B (Optimized)
def find_fast(items_set, target):
    return target in items_set

# Benchmark
slow_time = timeit.timeit('find_slow(my_list, "X")', globals=globals(), number=10000)
fast_time = timeit.timeit('find_fast(my_set, "X")', globals=globals(), number=10000)

print(f"Slow: {slow_time:.5f}s, Fast: {fast_time:.5f}s")
```

### Node.js / JavaScript (`perf_hooks`)
Agents should write micro-benchmarks utilizing Node's native `perf_hooks`.

**Example `perf_hooks` usage:**
```javascript
const { performance } = require('perf_hooks');

function bench(fn, iterations = 10000) {
  const start = performance.now();
  for (let i = 0; i < iterations; i++) {
    fn();
  }
  const end = performance.now();
  console.log(`Execution time: ${(end - start).toFixed(4)} ms`);
}

bench(() => { /* test code A */ });
bench(() => { /* test code B */ });
```

### Bash (`hyperfine` or `time`)
If analyzing CLI scripts or broader execution boundaries, utilize the native `time` command.
```bash
time ./my_script.sh
```

## Best Practices
1. **Always Measure Against Baselines:** You must measure the *original* code before implementing the optimization to prove the speedup ratio.
2. **Beware the JIT:** When benchmarking JavaScript or Java, run warmup iterations so the JIT compiler stabilizes before taking the final measurement.
3. **Data Independence:** Do not assume one set of inputs proves optimal performance. Test small datasets (N=10) and large datasets (N=10,000) to understand big-O degradation.
4. **Document Results:** Leave comments or commit messages detailing the speedup achieved (e.g., "Optimized byte parsing, reducing execution time by 19x (100ms -> 5ms)").