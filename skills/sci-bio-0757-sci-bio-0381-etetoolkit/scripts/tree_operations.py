import sys
import argparse
from ete3 import Tree

def tree_stats(tree_path, format=0):
    t = Tree(tree_path, format=format)
    print(f"--- Tree Statistics: {tree_path} ---")
    print(f"Leaves: {len(t)}")
    print(f"Total nodes: {len(list(t.traverse()))}")
    print(f"Is rooted: {t.is_rooted()}")
    print(f"Maximum depth: {t.get_distance(t.get_leaves()[0], t)}")

def tree_convert(in_path, out_path, in_fmt=0, out_fmt=1):
    t = Tree(in_path, format=in_fmt)
    t.write(outfile=out_path, format=out_fmt)
    print(f"✅ Converted {in_path} to {out_path} (format {out_fmt})")

def tree_reroot(in_path, out_path, midpoint=True, outgroup=None):
    t = Tree(in_path)
    if midpoint:
        m = t.get_midpoint_outgroup()
        t.set_outgroup(m)
        print("✅ Rooted at midpoint")
    elif outgroup:
        t.set_outgroup(outgroup)
        print(f"✅ Rooted at {outgroup}")
    t.write(outfile=out_path)

def tree_prune(in_path, out_path, taxa_list):
    t = Tree(in_path)
    taxa = taxa_list.split(',')
    t.prune(taxa, preserve_branch_length=True)
    t.write(outfile=out_path)
    print(f"✅ Pruned tree to {len(taxa)} taxa, saved to {out_path}")

def main():
    parser = argparse.ArgumentParser(description="ETE Tree Operations")
    subparsers = parser.add_subparsers(dest="command")

    # Stats
    p_stats = subparsers.add_parser("stats")
    p_stats.add_argument("tree")

    # Convert
    p_conv = subparsers.add_parser("convert")
    p_conv.add_argument("tree")
    p_conv.add_argument("output")
    p_conv.add_argument("--in-fmt", type=int, default=0)
    p_conv.add_argument("--out-fmt", type=int, default=1)

    # Reroot
    p_root = subparsers.add_parser("reroot")
    p_root.add_argument("tree")
    p_root.add_argument("output")
    p_root.add_argument("--midpoint", action="store_true")
    p_root.add_argument("--outgroup")

    # Prune
    p_prune = subparsers.add_parser("prune")
    p_prune.add_argument("tree")
    p_prune.add_argument("output")
    p_prune.add_argument("--taxa", help="Comma-separated list of taxa")

    # ASCII
    p_ascii = subparsers.add_parser("ascii")
    p_ascii.add_argument("tree")

    args = parser.parse_args()

    if args.command == "stats":
        tree_stats(args.tree)
    elif args.command == "convert":
        tree_convert(args.tree, args.output, args.in_fmt, args.out_fmt)
    elif args.command == "reroot":
        tree_reroot(args.tree, args.output, args.midpoint, args.outgroup)
    elif args.command == "prune":
        tree_prune(args.tree, args.output, args.taxa)
    elif args.command == "ascii":
        t = Tree(args.tree)
        print(t.get_ascii(show_internal=True))

if __name__ == "__main__":
    main()
