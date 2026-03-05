import subprocess
import sys
import argparse

def query_db(path, vector, k=10, threshold=0.75, metric="cosine"):
    """
    Query AgentDB vector database.
    """
    cmd = ["npx", "agentdb@latest", "query", path, vector, "-k", str(k), "-t", str(threshold), "-m", metric]
    
    print(f"Querying database: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
    except Exception as e:
        print(f"Error querying database: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query AgentDB vector database")
    parser.add_argument("path", help="Path to database file")
    parser.add_argument("vector", help="Vector to query (as string, e.g. '[0.1, 0.2]')")
    parser.add_argument("-k", type=int, default=10, help="Top-k results")
    parser.add_argument("-t", "--threshold", type=float, default=0.75, help="Similarity threshold")
    parser.add_argument("-m", "--metric", choices=["cosine", "euclidean", "dot"], default="cosine", help="Distance metric")
    
    args = parser.parse_args()
    query_db(args.path, args.vector, args.k, args.threshold, args.metric)
