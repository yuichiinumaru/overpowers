# Auto-generated example usage from SKILL.md

# from tooluniverse import ToolUniverse
#
# tu = ToolUniverse(use_cache=True)
# tu.load_tools()
#
# # Example: Find repurposing candidates for a disease
# disease_name = "rheumatoid arthritis"
#
# # Step 1: Get disease information
# disease_info = tu.tools.OpenTargets_get_disease_id_description_by_name(
#     diseaseName=disease_name
# )
#
# # Step 2: Get associated targets
# disease_id = disease_info['data']['id']
# targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(
#     efoId=disease_id,
#     limit=10
# )
#
# # Step 3: Find drugs for each target
# for target in targets['data'][:5]:
#     drugs = tu.tools.DGIdb_get_drug_gene_interactions(
#         gene_name=target['gene_symbol']
#     )
#     # Evaluate each drug candidate...

# # 1.1 Get disease information
# disease_info = tu.tools.OpenTargets_get_disease_id_description_by_name(
#     diseaseName="[disease_name]"
# )
#
# # 1.2 Find associated targets
# targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(
#     efoId=disease_info['data']['id'],
#     limit=20
# )
#
# # 1.3 Get target details for top candidates
# target_details = []
# for target in targets['data'][:10]:
#     details = tu.tools.UniProt_get_entry_by_accession(
#         accession=target['uniprot_id']
#     )
#     target_details.append(details)

# # 2.1 Find drugs targeting disease-associated targets
# drug_candidates = []
#
# for target in targets['data'][:10]:
#     # Search DrugBank
#     drugbank_results = tu.tools.drugbank_get_drug_name_and_description_by_target_name(
#         target_name=target['gene_symbol']
#     )
#
#     # Search DGIdb
#     dgidb_results = tu.tools.DGIdb_get_drug_gene_interactions(
#         gene_name=target['gene_symbol']
#     )
#
#     # Search ChEMBL
#     chembl_results = tu.tools.ChEMBL_search_drugs(
#         query=target['gene_symbol'],
#         limit=10
#     )
#
#     drug_candidates.extend([drugbank_results, dgidb_results, chembl_results])
#
# # 2.2 Get drug details
# for drug_name in unique_drugs:
#     # Get DrugBank info
#     drug_info = tu.tools.drugbank_get_drug_basic_info_by_drug_name_or_id(
#         drug_name_or_drugbank_id=drug_name
#     )
#
#     # Get current indications
#     indications = tu.tools.drugbank_get_indications_by_drug_name_or_drugbank_id(
#         drug_name_or_drugbank_id=drug_name
#     )
#
#     # Get pharmacology
#     pharmacology = tu.tools.drugbank_get_pharmacology_by_drug_name_or_drugbank_id(
#         drug_name_or_drugbank_id=drug_name
#     )

# # 3.1 Check FDA safety data
# for drug in top_candidates:
#     # Get warnings and precautions
#     warnings = tu.tools.FDA_get_warnings_and_cautions_by_drug_name(
#         drug_name=drug['name']
#     )
#
#     # Get adverse event reports
#     adverse_events = tu.tools.FAERS_search_reports_by_drug_and_reaction(
#         drug_name=drug['name'],
#         limit=100
#     )
#
#     # Get drug interactions
#     interactions = tu.tools.drugbank_get_drug_interactions_by_drug_name_or_id(
#         drug_name_or_id=drug['name']
#     )
#
# # 3.2 Assess ADMET properties (for novel formulations)
# for drug in top_candidates:
#     if 'smiles' in drug:
#         admet = tu.tools.ADMETAI_predict_admet(
#             smiles=drug['smiles'],
#             use_cache=True
#         )

# # 4.1 Search for existing evidence
# for drug in top_candidates:
#     # PubMed search
#     query = f"{drug['name']} AND {disease_name}"
#     pubmed_results = tu.tools.PubMed_search_articles(
#         query=query,
#         max_results=50
#     )
#
#     # Europe PMC search
#     pmc_results = tu.tools.EuropePMC_search_articles(
#         query=query,
#         limit=50
#     )
#
#     # Clinical trials
#     trials = tu.tools.ClinicalTrials_search(
#         condition=disease_name,
#         intervention=drug['name']
#     )

# def score_repurposing_candidate(drug, target_score, safety_data, literature_count):
#     """Score drug repurposing candidate (0-100)."""
#     score = 0
#
#     # Target association strength (0-40 points)
#     score += min(target_score * 40, 40)
#
#     # Safety profile (0-30 points)
#     if drug['approval_status'] == 'approved':
#         score += 20
#     elif drug['approval_status'] == 'clinical':
#         score += 10
#
#     if not safety_data.get('black_box_warning'):
#         score += 10
#
#     # Literature evidence (0-20 points)
#     score += min(literature_count / 5 * 20, 20)
#
#     # Drug-likeness (0-10 points)
#     if drug.get('bioavailability') == 'high':
#         score += 10
#
#     return score
#
# # Score all candidates
# scored_candidates = []
# for drug in drug_candidates:
#     score = score_repurposing_candidate(
#         drug=drug,
#         target_score=drug['target_association_score'],
#         safety_data=drug['safety_profile'],
#         literature_count=drug['supporting_papers']
#     )
#     drug['repurposing_score'] = score
#     scored_candidates.append(drug)
#
# # Sort by score
# ranked_candidates = sorted(
#     scored_candidates,
#     key=lambda x: x['repurposing_score'],
#     reverse=True
# )

# # Find drugs with similar mechanism of action
# known_drug = "metformin"
#
# # Get mechanism
# moa = tu.tools.drugbank_get_drug_desc_pharmacology_by_moa(
#     mechanism_of_action="[moa_term]"
# )
#
# # Get similar drugs
# similar = tu.tools.ChEMBL_search_similar_molecules(
#     query=known_drug,
#     similarity_threshold=70
# )

# # Use pathway analysis
# pathways = tu.tools.drugbank_get_pathways_reactions_by_drug_or_id(
#     drug_name_or_drugbank_id="[drug_name]"
# )
#
# # Find drugs affecting same pathways
# pathway_drugs = tu.tools.drugbank_get_drug_name_and_description_by_pathway_name(
#     pathway_name=pathways['data'][0]['pathway_name']
# )

# # Search by indication/phenotype
# indication_drugs = tu.tools.drugbank_get_drug_name_and_description_by_indication(
#     indication="[related_indication]"
# )
#
# # Analyze adverse events as therapeutic effects
# # Example: minoxidil (hypertension) → hair growth
# adverse_as_therapeutic = tu.tools.FAERS_search_reports_by_drug_and_reaction(
#     drug_name="[drug_name]",
#     limit=1000
# )

# # Quick screening of 100+ drugs against disease targets
# targets = get_disease_targets(disease_id)[:10]
# all_drugs = []
#
# for target in targets:
#     drugs = tu.tools.DGIdb_get_drug_gene_interactions(
#         gene_name=target['gene_symbol']
#     )
#     all_drugs.extend(drugs)
#
# # Filter to FDA approved only
# approved_drugs = [d for d in all_drugs if d.get('approved')]

# # Comprehensive analysis of one drug candidate
# drug_name = "metformin"
#
# # Get everything
# info = tu.tools.drugbank_get_drug_basic_info_by_drug_name_or_id(drug_name_or_drugbank_id=drug_name)
# targets = tu.tools.drugbank_get_targets_by_drug_name_or_drugbank_id(drug_name_or_drugbank_id=drug_name)
# indications = tu.tools.drugbank_get_indications_by_drug_name_or_drugbank_id(drug_name_or_drugbank_id=drug_name)
# pharmacology = tu.tools.drugbank_get_pharmacology_by_drug_name_or_drugbank_id(drug_name_or_drugbank_id=drug_name)
# interactions = tu.tools.drugbank_get_drug_interactions_by_drug_name_or_id(drug_name_or_id=drug_name)
# warnings = tu.tools.FDA_get_warnings_and_cautions_by_drug_name(drug_name=drug_name)
# papers = tu.tools.PubMed_search_articles(query=f"{drug_name} AND [new_disease]", max_results=100)

# # Compare multiple candidates side-by-side
# candidates = ["drug_a", "drug_b", "drug_c"]
#
# comparison = []
# for drug in candidates:
#     data = {
#         'name': drug,
#         'info': tu.tools.drugbank_get_drug_basic_info_by_drug_name_or_id(drug_name_or_drugbank_id=drug),
#         'safety': tu.tools.FDA_get_warnings_and_cautions_by_drug_name(drug_name=drug),
#         'evidence': tu.tools.PubMed_search_articles(query=drug, max_results=10)
#     }
#     comparison.append(data)

# # Rare disease often lack approved drugs
# # Strategy: Find drugs targeting same pathways as related common diseases
#
# rare_disease = "Niemann-Pick disease"
# related_disease = "Alzheimer's disease"  # Similar pathology
#
# # Get pathways affected in related disease
# targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(
#     efoId=related_disease_id
# )
#
# # Find drugs for those targets
# # Evaluate for rare disease applicability

# # Adverse effect in one context = therapeutic in another
# # Example: Thalidomide (teratogenic) → cancer treatment
#
# drug = "drug_name"
# adverse_events = tu.tools.FAERS_search_reports_by_drug_and_reaction(
#     drug_name=drug,
#     limit=1000
# )
#
# # Analyze if adverse effects beneficial in other contexts
# # Example: weight loss AE → obesity treatment potential

# # Find drugs that complement existing therapy
# primary_drug = "existing_therapy"
# disease = "disease_name"
#
# # Get targets not covered by primary drug
# disease_targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(
#     efoId=disease_id
# )
#
# primary_targets = tu.tools.drugbank_get_targets_by_drug_name_or_drugbank_id(
#     drug_name_or_drugbank_id=primary_drug
# )
#
# # Find drugs for uncovered targets
# uncovered_targets = [t for t in disease_targets if t not in primary_targets]

# # Find drugs with multi-target activity matching disease network
#
# # Get disease network
# targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(
#     efoId=disease_id,
#     limit=50
# )
#
# # For each drug, count how many disease targets it hits
# for drug in candidate_drugs:
#     drug_targets = tu.tools.drugbank_get_targets_by_drug_name_or_drugbank_id(
#         drug_name_or_drugbank_id=drug
#     )
#
#     overlap = len(set(drug_targets) & set(disease_targets))
#     if overlap >= 3:  # Multi-target match
#         print(f"{drug}: hits {overlap} disease targets")

# # Find structurally similar approved drugs
#
# known_active = "known_active_compound"
#
# # Get structure
# cid = tu.tools.PubChem_get_CID_by_compound_name(
#     compound_name=known_active
# )
#
# # Find similar
# similar = tu.tools.PubChem_search_compounds_by_similarity(
#     cid=cid['data']['cid'],
#     threshold=85
# )
#
# # Check which are approved drugs
# for compound in similar['data']:
#     drug_info = tu.tools.PubChem_get_drug_label_info_by_CID(
#         cid=compound['cid']
#     )

# # Use ML predictions to filter candidates
#
# candidates_with_smiles = get_candidates_with_structures()
#
# # Predict ADMET for all
# admet_results = []
# for drug in candidates_with_smiles:
#     admet = tu.tools.ADMETAI_predict_admet(
#         smiles=drug['smiles'],
#         use_cache=True
#     )
#     admet_results.append({
#         'drug': drug['name'],
#         'admet': admet,
#         'pass': evaluate_admet_criteria(admet)
#     })
#
# # Keep only drugs passing ADMET criteria
# viable_candidates = [r for r in admet_results if r['pass']]
