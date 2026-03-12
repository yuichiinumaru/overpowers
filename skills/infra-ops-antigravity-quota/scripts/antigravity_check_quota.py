#!/usr/bin/env python3

# Copyright (C) 2025 David Dallet
# Under permissive open source license known as "BSD 3-Clause License", see LICENSE file

import sys
import os
import re
import json
import time
import socket
import ssl
import subprocess
import urllib.request
import urllib.error
from typing import Optional, Tuple, List, Dict, Any

# --- Configuration ---
PROCESS_NAME_PATTERN = "language_server_linux"  # Matches language_server_linux_x64
ENDPOINT_PATH = "/exa.language_server_pb.LanguageServerService/GetUserStatus"
REQUEST_BODY = {
    "metadata": {
        "ideName": "antigravity",
        "extensionName": "antigravity",
        "locale": "en"
    }
}

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log(msg: str, color: str = ""):
    print(f"{color}{msg}{Colors.ENDC}")

def get_process_info() -> Optional[Tuple[int, str]]:
    """Finds the language server PID and CSRF token."""
    try:
        # Get all processes with full command line
        cmd = ["ps", "-eo", "pid,args"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        for line in result.stdout.splitlines():
            if PROCESS_NAME_PATTERN in line:
                # Extract PID
                parts = line.strip().split(maxsplit=1)
                if len(parts) < 2:
                    continue
                pid = int(parts[0])
                args = parts[1]

                # Extract CSRF token
                match = re.search(r'--csrf_token\s+([a-f0-9-]+)', args)
                if match:
                    return pid, match.group(1)
    except Exception as e:
        log(f"Error finding process: {e}", Colors.FAIL)
    return None

def get_listening_ports(pid: int) -> List[int]:
    """Finds listening TCP ports for a given PID using lsof."""
    ports = []
    try:
        # -a: AND selection, -P: no port names, -n: no host names, -iTCP: only TCP, -sTCP:LISTEN: only listening
        cmd = ["lsof", "-a", "-P", "-n", "-p", str(pid), "-iTCP", "-sTCP:LISTEN"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        # lsof returns 1 if no files found, which is fine
        if result.returncode != 0 and result.returncode != 1:
            return []

        for line in result.stdout.splitlines()[1:]: # Skip header
            parts = line.split()
            if len(parts) >= 9:
                # Address is usually the 9th column (index 8) like 127.0.0.1:12345
                address = parts[8]
                if ':' in address:
                    port_str = address.split(':')[-1]
                    try:
                        ports.append(int(port_str))
                    except ValueError:
                        pass
    except Exception as e:
        log(f"Error finding ports: {e}", Colors.FAIL)
    return ports

def check_quota(port: int, csrf_token: str) -> Optional[Dict[str, Any]]:
    """Attempts to fetch quota from a specific port."""
    url = f"https://127.0.0.1:{port}{ENDPOINT_PATH}"
    headers = {
        "Content-Type": "application/json",
        "Connect-Protocol-Version": "1",
        "X-Codeium-Csrf-Token": csrf_token
    }
    data = json.dumps(REQUEST_BODY).encode('utf-8')

    # Create a custom context to ignore self-signed certs
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=2) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except (urllib.error.URLError, socket.timeout, ConnectionRefusedError):
        return None
    except Exception:
        return None
    return None

def format_time_remaining(reset_time_str: str) -> str:
    if not reset_time_str:
        return "Unknown"
    try:
        # Simple parsing, assuming UTC ISO format like 2025-12-30T07:11:46Z
        # Removing Z for simple parsing if present
        ts_str = reset_time_str.replace('Z', '+00:00')
        # This requires python 3.7+
        from datetime import datetime, timezone
        reset_dt = datetime.fromisoformat(ts_str)
        now = datetime.now(timezone.utc)

        diff = reset_dt - now
        if diff.total_seconds() < 0:
            return "Ready"

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        parts = []
        if days > 0: parts.append(f"{days}d")
        if hours > 0: parts.append(f"{hours}h")
        parts.append(f"{minutes}m")
        return " ".join(parts)
    except:
        return reset_time_str

def main():
    log("🔍 Searching for Antigravity process...", Colors.BLUE)
    proc_info = get_process_info()

    if not proc_info:
        log("❌ Could not find running 'language_server' process.", Colors.FAIL)
        log("   Make sure VS Code with Antigravity is open.", Colors.WARNING)
        sys.exit(1)

    pid, token = proc_info
    log(f"✅ Found process (PID: {pid})", Colors.GREEN)

    log("🔍 Scanning ports...", Colors.BLUE)
    ports = get_listening_ports(pid)
    if not ports:
        log("❌ No listening ports found for the process.", Colors.FAIL)
        sys.exit(1)

    log(f"   Candidate ports: {ports}", Colors.CYAN)

    quota_data = None
    active_port = 0

    for port in ports:
        # print(f"   Testing port {port}...", end="\r")
        res = check_quota(port, token)
        if res:
            quota_data = res
            active_port = port
            break

    if not quota_data:
        log("❌ Could not connect to any port. The API might have changed.", Colors.FAIL)
        sys.exit(1)

    log(f"✅ Connected on port {active_port}\n", Colors.GREEN)

    # --- Display Results ---
    try:
        user_status = quota_data.get('userStatus', {})
        plan_info = user_status.get('planStatus', {}).get('planInfo', {})
        plan_status = user_status.get('planStatus', {})

        name = user_status.get('name', 'Unknown')
        email = user_status.get('email', 'Unknown')
        tier = plan_info.get('teamsTier', 'Unknown')

        print(f"{Colors.BOLD}User:{Colors.ENDC} {name} ({email})")
        print(f"{Colors.BOLD}Plan:{Colors.ENDC} {tier}\n")

        # Credits
        avail_prompt = plan_status.get('availablePromptCredits', 0)
        total_prompt = plan_info.get('monthlyPromptCredits', 0)
        avail_flow = plan_status.get('availableFlowCredits', 0)
        total_flow = plan_info.get('monthlyFlowCredits', 0)

        print(f"{Colors.HEADER}--- Credits ---{Colors.ENDC}")
        print(f"Prompt Credits: {Colors.BOLD}{avail_prompt:,}{Colors.ENDC} / {total_prompt:,}")
        print(f"Flow Credits:   {Colors.BOLD}{avail_flow:,}{Colors.ENDC} / {total_flow:,}")
        print("")

        # Models
        print(f"{Colors.HEADER}--- Model Quotas ---{Colors.ENDC}")
        models = user_status.get('cascadeModelConfigData', {}).get('clientModelConfigs', [])

        # Sort by remaining fraction (lowest first) to highlight exhausted ones
        models.sort(key=lambda x: x.get('quotaInfo', {}).get('remainingFraction', 1.0))

        print(f"{'Model Name':<35} {'Status':<15} {'Reset In':<15}")
        print("-" * 65)

        for model in models:
            label = model.get('label', 'Unknown')
            quota = model.get('quotaInfo', {})

            # If remainingFraction is missing but resetTime exists, it likely means 0% (exhausted)
            # Some APIs omit the field entirely when it is 0
            fraction = quota.get('remainingFraction')
            reset_time = quota.get('resetTime', '')

            if fraction is None:
                if reset_time:
                    fraction = 0.0
                else:
                    fraction = 1.0

            status_str = f"{int(fraction * 100)}%"
            color = Colors.GREEN
            if fraction < 0.01: # Effectively 0
                color = Colors.FAIL
            elif fraction < 0.2:
                color = Colors.WARNING
            elif fraction < 0.5:
                color = Colors.WARNING

            # Show reset time if fraction is less than 100% OR if there is a reset time present
            reset_str = format_time_remaining(reset_time) if (fraction < 1.0 or reset_time) else "-"

            print(f"{label:<35} {color}{status_str:<15}{Colors.ENDC} {reset_str:<15}")

    except Exception as e:
        log(f"Error parsing response: {e}", Colors.FAIL)
        print(json.dumps(quota_data, indent=2))

if __name__ == "__main__":
    main()
