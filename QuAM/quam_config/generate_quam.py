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
########################################################################################################################
# %%                                             Import section
########################################################################################################################
import json
from qualang_tools.units import unit
from quam_config import Quam
from quam_builder.builder.superconducting.pulses import add_DragCosine_pulses
from quam.components.pulses import GaussianPulse, SquarePulse  # (+SquarePulse)
import numpy as np
import json
from pprint import pprint
import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam

########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "http://172.16.33.101/"  # QOP IP address
port = None  # QOP Port
cluster_name = "CS_1"  # Name of the cluster
calibration_db_path = "C:/Users/BenjaminSafvati/Customers/Mo_Chen"  

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_opx_plus(controllers=[1])
instruments.add_octave(indices=1)

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [1, 2, 3]
qubit_pairs = [(qubits[i], qubits[i + 1]) for i in range(len(qubits) - 1)]

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# multiplexed readout for qubits 1 to 3
q_res_ch = octave_spec(index=1, rf_out=1, rf_in=1)

########################################################################################################################
# %%                 Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# The readout line
connectivity.add_resonator_line(qubits=qubits, constraints=q_res_ch, triggered=True)
# The individual xy drive lines
connectivity.add_qubit_drive_lines(qubits=qubits, triggered=True)
# The flux lines for the individual qubits
connectivity.add_qubit_flux_lines(qubits=[1], constraints=opx_spec(con=1, out_port=10, in_port=None))  # AO10 to TLS1

### NEED TO MANUALLY EDIT AFTER RUNNING CODE ###
connectivity.add_qubit_flux_lines(qubits=[2], constraints=opx_spec(con=1, out_port=9,  in_port=None))  # Q2 & Q3 share AO9

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

