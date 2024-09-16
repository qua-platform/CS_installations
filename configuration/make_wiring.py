# %%
from pathlib import Path

from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring

# Define static parameters
host_ip = "10.1.1.110" # "172.16.33.101"
cluster_name = "QC1"  # "Cluster_81"
path = r"C:\\Users\\tomdv\\Documents\\QCC_QUAM\\CS_installations\\configuration\\quam_state"


# Define the available instrument setup
instruments = Instruments()
instruments.add_opx_plus(controllers = [4,5])
instruments.add_octave(indices = 3)
# instruments.add_lf_fem(controller=1, slots=[3, 4, 5])
# instruments.add_mw_fem(controller=1, slots=[1, 2])


# Define any custom/hardcoded channel addresses
q_drive_chs = [
    opx_iq_octave_spec(con=5, out_port_i=7, out_port_q=8, rf_out=4),
    opx_iq_octave_spec(con=5, out_port_i=5, out_port_q=6, rf_out=3),
    opx_iq_octave_spec(con=5, out_port_i=3, out_port_q=4, rf_out=2),
    opx_iq_octave_spec(con=5, out_port_i=9, out_port_q=10, rf_out=5),
]
q_flux_chs = [
    opx_spec(con=4, out_port=6),
    opx_spec(con=4, out_port=7),
    opx_spec(con=4, out_port=8),
    opx_spec(con=4, out_port=9),
]
q1_res_ch = opx_iq_octave_spec(con=5)

# Define which quantum elements are present in the system
qubits = [1, 2, 3, 4]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits, constraints=q1_res_ch)
for i, drive_ch in enumerate(q_drive_chs):
    connectivity.add_qubit_drive_lines(qubits=qubits[i], constraints=drive_ch)
for i, flux_ch in enumerate(q_flux_chs):
    connectivity.add_qubit_flux_lines(qubits=qubits[i], constraints=flux_ch)
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
