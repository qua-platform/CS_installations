# %%
from qualang_tools.wirer.wirer.channel_specs import opx_iq_octave_spec
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_libs.quam_builder.machine import build_quam_wiring

# ----------------------------
# Configuration Parameters
# ----------------------------
qop_ip_address = "172.16.33.101"
qop_cluster_name = "CS_1"
output_directory = "./quam_state"  # Folder to save wiring.json and state.json (must be empty of other .json files)

# ----------------------------
# Instrument Setup
# ----------------------------
instrument_setup = Instruments()
instrument_setup.add_opx_plus(controllers=[1])
instrument_setup.add_octave(indices=[1])

# ----------------------------
# Qubit Setup
# ----------------------------
qubits = [1, 2, 3]
qubit_pairs = [
    (1, 2), (2, 3),
    (2, 1), (3, 2),
]

# ----------------------------
# Connectivity Definition
# ----------------------------
connectivity_graph = Connectivity()

# ----------------------------
# Readout Line Configuration
# ----------------------------
readout_line_to_qubits = {
    1: [1, 2, 3],  # Line 1 connects to qubits 1, 2, 3
}
readout_line_channels = {
    1: opx_iq_octave_spec(
        con=1,
        in_port_i=1,
        in_port_q=2,
        out_port_i=1,
        out_port_q=2,
        octave_index=1,
        rf_in=1,
        rf_out=1,
    ),
}

# ----------------------------
# Qubit Drive Configuration
# ----------------------------
qubit_drive_channels = {
    1: opx_iq_octave_spec(con=1, out_port_i=3, out_port_q=4, octave_index=1, rf_out=2),
    2: opx_iq_octave_spec(con=1, out_port_i=5, out_port_q=6, octave_index=1, rf_out=3),
    3: opx_iq_octave_spec(con=1, out_port_i=7, out_port_q=8, octave_index=1, rf_out=4),
}

# ----------------------------
# Assign Readout Wiring
# ----------------------------
for line_index, qubit_list in readout_line_to_qubits.items():
    readout_channel = readout_line_channels[line_index]
    connectivity_graph.add_resonator_line(qubits=qubit_list, constraints=readout_channel)
    allocate_wiring(connectivity_graph, instrument_setup)

# ----------------------------
# Assign Qubit Drive Wiring
# ----------------------------
for qubit, drive_channel in qubit_drive_channels.items():
    connectivity_graph.add_qubit_drive_lines(qubits=qubit, constraints=drive_channel)
    allocate_wiring(connectivity_graph, instrument_setup, block_used_channels=False)

# ----------------------------
# Assign Qubit Pair Wiring (CR and ZZ)
# ----------------------------
for qbc, qbt in qubit_pairs:
    constraint_channel = qubit_drive_channels[qbc]   # Cross Resonance
    connectivity_graph.add_qubit_pair_cross_resonance_lines(
        qubit_pairs=[(qbc, qbt)],
        constraints=constraint_channel,
    )
    allocate_wiring(connectivity_graph, instrument_setup, block_used_channels=False)

    # ZZ Drive
    connectivity_graph.add_qubit_pair_zz_drive_lines(
        qubit_pairs=[(qbc, qbt)],
        constraints=constraint_channel,
    )
    allocate_wiring(connectivity_graph, instrument_setup, block_used_channels=False)

# ----------------------------
# Build QuAM Machine + Visualization
# ----------------------------
build_quam_wiring(connectivity_graph, qop_ip_address, qop_cluster_name, output_directory)
visualize(connectivity_graph.elements, available_channels=instrument_setup.available_channels)

# %%
