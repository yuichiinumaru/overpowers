#!/bin/bash
# Scan for potential entry points and assets for threat modeling
echo "--- Potential API/Web Entry Points ---"
grep -rEi "route|endpoint|app\.(get|post|put|delete)|@app\.|/api/" . --exclude-dir={node_modules,.git,.jj,venv} | head -n 20

echo -e "\n--- Potential Upload/Parser Surfaces ---"
grep -rEi "upload|parse|file|multipart|decoder|json\.load|xml" . --exclude-dir={node_modules,.git,.jj,venv} | head -n 20

echo -e "\n--- Potential Sensitive Assets (Secrets/Config) ---"
find . -maxdepth 2 -name "*.env*" -o -name "config*" -o -name "credentials*" -o -name "*.pem" -o -name "*.key" | grep -v "node_modules"

echo -e "\n--- Authentication/Authorization Logic ---"
grep -rEi "auth|login|signin|authorize|permission|jwt|token|cookie|session" . --exclude-dir={node_modules,.git,.jj,venv} | head -n 20
