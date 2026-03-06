#!/usr/bin/env python3
import os

SUB_SKILLS = [
    "defi-protocol-templates",
    "nft-standards",
    "solidity-security",
    "web3-testing"
]

def main():
    print("--- Blockchain & Web3 Sub-Skills ---")
    base_path = "skills/sec-safety-0939-sec-safety-0145-blockchain-web3/skills"
    for skill in SUB_SKILLS:
        skill_path = os.path.join(base_path, skill)
        exists = os.path.exists(skill_path)
        status = "[Found]" if exists else "[Missing]"
        print(f"{status} {skill}")

if __name__ == "__main__":
    main()
