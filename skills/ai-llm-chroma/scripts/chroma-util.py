#!/usr/bin/env python3
import argparse
import os
try:
    import chromadb
except ImportError:
    print("Error: chromadb not installed. Run 'pip install chromadb'")
    exit(1)

def main():
    parser = argparse.ArgumentParser(description='Chroma DB Utility')
    parser.add_argument('--path', default='./chroma_db', help='Path to persistent client')
    parser.add_argument('--list', action='store_true', help='List collections')
    parser.add_argument('--query', help='Query text for similarity search')
    parser.add_argument('--collection', help='Collection name for query')
    parser.add_argument('--n', type=int, default=5, help='Number of results')

    args = parser.parse_args()
    
    client = chromadb.PersistentClient(path=args.path)
    print(f"Connected to Chroma DB at {args.path}")

    if args.list:
        collections = client.list_collections()
        print(f"\nCollections ({len(collections)}):")
        for c in collections:
            print(f"  - {c.name}")

    if args.query:
        if not args.collection:
            print("Error: --collection required for query")
            return
        
        collection = client.get_collection(name=args.collection)
        results = collection.query(
            query_texts=[args.query],
            n_results=args.n
        )
        
        print(f"\nResults for '{args.query}' in '{args.collection}':")
        for i in range(len(results['ids'][0])):
            print(f"[{i+1}] ID: {results['ids'][0][i]}")
            print(f"    Document: {results['documents'][0][i][:100]}...")
            if results['metadatas']:
                print(f"    Metadata: {results['metadatas'][0][i]}")
            print(f"    Distance: {results['distances'][0][i]}")

if __name__ == "__main__":
    main()
