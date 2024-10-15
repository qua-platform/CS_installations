import json

# mw_out = MWChannel(
#     id="mw_out",
#     operations={
#         "cw": SquarePulse(amplitude=1, length=100),
#         "readout": SquareReadoutPulse(amplitude=0.2, length=100),
#     },
#     opx_output=MWFEMAnalogOutputPort(
#         controller_id="con1", fem_id=1, port_id=2, band=1, upconverter_frequency=int(3e9), full_scale_power_dbm=-14
#     ),
#     upconverter=1,
#     intermediate_frequency=20e6,
# )
# mw_in = InOutMWChannel(
#     id="mw_in",
#     operations={
#         "readout": SquareReadoutPulse(amplitude=0.1, length=100),
#     },
#     opx_output=MWFEMAnalogOutputPort(
#         controller_id="con1", fem_id=1, port_id=1, band=1, upconverter_frequency=int(3e9), full_scale_power_dbm=-14
#     ),
#     opx_input=MWFEMAnalogInputPort(controller_id="con1", fem_id=1, port_id=1, band=1, downconverter_frequency=int(3e9)),
#     upconverter=1,
#     time_of_flight=28,
#     intermediate_frequency=10e6,
# )


def create_wiring(qubits, qubit_pairs, qubit_xy_port_map, resonator_port_map) -> dict:
    """
    Create a wiring config tailored to the number of qubits.
    """
    wiring = {"qubits": {}, "qubit_pairs": []}

    for q_idx in qubits:
        wiring["qubits"][f"q{q_idx}"] = create_qubit_wiring(
            xy_ports=qubit_xy_port_map[q_idx],
            res_ports=resonator_port_map[q_idx],
        )

    for q_idx in range(num_qubits - 1):
        qubit_pair_wiring = create_qubit_pair_wiring(
            coupler_ports=coupler_ports[q_idx],
            qubit_control=q_idx,
            qubit_target=q_idx + 1,
        )
        wiring["qubit_pairs"].append(qubit_pair_wiring)

    return wiring


def create_qubit_wiring(xy_port, res_port):
    con_xy, fem_xy, output_port_xy, _ = xy_port
    con_res, fem_res, output_port_res, input_port_res = res_port
    return {
        "xy": {
            "opx_output": f"#/ports/analog_outputs/{con_xy}/{fem_xy}/{output_port_xy}",
            "digital_port": f"#/ports/digital_outputs/{con_xy}/{fem_xy}/{output_port_xy}",
        },
        "resonator": {
            "opx_output": f"#/ports/analog_outputs/{con_res}/{fem_res}/{output_port_res}",
            "opx_input": f"#/ports/analog_inputs/{con_res}/{fem_res}/{input_port_res}",
            "digital_port": f"#/ports/digital_outputs/{con_res}/{fem_res}/{output_port_res}",
        },
    }


def create_qubit_pair_wiring(qubit_control, qubit_target):
    return {
        "qubit_control": f"#/qubits/q{qubit_control}",  # reference to f"q{q_idx}"
        "qubit_target": f"#/qubits/q{qubit_target}",  # reference to f"q{q_idx + 1}"
    }