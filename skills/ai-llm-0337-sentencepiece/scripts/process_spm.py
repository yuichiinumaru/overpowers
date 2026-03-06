import sentencepiece as spm
import argparse
import sys

def process_text(model_file, text, mode):
    sp = spm.SentencePieceProcessor(model_file=model_file)
    
    if mode == 'encode':
        pieces = sp.encode(text, out_type=str)
        ids = sp.encode(text, out_type=int)
        print("Pieces:", pieces)
        print("IDs:", ids)
    elif mode == 'decode':
        # Assuming space-separated IDs for simplicity in CLI
        try:
            ids = [int(i) for i in text.split()]
            decoded = sp.decode(ids)
            print("Decoded text:", decoded)
        except ValueError:
            print("Error: For decode mode, input must be a space-separated list of integer IDs.")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode or decode text using a SentencePiece model.")
    parser.add_argument("--model", required=True, help="SentencePiece model file (.model)")
    parser.add_argument("--text", required=True, help="Text to encode or space-separated IDs to decode")
    parser.add_argument("--mode", default="encode", choices=['encode', 'decode'], help="Operation mode")
    args = parser.parse_args()
    
    process_text(args.model, args.text, args.mode)
