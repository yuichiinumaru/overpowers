import cirq
import sys

def create_basic_circuit(num_qubits=2):
    """
    Create a basic Bell state circuit.
    """
    qubits = cirq.LineQubit.range(num_qubits)
    circuit = cirq.Circuit()
    
    # Add gates
    circuit.append(cirq.H(qubits[0])) # Hadamard gate
    circuit.append(cirq.CNOT(qubits[0], qubits[1])) # CNOT gate
    
    # Add measurements
    circuit.append(cirq.measure(*qubits, key='result'))
    
    print("Circuit:")
    print(circuit)
    
    # Simulate
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)
    print("\nSimulation Results (1000 repetitions):")
    print(result.histogram(key='result'))
    return circuit

if __name__ == "__main__":
    create_basic_circuit()
