#!/usr/bin/env python3
"""
Generate focused agent task prompts for parallel dispatch.
"""
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: task_generator.py <domain> <context>")
        print('Example: task_generator.py "agent-tool-abort.test.ts" "3 failing tests with timing issues"')
        sys.exit(1)

    domain = sys.argv[1]
    context = sys.argv[2]

    prompt = f"""Fix the failures in {domain}:

{context}

Your task:
1. Read the relevant files and understand the expected behavior.
2. Identify the root cause of the failures.
3. Apply surgical fixes strictly within the domain.
4. Verify your changes.

Constraints:
- Do NOT change code outside of this domain.
- Maintain existing coding style and conventions.

Return: A concise summary of the root cause and the applied fixes.
"""
    
    print("-" * 20 + " GENERATED PROMPT " + "-" * 20)
    print(prompt)
    print("-" * 58)

if __name__ == "__main__":
    main()
