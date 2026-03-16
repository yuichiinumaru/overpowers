#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
import json
import re
import argparse

def run_cmd(cmd, capture=True, **kwargs):
    """Run a command and optionally capture its output."""
    try:
        if capture:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, **kwargs)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=True, **kwargs)
            return None
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error executing command: {' '.join(cmd)}")
        if capture:
            print(f"Stderr: {e.stderr}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Upload Gitingest chunks to NotebookLM.")
    parser.add_argument("chunks_dir", type=str, help="Directory containing the .md chunks")
    parser.add_argument("notebook_name", type=str, help="Name of the NotebookLM notebook")
    parser.add_argument("-y", "--yes", action="store_true", help="Automatically use existing notebook if found")
    parser.add_argument("-n", "--no-reuse", action="store_true", help="Automatically create a new notebook even if one exists")
    
    args = parser.parse_args()

    chunks_dir = Path(args.chunks_dir)
    notebook_name = args.notebook_name

    if not chunks_dir.exists() or not chunks_dir.is_dir():
        print(f"❌ Chunks directory not found: {chunks_dir}")
        sys.exit(1)

    # 1. Check login
    print("🔐 Checking authentication...")
    try:
        subprocess.run(["nlm", "login", "--check"], check=True, capture_output=True)
        print("✅ Authenticated.")
    except subprocess.CalledProcessError:
        print("⚠️ Authentication expired or missing. Attempting login...")
        if run_cmd(["nlm", "login"], capture=False) is None:
            print("❌ Failed to login. Please run 'nlm login' manually.")
            sys.exit(1)
            
    # 2. Check for existing notebooks
    print("🔍 Checking existing notebooks...")
    nb_id = None
    list_output = run_cmd(["nlm", "notebook", "list", "--json"])
    if list_output:
        try:
            notebooks = json.loads(list_output)
            # Find exact match with notebook title
            existing_nbs = [nb for nb in notebooks if nb.get("title") == notebook_name]
            if existing_nbs:
                # Pick the first match
                existing_nb = existing_nbs[0]
                print(f"⚠️ Found existing notebook '{notebook_name}' (ID: {existing_nb.get('id')})")
                
                use_existing = False
                if args.yes:
                    use_existing = True
                    print("➡️ Auto-selected to USE existing notebook (-y flag).")
                elif args.no_reuse:
                    use_existing = False
                    print("➡️ Auto-selected to CREATE NEW notebook (-n flag).")
                else:
                    ans = input(f"Do you want to upload to this existing notebook? [y/N] (y = Use existing, n = Create new): ").strip().lower()
                    if ans == 'y':
                        use_existing = True
                        
                if use_existing:
                    nb_id = existing_nb.get('id')
                    print(f"✅ Using existing Notebook ID: {nb_id}")
        except json.JSONDecodeError:
            print("⚠️ Failed to parse notebook list API response.")

    # 3. Create new notebook if nb_id was not reused or found
    if not nb_id:
        print(f"\n📓 Creating new NotebookLM notebook: '{notebook_name}'...")
        output = run_cmd(["nlm", "notebook", "create", notebook_name])
        if not output:
            print("❌ Failed to create notebook.")
            sys.exit(1)
            
        print(output)
        
        match = re.search(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', output)
        if not match:
            nb_id = output.split()[-1].strip()
        else:
            nb_id = match.group(0)
            
        print(f"✅ Extracted new Notebook ID: {nb_id}")

    # Aliases can be set for convenience
    run_cmd(["nlm", "alias", "set", notebook_name.lower(), nb_id], capture=False)

    # 4. Deduplication check
    existing_titles = set()
    print("\n🔍 Fetching existing sources for deduplication...")
    sources_output = run_cmd(["nlm", "source", "list", nb_id, "--json"])
    if sources_output:
        try:
            sources = json.loads(sources_output)
            for s in sources:
                if "title" in s:
                    existing_titles.add(s["title"])
            print(f"ℹ️ Found {len(existing_titles)} existing sources in notebook.")
        except json.JSONDecodeError:
            print("⚠️ Failed to parse sources API response. Uploading all...")

    # 5. Upload chunks
    print(f"\n📤 Uploading chunks from {chunks_dir}...")
    all_chunks = sorted(list(chunks_dir.glob("*.md")))
    if not all_chunks:
        print("❌ No .md chunks found in directory.")
        sys.exit(1)
        
    chunks_to_upload = [c for c in all_chunks if c.name not in existing_titles]
    skipped_count = len(all_chunks) - len(chunks_to_upload)
    
    if skipped_count > 0:
        print(f"⏭️ Skipping {skipped_count} chunks that already exist in the notebook.")
        
    if not chunks_to_upload:
        print("✅ All chunks are already uploaded! Nothing to do.")
    else:
        for i, chunk in enumerate(chunks_to_upload, 1):
            print(f"  [{i}/{len(chunks_to_upload)}] Uploading {chunk.name}...")
            
            cmd = ["nlm", "source", "add", nb_id, "--file", str(chunk.resolve())]
            
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                print("    ✅ Uploaded successfully.")
            except subprocess.CalledProcessError as e:
                # Fallback to text if --file isn't supported by the CLI natively
                print(f"    ⚠️ --file failed, falling back to --text: {e.stderr.decode('utf-8', errors='ignore') if e.stderr else 'Unknown Error'}")
                
                content = chunk.read_text(encoding="utf-8")
                cmd_fallback = ["nlm", "source", "add", nb_id, "--title", chunk.name, "--text", content]
                try:
                    subprocess.run(cmd_fallback, check=True, capture_output=True)
                    print("    ✅ Uploaded successfully via --text.")
                except subprocess.CalledProcessError as e2:
                    print(f"    ❌ Failed to upload {chunk.name}: {e2.stderr.decode('utf-8', errors='ignore') if e2.stderr else 'Unknown Error'}")

    print("\n✅ All chunks uploaded/verified!")

    # 6. Batch Querying Test
    print("\n🧪 Testing batch queries...")
    test_questions = [
        "What is the main purpose of this repository?",
        "Can you summarize the architecture or main components?",
        "Are there any instructions for setting up or contributing?"
    ]

    for q in test_questions:
        print(f"\n❓ Question: {q}")
        print("⏳ Waiting for NotebookLM response...")
        answer = run_cmd(["nlm", "notebook", "query", nb_id, q])
        if answer:
            print(f"\n💡 Answer:\n{answer}")
            print("-" * 60)
        else:
            print("❌ Failed to get an answer.")

    print("\n🎉 Integration test complete!")

if __name__ == "__main__":
    main()
