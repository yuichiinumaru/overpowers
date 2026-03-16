import os
import shutil
import csv
import argparse
from datetime import datetime

def organize_invoices(src_dir, dest_dir, dry_run=False):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    summary = []
    supported_exts = ('.pdf', '.jpg', '.png')
    
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(supported_exts)]
    print(f"Found {len(files)} files to process.")
    
    for filename in files:
        # Mocking information extraction logic as described in SKILL.md
        # In a real scenario, this would use OCR or PDF text extraction
        
        # Simple extraction from filename for demo purposes
        parts = filename.replace('_', ' ').replace('-', ' ').split()
        vendor = parts[0].capitalize() if parts else "Unknown"
        date_str = datetime.now().strftime("%Y-%m-%d") # Fallback date
        description = "Invoice"
        amount = "0.00"
        category = "General"
        
        new_filename = f"{date_str} {vendor} - {description}.{filename.split('.')[-1]}"
        year = date_str.split('-')[0]
        
        target_path = os.path.join(dest_dir, year, category, vendor)
        if not os.path.exists(target_path) and not dry_run:
            os.makedirs(target_path)
            
        full_target_path = os.path.join(target_path, new_filename)
        
        if not dry_run:
            shutil.copy(os.path.join(src_dir, filename), full_target_path)
            print(f"Copied {filename} -> {full_target_path}")
        else:
            print(f"[DRY RUN] Would copy {filename} -> {full_target_path}")
            
        summary.append({
            'Date': date_str,
            'Vendor': vendor,
            'Description': description,
            'Amount': amount,
            'Category': category,
            'File Path': full_target_path
        })
        
    # Write CSV summary
    csv_path = os.path.join(dest_dir, 'invoice-summary.csv')
    if not dry_run:
        with open(csv_path, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Vendor', 'Description', 'Amount', 'Category', 'File Path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in summary:
                writer.writerow(row)
        print(f"✅ Generated summary report at {csv_path}")

def main():
    parser = argparse.ArgumentParser(description='Organize invoices and receipts')
    parser.add_argument('src', help='Source directory with messy invoices')
    parser.add_argument('dest', help='Destination directory for organized filing')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without moving files')
    
    args = parser.parse_args()
    organize_invoices(args.src, args.dest, args.dry_run)

if __name__ == "__main__":
    main()
