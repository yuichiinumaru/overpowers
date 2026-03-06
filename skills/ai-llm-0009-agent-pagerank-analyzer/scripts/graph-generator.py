#!/usr/bin/env python3
import random
import sys

def generate_graph(nodes, density=0.1):
    edges = []
    for i in range(nodes):
        for j in range(nodes):
            if i != j and random.random() < density:
                edges.append((i, j))
    return edges

if __name__ == "__main__":
    nodes = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    density = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
    
    edges = generate_graph(nodes, density)
    print(f"Nodes: {nodes}")
    print(f"Edges: {len(edges)}")
    for u, v in edges:
        print(f"{u} -> {v}")
