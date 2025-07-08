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
host_ip = "172.16.33.115"  # QOP IP address
port = None  # QOP Port
cluster_name = "CS_4"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1, 2])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [
    1, 2, 3,
]
qubit_idxes = {q: i for i, q in enumerate(qubits)}


########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
con = 1
rr_slots = [
    1, 1, 1,
]
rr_out_ports = [
    1, 1, 1,
]
rr_in_ports = [
    1, 1, 1,
]

assert len(rr_slots) == len(qubits)
assert len(rr_out_ports) == len(qubits)
assert len(rr_in_ports) == len(qubits)

xy_slots = [
    1, 1, 1,
]
xy_ports = [
    2, 3, 4,
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

script = "populate_quam_mwfems.py"
path_config = Path.cwd()
print(f"Running: {script}")
subprocess.run(["python", path_config / script], check=True)


# %%
