#!/usr/bin/env python3

import json
import time
from typing import Dict, List

class PerformanceMonitor:
    def __init__(self):
        self.metrics = []

    def log_event(self, agent_id: str, task: str, duration: float, tokens: int = 0):
        self.metrics.append({
            "agent_id": agent_id,
            "task": task,
            "duration": duration,
            "tokens": tokens,
            "timestamp": time.time()
        })

    def generate_report(self):
        if not self.metrics:
            return "No metrics recorded."

        total_duration = sum(m["duration"] for m in self.metrics)
        total_tokens = sum(m["tokens"] for m in self.metrics)
        avg_duration = total_duration / len(self.metrics)

        report = f"""
# Multi-Agent Performance Report

- Total Tasks: {len(self.metrics)}
- Total Duration: {total_duration:.2f}s
- Average Duration: {avg_duration:.2f}s
- Total Tokens: {total_tokens}

## Task Breakdown
"""
        for m in self.metrics:
            report += f"- **{m['agent_id']}**: {m['task']} ({m['duration']:.2f}s, {m['tokens']} tokens)\n"

        return report

if __name__ == "__main__":
    # Example usage
    monitor = PerformanceMonitor()
    monitor.log_event("agent-1", "Research", 1.2, 450)
    monitor.log_event("agent-2", "Coding", 3.5, 1200)
    print(monitor.generate_report())
