#!/usr/bin/env python3

import sys
import json

def analyze_metrics(metrics: dict):
    bottlenecks = []
    
    # Simple threshold analysis
    if metrics.get("cpu_percent", 0) > 80:
        bottlenecks.append({"type": "CPU", "severity": "HIGH", "description": "CPU usage is above 80%"})
    
    if metrics.get("memory_percent", 0) > 85:
        bottlenecks.append({"type": "Memory", "severity": "HIGH", "description": "Memory usage is above 85%"})
        
    if metrics.get("io_wait", 0) > 10:
        bottlenecks.append({"type": "IO", "severity": "MEDIUM", "description": "High IO wait detected"})

    return bottlenecks

def generate_recommendations(bottlenecks: list):
    recommendations = []
    for b in bottlenecks:
        if b["type"] == "CPU":
            recommendations.append("- Scale compute resources or optimize CPU-intensive code.")
        elif b["type"] == "Memory":
            recommendations.append("- Check for memory leaks or increase available memory.")
        elif b["type"] == "IO":
            recommendations.append("- Optimize disk access or consider faster storage.")
    return recommendations

if __name__ == "__main__":
    # Example input
    sample_metrics = {
        "cpu_percent": 85,
        "memory_percent": 70,
        "io_wait": 5
    }
    
    print("# Performance Bottleneck Analysis")
    results = analyze_metrics(sample_metrics)
    
    if not results:
        print("No bottlenecks identified.")
    else:
        for r in results:
            print(f"- **[{r['severity']}] {r['type']}**: {r['description']}")
        
        print("\n## Recommendations")
        for rec in generate_recommendations(results):
            print(rec)
