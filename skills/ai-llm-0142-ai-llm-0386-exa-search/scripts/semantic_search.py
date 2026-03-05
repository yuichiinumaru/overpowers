import os
import sys

def semantic_search(query):
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        print("Error: EXA_API_KEY environment variable is not set.")
        sys.exit(1)
    
    print(f"Performing semantic search for: {query}")
    # Integration logic would go here

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python semantic_search.py <query>")
        sys.exit(1)
    semantic_search(sys.argv[1])
