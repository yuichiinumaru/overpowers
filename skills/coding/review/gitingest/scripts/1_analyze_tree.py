import os
import json
import argparse
import pathspec

def get_ignore_spec(repo_path):
    """Load .gitignore and add default ignores."""
    patterns = [
        ".git/", "node_modules/", "__pycache__/", "*.pyc", ".venv/", "venv/",
        "*.png", "*.jpg", "*.jpeg", "*.gif", "*.ico", "*.pdf", "*.mp4", "*.webm"
    ]
    gitignore_path = os.path.join(repo_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8", errors="ignore") as f:
            patterns.extend(f.readlines())
    return pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, patterns)

def build_tree(repo_path):
    """Builds a tree of directories and files with sizes."""
    spec = get_ignore_spec(repo_path)
    
    # We will compute sizes bottom-up later, or during a second pass.
    # It's easier to list all valid files, then build the tree.
    
    valid_files = []
    
    for root, dirs, files in os.walk(repo_path):
        rel_root = os.path.relpath(root, repo_path)
        if rel_root == ".":
            rel_root = ""
            
        # Filter directories in place
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_root, d) + "/")]
        
        for file in files:
            rel_file = os.path.join(rel_root, file) if rel_root else file
            if not spec.match_file(rel_file):
                abs_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(abs_path)
                    valid_files.append({"path": rel_file, "size": size})
                except OSError:
                    pass

    # Build Tree
    tree_root = {"name": os.path.basename(os.path.abspath(repo_path)), "path": "", "type": "directory", "size": 0, "children": {}}
    
    for vf in valid_files:
        parts = vf["path"].split(os.sep)
        current = tree_root
        
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                # File
                current["children"][part] = {"name": part, "path": vf["path"], "type": "file", "size": vf["size"]}
            else:
                # Directory
                current_path = os.sep.join(parts[:i+1])
                if part not in current["children"]:
                    current["children"][part] = {"name": part, "path": current_path, "type": "directory", "size": 0, "children": {}}
                current = current["children"][part]

    # Calculate sizes bottom-up and format children as lists
    def compute_size(node):
        if node["type"] == "file":
            return node["size"]
        
        total_size = 0
        children_list = []
        for child_name, child_node in node["children"].items():
            child_size = compute_size(child_node)
            total_size += child_size
            children_list.append(child_node)
            
        node["size"] = total_size
        node["children"] = children_list
        return total_size

    compute_size(tree_root)
    return tree_root, valid_files

def main():
    parser = argparse.ArgumentParser(description="Analyze directory tree and file sizes.")
    parser.add_argument("repo_path", help="Path to the repository")
    parser.add_argument("-o", "--output", default="tree_analysis.json", help="Output JSON file")
    
    args = parser.parse_args()
    
    tree, files = build_tree(args.repo_path)
    
    output_data = {
        "repo_path": os.path.abspath(args.repo_path),
        "total_files": len(files),
        "total_size": tree["size"],
        "tree": tree
    }
    
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    print(f"Tree analysis completed: {len(files)} files, {tree['size']/1024:.2f} KB total.")
    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
