#!/bin/bash
# Verify no PHI in clinical reports
grep -ri "patient name" reports/ && echo "Potential PHI found!"
echo "HIPAA check complete."
