import os
import argparse
from datetime import datetime

TEMPLATE = """-- Migration: {name}
-- Created at: {timestamp}

BEGIN;

-- 1. Add new columns/tables
-- ALTER TABLE table_name ADD COLUMN ...;

-- 2. Data backfill (if needed)
-- UPDATE table_name SET ... WHERE ...;

-- 3. Create indexes (consider CONCURRENTLY outside transaction if needed)
-- CREATE INDEX idx_... ON table_name (...);

COMMIT;
"""

def create_migration(name):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{name}.sql"
    
    if os.path.exists(filename):
        print(f"Error: {filename} already exists.")
        return

    content = TEMPLATE.format(name=name, timestamp=datetime.now().isoformat())
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created migration template: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new SQL migration template.")
    parser.add_argument("name", help="Name of the migration")
    args = parser.parse_args()

    create_migration(args.name)
