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
host_ip = "10.1.1.11"  # QOP IP address
port = None  # QOP Port
cluster_name = "carmel_arbel"  # Name of the cluster


########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1, 2, 3, 4])
instruments.add_lf_fem(controller=1, slots=[5, 6, 7, 8])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = ["C1", "C2"]
# Allocate the wiring to the connectivity object based on the available instruments
connectivity = Connectivity()

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
con = 1
rr_slots = [2, 2]
rr_out_ports = [1, 1]
rr_in_ports = [1, 1]

assert len(rr_slots) == len(qubits)
assert len(rr_out_ports) == len(qubits)
assert len(rr_in_ports) == len(qubits)

xy_slots = [2, 2]
xy_ports = [2, 3]

assert len(xy_slots) == len(qubits)
assert len(xy_ports) == len(qubits)

z_slots = [7, 7]
z_ports = [1, 2]

assert len(z_slots) == len(qubits)
assert len(z_ports) == len(qubits)


########################################################################################################################
# %%                 Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
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

    connectivity.add_qubit_flux_lines(
        qubits=qb,
        constraints=lf_fem_spec(con=con, out_slot=z_slots[i], out_port=z_ports[i]),
    )
    # Don't block the xy channels to connect the CR and ZZ drives to the same ports
    allocate_wiring(connectivity, instruments, block_used_channels=False)

# # Single feed-line for reading the resonators & individual qubit drive lines
# # Define any custom/hardcoded channel addresses
# q1_res_ch = mw_fem_spec(con=1, slot=2, in_port=1, out_port=1)
# connectivity.add_resonator_line(qubits=qubits, constraints=q1_res_ch)
# connectivity.add_qubit_flux_lines(qubits=qubits)
# connectivity.add_qubit_drive_lines(qubits=qubits)
# # connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(1,2)])  # Tunable coupler
# allocate_wiring(connectivity, instruments)

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

script = "populate_quam_lf_mw_fems.py"
path_config = Path.cwd()
print(f"Running: {script}")
subprocess.run(["python", path_config / script], check=True)


# %%
