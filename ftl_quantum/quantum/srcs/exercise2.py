from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to the qubit (creates superposition)
qc.h(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Visualize the circuit
print(qc.draw('mpl'))

# Set up the simulator
simulator = Aer.get_backend('aer_simulator')

# Execute the circuit on the simulator with 500 shots
job = simulator.run(qc, shots=500)

# Get the results
result = job.result()

# Get the counts (measurement outcomes)
counts = result.get_counts(qc)

# Plot the histogram of the results
plot_histogram(counts)
