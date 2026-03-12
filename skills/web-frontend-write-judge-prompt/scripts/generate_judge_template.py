#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        failure_mode = sys.argv[1]
    else:
        failure_mode = "[Insert Specific Failure Mode]"

    template = f"""You are an evaluator assessing whether an AI assistant's response exhibits the following failure mode: {failure_mode}

## Definitions

PASS: [Define exactly what constitutes a successful response that avoids the failure mode]

FAIL: [Define exactly what constitutes a failure. Provide specific examples of what to look for]

## Examples

### Example 1: PASS
Input Context: [Insert context needed for judgment]
Response: [Insert human-labeled PASS example]
Critique: [Detailed reasoning for why this passes]
Result: Pass

### Example 2: FAIL
Input Context: [Insert context needed for judgment]
Response: [Insert human-labeled FAIL example]
Critique: [Detailed reasoning for why this fails]
Result: Fail

### Example 3: PASS/FAIL (Borderline)
Input Context: [Insert context needed for judgment]
Response: [Insert borderline example]
Critique: [Detailed reasoning explaining the nuance of why this passes or fails]
Result: [Pass or Fail]

## Instructions
Review the provided context and response.
First, write a detailed critique assessing the response against the definitions above.
Then, output a final result of either "Pass" or "Fail".

Output format:
{{
  "critique": "string — detailed assessment of the output against the criterion",
  "result": "Pass or Fail"
}}
"""

    filepath = "judge_prompt_template.txt"
    with open(filepath, "w") as f:
        f.write(template)

    print(f"Generated judge prompt template: {filepath}")

if __name__ == "__main__":
    main()
