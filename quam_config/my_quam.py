from quam_builder.architecture.superconducting.qpu import FixedFrequencyQuam, FluxTunableQuam


# Define the QUAM class that will be used in all calibration nodes
# Should inherit from either FixedFrequencyQuam or FluxTunableQuam
class Quam(FluxTunableQuam):
    pass


# Already has attributes to add qubits, qubit_pairs, etc... but ensure that any necessary additions are made

