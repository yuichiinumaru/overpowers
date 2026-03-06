#!/usr/bin/env python3
import sys

def setup_pentest(target_account):
    print(f"Setting up AWS Pentesting rules and scope for: {target_account}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        setup_pentest(sys.argv[1])
    else:
        print("Usage: ./aws_pentest_setup.py <target_account_id>")
