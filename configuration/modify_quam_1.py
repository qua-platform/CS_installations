# %%
import json
import argparse
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np


def get_band(frequency: float):
    u = unit(coerce_to_integer=True)
    # Define which quantum elements are present in the system
    # The keyword "band" refers to the following frequency bands:
    #   1: (50 MHz - 5.5 GHz)
    #   2: (4.5 GHz - 7.5 GHz)
    #   3: (6.5 GHz - 10.5 GHz)
    # The keyword "full_scale_power_dbm" is the maximum power of
    # normalized pulse waveforms in [-1,1]. To convert to voltage,
    #   power_mw = 10**(full_scale_power_dbm / 10)
    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
    #   amp_in_volts = waveform * max_voltage_amp
    #   ^ equivalent to OPX+ amp
    # Its range is -11dBm to +16dBm with 3dBm steps.

    ## Update qubit rr freq and power
    if frequency > 7.5 * u.GHz:
        return 3
    elif 5.5 * u.GHz < frequency <= 7.5 * u.GHz:
        return 2
    elif frequency <= 5.5 * u.GHz:
        return 1
    else:
        raise ValueError(f"The rr frequency {frequency} is outside the MW fem bandwidth [50MHz, 10.5GHz].")
    

def configure_machine(path: str = "./quam_state"):

    machine = QuAM.load()
    
    qubits = machine.active_qubits
    num_qubits = len(qubits)

    u = unit(coerce_to_integer=True)

    # Change active qubits
    # machine.active_qubit_names = ["q0"]

    # Update frequencies
    rr_freq = np.array([4.5] * num_qubits) * u.GHz
    rr_if = 50 * u.MHz
    rr_LO = rr_freq - rr_if
    rr_delays = [0] * num_qubits

    xy_freq_01 = np.array([4.5] * num_qubits) * u.GHz
    xy_freq_12 = np.array([4.3] * num_qubits) * u.GHz
    anaharmonicity = np.abs(xy_freq_12 - xy_freq_01)
    xy_if = 50 * u.MHz
    xy_LO = xy_freq_01 - xy_if
    xy_delays = [0] * num_qubits

    # Update qubit parameters
    T1 = np.array([30] * num_qubits) * 1e-6
    # grid_locations = ["0-2", "1-2", "2-2", "2-1", "2-0", "1-0", "0-0", "0-1"]
    # NOTE: be aware of coupled ports for bands
    for i, qb in enumerate(qubits):

        qb.resonator.opx_output.upconverter_frequency = round(rr_LO[i])
        qb.resonator.opx_output.band = get_band(rr_LO[i])
        qb.resonator.opx_output.delay = int(rr_delays[i])
        qb.resonator.opx_output.delay = 4 if qb.resonator.opx_output.controller_id == "con2" else 0
        print(qb.resonator.opx_output, qb.resonator.opx_output.delay)
        qb.resonator.opx_input.downconverter_frequency = round(rr_LO[i])
        qb.resonator.opx_input.band = get_band(rr_LO[i])
        qb.resonator.intermediate_frequency = rr_if
        if (qb.xy.opx_output.controller_id == qb.resonator.opx_output.controller_id) and (qb.xy.opx_output.fem_id == qb.resonator.opx_output.fem_id):
            qb.resonator.thread = qb.name
        else:
            qb.resonator.thread = qb.name + "_rr"
        ## Update qubit xy freq and power
        qb.xy.opx_output.upconverter_frequency = None # round(xy_LO[i])
        qb.xy.opx_output.upconverters = {
            1: {'frequency': 4.5e9},
            2: {'frequency': 4.8e9},
        }
        # qb.xy.opx_output.upconverters = {
        #     1: 4.5e9,
        #     2: 4.8e9,
        # }
        qb.xy.upconverter = 1
        qb.xy.opx_output.band = get_band(xy_LO[i])
        qb.xy.opx_output.delay = 4 if qb.xy.opx_output.controller_id == "con2" else 0
        print(qb.xy.opx_output, qb.xy.opx_output.delay)
        qb.xy.intermediate_frequency = xy_if
        qb.xy.opx_output.delay = int(xy_delays[i])
        qb.xy.thread = qb.name

        qb.anharmonicity = int(anaharmonicity[i])
        ## Update qubit xy detuned freq and power
        # qb.xy_detuned.frequency_converter_up.LO_frequency = round(xy_LO[i])
        # qb.xy_detuned.intermediate_frequency = qb.xy.intermediate_frequency + round(xy_if_detuning[i])
        # qb.xy_detuned.thread = qb.name

        # Qubit T1
        qb.T1 = T1[i]
        ## Update pulses
        # readout
        qb.resonator.opx_output.full_scale_power_dbm = 1
        qb.resonator.operations["readout"].length = 1000
        qb.resonator.operations["readout"].amplitude = 0.2
        # Qubit constant
        qb.xy.opx_output.full_scale_power_dbm = 1
        qb.xy.operations["saturation"].length = 40 * u.us
        qb.xy.operations["saturation"].amplitude = 0.25
        # Single qubit gates - DragCosine
        qb.xy.operations["x180_DragCosine"].length = 40
        qb.xy.operations["x180_DragCosine"].amplitude = 0.2
        qb.xy.operations["x90_DragCosine"].amplitude = qb.xy.operations["x180_DragCosine"].amplitude / 2
        # Single qubit gates - Square
        qb.xy.operations["x180_Square"].length = 40
        qb.xy.operations["x180_Square"].amplitude = 0.1
        qb.xy.operations["x90_Square"].amplitude = qb.xy.operations["x180_Square"].amplitude / 2

        # print(i, qb.xy.inferred_RF_frequency)

    from quam.components import pulses

    qubit_pairs = machine.active_qubit_pairs

    for i, qb_pair in enumerate(qubit_pairs):
        qbc = qb_pair.qubit_control
        qbt = qb_pair.qubit_target
        cr = qb_pair.cross_resonance
        # zz = qb_pair.zz_drive

        # CR gates - Square
        # cr.thread = qbc.name
        qbt.xy.operations[f"{cr.name}_Square"] = pulses.SquarePulse(amplitude=-0.25, length=100, axis_angle=0, digital_marker="ON")
        qbt.xy.operations[f"{cr.name}_Square"].amplitude = 0.1
        qbt.xy.operations[f"{cr.name}_Square"].length = f"#/qubit_pairs/{qb_pair.name}/cross_resonance/operations/square/length"
        qbt.xy.operations[f"{cr.name}_Square"].axis_angle = 0
        # cr.opx_output.upconverters = {int(1): round(xy_LO[i]), int(2): round(xy_LO[i]) + 100 * u.MHz} # round(xy_LO[i])
        cr.upconverter = 2 
        cr.intermediate_frequency = cr.inferred_intermediate_frequency
        cr.thread = qbc.name + "_cr"

        # print(i, cr.intermediate_frequency)

        # # ZZ gates - Square
        # zz.thread = qbc.name
        # zz.detuning = -15 * u.MHz
        # # qbt.xy_detuned.detuning = f"#/qubit_pairs/{qb_pair.name}/zz_drive/intermediate_frquencys"
        # qbt.xy_detuned.operations[f"{zz.name}_Square"] = pulses.SquarePulse(amplitude=-0.25, length=100, axis_angle=0, digital_marker="ON")
        # qbt.xy_detuned.operations[f"{zz.name}_Square"].amplitude = 0.1
        # qbt.xy_detuned.operations[f"{zz.name}_Square"].length = f"#/qubit_pairs/{qb_pair.name}/zz_drive/operations/square/length"
        # qbt.xy_detuned.operations[f"{zz.name}_Square"].axis_angle = 0
            

    # %%
    # save into state.json
    save_machine(machine, path)

    # %%
    # View the corresponding "raw-QUA" config
    with open("qua_config.json", "w+") as f:
        json.dump(machine.generate_config(), f, indent=4)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Configure the quantum machine.")
    # parser.add_argument("--num_qubits", type=int, default=60, help="Number of qubits to configure.")
    # args = parser.parse_args()

    configure_machine()