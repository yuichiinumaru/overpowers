#!/usr/bin/env python3
import subprocess
import requests

def check_docker():
    try:
        result = subprocess.run(["docker", "ps", "--filter", "name=eleutherios", "--format", "{{.Names}}"], capture_output=True, text=True)
        containers = result.stdout.strip().split("\n")
        if any(c for c in containers if c):
            print(f"[OK] Eleutherios containers running: {', '.join(c for c in containers if c)}")
            return True
        else:
            print("[!] No Eleutherios containers found running.")
            return False
    except FileNotFoundError:
        print("[!] Docker command not found.")
        return False

def check_api():
    try:
        response = requests.get("http://localhost:8100/health", timeout=5)
        if response.status_code == 200:
            print("[OK] Eleutherios API healthy on port 8100.")
            return True
        else:
            print(f"[!] Eleutherios API returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"[!] Could not connect to Eleutherios API: {e}")
        return False

def main():
    print("--- Eleutherios Environment Check ---")
    docker = check_docker()
    api = check_api()
    
    if docker and api:
        print("[SUCCESS] Eleutherios is active and ready.")
    else:
        print("[FAILURE] Eleutherios is not properly configured or running.")

if __name__ == "__main__":
    main()
