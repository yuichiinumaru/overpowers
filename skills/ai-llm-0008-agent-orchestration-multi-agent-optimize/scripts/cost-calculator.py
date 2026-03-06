#!/usr/bin/env python3
import sys

def calculate_cost(tokens, model='gpt-4o'):
    costs = {
        'gpt-4o': 0.005,
        'claude-3-5-sonnet': 0.003,
        'claude-3-haiku': 0.00025
    }
    rate = costs.get(model, 0.001)
    return (tokens / 1000) * rate

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cost-calculator.py <tokens> [model]")
        sys.exit(1)
    
    tokens = int(sys.argv[1])
    model = sys.argv[2] if len(sys.argv) > 2 else 'gpt-4o'
    print(f"Estimated cost for {tokens} tokens on {model}: ${calculate_cost(tokens, model):.4f}")
