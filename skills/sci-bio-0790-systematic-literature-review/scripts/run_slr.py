import argparse
import subprocess

def run_pipeline(topic, mode):
    print(f"Starting Systematic Literature Review for: {topic} (Mode: {mode})")
    # Call the actual pipeline scripts as defined in SKILL.md
    # subprocess.run(["python", "scripts/run_pipeline.py", "--topic", topic, "--mode", mode])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SLR pipeline runner")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--mode", choices=['Premium', 'Standard', 'Basic'], default='Premium')
    args = parser.parse_args()
    run_pipeline(args.topic, args.mode)
