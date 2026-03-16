#!/usr/bin/env python3
import json
import argparse
import sys

def calculate_recall_at_k(retrieved, relevant, k):
    if not relevant:
        return 0.0
    top_k = set(retrieved[:k])
    relevant_set = set(relevant)
    return len(top_k.intersection(relevant_set)) / len(relevant_set)

def calculate_precision_at_k(retrieved, relevant, k):
    if k == 0:
        return 0.0
    top_k = set(retrieved[:k])
    relevant_set = set(relevant)
    return len(top_k.intersection(relevant_set)) / k

def calculate_mrr(retrieved, relevant):
    relevant_set = set(relevant)
    for i, doc in enumerate(retrieved):
        if doc in relevant_set:
            return 1.0 / (i + 1)
    return 0.0

def main():
    parser = argparse.ArgumentParser(description="Calculate RAG Retrieval Metrics (Recall@k, Precision@k, MRR)")
    parser.add_argument("input_file", help="JSON file containing list of dicts with 'retrieved' and 'relevant' doc IDs")
    parser.add_argument("-k", type=int, default=5, help="K value for top-k metrics (default: 5)")
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    recalls = []
    precisions = []
    mrrs = []

    for item in data:
        retrieved = item.get('retrieved', [])
        relevant = item.get('relevant', [])

        recalls.append(calculate_recall_at_k(retrieved, relevant, args.k))
        precisions.append(calculate_precision_at_k(retrieved, relevant, args.k))
        mrrs.append(calculate_mrr(retrieved, relevant))

    if not data:
        print("No data found.")
        return

    avg_recall = sum(recalls) / len(recalls)
    avg_precision = sum(precisions) / len(precisions)
    avg_mrr = sum(mrrs) / len(mrrs)

    print(f"Results for {len(data)} queries at K={args.k}:")
    print(f"Mean Recall@{args.k}:    {avg_recall:.4f}")
    print(f"Mean Precision@{args.k}: {avg_precision:.4f}")
    print(f"Mean Reciprocal Rank: {avg_mrr:.4f}")

if __name__ == "__main__":
    main()
