#!/usr/bin/env python3
import argparse
import sys
import json
import asyncio

async def generate_forge(sequence, model_name, steps, token):
    try:
        from esm.sdk.forge import ESM3ForgeInferenceClient
        from esm.sdk.api import ESMProtein, GenerationConfig

        client = ESM3ForgeInferenceClient(model=model_name, token=token)
        protein = ESMProtein(sequence=sequence)
        config = GenerationConfig(track="sequence", num_steps=steps)

        result = await client.async_generate(protein, config)
        return result.sequence
    except ImportError:
        print("Error: esm package not installed. Run 'pip install esm'")
        sys.exit(1)
    except Exception as e:
        print(f"Forge generation failed: {e}")
        return None

def generate_local(sequence, model_name, steps):
    try:
        from esm.models.esm3 import ESM3
        from esm.sdk.api import ESMProtein, GenerationConfig

        model = ESM3.from_pretrained(model_name)
        protein = ESMProtein(sequence=sequence)
        config = GenerationConfig(track="sequence", num_steps=steps)

        result = model.generate(protein, config)
        return result.sequence
    except ImportError:
        print("Error: esm package not installed. Run 'pip install esm'")
        sys.exit(1)
    except Exception as e:
        print(f"Local generation failed: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="ESM3 Protein Generation")
    parser.add_argument("--sequence", required=True, help="Input sequence with '_' for masked positions")
    parser.add_argument("--model", default="esm3-sm-open-v1", help="ESM3 model version")
    parser.add_argument("--steps", type=int, default=8, help="Generation steps")
    parser.add_argument("--use-forge", action="store_true", help="Use remote Forge API")
    parser.add_argument("--token", help="Forge API token")

    args = parser.parse_args()

    print(f"Generating protein sequence using {args.model}...")

    if args.use_forge:
        if not args.token:
            print("Error: Forge token required. Provide via --token.")
            sys.exit(1)
        result = asyncio.run(generate_forge(args.sequence, args.model, args.steps, args.token))
    else:
        result = generate_local(args.sequence, args.model, args.steps)

    if result:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
