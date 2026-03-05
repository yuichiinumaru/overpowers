import subprocess
import sys
import argparse

def backup_db(db_path, backup_path):
    """
    Export vectors from AgentDB to JSON.
    """
    cmd = ["npx", "agentdb@latest", "export", db_path, backup_path]
    
    print(f"Backing up database: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        print(f"Database backed up to {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error backing up database: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup AgentDB vector database")
    parser.add_argument("db_path", help="Path to database file")
    parser.add_argument("backup_path", help="Path to output JSON file")
    
    args = parser.parse_args()
    backup_db(args.db_path, args.backup_path)
