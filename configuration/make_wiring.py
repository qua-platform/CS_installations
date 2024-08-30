from pathlib import Path

from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from qualang_tools.wirer.wirer.channel_specs import opx_iq_spec, opx_iq_octave_spec
from quam_libs.quam_builder.machine import build_quam_wiring

# set static parameters
host_ip = "172.16.33.101"
cluster_name = "Cluster_1"
path = Path(".") / "quam_state"

##########################
# WIRING LF-FEM & MW-FEM #
##########################
# instruments = Instruments()
# instruments.add_lf_fem(controller=1, slots=2)
# instruments.add_mw_fem(controller=1, slots=1)
#
# qubits = [1, 2, 3, 4, 5, 6]
# connectivity = Connectivity()
# connectivity.add_resonator_line(qubits=qubits, triggered=True)
# connectivity.add_qubit_drive_lines(qubits=qubits, triggered=True)
# connectivity.add_qubit_flux_lines(qubits=qubits)
# connectivity.add_qubit_pair_flux_lines(qubit_pairs=[(2,5)])

########################
# WIRING OPX+ & Octave #
########################
instruments = Instruments()
instruments.add_opx_plus(controllers = [1])
instruments.add_octave(indices = 1)

qubits = [1, 2] #, 3, 4]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits, triggered=True)
connectivity.add_qubit_drive_lines(qubits=1, constraints=opx_iq_octave_spec(out_port_i=9, out_port_q=10, rf_out=5), triggered=True)
connectivity.add_qubit_drive_lines(qubits=2, triggered=True)
connectivity.add_qubit_flux_lines(qubits=qubits)

# build wiring
allocate_wiring(connectivity, instruments)
build_quam_wiring(connectivity, host_ip, cluster_name, path)

# view wiring schematic
visualize(connectivity.elements, available_channels=instruments.available_channels)
