import subprocess
import json
import argparse
import sys

def deep_dive(trace_id):
    print(f"🎯 Analyzing Trace: {trace_id}\n")
    
    try:
        # Fetch trace in JSON format
        cmd = ["langsmith-fetch", "trace", trace_id, "--format", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        trace_data = json.loads(result.stdout)
        
        # In a real scenario, we would parse the actual LangSmith trace structure
        # Here we mock the analysis output based on the skill description
        print("Execution Flow:")
        # Mock parsing logic
        for idx, step in enumerate(trace_data.get('steps', []), 1):
            status = "✅" if step.get('success') else "❌"
            print(f"{idx}. {status} {step.get('tool')}({step.get('args')})")
            
        print(f"\nToken Usage: {trace_data.get('usage', {}).get('total_tokens', 'Unknown')}")
        print(f"Execution Time: {trace_data.get('duration', 'Unknown')}s")
        
    except subprocess.CalledProcessError as e:
        print(f"Error fetching trace: {e.stderr}")
    except Exception as e:
        print(f"Analysis error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Deep dive into a specific LangSmith trace')
    parser.add_argument('trace_id', help='The ID of the trace to analyze')
    
    args = parser.parse_args()
    deep_dive(args.trace_id)

if __name__ == "__main__":
    main()
