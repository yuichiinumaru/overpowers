#!/usr/bin/env python3
import argparse

def calculate_savings(vectors, original_dims, truncated_dims, precision_bytes=4):
    """
    Calculates memory footprint for raw embeddings (excluding index overhead like HNSW graphs).
    Default precision is 4 bytes (Float32).
    """
    original_size_bytes = vectors * original_dims * precision_bytes
    truncated_size_bytes = vectors * truncated_dims * precision_bytes
    
    original_mb = original_size_bytes / (1024 ** 2)
    truncated_mb = truncated_size_bytes / (1024 ** 2)
    
    savings_mb = original_mb - truncated_mb
    savings_pct = (savings_mb / original_mb) * 100 if original_mb > 0 else 0
    
    print(f"--- Matryoshka (MRL) Savings Calculator ---")
    print(f"Total Vectors: {vectors:,}")
    print(f"Data Type: {precision_bytes * 8}-bit float")
    print(f"Original Dimensions: {original_dims} -> {original_mb:,.2f} MB")
    print(f"Truncated Dimensions: {truncated_dims} -> {truncated_mb:,.2f} MB")
    print(f"-------------------------------------------")
    print(f"Total Raw Memory Saved: {savings_mb:,.2f} MB ({savings_pct:.1f}%)")
    print("\n*Note: This is RAW vector data. Actual RAM usage will be higher due to index overhead (e.g., HNSW graphs).*")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate memory savings using Matryoshka Representation Learning (MRL).")
    parser.add_argument("--vectors", type=int, required=True, help="Number of vectors in the database")
    parser.add_argument("--orig-dim", type=int, default=1536, help="Original vector dimension (e.g., 1536)")
    parser.add_argument("--trunc-dim", type=int, default=256, help="Truncated vector dimension (e.g., 256 or 512)")
    parser.add_argument("--precision", type=int, default=4, choices=[2, 4, 8], help="Bytes per value (2=FP16, 4=FP32, 8=FP64)")
    
    args = parser.parse_args()
    
    if args.trunc_dim >= args.orig_dim:
        print("[ERROR] Truncated dimensions must be smaller than original dimensions.")
        exit(1)
        
    calculate_savings(args.vectors, args.orig_dim, args.trunc_dim, args.precision)
