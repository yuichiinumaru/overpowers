#!/bin/bash
echo "--- Basic System Enumeration ---"
echo "[*] OS Release:"
cat /etc/os-release 2>/dev/null || cat /etc/*-release 2>/dev/null
echo ""
echo "[*] Kernel:"
uname -a
echo ""
echo "[*] Current User:"
id
echo ""
echo "[*] Sudo Privileges:"
sudo -l 2>/dev/null || echo "Cannot run sudo -l without password"
echo ""
echo "[*] SUID Binaries (First 10):"
find / -perm -4000 -type f 2>/dev/null | head -n 10
