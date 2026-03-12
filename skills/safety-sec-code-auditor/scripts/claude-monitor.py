#!/usr/bin/env python3
"""
Simple Claude Wrapper for Monitoring
Adapted from Omnara's Claude Wrapper V3

This script wraps the `claude` CLI command, intercepting stdout/stdin to log activity.
It uses PTY to maintain the interactive terminal experience.
"""

import argparse
import os
import pty
import select
import signal
import sys
import termios
import threading
import time
import tty
import shutil
from pathlib import Path

# Constants
LOG_DIR = Path.home() / ".opencode" / "logs"

def find_claude_cli():
    """Find Claude CLI binary"""
    if cli := shutil.which("claude"):
        return cli

    # Fallbacks
    locations = [
        Path.home() / ".npm-global/bin/claude",
        Path("/usr/local/bin/claude"),
        Path.home() / ".local/bin/claude",
    ]

    for path in locations:
        if path.exists() and path.is_file():
            return str(path)

    # Default to just 'claude' if not found, letting the shell resolve it or fail
    return "claude"

class ClaudeMonitorWrapper:
    def __init__(self, log_file_path=None):
        self.running = True
        self.child_pid = None
        self.master_fd = None
        self.original_tty_attrs = None

        # Setup logging
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        if not log_file_path:
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            log_file_path = LOG_DIR / f"session_{timestamp}.log"

        self.log_file = open(log_file_path, "wb")
        print(f"Logging session to: {log_file_path}")

    def run_claude_with_pty(self, claude_args):
        """Run Claude CLI in a PTY"""
        claude_path = find_claude_cli()
        cmd = [claude_path] + claude_args

        # Save terminal settings
        try:
            self.original_tty_attrs = termios.tcgetattr(sys.stdin)
        except Exception:
            self.original_tty_attrs = None

        # Get terminal size
        try:
            cols, rows = os.get_terminal_size()
        except Exception:
            cols, rows = 80, 24

        # Fork PTY
        self.child_pid, self.master_fd = pty.fork()

        if self.child_pid == 0:
            # Child process
            os.execvp(cmd[0], cmd)

        # Parent process
        if self.child_pid > 0:
            # Set window size
            try:
                import fcntl
                import struct
                TIOCSWINSZ = 0x5414 # Linux default
                if sys.platform == "darwin":
                    TIOCSWINSZ = 0x80087467
                winsize = struct.pack("HHHH", rows, cols, 0, 0)
                fcntl.ioctl(self.master_fd, TIOCSWINSZ, winsize)
            except Exception:
                pass

        try:
            if self.original_tty_attrs:
                tty.setraw(sys.stdin)

            while self.running:
                rlist, _, _ = select.select([sys.stdin, self.master_fd], [], [], 0.1)

                # Handle Output from Claude
                if self.master_fd in rlist:
                    try:
                        data = os.read(self.master_fd, 10240)
                        if data:
                            os.write(sys.stdout.fileno(), data)
                            sys.stdout.flush()
                            # Log output
                            self.log_file.write(b"[OUT] " + data + b"\n")
                        else:
                            self.running = False
                            break
                    except OSError:
                        self.running = False
                        break

                # Handle Input from User
                if sys.stdin in rlist:
                    try:
                        data = os.read(sys.stdin.fileno(), 1024)
                        if data:
                            os.write(self.master_fd, data)
                            # Log input
                            self.log_file.write(b"[IN] " + data + b"\n")
                    except OSError:
                        pass

        finally:
            if self.original_tty_attrs:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.original_tty_attrs)

            self.log_file.close()

            if self.child_pid:
                try:
                    os.kill(self.child_pid, signal.SIGTERM)
                    os.waitpid(self.child_pid, 0)
                except Exception:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Claude Monitor Wrapper")
    args, claude_args = parser.parse_known_args()

    wrapper = ClaudeMonitorWrapper()

    def signal_handler(sig, frame):
        wrapper.running = False

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGWINCH, lambda s, f: None) # Ignore resize for now

    try:
        wrapper.run_claude_with_pty(claude_args)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
