#!/usr/bin/env python3
import sys
import subprocess

def run_gemini_query(prompt, model=None, output_format=None):
    cmd = ["gemini"]
    if model:
        cmd.extend(["--model", model])
    if output_format:
        cmd.extend(["--output-format", output_format])
    
    cmd.append(prompt)
    
    print(f"Running command: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing gemini CLI: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: one_shot_query.py <prompt> [model] [output_format]")
        sys.exit(1)
    
    prompt = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else None
    fmt = sys.argv[3] if len(sys.argv) > 3 else None
    
    run_gemini_query(prompt, model, fmt)
