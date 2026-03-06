#!/bin/bash
# security_scan.sh - Basic security scanner wrapper

TARGET=${1:-.}

echo "Starting basic security scan on $TARGET..."

echo "[*] Checking for potential secrets..."
# Very basic grep for common secret patterns
grep -riE "(password|secret|api[_-]?key|token|credential)[\s]*[=:][\s]*['\"][^'\"]+['\"]" "$TARGET" 2>/dev/null | grep -v "test" || echo "No obvious secrets found in codebase."

echo "[*] Checking for common vulnerable functions in Python..."
find "$TARGET" -name "*.py" -exec grep -Hn "eval(" {} \; || echo "No eval() found in Python files."
find "$TARGET" -name "*.py" -exec grep -Hn "exec(" {} \; || echo "No exec() found in Python files."

echo "[*] Checking for hardcoded IPs..."
grep -riEo "([0-9]{1,3}\.){3}[0-9]{1,3}" "$TARGET" | grep -v "127.0.0.1" | grep -v "0.0.0.0" | grep -v "test" || echo "No obvious external IPs found."

echo "Scan complete. For thorough scanning, use SAST tools like Bandit, Semgrep, or SonarQube."
