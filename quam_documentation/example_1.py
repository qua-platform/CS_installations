from quam.components import BasicQuam, SingleChannel, pulses
from qm import qua

# Create a root-level QUAM instance
machine = BasicQuam()

# Add a qubit connected to an OPX output channel
qubit = SingleChannel(opx_output=("con1", 1))
machine.channels["qubit"] = qubit

# Add a Gaussian pulse to the channel
qubit.operations["gaussian"] = pulses.GaussianPulse(
    length=100,  # Pulse length in ns
    amplitude=0.5,  # Peak amplitude of Gaussian pulse
    sigma=20,  # Standard deviation of Guassian pulse
)

# Play the Gaussian pulse on the channel within a QUA program
with qua.program() as prog:
    qubit.play("gaussian")

# Generate the QUA configuration from QUAM
qua_configuration = machine.generate_config()

# from qm import QuantumMachinesManager
# qmm = QuantumMachinesManager(host_ip = "", cluster_name = "")
# qm = qmm.open_qm(qua_configuration)

# job = qm.execute(prog)
# res = job.result_handles
# res.fetch_results.get("...")
