#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = "LLM Pipeline"

    template = f"""# Eval Audit Report: {project_name}

## Executive Summary
[Brief overview of the eval infrastructure state and top priority fixes.]

## Priority Findings

### 1. Error Analysis
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to error analysis, failure categories, etc.]
**Fix:** [Concrete action, e.g., Run error-analysis skill]

### 2. Evaluator Design
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to binary pass/fail, holistic vs specific judges, code vs LLM checks.]
**Fix:** [Concrete action, e.g., Use write-judge-prompt to create specific binary evaluators]

### 3. Judge Validation
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to TPR/TNR, human label alignment, dataset splits.]
**Fix:** [Concrete action, e.g., Run validate-evaluator on held-out test set]

### 4. Human Review Process
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to reviewer expertise, trace visibility, and UI.]
**Fix:** [Concrete action, e.g., Use build-review-interface to improve reviewer UI]

### 5. Labeled Data
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to dataset size and sampling strategies.]
**Fix:** [Concrete action, e.g., Sample more traces or use generate-synthetic-data]

### 6. Pipeline Hygiene
**Status:** [Problem exists / OK / Cannot determine]
[Explanation of findings related to evaluator maintenance and re-running analysis after changes.]
**Fix:** [Concrete action, e.g., Establish process to re-run error analysis after major updates]

## Next Steps
1. [Highest priority fix]
2. [Second priority fix]
3. [Third priority fix]
"""

    filepath = f"eval-audit-report.md"
    with open(filepath, "w") as f:
        f.write(template)

    print(f"Generated audit report template: {filepath}")

if __name__ == "__main__":
    main()
