# Auto-generated example usage from SKILL.md

#    import pandas as pd
#
#    # Load results
#    df = pd.read_csv('docking_library.txt', sep='\t')
#
#    # Filter by properties in tranche data
#    # Tranche format: H##P###M###-phase
#    # H = H-bond donors, P = LogP*10, M = MW
#    ```
#
# 4. **Download 3D structures** for docking using ZINC ID or download from file repositories
#
# ### Workflow 2: Finding Analogs of a Hit Compound
#
# 1. **Obtain SMILES** of the hit compound:
#    ```python
#    hit_smiles = "CC(C)Cc1ccc(cc1)C(C)C(=O)O"  # Example: Ibuprofen
#    ```
#
# 2. **Perform similarity search** with distance threshold:
#    ```bash
#    curl "https://cartblanche22.docking.org/smiles.txt:smiles=CC(C)Cc1ccc(cc1)C(C)C(=O)O&dist=5&output_fields=zinc_id,smiles,catalogs" > analogs.txt
#    ```
#
# 3. **Analyze results** to identify purchasable analogs:
#    ```python
#    import pandas as pd
#
#    analogs = pd.read_csv('analogs.txt', sep='\t')
#    print(f"Found {len(analogs)} analogs")
#    print(analogs[['zinc_id', 'smiles', 'catalogs']].head(10))
#    ```
#
# 4. **Retrieve 3D structures** for the most promising analogs
#
# ### Workflow 3: Batch Compound Retrieval
#
# 1. **Compile list of ZINC IDs** from literature, databases, or previous screens:
#    ```python
#    zinc_ids = [
#        "ZINC000000000001",
#        "ZINC000000000002",
#        "ZINC000000000003"
#    ]
#    zinc_ids_str = ",".join(zinc_ids)
#    ```
#
# 2. **Query ZINC22 API**:
#    ```bash
#    curl "https://cartblanche22.docking.org/substances.txt:zinc_id=ZINC000000000001,ZINC000000000002&output_fields=zinc_id,smiles,supplier_code,catalogs"
#    ```
#
# 3. **Process results** for downstream analysis or purchasing
#
# ### Workflow 4: Chemical Space Sampling
#
# 1. **Select subset parameters** based on screening goals:
#    - Fragment: MW < 250, good for fragment-based drug discovery
#    - Lead-like: MW 250-350, LogP ≤ 3.5
#    - Drug-like: MW 350-500, follows Lipinski's Rule of Five
#
# 2. **Generate random sample**:
#    ```bash
#    curl "https://cartblanche22.docking.org/substance/random.txt:count=5000&subset=lead-like&output_fields=zinc_id,smiles,tranche" > chemical_space_sample.txt
#    ```
#
# 3. **Analyze chemical diversity** and prepare for virtual screening
#
# ## Output Fields
#
# Customize API responses with the `output_fields` parameter:
#
# **Available fields**:
# - `zinc_id`: ZINC identifier
# - `smiles`: SMILES string representation
# - `sub_id`: Internal substance ID
# - `supplier_code`: Vendor catalog number
# - `catalogs`: List of suppliers offering the compound
# - `tranche`: Encoded molecular properties (H-count, LogP, MW, reactivity phase)
#
# **Example**:

# import subprocess
# import json
#
# def query_zinc_by_id(zinc_id, output_fields="zinc_id,smiles,catalogs"):
#     """Query ZINC22 by ZINC ID."""
#     url = f"https://cartblanche22.docking.org/[email protected]_id={zinc_id}&output_fields={output_fields}"
#     result = subprocess.run(['curl', url], capture_output=True, text=True)
#     return result.stdout
#
# def search_by_smiles(smiles, dist=0, adist=0, output_fields="zinc_id,smiles"):
#     """Search ZINC22 by SMILES with optional distance parameters."""
#     url = f"https://cartblanche22.docking.org/smiles.txt:smiles={smiles}&dist={dist}&adist={adist}&output_fields={output_fields}"
#     result = subprocess.run(['curl', url], capture_output=True, text=True)
#     return result.stdout
#
# def get_random_compounds(count=100, subset=None, output_fields="zinc_id,smiles,tranche"):
#     """Get random compounds from ZINC22."""
#     url = f"https://cartblanche22.docking.org/substance/random.txt:count={count}&output_fields={output_fields}"
#     if subset:
#         url += f"&subset={subset}"
#     result = subprocess.run(['curl', url], capture_output=True, text=True)
#     return result.stdout

# import pandas as pd
# from io import StringIO
#
# # Query ZINC and parse as DataFrame
# result = query_zinc_by_id("ZINC000000000001")
# df = pd.read_csv(StringIO(result), sep='\t')
#
# # Extract tranche properties
# def parse_tranche(tranche_str):
#     """Parse ZINC tranche code to extract properties."""
#     # Format: H##P###M###-phase
#     import re
#     match = re.match(r'H(\d+)P(\d+)M(\d+)-(\d+)', tranche_str)
#     if match:
#         return {
#             'h_donors': int(match.group(1)),
#             'logP': int(match.group(2)) / 10.0,
#             'mw': int(match.group(3)),
#             'phase': int(match.group(4))
#         }
#     return None
#
# df['tranche_props'] = df['tranche'].apply(parse_tranche)
