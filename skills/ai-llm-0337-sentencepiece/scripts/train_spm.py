#!/usr/bin/env python3
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Train a SentencePiece model.")
    parser.add_argument("--input", required=True, help="Input text file for training")
    parser.add_argument("--prefix", required=True, help="Output model prefix")
    parser.add_argument("--vocab-size", type=int, default=8000, help="Vocabulary size")
    parser.add_argument("--model-type", choices=["unigram", "bpe", "char", "word"], default="unigram", help="Model type")

    args = parser.parse_args()
    
    try:
        import sentencepiece as spm
    except ImportError:
        print("Error: sentencepiece python package is not installed.")
        print("Install it with: pip install sentencepiece")
        return

    print(f"Training SentencePiece {args.model_type} model with vocab size {args.vocab_size}...")

    spm.SentencePieceTrainer.train(
        input=args.input,
        model_prefix=args.prefix,
        vocab_size=args.vocab_size,
        model_type=args.model_type,
        character_coverage=0.9995
    )

    print(f"Training complete. Model saved as {args.prefix}.model and {args.prefix}.vocab")

if __name__ == "__main__":
    main()
