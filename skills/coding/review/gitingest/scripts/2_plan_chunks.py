import os
import json
import argparse

def process_directory(node, min_size, max_size):
    """
    Bottom-up greedy bucketing of files and subdirectories.
    Returns: (leftover_items_list, completed_chunks_list)
    """
    chunks = []
    
    # If this entire directory (including all subdirs) is small enough, 
    # and > 0, we can just treat it as a single splittable item for the parent.
    if node["size"] <= max_size and node["size"] > 0:
        return [node], chunks

    # Otherwise, it's too big, so we must process its children
    items_to_bucket = []
    for child in node.get("children", []):
        if child["type"] == "directory":
            child_leftovers, child_chunks = process_directory(child, min_size, max_size)
            items_to_bucket.extend(child_leftovers)
            chunks.extend(child_chunks)
        else:
            if child["size"] > 0:
                items_to_bucket.append(child)
                
    # Now, try to bucket items_to_bucket
    state = {"bucket": [], "size": 0, "index": 1}
    
    def flush():
        if not state["bucket"]: return
        
        name_prefix = node["path"].replace(os.sep, "-") if node["path"] else "root"
        # If we have multiple buckets for this directory, append part index
        chunk_name = f"{name_prefix}_part{state['index']}.md" if len(items_to_bucket) > len(state["bucket"]) else f"{name_prefix}.md"
        
        includes = []
        for i in state["bucket"]:
            if i["type"] == "directory":
                # Ensure the wildcard suffix is correctly joined
                includes.append(f"{i['path']}/**")
            else:
                includes.append(i["path"])
                
        chunks.append({
            "name": chunk_name,
            "includes": includes,
            "size": state["size"]
        })
        state["bucket"] = []
        state["size"] = 0
        state["index"] += 1

    for item in items_to_bucket:
        # If adding this item exceeds max_size, and our bucket is already at least min_size, flush first.
        if state["size"] + item["size"] > max_size and state["size"] >= min_size:
            flush()
            
        state["bucket"].append(item)
        state["size"] += item["size"]
        
        # If a single huge file/dir or accumulated bucket exceeds max_size, flush it immediately.
        if state["size"] >= max_size:
            flush()
            
    # Deal with leftovers
    if state["bucket"]:
        if state["size"] < min_size:
            # Pass it up to the parent to combine with other small directories/files
            return state["bucket"], chunks
        else:
            flush()
            
    return [], chunks

def main():
    parser = argparse.ArgumentParser(description="Plan chunks from analyzed tree.")
    parser.add_argument("analysis_file", help="Path to tree_analysis.json")
    parser.add_argument("--min-size", type=int, default=20000, help="Min chunk size in bytes (default 20KB)")
    parser.add_argument("--max-size", type=int, default=100000, help="Max chunk size in bytes (default 100KB)")
    parser.add_argument("-o", "--output", default="chunks_plan.json", help="Output chunks plan JSON")
    
    args = parser.parse_args()
    
    with open(args.analysis_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    tree = data["tree"]
    repo_path = data["repo_path"]
    
    leftovers, chunks = process_directory(tree, args.min_size, args.max_size)
    
    # If the root has leftovers, we flush them into a final 'root_misc.md' chunk
    if leftovers:
        includes = []
        for i in leftovers:
            if i["type"] == "directory":
                includes.append(f"{i['path']}/**")
            else:
                includes.append(i["path"])
                
        chunks.append({
            "name": "root_misc.md",
            "includes": includes,
            "size": sum(i["size"] for i in leftovers)
        })
    
    plan = {
        "repo_path": repo_path,
        "min_size_target": args.min_size,
        "max_size_target": args.max_size,
        "total_chunks": len(chunks),
        "chunks": chunks
    }
    
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)
        
    print(f"Plan generated: {len(chunks)} chunks targeted (Between {args.min_size/1000}k and {args.max_size/1000}k).")
    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
