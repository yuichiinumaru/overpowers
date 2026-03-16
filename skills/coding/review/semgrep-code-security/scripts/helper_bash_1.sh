#!/bin/bash

semgrep --config auto .                    # Automatically detect relevant rulesets
semgrep --config p/security-audit .        # Run curated security-audit ruleset
semgrep --config p/owasp-top-ten .         # Scan for OWASP Top 10 vulnerabilities
