#!/usr/bin/env python3
"""
Automatically wrap markdown text to 80 characters.
"""
import sys
import textwrap
import argparse

def wrap_markdown(text, width=80):
    lines = text.splitlines()
    wrapped_lines = []
    
    in_code_block = False
    in_table = False
    
    for line in lines:
        # Don't wrap code blocks or tables
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            wrapped_lines.append(line)
            continue
        
        if line.strip().startswith("|"):
            in_table = True
        elif in_table and not line.strip().startswith("|"):
            in_table = False
            
        if in_code_block or in_table or not line.strip():
            wrapped_lines.append(line)
            continue
            
        # Don't wrap headings or list items (simplified)
        if line.strip().startswith(("#", "-", "*", "1.")):
            wrapped_lines.append(line)
            continue
            
        # Wrap normal paragraphs
        wrapped_lines.extend(textwrap.wrap(line, width=width, break_long_words=False, replace_whitespace=False))
        
    return "\n".join(wrapped_lines)

def main():
    parser = argparse.ArgumentParser(description="Wrap markdown text to 80 chars.")
    parser.add_argument("file", help="Markdown file to wrap")
    parser.add_argument("--inplace", action="store_true", help="Modify file in place")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as f:
            content = f.read()
            
        wrapped = wrap_markdown(content)
        
        if args.inplace:
            with open(args.file, 'w') as f:
                f.write(wrapped)
            print(f"Wrapped {args.file}")
        else:
            print(wrapped)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
