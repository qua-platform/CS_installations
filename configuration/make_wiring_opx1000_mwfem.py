# %%
from qualang_tools.wirer import Connectivity, Instruments, allocate_wiring, visualize
from qualang_tools.wirer.wirer.channel_specs import mw_fem_spec
from qualang_tools.wirer.connectivity.element import QubitReference
from qualang_tools.wirer.connectivity.wiring_spec import WiringLineType
from quam_libs.quam_builder.machine import build_quam_wiring

# ----------------------------
# Configuration Parameters
# ----------------------------
qop_ip_address = "172.16.33.115"
qop_cluster_name = "CS_3"
output_directory = "./quam_state"

# ----------------------------
# Instrument Setup
# ----------------------------
instrument_setup = Instruments()
instrument_setup.add_mw_fem(controller=1, slots=[1])

# ----------------------------
# Qubit Setup
# ----------------------------
qubits = [1, 2, 3, 4, 5, 6, 7]
qubit_pairs = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7),
    # (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6),
]

# ----------------------------
# Connectivity Definition
# ----------------------------
connectivity = Connectivity()

# ----------------------------
# Readout Line Configuration
# ----------------------------
readoutline_qubits = {
    1: qubits
}
readoutline_channels = {
    1: mw_fem_spec(con=1, slot=1, in_port=1, out_port=1),
}

# ----------------------------
# Qubit Drive Configuration
# ----------------------------
qubit_drive_channels = {
    1: mw_fem_spec(con=1, slot=1, out_port=2),
    2: mw_fem_spec(con=1, slot=1, out_port=3),
    3: mw_fem_spec(con=1, slot=1, out_port=4),
    4: mw_fem_spec(con=1, slot=1, out_port=5),
    5: mw_fem_spec(con=1, slot=1, out_port=6),
    6: mw_fem_spec(con=1, slot=1, out_port=7),
    7: mw_fem_spec(con=1, slot=1, out_port=8),
}

# ----------------------------
# Assign Readout Wiring
# ----------------------------
for rl, qbs in readoutline_qubits.items():
    connectivity.add_resonator_line(qubits=qbs, constraints=readoutline_channels[rl])
    allocate_wiring(connectivity, instrument_setup)

# ----------------------------
# Assign Qubit Drive Wiring
# ----------------------------
for qubit, drive_channel in qubit_drive_channels.items():
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=drive_channel)
    allocate_wiring(connectivity, instrument_setup, block_used_channels=False)

# ----------------------------
# Assign Qubit Pair Wiring (CR and ZZ)
# ----------------------------
for qubit_control, qubit_target in qubit_pairs:
    control_drive_channel = connectivity.elements[QubitReference(index=qubit_control)].channels[WiringLineType.DRIVE][0]
    control_channel_constraint = mw_fem_spec(con=control_drive_channel.con, slot=control_drive_channel.slot, out_port=control_drive_channel.port)

    # Cross Resonance
    connectivity.add_qubit_pair_cross_resonance_lines(
        qubit_pairs=[(qubit_control, qubit_target)],
        constraints=control_channel_constraint,
    )
    allocate_wiring(connectivity, instrument_setup, block_used_channels=False)

    # # ZZ Drive
    # connectivity.add_qubit_pair_zz_drive_lines(
    #     qubit_pairs=[(qubit_control, qubit_target)],
    #     constraints=control_channel_constraint,
    # )
    # allocate_wiring(connectivity, instrument_setup, block_used_channels=False)

# ----------------------------
# Build QuAM Machine + Visualization
# ----------------------------
build_quam_wiring(connectivity, qop_ip_address, qop_cluster_name, output_directory)
visualize(connectivity.elements, available_channels=instrument_setup.available_channels)

# %%
