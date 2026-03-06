import subprocess
import sys

def check_command(command, args=None):
    if args is None:
        args = ["--version"]
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {command} is installed: {result.stdout.splitlines()[0]}")
            return True
        else:
            print(f"❌ {command} check failed with return code {result.returncode}")
            return False
    except FileNotFoundError:
        print(f"❌ {command} is not installed.")
        return False

def main():
    deps = sys.argv[1:]
    if not deps:
        print("Usage: check_deps.py <cmd1> <cmd2> ...")
        sys.exit(1)
    
    all_ok = True
    for dep in deps:
        # Special case for npx commands
        if dep.startswith("npx "):
            cmd = dep.split()[1]
            if not check_command("npx", [cmd, "--version"]):
                all_ok = False
        else:
            if not check_command(dep):
                all_ok = False
    
    if not all_ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
