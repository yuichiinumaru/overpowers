import argparse
from tdc.single_pred import ADME, Tox, HTS, QM
from tdc.multi_pred import DTI, DDI, PPI
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Load and split PyTDC datasets.')
    parser.add_argument('--task', required=True, choices=['ADME', 'Tox', 'HTS', 'QM', 'DTI', 'DDI', 'PPI'], help='Task category')
    parser.add_argument('--name', required=True, help='Dataset name')
    parser.add_argument('--split', default='scaffold', help='Split method')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--output-dir', default='data/', help='Directory to save split data')

    args = parser.parse_args()

    # Dynamic loading based on task
    task_map = {
        'ADME': ADME, 'Tox': Tox, 'HTS': HTS, 'QM': QM,
        'DTI': DTI, 'DDI': DDI, 'PPI': PPI
    }
    
    TaskClass = task_map[args.task]
    print(f"Loading dataset {args.name} for task {args.task}...")
    data = TaskClass(name=args.name)
    
    print(f"Splitting data using {args.split} method (seed={args.seed})...")
    split = data.get_split(method=args.split, seed=args.seed)
    
    import os
    os.makedirs(args.output_dir, exist_ok=True)
    
    for key, df in split.items():
        out_path = os.path.join(args.output_dir, f"{args.name}_{key}.csv")
        df.to_csv(out_path, index=False)
        print(f"Saved {key} split to {out_path} ({len(df)} rows)")

if __name__ == "__main__":
    main()
