import subprocess
import sys
import argparse

def init_db(path, dimension=1536, preset=None):
    """
    Initialize AgentDB vector database.
    """
    cmd = ["npx", "agentdb@latest", "init", path, "--dimension", str(dimension)]
    if preset:
        cmd.extend(["--preset", preset])
    
    print(f"Initializing database: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        print(f"Database initialized at {path}")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize AgentDB vector database")
    parser.add_argument("path", help="Path to database file")
    parser.add_argument("--dimension", type=int, default=1536, help="Vector dimension (default: 1536 for OpenAI)")
    parser.add_argument("--preset", choices=["small", "medium", "large"], help="Configuration preset")
    
    args = parser.parse_args()
    init_db(args.path, args.dimension, args.preset)
