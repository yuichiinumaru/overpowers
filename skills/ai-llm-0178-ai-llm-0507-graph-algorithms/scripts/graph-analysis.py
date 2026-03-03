import networkx as nx
import sys

def analyze_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Is connected: {nx.is_connected(G)}")
    if nx.is_connected(G):
        print(f"Diameter: {nx.diameter(G)}")

if __name__ == "__main__":
    # Example usage
    edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
    analyze_graph(edges)
