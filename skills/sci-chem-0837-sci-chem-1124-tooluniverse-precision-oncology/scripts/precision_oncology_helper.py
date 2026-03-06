import sys

def filter_tcga_mutations(mutations, min_frequency=0.01):
    """Filter TCGA mutations by frequency threshold."""
    significant_mutations = []
    for mut in mutations:
        freq = mut.get('frequency', 0.0)
        if freq >= min_frequency:
            significant_mutations.append(mut)
    return significant_mutations

if __name__ == "__main__":
    sample_muts = [{'variant': 'V600E', 'frequency': 0.05}, {'variant': 'L858R', 'frequency': 0.005}]
    res = filter_tcga_mutations(sample_muts)
    print(f"Significant mutations (>= 1%): {res}")
