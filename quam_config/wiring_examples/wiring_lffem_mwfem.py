import matplotlib.pyplot as plt
from qualang_tools.wirer import Connectivity, Instruments, allocate_wiring, visualize
from qualang_tools.wirer.wirer.channel_specs import *
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import Quam

########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "127.0.0.1"  # QOP IP address
port = None  # QOP Port
cluster_name = "Cluster_1"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[1])
instruments.add_lf_fem(controller=1, slots=[2])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [1, 2, 3, 5]
# qubit_pairs = [(qubits[i], qubits[i + 1]) for i in range(len(qubits) - 1)]

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# multiplexed readout for qubits 1 to 4 and 5 to 8 on two feed-lines
res_ch = mw_fem_spec(con=1, slot=1, in_port=2, out_port=8)
# individual xy drive for qubits 1 to 4 on MW-FEM 1
drive1_ch = mw_fem_spec(con=1, slot=1, in_port=None, out_port=2)
drive2_ch = mw_fem_spec(con=1, slot=1, in_port=None, out_port=3)
drive3_ch = mw_fem_spec(con=1, slot=1, in_port=None, out_port=4)
drive5_ch = mw_fem_spec(con=1, slot=1, in_port=None, out_port=6)

flux1_ch = lf_fem_spec(con=1, out_slot=2, in_port=None, out_port=1)
flux2_ch = lf_fem_spec(con=1, out_slot=2, in_port=None, out_port=2)
flux3_ch = lf_fem_spec(con=1, out_slot=2, in_port=None, out_port=3)
flux5_ch = lf_fem_spec(con=1, out_slot=2, in_port=None, out_port=5)


########################################################################################################################
# %%                Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# The readout lines
connectivity.add_resonator_line(qubits=qubits, constraints=res_ch)
# The xy drive lines
connectivity.add_qubit_drive_lines(qubits=qubits[0], constraints=drive1_ch)
connectivity.add_qubit_drive_lines(qubits=qubits[1], constraints=drive2_ch)
connectivity.add_qubit_drive_lines(qubits=qubits[2], constraints=drive3_ch)
connectivity.add_qubit_drive_lines(qubits=qubits[3], constraints=drive5_ch)
# The flux lines for the individual qubits
connectivity.add_qubit_flux_lines(qubits=qubits[0], constraints=flux1_ch)
connectivity.add_qubit_flux_lines(qubits=qubits[1], constraints=flux2_ch)
connectivity.add_qubit_flux_lines(qubits=qubits[2], constraints=flux3_ch)
connectivity.add_qubit_flux_lines(qubits=qubits[3], constraints=flux5_ch)
# The flux lines for the tunable couplers
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=qubit_pairs)
# Allocate the wiring
allocate_wiring(connectivity, instruments)

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

# %%
