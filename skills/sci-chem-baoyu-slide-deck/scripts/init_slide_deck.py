#!/usr/bin/env python3
import argparse
import os
import sys
import re
from datetime import datetime

def generate_slug(text):
    # Simplified slug generation
    slug = re.sub(r'[^\w\s-]', '', text).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug[:30]

def init_deck(content_path, topic_name=None):
    if not os.path.exists(content_path):
        print(f"Error: Content file {content_path} not found.")
        return

    with open(content_path, 'r') as f:
        content = f.read()

    if not topic_name:
        # Try to extract topic from first line
        topic_name = content.split('\n')[0].strip('# ')
    
    slug = generate_slug(topic_name)
    base_dir = f"slide-deck/{slug}"
    
    os.makedirs(f"{base_dir}/prompts", exist_ok=True)
    
    # Save source
    target_source = f"{base_dir}/source-{slug}.md"
    if os.path.exists(target_source):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        os.rename(target_source, f"{base_dir}/source-backup-{timestamp}.md")
    
    with open(target_source, 'w') as f:
        f.write(content)
        
    print(f"Initialized slide deck directory: {base_dir}")
    print(f"Source content saved to: {target_source}")
    
    # Create analysis placeholder
    analysis_file = f"{base_dir}/analysis.md"
    with open(analysis_file, 'w') as f:
        f.write(f"# Analysis: {topic_name}\n\n- Slug: {slug}\n- Date: {datetime.now()}\n- Status: Initialized\n")
    
    print(f"Created analysis file: {analysis_file}")
    return base_dir

def main():
    parser = argparse.ArgumentParser(description='Initialize a Baoyu Slide Deck.')
    parser.add_argument('content', help='Path to source content (markdown file)')
    parser.add_argument('--topic', help='Optional topic name for slug generation')

    args = parser.parse_args()

    init_deck(args.content, args.topic)

if __name__ == "__main__":
    main()
