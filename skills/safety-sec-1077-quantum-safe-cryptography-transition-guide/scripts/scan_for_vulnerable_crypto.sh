#!/bin/bash
# Scan codebase for potentially vulnerable cryptographic algorithms
# Based on the Quantum-Safe Cryptography Transition Guide

echo "--- Scanning for vulnerable cryptographic algorithms ---"
echo "Algorithms being searched: RSA, ECC, Diffie-Hellman, ECDSA"

# List of keywords to search for
KEYWORDS=("RSA" "ECC" "Diffie-Hellman" "DiffieHellman" "ECDSA" "X25519" "ED25519")

for kw in "${KEYWORDS[@]}"; do
    echo "Searching for '$kw'..."
    grep -rnEi "$kw" . --exclude-dir={.git,node_modules,build,dist,.jj,.serena,.agents}
done

echo "--- Scan complete ---"
echo "Note: This is a simple grep-based scan. A full CBOM requires more in-depth analysis."
