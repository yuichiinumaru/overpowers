import urllib.parse

class ClaimChecker:
    """Helper to manage the fact-checking workflow."""
    def __init__(self):
        self.claims = []
        self.fact_checkers = []
        self.findings = {}

    def add_claim(self, claim_text):
        self.claims.append(claim_text)

    def select_fact_checkers(self, codes):
        """Select common fact-checkers by short code."""
        common = {
            'snopes': 'snopes.com',
            'factcheck': 'factcheck.org',
            'politifact': 'politifact.com',
            'fullfact': 'fullfact.org',
            'afp': 'factcheck.afp.com',
            'healthfeedback': 'healthfeedback.org',
            'climatefeedback': 'climatefeedback.org'
        }
        for code in codes:
            if code in common:
                self.fact_checkers.append(common[code])
            else:
                self.fact_checkers.append(code)

    def get_search_queries(self):
        queries = []
        for checker in self.fact_checkers:
            for claim in self.claims:
                # Simple query construction
                query = f"site:{checker} {claim}"
                encoded_query = urllib.parse.quote(query)
                queries.append(f"https://duckduckgo.com/?q={encoded_query}")
        return queries

    def add_finding(self, claim, checker, verdict, url, evidence=""):
        if claim not in self.findings:
            self.findings[claim] = []
        self.findings[claim].append({
            'checker': checker,
            'verdict': verdict,
            'url': url,
            'evidence': evidence
        })

    def generate_report(self):
        report = ["# Fact-Check Report", ""]
        for claim, results in self.findings.items():
            report.append(f"## Claim: {claim}")
            for res in results:
                report.append(f"### {res['checker']}")
                report.append(f"**Verdict**: {res['verdict']}")
                report.append(f"**Source**: [{res['url']}]({res['url']})")
                if res['evidence']:
                    report.append(f"**Evidence**: {res['evidence']}")
                report.append("")
        return "\n".join(report)

if __name__ == "__main__":
    checker = ClaimChecker()
    checker.add_claim("Vaccines cause autism")
    checker.select_fact_checkers(['snopes', 'fullfact'])
    print("Search Queries:")
    for q in checker.get_search_queries():
        print(q)
