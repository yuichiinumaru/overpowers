#!/usr/bin/env python3
import sys
import subprocess

def check_package():
    try:
        import dxpy
        print(f"[OK] dxpy found (version: {dxpy.__version__})")
        return True
    except ImportError:
        print("[!] dxpy NOT installed.")
        print("    Run: uv pip install dxpy")
        return False

def check_auth():
    try:
        result = subprocess.run(["dx", "whoami"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Authenticated as: {result.stdout.strip()}")
            return True
        else:
            print("[!] Not logged into DNAnexus.")
            print("    Run: dx login")
            return False
    except FileNotFoundError:
        print("[!] dx CLI not found in PATH.")
        return False

def main():
    print("--- DNAnexus Integration Check ---")
    pkg = check_package()
    auth = check_auth()
    
    if pkg and auth:
        print("[SUCCESS] Environment ready for DNAnexus operations.")
    else:
        print("[FAILURE] Environment NOT ready.")

if __name__ == "__main__":
    main()
