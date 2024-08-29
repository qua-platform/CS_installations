from pathlib import Path
from builder.quam import build_quam
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.components import QuAM

instruments = Instruments()
instruments.add_lf_fem(controller=1, slots=1)
instruments.add_mw_fem(controller=1, slots=2)

qubits = [1, 2, 3, 4, 5, 6]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits)
connectivity.add_qubit_drive_lines(qubits=qubits)
connectivity.add_qubit_flux_lines(qubits=qubits)

allocate_wiring(connectivity, instruments)

host_ip = "123.456.789.12"
cluster_name = "Cluster_1"
path = Path(".") / "quam_state"

quam = build_quam(
    connectivity=connectivity,
    host_ip=host_ip,
    cluster_name=cluster_name,
    quam_state_path=path
)

machine = QuAM.load(path)
machine.qubits["q1"].xy

visualize(connectivity.elements, available_channels=instruments.available_channels)
