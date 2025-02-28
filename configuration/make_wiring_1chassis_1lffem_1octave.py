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
host_ip = "172.16.33.107"
cluster_name = "Cluster_1" 
# Desired location of wiring.json and state.json
# The folder must not contain other json files.
path = "/workspaces/HI_20250303_NobuKaneko/configuration/quam_state"

# Define the available instrument setup
instruments = Instruments()
instruments.add_lf_fem(controller=1, slots=[3])
instruments.add_octave(indices=[1])

# Define which qubit indices are present in the system
qubits_fem1 = [1, 2]
# Allocate the wiring to the connectivity object based on the available instruments
connectivity = Connectivity()

# Single feed-line for reading the resonators & individual qubit drive lines
# Define any custom/hardcoded channel addresses
q1_res_ch = octave_spec(index=1, rf_out=1, rf_in=1)
connectivity.add_resonator_line(qubits=qubits_fem1, constraints=q1_res_ch)
connectivity.add_qubit_drive_lines(qubits=[1], constraints=octave_spec(index=1, rf_out=2))
connectivity.add_qubit_drive_lines(qubits=[2], constraints=octave_spec(index=1, rf_out=3))

allocate_wiring(connectivity, instruments)

# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)

# %%