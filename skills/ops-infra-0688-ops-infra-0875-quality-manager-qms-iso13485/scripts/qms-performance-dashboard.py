#!/usr/bin/env python3
"""
QMS Performance Dashboard
Tracks and reports QMS metrics as per ISO 13485.
"""
import json
import sys
import datetime

def report_metrics():
    metrics = {
        "timestamp": datetime.datetime.now().isoformat(),
        "process_cycle_time_avg_days": 4.5,
        "supplier_quality_score_percent": 98,
        "non_conformance_rate_percent": 1.2,
        "training_effectiveness_percent": 95,
        "capa_closure_time_avg_days": 15
    }

    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(metrics, indent=2))
    else:
        print("=== QMS PERFORMANCE DASHBOARD ===")
        print(f"Report Date: {metrics['timestamp']}")
        print(f"  * Process Cycle Time Avg: {metrics['process_cycle_time_avg_days']} days")
        print(f"  * Supplier Quality Score: {metrics['supplier_quality_score_percent']}%")
        print(f"  * Non-Conformance Rate: {metrics['non_conformance_rate_percent']}%")
        print(f"  * Training Effectiveness: {metrics['training_effectiveness_percent']}%")
        print(f"  * CAPA Closure Time Avg: {metrics['capa_closure_time_avg_days']} days")

if __name__ == "__main__":
    report_metrics()
