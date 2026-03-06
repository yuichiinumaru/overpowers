#!/usr/bin/env python3
import json
import os
import subprocess
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Retrieve and apply Jules sessions locally.")
    parser.add_argument("--limit", type=int, default=None, help="Limit how many to pull")
    args = parser.parse_args()

    tracking_file = "/tmp/jules-dispatch/jules_active_sessions.json"
    if not os.path.exists(tracking_file):
        print(f"❌ No active sessions found at {tracking_file}")
        sys.exit(1)

    with open(tracking_file, "r") as f:
        try:
            sessions = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Corrupted JSON in {tracking_file}: {e}")
            sys.exit(1)

    print(f"🔍 Found {len(sessions)} sessions in tracking file.")

    processed = 0
    for session_id, data in sessions.items():
        if args.limit and processed >= args.limit:
            break
            
        if data.get("pulled", False):
            continue

        task_name = data.get("task", "unknown_task")
        task_base = os.path.basename(task_name).replace(".md", "")
        print(f"\n==============================================")
        print(f"⬇️ Pulling session: {session_id} [{task_base}]")

        patch_file = f"/tmp/jules-dispatch/patch_{session_id}.diff"
        try:
            # Note: npx jules remote pull might succeed with "api error: status 404" if not found or not done.
            # Using capture_output so we can inspect it safely.
            result = subprocess.run(
                ["npx", "jules", "remote", "pull", "--session", session_id],
                capture_output=True,
                text=True
            )
            
            out = result.stdout
            err = result.stderr
            combined = out + err

            if "api error" in combined or "error:" in combined.lower() or "not found" in combined.lower():
                print(f"⚠️ Session may not be ready or failed: {combined.strip()[:150]}")
                continue

            if not out.strip().startswith("diff --git"):
                print(f"⚠️ Unexpected patch format received: {out.strip()[:100]}")
                continue

            with open(patch_file, "w") as pf:
                pf.write(out)
                
            print(f"✅ Patch downloaded: {patch_file}")

            # Now we use Jujutsu to safely create a branch off development
            cmd_new = ["jj", "new", "development", "-m", f"feat(jules): auto-pull {task_base}"]
            subprocess.run(cmd_new, check=True, capture_output=True)
            
            # Apply the patch
            cmd_apply = ["git", "apply", patch_file]
            apply_result = subprocess.run(cmd_apply, capture_output=True, text=True)
            
            if apply_result.returncode != 0:
                print(f"❌ Failed to apply patch cleanly. Rolling back branch.")
                print(apply_result.stderr)
                subprocess.run(["jj", "abandon"], check=True, capture_output=True)
            else:
                print(f"✅ Patch applied cleanly into new JJ branch!")
                # Create a bookmark so it shows up named
                subprocess.run(["jj", "bookmark", "create", f"jules/{session_id}", "-r", "@"], check=True, capture_output=True)
                
                # Mark as pulled
                data["pulled"] = True
                processed += 1

        except subprocess.CalledProcessError as e:
            print(f"❌ Error during JJ commands: {e.stderr}")
            continue
            
    # Update state file
    with open(tracking_file, "w") as f:
        json.dump(sessions, f, indent=2)
        
    print(f"\n🎉 Finished processing. Successfully pulled and applied {processed} sessions.")

if __name__ == "__main__":
    main()
