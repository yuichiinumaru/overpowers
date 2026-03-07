#!/usr/bin/env python3
"""
Basic Region Embedding Pipeline using GeniML.
Derived from geniml SKILL.md.
"""
import sys
import os

try:
    from geniml.tokenization import hard_tokenization
    from geniml.region2vec import region2vec
    from geniml.evaluation import evaluate_embeddings
except ImportError:
    print("Error: geniml is not installed. Please install it using 'uv pip install geniml'.")
    sys.exit(1)

def main():
    if len(sys.argv) < 5:
        print("Usage: python region2vec_pipeline.py <src_folder> <dst_folder> <universe_file> <save_dir>")
        sys.exit(1)

    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]
    universe_file = sys.argv[3]
    save_dir = sys.argv[4]

    if not os.path.exists(src_folder):
        print(f"Error: Source folder '{src_folder}' does not exist.")
        sys.exit(1)

    try:
        print("Step 1: Tokenize BED files...")
        hard_tokenization(
            src_folder=src_folder,
            dst_folder=dst_folder,
            universe_file=universe_file,
            p_value_threshold=1e-9
        )

        print("Step 2: Train Region2Vec...")
        region2vec(
            token_folder=dst_folder,
            save_dir=save_dir,
            num_shufflings=1000,
            embedding_dim=100
        )
        print("Pipeline complete. Models saved to:", save_dir)
        print("Use evaluate_embeddings() for downstream evaluation metrics.")

    except Exception as e:
        print(f"Error running pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
