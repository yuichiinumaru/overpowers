import argparse
import os
import re

def main():
    parser = argparse.ArgumentParser(description="Copy Editing Sweeper (Seven Sweeps)")
    parser.add_argument("file", help="Path to copy file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Error: {args.file} not found.")
        return
        
    with open(args.file, "r") as f:
        content = f.read()
        
    sweeps = [
        "Clarity (Confusing sentences, jargon)",
        "Voice and Tone (Consistency)",
        "So What (Features vs Benefits)",
        "Prove It (Social proof, evidence)",
        "Specificity (Concrete details, numbers)",
        "Heightened Emotion (Emotional triggers)",
        "Zero Risk (Removing friction, CTAs)"
    ]
    
    print(f"--- Seven Sweeps Analysis for {args.file} ---")
    
    # Simple automated checks
    words = content.split()
    print(f"Word count: {len(words)}")
    
    filler_words = ["very", "really", "extremely", "just", "actually", "basically"]
    found_filler = [w for w in filler_words if w in content.lower()]
    if found_filler:
        print(f"Recommended Removal: {found_filler} (filler words)")
        
    passive_voice = ["is being", "was being", "been done"] # very basic
    if any(pv in content.lower() for pv in passive_voice):
        print("Check for Passive Voice: Active voice is stronger for marketing.")

    print("\nNext Steps (Manual Sweeps):")
    for i, sweep in enumerate(sweeps, 1):
        print(f"{i}. {sweep}")

if __name__ == "__main__":
    main()
