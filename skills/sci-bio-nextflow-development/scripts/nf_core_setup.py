import argparse
import subprocess
import os
import sys

def check_dependencies():
    """Check if docker, nextflow, and java are installed."""
    print("Checking dependencies...")
    missing = []

    # Check Docker
    try:
        subprocess.run(["docker", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("✓ Docker is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Docker is NOT installed or not in PATH")
        missing.append("docker")

    # Check Nextflow
    try:
        subprocess.run(["nextflow", "-v"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("✓ Nextflow is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Nextflow is NOT installed or not in PATH")
        missing.append("nextflow")

    # Check Java
    try:
        subprocess.run(["java", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("✓ Java is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Java is NOT installed or not in PATH")
        missing.append("java")

    if missing:
        print(f"\nMissing dependencies: {', '.join(missing)}")
        return False
    return True

def run_test_profile(pipeline: str, outdir: str = "results"):
    """Run a nf-core pipeline with the test profile."""
    if not check_dependencies():
        print("Cannot run pipeline without dependencies.")
        return False

    cmd = [
        "nextflow", "run", f"nf-core/{pipeline}",
        "-profile", "test,docker",
        "--outdir", outdir
    ]

    print(f"\nRunning test profile for nf-core/{pipeline}...")
    print(f"Command: {' '.join(cmd)}")
    print("This may take some time to download containers and run the pipeline.")

    try:
        # Use subprocess.Popen to stream output
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end="")
        process.wait()

        if process.returncode == 0:
            print(f"\n✓ Pipeline test completed successfully.")
            print(f"Results saved to {outdir}")
            return True
        else:
            print(f"\n✗ Pipeline test failed with exit code {process.returncode}")
            return False
    except FileNotFoundError:
        print("Nextflow not found in PATH.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Helper script for nf-core pipelines")
    parser.add_argument("command", choices=["check", "test"], help="Command to run")
    parser.add_argument("--pipeline", help="Name of the nf-core pipeline to test (e.g. rnaseq, rnafusion)")
    parser.add_argument("--outdir", default="test_results", help="Output directory for test results")

    args = parser.parse_args()

    if args.command == "check":
        if check_dependencies():
            print("\nAll required dependencies are installed.")
        else:
            sys.exit(1)
    elif args.command == "test":
        if not args.pipeline:
            print("Error: --pipeline argument is required for the 'test' command.")
            sys.exit(1)
        if not run_test_profile(args.pipeline, args.outdir):
            sys.exit(1)
