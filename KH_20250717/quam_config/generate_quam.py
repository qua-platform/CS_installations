# %%
import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import Quam

########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "192.168.88.xxxxxxx"  # QOP IP address
port = None  # QOP Port
cluster_name = "xxxxxxxxxx"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1, 2, 3, 4, 5])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27,
]

qubit_idxes = {q: i for i, q in enumerate(qubits)}
qubit_pairs = [
    (1, 2), (2, 1),
    (2, 3), (3, 2),
    (3, 4), (4, 3),
    (4, 5), (5, 4),
    (5, 6), (6, 5),
    (6, 7), (7, 6),
    (7, 8), (8, 7),
    (8, 9), (9, 8),

    (9, 18), (18, 9),
    (10, 11), (11, 10),
    (11, 12), (12, 11),
    (12, 13), (13, 12),
    (13, 14), (14, 13),
    (14, 15), (15, 14),
    (15, 16), (16, 15),
    (16, 17), (17, 16),
    (17, 18), (18, 17),
    
    (10, 19), (19, 10),
    (19, 20), (20, 19),
    (20, 21), (21, 20),
    (21, 22), (22, 21),
    (22, 23), (23, 22),
    (23, 24), (24, 23),
    (24, 25), (25, 24),
    (25, 26), (26, 25),
    (26, 27), (27, 26),
]

# Flatten the pairs
flattened_qubits = {q for pair in qubit_pairs for q in pair}

# Check if all entries are in `qubits`
assert flattened_qubits.issubset(set(qubits))


########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
con = 1
rr_slots = [
    3, 3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 5, 5,
]
rr_out_ports = [
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
]
rr_in_ports = [
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
]

assert len(rr_slots) == len(qubits)
assert len(rr_out_ports) == len(qubits)
assert len(rr_in_ports) == len(qubits)

xy_slots = [
    3, 3, 3, 3, 3, 3, 3, 2, 2,
    4, 4, 4, 4, 2, 4, 4, 4, 2,
    5, 5, 5, 5, 5, 5, 5, 2, 2,
]
xy_ports = [
    2, 3, 4, 5, 6, 7, 8, 1, 2,
    2, 3, 4, 5, 6, 6, 7, 8, 3,
    2, 3, 4, 5, 6, 7, 8, 4, 5,
]

assert len(xy_slots) == len(qubits)
assert len(xy_ports) == len(qubits)


########################################################################################################################
# %%                 Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# Single qubit individual drive and readout lines
for i, qb in enumerate(qubits):
    connectivity.add_resonator_line(
        qubits=qb,
        constraints=mw_fem_spec(con=con, slot=rr_slots[i], in_port=rr_in_ports[i], out_port=rr_out_ports[i]),
    )
    # Don't block the xy channels to connect the CR and ZZ drives to the same ports
    allocate_wiring(connectivity, instruments, block_used_channels=False)

    connectivity.add_qubit_drive_lines(
        qubits=qb,
        constraints=mw_fem_spec(con=con, slot=xy_slots[i], out_port=xy_ports[i]),
    )
    # Don't block the xy channels to connect the CR and ZZ drives to the same ports
    allocate_wiring(connectivity, instruments, block_used_channels=False)

# Two-qubit drives
for (qc, qt) in qubit_pairs:
    idc, idt = qubit_idxes[qc], qubit_idxes[qt]

    # Add CR lines
    connectivity.add_qubit_pair_cross_resonance_lines(
        qubit_pairs=(qc, qt),
        constraints=mw_fem_spec(con=con, slot=xy_slots[idc], out_port=xy_ports[idc]),
    )
    allocate_wiring(connectivity, instruments, block_used_channels=False)

    # # Add ZZ lines
    # connectivity.add_qubit_pair_zz_drive_lines(
    #     qubit_pairs=qubit_pairs[i],
    #     constraints=mw_fem_spec(con=con, slot=xy_slots[idc], out_port=xy_ports[idc]),
    # )
    # allocate_wiring(connectivity, instruments, block_used_channels=False)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)
plt.show(block=True)

########################################################################################################################
# %%                                   Build the wiring and QUAM
########################################################################################################################

machine = Quam()
# Build the wiring (wiring.json) and initiate the QUAM
build_quam_wiring(connectivity, host_ip, cluster_name, machine)

# Reload QUAM, build the QUAM object and save the state as state.json
machine = Quam.load()
build_quam(machine)


########################################################################################################################
# %%                                   Populate QUAM
########################################################################################################################

from pathlib import Path
import subprocess

script = "populate_quam_mw_fems.py"
path_config = Path.cwd()
print(f"Running: {script}")
subprocess.run(["python", path_config / script], check=True)


# %%
