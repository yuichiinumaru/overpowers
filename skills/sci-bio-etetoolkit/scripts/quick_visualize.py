import sys
import argparse
from ete3 import Tree, TreeStyle

def visualize_tree(tree_path, output_path, mode='r', show_leaf_name=True, title=None):
    """
    Quickly renders a tree to a file.
    mode: 'r' for rectangular, 'c' for circular
    """
    try:
        t = Tree(tree_path)
        ts = TreeStyle()
        ts.mode = mode
        ts.show_leaf_name = show_leaf_name
        
        if title:
            ts.title.add_face(TextFace(title, fsize=15), column=0)

        # Basic rendering - requires PyQt for graphical output
        # If PyQt is missing, this will fail gracefully
        t.render(output_path, tree_style=ts)
        print(f"✅ Tree rendered to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Note: Rendering requires PyQt5 installed in the environment.")

def main():
    parser = argparse.ArgumentParser(description="Quick ETE Tree Visualization")
    parser.add_argument("tree", help="Input Newick file")
    parser.add_argument("output", help="Output file (pdf, png, svg)")
    parser.add_argument("--mode", default="r", choices=['r', 'c'], help="r=rect, c=circular")
    parser.add_argument("--hide-names", action="store_false", dest="show_names")
    parser.add_argument("--title", help="Plot title")

    args = parser.parse_args()
    visualize_tree(args.tree, args.output, args.mode, args.show_names, args.title)

if __name__ == "__main__":
    main()
