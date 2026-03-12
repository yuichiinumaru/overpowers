import argparse
import os

def run_rag_bi(csv_path, query):
    print(f"📊 Running RAG BI Pipeline for: {csv_path}")
    print(f"❓ User Query: {query}")
    
    # This script mocks the logic in SKILL.md
    print("\n1. Ingesting & Preprocessing...")
    print(f"   Loaded data from {csv_path}")
    
    print("\n2. Vectorization (Embedding)...")
    print("   Generated embeddings for 15 chunks.")
    
    print("\n3. Retrieval Phase...")
    print("   Found top 3 relevant chunks.")
    
    print("\n4. Augmentation & Generation...")
    print("\n[LLM Response]:")
    print(f"Based on the provided sales data, the total sales in the requested period were $45,200. This was driven primarily by the 'Software' category which accounted for 60% of the volume.")
    
    print("\n✅ Pipeline execution complete.")

def main():
    parser = argparse.ArgumentParser(description='LLM Powered RAG for Business Intelligence')
    parser.add_argument('--csv', required=True, help='Path to sales data CSV')
    parser.add_argument('--query', required=True, help='Natural language query about the data')
    
    args = parser.parse_args()
    run_rag_bi(args.csv, args.query)

if __name__ == "__main__":
    main()
