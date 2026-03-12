#!/usr/bin/env python3
import argparse
import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, count) for char, count in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(node, prefix="", code_dict={}):
    if node is not None:
        if node.char is not None:
            code_dict[node.char] = prefix
        build_codes(node.left, prefix + "0", code_dict)
        build_codes(node.right, prefix + "1", code_dict)
    return code_dict

def main():
    parser = argparse.ArgumentParser(description="Demonstrate basic source coding (Huffman compression).")
    parser.add_argument("text", help="Text string to encode")

    args = parser.parse_args()

    if not args.text:
        return

    tree = build_huffman_tree(args.text)
    codes = build_codes(tree, "", {})

    encoded = "".join(codes[char] for char in args.text)

    print("Character Frequencies:")
    for char, count in Counter(args.text).most_common():
        print(f"  '{char}': {count} -> {codes[char]}")

    print(f"\nOriginal text size (8 bits/char): {len(args.text) * 8} bits")
    print(f"Encoded text size: {len(encoded)} bits")
    compression_ratio = len(encoded) / (len(args.text) * 8)
    print(f"Compression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    main()
