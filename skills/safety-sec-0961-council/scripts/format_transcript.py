import sys
import json

def format_debate(rounds):
    output = "# Council Debate Transcript\n\n"
    for i, round_data in enumerate(rounds):
        output += f"## Round {i+1}\n\n"
        for agent, contribution in round_data.items():
            output += f"### {agent}\n{contribution}\n\n"
    return output

if __name__ == "__main__":
    # Expects JSON input from stdin
    try:
        data = json.load(sys.stdin)
        print(format_debate(data))
    except Exception as e:
        print(f"Error formatting transcript: {e}")
