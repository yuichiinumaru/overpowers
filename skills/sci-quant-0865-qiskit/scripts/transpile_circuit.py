import argparse
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService

def main():
    parser = argparse.ArgumentParser(description='Transpile a circuit for a specific backend.')
    parser.add_argument('--backend', required=True, help='Name of the IBM Quantum backend')
    parser.add_argument('--opt-level', type=int, default=3, choices=[0, 1, 2, 3], help='Optimization level')

    args = parser.parse_args()

    try:
        service = QiskitRuntimeService()
        backend = service.backend(args.backend)
        
        # Example circuit
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        
        print(f"Transpiling circuit for {args.backend} at level {args.opt_level}...")
        qc_isa = transpile(qc, backend=backend, optimization_level=args.opt_level)
        print("Transpilation successful.")
        print(f"Depth: {qc_isa.depth()}")
        print(f"Gate counts: {qc_isa.count_ops()}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
