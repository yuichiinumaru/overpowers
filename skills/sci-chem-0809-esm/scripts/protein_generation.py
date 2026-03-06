#!/usr/bin/env python3
import argparse
import sys
import os

try:
    from esm.models.esm3 import ESM3
    from esm.sdk.api import ESMProtein, GenerationConfig
except ImportError:
    print("Error: esm library not found. Please install it with 'pip install esm'.")
    sys.exit(1)

def generate_sequence(prompt_seq, model_name="esm3-sm-open-v1", steps=8, device="cpu"):
    print(f"Loading model {model_name} on {device}...")
    model = ESM3.from_pretrained(model_name).to(device)
    
    protein = ESMProtein(sequence=prompt_seq)
    print(f"Generating sequence for prompt: {prompt_seq}...")
    
    generated = model.generate(protein, GenerationConfig(track="sequence", num_steps=steps))
    return generated.sequence

def main():
    parser = argparse.ArgumentParser(description='Protein sequence generation using ESM3.')
    parser.add_argument('sequence', help='Protein sequence prompt (use "_" for masked positions)')
    parser.add_argument('--model', default='esm3-sm-open-v1', help='Model name (default: esm3-sm-open-v1)')
    parser.add_argument('--steps', type=int, default=8, help='Number of generation steps (default: 8)')
    parser.add_argument('--device', default='cpu', help='Device to run on (cpu or cuda)')
    parser.add_argument('--output', help='Output file for generated sequence')

    args = parser.parse_args()

    try:
        result = generate_sequence(args.sequence, args.model, args.steps, args.device)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Generated sequence saved to {args.output}")
        else:
            print(f"Generated sequence: {result}")
    except Exception as e:
        print(f"Error during generation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
