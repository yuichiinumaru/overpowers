#!/usr/bin/env python3
import sys

def detect_manipulation(text):
    patterns = {
        "urgency": ["act now", "limited time", "hurry", "urgent"],
        "authority_claims": ["trust me", "experts agree", "studies show"],
        "social_proof": ["everyone is", "don't be left behind", "thousands have"],
        "fear_uncertainty": ["you'll regret", "they don't want you to know"],
        "grandiosity": ["revolutionary", "new order", "empire"],
        "dominance_assertions": ["you will all", "fall in line"],
        "us_vs_them": ["enemies", "the elite", "sheeple"]
    }

    score = 0
    text_lower = text.lower()

    for category, words in patterns.items():
        for word in words:
            if word in text_lower:
                score += 5
                print(f"Detected {category}: '{word}'")

    return score

def main():
    text = ""
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    score = detect_manipulation(text)
    print(f"\nFinal Score: {score}")
    if score < 5:
        print("✅ LOW — probably fine")
    elif score < 15:
        print("⚠️ MODERATE — read critically")
    else:
        print("🚨 HIGH — strong skepticism warranted")

if __name__ == "__main__":
    main()
