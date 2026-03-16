#!/usr/bin/env python3
import importlib.util
import sys

def check_package(name):
    spec = importlib.util.find_spec(name)
    if spec is not None:
        print(f"[OK] {name} is installed.")
        return True
    else:
        print(f"[!] {name} is NOT installed.")
        return False

def main():
    frameworks = ["tensorflow_federated", "syft", "ibm_fl"]
    print("--- Federated Learning Framework Inventory ---\n")
    
    found = 0
    for fw in frameworks:
        if check_package(fw):
            found += 1
            
    print(f"\nFound {found} of {len(frameworks)} recommended frameworks.")
    if found == 0:
        print("\nTo get started, consider installing one of these:")
        print("- pip install tensorflow-federated")
        print("- pip install syft")

if __name__ == "__main__":
    main()
