#!/bin/bash
set -euo pipefail

# Generate incident responder templates

echo "[*] Generating Incident Responder Templates..."

if [ ! -d "incidents" ]; then
    mkdir -p incidents
    echo "[+] Created 'incidents' directory."
fi

cat << 'TPL' > incidents/incident_report_template.md
# Incident Report: [Incident Title]
**Date**: YYYY-MM-DD
**Severity**: SEV-1/SEV-2
**Incident Commander**: [Name]
**Status**: Investigating / Mitigated / Resolved

## Timeline
*   **00:00 UTC** - Incident detected via [Alert/Customer]
*   **00:05 UTC** - Initial investigation started
*   **00:15 UTC** - Mitigation applied
*   **00:30 UTC** - System stable, monitoring

## Impact
[Describe the impact on users, revenue, data, etc.]

## Root Cause
[Technical explanation of what failed and why.]

## Action Items
- [ ] Preventative measure 1 (Owner: [Name])
- [ ] Better detection 1 (Owner: [Name])

TPL

echo "[+] Generated incident_report_template.md in 'incidents/'"

cat << 'TPL' > incidents/post_mortem_template.md
# Blameless Post-Mortem: [Incident Title]

## Summary
[Brief description of the incident.]

## Contributing Factors
1.  [Factor 1]
2.  [Factor 2]

## What Went Well
*   [e.g., Monitoring caught it quickly.]

## What Didn't Go Well
*   [e.g., Mitigation took too long.]

## Root Cause Analysis (5 Whys)
1.  Why did X happen? Because Y.
2.  Why did Y happen? Because Z.
3.  Why did Z happen? ...

TPL

echo "[+] Generated post_mortem_template.md in 'incidents/'"
echo "[*] Incident template generation complete."
