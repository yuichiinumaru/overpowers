import os
import argparse
import sys
from geniml.tokenization import hard_tokenization
from geniml.region2vec import region2vec
from geniml.evaluation import evaluate_embeddings

def main():
    parser = argparse.ArgumentParser(description="Basic Region Embedding Pipeline using geniml.")
    parser.add_argument("--src-folder", required=True, help="Folder containing input BED files")
    parser.add_argument("--universe-file", required=True, help="Universe reference BED file")
    parser.add_argument("--tokens-folder", default="tokens/", help="Folder to output tokens")
    parser.add_argument("--model-dir", default="model/", help="Folder to save trained model")
    parser.add_argument("--embedding-dim", type=int, default=100, help="Embedding dimension")
    parser.add_argument("--num-shufflings", type=int, default=1000, help="Number of shufflings")
    parser.add_argument("--labels-file", help="Metadata labels CSV for evaluation (optional)")

    args = parser.parse_args()

    # Step 1: Tokenize BED files
    print(f"Step 1: Tokenizing BED files from {args.src_folder}...")
    try:
        os.makedirs(args.tokens_folder, exist_ok=True)
        hard_tokenization(
            src_folder=args.src_folder,
            dst_folder=args.tokens_folder,
            universe_file=args.universe_file,
            p_value_threshold=1e-9
        )
    except Exception as e:
        print(f"Error during tokenization: {e}", file=sys.stderr)
        sys.exit(1)

    # Step 2: Train Region2Vec
    print(f"Step 2: Training Region2Vec model...")
    try:
        os.makedirs(args.model_dir, exist_ok=True)
        region2vec(
            token_folder=args.tokens_folder,
            save_dir=args.model_dir,
            num_shufflings=args.num_shufflings,
            embedding_dim=args.embedding_dim
        )
    except Exception as e:
        print(f"Error during training: {e}", file=sys.stderr)
        sys.exit(1)

    # Step 3: Evaluate (if labels provided)
    if args.labels_file:
        print(f"Step 3: Evaluating embeddings using {args.labels_file}...")
        try:
            embeddings_file = os.path.join(args.model_dir, 'embeddings.npy')
            metrics = evaluate_embeddings(
                embeddings_file=embeddings_file,
                labels_file=args.labels_file
            )
            print("Evaluation metrics:", metrics)
        except Exception as e:
            print(f"Error during evaluation: {e}", file=sys.stderr)
            sys.exit(1)

    print("Pipeline complete.")

if __name__ == "__main__":
    main()
