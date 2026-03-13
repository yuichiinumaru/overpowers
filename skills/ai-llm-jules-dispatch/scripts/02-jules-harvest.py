#!/usr/bin/env python3
import json
import os
import subprocess
import time
import sys

def main():
    sessions_file = ".agents/jules_sessions.json"
    harvest_dir = ".archive/harvest/jules"
    os.makedirs(harvest_dir, exist_ok=True)

    if not os.path.exists(sessions_file):
        print(f"❌ No sessions file found at {sessions_file}")
        sys.exit(1)

    with open(sessions_file, "r") as f:
        try:
            sessions = json.load(f)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in sessions file.")
            sys.exit(1)

    if not sessions:
        print("⚠️ No active sessions to harvest.")
        sys.exit(0)

    print(f"🌾 Harvesting {len(sessions)} Jules sessions...")

    report_lines = [
        "| Task | Session ID | Diff Size (KB) | Files Touched |",
        "|---|---|---|---|"
    ]

    for session_id, data in sessions.items():
        task_name = os.path.basename(data.get("task", "unknown_task"))
        diff_path = os.path.join(harvest_dir, f"{session_id}.diff")
        
        print(f"📥 Pulling diff for session {session_id} ({task_name})...")
        
        try:
            # We assume `jules remote pull --session ID --diff` outputs the raw patch to stdout
            result = subprocess.run(
                ["jules", "remote", "pull", "--session", session_id, "--diff"],
                capture_output=True, text=True, check=True
            )
            diff_content = result.stdout
            
            # Save the diff to the staging folder
            with open(diff_path, "w", encoding="utf-8") as df:
                df.write(diff_content)
                
            # Analyze diff
            size_kb = len(diff_content.encode('utf-8')) / 1024.0
            
            # Count touched files (lines starting with 'diff --git')
            files_touched = sum(1 for line in diff_content.split('\n') if line.startswith('diff --git'))
            
            report_lines.append(f"| {task_name} | `{session_id}` | {size_kb:.2f} | {files_touched} |")
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Failed to pull session {session_id}: {e.stderr.strip()}")
            report_lines.append(f"| {task_name} | `{session_id}` | FAILED | N/A |")

    report_path = os.path.join(harvest_dir, "HARVEST_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Jules Harvest Report\n\n")
        f.write("\n".join(report_lines))
        f.write("\n")

    print(f"\n✅ Harvest complete. Diffs stored in {harvest_dir}")
    print(f"✅ Report generated at {report_path}")

if __name__ == "__main__":
    main()
