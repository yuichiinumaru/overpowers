import os
import re
import sys

def check_ts_conventions(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []
        
    errors = []
    
    # 1. Check for 'any' (excluding comments)
    # Simple regex to catch ': any' or ':any'
    if re.search(r':\s*any\b', content) and 'test' not in file_path.lower():
        errors.append("Convention violation: Found 'any' type. Use 'unknown' instead.")
        
    # 2. Check for ApplicationError
    if 'ApplicationError' in content:
        errors.append("Convention violation: Found deprecated 'ApplicationError'. Use 'UnexpectedError' from 'n8n-workflow' instead.")
        
    # 3. Check for 'as' casting (ignoring tests)
    if ' as ' in content and 'test' not in file_path.lower():
        # This is a bit broad, but captures the preference for 'satisfies'
        if ' satisfies ' not in content:
             errors.append("Convention hint: Consider using 'satisfies' over 'as' where possible.")
        
    return errors

def check_vue_conventions(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []
        
    errors = []
    
    # 1. Check for Composition API
    if '<script' in content and 'setup' not in content:
        errors.append("Convention violation: Use Vue 3 Composition API (<script setup lang=\"ts\">).")
        
    # 2. Check for hardcoded px in style
    if re.search(r'[:\s]\d+px', content):
        errors.append("Convention violation: Potential hardcoded px found in styles. Verify if CSS variables should be used.")
        
    # 3. i18n check
    if '{{' in content and '$t(' not in content and re.search(r'>[A-Za-z\s]+<', content):
        errors.append("Convention hint: Ensure all UI text uses i18n ($t('key')).")
        
    return errors

def scan_project(root_dir):
    print(f"Scanning {root_dir} for n8n convention violations...\n")
    for root, _, files in os.walk(root_dir):
        # Skip node_modules and .git
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            path = os.path.join(root, file)
            if file.endswith('.ts') or file.endswith('.tsx'):
                errs = check_ts_conventions(path)
                for e in errs:
                    print(f"[TS] [{path}] {e}")
            elif file.endswith('.vue'):
                errs = check_vue_conventions(path)
                for e in errs:
                    print(f"[VUE][{path}] {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_n8n_conventions.py <directory>")
    else:
        scan_project(sys.argv[1])
