from pathlib import Path

from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring
from qualang_tools.wirer.wirer.channel_specs import *

# 1. Define static parameters
host_ip = "172.16.33.107"  # "172.16.33.101"
cluster_name = "Cluster_1"
path = Path(".") / "quam_state"

# 2. Define the available instrument setup
instruments = Instruments()
instruments.add_lf_fem(controller=1, slots=2)
instruments.add_mw_fem(controller=1, slots=1)
# instruments.add_opx_plus(controllers = [1])
# instruments.add_octave(indices = 1)

# 3a. Define any custom/hardcoded channel addresses
q1_drive_ch = None  # will resort to automatic allocation
# q1_drive_ch = opx_iq_octave_spec(out_port_i=9, out_port_q=10, rf_out=5)

# 3b. Define which quantum elements are present in the system
connectivity = Connectivity()
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(1,2)])
connectivity.add_resonator_line(qubits=[1, 2], triggered=True)
connectivity.add_qubit_flux_lines(qubits=[1, 2])
connectivity.add_qubit_drive_lines(qubits=[1], triggered=True, constraints=q1_drive_ch)
connectivity.add_qubit_drive_lines(qubits=[2], triggered=True)

# 3c. View wiring schematic
# visualize(connectivity.elements, available_channels=instruments.available_channels)

# 4. Allocate the wiring to the connectivity object based on the available instruments
allocate_wiring(connectivity, instruments)

# Build the wiring and network into a QuAM machine and save it as "wiring.json"
build_quam_wiring(connectivity, host_ip, cluster_name, path)
