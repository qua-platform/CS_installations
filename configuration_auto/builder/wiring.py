# todo: add a function for processing each line type --> delegate for each channel type
def create_qubit_wiring_opx1000(xy_ports, res_ports, flux_ports, con="con1"):
    return {
        "xy": {
            "opx_output_I": f"#/ports/analog_outputs/{con}/{xy_module}/{xy_i_ch}",
            "opx_output_Q": f"#/ports/analog_outputs/{con}/{xy_module}/{xy_i_ch+1}",
            "digital_port": f"#/ports/digital_outputs/{con}/{xy_module}/{xy_i_ch}",
            "frequency_converter_up": f"#/octaves/octave{xy_octave}/RF_outputs/{xy_octave_ch}",
        },
        "z": {"opx_output": f"#/ports/analog_outputs/{con}/{z_module}/{z_ch}"},
        "resonator": {
            "opx_output_I": f"#/ports/analog_outputs/{con}/{res_module}/{res_i_ch_out}",
            "opx_output_Q": f"#/ports/analog_outputs/{con}/{res_module}/{res_i_ch_out+1}",
            "opx_input_I": f"#/ports/analog_inputs/{con}/{res_module}/1",
            "opx_input_Q": f"#/ports/analog_inputs/{con}/{res_module}/2",
            "digital_port": f"#/ports/digital_outputs/{con}/{res_module}/{res_i_ch_out}",
            "frequency_converter_up": "#/octaves/octave1/RF_outputs/1",
            "frequency_converter_down": "#/octaves/octave1/RF_inputs/1",
        },
    }

def create_qubit_pair_wiring_opx1000(coupler_ports, qubit_control, qubit_target, con="con1"):
    c_module, c_ch = coupler_ports

    return {
        "qubit_control": f"#/qubits/q{qubit_control}",  # reference to f"q{q_idx}"
        "qubit_target": f"#/qubits/q{qubit_target}",  # reference to f"q{q_idx + 1}"
        "coupler": {"opx_output": f"#/ports/analog_outputs/{con}/{c_module}/{c_ch}"},
    }


def create_qubit_wiring_opx_plus(xy_ports, res_ports, flux_ports):
    res_module, res_i_ch_out, res_octave, res_octave_ch = res_ports
    xy_module, xy_i_ch, xy_octave, xy_octave_ch = xy_ports
    z_module, z_ch = flux_ports
    res_module = f"con{res_module}"
    xy_module = f"con{xy_module}"
    z_module = f"con{z_module}"
    # Note: The Q channel is set to the I channel plus one.
    return {
        "xy": {
            "opx_output_I": f"#/ports/analog_outputs/{xy_module}/{xy_i_ch}",
            "opx_output_Q": f"#/ports/analog_outputs/{xy_module}/{xy_i_ch+1}",
            "digital_port": f"#/ports/digital_outputs/{xy_module}/{xy_i_ch}",
            "frequency_converter_up": f"#/octaves/octave{xy_octave}/RF_outputs/{xy_octave_ch}",
        },
        "z": {"opx_output": f"#/ports/analog_outputs/{z_module}/{z_ch}"},
        "resonator": {
            "opx_output_I": f"#/ports/analog_outputs/{res_module}/{res_i_ch_out}",
            "opx_output_Q": f"#/ports/analog_outputs/{res_module}/{res_i_ch_out+1}",
            "opx_input_I": f"#/ports/analog_inputs/{res_module}/1",
            "opx_input_Q": f"#/ports/analog_inputs/{res_module}/2",
            "digital_port": f"#/ports/digital_outputs/{res_module}/{res_i_ch_out}",
            "frequency_converter_up": "#/octaves/octave1/RF_outputs/1",
            "frequency_converter_down": "#/octaves/octave1/RF_inputs/1",
        },
    }


def create_qubit_pair_wiring_opx_plus(coupler_ports, qubit_control, qubit_target, con="con1"):
    c_module, c_ch = coupler_ports

    return {
        "qubit_control": f"#/qubits/q{qubit_control}",  # reference to f"q{q_idx}"
        "qubit_target": f"#/qubits/q{qubit_target}",  # reference to f"q{q_idx + 1}"
        "coupler": {"opx_output": f"#/ports/analog_outputs/{c_module}/{c_ch}"},
    }
