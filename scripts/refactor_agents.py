import os
import shutil
import re
import difflib

AGENTS_DIR = 'agents'

def clean_frontmatter(content):
    # Split frontmatter
    # Matches --- at start, content, --- on own line
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return content

    frontmatter_raw = match.group(1)
    body = match.group(2)

    new_frontmatter_lines = []
    for line in frontmatter_raw.split('\n'):
        if line.strip() == '':
            continue
        key_part = line.split(':')[0].strip()
        # Remove fields: tools, model, model_fallback, fallback, fallback_models
        if key_part not in ['tools', 'model', 'model_fallback', 'fallback', 'fallback_models']:
            new_frontmatter_lines.append(line)

    if not new_frontmatter_lines:
        return body # If frontmatter is empty, just return body

    new_frontmatter = '\n'.join(new_frontmatter_lines)
    return f"---\n{new_frontmatter}\n---\n{body}"

def is_similar(content1, content2, threshold=0.9):
    return difflib.SequenceMatcher(None, content1, content2).ratio() > threshold

def process_files():
    # 1. Clean up all files in place first (recursively)
    print("Step 1: Cleaning frontmatter...")
    for root, dirs, files in os.walk(AGENTS_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()

                new_content = clean_frontmatter(content)

                if new_content != content:
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Cleaned {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

    # 2. Move files from subfolders
    print("\nStep 2: Moving files...")
    # Get immediate subdirectories
    subdirs = [d for d in os.listdir(AGENTS_DIR) if os.path.isdir(os.path.join(AGENTS_DIR, d))]

    for subdir in subdirs:
        subdir_path = os.path.join(AGENTS_DIR, subdir)
        for file in os.listdir(subdir_path):
            source_path = os.path.join(subdir_path, file)
            if not os.path.isfile(source_path):
                continue

            dest_path = os.path.join(AGENTS_DIR, file)

            if os.path.exists(dest_path):
                print(f"Conflict detected for {file} in {subdir}")
                # Conflict resolution
                if not file.endswith('.md'):
                     # Rename non-md files directly
                    new_filename = f"{subdir}_{file}"
                    new_dest_path = os.path.join(AGENTS_DIR, new_filename)
                    print(f"Renaming non-md file: {source_path} -> {new_dest_path}")
                    shutil.move(source_path, new_dest_path)
                    continue

                with open(source_path, 'r') as f:
                    source_content = f.read()
                with open(dest_path, 'r') as f:
                    dest_content = f.read()

                if is_similar(source_content, dest_content):
                    print(f"Merging similar file (>90%): {source_path} into {dest_path}")
                    # Extract body from source to append
                    match = re.match(r'^---\s*\n.*?\n---\s*\n(.*)', source_content, re.DOTALL)
                    body_to_append = match.group(1) if match else source_content

                    with open(dest_path, 'a') as f:
                        f.write(f"\n\n## Additional Details from {subdir}/{file}\n\n")
                        f.write(body_to_append)

                    os.remove(source_path)
                else:
                    # Rename and move
                    new_filename = f"{subdir}_{file}"
                    new_dest_path = os.path.join(AGENTS_DIR, new_filename)
                    print(f"Renaming and moving: {source_path} -> {new_dest_path}")
                    shutil.move(source_path, new_dest_path)
            else:
                # No conflict, just move
                print(f"Moving: {source_path} -> {dest_path}")
                shutil.move(source_path, dest_path)

        # Remove empty directory
        try:
            if not os.listdir(subdir_path):
                os.rmdir(subdir_path)
                print(f"Removed empty directory: {subdir_path}")
            else:
                print(f"Directory not empty, skipping removal: {subdir_path}")
        except OSError as e:
            print(f"Error removing directory {subdir_path}: {e}")

if __name__ == '__main__':
    process_files()
