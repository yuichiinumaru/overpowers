#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="TorchDrug Model Training")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset to load")
    parser.add_argument("--model", type=str, required=True, help="Model type to use")
    args = parser.parse_args()

    print(f"Loading dataset: {args.dataset}")
    print(f"Building model: {args.model}")
    print("Training started...")

if __name__ == "__main__":
    main()
