#!/bin/bash

SKILL_PATH=$1
STRICT=$2

if [ -z "$SKILL_PATH" ]; then
    echo "Usage: $0 <skill-path> [--strict]"
    exit 1
fi

if [ ! -f "$SKILL_PATH/SKILL.md" ]; then
    echo "❌ Error: $SKILL_PATH/SKILL.md not found."
    exit 1
fi

echo "Validating skill at $SKILL_PATH..."

# 1. Name check
DIR_NAME=$(basename "$SKILL_PATH")
FRONT_NAME=$(grep "^name:" "$SKILL_PATH/SKILL.md" | head -1 | cut -d':' -f2 | xargs)

if [[ "$DIR_NAME" == *"$FRONT_NAME"* ]] || [[ "$FRONT_NAME" == *"$DIR_NAME"* ]]; then
    echo "✅ Name matches directory (loosely)."
else
    echo "⚠️ Warning: Frontmatter name ($FRONT_NAME) does not match directory name ($DIR_NAME)."
fi

# 2. Required sections
SECTIONS=("When to Use This Skill" "Not For / Boundaries" "Quick Reference" "Examples")
for section in "${SECTIONS[@]}"; do
    if grep -q "## $section" "$SKILL_PATH/SKILL.md"; then
        echo "✅ Section '$section' found."
    else
        echo "❌ Error: Missing section '## $section'."
        [ "$STRICT" == "--strict" ] && exit 1
    fi
done

# 3. Pattern count
PATTERN_COUNT=$(grep -c "^\*\*Pattern" "$SKILL_PATH/SKILL.md")
if [ "$PATTERN_COUNT" -gt 20 ]; then
    echo "⚠️ Warning: Too many patterns ($PATTERN_COUNT). Recommended <= 20."
fi

# 4. Examples count
EXAMPLE_COUNT=$(grep -c "### Example" "$SKILL_PATH/SKILL.md")
if [ "$EXAMPLE_COUNT" -lt 3 ]; then
    echo "⚠️ Warning: Only $EXAMPLE_COUNT examples found. Recommended >= 3."
fi

echo "Validation complete."
