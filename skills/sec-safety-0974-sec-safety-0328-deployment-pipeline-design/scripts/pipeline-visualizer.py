#!/usr/bin/env python3
import sys

def main():
    stages = ["Source", "Build", "Test", "Staging", "Approve", "Production"]
    
    print("\n--- Deployment Pipeline Visualization ---\n")
    
    pipeline_str = ""
    for i, stage in enumerate(stages):
        box = f"[{stage}]"
        pipeline_str += box
        if i < len(stages) - 1:
            pipeline_str += " --> "
            
    print(pipeline_str)
    print("\nStage Descriptions:")
    print("1. Source: Code checkout and metadata extraction")
    print("2. Build: Compilation and containerization")
    print("3. Test: Unit, integration, and security scans")
    print("4. Staging: Environment deployment and E2E testing")
    print("5. Approve: Manual or automated gate")
    print("6. Production: Final rollout (Canary/Blue-Green)")
    print("\n----------------------------------------\n")

if __name__ == "__main__":
    main()
