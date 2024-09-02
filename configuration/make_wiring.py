from pathlib import Path

from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring

# Define static parameters
host_ip = "10.2.0.201"  # "172.16.33.107"  # "172.16.33.101"
cluster_name = "DGX_Cluster"  # "Beta_8"  # "Cluster_81"
path = Path(".") / "quam_state"


# Define the available instrument setup
instruments = Instruments()
instruments.add_opx_plus(controllers = [1])
instruments.add_octave(indices = 1)
# instruments.add_lf_fem(controller=1, slots=2)
# instruments.add_mw_fem(controller=1, slots=1)


# Define any custom/hardcoded channel addresses
q1_drive_ch = None
q1_res_ch = opx_iq_octave_spec(out_port_i=9, out_port_q=10, rf_out=1)

# Define which quantum elements are present in the system
qubits = [1]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits, triggered=True, constraints=q1_res_ch)
connectivity.add_qubit_drive_lines(qubits=qubits[0], triggered=True, constraints=q1_drive_ch)
# connectivity.add_qubit_drive_lines(qubits=qubits[1:], triggered=True)
connectivity.add_qubit_flux_lines(qubits=qubits)
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(1,2)])

# Allocate the wiring to the connectivity object based on the available instruments
allocate_wiring(connectivity, instruments)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)

# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)
