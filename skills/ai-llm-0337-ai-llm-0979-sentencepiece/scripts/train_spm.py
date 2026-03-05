import sentencepiece as spm
import argparse
import sys

def train_model(input_file, model_prefix, vocab_size, model_type):
    print(f"Training SentencePiece model from {input_file}...")
    try:
        spm.SentencePieceTrainer.train(
            input=input_file,
            model_prefix=model_prefix,
            vocab_size=vocab_size,
            model_type=model_type,
            character_coverage=0.9995 if model_type == 'unigram' else 1.0
        )
        print(f"Model saved as {model_prefix}.model and {model_prefix}.vocab")
    except Exception as e:
        print(f"Error during training: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a SentencePiece model.")
    parser.add_argument("--input", required=True, help="Input text file")
    parser.add_argument("--prefix", default="m", help="Model prefix")
    parser.add_argument("--vocab_size", type=int, default=8000, help="Vocabulary size")
    parser.add_argument("--type", default="unigram", choices=['unigram', 'bpe', 'char', 'word'], help="Model type")
    args = parser.parse_args()
    
    train_model(args.input, args.prefix, args.vocab_size, args.type)
