import argparse
from tdc import Oracle

def main():
    parser = argparse.ArgumentParser(description='Evaluate molecular property oracles.')
    parser.add_argument('--name', required=True, help='Oracle name (e.g. GSK3B, DRD2, QED)')
    parser.add_argument('--smiles', required=True, help='SMILES string to evaluate')

    args = parser.parse_args()

    print(f"Loading oracle {args.name}...")
    try:
        oracle = Oracle(name=args.name)
        score = oracle(args.smiles)
        print(f"\nOracle: {args.name}")
        print(f"SMILES: {args.smiles}")
        print(f"Score:  {score:.4f}")
    except Exception as e:
        print(f"Error evaluating oracle: {e}")

if __name__ == "__main__":
    main()
