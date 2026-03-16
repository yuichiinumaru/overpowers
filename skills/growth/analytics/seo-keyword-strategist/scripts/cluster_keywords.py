#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict

def simple_cluster(keywords):
    clusters = defaultdict(list)

    # Very basic token-based clustering
    for kw in keywords:
        kw_clean = kw.lower().strip()
        tokens = set(kw_clean.split())

        # Try to find a matching cluster
        matched = False
        for cluster_name, items in clusters.items():
            cluster_tokens = set(cluster_name.split())
            # If significant overlap, add to cluster
            if len(tokens.intersection(cluster_tokens)) > 0:
                clusters[cluster_name].append(kw)
                matched = True
                break

        if not matched:
            # Create new cluster using the keyword itself as the name
            clusters[kw_clean].append(kw)

    return dict(clusters)

def main():
    parser = argparse.ArgumentParser(description="Basic keyword clustering tool.")
    parser.add_argument("--input", required=True, help="Input file with keywords (one per line)")
    parser.add_argument("--output", help="Output JSON file")

    args = parser.parse_args()

    with open(args.input, "r") as f:
        keywords = [line.strip() for line in f if line.strip()]

    clusters = simple_cluster(keywords)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(clusters, f, indent=2)
        print(f"Clustered {len(keywords)} keywords into {len(clusters)} clusters. Saved to {args.output}")
    else:
        print(json.dumps(clusters, indent=2))

if __name__ == "__main__":
    main()
