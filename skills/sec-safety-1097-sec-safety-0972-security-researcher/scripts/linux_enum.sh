#!/bin/bash
# Basic Linux privilege escalation enumeration
echo "--- User Info ---"
id
whoami
groups

echo -e "\n--- System Info ---"
uname -a
lsb_release -a 2>/dev/null | head -n 5

echo -e "\n--- Sudo Permissions ---"
sudo -l 2>/dev/null || echo "Cannot run sudo -l or password required"

echo -e "\n--- SUID Binaries ---"
find / -perm -4000 2>/dev/null | head -n 20

echo -e "\n--- Writable PATH Directories ---"
echo $PATH | tr ":" "\n" | while read dir; do [ -w "$dir" ] && echo "$dir is WRITABLE"; done
