#!/bin/bash
# Recommend POI Helper Script

cat << 'EOF' > result.json
{
  "poi": "Eiffel Tower",
  "city": "Paris",
  "score": 98
}
EOF

echo "Mock POI generated in result.json"
cat result.json