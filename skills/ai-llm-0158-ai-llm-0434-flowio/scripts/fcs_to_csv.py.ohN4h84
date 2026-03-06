#!/usr/bin/env python3
import sys
import os
import pandas as pd
try:
    from flowio import FlowData
except ImportError:
    print("Error: flowio not installed. Run 'uv pip install flowio'.")
    sys.exit(1)

def fcs_to_csv(fcs_path, csv_path=None):
    if not os.path.exists(fcs_path):
        print(f"Error: {fcs_path} not found.")
        return

    if csv_path is None:
        csv_path = os.path.splitext(fcs_path)[0] + ".csv"

    try:
        flow = FlowData(fcs_path)
        events = flow.as_array()
        
        df = pd.DataFrame(events, columns=flow.pnn_labels)
        df.to_csv(csv_path, index=False)
        
        print(f"Successfully exported {len(df)} events to {csv_path}")

    except Exception as e:
        print(f"Error converting FCS to CSV: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fcs_to_csv.py <file.fcs> [output.csv]")
        sys.exit(1)
    
    fcs_file = sys.argv[1]
    csv_file = sys.argv[2] if len(sys.argv) > 2 else None
    fcs_to_csv(fcs_file, csv_file)
