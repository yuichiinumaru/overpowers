#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Scaffold a rigorous research implementation document.")
    parser.add_argument('--topic', required=True, help="Topic of research")

    args = parser.parse_args()

    template = f"""# Theoretical Analysis and Implementation Plan: {args.topic}

## 1. Formal Problem Statement
Let P be the problem of {args.topic}.
We define the inputs as X and expected outputs as Y.
The formal constraints are:
- Constraint 1: [Define mathematically]
- Constraint 2: [Define mathematically]

## 2. Complexity Analysis
The optimal theoretical bound for this problem is:
- Time Complexity: O(...)
- Space Complexity: O(...)

This bound is proven by [Reference/Reduction].

## 3. Algorithm Selection
We reject naive approaches (e.g., O(N^2) brute force) due to intractability at scale.
The selected algorithm is [Algorithm Name], which achieves the optimal theoretical bound.

## 4. Implementation Constraints
- Memory safety: Must avoid buffer overflows.
- Thread safety: Must utilize proper synchronization primitives for concurrent execution.
- Edge cases: Empty inputs, maximal values, precision loss in floating-point operations.

## 5. Formal Verification
The correctness of this implementation will be verified through:
1. Unit tests covering all boundary conditions.
2. Fuzzing with malformed inputs.
3. Asymptotic behavior verification via empirical benchmarks.

---
[Begin Implementation Below]
"""
    print(template)

if __name__ == '__main__':
    main()
