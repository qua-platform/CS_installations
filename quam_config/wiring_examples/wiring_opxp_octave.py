import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import Quam

########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "172.16.33.101"  # QOP IP address
port = None  # QOP Port
cluster_name = "CS_1"  # Name of the cluster
calibration_db_path = "/Users/paul/QM/CS_installations/quam_state"  # "/path/to/some/config/folder"

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_opx_plus(controllers=[1])
instruments.add_octave(indices=1)

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
# qubits = [5, 6, 7]
qubits = [5, 6]

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# multiplexed readout for all qubits
res_ch = octave_spec(index=1, rf_out=1, rf_in=1)
# individual qubit drive lines
q5_drive_ch = opx_iq_octave_spec(con=1, octave_index=1, rf_out=4, out_port_i=7, out_port_q=8)
q6_drive_ch = opx_iq_octave_spec(con=1, octave_index=1, rf_out=3, out_port_i=5, out_port_q=6)
# q7_drive_ch = opx_iq_octave_spec(con=1, octave_index=1, rf_out=2, out_port_i=3, out_port_q=4)

# flux lines if needed
q5_flux_ch = opx_spec(con=1, out_port=9)
q6_flux_ch = opx_spec(con=1, out_port=10)
# q7_flux_ch = opx_spec(con=1, out_port=9)

########################################################################################################################
# %%                 Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# The readout line
connectivity.add_resonator_line(qubits=qubits, constraints=res_ch)
# The individual xy drive lines
connectivity.add_qubit_drive_lines(qubits=qubits[0], constraints=q5_drive_ch)
connectivity.add_qubit_drive_lines(qubits=qubits[1], constraints=q6_drive_ch)
# connectivity.add_qubit_drive_lines(qubits=qubits[2], constraints=q7_drive_ch)
# # The flux lines for the individual qubits
connectivity.add_qubit_flux_lines(qubits=qubits[0], constraints=q5_flux_ch)
connectivity.add_qubit_flux_lines(qubits=qubits[1], constraints=q6_flux_ch)
# connectivity.add_qubit_flux_lines(qubits=qubits[2], constraints=q7_flux_ch)
# Allocate the wiring
allocate_wiring(connectivity, instruments)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)
plt.show(block=True)

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
    build_quam(machine, calibration_db_path)

# %%
