import os
import argparse
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Art Skill Image Generation Wrapper')
    parser.add_argument('--prompt', required=True, help='Image prompt')
    parser.add_argument('--model', default='nano-banana-pro', help='Model to use')
    parser.add_argument('--name', default='generated-art', help='Base filename')
    parser.add_argument('--workflow', help='Workflow name for notification')
    parser.add_argument('--action', help='Action description for notification')
    
    args = parser.parse_args()
    
    # 1. Mandatory Notification
    if args.workflow and args.action:
        script_dir = Path(__file__).parent
        subprocess.run(['bash', str(script_dir / 'notify.sh'), args.workflow, args.action])
    
    # 2. Enforce Downloads directory
    downloads_dir = Path.home() / "Downloads"
    output_path = downloads_dir / f"{args.name}.png"
    
    print(f"Generating image to: {output_path}")
    print("MANDATORY: Output to Downloads First.")
    
    # In real usage, this would call the actual generation tool
    # Example: bun run ~/.claude/skills/Art/Tools/Generate.ts ...
    
    cmd = [
        "echo", "Mock generating image with", args.model, 
        "--prompt", args.prompt,
        "--output", str(output_path)
    ]
    
    subprocess.run(cmd)
    
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"⚠️  Image should be available at: {output_path}")
    print("⚠️  Please preview in Finder/Preview before use.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == "__main__":
    main()
