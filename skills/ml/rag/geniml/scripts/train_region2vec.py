#!/usr/bin/env python3
import os
import argparse
from geniml.tokenization import hard_tokenization
from geniml.region2vec import region2vec
from geniml.evaluation import evaluate_embeddings

def main():
    parser = argparse.ArgumentParser(description="Train Region2Vec model")
    parser.add_argument("--src-folder", required=True, help="Folder containing input BED files")
    parser.add_argument("--tokens-folder", default="tokens/", help="Folder to output tokens")
    parser.add_argument("--universe-file", required=True, help="Universe reference BED file")
    parser.add_argument("--save-dir", default="model/", help="Directory to save the trained model")
    parser.add_argument("--p-value", type=float, default=1e-9, help="P-value threshold for tokenization")
    parser.add_argument("--shuffles", type=int, default=1000, help="Number of shufflings for training")
    parser.add_argument("--dim", type=int, default=100, help="Embedding dimension")
    parser.add_argument("--labels", help="Optional metadata/labels file for evaluation")

    args = parser.parse_args()

    # Create necessary directories
    os.makedirs(args.tokens_folder, exist_ok=True)
    os.makedirs(args.save_dir, exist_ok=True)

    print(f"Tokenizing BED files from {args.src_folder} using {args.universe_file}...")
    hard_tokenization(
        src_folder=args.src_folder,
        dst_folder=args.tokens_folder,
        universe_file=args.universe_file,
        p_value_threshold=args.p_value
    )

    print(f"Training Region2Vec model (dim={args.dim}, shuffles={args.shuffles})...")
    region2vec(
        token_folder=args.tokens_folder,
        save_dir=args.save_dir,
        num_shufflings=args.shuffles,
        embedding_dim=args.dim
    )

    if args.labels:
        embeddings_file = os.path.join(args.save_dir, "embeddings.npy")
        if os.path.exists(embeddings_file) and os.path.exists(args.labels):
            print(f"Evaluating embeddings with labels from {args.labels}...")
            metrics = evaluate_embeddings(
                embeddings_file=embeddings_file,
                labels_file=args.labels
            )
            print("Evaluation Metrics:", metrics)
        else:
            print(f"Warning: Embeddings or labels file not found. Skipping evaluation.")

    print("Training complete!")

if __name__ == "__main__":
    main()
