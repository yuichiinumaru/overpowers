#!/usr/bin/env python3
import sys
import subprocess

def delegate_task(prompt, model=None, format="text", input_data=None):
    cmd = ["gemini", "-y"]
    if model:
        cmd.extend(["-m", model])
    if format == "json":
        cmd.extend(["-o", "json"])
    
    cmd.append(prompt)
    
    print(f"Delegating task: '{prompt}'")
    try:
        if input_data:
            result = subprocess.run(cmd, input=input_data, text=True, capture_output=True)
        else:
            result = subprocess.run(cmd, capture_output=True, text=True)
            
        print("--- Output ---")
        print(result.stdout)
        
        if result.returncode != 0:
            print(f"\nTask failed with exit code: {result.returncode}")
            print("Errors:")
            print(result.stderr)
            return False
            
        print("\nTask completed successfully.")
        return True
        
    except FileNotFoundError:
        print("Error: 'gemini' CLI not found.")
        return False
    except Exception as e:
        print(f"Error executing task: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: delegate_task.py <prompt> [model] [format] [input_file]")
        sys.exit(1)
        
    prompt = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else None
    fmt = sys.argv[3] if len(sys.argv) > 3 else "text"
    
    input_data = None
    if len(sys.argv) > 4:
        try:
            with open(sys.argv[4], 'r') as f:
                input_data = f.read()
        except Exception as e:
            print(f"Could not read input file: {e}")
            sys.exit(1)
            
    delegate_task(prompt, model, fmt, input_data)
