#!/usr/bin/env python3
import sys
import os
import re

def convert_to_v2(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()

    # Simple regex for AT_DISPATCH_ALL_TYPES_AND3 conversion
    # This is a complex transformation for regex, better handled with specific patterns
    patterns = [
        (r'AT_DISPATCH_ALL_TYPES_AND3\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*"([^"]+)",\s*\[&\]\(\)\s*\{',
         r'AT_DISPATCH_V2(\4, "\5", AT_WRAP([&]() {'),
    ]

    new_content = content
    for old, new in patterns:
        new_content = re.sub(old, new, new_content)

    if new_content != content:
        # Add include if modified
        if "#include <ATen/Dispatch_v2.h>" not in new_content:
            new_content = new_content.replace("#include <ATen/Dispatch.h>", "#include <ATen/Dispatch.h>\n#include <ATen/Dispatch_v2.h>")
        
        with open(file_path, "w") as f:
            f.write(new_content)
        print(f"Partially converted {file_path} to V2 (review manual checks needed for type groups).")
    else:
        print("No matches found for conversion.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dispatch_v2_converter.py <file.cpp>")
        sys.exit(1)
    
    convert_to_v2(sys.argv[1])
