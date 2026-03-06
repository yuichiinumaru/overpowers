import argparse

def calculate_cost(model, input_tokens, output_tokens):
    # Rates per 1M tokens (USD) - Standard rates as of 2024
    rates = {
        'gpt-4o': {'input': 5.00, 'output': 15.00},
        'gpt-4o-mini': {'input': 0.15, 'output': 0.60},
        'claude-3-5-sonnet': {'input': 3.00, 'output': 15.00},
        'claude-3-haiku': {'input': 0.25, 'output': 1.25},
        'gemini-1.5-pro': {'input': 3.50, 'output': 10.50},
        'gemini-1.5-flash': {'input': 0.075, 'output': 0.30},
    }
    
    if model not in rates:
        return None
    
    rate = rates[model]
    cost = (input_tokens * rate['input'] + output_tokens * rate['output']) / 1_000_000
    return cost

def main():
    parser = argparse.ArgumentParser(description='Calculate AI API cost')
    parser.add_argument('--model', type=str, required=True, help='Model name (e.g., gpt-4o, claude-3-haiku)')
    parser.add_argument('--input', type=int, required=True, help='Number of input tokens')
    parser.add_argument('--output', type=int, required=True, help='Number of output tokens')
    
    args = parser.parse_args()
    
    cost = calculate_cost(args.model, args.input, args.output)
    if cost is not None:
        print(f"Estimated cost for {args.model}: ${cost:.6f}")
    else:
        print(f"Model '{args.model}' not found in rate table.")

if __name__ == "__main__":
    main()
