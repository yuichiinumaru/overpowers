#!/usr/bin/env python3
import argparse
import json

def generate_prompts(subject, style, action, environment):
    prompts = [
        f"{subject} doing {action} in {environment}. {style} style, 4k resolution, cinematic lighting.",
        f"A tracking shot of {subject} doing {action} through {environment}. Shot on 35mm lens, {style} aesthetic.",
        f"Close up on {subject}'s details while {action} in {environment}. {style}, hyper-realistic textures, slow motion.",
        f"Drone view descending upon {environment} where {subject} is {action}. Beautiful {style} colors and lighting."
    ]
    return prompts

def main():
    parser = argparse.ArgumentParser(description="Generate varied prompt structures for Sora video generation.")
    parser.add_argument("--subject", required=True, help="Main subject/character")
    parser.add_argument("--action", required=True, help="What the subject is doing")
    parser.add_argument("--environment", required=True, help="The setting or background")
    parser.add_argument("--style", required=True, help="Visual style (e.g., photorealistic, cyberpunk, anime)")
    parser.add_argument("--output", help="Output JSON file")

    args = parser.parse_args()

    prompts = generate_prompts(args.subject, args.style, args.action, args.environment)

    if args.output:
        with open(args.output, "w") as f:
            json.dump({"prompts": prompts}, f, indent=2)
        print(f"Saved {len(prompts)} prompts to {args.output}")
    else:
        for i, p in enumerate(prompts):
            print(f"Prompt {i+1}:\n{p}\n")

if __name__ == "__main__":
    main()
