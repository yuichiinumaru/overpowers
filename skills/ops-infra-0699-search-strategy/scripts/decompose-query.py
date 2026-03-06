import argparse
import json

def decompose_query(query):
    """
    Decomposes a natural language query into source-specific search strategies.
    """
    # Simple keyword extraction logic (placeholder)
    keywords = query.split()
    
    # Define source strategies
    strategies = {
        "chat": {
            "semantic": query,
            "keyword": f"{' '.join(keywords[:3])}",
            "filters": ["in:#engineering", "after:2025-01-01"]
        },
        "knowledge_base": {
            "semantic": query,
            "keyword": f"\"{' '.join(keywords[:2])}\""
        },
        "project_tracker": {
            "text": ' '.join(keywords[:2]),
            "completed": False
        }
    }
    
    return strategies

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompose natural language query into source-specific searches")
    parser.add_argument("query", help="The user's search query")
    
    args = parser.parse_args()
    
    print(f"Decomposing query: '{args.query}'\n")
    strategies = decompose_query(args.query)
    
    for source, strategy in strategies.items():
        print(f"--- Source: {source} ---")
        print(json.dumps(strategy, indent=2))
        print()
