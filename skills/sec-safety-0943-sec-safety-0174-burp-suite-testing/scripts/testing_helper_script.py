#!/usr/bin/env python3
import sys

def parse_burp(xml_report):
    print(f"Parsing Burp Suite XML report: {xml_report}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parse_burp(sys.argv[1])
    else:
        print("Usage: ./burp_parser.py <xml_report>")
