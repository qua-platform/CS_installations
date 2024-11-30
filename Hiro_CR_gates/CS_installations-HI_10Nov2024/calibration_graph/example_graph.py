from typing import List, Optional
from qualibrate import QualibrationLibrary, QualibrationGraph, GraphParameters
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator

library = QualibrationLibrary.get_active_library()

# Define graph target parameters
class Parameters(GraphParameters):
    qubits: Optional[List[str]] = None

# Create the QualibrationGraph
graph = QualibrationGraph(
    name="workflow1",  # Unique graph name
    parameters=Parameters(),  # Instantiate graph parameters
    nodes={  # Specify nodes used in the graph
        "qubit_spec": library.nodes["03a_Qubit_Spectroscopy"],
        "rabi": library.nodes["04b_Power_Rabi_with_Error_Amplification"],
        "ramsey": library.nodes["06a_Ramsey"],
    },
    # Specify directed relationships between graph nodes
    connectivity=[("qubit_spec", "rabi"), ("rabi", "ramsey")],
    # Specify orchestrator used to run the graph
    orchestrator=BasicOrchestrator(skip_failed=True),
)

# Run the calibration graph for qubits q1, q2, and q3
graph.run(qubits=["q1"])