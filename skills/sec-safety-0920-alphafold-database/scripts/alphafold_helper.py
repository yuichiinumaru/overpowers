import os
import requests

class AlphaFoldHelper:
    """Helper to retrieve AlphaFold structures and metadata."""
    
    @staticmethod
    def get_prediction_metadata(uniprot_id):
        api_url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
        response = requests.get(api_url)
        if response.status_code == 200 and response.json():
            return response.json()[0]
        return None

    @staticmethod
    def download_structure_and_metrics(alphafold_id, version="v4", output_dir="."):
        os.makedirs(output_dir, exist_ok=True)
        
        # Download mmCIF
        cif_url = f"https://alphafold.ebi.ac.uk/files/{alphafold_id}-model_{version}.cif"
        cif_resp = requests.get(cif_url)
        if cif_resp.status_code == 200:
            with open(os.path.join(output_dir, f"{alphafold_id}.cif"), "w") as f:
                f.write(cif_resp.text)
                
        # Download Confidence (pLDDT)
        conf_url = f"https://alphafold.ebi.ac.uk/files/{alphafold_id}-confidence_{version}.json"
        conf_resp = requests.get(conf_url)
        if conf_resp.status_code == 200:
            with open(os.path.join(output_dir, f"{alphafold_id}_confidence.json"), "w") as f:
                f.write(conf_resp.text)
                
        # Download PAE
        pae_url = f"https://alphafold.ebi.ac.uk/files/{alphafold_id}-predicted_aligned_error_{version}.json"
        pae_resp = requests.get(pae_url)
        if pae_resp.status_code == 200:
            with open(os.path.join(output_dir, f"{alphafold_id}_pae.json"), "w") as f:
                f.write(pae_resp.text)
                
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python alphafold_helper.py <uniprot_id>")
        sys.exit(1)
        
    uniprot_id = sys.argv[1]
    print(f"Fetching metadata for {uniprot_id}...")
    metadata = AlphaFoldHelper.get_prediction_metadata(uniprot_id)
    
    if metadata:
        af_id = metadata['entryId']
        print(f"Found AlphaFold ID: {af_id}")
        print(f"Downloading files for {af_id}...")
        AlphaFoldHelper.download_structure_and_metrics(af_id)
        print("Done.")
    else:
        print(f"No AlphaFold prediction found for {uniprot_id}.")
