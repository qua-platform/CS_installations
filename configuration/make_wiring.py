# %%
from pathlib import Path

from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring

# Define static parameters
host_ip = "qum.phys.sinica.edu.tw"  # "172.16.33.101"
cluster_name = "QPX_20q"  # "Cluster_81"
path = "quam_state"


# Define the available instrument setup
instruments = Instruments()
# instruments.add_opx_plus(controllers = [4,5])
instruments.add_octave(indices=[1,2,3])
instruments.add_lf_fem(controller=1, slots=[1, 2, 3])
# instruments.add_mw_fem(controller=1, slots=[1, 2])


# Define any custom/hardcoded channel addresses
# q_drive_chs = [
#     lf_fem_iq_octave_spec(con=1, slot=1, out_port_i=3, out_port_q=4, octave_index=1, rf_out=2),
#     lf_fem_iq_octave_spec(con=1, slot=1, out_port_i=5, out_port_q=6, octave_index=1, rf_out=3),
#     lf_fem_iq_octave_spec(con=1, slot=1, out_port_i=7, out_port_q=8, octave_index=1, rf_out=4),
#     lf_fem_iq_octave_spec(con=1, slot=2, out_port_i=1, out_port_q=2, octave_index=2, rf_out=1),
#     lf_fem_iq_octave_spec(con=1, slot=2, out_port_i=3, out_port_q=4, octave_index=2, rf_out=2),
# ]

# q_flux_chs = [
#     lf_fem_spec(con=1, out_slot=2, out_port=5),
#     lf_fem_spec(con=1, out_slot=2, out_port=6),
#     lf_fem_spec(con=1, out_slot=2, out_port=7),
#     lf_fem_spec(con=1, out_slot=2, out_port=8),
#     lf_fem_spec(con=1, out_slot=3, out_port=1),

# ]
# q1_res_ch = lf_fem_iq_octave_spec(
#     con=1, slot=1,
#     # out_port_i=1,
#     # out_port_q=2, octave_index=1, rf_out=1,
#     # in_port_i=1, in_port_q=2, rf_in=1
# ),

# coupler_res_ch = [
#     lf_fem_spec(con=1, out_slot=3, out_port=2),
#     lf_fem_spec(con=1, out_slot=3, out_port=3),
#     lf_fem_spec(con=1, out_slot=3, out_port=4),
#     lf_fem_spec(con=1, out_slot=3, out_port=5),
#
# ]

# Define which quantum elements are present in the system
qubits = [0, 1, 2, 3, 4]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits)
# for i, drive_ch in enumerate(q_drive_chs):
#     connectivity.add_qubit_drive_lines(qubits=qubits[i])
# for i, flux_ch in enumerate(q_flux_chs):
#     connectivity.add_qubit_flux_lines(qubits=qubits[i])
# for i, coupler_ch in enumerate(coupler_res_ch):
#     connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(qubits[i], qubits[i+1])])

# connectivity.add_qubit_drive_lines(qubits=qubits)
# connectivity.add_qubit_flux_lines(qubits=qubits)
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(1,2)])
# Allocate the wiring to the connectivity object based on the available instruments
for qubit in qubits:
    connectivity.add_qubit_drive_lines(qubits=qubit)
    connectivity.add_qubit_flux_lines(qubits=qubit)
for i in range(len(qubits)-1):
    connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(qubits[i], qubits[i + 1])])

allocate_wiring(connectivity, instruments, block_used_channels=False)

# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)

# %%
