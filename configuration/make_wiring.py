# %%

import json
from dataclasses import dataclass

@dataclass
class Port:
    con: str
    module: int
    ch_I: int
    ch_Q: int
    octave: int
    octave_ch: int

QUBIT_IDXES = [1, 2, 3, 4]
qubit_pairs = [
    [1, 2],
    [2, 3],
    [3, 4],
]
QUBIT_PAIRS = [pair for pair in qubit_pairs for pair in (pair, pair[::-1])]


def default_port_allocation():
    res_ports = [
        Port(con="con1", module=1, ch_I=1, ch_Q=2, octave=1, octave_ch=1),
        Port(con="con1", module=1, ch_I=1, ch_Q=2, octave=1, octave_ch=1),
        Port(con="con1", module=1, ch_I=1, ch_Q=2, octave=1, octave_ch=1),
        Port(con="con1", module=1, ch_I=1, ch_Q=2, octave=1, octave_ch=1),
    ]
    xy_ports = [
        Port(con="con1", module=1, ch_I=3, ch_Q=4, octave=1, octave_ch=2),
        Port(con="con1", module=1, ch_I=5, ch_Q=6, octave=1, octave_ch=3),
        Port(con="con1", module=1, ch_I=7, ch_Q=8, octave=1, octave_ch=4),
        Port(con="con1", module=1, ch_I=9, ch_Q=10, octave=1, octave_ch=5),
    ]
    return res_ports, xy_ports


def create_wiring(port_allocation) -> dict:
    """
    Create a wiring config tailored to the number of qubits.
    """
    wiring = {"qubits": {}, "qubit_pairs": []}

    # Generate example wiring by default
    res_ports, xy_ports = port_allocation

    num_qubits = len(port_allocation[0])
    for q, q_idx in enumerate(QUBIT_IDXES):
        wiring["qubits"][f"q{q_idx}"] = create_qubit_wiring_opx1000(
            xy_ports=xy_ports[q],
            res_ports=res_ports[q],
        )

    for qc_idx, qt_idx in QUBIT_PAIRS:
        qubit_pair_wiring = create_qubit_pair_wiring_opx1000(
            qc_idx=qc_idx,
            qt_idx=qt_idx,
        )
        wiring["qubit_pairs"].append(qubit_pair_wiring)

    return wiring


def create_qubit_wiring_opx1000(xy_ports, res_ports):
    xyp = xy_ports
    rp = res_ports

    # Note: The Q channel is set to the I channel plus one.
    return {
        "xy": {
            "opx_output_I": f"#/ports/analog_outputs/{xyp.con}/{xyp.module}/{xyp.ch_I}",
            "opx_output_Q": f"#/ports/analog_outputs/{xyp.con}/{xyp.module}/{xyp.ch_Q}",
            "digital_port": f"#/ports/digital_outputs/{xyp.con}/{xyp.module}/{xyp.ch_I}",
            "frequency_converter_up": f"#/octaves/octave{xyp.octave}/RF_outputs/{xyp.octave_ch}",
        },
        "resonator": {
            "opx_output_I": f"#/ports/analog_outputs/{rp.con}/{rp.module}/{rp.ch_I}",
            "opx_output_Q": f"#/ports/analog_outputs/{rp.con}/{rp.module}/{rp.ch_Q}",
            "opx_input_I": f"#/ports/analog_inputs/{rp.con}/{rp.module}/1",
            "opx_input_Q": f"#/ports/analog_inputs/{rp.con}/{rp.module}/2",
            "digital_port": f"#/ports/digital_outputs/{rp.con}/{rp.module}/{rp.ch_I}",
            "frequency_converter_up": "#/octaves/octave1/RF_outputs/1",
            "frequency_converter_down": "#/octaves/octave1/RF_inputs/1",
        },
    }


def create_qubit_pair_wiring_opx1000(qc_idx, qt_idx, con="con1"):
    return {
        "qubit_control": f"#/qubits/q{qc_idx}", # reference to f"q{qc_idx}"
        "qubit_target": f"#/qubits/q{qt_idx}", # reference to f"q{qt_idx}"
        "cr_control": {
            "opx_output_I": f"#/qubits/q{qc_idx}/xy/opx_output_I",
            "opx_output_Q": f"#/qubits/q{qc_idx}/xy/opx_output_Q",
            "digital_port": f"#/qubits/q{qc_idx}/xy/digital_port",
            "frequency_converter_up": f"#/qubits/q{qc_idx}/xy/frequency_converter_up",
        },
        "cr_target": {
            "opx_output_I": f"#/qubits/q{qc_idx}/xy/opx_output_I",
            "opx_output_Q": f"#/qubits/q{qc_idx}/xy/opx_output_Q",
            "digital_port": f"#/qubits/q{qc_idx}/xy/digital_port",
            "frequency_converter_up": f"#/qubits/q{qc_idx}/xy/frequency_converter_up",
        },
    }


# def create_qubit_wiring_opx_plus(xy_ports, res_ports, flux_ports):
#     res_module, res_i_ch_out, res_octave, res_octave_ch = res_ports
#     xy_module, xy_i_ch, xy_octave, xy_octave_ch = xy_ports
#     z_module, z_ch = flux_ports

#     # Note: The Q channel is set to the I channel plus one.
#     return {
#         "xy": {
#             "opx_output_I": f"#/ports/analog_outputs/{xy_module}/{xy_i_ch}",
#             "opx_output_Q": f"#/ports/analog_outputs/{xy_module}/{xy_i_ch+1}",
#             "digital_port": f"#/ports/digital_outputs/{xy_module}/{xy_i_ch}",
#             "frequency_converter_up": f"#/octaves/octave{xy_octave}/RF_outputs/{xy_octave_ch}",
#         },
#         "z": {"opx_output": f"#/ports/analog_outputs/{z_module}/{z_ch}"},
#         "resonator": {
#             "opx_output_I": f"#/ports/analog_outputs/{res_module}/{res_i_ch_out}",
#             "opx_output_Q": f"#/ports/analog_outputs/{res_module}/{res_i_ch_out+1}",
#             "opx_input_I": f"#/analog_inputs/{res_module}/1",
#             "opx_input_Q": f"#/analog_inputs/{res_module}/2",
#             "digital_port": f"#/ports/digital_outputs/{res_module}/{res_i_ch_out}",
#             "frequency_converter_up": "#/octaves/octave1/RF_outputs/1",
#             "frequency_converter_down": "#/octaves/octave1/RF_inputs/1",
#         },
#     }


# def create_qubit_pair_wiring_opx_plus(coupler_ports, qubit_control, qubit_target, con="con1"):
#     c_module, c_ch = coupler_ports

#     return {
#         "qubit_control": f"#/qubits/q{qc_idx}",  # reference to f"q{q_idx}"
#         "qubit_target": f"#/qubits/q{qt_idx}",  # reference to f"q{q_idx + 1}"
#         "coupler": {"opx_output": f"#/ports/analog_outputs/{c_module}/{c_ch}"},
#         "cr_control": {
#             "opx_output_I": f"#/qubits/q{qc_idx}/xy/opx_output_I",
#             "opx_output_Q": f"#/qubits/q{qc_idx}/xy/opx_output_Q",
#             "digital_port": f"#/qubits/q{qc_idx}/xy/digital_port",
#             "frequency_converter_up": f"#/qubits/q{qc_idx}/xy/frequency_converter_up",
#         },
#         "cr_target": {
#             "opx_output_I": f"#/qubits/q{qc_idx}/xy/opx_output_I",
#             "opx_output_Q": f"#/qubits/q{qc_idx}/xy/opx_output_Q",
#             "digital_port": f"#/qubits/q{qc_idx}/xy/digital_port",
#             "frequency_converter_up": f"#/qubits/q{qc_idx}/xy/frequency_converter_up",
#         },
#     }

# %%
