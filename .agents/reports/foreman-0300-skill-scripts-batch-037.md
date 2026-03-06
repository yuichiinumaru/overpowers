# Task 0300: Skill Scripts Batch 037 - Report

**Execution Date**: 2026-03-05
**Task**: `docs/tasks/0300-ops-skill-scripts-batch-037.md`

## Summary
Analyzed and processed 20 skills (`sci-bio-0751` to `sci-bio-0770`), adding helper scripts where specified by their respective `SKILL.md` files.

### Processed Skills & Scripts Added
1. **sci-bio-0751-sci-bio-0309-data-stats-analysis**: No scripts needed.
2. **sci-bio-0752-sci-bio-0311-data-transform**: No scripts needed.
3. **sci-bio-0753-sci-bio-0313-data-viz-plots**: No scripts needed.
4. **sci-bio-0754-sci-bio-0325-deeptools**: Scripts already exist and were kept intact.
5. **sci-bio-0755-sci-bio-0375-ena-database**: No scripts needed.
6. **sci-bio-0756-sci-bio-0377-ensembl-database**: Scripts already exist and were kept intact.
7. **sci-bio-0757-sci-bio-0381-etetoolkit**: Scripts already exist and were kept intact.
8. **sci-bio-0758-sci-bio-0466-gene-database**: Scripts already exist and were kept intact.
9. **sci-bio-0759-sci-bio-0467-generate-image**: Scripts already exist and were kept intact.
10. **sci-bio-0760-sci-bio-0473-get-available-resources**: Scripts already exist and were kept intact.
11. **sci-bio-0761-sci-bio-0509-gsea-enrichment-analysis**: No scripts needed.
12. **sci-bio-0762-sci-bio-0510-gtars**: No scripts needed.
13. **sci-bio-0763-sci-bio-0512-gwas-database**: No scripts needed.
14. **sci-bio-0764-sci-bio-0564-instrument-data-to-allotrope**:
    - `validate_asm.py`: Validate ASM output quality.
    - `convert_to_asm.py`: Main conversion script.
    - `flatten_asm.py`: ASM -> 2D CSV conversion.
    - `export_parser.py`: Generate standalone parser code.
15. **sci-bio-0765-sci-bio-0669-metabolomics-workbench-database**: No scripts needed.
16. **sci-bio-0766-sci-bio-0711-nextflow-development**:
    - `sra_geo_fetch.py`: Fetch datasets from GEO/SRA.
    - `check_environment.py`: Environment checks for Nextflow deployment.
    - `detect_data_type.py`: Detect appropriate nf-core pipeline.
    - `generate_samplesheet.py`: Generate samplesheets for nf-core pipelines.
    - `manage_genomes.py`: Manage reference genomes.
17. **sci-bio-0767-sci-bio-0735-omicverse-visualization-for-bulk-color-systems-and-single-cell-d**: No scripts needed.
18. **sci-bio-0768-sci-bio-0771-pathml**: No scripts needed.
19. **sci-bio-0769-sci-bio-0855-pydeseq2**:
    - `run_deseq2_analysis.py`: Complete command-line script for standard analyses.
20. **sci-bio-0770-sci-bio-0861-pyopenms**: No scripts needed.

All newly added scripts implement necessary functionalities defined in their respective skills' documentation, providing CLIs for automation and ease of use. Existing scripts were preserved.
