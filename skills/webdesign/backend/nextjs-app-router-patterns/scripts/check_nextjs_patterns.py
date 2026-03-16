import os
import re
import sys

def check_nextjs_patterns(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []
        
    errors_or_hints = []
    
    # Check for 'use client' and 'use server'
    has_use_client = re.search(r"['\"]use client['\"]", content)
    has_use_server = re.search(r"['\"]use server['\"]", content)
    
    # Check if 'use client' is importing server-only modules (basic heuristic)
    if has_use_client:
        if 'next/headers' in content or 'next/cache' in content:
             errors_or_hints.append("Warning: 'use client' component seems to import server-only modules like next/headers or next/cache.")
    
    # Check for cache definitions
    if 'force-cache' in content:
        errors_or_hints.append("Hint: 'force-cache' is used. Verify if this data should ever be revalidated.")
    if 'no-store' in content:
        errors_or_hints.append("Hint: 'no-store' is used. This opts out of caching completely.")
    if 'revalidate:' in content or 'revalidateTag' in content or 'revalidatePath' in content:
        errors_or_hints.append("Hint: ISR or Cache Revalidation pattern detected.")
        
    return errors_or_hints

def scan_project(root_dir):
    print(f"Scanning {root_dir} for Next.js App Router patterns...\n")
    for root, _, files in os.walk(root_dir):
        if 'node_modules' in root or '.git' in root or '.next' in root:
            continue
            
        for file in files:
            if file.endswith('.ts') or file.endswith('.tsx') or file.endswith('.js') or file.endswith('.jsx'):
                path = os.path.join(root, file)
                hints = check_nextjs_patterns(path)
                if hints:
                    print(f"[{path}]")
                    for h in hints:
                        print(f"  - {h}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_nextjs_patterns.py <directory>")
    else:
        scan_project(sys.argv[1])
