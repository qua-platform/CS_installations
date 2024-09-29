# %%
import json
# from pathlib import Path

# from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine

path = "quam_state"

machine = QuAM.load(path)

# u = unit(coerce_to_integer=True)

# Change active qubits
# machine.active_qubit_names = ["q0"]

# %%
resonators_dict = {
    "q0": {"LO": 6200000000, "IF": 5914243468-6200000000, "RF_gain": 0},
    "q1": {"LO": 6200000000, "IF": 6014269234-6200000000, "RF_gain": 0},
    "q2": {"LO": 6200000000, "IF": 5857408866-6200000000, "RF_gain": 0},
    "q3": {"LO": 6200000000, "IF": 6037730991-6200000000, "RF_gain": 0},
    "q4": {"LO": 6200000000, "IF": 5943264487-6200000000, "RF_gain": 0},
}

drive_dict = {
    "q0": {"LO": 4700000000, "IF": 5079483955.48066-4700000000, "RF_gain": 0},
    "q1": {"LO": 4700000000, "IF": 4432249612.1778145-4700000000, "RF_gain": 0},
    "q2": {"LO": 4700000000, "IF": 4462607180.192034-4700000000, "RF_gain": 0},
    "q3": {"LO": 4700000000, "IF": 4413807509.189671-4700000000, "RF_gain": 0},
    "q4": {"LO": 4700000000, "IF": 4361646145.139638-4700000000, "RF_gain": 0},
}

# for qubit in machine.active_qubits:
#     qubit.xy.frequency_converter_up.LO_frequency = 4.5 * u.GHz
#     qubit.xy.intermediate_frequency = 50 * u.MHz
#     qubit.resonator.frequency_converter_up.LO_frequency = \
#     qubit.resonator.frequency_converter_down.LO_frequency = 7.175 * u.GHz
#     qubit.resonator.operations["readout"].amplitude = 0.2
#
# machine.qubits["q0"].resonator.intermediate_frequency = -114 * u.MHz
# machine.qubits["q1"].resonator.intermediate_frequency = -23 * u.MHz
# machine.qubits["q2"].resonator.intermediate_frequency = 135 * u.MHz
#
# machine.qubits["q2"].xy.frequency_converter_up.LO_frequency = 4.5 * u.GHz



qubits = machine.active_qubits
for qubit in qubits:
    machine.qubits[qubit.name].resonator.frequency_converter_up.gain = resonators_dict[qubit.name]["RF_gain"]
    machine.qubits[qubit.name].resonator.frequency_converter_up.LO_frequency = resonators_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].resonator.frequency_converter_down.LO_frequency  = resonators_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].resonator.depletion_time = 2500
    machine.qubits[qubit.name].resonator.time_of_flight = 264
    machine.qubits[qubit.name].resonator.operations["readout"].length = 1024
    
    machine.qubits[qubit.name].resonator.intermediate_frequency = resonators_dict[qubit.name]["IF"]
    machine.qubits[qubit.name].xy.frequency_converter_up.gain = drive_dict[qubit.name]["RF_gain"]
    machine.qubits[qubit.name].xy.frequency_converter_up.LO_frequency = drive_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].xy.intermediate_frequency = drive_dict[qubit.name]["IF"]
    

# %%
# save into state.json
save_machine(machine, path)

# %%
# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)

# %%
