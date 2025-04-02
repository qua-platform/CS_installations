# %%
from qualang_tools.wirer import Connectivity, Instruments, allocate_wiring, visualize
from qualang_tools.wirer.wirer.channel_specs import *
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import QuAM

########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "172.16.33.115"  # QOP IP address
port = None  # QOP Port
cluster_name = "CS_3"  # Name of the cluster
calibration_db_path = None  # "/path/to/some/config/folder"

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[2])
instruments.add_lf_fem(controller=1, slots=[3])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [1, 2, 3, 4]
qubit_pairs = [(1, 3), (1, 4)]

########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
drive_lines = mw_fem_spec()
feedline = mw_fem_spec(in_port=1, out_port=1)

########################################################################################################################
# %%                Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()
# The readout lines
connectivity.add_resonator_line(qubits=qubits, constraints=feedline)
# The xy drive lines
connectivity.add_qubit_drive_lines(qubits=qubits, constraints=drive_lines)

# The flux lines for the individual qubits
connectivity.add_qubit_flux_lines(qubits=[1, 3, 4])
# Allocate the wiring
allocate_wiring(connectivity, instruments)

# View wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)


########################################################################################################################
# %%                                   Build the wiring and QuAM
########################################################################################################################
quam = QuAM()
# Build the wiring (wiring.json) and initiate the QuAM
build_quam_wiring(connectivity, host_ip, cluster_name, quam)
# Build the QuAM object and save the state as state.json
machine = QuAM.load()
quam = build_quam(machine, calibration_db_path)
