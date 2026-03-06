#!/usr/bin/env python3
import sys
import json
import re

def check_g2_config(file_path):
    """
    Checks G2 configuration files for known legend layout issues.
    Specifically: manually set padding which triggers default size fallback.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Look for padding settings and legend settings
        has_padding = re.search(r'paddingTop|paddingBottom|paddingLeft|paddingRight|padding', content)
        has_legend = re.search(r'legend', content)
        has_size = re.search(r'size\s*:', content)
        
        if has_padding and has_legend and not has_size:
            print(f"[WARNING] {file_path}: Manual padding detected with legend configuration, but no 'size' property found.")
            print("          This might cause the legend to fall back to default sizing (40px) instead of measuring content.")
            print("          Refer to the g2-legend-expert skill for more details.")
        else:
            print(f"[OK] {file_path}: No obvious legend layout issues detected.")
            
    except Exception as e:
        print(f"[ERROR] Could not process {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: g2_legend_checker.py <path_to_g2_config_file>")
        sys.exit(1)
        
    for arg in sys.argv[1:]:
        check_g2_config(arg)
