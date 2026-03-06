#!/usr/bin/env python3
import sys

def check_contract(contract_address):
    print(f"Checking Web3 Smart Contract: {contract_address}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        check_contract(sys.argv[1])
    else:
        print("Usage: ./web3_contract_check.py <contract_address>")
