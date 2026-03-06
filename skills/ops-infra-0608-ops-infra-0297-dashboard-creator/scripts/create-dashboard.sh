#!/bin/bash
# Basic HTML dashboard creator template
OUTPUT_FILE="${1:-dashboard.html}"

cat << 'HTML_EOF' > "$OUTPUT_FILE"
<!DOCTYPE html>
<html>
<head>
  <title>Dashboard</title>
  <style>
    body { font-family: sans-serif; }
    .card { border: 1px solid #ccc; padding: 10px; margin: 10px; display: inline-block; }
    .value { font-size: 24px; font-weight: bold; }
  </style>
</head>
<body>
  <h1>KPI Dashboard</h1>
  <div class="card">
    <div class="title">Metric 1</div>
    <div class="value">0</div>
  </div>
</body>
</html>
HTML_EOF

echo "Dashboard template created at $OUTPUT_FILE"
