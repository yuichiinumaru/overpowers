#!/usr/bin/env python3
import sys
import os
try:
    from flowio import FlowData
except ImportError:
    print("Error: flowio not installed. Run 'uv pip install flowio'.")
    sys.exit(1)

def inspect_fcs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    try:
        flow = FlowData(file_path)
        print("=" * 50)
        print(f"File: {os.path.basename(file_path)}")
        print(f"FCS Version: {flow.version}")
        print("-" * 50)
        print(f"Events: {flow.event_count:,}")
        print(f"Channels: {flow.channel_count}")
        
        print("\nChannel Information:")
        for i in range(flow.channel_count):
            pnn = flow.pnn_labels[i]
            pns = flow.pns_labels[i]
            ch_type = "scatter" if i in flow.scatter_indices else \
                      "fluoro" if i in flow.fluoro_indices else \
                      "time" if i == flow.time_index else "other"
            print(f"  [{i}] {pnn:10s} | {pns:30s} | {ch_type}")

        print("\nKey Metadata:")
        for key in ['$DATE', '$BTIM', '$ETIM', '$CYT', '$INST', '$SRC']:
            value = flow.text.get(key, 'N/A')
            print(f"  {key:15s}: {value}")
        print("=" * 50)

    except Exception as e:
        print(f"Error parsing FCS file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: inspect_fcs.py <file.fcs>")
        sys.exit(1)
    inspect_fcs(sys.argv[1])
