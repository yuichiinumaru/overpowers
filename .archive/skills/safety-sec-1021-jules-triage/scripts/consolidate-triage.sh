#!/bin/bash
# Script to consolidate Jules triage reports into a single TRIAGE-REPORT.md

JULES_DIR=".jules"
TRIAGE_DIR="$JULES_DIR/triage"
OUTPUT_FILE="$JULES_DIR/TRIAGE-REPORT.md"

if [ ! -d "$TRIAGE_DIR" ]; then
    echo "Error: Triage directory $TRIAGE_DIR not found."
    exit 1
fi

COUNT=$(ls -1q "$TRIAGE_DIR"/*.md 2>/dev/null | wc -l)
if [ "$COUNT" -eq 0 ]; then
    echo "No triage reports found in $TRIAGE_DIR."
    exit 0
fi

echo "Consolidating $COUNT triage reports..."

cat <<EOF > "$OUTPUT_FILE"
# Jules Triage Report

*Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")*
*Branches Analyzed: $COUNT*

## Quick Summary
| Recommendation | Count | Action |
|---------------|-------|--------|
| ✅ MERGE | $(grep -c "✅ MERGE" "$TRIAGE_DIR"/*.md || echo 0) | Ready for jules_integrate |
| 🔧 ADAPT | $(grep -c "🔧 ADAPT" "$TRIAGE_DIR"/*.md || echo 0) | Extract valuable parts |
| 📝 DOCS-ONLY | $(grep -c "📝 DOCS-ONLY" "$TRIAGE_DIR"/*.md || echo 0) | Copy documentation/plans |
| ❌ DISCARD | $(grep -c "❌ DISCARD" "$TRIAGE_DIR"/*.md || echo 0) | Can delete branches |

EOF

# Function to append sections based on recommendation
append_section() {
    local keyword="$1"
    local title="$2"
    
    echo -e "\n## $title" >> "$OUTPUT_FILE"
    
    for file in "$TRIAGE_DIR"/*.md; do
        if grep -q "$keyword" "$file"; then
            branch_name=$(basename "$file" .md)
            echo -e "\n### $branch_name" >> "$OUTPUT_FILE"
            # Extract summary (assuming it's after ## Summary)
            summary=$(sed -n '/## Summary/,/^## /p' "$file" | sed '1d;$d' | tr '\n' ' ')
            echo "- **Summary:** $summary" >> "$OUTPUT_FILE"
            # Extract scores
            scores=$(sed -n '/## Scores/,/^## /p' "$file" | grep '-' | tr '\n' ' | ' | sed 's/ | $//')
            echo "- **Scores:** $scores" >> "$OUTPUT_FILE"
        fi
    done
}

append_section "✅ MERGE" "✅ Ready to Merge"
append_section "🔧 ADAPT" "🔧 Needs Adaptation"
append_section "📝 DOCS-ONLY" "📝 Documentation/Plans Only"
append_section "❌ DISCARD" "❌ Discard"

echo -e "\n## Integration Order\n\n1. " >> "$OUTPUT_FILE"

echo "✅ Consolidated report saved to $OUTPUT_FILE"
