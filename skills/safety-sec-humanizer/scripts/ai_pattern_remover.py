#!/usr/bin/env python3
import sys
import re

def remove_ai_patterns(text):
    print("[*] Removing common AI patterns from text...")

    # Common phrases
    patterns = [
        (r"It is important to note that", ""),
        (r"In conclusion,", ""),
        (r"In summary,", ""),
        (r"Furthermore,", "And"),
        (r"Moreover,", "Also"),
        (r"Additionally,", "Also"),
        (r"As an AI language model,", ""),
        (r"I'm sorry, but", ""),
    ]

    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    print("[+] Done removing patterns.")
    return text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ai_pattern_remover.py <input_file> [<output_file>]")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            content = f.read()

        cleaned_content = remove_ai_patterns(content)

        if len(sys.argv) > 2:
            output_file = sys.argv[2]
            with open(output_file, 'w') as f:
                f.write(cleaned_content)
            print(f"[*] Saved cleaned text to {output_file}")
        else:
            print("\n--- Cleaned Text ---\n")
            print(cleaned_content)

    except Exception as e:
        print(f"[-] Error: {e}")
