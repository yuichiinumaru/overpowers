#!/usr/bin/env python3
"""
Basic NetworkX analysis script.
Loads a graph, computes basic metrics, and optionally visualizes it.
"""
import argparse
import sys

try:
    import networkx as nx
    import matplotlib.pyplot as plt
    import pandas as pd
except ImportError:
    print("Error: Missing required packages. Please install networkx, matplotlib, and pandas.")
    print("Run: uv pip install networkx matplotlib pandas")
    sys.exit(1)

def analyze_graph(file_path, format_type, output_prefix=None, visualize=False):
    print(f"Loading graph from {file_path} (format: {format_type})...")

    # Load graph
    try:
        if format_type == 'edgelist':
            G = nx.read_edgelist(file_path)
        elif format_type == 'graphml':
            G = nx.read_graphml(file_path)
        elif format_type == 'gml':
            G = nx.read_gml(file_path)
        elif format_type == 'csv':
            df = pd.read_csv(file_path)
            # Assume first two columns are source and target
            source_col, target_col = df.columns[0], df.columns[1]
            G = nx.from_pandas_edgelist(df, source=source_col, target=target_col)
        else:
            print(f"Unsupported format: {format_type}")
            return
    except Exception as e:
        print(f"Error loading graph: {e}")
        return

    # Basic stats
    print("\n--- Basic Statistics ---")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Density: {nx.density(G):.4f}")

    is_directed = G.is_directed()
    print(f"Directed: {is_directed}")

    if is_directed:
        print(f"Strongly connected components: {nx.number_strongly_connected_components(G)}")
        print(f"Weakly connected components: {nx.number_weakly_connected_components(G)}")
    else:
        print(f"Connected components: {nx.number_connected_components(G)}")
        print(f"Is connected: {nx.is_connected(G)}")

    # Centrality metrics
    print("\n--- Top 5 Nodes by Degree Centrality ---")
    deg_cent = nx.degree_centrality(G)
    top_deg = sorted(deg_cent.items(), key=lambda x: x[1], reverse=True)[:5]
    for node, cent in top_deg:
        print(f"  Node {node}: {cent:.4f}")

    # Export results if requested
    if output_prefix:
        out_file = f"{output_prefix}_degree_centrality.csv"
        print(f"\nSaving centrality metrics to {out_file}...")
        df_cent = pd.DataFrame(list(deg_cent.items()), columns=['Node', 'DegreeCentrality'])
        df_cent.to_csv(out_file, index=False)

    # Visualization
    if visualize:
        print("\nGenerating visualization...")
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, seed=42)

        # Color nodes by degree
        node_colors = [deg_cent[n] for n in G.nodes()]

        nx.draw(G, pos, node_color=node_colors, cmap=plt.cm.viridis,
                with_labels=G.number_of_nodes() < 50,
                node_size=100 if G.number_of_nodes() > 100 else 300,
                edge_color='gray', alpha=0.7)

        plt.title('Network Visualization')
        plt.axis('off')

        if output_prefix:
            plt.savefig(f"{output_prefix}_network.png", dpi=300, bbox_inches='tight')
            print(f"Saved visualization to {output_prefix}_network.png")
        else:
            plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a network graph")
    parser.add_argument("file", help="Path to graph file")
    parser.add_argument("--format", choices=['edgelist', 'graphml', 'gml', 'csv'],
                        default='edgelist', help="File format (default: edgelist)")
    parser.add_argument("--output", help="Prefix for output files (e.g., 'results/mygraph')")
    parser.add_argument("--visualize", action="store_true", help="Generate and show/save visualization")

    args = parser.parse_args()
    analyze_graph(args.file, args.format, args.output, args.visualize)
