# %%
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from qualang_tools.wirer import Connectivity, Instruments, allocate_wiring, visualize
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer.connectivity.element import QubitReference
from qualang_tools.wirer.connectivity.wiring_spec import WiringLineType
from quam_libs.quam_builder.machine import build_quam_wiring


# Define static parameters
host_ip = "172.16.33.107"  # "172.16.33.101"
cluster_name = "Beta_8"  # "Cluster
# Desired location of wiring.json and state.json
# The folder must not contain other json files.
path = "./quam_state"

# Define the available instrument setup
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1, 2])
# instruments.add_mw_fem(controller=3, slots=[i + 1 for i in range(2)])

# Define which qubit indices are present in the system
qubits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Allocate the wiring to the connectivity object based on the available instruments
connectivity = Connectivity()

# Single feed-line for reading the resonators & individual qubit drive lines
# Define any custom/hardcoded channel addresses
q_res_chs = [
    [[ 1, 2, 3, 4], mw_fem_spec(con=1, slot=1, in_port=1, out_port=1)], # FEM1 - RL1
    [[ 5, 6, 7, 8], mw_fem_spec(con=1, slot=2, in_port=1, out_port=1)], # FEM2 - RL3
]

qb_chs = [
    [[1], mw_fem_spec(con=1, slot=1, out_port=2)],
    [[2], mw_fem_spec(con=1, slot=1, out_port=3)],
    [[3], mw_fem_spec(con=1, slot=1, out_port=4)],
    [[4], mw_fem_spec(con=1, slot=1, out_port=5)],
    [[5], mw_fem_spec(con=1, slot=2, out_port=2)],
    [[6], mw_fem_spec(con=1, slot=2, out_port=3)],
    [[7], mw_fem_spec(con=1, slot=2, out_port=4)],
    [[8], mw_fem_spec(con=1, slot=2, out_port=5)],
]

for qs, q_res_ch in q_res_chs:
    connectivity.add_resonator_line(qubits=qs, constraints=q_res_ch)
    allocate_wiring(connectivity, instruments)

for qs, qb_ch in qb_chs:
    connectivity.add_qubit_drive_lines(qubits=qs, constraints=qb_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)


qubit_pairs = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
]
qubit_pairs = qubit_pairs + [(qp[1], qp[0]) for qp in qubit_pairs]
# Allocate the wiring to the connectivity object based on the available instruments
for qp in qubit_pairs:
    qc_wires = connectivity.elements[QubitReference(index=qp[0])].channels[WiringLineType.DRIVE][0]
    print(f"qubit: {qp[0]}, con: {qc_wires.con}, slot: {qc_wires.slot}, out_port: {qc_wires.port}")
    qc_constraint = mw_fem_spec(con=qc_wires.con, slot=qc_wires.slot, out_port=qc_wires.port)
    # cross resonance
    connectivity.add_qubit_pair_cross_resonance_lines(qubit_pairs=[qp], constraints=qc_constraint)
    allocate_wiring(connectivity, instruments, block_used_channels=False)


# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)

# %%