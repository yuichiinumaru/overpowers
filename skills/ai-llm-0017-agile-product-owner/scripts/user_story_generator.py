#!/usr/bin/env python3
import sys
import json

def generate_story(epic):
    return {
        "story": f"As a user, I want to {epic} so that I can achieve my goal.",
        "acceptance_criteria": [
            "Verify the feature works as expected",
            "Ensure edge cases are handled",
            "Validate performance requirements"
        ],
        "points": 3,
        "priority": "Medium"
    }

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sprint":
        capacity = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        print(f"Planning sprint with capacity: {capacity} points")
    else:
        epic = input("Enter Epic description: ") if len(sys.argv) == 1 else sys.argv[1]
        story = generate_story(epic)
        print(json.dumps(story, indent=2))
