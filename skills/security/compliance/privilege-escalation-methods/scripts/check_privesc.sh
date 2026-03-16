#!/bin/bash
# Simple script to check for common privilege escalation vectors

echo "Checking sudo permissions..."
sudo -l

echo "Checking SUID/SGID files..."
find / -perm -4000 -o -perm -2000 -type f 2>/dev/null
