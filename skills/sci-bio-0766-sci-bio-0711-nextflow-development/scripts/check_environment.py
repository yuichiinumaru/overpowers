import argparse
import sys
import subprocess

def check_env():
    checks = [
        ("docker", ["docker", "--version"]),
        ("nextflow", ["nextflow", "-v"]),
        ("java", ["java", "-version"])
    ]

    all_passed = True
    print("Checking environment for Nextflow deployment...\n")

    for name, cmd in checks:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                version_info = result.stdout.strip().split('\n')[0] if result.stdout else result.stderr.strip().split('\n')[0]
                print(f"[OK] {name}: {version_info}")
            else:
                print(f"[FAIL] {name} check failed: {result.stderr}")
                all_passed = False
        except FileNotFoundError:
            print(f"[FAIL] {name} is not installed or not in PATH.")
            all_passed = False

    print("\nEnvironment check summary:")
    if all_passed:
        print("✅ All required tools are installed and accessible.")
        sys.exit(0)
    else:
        print("❌ Some required tools are missing or misconfigured.")
        sys.exit(1)

if __name__ == "__main__":
    check_env()
