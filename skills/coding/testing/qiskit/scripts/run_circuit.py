import argparse
import sys
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

def run_bell_state(shots=1024):
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    sampler = StatevectorSampler()
    job = sampler.run([qc], shots=shots)
    result = job.result()
    counts = result[0].data.meas.get_counts()
    return counts

def main():
    parser = argparse.ArgumentParser(description='Run a local Qiskit simulation.')
    parser.add_argument('--bell', action='store_true', help='Run a simple Bell state circuit')
    parser.add_argument('--shots', type=int, default=1024, help='Number of shots')

    args = parser.parse_args()

    if args.bell:
        print(f"Running Bell state simulation with {args.shots} shots...")
        counts = run_bell_state(args.shots)
        print("Results:", counts)
    else:
        print("Provide a circuit or use --bell for a demo.")

if __name__ == "__main__":
    main()
