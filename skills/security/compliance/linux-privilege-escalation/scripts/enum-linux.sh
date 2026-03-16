#!/bin/bash

# Simple script to perform basic Linux privilege escalation enumeration
# Note: DO NOT use maliciously. This is for authorized penetration testing only.

echo "[*] Basic Linux Privilege Escalation Enumeration"
echo "------------------------------------------------"

echo "[+] Kernel Version"
uname -a

echo "[+] Current User & Groups"
id

echo "[+] Sudo Privileges"
sudo -l 2>/dev/null

echo "[+] SUID Files"
find / -perm -u=s -type f 2>/dev/null | head -n 10
echo "... (showing top 10 SUID files)"

echo "[+] Writable Directories in PATH"
for dir in $(echo $PATH | tr ":" "\n"); do
  if [ -d "$dir" ] && [ -w "$dir" ]; then
    echo "    $dir"
  fi
done

echo "[+] Cron Jobs"
cat /etc/crontab 2>/dev/null

echo "[+] Active Connections"
netstat -tulpn 2>/dev/null || ss -tulpn 2>/dev/null

echo "[+] Enumeration complete."
