def generate_fact_check_report(claim, verdict, analysis, evidence, context, source_quality, correct_info, sources):
    """
    Generates a Markdown fact-check report following the Fact Checker skill format.
    """
    report = f"## Claim\n{claim}\n\n"
    report += f"## Verdict: {verdict}\n\n"

    report += f"## Analysis\n{analysis}\n\n"

    report += "**Evidence:**\n"
    for item in evidence:
        report += f"- {item}\n"
    report += "\n"

    report += "**Context:**\n"
    for item in context:
        report += f"- {item}\n"
    report += "\n"

    report += f"**Source Quality:**\n{source_quality}\n\n"

    report += f"## Correct Information\n{correct_info}\n\n"

    report += "## Sources\n"
    for item in sources:
        report += f"{item}\n"

    return report
