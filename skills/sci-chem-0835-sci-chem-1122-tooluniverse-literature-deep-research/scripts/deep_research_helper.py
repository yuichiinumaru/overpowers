import sys

def format_methods_verification(method_findings, total_oa_papers):
    """Format the Methods Verification section for a report."""
    report = "## Methods Verification\n\n**Antibiotic concentrations** (verified from full text):\n"
    for finding in method_findings:
        report += f"- {finding}\n"
    report += f"\n*Note: Full-text verification performed on {len(method_findings)}/{total_oa_papers} OA papers ({len(method_findings)/max(1, total_oa_papers)*100:.0f}% coverage)*\n"
    return report

if __name__ == "__main__":
    findings = [
        "Study A: Ciprofloxacin 5 μg/mL [PMC12345, Methods section]",
        "Study B: Meropenem 8 μg/mL [arXiv:2301.12345, Experimental Design]"
    ]
    print(format_methods_verification(findings, 15))
