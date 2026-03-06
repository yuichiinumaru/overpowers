import sys
import json

def analyze_context(token_count, turn_count):
    print("Context Degradation Analysis:")
    print("-" * 30)
    print(f"Total Tokens: {token_count}")
    print(f"Conversation Turns: {turn_count}")
    
    if token_count > 60000:
        print("\nWARNING: High risk of context degradation.")
        print("- Potential 'lost-in-middle' phenomenon.")
        print("- Consider compaction or isolation strategies.")
    elif token_count > 25000:
        print("\nNOTICE: Moderate context length.")
        print("- Monitor for context distraction.")
        print("- Ensure critical information is at edges.")
    else:
        print("\nSTATUS: Context size is within safe limits.")
        print("- Degradation risk is currently low.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python context_degradation_analyzer.py <token_count> <turn_count>")
        sys.exit(1)
    
    analyze_context(int(sys.argv[1]), int(sys.argv[2]))
