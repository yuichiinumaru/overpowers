#!/usr/bin/env python3
"""
Markdown-to-TOML converter for Gemini CLI commands.

Converts workflow .md files (with YAML frontmatter) into .toml command files.

Key design decisions:
  - Uses TOML multi-line LITERAL strings (''') for the prompt body.
    This avoids TOML interpreting backslashes as escape sequences, which
    is critical since Markdown content is full of literal backslashes
    (e.g., \\n in regex, \\* in grep, \\| in bash pipes).
  - Escapes inner double-quotes in the description field.
  - Handles edge cases where the body itself contains ''' by replacing
    with the unicode equivalent.
"""
import os
import sys
import yaml
import pathlib


def md_to_toml(md_path, output_dir):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            # Fallback for files without frontmatter
            description = "Custom workflow"
            body = content.strip()
        else:
            try:
                metadata = yaml.safe_load(parts[1]) or {}
                description = metadata.get('description', 'Custom workflow')
                body = parts[2].strip()
            except Exception:
                description = "Custom workflow"
                body = content.strip()

        name = pathlib.Path(md_path).stem
        output_path = os.path.join(output_dir, f"{name}.toml")

        # Clean description for TOML — escape inner double-quotes
        if isinstance(description, str):
            description = description.replace('\\', '\\\\').replace('"', '\\"')
        else:
            description = "Custom workflow"

        # Sanitize body for TOML literal strings:
        # Multi-line literal strings (''') cannot contain ''' sequences.
        # Replace any occurrence of ''' in the body with escaped alternative.
        body = body.replace("'''", "' ' '")

        toml_content = f"description = \"{description}\"\n\nprompt = '''\n{body}\n'''\n"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(toml_content)
        print(f"✅ Converted: {name}.toml")

    except Exception as e:
        print(f"❌ Error converting {md_path}: {e}")


def main():
    if len(sys.argv) < 3:
        print("Usage: md-to-toml.py <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)

    # --- Cleanup orphaned TOML files (from renamed/deleted .md workflows) ---
    source_stems = {
        pathlib.Path(f).stem
        for f in os.listdir(input_dir)
        if f.endswith('.md')
    }
    orphans_removed = 0
    for toml_file in list(os.listdir(output_dir)):
        if toml_file.endswith('.toml'):
            stem = pathlib.Path(toml_file).stem
            if stem not in source_stems:
                os.remove(os.path.join(output_dir, toml_file))
                print(f"🗑️  Removed orphan: {toml_file}")
                orphans_removed += 1
    if orphans_removed:
        print(f"   Cleaned {orphans_removed} orphaned TOML files.\n")

    count = 0
    for file in sorted(os.listdir(input_dir)):
        if file.endswith('.md'):
            md_to_toml(os.path.join(input_dir, file), output_dir)
            count += 1

    print(f"\nDone! Processed {count} files.")


if __name__ == "__main__":
    main()
