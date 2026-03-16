import datamol as dm
import medchem as mc
import pandas as pd
import argparse
import sys

def filter_compounds(input_file, rules=None, alerts=None, output_file=None):
    """Batch filter compounds using medchem rules and alerts"""
    print(f"Loading compounds from {input_file}...")
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
        # Assume 'smiles' column exists
        smiles_col = 'smiles' if 'smiles' in df.columns else df.columns[0]
        mols = [dm.to_mol(smi) for smi in df[smiles_col]]
    else:
        # Basic SMILES list file
        with open(input_file, 'r') as f:
            mols = [dm.to_mol(line.strip()) for line in f if line.strip()]
            df = pd.DataFrame({'smiles': [dm.to_smiles(m) for m in mols]})

    results_df = df.copy()

    if rules:
        rule_list = rules.split(',')
        print(f"Applying rules: {', '.join(rule_list)}...")
        rfilter = mc.rules.RuleFilters(rule_list=rule_list)
        rule_results = rfilter(mols=mols, n_jobs=-1)
        results_df['passes_rules'] = rule_results['pass']

    if alerts:
        print(f"Applying structural alerts: {alerts}...")
        if alerts == 'common':
            afilter = mc.structural.CommonAlertsFilters()
        elif alerts == 'nibr':
            afilter = mc.structural.NIBRFilters()
        elif alerts == 'lilly':
            afilter = mc.structural.LillyDemeritsFilters()
        else:
            print(f"Unknown alert type: {alerts}. Skipping.")
            afilter = None
            
        if afilter:
            alert_results = afilter(mols=mols, n_jobs=-1)
            # Lilly returns pass/fail based on demerits
            if alerts == 'lilly':
                results_df['passes_alerts'] = alert_results['pass']
            else:
                results_df['has_alerts'] = alert_results['has_alerts']
                results_df['passes_alerts'] = ~alert_results['has_alerts']

    if output_file:
        results_df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    
    return results_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch filter molecules using medchem")
    parser.add_argument("input", help="Input CSV or SMILES file")
    parser.add_argument("--rules", help="Comma-separated list of rules (e.g. rule_of_five,rule_of_veber)")
    parser.add_argument("--alerts", choices=['common', 'nibr', 'lilly'], help="Type of structural alerts to check")
    parser.add_argument("--output", help="Output CSV file")
    
    args = parser.parse_args()
    
    try:
        filter_compounds(args.input, args.rules, args.alerts, args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
