#!/bin/bash
set -e

echo "[*] LLM Application Security Audit Checklist"
echo "--------------------------------------------"
echo "This script provides a quick interactive checklist based on OWASP Top 10 for LLMs 2025."

read -p "1. LLM01: Are input validation and output filtering in place? (y/n) " llm01
read -p "2. LLM02: Is sensitive data sanitized before sending to the model? (y/n) " llm02
read -p "3. LLM03: Have you verified the source and integrity of your models/dependencies? (y/n) " llm03
read -p "4. LLM04: Is training/fine-tuning data validated against poisoning? (y/n) " llm04
read -p "5. LLM05: Are outputs treated as untrusted and encoded properly? (y/n) " llm05
read -p "6. LLM06: Is the principle of least privilege applied to the LLM agent? (y/n) " llm06
read -p "7. LLM07: Are system prompts protected from leakage? (y/n) " llm07
read -p "8. LLM08: Are RAG embeddings and databases secured? (y/n) " llm08
read -p "9. LLM09: Do you have mechanisms to detect/prevent hallucinations? (y/n) " llm09
read -p "10. LLM10: Are rate limits and resource consumption controls active? (y/n) " llm10

echo -e "\n--- Summary ---"
score=0
for i in $llm01 $llm02 $llm03 $llm04 $llm05 $llm06 $llm07 $llm08 $llm09 $llm10; do
    if [ "$i" == "y" ]; then
        score=$((score + 1))
    fi
done

echo "Security Score: $score/10"
if [ $score -lt 10 ]; then
    echo "Warning: Your application is missing some critical security controls."
    echo "Refer to the LLM Security Guidelines (OWASP Top 10 for LLM 2025)."
else
    echo "Great job! All basic checks passed."
fi
