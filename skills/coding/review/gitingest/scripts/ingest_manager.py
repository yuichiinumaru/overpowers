import subprocess
import os

class IngestManager:
    def __init__(self, url, output="digest.md", max_size=None, include_patterns=None, 
                 exclude_patterns=None, branch=None, token=None):
        self.url = url
        self.output = output
        self.max_size = max_size
        self.include_patterns = include_patterns or []
        self.exclude_patterns = exclude_patterns or []
        self.branch = branch
        self.token = token

    def run(self):
        """Executes gitingest via CLI."""
        cmd = ["gitingest", self.url]

        if self.output:
            cmd.extend(["-o", self.output])
        
        if self.max_size:
            cmd.extend(["--max-size", str(self.max_size)])

        for pattern in self.include_patterns:
            cmd.extend(["--include-pattern", pattern])

        for pattern in self.exclude_patterns:
            cmd.extend(["--exclude-pattern", pattern])

        if self.branch:
            cmd.extend(["--branch", self.branch])

        if self.token:
            cmd.extend(["--token", self.token])

        # Run the command
        # Run the command with a timeout to prevent indefinite hangs
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"Gitingest timed out after 60 seconds while processing {self.url}")

        if result.returncode != 0:
            raise RuntimeError(f"Gitingest failed: {result.stderr}")
        
        return result.stdout
