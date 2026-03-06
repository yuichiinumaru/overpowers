# Auto-generated example usage from SKILL.md

# from datetime import datetime
#
# def create_report_file(disease_name):
#     """Create initial report file with template"""
#     filename = f"{disease_name.lower().replace(' ', '_')}_research_report.md"
#
#     template = f"""# Disease Research Report: {disease_name}
#
# **Report Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
# **Disease Identifiers**: Pending research...
#
# ---
#
# ## Executive Summary
#
# *Research in progress...*
#
# ---
#
# ## 1. Disease Identity & Classification
# *Researching...*
#
# ## 2. Clinical Presentation
# *Pending...*
#
# [... rest of template ...]
# """
#
#     with open(filename, 'w') as f:
#         f.write(template)
#
#     return filename

# def research_with_citations(tu, disease_name, report_file):
#     """Research and update report with full citations"""
#
#     references = []  # Track all sources
#
#     # === DIMENSION 1: Identity ===
#
#     # Get EFO ID
#     efo_result = tu.tools.OSL_get_efo_id_by_disease_name(disease=disease_name)
#     efo_id = efo_result.get('efo_id')
#     references.append({
#         'tool': 'OSL_get_efo_id_by_disease_name',
#         'params': {'disease': disease_name},
#         'section': 'Identity'
#     })
#
#     # Get ICD codes
#     icd_result = tu.tools.icd_search_codes(query=disease_name, version="ICD10CM")
#     references.append({
#         'tool': 'icd_search_codes',
#         'params': {'query': disease_name, 'version': 'ICD10CM'},
#         'section': 'Identity'
#     })
#
#     # Get UMLS
#     umls_result = tu.tools.umls_search_concepts(query=disease_name)
#     references.append({
#         'tool': 'umls_search_concepts',
#         'params': {'query': disease_name},
#         'section': 'Identity'
#     })
#
#     # Get synonyms from EFO
#     if efo_id:
#         efo_term = tu.tools.ols_get_efo_term(obo_id=efo_id.replace('_', ':'))
#         references.append({
#             'tool': 'ols_get_efo_term',
#             'params': {'obo_id': efo_id},
#             'section': 'Identity'
#         })
#
#         # Get subtypes
#         children = tu.tools.ols_get_efo_term_children(obo_id=efo_id.replace('_', ':'), size=20)
#         references.append({
#             'tool': 'ols_get_efo_term_children',
#             'params': {'obo_id': efo_id, 'size': 20},
#             'section': 'Identity'
#         })
#
#     # UPDATE REPORT FILE with Identity section
#     update_report_section(report_file, 'Identity', {
#         'efo_id': efo_id,
#         'icd_codes': icd_result,
#         'umls': umls_result,
#         'synonyms': efo_term.get('synonyms', []) if efo_term else [],
#         'subtypes': children
#     }, references[-5:])  # Last 5 references for this section
#
#     # === DIMENSION 2: Clinical ===
#     # ... continue for all dimensions

# def update_report_section(filename, section_name, data, sources):
#     """Update a specific section in the report file"""
#
#     # Read current file
#     with open(filename, 'r') as f:
#         content = f.read()
#
#     # Format section content with citations
#     if section_name == 'Identity':
#         section_content = format_identity_section(data, sources)
#     elif section_name == 'Clinical':
#         section_content = format_clinical_section(data, sources)
#     # ... etc
#
#     # Replace placeholder with actual content
#     placeholder = f"## {section_number}. {section_name}\n*Researching...*"
#     content = content.replace(placeholder, section_content)
#
#     # Write back
#     with open(filename, 'w') as f:
#         f.write(content)
#
#
# def format_identity_section(data, sources):
#     """Format Identity section with proper citations"""
#
#     source_list = ', '.join([s['tool'] for s in sources])
#
#     return f"""## 1. Disease Identity & Classification
#
# ### Ontology Identifiers
# | System | ID | Source |
# |--------|-----|--------|
# | EFO | {data['efo_id']} | OSL_get_efo_id_by_disease_name |
# | ICD-10 | {data['icd_codes']} | icd_search_codes |
# | UMLS CUI | {data['umls']} | umls_search_concepts |
#
# ### Synonyms & Alternative Names
# {format_list_with_source(data['synonyms'], 'ols_get_efo_term')}
#
# ### Disease Subtypes
# {format_list_with_source(data['subtypes'], 'ols_get_efo_term_children')}
#
# **Sources**: {source_list}
# """

# # Required tools - use all
# tu.tools.OSL_get_efo_id_by_disease_name(disease=disease_name)
# tu.tools.OpenTargets_get_disease_id_description_by_name(diseaseName=disease_name)
# tu.tools.ols_search_efo_terms(query=disease_name)
# tu.tools.ols_get_efo_term(obo_id=efo_id)
# tu.tools.ols_get_efo_term_children(obo_id=efo_id, size=30)
# tu.tools.umls_search_concepts(query=disease_name)
# tu.tools.umls_get_concept_details(cui=cui)
# tu.tools.icd_search_codes(query=disease_name, version="ICD10CM")
# tu.tools.snomed_search_concepts(query=disease_name)

# tu.tools.OpenTargets_get_associated_phenotypes_by_disease_efoId(efoId=efo_id)
# tu.tools.get_HPO_ID_by_phenotype(query=symptom)  # for each key symptom
# tu.tools.get_phenotype_by_HPO_ID(id=hpo_id)  # for top phenotypes
# tu.tools.MedlinePlus_search_topics_by_keyword(term=disease_name, db="healthTopics")
# tu.tools.MedlinePlus_get_genetics_condition_by_name(condition=disease_slug)
# tu.tools.MedlinePlus_connect_lookup_by_code(cs=icd_oid, c=icd_code)

# tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(efoId=efo_id)
# tu.tools.OpenTargets_target_disease_evidence(efoId=efo_id, ensemblId=gene_id)  # for top genes
# tu.tools.clinvar_search_variants(condition=disease_name, max_results=50)
# tu.tools.clinvar_get_variant_details(variant_id=vid)  # for top variants
# tu.tools.clinvar_get_clinical_significance(variant_id=vid)
# tu.tools.gwas_search_associations(disease_trait=disease_name, size=50)
# tu.tools.gwas_get_variants_for_trait(disease_trait=disease_name, size=50)
# tu.tools.gwas_get_associations_for_trait(disease_trait=disease_name, size=50)
# tu.tools.gwas_get_studies_for_trait(disease_trait=disease_name, size=30)
# tu.tools.GWAS_search_associations_by_gene(gene_name=gene)  # for top genes
# tu.tools.gnomad_get_variant_frequency(variant=variant)  # for key variants

# tu.tools.OpenTargets_get_associated_drugs_by_disease_efoId(efoId=efo_id, size=100)
# tu.tools.OpenTargets_get_drug_chembId_by_generic_name(drugName=drug)  # for each drug
# tu.tools.OpenTargets_get_drug_mechanisms_of_action_by_chemblId(chemblId=chembl_id)
# tu.tools.search_clinical_trials(condition=disease_name, pageSize=50)
# tu.tools.get_clinical_trial_descriptions(nct_ids=nct_list)
# tu.tools.get_clinical_trial_conditions_and_interventions(nct_ids=nct_list)
# tu.tools.get_clinical_trial_eligibility_criteria(nct_ids=nct_list)
# tu.tools.get_clinical_trial_outcome_measures(nct_ids=nct_list)
# tu.tools.extract_clinical_trial_outcomes(nct_ids=nct_list)
# tu.tools.GtoPdb_list_diseases(name=disease_name)
# tu.tools.GtoPdb_get_disease(disease_id=gtopdb_id)

# tu.tools.Reactome_get_diseases()
# tu.tools.Reactome_map_uniprot_to_pathways(id=uniprot_id)  # for top genes
# tu.tools.Reactome_get_pathway(stId=pathway_id)  # for key pathways
# tu.tools.Reactome_get_pathway_reactions(stId=pathway_id)
# tu.tools.humanbase_ppi_analysis(gene_list=top_genes, tissue=relevant_tissue)
# tu.tools.gtex_get_expression_by_gene(gene=gene)  # for top genes
# tu.tools.HPA_get_protein_expression(gene=gene)
# tu.tools.geo_search_datasets(query=disease_name)

# tu.tools.PubMed_search_articles(query=f'"{disease_name}"', limit=100)
# tu.tools.PubMed_search_articles(query=f'"{disease_name}" AND epidemiology', limit=50)
# tu.tools.PubMed_search_articles(query=f'"{disease_name}" AND mechanism', limit=50)
# tu.tools.PubMed_search_articles(query=f'"{disease_name}" AND treatment', limit=50)
# tu.tools.PubMed_get_article(pmid=pmid)  # for top 10 articles
# tu.tools.PubMed_get_related(pmid=key_pmid)
# tu.tools.PubMed_get_cited_by(pmid=key_pmid)
# tu.tools.OpenTargets_get_publications_by_disease_efoId(efoId=efo_id)
# tu.tools.openalex_search_works(query=disease_name, limit=50)
# tu.tools.europe_pmc_search_abstracts(query=disease_name, limit=50)
# tu.tools.semantic_scholar_search_papers(query=disease_name, limit=50)

# tu.tools.OpenTargets_get_similar_entities_by_disease_efoId(efoId=efo_id, threshold=0.3, size=30)

# tu.tools.civic_search_diseases(limit=100)
# tu.tools.civic_search_genes(query=gene, limit=20)  # for cancer genes
# tu.tools.civic_get_variants_by_gene(gene_id=civic_gene_id, limit=50)
# tu.tools.civic_get_variant(variant_id=vid)
# tu.tools.civic_get_evidence_item(evidence_id=eid)
# tu.tools.civic_search_therapies(limit=100)
# tu.tools.civic_search_molecular_profiles(limit=50)

# tu.tools.GtoPdb_get_targets(target_type=type, limit=50)  # GPCR, ion channel, etc
# tu.tools.GtoPdb_get_target(target_id=tid)  # for disease-relevant targets
# tu.tools.GtoPdb_get_target_interactions(target_id=tid)
# tu.tools.GtoPdb_search_interactions(approved_only=True)
# tu.tools.GtoPdb_list_ligands(ligand_type="Approved")

# tu.tools.OpenTargets_get_drug_warnings_by_chemblId(chemblId=cid)  # for each drug
# tu.tools.OpenTargets_get_drug_blackbox_status_by_chembl_ID(chemblId=cid)
# tu.tools.extract_clinical_trial_adverse_events(nct_ids=nct_list)
# tu.tools.FAERS_count_reactions_by_drug_event(drug=drug_name, event=event)
# tu.tools.AdverseEventPredictionQuestionGenerator(disease_name=disease, drug_name=drug)

# # After each dimension's research completes:
#
# # 1. Read current report
# with open(report_file, 'r') as f:
#     report = f.read()
#
# # 2. Replace placeholder with formatted content
# report = report.replace(
#     "## 3. Genetic & Molecular Basis\n*Pending...*",
#     formatted_genetics_section
# )
#
# # 3. Write back immediately
# with open(report_file, 'w') as f:
#     f.write(report)
#
# # 4. Continue to next dimension
