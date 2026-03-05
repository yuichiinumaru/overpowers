import os
import shutil

STAGING_DIR = "/home/sephiroth/Work/overpowers/.archive/staging_skills/"
ACTIVE_SKILLS_DIR = "/home/sephiroth/Work/overpowers/skills/"

def transpose_skills():
    moved_count = 0
    skipped_count = 0
    
    print(f"Starting mass transposition to {ACTIVE_SKILLS_DIR}...")
    
    for item in os.listdir(STAGING_DIR):
        if item.endswith('.py'):
            continue # skip the helper scripts we wrote
            
        src_path = os.path.join(STAGING_DIR, item)
        dst_path = os.path.join(ACTIVE_SKILLS_DIR, item)
        
        if os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                try:
                    shutil.move(src_path, dst_path)
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {item}: {e}")
            else:
                # Skill folder already exists, skip to be safe
                skipped_count += 1
                
    print(f"\\nTransposition complete!\\nMoved: {moved_count} skills.\\nSkipped (already existed): {skipped_count} skills.")

if __name__ == "__main__":
    transpose_skills()
