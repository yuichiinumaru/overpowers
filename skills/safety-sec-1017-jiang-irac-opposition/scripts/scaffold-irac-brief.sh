#!/bin/bash
# Script to scaffold a trademark opposition/invalidation brief using IRAC

if [ -z "$1" ]; then
    echo "Usage: $0 <case-number> [type]"
    echo "Types: opposition (default), invalidation"
    exit 1
fi

CASE_ID=$1
TYPE=${2:-opposition}
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="brief-${CASE_ID}-${DATE}.md"

cat <<EOF > "$OUTPUT_FILE"
# Trademark ${TYPE^} Brief: ${CASE_ID}

## 1. Issue (争议焦点)
- **Target Mark**: 
- **Parties**: 
- **Goods/Services**: 
- **Core Dispute**: 

## 2. Rule (法律依据)
- **Primary Articles**: 
- **Guidelines**: 
- **Burden of Proof**: 

## 3. Application (事实与理由)
### Element 1: [Element Name]
- **Facts**: 
- **Evidence**: [Exhibit X]
- **Analysis**: 

### Element 2: [Element Name]
- **Facts**: 
- **Evidence**: [Exhibit Y]
- **Analysis**: 

## 4. Conclusion (结论与请求)
- **Requested Outcome**: 
- **Action Plan**: 

---

## SJ-6 Evidence Chain Map
| Exhibit | Proof Purpose | Date | Authenticity | Relevance |
|---------|---------------|------|--------------|-----------|
| 1       |               |      |              |           |

## Risk Assessment (A–E)
- **Level**: 
- **Kill Gates Check**: 
EOF

echo "Scaffolded IRAC brief to $OUTPUT_FILE"
