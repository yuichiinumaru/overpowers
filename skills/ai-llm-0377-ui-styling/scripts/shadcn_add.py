import subprocess
import sys
import argparse

def add_components(components):
    if not components:
        print("No components specified.")
        return

    cmd = ["npx", "shadcn@latest", "add"] + components
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding components: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add shadcn/ui components.")
    parser.add_argument("components", nargs="+", help="Components to add.")
    args = parser.parse_args()
    add_components(args.components)
