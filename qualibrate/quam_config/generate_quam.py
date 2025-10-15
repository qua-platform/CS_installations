"""
General purpose script to generate the wiring and the QUAM that corresponds to your experiment for the first time.
The workflow is as follows:
    - Copy the content of the wiring example corresponding to your architecture and paste it here.
    - Modify the statis parameters to match your network configuration.
    - Update the instrument setup section with the available hardware.
    - Define which qubit ids are present in the system.
    - Define any custom/hardcoded channel addresses.
    - Allocate the wiring to the connectivity object based on the available instruments.
    - Visualize and validate the resulting connectivity.
    - Build the wiring and QUAM.
    - Populate the generated quam with initial values by modifying and running populate_quam_xxx.py
"""
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
cluster_name = "CS_3"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1])


########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [1, 2, 3, 4, 5]

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# multiplexed readout for all qubits
res_ch = mw_fem_spec(con=1, slot=1, in_port=1, out_port=1)
# multiplexed xy drive for all qubits
qubits_ch = mw_fem_spec(con=1, slot=1, in_port=None, out_port=2)

########################################################################################################################
# %%                Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# The readout lines
connectivity.add_resonator_line(qubits=qubits, constraints=res_ch)

# The xy drive lines
for qubit in qubits:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=qubits_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)

allocate_wiring(connectivity, instruments)
# Allocate the wiring
# allocate_wiring(connectivity, instruments)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)
plt.show(block=False)

########################################################################################################################
# %%                                   Build the wiring and QUAM
########################################################################################################################
user_input = input("Do you want to save the updated QUAM? (y/n)")
if user_input.lower() == "y":
    machine = Quam()
    # Build the wiring (wiring.json) and initiate the QUAM
    build_quam_wiring(connectivity, host_ip, cluster_name, machine)

    # Reload QUAM, build the QUAM object and save the state as state.json
    machine = Quam.load()
    build_quam(machine)
