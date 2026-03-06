#!/usr/bin/env python3
import sys

def build_attack_tree(goal, nodes):
    print(f"Building attack tree for: {goal}")
    print("Nodes:")
    for node in nodes:
        print(f" - {node}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        build_attack_tree(sys.argv[1], sys.argv[2:])
    else:
        print("Usage: ./attack_tree_helper.py <goal> [nodes...]")
