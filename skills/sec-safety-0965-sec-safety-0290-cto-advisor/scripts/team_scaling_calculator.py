#!/usr/bin/env python3
import sys

print("--- Team Scaling Calculator ---")

try:
    if len(sys.argv) > 1:
        current_engineers = int(sys.argv[1])
    elif sys.stdin.isatty():
        current_engineers = int(input("Enter current number of engineers: "))
    else:
        current_engineers = 20
except (ValueError, EOFError):
    current_engineers = 20

managers_needed = current_engineers // 8
qa_needed = int(current_engineers * (1.5/10))
pm_needed = current_engineers // 10

print(f"Optimal Engineering Organization Structure for {current_engineers} engineers:")
print(f"- Managers required: {max(1, managers_needed)} (Target Ratio 1:8)")
print(f"- QA Engineers required: {max(1, qa_needed)} (Target Ratio 1.5:10)")
print(f"- Product Managers required: {max(1, pm_needed)} (Target Ratio 1:10)")
print("- Target Seniority Mix: 30% Senior / 40% Mid / 30% Junior")
