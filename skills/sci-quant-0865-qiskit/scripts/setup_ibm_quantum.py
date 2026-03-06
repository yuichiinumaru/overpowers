import argparse
from qiskit_ibm_runtime import QiskitRuntimeService

def main():
    parser = argparse.ArgumentParser(description='Save IBM Quantum account credentials.')
    parser.add_argument('--token', required=True, help='IBM Quantum API token')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing credentials')

    args = parser.parse_args()

    try:
        QiskitRuntimeService.save_account(channel="ibm_quantum", token=args.token, overwrite=args.overwrite)
        print("Successfully saved IBM Quantum account credentials.")
    except Exception as e:
        print(f"Error saving account: {e}")

if __name__ == "__main__":
    main()
