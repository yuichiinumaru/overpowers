#!/usr/bin/env python3
import sys
import argparse
import os

try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: networkx and matplotlib are required. Install with: pip install networkx matplotlib")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Analyze and visualize a graph from an edge list file.")
    parser.add_argument("file", help="Path to the edge list file (space-separated sources and targets)")
    parser.add_argument("--directed", action="store_true", help="Treat as a directed graph")
    parser.add_argument("--output", "-o", default="graph_analysis.png", help="Path to save the visualization")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    # Load graph
    if args.directed:
        G = nx.read_edgelist(args.file, create_using=nx.DiGraph())
    else:
        G = nx.read_edgelist(args.file)

    # Basic analysis
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Density: {nx.density(G):.4f}")
    
    if not args.directed:
        print(f"Connected: {nx.is_connected(G)}")
        if nx.is_connected(G):
            print(f"Average clustering coefficient: {nx.average_clustering(G):.4f}")
    else:
        print(f"Strongly connected: {nx.is_strongly_connected(G)}")

    # Compute degree centrality
    print("\nTop 5 nodes by degree centrality:")
    centrality = nx.degree_centrality(G)
    top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
    for node, cent in top_nodes:
        print(f"  {node}: {cent:.4f}")

    # Visualization
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, edge_color='gray', arrowsize=20)
    plt.title(f"Graph Visualization: {os.path.basename(args.file)}")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(args.output, dpi=300)
    print(f"\nVisualization saved to {args.output}")

if __name__ == "__main__":
    main()
