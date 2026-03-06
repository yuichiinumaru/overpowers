# Auto-generated example usage from SKILL.md

# from tooluniverse import ToolUniverse
# tu = ToolUniverse()
# tu.load_tools()
#
# # Strategy depends on input type
# if user_provided_pdb_id:
#     # Direct structure retrieval
#     pdb_id = user_provided_pdb_id.upper()
#
# elif user_provided_uniprot:
#     # Get UniProt info, then search structures
#     uniprot_id = user_provided_uniprot
#     # Can also get AlphaFold structure
#     af_structure = tu.tools.alphafold_get_structure_by_uniprot(
#         uniprot_id=uniprot_id
#     )
#
# elif user_provided_protein_name:
#     # Search by name
#     result = tu.tools.search_structures_by_protein_name(
#         protein_name=protein_name
#     )

# # Search by protein name
# result = tu.tools.search_structures_by_protein_name(
#     protein_name=protein_name
# )
#
# # Filter results by quality
# high_res = [
#     entry for entry in result["data"]
#     if entry.get("resolution") and entry["resolution"] < 2.5
# ]

# pdb_id = "4INS"
#
# # Basic metadata
# metadata = tu.tools.get_protein_metadata_by_pdb_id(pdb_id=pdb_id)
#
# # Experimental details
# exp_details = tu.tools.get_protein_experimental_details_by_pdb_id(
#     pdb_id=pdb_id
# )
#
# # Resolution (if X-ray)
# resolution = tu.tools.get_protein_resolution_by_pdb_id(pdb_id=pdb_id)
#
# # Bound ligands
# ligands = tu.tools.get_protein_ligands_by_pdb_id(pdb_id=pdb_id)
#
# # Similar structures
# similar = tu.tools.get_similar_structures_by_pdb_id(
#     pdb_id=pdb_id,
#     cutoff=2.0
# )

# # Entry summary
# summary = tu.tools.pdbe_get_entry_summary(pdb_id=pdb_id)
#
# # Molecular entities
# molecules = tu.tools.pdbe_get_molecules(pdb_id=pdb_id)
#
# # Binding sites
# binding_sites = tu.tools.pdbe_get_binding_sites(pdb_id=pdb_id)

# # When no experimental structure exists, or for comparison
# if uniprot_id:
#     af_structure = tu.tools.alphafold_get_structure_by_uniprot(
#         uniprot_id=uniprot_id
#     )
