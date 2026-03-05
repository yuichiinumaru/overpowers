import argparse

# Thresholds from SKILL.md
THRESHOLDS = {
    "GPT-5.2": {"onset": 64000, "severe": 200000},
    "Claude Opus 4.5": {"onset": 100000, "severe": 180000},
    "Claude Sonnet 4.5": {"onset": 80000, "severe": 150000},
    "Gemini 3 Pro": {"onset": 500000, "severe": 800000},
    "Gemini 3 Flash": {"onset": 300000, "severe": 600000},
}

def check_degradation(model, token_count):
    if model not in THRESHOLDS:
        return f"Unknown model: {model}. Cannot check degradation."
    
    onset = THRESHOLDS[model]["onset"]
    severe = THRESHOLDS[model]["severe"]
    
    if token_count >= severe:
        return f"CRITICAL: {model} is at {token_count} tokens. SEVERE DEGRADATION expected (>={severe})."
    elif token_count >= onset:
        return f"WARNING: {model} is at {token_count} tokens. Degradation onset detected (>={onset})."
    else:
        return f"OK: {model} is at {token_count} tokens. Below degradation onset ({onset})."

def main():
    parser = argparse.ArgumentParser(description='Check context degradation risks based on model and token count.')
    parser.add_argument('--model', required=True, choices=list(THRESHOLDS.keys()), help='AI Model name')
    parser.add_argument('--tokens', type=int, required=True, help='Current token count')

    args = parser.parse_args()
    print(check_degradation(args.model, args.tokens))

if __name__ == "__main__":
    main()
