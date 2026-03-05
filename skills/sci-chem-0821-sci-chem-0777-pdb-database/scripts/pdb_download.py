import requests
import os

def download_pdb(pdb_id, format="cif", dest_dir="./data"):
    """Download PDB structure file"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    pdb_id = pdb_id.lower()
    url = f"https://files.rcsb.org/download/{pdb_id}.{format}"
    
    print(f"Downloading {pdb_id} in {format} format...")
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(dest_dir, f"{pdb_id}.{format}")
        with open(file_path, "w") as f:
            f.write(response.text)
        print(f"Saved to {file_path}")
        return file_path
    else:
        print(f"Error downloading {pdb_id}: Status code {response.status_code}")
        return None

if __name__ == "__main__":
    import sys
    pdb_id = sys.argv[1] if len(sys.argv) > 1 else "4hhb"
    download_pdb(pdb_id)
