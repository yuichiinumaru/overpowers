#!/bin/bash
# YouTube Video Analysis Report Scaffolding

VIDEO_TITLE=${1:-"video_title"}
FILENAME="video_analysis_${VIDEO_TITLE}.md"

cat <<EOF > "$FILENAME"
# Video Analysis: ${VIDEO_TITLE}

## 1. Metadata
- URL:
- Title:
- Channel:

## 2. Procedure Extraction
- Summary:
- Key Steps:
  1.
  2.
  3.

## 3. Skill Scorecard
- Frequência/Volume:
- Repetitividade:
- Regra Clara:
- Estabilidade:
- Entradas Padronizadas:
- Complexidade:
- Testabilidade:
- Reuso/Portabilidade:
- Segurança/Risco:
- **TOTAL:** (>= 15 for approval)

## 4. Recommendation
- [ ] Create New Skill
- [ ] Update Existing Skill
- [ ] Discard
EOF

echo "Scaffolded video analysis report: $FILENAME"
