# %%
import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import Quam

###################W#####################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "172.16.33.115"  # QOP IP address
port = None  # QOP Port
cluster_name = "CS_3"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_lf_fem(controller=1, slots=[5])
instruments.add_octave(indices=1)

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [
    1, 2, 3,
]


########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# common
con = 1
lffem1 = 5

# RR
rr_slots = [
    lffem1, lffem1, lffem1,
]
rr_iq_out_ports_i = [
    1, 1, 1,
]
rr_iq_out_ports_q = [
    2, 2, 2,
]
rr_iq_in_ports_i = [
    1, 1, 1,
]
rr_iq_in_ports_q = [
    2, 2, 2,
]
rr_octaves = [
    1, 1, 1,
]
rr_rf_out_ports = [
    1, 1, 1,
]
rr_rf_in_ports = [
    1, 1, 1,
]

assert len(rr_slots) == len(qubits)
assert len(rr_iq_out_ports_i) == len(qubits)
assert len(rr_iq_out_ports_q) == len(qubits)
assert len(rr_iq_in_ports_i) == len(qubits)
assert len(rr_iq_in_ports_q) == len(qubits)
assert len(rr_octaves) == len(qubits)
assert len(rr_rf_out_ports) == len(qubits)
assert len(rr_rf_in_ports) == len(qubits)

xy_slots = [
    lffem1, lffem1, lffem1,
]
xy_iq_out_ports_i = [
    3, 5, 7,
]
xy_iq_out_ports_q = [
    4, 6, 8,
]
xy_octaves = [
    1, 1, 1,
]
xy_rf_out_ports = [
    2, 3, 4,
]

assert len(xy_slots) == len(qubits)
assert len(xy_iq_out_ports_i) == len(qubits)
assert len(xy_iq_out_ports_q) == len(qubits)
assert len(xy_octaves) == len(qubits)
assert len(xy_rf_out_ports) == len(qubits)


########################################################################################################################
# %%                 Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# Single qubit individual drive and readout lines
for i, qb in enumerate(qubits):
    print(f"q{qb}, rr")
    connectivity.add_resonator_line(
        qubits=qb,
        constraints=lf_fem_iq_octave_spec(
            con=con,
            slot=rr_slots[i],
            in_port_i=rr_iq_in_ports_i[i],
            in_port_q=rr_iq_in_ports_q[i],
            out_port_i=rr_iq_out_ports_i[i],
            out_port_q=rr_iq_out_ports_q[i],
            octave_index=rr_octaves[i],
            rf_out=rr_rf_out_ports[i],
            rf_in=rr_rf_in_ports[i],
        ),
    )
    # Don't block the xy channels to connect the CR and ZZ drives to the same ports
    allocate_wiring(connectivity, instruments, block_used_channels=False)

    print(f"q{qb}, xy")
    connectivity.add_qubit_drive_lines(
        qubits=qb,
        constraints=lf_fem_iq_octave_spec(
            con=con,
            slot=xy_slots[i],
            out_port_i=xy_iq_out_ports_i[i],
            out_port_q=xy_iq_out_ports_q[i],
            octave_index=xy_octaves[i],
            rf_out=xy_rf_out_ports[i],
        ),
    )
    # Don't block the xy channels to connect the CR and ZZ drives to the same ports
    allocate_wiring(connectivity, instruments, block_used_channels=False)

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

script = "populate_quam_lffem_octave.py"
path_config = Path.cwd()
print(f"Running: {script}")
subprocess.run(["python", path_config / script], check=True)


# %%
