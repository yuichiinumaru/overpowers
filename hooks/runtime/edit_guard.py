#!/usr/bin/env python3
import sys
import re

def analyze_error(error_message):
    error_message_lower = error_message.lower()
    
    # Indentation errors
    if any(kw in error_message_lower for kw in ["indentation", "expected an indented block", "unindent"]):
        return ("CRITICAL: Indentation error detected.\n"
                "HINT: Check spaces vs tabs. Ensure the block you are adding matches the parent scope's indentation level.\n"
                "STRATEGY: Read the surrounding code block first to verify exact whitespace count.")
    
    # Replacement errors (no match)
    if "match" in error_message_lower and any(kw in error_message_lower for kw in ["no", "zero", "found", "fail"]):
        return ("CRITICAL: Exact match failed.\n"
                "HINT: The 'old_string' must be a LITERAL match, including every space and newline.\n"
                "STRATEGY: Use read_file to copy the EXACT block, then use it in replace/edit_block. Avoid hand-typing whitespace.")
    
    # Multiple matches
    if "multiple" in error_message_lower and "match" in error_message_lower:
        return ("CRITICAL: Ambiguous match.\n"
                "HINT: The 'old_string' matches multiple locations in the file.\n"
                "STRATEGY: Provide more context lines (before and after the change) to make the replacement unique.")
    
    # Line number / Bounds errors
    if any(kw in error_message_lower for kw in ["bounds", "line number", "range"]):
        return ("CRITICAL: Out of bounds error.\n"
                "HINT: You are trying to edit lines that don't exist in the current version of the file.\n"
                "STRATEGY: The file might have changed since your last read. Re-read the file to get fresh line numbers.")
    
    # Syntax errors (general)
    if "syntax" in error_message_lower:
        return ("CRITICAL: Syntax error detected.\n"
                "HINT: Your proposed change breaks the language rules.\n"
                "STRATEGY: Run a syntax checker (like 'python -m py_compile' or 'tsc') before applying the edit.")
    
    # Path errors
    if "no such file" in error_message_lower or "not found" in error_message_lower:
        return ("CRITICAL: File path error.\n"
                "HINT: The target file path is incorrect or the file doesn't exist.\n"
                "STRATEGY: Use 'ls' or 'find' to verify the exact path relative to root.")

    return "HINT: The tool operation failed. Carefully analyze the error above and verify your assumptions before retrying."

def main():
    # If passed as args or stdin
    if len(sys.argv) > 1:
        error_msg = " ".join(sys.argv[1:])
    else:
        error_msg = sys.stdin.read()

    if not error_msg.strip():
        sys.exit(0)

    hint = analyze_error(error_msg)
    
    print("\n" + "="*40)
    print("🛡️  EDIT GUARD PROTECTION TRIGGERED")
    print("="*40)
    print(f"ERROR: {error_msg.strip()}")
    print("-" * 20)
    print(hint)
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
