import cirq
import sys

def simulate_noise(noise_level=0.01):
    """
    Simulate a circuit with depolarizing noise.
    """
    qubits = cirq.LineQubit.range(2)
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),
        cirq.CNOT(qubits[0], qubits[1]),
        cirq.measure(*qubits, key='result')
    )
    
    # Apply noise
    noisy_circuit = circuit.with_noise(cirq.depolarize(p=noise_level))
    
    print(f"Noisy Circuit (depolarize={noise_level}):")
    print(noisy_circuit)
    
    # Simulate with density matrix simulator (handles mixed states/noise)
    simulator = cirq.DensityMatrixSimulator()
    result = simulator.run(noisy_circuit, repetitions=1000)
    print("\nNoisy Simulation Results (1000 repetitions):")
    print(result.histogram(key='result'))

if __name__ == "__main__":
    level = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01
    simulate_noise(level)
