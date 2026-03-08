#!/usr/bin/env python3
"""
model_selector.py - Stateful health monitor for model providers.
Reads and updates ~/.config/opencode/model_status.json to track rate limits and cooldowns.
Supports returning fallback chains: Opus -> Sonnet -> Flash -> GLM.
"""

import os
import sys
import json
import time
import argparse

STATUS_FILE = os.path.expanduser("~/.config/opencode/model_status.json")

# Define our models and fallback chains based on complexity
MODELS = {
    "opus": "google/antigravity-claude-opus-4-5-thinking",
    "sonnet": "google/antigravity-claude-sonnet-4-5-thinking",
    "flash": "google/gemini-3-flash",
    "glm": "windsurf/glm-4.7"
}

CHAINS = {
    "high": ["opus", "sonnet", "flash", "glm"],
    "medium": ["sonnet", "flash", "glm", "opus"],
    "low": ["flash", "glm", "sonnet", "opus"]
}

DEFAULT_COOLDOWN_SECONDS = 300  # 5 minutes

def load_status():
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_status(status):
    os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=2)

def is_model_available(model_key, status, current_time):
    cooldown_until = status.get(model_key, {}).get("cooldown_until", 0)
    return current_time >= cooldown_until

def get_model(complexity, skip_models=None):
    if skip_models is None:
        skip_models = []
    
    status = load_status()
    current_time = time.time()
    
    chain = CHAINS.get(complexity, CHAINS["medium"])
    
    for key in chain:
        if key in skip_models or MODELS[key] in skip_models:
            continue
        if is_model_available(key, status, current_time):
            # Print the actual model string
            print(MODELS[key])
            return 0
            
    # If all preferred models are on cooldown, just print the first one from the chain
    # that we haven't skipped (or fallback to glm)
    for key in chain:
        if key not in skip_models and MODELS[key] not in skip_models:
            print(MODELS[key])
            return 0
    
    # Last resort
    print(MODELS["glm"])
    return 0

def report_failure(model_name):
    # Find the key for this model
    model_key = None
    for k, v in MODELS.items():
        if v == model_name or k == model_name:
            model_key = k
            break
            
    if not model_key:
        model_key = model_name  # Custom model
        
    status = load_status()
    current_time = time.time()
    
    if model_key not in status:
        status[model_key] = {}
        
    status[model_key]["cooldown_until"] = current_time + DEFAULT_COOLDOWN_SECONDS
    status[model_key]["last_failure"] = current_time
    status[model_key]["failures"] = status[model_key].get("failures", 0) + 1
    
    save_status(status)
    print(f"Reported failure for {model_key}. Cooldown until {time.ctime(status[model_key]['cooldown_until'])}")

def main():
    parser = argparse.ArgumentParser(description="Model Selector and Health Monitor")
    parser.add_argument("--get-model", choices=["high", "medium", "low"], help="Get best available model for complexity")
    parser.add_argument("--report-failure", metavar="MODEL", help="Report a rate limit/failure for a model")
    parser.add_argument("--skip", nargs="*", default=[], help="List of model keys to skip")
    
    args = parser.parse_args()
    
    if args.report_failure:
        report_failure(args.report_failure)
    elif args.get_model:
        sys.exit(get_model(args.get_model, args.skip))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
