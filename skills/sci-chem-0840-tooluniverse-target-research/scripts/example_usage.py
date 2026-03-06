# Auto-generated example usage from SKILL.md

# # Always check tool params to prevent silent failures
# tool_info = tu.tools.get_tool_info(tool_name="Reactome_map_uniprot_to_pathways")
# # Reveals: takes `id` not `uniprot_id`

# # Step 1: Get gene info with version
# gene_info = tu.tools.ensembl_lookup_gene(id=ensembl_id, species="human")
# version = gene_info.get('version', 1)
#
# # Step 2: Try versioned ID
# versioned_id = f"{ensembl_id}.{version}"  # e.g., "ENSG00000123456.12"
# result = tu.tools.GTEx_get_median_gene_expression(
#     gencode_id=versioned_id,
#     operation="median"
# )

# def resolve_target_ids(tu, query):
#     """
#     Resolve target query to ALL needed identifiers.
#     Returns dict with: query, uniprot, ensembl, ensembl_version, symbol,
#     entrez, chembl_target, hgnc
#     """
#     ids = {
#         'query': query,
#         'uniprot': None,
#         'ensembl': None,
#         'ensembl_versioned': None,  # For GTEx
#         'symbol': None,
#         'entrez': None,
#         'chembl_target': None,
#         'hgnc': None,
#         'full_name': None,
#         'synonyms': []
#     }
#
#     # [Resolution logic based on input type]
#     # ... (see current implementation)
#
#     # CRITICAL: Get versioned Ensembl ID for GTEx
#     if ids['ensembl']:
#         gene_info = tu.tools.ensembl_lookup_gene(id=ids['ensembl'], species="human")
#         if gene_info and gene_info.get('version'):
#             ids['ensembl_versioned'] = f"{ids['ensembl']}.{gene_info['version']}"
#
#         # Also get synonyms for literature collision detection
#         ids['full_name'] = gene_info.get('description', '').split(' [')[0]
#
#     # Get UniProt alternative names for synonyms
#     if ids['uniprot']:
#         alt_names = tu.tools.UniProt_get_alternative_names_by_accession(accession=ids['uniprot'])
#         if alt_names:
#             ids['synonyms'].extend(alt_names)
#
#     return ids

# def check_gpcr_target(tu, ids):
#     """
#     Check if target is a GPCR and retrieve specialized data.
#     Call after identifier resolution.
#     """
#     symbol = ids.get('symbol', '')
#
#     # Build GPCRdb entry name
#     entry_name = f"{symbol.lower()}_human"
#
#     gpcr_info = tu.tools.GPCRdb_get_protein(
#         operation="get_protein",
#         protein=entry_name
#     )
#
#     if gpcr_info.get('status') == 'success':
#         # Target is a GPCR - get specialized data
#
#         # Get structures with receptor state
#         structures = tu.tools.GPCRdb_get_structures(
#             operation="get_structures",
#             protein=entry_name
#         )
#
#         # Get known ligands (critical for binder projects)
#         ligands = tu.tools.GPCRdb_get_ligands(
#             operation="get_ligands",
#             protein=entry_name
#         )
#
#         # Get mutation data
#         mutations = tu.tools.GPCRdb_get_mutations(
#             operation="get_mutations",
#             protein=entry_name
#         )
#
#         return {
#             'is_gpcr': True,
#             'gpcr_family': gpcr_info['data'].get('family'),
#             'gpcr_class': gpcr_info['data'].get('receptor_class'),
#             'structures': structures.get('data', {}).get('structures', []),
#             'ligands': ligands.get('data', {}).get('ligands', []),
#             'mutations': mutations.get('data', {}).get('mutations', []),
#             'ballesteros_numbering': True  # GPCRdb provides this
#         }
#
#     return {'is_gpcr': False}

# def detect_collisions(tu, symbol, full_name):
#     """
#     Detect if gene symbol has naming collisions in literature.
#     Returns negative filter terms if collisions found.
#     """
#     # Search by symbol in title
#     results = tu.tools.PubMed_search_articles(
#         query=f'"{symbol}"[Title]',
#         limit=20
#     )
#
#     # Check if >20% are off-topic
#     off_topic_terms = []
#     for paper in results.get('articles', []):
#         title = paper.get('title', '').lower()
#         # Check if title mentions biology/protein/gene context
#         bio_terms = ['protein', 'gene', 'cell', 'expression', 'mutation', 'kinase', 'receptor']
#         if not any(term in title for term in bio_terms):
#             # Extract potential collision terms
#             # e.g., "JAK" might collide with "Just Another Kinase" jokes
#             # e.g., "WDR7" might collide with other WDR family members in certain contexts
#             pass
#
#     # Build negative filter
#     collision_filter = ""
#     if off_topic_terms:
#         collision_filter = " NOT " + " NOT ".join(off_topic_terms)
#
#     return collision_filter

# def path_0_open_targets(tu, ids):
#     """
#     Open Targets foundation data - fills gaps for sections 5, 6, 8, 9, 10, 11.
#     ALWAYS run this first.
#     """
#     ensembl_id = ids['ensembl']
#     if not ensembl_id:
#         return {'status': 'skipped', 'reason': 'No Ensembl ID'}
#
#     results = {}
#
#     # 1. Diseases & Phenotypes (Section 8)
#     diseases = tu.tools.OpenTargets_get_diseases_phenotypes_by_target_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['diseases'] = diseases if diseases else {'note': 'No disease associations returned'}
#
#     # 2. Tractability (Section 9)
#     tractability = tu.tools.OpenTargets_get_target_tractability_by_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['tractability'] = tractability if tractability else {'note': 'No tractability data returned'}
#
#     # 3. Safety Profile (Section 10)
#     safety = tu.tools.OpenTargets_get_target_safety_profile_by_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['safety'] = safety if safety else {'note': 'No safety liabilities identified'}
#
#     # 4. Interactions (Section 6)
#     interactions = tu.tools.OpenTargets_get_target_interactions_by_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['interactions'] = interactions if interactions else {'note': 'No interactions returned'}
#
#     # 5. GO Annotations (Section 5)
#     go_terms = tu.tools.OpenTargets_get_target_gene_ontology_by_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['go_terms'] = go_terms if go_terms else {'note': 'No GO annotations returned'}
#
#     # 6. Publications (Section 11)
#     publications = tu.tools.OpenTargets_get_publications_by_target_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['publications'] = publications if publications else {'note': 'No publications returned'}
#
#     # 7. Mouse Models (Section 8/10)
#     mouse_models = tu.tools.OpenTargets_get_biological_mouse_models_by_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['mouse_models'] = mouse_models if mouse_models else {'note': 'No mouse model data returned'}
#
#     # 8. Chemical Probes (Section 9)
#     probes = tu.tools.OpenTargets_get_chemical_probes_by_target_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['chemical_probes'] = probes if probes else {'note': 'No chemical probes available'}
#
#     # 9. Associated Drugs (Section 9)
#     drugs = tu.tools.OpenTargets_get_associated_drugs_by_target_ensemblId(
#         ensemblId=ensembl_id
#     )
#     results['drugs'] = drugs if drugs else {'note': 'No approved/trial drugs found'}
#
#     return results

# def path_structure_robust(tu, ids):
#     """
#     Robust structure search using 3-step chain.
#     """
#     structures = {'pdb': [], 'alphafold': None, 'domains': [], 'method_notes': []}
#
#     # STEP 1: UniProt PDB Cross-References (most reliable)
#     if ids['uniprot']:
#         entry = tu.tools.UniProt_get_entry_by_accession(accession=ids['uniprot'])
#         pdb_xrefs = [x for x in entry.get('uniProtKBCrossReferences', [])
#                     if x.get('database') == 'PDB']
#         for xref in pdb_xrefs:
#             pdb_id = xref.get('id')
#             # Get details for each PDB
#             pdb_info = tu.tools.get_protein_metadata_by_pdb_id(pdb_id=pdb_id)
#             if pdb_info:
#                 structures['pdb'].append(pdb_info)
#         structures['method_notes'].append(f"Step 1: {len(pdb_xrefs)} PDB cross-refs from UniProt")
#
#     # STEP 2: Sequence-based PDB Search (catches missing annotations)
#     if ids['uniprot'] and len(structures['pdb']) < 5:
#         sequence = tu.tools.UniProt_get_sequence_by_accession(accession=ids['uniprot'])
#         if sequence and len(sequence) < 1000:  # Reasonable length for search
#             similar = tu.tools.PDB_search_similar_structures(
#                 sequence=sequence[:500],  # Use first 500 AA if long
#                 identity_cutoff=0.7
#             )
#             if similar:
#                 for hit in similar[:10]:  # Top 10 similar
#                     if hit['pdb_id'] not in [s.get('pdb_id') for s in structures['pdb']]:
#                         structures['pdb'].append(hit)
#         structures['method_notes'].append(f"Step 2: Sequence search (identity ≥70%)")
#
#     # STEP 3: Domain-based Search (for multi-domain proteins)
#     if ids['uniprot']:
#         domains = tu.tools.InterPro_get_protein_domains(uniprot_accession=ids['uniprot'])
#         structures['domains'] = domains if domains else []
#
#         # For large proteins with domains, search by domain sequence windows
#         if len(structures['pdb']) < 3 and domains:
#             for domain in domains[:3]:  # Top 3 domains
#                 domain_name = domain.get('name', '')
#                 # Could search PDB by domain name
#                 domain_hits = tu.tools.PDB_search_by_keyword(query=domain_name, limit=5)
#                 if domain_hits:
#                     structures['method_notes'].append(f"Step 3: Domain '{domain_name}' search")
#
#     # AlphaFold (always check)
#     alphafold = tu.tools.alphafold_get_prediction(uniprot_accession=ids['uniprot'])
#     structures['alphafold'] = alphafold if alphafold else {'note': 'No AlphaFold prediction'}
#
#     # IMPORTANT: Document limitations
#     if not structures['pdb']:
#         structures['limitation'] = "No direct PDB hit does NOT mean no structure exists. Check: (1) structures under different UniProt entries, (2) homolog structures, (3) domain-only structures."
#
#     return structures

# def path_expression(tu, ids):
#     """
#     Expression data with GTEx versioned ID fallback.
#     """
#     results = {'gtex': None, 'hpa': None, 'failed_tools': []}
#
#     # GTEx with fallback
#     ensembl_id = ids['ensembl']
#     versioned_id = ids.get('ensembl_versioned')
#
#     # Try unversioned first
#     gtex_result = tu.tools.GTEx_get_median_gene_expression(
#         gencode_id=ensembl_id,
#         operation="median"
#     )
#
#     # Fallback to versioned if empty
#     if not gtex_result or gtex_result.get('data') == []:
#         if versioned_id:
#             gtex_result = tu.tools.GTEx_get_median_gene_expression(
#                 gencode_id=versioned_id,
#                 operation="median"
#             )
#             if gtex_result and gtex_result.get('data'):
#                 results['gtex'] = gtex_result
#                 results['gtex_note'] = f"Used versioned ID: {versioned_id}"
#
#         if not results.get('gtex'):
#             results['failed_tools'].append({
#                 'tool': 'GTEx_get_median_gene_expression',
#                 'tried': [ensembl_id, versioned_id],
#                 'fallback': 'See HPA data below'
#             })
#     else:
#         results['gtex'] = gtex_result
#
#     # HPA (always query as backup)
#     hpa_result = tu.tools.HPA_get_rna_expression_by_source(ensembl_id=ensembl_id)
#     results['hpa'] = hpa_result if hpa_result else {'note': 'No HPA RNA data'}
#
#     return results

# def get_hpa_comprehensive_expression(tu, gene_symbol):
#     """
#     Get comprehensive expression data from Human Protein Atlas.
#
#     Provides:
#     - Tissue expression (protein and RNA)
#     - Subcellular localization
#     - Cell line expression comparison
#     - Tissue specificity
#     """
#
#     # 1. Search for gene to get IDs
#     gene_info = tu.tools.HPA_search_genes_by_query(search_query=gene_symbol)
#
#     if not gene_info:
#         return {'error': f'Gene {gene_symbol} not found in HPA'}
#
#     # 2. Get tissue expression with specificity
#     tissue_search = tu.tools.HPA_generic_search(
#         search_query=gene_symbol,
#         columns="g,gs,rnat,rnatsm,scml,scal",  # Gene, synonyms, tissue specificity, subcellular
#         format="json"
#     )
#
#     # 3. Compare expression in cancer cell lines vs normal tissue
#     cell_lines = ['a549', 'mcf7', 'hela', 'hepg2', 'pc3']
#     cell_line_expression = {}
#
#     for cell_line in cell_lines:
#         try:
#             expr = tu.tools.HPA_get_comparative_expression_by_gene_and_cellline(
#                 gene_name=gene_symbol,
#                 cell_line=cell_line
#             )
#             cell_line_expression[cell_line] = expr
#         except:
#             continue
#
#     return {
#         'gene_info': gene_info,
#         'tissue_data': tissue_search,
#         'cell_line_expression': cell_line_expression,
#         'source': 'Human Protein Atlas'
#     }

# def get_disgenet_associations(tu, ids):
#     """
#     Get gene-disease associations from DisGeNET.
#     Complements Open Targets with curated association scores.
#     """
#     symbol = ids.get('symbol')
#     if not symbol:
#         return {'status': 'skipped', 'reason': 'No gene symbol'}
#
#     # Get all disease associations for gene
#     gda = tu.tools.DisGeNET_search_gene(
#         operation="search_gene",
#         gene=symbol,
#         limit=50
#     )
#
#     if gda.get('status') != 'success':
#         return {'status': 'error', 'message': 'DisGeNET query failed'}
#
#     associations = gda.get('data', {}).get('associations', [])
#
#     # Categorize by evidence strength
#     strong = []     # score >= 0.7
#     moderate = []   # score 0.4-0.7
#     weak = []       # score < 0.4
#
#     for assoc in associations:
#         score = assoc.get('score', 0)
#         disease_name = assoc.get('disease_name', '')
#         umls_cui = assoc.get('disease_id', '')
#
#         entry = {
#             'disease': disease_name,
#             'umls_cui': umls_cui,
#             'score': score,
#             'evidence_index': assoc.get('ei'),
#             'dsi': assoc.get('dsi'),  # Disease Specificity Index
#             'dpi': assoc.get('dpi')   # Disease Pleiotropy Index
#         }
#
#         if score >= 0.7:
#             strong.append(entry)
#         elif score >= 0.4:
#             moderate.append(entry)
#         else:
#             weak.append(entry)
#
#     return {
#         'total_associations': len(associations),
#         'strong_associations': strong,
#         'moderate_associations': moderate,
#         'weak_associations': weak[:10],  # Limit weak
#         'disease_pleiotropy': len(associations)  # How many diseases linked
#     }

# def get_pharos_target_info(tu, ids):
#     """
#     Get Pharos/TCRD target development level and druggability.
#
#     TDL Classification:
#     - Tclin: Approved drug targets
#     - Tchem: Targets with small molecule activities (IC50 < 30nM)
#     - Tbio: Targets with biological annotations
#     - Tdark: Understudied proteins
#     """
#     gene_symbol = ids.get('symbol')
#     uniprot = ids.get('uniprot')
#
#     # Try by gene symbol first
#     if gene_symbol:
#         result = tu.tools.Pharos_get_target(
#             gene=gene_symbol
#         )
#     elif uniprot:
#         result = tu.tools.Pharos_get_target(
#             uniprot=uniprot
#         )
#     else:
#         return {'status': 'error', 'message': 'Need gene symbol or UniProt'}
#
#     if result.get('status') == 'success' and result.get('data'):
#         target = result['data']
#         return {
#             'name': target.get('name'),
#             'symbol': target.get('sym'),
#             'tdl': target.get('tdl'),  # Tclin/Tchem/Tbio/Tdark
#             'family': target.get('fam'),  # Kinase, GPCR, etc.
#             'novelty': target.get('novelty'),
#             'description': target.get('description'),
#             'publications': target.get('publicationCount'),
#             'interpretation': interpret_tdl(target.get('tdl'))
#         }
#     return None
#
# def interpret_tdl(tdl):
#     """Interpret Target Development Level for druggability."""
#     interpretations = {
#         'Tclin': 'Approved drug target - highest confidence for druggability',
#         'Tchem': 'Small molecule active - good chemical tractability',
#         'Tbio': 'Biologically characterized - may require novel modalities',
#         'Tdark': 'Understudied - limited data, high novelty potential'
#     }
#     return interpretations.get(tdl, 'Unknown')
#
# def search_disease_targets(tu, disease_name):
#     """Find targets associated with a disease via Pharos."""
#
#     result = tu.tools.Pharos_get_disease_targets(
#         disease=disease_name,
#         top=50
#     )
#
#     if result.get('status') == 'success':
#         targets = result['data'].get('targets', [])
#         # Group by TDL for prioritization
#         by_tdl = {'Tclin': [], 'Tchem': [], 'Tbio': [], 'Tdark': []}
#         for t in targets:
#             tdl = t.get('tdl', 'Unknown')
#             if tdl in by_tdl:
#                 by_tdl[tdl].append(t)
#         return by_tdl
#     return None

# def assess_target_essentiality(tu, ids):
#     """
#     Is this target essential for cancer cell survival?
#
#     Negative effect scores = gene is essential (cells die upon KO)
#     """
#     gene_symbol = ids.get('symbol')
#
#     if not gene_symbol:
#         return {'status': 'error', 'message': 'Need gene symbol'}
#
#     deps = tu.tools.DepMap_get_gene_dependencies(
#         gene_symbol=gene_symbol
#     )
#
#     if deps.get('status') == 'success':
#         return {
#             'gene': gene_symbol,
#             'data': deps.get('data', {}),
#             'interpretation': 'Negative scores indicate gene is essential for cell survival',
#             'note': 'Score < -0.5 is strongly essential, < -1.0 is extremely essential'
#         }
#     return None
#
# def get_cancer_type_essentiality(tu, gene_symbol, cancer_type):
#     """Check if gene is essential in specific cancer type."""
#
#     # Get cell lines for cancer type
#     cell_lines = tu.tools.DepMap_get_cell_lines(
#         cancer_type=cancer_type,
#         page_size=20
#     )
#
#     return {
#         'gene': gene_symbol,
#         'cancer_type': cancer_type,
#         'cell_lines': cell_lines.get('data', {}).get('cell_lines', []),
#         'note': 'Query individual cell lines for dependency scores via DepMap portal'
#     }

# def predict_protein_domains(tu, sequence, title="Query protein"):
#     """
#     Run InterProScan for de novo domain prediction.
#
#     Use when:
#     - Protein has no InterPro annotations
#     - Novel/uncharacterized protein
#     - Custom sequence analysis
#     """
#
#     result = tu.tools.InterProScan_scan_sequence(
#         sequence=sequence,
#         title=title,
#         go_terms=True,
#         pathways=True
#     )
#
#     if result.get('status') == 'success':
#         data = result.get('data', {})
#
#         # Job may still be running
#         if data.get('job_status') == 'RUNNING':
#             return {
#                 'job_id': data.get('job_id'),
#                 'status': 'running',
#                 'note': 'Use InterProScan_get_job_results to retrieve when ready'
#             }
#
#         # Parse completed results
#         return {
#             'domains': data.get('domains', []),
#             'domain_count': data.get('domain_count', 0),
#             'go_annotations': data.get('go_annotations', []),
#             'pathways': data.get('pathways', []),
#             'sequence_length': data.get('sequence_length')
#         }
#     return None
#
# def check_interproscan_job(tu, job_id):
#     """Check status and get results for InterProScan job."""
#
#     status = tu.tools.InterProScan_get_job_status(job_id=job_id)
#
#     if status.get('data', {}).get('is_finished'):
#         results = tu.tools.InterProScan_get_job_results(job_id=job_id)
#         return results.get('data', {})
#
#     return status.get('data', {})

# def get_bindingdb_ligands(tu, uniprot_id, affinity_cutoff=10000):
#     """
#     Get ligands with measured binding affinities from BindingDB.
#
#     Critical for:
#     - Identifying chemical starting points
#     - Understanding existing chemical matter
#     - Assessing tractability with small molecules
#
#     Args:
#         uniprot_id: UniProt accession (e.g., P00533 for EGFR)
#         affinity_cutoff: Maximum affinity in nM (lower = more potent)
#     """
#
#     # Get ligands by UniProt
#     result = tu.tools.BindingDB_get_ligands_by_uniprot(
#         uniprot=uniprot_id,
#         affinity_cutoff=affinity_cutoff
#     )
#
#     if result:
#         ligands = []
#         for entry in result:
#             ligands.append({
#                 'smiles': entry.get('smile'),
#                 'affinity_type': entry.get('affinity_type'),  # Ki, IC50, Kd
#                 'affinity_nM': entry.get('affinity'),
#                 'monomer_id': entry.get('monomerid'),
#                 'pmid': entry.get('pmid')
#             })
#
#         # Sort by affinity (most potent first)
#         ligands.sort(key=lambda x: float(x['affinity_nM']) if x['affinity_nM'] else float('inf'))
#
#         return {
#             'total_ligands': len(ligands),
#             'ligands': ligands[:20],  # Top 20 most potent
#             'best_affinity': ligands[0]['affinity_nM'] if ligands else None
#         }
#
#     return {'total_ligands': 0, 'ligands': [], 'note': 'No ligands found in BindingDB'}
#
# def get_ligands_by_structure(tu, pdb_id, affinity_cutoff=10000):
#     """Get ligands for a protein by PDB structure ID."""
#
#     result = tu.tools.BindingDB_get_ligands_by_pdb(
#         pdb_ids=pdb_id,
#         affinity_cutoff=affinity_cutoff,
#         sequence_identity=100
#     )
#
#     return result
#
# def find_compound_targets(tu, smiles, similarity_cutoff=0.85):
#     """Find other targets for a compound (polypharmacology)."""
#
#     result = tu.tools.BindingDB_get_targets_by_compound(
#         smiles=smiles,
#         similarity_cutoff=similarity_cutoff
#     )
#
#     return result

# def get_pubchem_assays_for_target(tu, gene_symbol):
#     """
#     Get bioassays targeting a gene from PubChem.
#
#     Provides:
#     - HTS screening results
#     - Dose-response data (IC50/EC50)
#     - Active compound counts
#     """
#
#     # Search assays by target gene
#     assays = tu.tools.PubChem_search_assays_by_target_gene(
#         gene_symbol=gene_symbol
#     )
#
#     assay_info = []
#     if assays.get('data', {}).get('aids'):
#         for aid in assays['data']['aids'][:10]:  # Top 10 assays
#             # Get assay details
#             summary = tu.tools.PubChem_get_assay_summary(aid=aid)
#             targets = tu.tools.PubChem_get_assay_targets(aid=aid)
#
#             assay_info.append({
#                 'aid': aid,
#                 'summary': summary.get('data', {}),
#                 'targets': targets.get('data', {})
#             })
#
#     return {
#         'total_assays': len(assays.get('data', {}).get('aids', [])),
#         'assay_details': assay_info
#     }
#
# def get_active_compounds_from_assay(tu, aid):
#     """Get active compounds from a specific bioassay."""
#
#     actives = tu.tools.PubChem_get_assay_active_compounds(aid=aid)
#
#     return {
#         'aid': aid,
#         'active_cids': actives.get('data', {}).get('cids', []),
#         'count': len(actives.get('data', {}).get('cids', []))
#     }

# def path_literature_collision_aware(tu, ids):
#     """
#     Literature search with collision detection and filtering.
#     """
#     symbol = ids['symbol']
#     full_name = ids.get('full_name', '')
#     uniprot = ids['uniprot']
#     synonyms = ids.get('synonyms', [])
#
#     # Step 1: Detect collisions
#     collision_filter = detect_collisions(tu, symbol, full_name)
#
#     # Step 2: Build high-precision seed queries
#     seed_queries = [
#         f'"{symbol}"[Title] AND (protein OR gene OR expression)',  # Symbol in title
#         f'"{full_name}"[Title]' if full_name else None,  # Full name in title
#         f'"UniProt:{uniprot}"' if uniprot else None,  # UniProt accession
#     ]
#     seed_queries = [q for q in seed_queries if q]
#
#     # Add key synonyms
#     for syn in synonyms[:3]:
#         seed_queries.append(f'"{syn}"[Title]')
#
#     # Step 3: Execute seed queries and collect PMIDs
#     seed_pmids = set()
#     for query in seed_queries:
#         if collision_filter:
#             query = f"({query}){collision_filter}"
#         results = tu.tools.PubMed_search_articles(query=query, limit=30)
#         for article in results.get('articles', []):
#             seed_pmids.add(article.get('pmid'))
#
#     # Step 4: Expand via citation network (for sparse targets)
#     if len(seed_pmids) < 30:
#         expanded_pmids = set()
#         for pmid in list(seed_pmids)[:10]:  # Top 10 seeds
#             # Get related articles
#             related = tu.tools.PubMed_get_related(pmid=pmid, limit=20)
#             for r in related.get('articles', []):
#                 expanded_pmids.add(r.get('pmid'))
#
#             # Get citing articles
#             citing = tu.tools.EuropePMC_get_citations(pmid=pmid, limit=20)
#             for c in citing.get('citations', []):
#                 expanded_pmids.add(c.get('pmid'))
#
#         seed_pmids.update(expanded_pmids)
#
#     # Step 5: Classify papers by evidence tier
#     papers_by_tier = {'T1': [], 'T2': [], 'T3': [], 'T4': []}
#     # ... classification logic based on title/abstract keywords
#
#     return {
#         'total_papers': len(seed_pmids),
#         'collision_filter_applied': collision_filter if collision_filter else 'None needed',
#         'seed_queries': seed_queries,
#         'papers_by_tier': papers_by_tier
#     }

# def call_with_retry(tu, tool_name, params, max_retries=3):
#     """
#     Call tool with retry logic.
#     """
#     for attempt in range(max_retries):
#         try:
#             result = getattr(tu.tools, tool_name)(**params)
#             if result and not result.get('error'):
#                 return result
#         except Exception as e:
#             if attempt < max_retries - 1:
#                 time.sleep(2 ** attempt)  # Exponential backoff
#             else:
#                 return {'error': str(e), 'tool': tool_name, 'attempts': max_retries}
#     return None
