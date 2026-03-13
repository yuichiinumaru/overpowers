#!/usr/bin/env python3
import os
import glob

def generate_preview():
    harvest_dir = ".archive/harvest/jules"
    preview_file = os.path.join(harvest_dir, "PREVIEW_REPORT.md")
    
    if not os.path.exists(harvest_dir):
        print(f"❌ Harvest directory not found at {harvest_dir}")
        return

    diff_files = glob.glob(os.path.join(harvest_dir, "*.diff"))
    
    if not diff_files:
        print("⚠️ No diff files found to preview.")
        return

    print(f"🔍 Generating preview for {len(diff_files)} sessions...")

    with open(preview_file, "w", encoding="utf-8") as out:
        out.write("# Jules Surgical Preview Report\n\n")
        out.write("Review these diff previews to decide which session to integrate.\n\n")
        
        for diff_path in diff_files:
            session_id = os.path.basename(diff_path).replace(".diff", "")
            out.write(f"## Session ID: `{session_id}`\n")
            
            with open(diff_path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
                
            current_file = None
            file_lines = []
            
            for line in lines:
                if line.startswith("diff --git"):
                    # Dump previous file if any
                    if current_file and file_lines:
                        out.write(f"### {current_file}\n```diff\n")
                        # Show up to 10 context lines (ignoring header)
                        out.write("".join(file_lines[:15]))
                        if len(file_lines) > 15:
                            out.write("\n... (truncated)\n")
                        out.write("```\n\n")
                    
                    parts = line.split(" ")
                    if len(parts) >= 3:
                        current_file = parts[-1].strip()[2:] # remove b/
                    else:
                        current_file = "Unknown"
                    file_lines = []
                else:
                    if current_file is not None:
                        file_lines.append(line)
                        
            # Dump the last file
            if current_file and file_lines:
                out.write(f"### {current_file}\n```diff\n")
                out.write("".join(file_lines[:15]))
                if len(file_lines) > 15:
                    out.write("\n... (truncated)\n")
                out.write("```\n\n")
                
            out.write("---\n\n")
            
    print(f"✅ Preview report generated at {preview_file}")

if __name__ == "__main__":
    generate_preview()
