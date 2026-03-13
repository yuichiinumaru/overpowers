#!/usr/bin/env python3
import argparse
import sys

def audit_config(dims, index_type, metadata_size_kb, doc_chunk_size):
    issues = []
    
    # 1. Dimension check
    if dims > 1536:
        issues.append(f"[WARNING] High dimensionality ({dims}). Consider dimensionality reduction (PCA) to reduce RAM usage and latency.")
    
    # 2. Index type check
    if index_type.upper() == "FLAT":
        issues.append("[ERROR] FLAT index detected. This is a 'Toy' pattern and will not scale. Switch to HNSW or IVF.")
    
    # 3. Metadata size
    if metadata_size_kb > 50:
        issues.append(f"[WARNING] Metadata size ({metadata_size_kb}KB) is high. Vector DBs are for vectors, not document storage. Store full docs in a sidecar DB.")
        
    # 4. Chunking
    if doc_chunk_size > 1000:
        issues.append(f"[WARNING] Large chunk size ({doc_chunk_size} tokens). Large chunks create noisy embeddings. Optimal is usually 200-500.")

    if not issues:
        print("[OK] Vector DB configuration follows basic production patterns.")
    else:
        print("\n".join(issues))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit Vector DB configuration for production scaling.")
    parser.add_argument("--dims", type=int, required=True, help="Number of vector dimensions")
    parser.add_argument("--index", type=str, required=True, help="Index type (FLAT, HNSW, IVF, etc.)")
    parser.add_argument("--meta-kb", type=float, required=True, help="Average metadata size per vector in KB")
    parser.add_argument("--chunk", type=int, required=True, help="Average tokens per chunk")
    
    args = parser.parse_args()
    audit_config(args.dims, args.index, args.meta_kb, args.chunk)
