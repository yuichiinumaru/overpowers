#!/bin/bash
# Print QA Checklist
cat << 'EOF'
## Pre-Delivery QA Checklist

### Data Quality Checks
- [ ] Source verification
- [ ] Freshness
- [ ] Completeness
- [ ] Null handling
- [ ] Deduplication
- [ ] Filter verification

### Calculation Checks
- [ ] Aggregation logic
- [ ] Denominator correctness
- [ ] Date alignment
- [ ] Join correctness
EOF
