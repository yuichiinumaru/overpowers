#!/usr/bin/env python3
"""
Article Template Generator Helper

Scaffolds a new article by copying the requested template into _posts
with current date prefix.

Usage:
  python3 article_template.py --title "My New Post" --author "orta" --template "regular-post"
"""

import argparse
import datetime
import os
import sys

def generate_article(title, author, template, categories="Tech"):
    today = datetime.date.today().strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-")
    filename = f"{today}-{slug}.markdown"

    # Normally we would copy from Post-Templates/, but here we just generate content
    print(f"Creating article {filename} using template {template} for author {author}...")

    content = f"""---
layout: post
title: "{title}"
date: {today} 12:00:00 -0500
author: {author}
categories: [{categories}]
---

# Introduction

Write your amazing content here.
"""
    print("\nFile Content Preview:")
    print(content)
    print("\nTo actually write this, use:")
    print(f"cat << 'EOF' > _posts/{filename}")
    print(content)
    print("EOF")

def main():
    parser = argparse.ArgumentParser(description="Article Template Generator")
    parser.add_argument("--title", required=True, help="Post title")
    parser.add_argument("--author", required=True, help="Author key (must exist in _config.yml)")
    parser.add_argument("--template", choices=["regular-post", "long-post", "epic-post"], default="regular-post")
    parser.add_argument("--categories", default="Tech", help="Comma separated categories")

    args = parser.parse_args()
    generate_article(args.title, args.author, args.template, args.categories)

if __name__ == "__main__":
    main()
