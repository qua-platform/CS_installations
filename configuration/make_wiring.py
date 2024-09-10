# %%
from pathlib import Path

from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring

# Define static parameters
host_ip = "192.168.1.105"  # "172.16.33.101"
cluster_name = "Cluster_1"  # "Cluster_81"
path = r"C:\Users\daveh\Documents\Cloned Repos\CS_installations\configuration\quam_state"

# Define the available instrument setup
instruments = Instruments()
# instruments.add_opx_plus(controllers = [1])
# instruments.add_octave(indices = 1)
instruments.add_lf_fem(controller=1, slots=[2])
instruments.add_mw_fem(controller=1, slots=[1])

# Define any custom/hardcoded channel addresses
q1_drive_ch = mw_fem_spec(1, 1, None, 1)
q1_res_ch = mw_fem_spec(1, 1, 2, 8)  # mw_fem_spec(1, 1, 1, 2) 

# Define which quantum elements are present in the system
qubits = [1, 2, 3, 4, 5, 6]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits, constraints=q1_res_ch)
connectivity.add_qubit_flux_lines(qubits=qubits)
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(1,2)])

# Allocate the wiring to the connectivity object based on the available instruments
for qubit in qubits:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q1_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)

# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)

# %%
