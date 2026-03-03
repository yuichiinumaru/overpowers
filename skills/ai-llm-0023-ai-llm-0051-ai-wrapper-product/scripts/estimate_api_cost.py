#!/usr/bin/env python3
import sys
import argparse

def calculate_cost(input_tokens, output_tokens, model):
    # Prices per 1M tokens (as of early 2024 standards mentioned in SKILL.md and current market)
    rates = {
        'gpt-4o': {'input': 5.00, 'output': 15.00},
        'gpt-4o-mini': {'input': 0.15, 'output': 0.60},
        'claude-3-5-sonnet': {'input': 3.00, 'output': 15.00},
        'claude-3-haiku': {'input': 0.25, 'output': 1.25},
    }
    
    if model not in rates:
        print(f"Unknown model: {model}")
        print(f"Supported models: {', '.join(rates.keys())}")
        return None
        
    rate = rates[model]
    cost = (input_tokens * rate['input'] + output_tokens * rate['output']) / 1_000_000
    return cost

def main():
    parser = argparse.ArgumentParser(description='Estimate AI API cost based on token usage.')
    parser.add_argument('--input', type=int, required=True, help='Number of input tokens')
    parser.add_argument('--output', type=int, required=True, help='Number of output tokens')
    parser.add_argument('--model', type=str, default='claude-3-haiku', help='Model name')
    
    args = parser.parse_args()
    
    cost = calculate_cost(args.input, args.output, args.model)
    if cost is not None:
        print(f"Estimated cost for {args.model}:")
        print(f"Input:  {args.input} tokens")
        print(f"Output: {args.output} tokens")
        print(f"Total:  ${cost:.6f}")

if __name__ == "__main__":
    main()
