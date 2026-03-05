#!/usr/bin/env python3
import random
import sys

def simulate_load_balancing(nodes, requests):
    distribution = [0] * nodes
    for _ in range(requests):
        # Round-robin or Random selection
        node = random.randint(0, nodes - 1)
        distribution[node] += 1
    return distribution

if __name__ == "__main__":
    nodes = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    requests = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    
    dist = simulate_load_balancing(nodes, requests)
    for i, count in enumerate(dist):
        print(f"Node {i}: {count} requests ({(count/requests)*100:.1f}%)")
