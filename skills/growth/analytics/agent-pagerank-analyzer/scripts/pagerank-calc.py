#!/usr/bin/env python3

import numpy as np
import sys

def pagerank(M, num_iterations: int = 100, d: float = 0.85):
    """
    Compute PageRank for a given adjacency matrix.
    M: Adjacency matrix (numpy array)
    """
    N = M.shape[1]
    v = np.ones(N) / N
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v

if __name__ == "__main__":
    # Simple Example: 3 nodes
    # 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0
    M = np.array([
        [0, 0, 1],
        [0.5, 0, 0],
        [0.5, 1, 0]
    ])
    
    print("Calculating PageRank for example matrix:")
    print(M)
    
    scores = pagerank(M)
    for i, score in enumerate(scores):
        print(f"Node {i}: {score:.4f}")
