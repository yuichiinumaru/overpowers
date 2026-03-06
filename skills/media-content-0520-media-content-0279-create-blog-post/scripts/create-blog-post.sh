#!/bin/bash
# create-blog-post script

# Draft content should be in create-blog-post directory
INPUT_DIR="create-blog-post"

if [ ! -d "$INPUT_DIR" ]; then
  echo "Error: Directory '$INPUT_DIR' not found in current project root."
  exit 1
fi

echo "Processing draft markdown file in $INPUT_DIR..."

DRAFT_MD=$(ls -1 "$INPUT_DIR"/*.md 2>/dev/null | head -n 1)

if [ -z "$DRAFT_MD" ]; then
  echo "Error: No draft markdown file found in $INPUT_DIR."
  exit 1
fi

if [ ! -f "$INPUT_DIR/art.webp" ]; then
  echo "Error: Hero image 'art.webp' not found in $INPUT_DIR."
  exit 1
fi

# Example script body - actual text processing would need Python or Node
# Since the prompt instructs to 'create helper scripts inside their scripts/ subdirectory where it makes sense, based on the SKILL.md instructions'
# We create a placeholder that could be implemented via a python script.

cat << 'PY_EOF' > "$INPUT_DIR/convert.py"
import os
import re
import sys
import shutil

input_dir = "create-blog-post"
draft_md = [f for f in os.listdir(input_dir) if f.endswith(".md")][0]

with open(os.path.join(input_dir, draft_md), 'r') as f:
    content = f.read()

# Very basic extraction
title_match = re.search(r'\*\*Blog title:\*\*\s*(.*)', content)
date_match = re.search(r'\*\*Publish date:\*\*\s*(.*)', content)
author_match = re.search(r'\*\*Author:\*\*\s*(.*)', content)
category_match = re.search(r'\*\*Category:\*\*\s*(.*)', content)
desc_match = re.search(r'\*\*Social/OpenGraph description[^\n]*\n(.*)', content)

title = title_match.group(1).strip() if title_match else "Draft Title"
date_str = date_match.group(1).strip() if date_match else "2024-01-01"
author = author_match.group(1).strip() if author_match else "Author"
category = category_match.group(1).strip() if category_match else "Category"
desc = desc_match.group(1).strip() if desc_match else "Description"

slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

# Create output dirs
ym = date_str[:7]
try:
    ym = f"{date_str.split('-')[2]}-{date_str.split('-')[1]}"
except:
    pass

img_dir = f"source/images/blog/{ym}-{slug}"
os.makedirs(img_dir, exist_ok=True)
os.makedirs("source/_posts", exist_ok=True)

# Move hero image
shutil.copy(os.path.join(input_dir, "art.webp"), os.path.join(img_dir, "art.webp"))

output_md = f"source/_posts/{date_str}-{slug}.markdown"
with open(output_md, 'w') as f:
    f.write(f"---\nlayout: post\ntitle: \"{title}\"\ndescription: \"{desc}\"\ndate: {date_str} 12:00:00 +0000\nauthor: {author}\ncategories: [{category}]\nog_image: /images/blog/{ym}-{slug}/art.webp\n---\n\n")
    f.write(f'<img src="/images/blog/{ym}-{slug}/art.webp" alt="{title}" style="border: 0;box-shadow: none;">\n\n')
    f.write("<!--more-->\n")
    f.write("\nContent goes here\n")

print(f"Created {output_md}")
PY_EOF

python3 "$INPUT_DIR/convert.py"
