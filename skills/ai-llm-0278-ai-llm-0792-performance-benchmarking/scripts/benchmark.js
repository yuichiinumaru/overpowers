#!/usr/bin/env node
/**
 * Simple utility script for benchmarking execution time of two functions using Node's native perf_hooks.
 */

const { performance } = require('perf_hooks');

function benchmark(fnName, fn, iterations = 10000) {
  const start = performance.now();
  for (let i = 0; i < iterations; i++) {
    fn();
  }
  const end = performance.now();
  console.log(`[${fnName}] Execution time over ${iterations} iterations: ${(end - start).toFixed(4)} ms`);
}

function implementationA() {
    // slow implementation
    const list = [1, 2, 3, 4, 5];
    return list.filter(i => i === 3).length > 0;
}

function implementationB() {
    // fast implementation
    const set = new Set([1, 2, 3, 4, 5]);
    return set.has(3);
}

// Warm up JIT
for(let i=0; i<100; i++) {
    implementationA();
    implementationB();
}

console.log('Running Benchmarks...');
benchmark('Slow Implementation (Array)', implementationA, 100000);
benchmark('Fast Implementation (Set)', implementationB, 100000);
