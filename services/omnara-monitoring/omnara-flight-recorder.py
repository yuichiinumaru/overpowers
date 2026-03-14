#!/usr/bin/env python3
"""
Omnara Flight Recorder - PTY-based CLI Session Monitor
Records all stdin/stdout activity for a given command.
"""

import argparse
import os
import pty
import select
import signal
import sys
import termios
import time
import tty
import fcntl
import struct
from pathlib import Path

# Constants
DEFAULT_LOG_ROOT = Path.home() / ".overpowers" / "logs" / "omnara"

class FlightRecorder:
    def __init__(self, command, log_path=None):
        self.command = command
        self.running = True
        self.child_pid = None
        self.master_fd = None
        self.original_tty_attrs = None
        
        # Setup logging
        if not log_path:
            DEFAULT_LOG_ROOT.mkdir(parents=True, exist_ok=True)
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            safe_cmd = command[0].split('/')[-1].replace(' ', '_')
            log_path = DEFAULT_LOG_ROOT / f"flight_{safe_cmd}_{timestamp}.log"
        
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.log_file = open(self.log_path, "wb")
        
        # Ensure log file has restrictive permissions
        try:
            os.chmod(self.log_path, 0o600)
        except Exception:
            pass

    def _set_pty_size(self):
        """Propagate current terminal size to the PTY"""
        if self.master_fd is None:
            return
        try:
            cols, rows = os.get_terminal_size()
            TIOCSWINSZ = getattr(termios, 'TIOCSWINSZ', 0x5414)
            winsize = struct.pack("HHHH", rows, cols, 0, 0)
            fcntl.ioctl(self.master_fd, TIOCSWINSZ, winsize)
        except Exception:
            pass

    def _handle_resize(self, sig, frame):
        self._set_pty_size()

    def log_entry(self, direction, data):
        """Write a tagged data entry to the log file"""
        timestamp = time.time()
        header = f"\n[{timestamp:.6f}] [{direction}] ".encode('utf-8')
        self.log_file.write(header + data)
        self.log_file.flush()

    def run(self):
        """Execute the command in a PTY and monitor it"""
        print(f"[*] Omnara Flight Recorder started.")
        print(f"[*] Recording command: {' '.join(self.command)}")
        print(f"[*] Flight log: {self.log_path}")
        print("-" * 40)

        # Save terminal settings
        try:
            self.original_tty_attrs = termios.tcgetattr(sys.stdin)
        except Exception:
            self.original_tty_attrs = None

        # Fork PTY
        self.child_pid, self.master_fd = pty.fork()

        if self.child_pid == 0:
            # Child process
            try:
                os.execvp(self.command[0], self.command)
            except Exception as e:
                print(f"Failed to execute command: {e}")
                sys.exit(1)

        # Parent process
        # Set initial size and handle future resizes
        self._set_pty_size()
        signal.signal(signal.SIGWINCH, self._handle_resize)

        try:
            if self.original_tty_attrs:
                tty.setraw(sys.stdin)

            while self.running:
                # Use select to wait for data from either stdin or the child process
                rlist, _, _ = select.select([sys.stdin, self.master_fd], [], [], 0.1)

                # Handle Output from Command
                if self.master_fd in rlist:
                    try:
                        data = os.read(self.master_fd, 16384)
                        if data:
                            os.write(sys.stdout.fileno(), data)
                            sys.stdout.flush()
                            self.log_entry("OUT", data)
                        else:
                            # End of stream
                            self.running = False
                    except OSError:
                        self.running = False

                # Handle Input from User
                if sys.stdin in rlist:
                    try:
                        data = os.read(sys.stdin.fileno(), 1024)
                        if data:
                            os.write(self.master_fd, data)
                            self.log_entry("IN ", data)
                    except OSError:
                        pass

        finally:
            # Restore terminal settings
            if self.original_tty_attrs:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.original_tty_attrs)

            self.log_file.close()
            print(f"\n[*] Flight Recorder finished. Log saved to: {self.log_path}")

            if self.child_pid:
                try:
                    # Give it a moment to exit gracefully, then kill if needed
                    _, status = os.waitpid(self.child_pid, os.WNOHANG)
                    if status == 0:
                        os.kill(self.child_pid, signal.SIGTERM)
                        os.waitpid(self.child_pid, 0)
                except Exception:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Omnara Flight Recorder")
    parser.add_argument("--log-path", help="Path to save the flight log")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to record")
    
    args = parser.parse_args()

    if not args.command:
        # Default to bash if no command provided
        command = ["/bin/bash"]
    else:
        command = args.command

    recorder = FlightRecorder(command, log_path=args.log_path)

    def sigint_handler(sig, frame):
        # We don't exit immediately on SIGINT because the child process 
        # might be handling it. We only exit if the child dies.
        pass

    signal.signal(signal.SIGINT, sigint_handler)

    try:
        recorder.run()
    except Exception as e:
        # Ensure terminal is restored even on error
        if recorder.original_tty_attrs:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, recorder.original_tty_attrs)
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
